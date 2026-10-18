"""Shared helpers for the guided-course checkers (tools/verify/needhelp/<course>/check.py).

The checkers read the RAW course levels (TeX still in $..$, the `chk` annotations still there) that
`node tools/build_courses.js --export <file>` writes, and assert every machine-checkable claim:
  - tm-trace / tm-lang : a transition table printed in a question is parsed and SIMULATED
  - arith              : a number in the options is recomputed
  - closure / fact / red-rule ... : options are checked against the rule tables in rules.py
  - brute-fn / brute-universe : reductions are brute-forced on small instances
Each check asserts that the keyed option is right AND that every other option is wrong (one defensible answer).
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
EXPORT = os.path.join(HERE, "_levels.json")


def load_levels(course, rebuild=True):
    if rebuild:
        r = subprocess.run(["node", os.path.join(APP, "tools", "build_courses.js"), "--export", EXPORT],
                           capture_output=True, text=True, encoding="utf-8", cwd=APP)
        if r.returncode != 0:
            print(r.stdout, r.stderr)
            sys.exit(2)
    with open(EXPORT, encoding="utf-8") as f:
        data = json.load(f)
    return [d["level"] for d in data if d["course"] == course]


def questions(levels):
    for L in levels:
        for q in L["questions"]:
            if "chk" in q:
                yield L, q


def plain(s):
    """option/question text with TeX markers removed and whitespace normalised"""
    s = re.sub(r"\*\*", "", str(s))
    s = s.replace("$", "")
    return re.sub(r"\s+", " ", s).strip()


class Report:
    def __init__(self, name):
        self.name, self.n, self.fails = name, 0, []

    def ok(self, cond, msg):
        self.n += 1
        if not cond:
            self.fails.append(msg)
            print("  FAIL", msg)

    def done(self):
        print(f"{self.name}: {self.n - len(self.fails)}/{self.n} checks passed")
        if self.fails:
            sys.exit(1)


def exactly_one(rep, q, truths, label):
    """truths[i] = is option i a correct statement?  The keyed option must be the only True one."""
    key = q["answer"]
    rep.ok(len(truths) == len(q["options"]), f"{q['id']}: {label}: {len(truths)} truths for {len(q['options'])} options")
    rep.ok(truths[key] is True, f"{q['id']}: {label}: keyed option {key} is not true")
    others = [i for i, t in enumerate(truths) if t and i != key]
    rep.ok(not others, f"{q['id']}: {label}: other option(s) {others} are also true (not exactly one defensible answer)")


# ----------------------------------------------------------------------------- Turing machine simulator
BLANK = "_"
ACC, REJ = "acc", "rej"


def _sym(s):
    s = s.strip()
    return BLANK if s in (r"\sqcup", "⊔", "_") else s


def _state(s):
    s = s.strip()
    if s in (r"q_{acc}", "acc"):
        return ACC
    if s in (r"q_{rej}", "rej"):
        return REJ
    return s


def parse_table(table):
    """q['table'] -> (delta, start).  Header: ['state', sym, sym, ...]; cell '(p, b, R)' or '-' / '—' (= reject)."""
    head = [_sym(plain(h)) for h in table["head"][1:]]
    delta, start = {}, None
    for row in table["rows"]:
        st = _state(plain(row[0]))
        start = start or st
        for sym, cell in zip(head, row[1:]):
            c = plain(cell)
            if c in ("-", "—", ""):
                continue
            m = re.fullmatch(r"\(\s*(.+?)\s*,\s*(.+?)\s*,\s*([LR])\s*\)", c)
            assert m, f"bad transition cell {cell!r}"
            delta[(st, sym)] = (_state(m.group(1)), _sym(m.group(2)), m.group(3))
    return delta, start


def run_tm(delta, start, word, cap=3000):
    """-> (result, steps, tape).  result in {'accept','reject','loop'}; the head stays put on L at cell 0;
    a missing transition rejects.  'loop' = no halt within `cap` steps."""
    tape = list(word) if word else []
    pos, st, steps = 0, start, 0
    while steps < cap:
        if st == ACC:
            return "accept", steps, "".join(tape).rstrip(BLANK)
        if st == REJ:
            return "reject", steps, "".join(tape).rstrip(BLANK)
        while pos >= len(tape):
            tape.append(BLANK)
        a = tape[pos]
        nxt = delta.get((st, a))
        if nxt is None:
            st = REJ   # a missing transition rejects without a step
            continue
        st, b, d = nxt
        tape[pos] = b
        pos = max(0, pos - 1) if d == "L" else pos + 1
        steps += 1
    return "loop", steps, "".join(tape).rstrip(BLANK)


# ----------------------------------------------------------------------------- generic checks
PREDS = {   # named languages over {0,1} used by tm-lang annotations
    "0n1n": lambda w: re.fullmatch(r"(0*)(1*)", w) is not None and w.count("0") == w.count("1"),
    "0n1m": lambda w: re.fullmatch(r"0+1+", w) is not None,
    "eqcount": lambda w: w.count("0") == w.count("1"),
    "01star": lambda w: re.fullmatch(r"(01)*", w) is not None,
    "starts1": lambda w: w.startswith("1"),
    "starts0": lambda w: w.startswith("0"),
    "all": lambda w: True,
    "none": lambda w: False,
    "even1": lambda w: w.count("1") % 2 == 0,
    "odd1": lambda w: w.count("1") % 2 == 1,
    "even0": lambda w: w.count("0") % 2 == 0,
    "lenEven": lambda w: len(w) % 2 == 0,
}


def words(maxlen):
    out = [""]
    for n in range(1, maxlen + 1):
        out += ["".join(p) for p in __import__("itertools").product("01", repeat=n)]
    return out


def lang_of(delta, start, maxlen=8, cap=4000):
    return {w for w in words(maxlen) if run_tm(delta, start, w, cap)[0] == "accept"}


def safe_eval(expr):
    assert re.fullmatch(r"[0-9+\-*/() ]+|[0-9+\-*/() ]*\*\*[0-9+\-*/() *]*", expr), expr
    return eval(expr)


def check_common(rep, q):
    """tm-trace, tm-lang, tm-halts, arith. Returns True when the kind was handled."""
    c, k = q["chk"], q["chk"]["kind"]
    n = len(q["options"])
    if k == "arith":
        want = safe_eval(c["expr"])
        vals = [safe_eval(str(o)) for o in c["opts"]]
        exactly_one(rep, q, [v == want for v in vals], f"arith {c['expr']}={want}")
        # the displayed option text must agree with the annotation when it is a plain number
        for i, o in enumerate(q["options"]):
            t = plain(o).replace(" ", "")
            if re.fullmatch(r"\d+", t):
                rep.ok(int(t) == vals[i], f"{q['id']}: option {i} text {t} != annotation {vals[i]}")
        return True
    if k in ("tm-trace", "tm-lang", "tm-halts"):
        delta, start = parse_table(q["table"])
    if k == "tm-trace":
        res, steps, tape = run_tm(delta, start, c["input"])
        got = {"result": res, "steps": str(steps), "tape": tape}[c["ask"]]
        rep.ok(res != "loop" or c["ask"] == "result", f"{q['id']}: trace asked on a looping run")
        exactly_one(rep, q, [str(o) == got for o in c["opts"]], f"trace {c['ask']}={got!r}")
        if c["ask"] != "result":   # option texts must equal the annotation
            for i, o in enumerate(q["options"]):
                rep.ok(plain(o) == str(c["opts"][i]), f"{q['id']}: option {i} text {plain(o)!r} != annotation {c['opts'][i]!r}")
        return True
    if k == "tm-lang":
        L = lang_of(delta, start)
        truths = [L == {w for w in words(8) if PREDS[p](w)} for p in c["opts"]]
        exactly_one(rep, q, truths, "tm-lang (words up to length 8)")
        return True
    if k == "tm-halts":
        halts = all(run_tm(delta, start, w, 4000)[0] != "loop" for w in words(8))
        exactly_one(rep, q, [(o == "halts") == halts for o in c["opts"]], f"tm-halts={halts}")
        return True
    return False
