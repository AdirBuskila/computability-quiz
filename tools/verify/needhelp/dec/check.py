"""Decidability course: every option is asserted against the rule tables (rules.py).

  rules   : opts = rule ids; the option is true iff RULES[id][0]
  closure : prem = {var: class}; opts = [expr, "always:<cls>" | "possible:<cls>"]  (closure engine + 4-element model)
  fact    : lang = key of FACTS, ask = class | complement; opts = class names
  shape   : shape = key of SHAPES; opts = class names
Each question must have exactly one true option, and it must be the keyed one."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from common import *
from rules import *

rep = Report("dec")
levels = load_levels("dec")
for L, q in questions(levels):
    c, k = q["chk"], q["chk"]["kind"]
    if k == "rules":
        exactly_one(rep, q, [rule(r) for r in c["opts"]], "rules")
    elif k == "closure":
        truths = []
        for e, claim in c["opts"]:
            try:
                truths.append(claim_truth(e, c["prem"], claim))
            except ValueError as ex:
                rep.ok(False, f"{q['id']}: {ex}")
                truths.append(None)
        if c.get("neg"):
            truths = [None if t is None else (not t) for t in truths]
        exactly_one(rep, q, truths, f"closure given {c['prem']}")
    elif k == "fact":
        cls = FACTS[c["lang"]]
        if c.get("ask") == "complement":
            cls = complement_class(cls)
        exactly_one(rep, q, [o == cls for o in c["opts"]], f"fact {c['lang']} -> {cls}")
    elif k == "shape":
        exactly_one(rep, q, [o == SHAPES[c["shape"]] for o in c["opts"]], f"shape {c['shape']} -> {SHAPES[c['shape']]}")
    elif not check_common(rep, q):
        rep.ok(False, f"{q['id']}: unknown chk kind {k}")
rep.done()
