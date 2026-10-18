"""TM course: simulate every printed transition table, recompute every number."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from common import *

rep = Report("tm")
levels = load_levels("tm")
for L, q in questions(levels):
    if not check_common(rep, q):
        rep.ok(False, f"{q['id']}: unknown chk kind {q['chk']['kind']}")
rep.done()
