# -*- coding: utf-8 -*-
"""Lint tools/raw/*.json against tools/RAW_SCHEMA.md. Run before build_questions.py.

    PYTHONUTF8=1 py tools/validate.py            # all raw files (skips names starting "_")
    PYTHONUTF8=1 py tools/validate.py 26B-B      # just one exam code (or a path)

Exit code 1 if any PROBLEM is found. Prints ASCII only.
"""
import json, pathlib, re, sys, collections

TOOLS = pathlib.Path(__file__).resolve().parent
RAW = TOOLS / "raw"
ROOT = TOOLS.parent

# Closed topic list -- keep in sync: build_questions.py, validate.py, app.js, build_learn.py
TOPICS = {"tm", "decidability", "enumerators", "undecidability", "mapping_reductions",
          "closure", "classification", "time_p", "np", "poly_reductions", "npc"}
OPT_TYPES = {"text", "math", "image"}
OPT_IDS = {"a", "b", "c", "d", "e", "f"}
CONFIDENCE = {"high", "med", "low"}
ANSWER_SOURCES = {"solution-pdf", "highlighted-pdf", "corrected-key", "letter-table",
                  "explanation-inferred", "solved"}
DERIVED = {"id", "examCode", "examLabel", "year", "source", "topicLabel", "dedupKey",
           "questionHtml", "explanationHtml"}
CODE_RE = re.compile(r"^(\d{2}[ABS]-[ABC]|SAMP-\d+)$")
HEB = re.compile(r"[֐-׿]")
TOKEN = re.compile(r"(\$\$.+?\$\$|\$[^$]+?\$|`[^`]+`)", re.S)


def rich_problems(s, where):
    """Balanced $, no Hebrew inside math. Returns a list of problem strings."""
    out = []
    s = str(s).replace("\\$", "")
    for part in TOKEN.split(s):
        if part.startswith("$$") and part.endswith("$$") and len(part) > 4:
            tex = part[2:-2]
        elif part.startswith("$") and part.endswith("$") and len(part) > 2:
            tex = part[1:-1]
        elif part.startswith("`"):
            continue
        else:
            if "$" in part:
                out.append(f"{where}: unbalanced $ (use \\$ for a literal dollar)")
            continue
        if HEB.search(tex):
            out.append(f"{where}: Hebrew inside math ${tex}$".encode("ascii", "backslashreplace").decode())
        if not tex.strip():
            out.append(f"{where}: empty math span")
    return out


def check_file(fp):
    problems, warns = [], []
    try:
        data = json.loads(fp.read_text(encoding="utf-8"))
    except Exception as e:
        return [f"{fp.name}: JSON parse error: {e}"], [], 0, collections.Counter()
    code = data.get("examCode")
    P = problems.append
    if not code:
        P(f"{fp.name}: missing examCode")
        code = fp.stem
    elif not CODE_RE.match(code):
        warns.append(f"{fp.name}: examCode {code} not YY[A|B|S]-[A|B|C] or SAMP-N")
    if code != fp.stem:
        P(f"{fp.name}: examCode {code} != file name")
    for k in ("examLabel", "year"):
        if data.get(k) in (None, ""):
            P(f"{code}: missing {k}")
    ctxs = data.get("contexts") or {}
    for cid, c in ctxs.items():
        w = f"{code} ctx {cid}"
        if c.get("kind") not in ("image", "text"):
            P(f"{w}: kind must be image|text")
        if c.get("kind") == "image":
            if not c.get("image"):
                P(f"{w}: image context without image")
            elif not (ROOT / c["image"]).is_file():
                P(f"{w}: image file missing {c['image']}")
        if c.get("kind") == "text" and not str(c.get("text", "")).strip():
            P(f"{w}: text context without text")
        for k in ("text", "caption", "title"):
            if c.get(k):
                problems += rich_problems(c[k], f"{w} {k}")
    qs = data.get("questions")
    if not isinstance(qs, list) or not qs:
        P(f"{code}: no questions")
        qs = []
    nums, by_topic = set(), collections.Counter()
    for q in qs:
        tag = f"{code} Q{q.get('num')}"
        for k in ("num", "topic", "question", "options", "correctId", "answerSource", "official", "confidence"):
            if k not in q:
                P(f"{tag}: missing {k}")
        if not isinstance(q.get("num"), int):
            P(f"{tag}: num must be an int")
        elif q["num"] in nums:
            P(f"{tag}: duplicate num")
        nums.add(q.get("num"))
        if q.get("topic") not in TOPICS:
            P(f"{tag}: topic {q.get('topic')} not in closed list")
        else:
            by_topic[q["topic"]] += 1
        if not str(q.get("question", "")).strip():
            P(f"{tag}: empty question")
        problems += rich_problems(q.get("question", ""), tag)
        problems += rich_problems(q.get("explanation") or "", tag + " explanation")
        if q.get("contextId") and q["contextId"] not in ctxs:
            P(f"{tag}: contextId {q['contextId']} not defined in this file")
        if q.get("image") and not (ROOT / q["image"]).is_file():
            P(f"{tag}: image file missing {q['image']}")
        opts = q.get("options") or []
        ids = [o.get("id") for o in opts]
        if len(opts) < 2:
            P(f"{tag}: fewer than 2 options")
        if len(set(ids)) != len(ids):
            P(f"{tag}: duplicate option ids {ids}")
        for o in opts:
            w = f"{tag} opt {o.get('id')}"
            if o.get("id") not in OPT_IDS:
                P(f"{w}: option id must be one of a..f")
            t = o.get("type", "text")
            if t not in OPT_TYPES:
                P(f"{w}: bad type {t}")
            v = str(o.get("value", ""))
            if not v.strip():
                P(f"{w}: blank value")
            if t == "math":
                if HEB.search(v):
                    P(f"{w}: Hebrew inside math option")
                if v.strip().startswith("$"):
                    P(f"{w}: math option value must be TeX without $")
            elif t == "image":
                if not (ROOT / v).is_file():
                    P(f"{w}: image file missing {v}")
            else:
                problems += rich_problems(v, w)
        if q.get("correctId") not in ids:
            P(f"{tag}: correctId {q.get('correctId')} not among option ids")
        acc = q.get("acceptedIds")
        if acc is not None:
            if not isinstance(acc, list) or len(acc) < 2:
                P(f"{tag}: acceptedIds only when >1 accepted (non-empty list of >=2)")
            else:
                if any(a not in ids for a in acc):
                    P(f"{tag}: acceptedIds {acc} contains an unknown option id")
                if acc[0] != q.get("correctId"):
                    P(f"{tag}: acceptedIds must start with correctId")
                if len(set(acc)) != len(acc):
                    P(f"{tag}: duplicate acceptedIds")
        if "answerSource" in q and q["answerSource"] not in ANSWER_SOURCES:
            P(f"{tag}: answerSource {q['answerSource']} not in {sorted(ANSWER_SOURCES)}")
        if "official" in q and not isinstance(q["official"], bool):
            P(f"{tag}: official must be true/false")
        if "confidence" in q and q["confidence"] not in CONFIDENCE:
            P(f"{tag}: confidence must be high|med|low")
        if "lockOrder" in q and not isinstance(q["lockOrder"], bool):
            P(f"{tag}: lockOrder must be a boolean")
        bad_derived = sorted(k for k in q if k in DERIVED)
        if bad_derived:
            P(f"{tag}: derived fields must not be in raw: {bad_derived}")
        if q.get("confidence") == "low":
            warns.append(f"{tag}: confidence low")
    return problems, warns, len(qs), by_topic


def main():
    args = sys.argv[1:]
    if args:
        files = []
        for a in args:
            p = pathlib.Path(a)
            files.append(p if p.suffix == ".json" else RAW / f"{a}.json")
    else:
        files = [p for p in sorted(RAW.glob("*.json")) if not p.name.startswith("_")]
    total, all_p, all_w, topics = 0, [], [], collections.Counter()
    for fp in files:
        if not fp.is_file():
            all_p.append(f"{fp}: not found")
            continue
        p, w, n, bt = check_file(fp)
        total += n
        topics.update(bt)
        all_p += p
        all_w += w
        print(f"{fp.stem}: {n} questions, {len(p)} problems")
    print(f"\nTOTAL: {total} questions across {len(files)} files")
    print("by topic:", dict(topics))
    if all_w:
        print(f"\nWARNINGS ({len(all_w)}):")
        for x in all_w:
            print("  -", x.encode("ascii", "backslashreplace").decode())
    # string-escape corruption (e.g. "\notin" in a non-raw generator string -> newline + "otin")
    import subprocess
    lint = subprocess.run([sys.executable, str(pathlib.Path(__file__).parent / "gen" / "lint_escapes.py")],
                          capture_output=True, text=True, encoding="utf-8")
    if lint.returncode:
        all_p += ["escape-lint: " + l for l in lint.stdout.splitlines() if not l.startswith("escape problems")]
    print(f"\nPROBLEMS ({len(all_p)}):")
    for x in all_p:
        print("  -", x.encode("ascii", "backslashreplace").decode())
    sys.exit(1 if all_p else 0)


if __name__ == "__main__":
    main()
