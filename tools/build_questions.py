# -*- coding: utf-8 -*-
"""Merge per-exam raw JSON files into the Computability & Complexity dataset.

Inputs : tools/raw/<CODE>.json  (contract: tools/RAW_SCHEMA.md). Files whose name starts
         with "_" are skipped (fixtures / scratch).
Outputs: ../questions.json   { meta, contexts, questions }
         ../questions.js     window.CC_QUIZ = {...};
         build_report.md

Derived here (never in raw): id, examCode, examLabel, year, source, topicLabel, dedupKey,
auto-lockOrder, namespaced contextId, and the *Html fields (questionHtml, option html,
explanationHtml, context textHtml / captionHtml) with math pre-rendered to MathML.

Math: every $...$ / $$...$$ span (and every type:"math" option) is collected and rendered in
ONE call to tools/render_math.js (KaTeX, output:"mathml", dir="ltr" on every <math>). Any
KaTeX error, or Hebrew inside a math span, fails the build loudly and writes nothing.

Run:  PYTHONUTF8=1 py tools/build_questions.py
Prints ASCII only (the Windows console is cp1255); Hebrew goes to UTF-8 files.
"""
import collections, glob, hashlib, html, json, pathlib, re, subprocess, sys

TOOLS = pathlib.Path(__file__).resolve().parent
RAW = TOOLS / "raw"
OUT = TOOLS.parent

# Closed topic list -- keep in sync: build_questions.py, validate.py, app.js, build_learn.py
TOPIC_LABEL = {
    "tm": 'מכונות טיורינג, וריאנטים ומ"ט א"ד',
    "decidability": "כריעות וקבלה: R, RE, coRE",
    "enumerators": "אנומרטורים",
    "undecidability": "אי-כריעות: לכסון ובעיית העצירה",
    "mapping_reductions": "רדוקציות מיפוי (≤m)",
    "closure": "תכונות סגור",
    "classification": "סיווג שפות",
    "time_p": "סיבוכיות זמן והמחלקה P",
    "np": "המחלקה NP ו-coNP",
    "poly_reductions": "רדוקציות פולינומיות (≤p)",
    "npc": "NP-שלמות",
}
OPT_TYPES = {"text", "math", "image"}
CONFIDENCE = {"high", "med", "low"}
ANSWER_SOURCES = {"solution-pdf", "highlighted-pdf", "corrected-key", "letter-table",
                  "explanation-inferred"}

HEB = re.compile(r"[֐-׿]")
HEB_LETTER = "א-ת"

# An option that cites its SIBLINGS by printed letter ("תשובות א ו-ב נכונות", "א' ו-ג'",
# "רק ב,ג") must keep the printed order -- shuffling would point the reference at whatever
# landed in those slots. "כל התשובות האחרות" / "אף אחת מהתשובות" cite no letter: no lock.
_L = r"(?<![%s])[אבגדה]['׳]?(?![%s])" % (HEB_LETTER, HEB_LETTER)
LETTER_PAIR = re.compile(_L + r"\s*(?:,|\+|&|-|/|או|וגם|ו-?)\s*" +
                         r"[אבגדה]['׳]?(?![%s])" % HEB_LETTER)
LETTER_NAMED = re.compile(r"(?:תשובה|תשובות|סעיף|סעיפים|אפשרות|אפשרויות)\s+[אבגדה]['׳]?(?![%s])"
                          % HEB_LETTER)


def locks_order(options):
    for o in options:
        if (o.get("type") or "text") != "text":
            continue
        v = str(o.get("value", ""))
        if LETTER_PAIR.search(v) or LETTER_NAMED.search(v):
            return True
    return False


# ---------------------------------------------------------------- rich text
ESC_DOLLAR = "\x00"
TOKEN = re.compile(r"(\$\$.+?\$\$|\$[^$]+?\$|`[^`]+`)", re.S)


def split_rich(s):
    """Yield (kind, payload) for kind in text|imath|dmath|code. Literal \\$ -> '$'."""
    s = str(s).replace("\\$", ESC_DOLLAR)
    for part in TOKEN.split(s):
        if not part:
            continue
        if part.startswith("$$") and part.endswith("$$") and len(part) > 4:
            yield "dmath", part[2:-2].replace(ESC_DOLLAR, "\\$").strip()
        elif part.startswith("$") and part.endswith("$") and len(part) > 2:
            yield "imath", part[1:-1].replace(ESC_DOLLAR, "\\$").strip()
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            yield "code", part[1:-1].replace(ESC_DOLLAR, "$")
        else:
            yield "text", part.replace(ESC_DOLLAR, "$")


def math_spans(s):
    return [(p, k == "dmath") for k, p in split_rich(s) if k in ("imath", "dmath")]


class MathBank:
    """Collects (tex, display) pairs; renders them all in one node call."""

    def __init__(self):
        self.items, self.index, self.where = [], {}, []

    def add(self, tex, display, where):
        key = (tex, bool(display))
        if key not in self.index:
            self.index[key] = len(self.items)
            self.items.append({"tex": tex, "display": bool(display)})
            self.where.append(where)
        return self.index[key]

    def render(self):
        if not self.items:
            self.html = []
            return []
        proc = subprocess.run(["node", str(TOOLS / "render_math.js")],
                              input=json.dumps({"items": self.items}, ensure_ascii=False),
                              capture_output=True, text=True, encoding="utf-8", cwd=str(TOOLS))
        if proc.returncode != 0:
            sys.stdout.write("render_math.js failed:\n" +
                             proc.stderr.encode("ascii", "backslashreplace").decode() + "\n")
            sys.exit(2)
        res = json.loads(proc.stdout)
        self.html = [fix_overlines(h) if h else h for h in res["html"]]
        return [(self.where[e["i"]], e["tex"], e["err"]) for e in res["errors"]]


OVL_OPEN = '<mover accent="true">'
OVL_TAIL = '<mo stretchy="true">‾</mo></mover>'


def fix_overlines(m):
    r"""Chrome's MathML Core does not stretch KaTeX's \overline (<mover> + stretchy U+203E):
    it draws a short bar at the base's corner. Rewrite each one to <mrow class="ovl">BASE</mrow>;
    styles.css draws the bar as a border-top spanning the whole base. Innermost first."""
    starts, i = [], m.find(OVL_OPEN)
    while i != -1:
        starts.append(i)
        i = m.find(OVL_OPEN, i + 1)
    for st in reversed(starts):
        depth, j = 0, st
        while True:
            o, c = m.find("<mover", j), m.find("</mover>", j)
            if c == -1:
                return m
            if o != -1 and o < c:
                depth, j = depth + 1, o + 6
            else:
                depth, j = depth - 1, c + 8
                if depth == 0:
                    break
        seg = m[st:j]
        if seg.endswith(OVL_TAIL):
            base = seg[len(OVL_OPEN):-len(OVL_TAIL)]
            m = m[:st] + '<mrow class="ovl">' + base + "</mrow>" + m[j:]
    return m


def unescape_quotes(x):
    """Generators use Python raw strings, so a Hebrew gershayim written as \\" (מ\\"ט) arrives
    with its backslash. TeX here never uses \\" (umlaut), so strip it everywhere."""
    if isinstance(x, str):
        return x.replace('\\"', '"')
    if isinstance(x, list):
        return [unescape_quotes(v) for v in x]
    if isinstance(x, dict):
        return {k: unescape_quotes(v) for k, v in x.items()}
    return x


def rich_html(s, bank, where, math_errors):
    """Rich text -> HTML with MATH placeholders (@@M<n>@@) resolved later."""
    out = []
    for kind, p in split_rich(s):
        if kind in ("imath", "dmath"):
            if HEB.search(p):
                math_errors.append((where, p, "Hebrew inside math span"))
                continue
            i = bank.add(p, kind == "dmath", where)
            out.append(f"@@{'D' if kind == 'dmath' else 'M'}{i}@@")
        elif kind == "code":
            out.append(f'<code class="tok" dir="ltr">{html.escape(p, quote=False)}</code>')
        else:
            t = html.escape(p, quote=False)
            t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t, flags=re.S)
            out.append(t)
    h = "".join(out)
    # bold may wrap math/code placeholders too: re-run across the joined string
    h = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", h, flags=re.S)
    return h.replace("\r\n", "\n").replace("\n", "<br>")


def resolve(h, bank):
    def sub(m):
        kind, i = m.group(1), int(m.group(2))
        mm = bank.html[i]
        cls = "math-block" if kind == "D" else "math-inline"
        return f'<span class="{cls}">{mm}</span>'
    return re.sub(r"@@([MD])(\d+)@@", sub, h)


# ---------------------------------------------------------------- validation (light)
def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().lower()


def valid_question(q):
    errs = []
    opts = q.get("options") or []
    if not isinstance(q.get("num"), int):
        errs.append("bad-num")
    if len(opts) < 2:
        errs.append("few-options")
    ids = [o.get("id") for o in opts]
    if len(set(ids)) != len(ids):
        errs.append("dup-option-ids")
    for o in opts:
        if (o.get("type") or "text") not in OPT_TYPES:
            errs.append(f"bad-option-type:{o.get('type')}")
        if not str(o.get("value", "")).strip():
            errs.append(f"blank-option:{o.get('id')}")
        if o.get("type") == "image" and not (OUT / str(o.get("value", ""))).is_file():
            errs.append(f"option-image-missing:{o.get('id')}")
    if q.get("correctId") not in ids:
        errs.append("correctId-not-in-options")
    acc = q.get("acceptedIds")
    if acc is not None:
        if not isinstance(acc, list) or not acc:
            errs.append("bad-acceptedIds")
        else:
            if any(a not in ids for a in acc):
                errs.append("acceptedIds-unknown-id")
            if q.get("correctId") not in acc:
                errs.append("correctId-not-in-acceptedIds")
    if q.get("topic") not in TOPIC_LABEL:
        errs.append(f"bad-topic:{q.get('topic')}")
    if not str(q.get("question", "")).strip():
        errs.append("empty-question")
    if q.get("image") and not (OUT / q["image"]).is_file():
        errs.append("image-missing")
    if q.get("confidence") not in CONFIDENCE:
        errs.append(f"bad-confidence:{q.get('confidence')}")
    if not isinstance(q.get("official"), bool):
        errs.append("official-not-bool")
    return errs


def exam_order(code):
    m = re.match(r"^(\d{2})([ABS])-([ABC])$", code)
    if code.startswith("SAMP-"):
        return (0, 0, code)
    if m:
        return (1, int(m.group(1)), code)
    return (2, 0, code)


# ---------------------------------------------------------------- main
def main():
    raw_files = [p for p in sorted(RAW.glob("*.json")) if not p.name.startswith("_")]
    bank = MathBank()
    math_errors = []
    contexts, questions, problems = {}, [], []
    excl = collections.Counter()
    held = []
    exams_meta = []

    for fp in raw_files:
        try:
            data = unescape_quotes(json.loads(fp.read_text(encoding="utf-8")))
        except Exception as e:
            print(f"FATAL: {fp.name}: JSON parse error: {str(e).encode('ascii', 'backslashreplace').decode()}")
            sys.exit(1)
        code = data.get("examCode") or fp.stem
        if code != fp.stem:
            problems.append(f"{fp.name}: examCode {code} != file name")
        label = data.get("examLabel", code)
        year = data.get("year")
        source = "sample" if code.startswith("SAMP-") else "exam"
        exams_meta.append({"examCode": code, "examLabel": label, "year": year, "source": source,
                           "examDate": data.get("examDate")})

        cmap = {}
        for cid, ctx in (data.get("contexts") or {}).items():
            gid = f"{code}-{cid}"
            c = dict(ctx)
            c["id"] = gid
            where = f"{code} ctx {cid}"
            if c.get("kind") not in ("image", "text"):
                problems.append(f"{where}: bad kind {c.get('kind')}")
            if c.get("image") and not (OUT / c["image"]).is_file():
                problems.append(f"{where}: image missing {c['image']}")
            if c.get("text"):
                c["textHtml"] = rich_html(c["text"], bank, where, math_errors)
            if c.get("caption"):
                c["captionHtml"] = rich_html(c["caption"], bank, where + " caption", math_errors)
            if c.get("title"):
                c["titleHtml"] = rich_html(c["title"], bank, where + " title", math_errors)
            contexts[gid] = c
            cmap[cid] = gid

        nums = set()
        for q in data.get("questions", []):
            tag = f"{code} Q{q.get('num')}"
            errs = valid_question(q)
            if q.get("num") in nums:
                errs.append("dup-num")
            nums.add(q.get("num"))
            if q.get("contextId") and q["contextId"] not in cmap:
                errs.append("contextId-undefined")
            if errs:
                excl["+".join(e.split(":")[0] for e in errs)] += 1
                problems.append(f"{tag}: {', '.join(errs)}")
                continue
            if q.get("hold"):
                # disputed / unverified: kept in raw, listed in the report, NOT in the bank
                held.append(f"{tag}: {q['hold']}")
                continue
            q = dict(q)
            q["id"] = f"{code}-Q{q['num']}"
            q["examCode"], q["examLabel"], q["year"], q["source"] = code, label, year, source
            q["topicLabel"] = TOPIC_LABEL[q["topic"]]
            if q.get("contextId"):
                q["contextId"] = cmap[q["contextId"]]
            if "lockOrder" not in q and locks_order(q["options"]):
                q["lockOrder"] = True
            if q.get("lockOrder") is False:
                q.pop("lockOrder")
            q["questionHtml"] = rich_html(q["question"], bank, tag, math_errors)
            q["explanationHtml"] = rich_html(q.get("explanation") or "", bank, tag + " expl", math_errors)
            q["explanation"] = q.get("explanation") or ""
            opts = []
            for o in q["options"]:
                o = dict(o)
                o["type"] = o.get("type") or "text"
                w = f"{tag} opt {o['id']}"
                if o["type"] == "math":
                    tex = str(o["value"]).strip()
                    if HEB.search(tex):
                        math_errors.append((w, tex, "Hebrew inside math option"))
                        o["html"] = ""
                    else:
                        o["html"] = f"@@M{bank.add(tex, False, w)}@@"
                elif o["type"] == "image":
                    o["html"] = f'<img class="opt-img" src="{html.escape(str(o["value"]))}" alt="" loading="lazy">'
                else:
                    o["html"] = rich_html(o["value"], bank, w, math_errors)
                opts.append(o)
            q["options"] = opts
            key = norm(q["question"]) + " || " + "|".join(sorted(norm(o["value"]) for o in opts))
            q["dedupKey"] = hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]
            questions.append(q)

    # ---- render all math in one node call
    math_errors += bank.render()
    if math_errors:
        print(f"MATH ERRORS ({len(math_errors)}) -- nothing written:")
        for where, tex, err in math_errors:
            line = f"  - {where}: ${tex}$ -> {err}"
            print(line.encode("ascii", "backslashreplace").decode())
        sys.exit(1)

    for c in contexts.values():
        for k in ("textHtml", "captionHtml", "titleHtml"):
            if k in c:
                c[k] = resolve(c[k], bank)
    for q in questions:
        q["questionHtml"] = resolve(q["questionHtml"], bank)
        q["explanationHtml"] = resolve(q["explanationHtml"], bank)
        for o in q["options"]:
            o["html"] = resolve(o["html"], bank)
            if o["type"] == "math":
                o["html"] = o["html"].replace('class="math-inline"', 'class="math-inline opt-math"')

    questions.sort(key=lambda q: (exam_order(q["examCode"]), q["num"]))
    exams_meta.sort(key=lambda e: exam_order(e["examCode"]))

    dup_groups = collections.Counter(q["dedupKey"] for q in questions)
    dup = sum(n - 1 for n in dup_groups.values() if n > 1)

    payload_obj = {
        "meta": {
            "generated": "tools/build_questions.py",
            "exams": exams_meta,
            "topics": [{"key": k, "label": v} for k, v in TOPIC_LABEL.items()],
            "counts": {"total": len(questions), "unique": len(dup_groups),
                       "contexts": len(contexts), "math": len(bank.items)},
        },
        "contexts": contexts,
        "questions": questions,
    }
    payload = json.dumps(payload_obj, ensure_ascii=False, indent=1)
    (OUT / "questions.json").write_text(payload + "\n", encoding="utf-8")
    (OUT / "questions.js").write_text("window.CC_QUIZ = " + payload + ";\n", encoding="utf-8")

    by_topic = collections.Counter(q["topic"] for q in questions)
    by_exam = collections.Counter(q["examCode"] for q in questions)
    by_source = collections.Counter(q["source"] for q in questions)
    by_conf = collections.Counter(q["confidence"] for q in questions)
    by_off = collections.Counter("official" if q["official"] else "unofficial" for q in questions)
    by_ans = collections.Counter(q.get("answerSource") or "-" for q in questions)
    locked = sum(1 for q in questions if q.get("lockOrder"))
    multi = sum(1 for q in questions if q.get("acceptedIds"))

    L = ["# Build report — Computability & Complexity questions", "",
         f"- Raw exam files: **{len(raw_files)}**",
         f"- **Final questions: {len(questions)}** (unique by dedupKey: {len(dup_groups)}, duplicates kept: {dup})",
         f"- Excluded: **{sum(excl.values())}** {dict(excl) if excl else ''}",
         f"- Shared context blocks: **{len(contexts)}**",
         f"- Math spans rendered (distinct): **{len(bank.items)}**",
         f"- lockOrder: {locked} · multiple accepted answers: {multi}", "",
         f"- **On hold (not in bank, see docs/ASK_ADIR.md): {len(held)}**", ""] + [f"  - {h}" for h in held] + ["",
         "## By topic", "", "| topic | label | n |", "|---|---|---|"]
    for k, v in TOPIC_LABEL.items():
        L.append(f"| `{k}` | {v} | {by_topic.get(k, 0)} |")
    L += ["", "## By exam", ""]
    for code in sorted(by_exam, key=exam_order):
        L.append(f"- {code}: {by_exam[code]}")
    L += ["", "## By source", ""] + [f"- {k}: {v}" for k, v in sorted(by_source.items())]
    L += ["", "## By confidence", ""] + [f"- {k}: {by_conf.get(k, 0)}" for k in ("high", "med", "low")]
    L += ["", "## Official vs unofficial", ""] + [f"- {k}: {by_off.get(k, 0)}" for k in ("official", "unofficial")]
    L += ["", "## By answerSource", ""] + [f"- {k}: {v}" for k, v in sorted(by_ans.items())]
    if problems:
        L += ["", "## Excluded / problems", ""] + [f"- {p}" for p in problems]
    (TOOLS / "build_report.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"files={len(raw_files)} final={len(questions)} unique={len(dup_groups)} "
          f"excluded={sum(excl.values())} contexts={len(contexts)} math={len(bank.items)} locked={locked}")
    print("by_topic:", dict(by_topic))
    if problems:
        print(f"PROBLEMS ({len(problems)}):")
        for p in problems:
            print("  -", p.encode("ascii", "backslashreplace").decode())
        sys.exit(1 if excl else 0)


if __name__ == "__main__":
    main()
