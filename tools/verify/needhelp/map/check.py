"""Mapping-reductions course.

  brute-fn       : A, B (python predicates over x / y), f (python expr over x) -> brute force every binary word up to
                   length 10: opts = yes | fail1 (x in A, f(x) not in B) | fail2 (x not in A, f(x) in B) | unc
  brute-fn2      : same, opts = A<=B | A<=coB | both | neither
  brute-universe : all subsets A,B,C of a universe of n words; R(X,Y) = a reduction function exists; every option is a
                   boolean expression that must hold (or fail) for ALL A,B,C
  red-impossible : the keyed option is a reduction forbidden by class monotonicity; every other option must be a
                   reduction the course lists as existing
  red-K          : simulate the printed machine to find the language of K_{M,w} / the length bound of R_{M,w}
  rules          : rule table (rules.py)
"""
import itertools, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from common import *
from rules import *

rep = Report("map")
levels = load_levels("map")

WORDS = words(10)


def fn_checks(c):
    A = eval("lambda x: " + c["A"])
    B = eval("lambda y: " + c["B"])
    f = eval("lambda x: " + c["f"])
    fail1 = any(A(x) and not B(f(x)) for x in WORDS)
    fail2 = any((not A(x)) and B(f(x)) for x in WORDS)
    return A, B, f, fail1, fail2


def reduction_exists(n, X, Y):
    U = range(n)
    for f in itertools.product(U, repeat=n):
        if all(((X >> x) & 1) == ((Y >> f[x]) & 1) for x in U):
            return True
    return False


# known reductions listed in the course (src, dst); everything else is judged by class monotonicity only
KNOWN = {("A_TM", "H_TM"), ("H_TM", "A_TM"), ("H_TM", "notE_TM"), ("coH_TM", "E_TM"), ("H_TM", "ALL_TM"),
         ("A_TM", "ALL_TM"), ("ALL_TM", "EQ_TM"), ("E_TM", "EQ_TM"), ("coA_TM", "E_TM"), ("H_TM", "EQ_TM")}


def flags_of(lang):
    return {"R": {"R", "RE", "coRE"}, "RE\\R": {"RE"}, "coRE\\R": {"coRE"}, "none": set()}[FACTS[lang]]


def impossible(src, dst):
    fs, fd = flags_of(src), flags_of(dst)
    return any(g in fd and g not in fs for g in ("R", "RE", "coRE"))


for L, q in questions(levels):
    c, k = q["chk"], q["chk"]["kind"]
    if k == "brute-fn":
        A, B, f, fail1, fail2 = fn_checks(c)
        got = "yes" if not (fail1 or fail2) else ("fail1" if fail1 and not fail2 else ("fail2" if fail2 and not fail1 else "both"))
        exactly_one(rep, q, [o == got for o in c["opts"]], f"brute-fn -> {got}")
    elif k == "brute-fn2":
        A, B, f, fail1, fail2 = fn_checks(c)
        to_b = not (fail1 or fail2)
        to_cob = all((A(x)) == (not B(f(x))) for x in WORDS)
        got = "both" if (to_b and to_cob) else "A<=B" if to_b else "A<=coB" if to_cob else "neither"
        exactly_one(rep, q, [o == got for o in c["opts"]], f"brute-fn2 -> {got}")
    elif k == "brute-universe":
        n = c["n"]
        full = (1 << n) - 1
        cache = {}

        def R(X, Y):
            if (X, Y) not in cache:
                cache[(X, Y)] = reduction_exists(n, X, Y)
            return cache[(X, Y)]
        truths = []
        for stmt in c["opts"]:
            ok = True
            for A_, B_, C_ in itertools.product(range(full + 1), repeat=3):
                env = dict(A=A_, B=B_, C=C_, E=0, S=full, R=R, comp=lambda X: full & ~X)
                if not eval(stmt, {}, env):
                    ok = False
                    break
            truths.append(ok)
        exactly_one(rep, q, truths, f"brute-universe n={n}")
    elif k == "red-impossible":
        key = q["answer"]
        for i, (s, d) in enumerate(c["opts"]):
            if i == key:
                rep.ok(impossible(s, d), f"{q['id']}: keyed {s}<={d} is not forbidden by the classes")
            else:
                rep.ok((s, d) in KNOWN and not impossible(s, d), f"{q['id']}: option {i} {s}<={d} is not a listed reduction")
    elif k == "red-K":
        # the machine printed in the question
        delta, start = parse_table(q["table"])
        res, steps, tape = run_tm(delta, start, c["w"], 4000)
        if c["ask"] == "K-lang":
            got = "Sigma*" if res != "loop" else "empty"
            exactly_one(rep, q, [o == got for o in c["opts"]], f"K-lang -> {got}")
        else:
            rep.ok(res != "loop", f"{q['id']}: R-min on a looping machine")
            # R_{M,w}(y) runs |y| steps and accepts if M has halted: the shortest accepted length is the halting step count
            shortest = steps   # M halts after exactly `steps` transitions
            exactly_one(rep, q, [o == str(shortest) for o in c["opts"]], f"R-min -> {shortest}")
            for i, o in enumerate(q["options"]):
                rep.ok(plain(o) == str(c["opts"][i]), f"{q['id']}: option text {plain(o)} != annotation {c['opts'][i]}")
    elif k == "rules":
        exactly_one(rep, q, [rule(r) for r in c["opts"]], "rules")
    elif not check_common(rep, q):
        rep.ok(False, f"{q['id']}: unknown chk kind {k}")
rep.done()
