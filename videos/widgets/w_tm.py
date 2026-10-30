# -*- coding: utf-8 -*-
"""Turing-machine widgets for the computability videos: a tape whose cells change, a head that moves, a state badge,
and the phrases that run a machine step by step. Every step comes from trace(), whose semantics are those of the
course checker (tools/verify/needhelp/common.py run_tm: a move L from cell 0 keeps the head in place, a missing
transition rejects); trace() asserts that it ends exactly like run_tm.

Ids for tape(pfx, ...):
  {pfx}-c{i}-{k}   version k of the symbol in cell i (k = 0 is the initial symbol, shown at start)
  {pfx}-hd{i}      the head over cell i (hd0 shown at start unless hidden=True)
  {pfx}-st-{q}     the state badge for state q (start state shown at start)
"""
from common import run_tm, BLANK, ACC, REJ          # course checker (SIM_PATHS)
from vid import P, show, hide
import lexicon

SHOW_SYM = {BLANK: "⊔"}
DIR_SAY = {"R": "וזזים ימינה", "L": "וזזים שמאלה"}


def sym_tex(c):
    return r"\sqcup" if c == BLANK else c


def sym_say(c):
    if c == BLANK:
        return "רווח"
    return lexicon.tex_say(c) or c


def state_tex(q):
    return {ACC: "q_{acc}", REJ: "q_{rej}"}.get(q, q if q.startswith("q") else f"q_{{{q}}}")


def state_say(q):
    return lexicon.tex_say(state_tex(q))


def trace(delta, start, word, cap=200):
    """configurations [(state, tape list, head)] from the start to the halt, and the result ('accept'/'reject'/'loop')"""
    tape = list(word) or [BLANK]
    pos, st = 0, start
    confs = [(st, tape[:], pos)]
    steps = 0
    while st not in (ACC, REJ) and steps < cap:
        while pos >= len(tape):
            tape.append(BLANK)
        nxt = delta.get((st, tape[pos]))
        if nxt is None:                       # a missing transition rejects without a step
            st = REJ
            confs.append((st, tape[:], pos))
            break
        st, b, d = nxt
        tape[pos] = b
        pos = max(0, pos - 1) if d == "L" else pos + 1
        while pos >= len(tape):
            tape.append(BLANK)
        confs.append((st, tape[:], pos))
        steps += 1
    result = {ACC: "accept", REJ: "reject"}.get(st, "loop")
    ref = run_tm(delta, start, word, cap)
    assert ref[0] == result, (ref, result)
    if result != "loop":
        assert ref[1] == steps, (ref, steps)
    return confs, result


def tape(pfx, confs, ncells, hidden=False):
    """the tape over the whole run: every symbol each cell ever holds, stacked; the head; the state badges"""
    versions = []
    for i in range(ncells):
        seq = []
        for _, t, _ in confs:
            c = t[i] if i < len(t) else BLANK
            if not seq or seq[-1] != c:
                seq.append(c)
        versions.append(seq)
    cells = []
    for i, seq in enumerate(versions):
        spans = "".join(f'<b id="{pfx}-c{i}-{k}" class="tsym{" h" if k else ""}">${sym_tex(c)}$</b>'
                        for k, c in enumerate(seq))
        head = f'<i id="{pfx}-hd{i}" class="thead{" h" if (i or hidden) else ""}">▼</i>'
        cells.append(f'<span class="tmcell">{head}{spans}</span>')
    more = '<span class="tmcell more"><b class="tsym">⋯</b></span>'
    states = sorted({q for q, _, _ in confs}, key=lambda q: (q in (ACC, REJ), q))
    badges = "".join(f'<span id="{pfx}-st-{q}" class="tmstate{" h" if (q != confs[0][0] or hidden) else ""}">'
                     f'${state_tex(q)}$</span>' for q in states)
    return (f'<div class="tmwrap" id="{pfx}" dir="ltr"><div class="tmtape">{"".join(cells)}{more}</div>'
            f'<div class="tmstates">{badges}</div></div>'), versions


def _version(versions, i, confs, upto):
    """index of the symbol version of cell i at configuration `upto`"""
    seq, k, last = versions[i], 0, None
    for _, t, _ in confs[:upto + 1]:
        c = t[i] if i < len(t) else BLANK
        if last is not None and c != last:
            k += 1
        last = c
    return k


def run_phrases(pfx, delta, confs, versions, step_sub=None, lead=None, end=True):
    """one phrase per step:  δ(q, a) = (p, b, D): write b, go to p, move D. Returns the phrases."""
    ph = []
    if lead:
        ph.append(P(lead))
    for s in range(1, len(confs)):
        (q, t0, h0), (p, t1, h1) = confs[s - 1], confs[s]
        a = t0[h0] if h0 < len(t0) else BLANK
        do = []
        if p == REJ and delta.get((q, a)) is None:
            sub = f"אין מעבר מ-${state_tex(q)}$ עם ${sym_tex(a)}$: המכונה דוחה."
            say = f"אין מעבר מ{state_say(q)} עם {sym_say(a)}: המכונה דוחה."
            do = hide(f"{pfx}-st-{q}") + show(f"{pfx}-st-{p}")
            ph.append(P(sub, say=say, do=do))
            continue
        _, b, d = delta[(q, a)]
        k0, k1 = _version(versions, h0, confs, s - 1), _version(versions, h0, confs, s)
        if k1 != k0:
            do += hide(f"{pfx}-c{h0}-{k0}") + show(f"{pfx}-c{h0}-{k1}")
        if h1 != h0:
            do += hide(f"{pfx}-hd{h0}") + show(f"{pfx}-hd{h1}")
        if p != q:
            do += hide(f"{pfx}-st-{q}") + show(f"{pfx}-st-{p}")
        move = DIR_SAY[d] if h1 != h0 else "והראש נשאר במקום"
        sub = step_sub(s, q, a, p, b, d) if step_sub else (
            f"$\\delta({state_tex(q)}, {sym_tex(a)}) = ({state_tex(p)}, {sym_tex(b)}, {d})$")
        say = (f"במצב {state_say(q)}, הראש רואה {sym_say(a)}: כותבים {sym_say(b)}, "
               f"עוברים ל{state_say(p)}, {move}.")
        ph.append(P(sub, say=say, do=do))
    return ph
