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


# ---------------------------------------------------------------- added for T02-T07 (T01 does not use these)
def step_do(pfx, confs, versions, s):
    """the show/hide list that moves tape `pfx` from configuration s-1 to s (same as one run_phrases step)"""
    (q, t0, h0), (p, t1, h1) = confs[s - 1], confs[s]
    do = []
    k0, k1 = _version(versions, h0, confs, s - 1), _version(versions, h0, confs, s)
    if k1 != k0:
        do += hide(f"{pfx}-c{h0}-{k0}") + show(f"{pfx}-c{h0}-{k1}")
    if h1 != h0:
        do += hide(f"{pfx}-hd{h0}") + show(f"{pfx}-hd{h1}")
    if p != q:
        do += hide(f"{pfx}-st-{q}") + show(f"{pfx}-st-{p}")
    return do


def delta_table(pfx, delta, states, syms):
    """δ as a table, LTR: a row per state, a column per symbol, '—' where no transition (= reject).
    Ids: {pfx}-hi-{q}-{a} highlight of a cell (hidden)."""
    head = "".join(f"<th>${sym_tex(a)}$</th>" for a in syms)
    rows = []
    for q in states:
        cells = []
        for a in syms:
            t = delta.get((q, a))
            txt = f"$({state_tex(t[0])}, {sym_tex(t[1])}, {t[2]})$" if t else "—"
            cells.append(f'<td><i id="{pfx}-hi-{q}-{a}" class="cell-hi h"></i>{txt}</td>')
        rows.append(f"<tr><th>${state_tex(q)}$</th>{''.join(cells)}</tr>")
    return (f'<table class="delta tmdelta" id="{pfx}" dir="ltr"><thead><tr><th>$\\delta$</th>{head}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table>')


def table_do(phrases, tpfx, confs, delta, first=0):
    """add to run_phrases' phrases the highlight of the table cell used in each step (phrases[first] = step 1)"""
    prev = None
    for s in range(1, len(confs)):
        q, t, h = confs[s - 1]
        a = t[h] if h < len(t) else BLANK
        cur = f"{tpfx}-hi-{q}-{a}" if (q, a) in delta else None
        do = (hide(prev) if prev else []) + (show(cur) if cur else [])
        phrases[first + s - 1].do += do
        prev = cur
    return prev


def conf_tex(conf):
    """configuration u q v (head on the first symbol of v); trailing blanks dropped, the scanned blank kept"""
    q, t, h = conf
    t = list(t)
    while len(t) > h + 1 and t[-1] == BLANK:
        t.pop()
    while len(t) <= h:
        t.append(BLANK)
    u = " ".join(sym_tex(c) for c in t[:h])
    v = " ".join(sym_tex(c) for c in t[h:])
    return (f"{u} \\; " if u else "") + f"{state_tex(q)} \\; {v}"


def conf_lines(pfx, confs):
    """the run as configurations, one line per step: {pfx}-cf{s} (all hidden)"""
    rows = "".join(f'<div id="{pfx}-cf{s}" class="cfline h">{"$\\vdash$ " if s else ""}${conf_tex(c)}$</div>'
                   for s, c in enumerate(confs))
    return f'<div class="cflines" dir="ltr">{rows}</div>'


def ntm_tree(pfx, branches, w=620, h=430):
    """a computation tree: a root and one branch per entry of `branches` = [(kind, nodes)], kind acc/rej/loop.
    Ids: {pfx}-b{i} branch i (hidden), {pfx}-l{i}-{kind} its end label (hidden; a swap can show the other)."""
    n = len(branches)
    rx, ry, R = w / 2, 40, 18
    out = [f'<svg class="ntm" id="{pfx}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">']
    lab = {"acc": ("✓", "acc"), "rej": ("✗", "rej"), "loop": ("∞", "loop")}
    for i, (kind, k) in enumerate(branches):
        x = w * (i + 0.5) / n
        span = h - (190 if kind == "loop" else 110)            # an infinite branch ends in a long dashed tail
        ys = [ry + span * (j + 1) / k for j in range(k)]
        pts = [(rx, ry)] + [(x, y) for y in ys]
        g = [f'<g id="{pfx}-b{i}" class="h">']
        g.append('<polyline class="ne" points="' + " ".join(f"{a:.0f},{b:.0f}" for a, b in pts) + '"/>')
        g += [f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{R - 4}" class="nn"/>' for y in ys]
        if kind == "loop":
            g.append(f'<line class="ne dash" x1="{x:.0f}" y1="{ys[-1]:.0f}" x2="{x:.0f}" y2="{h - 64:.0f}"/>')
        g.append("</g>")
        out += g
        for kk in ("acc", "rej", "loop"):
            sym, cls = lab[kk]
            vis = "" if kk == kind else " alt"
            out.append(f'<text id="{pfx}-l{i}-{kk}" class="nl {cls} h{vis}" x="{x:.0f}" y="{h - 8}">{sym}</text>')
    out.append(f'<circle cx="{rx}" cy="{ry}" r="{R}" class="nn"/></svg>')        # the root over the branch lines
    return "".join(out)


def ntm_verdict(kinds):
    """'accept' if some branch accepts, 'reject' if all reject, else 'none' (no accepting branch, one never halts)"""
    if "acc" in kinds:
        return "accept"
    return "reject" if all(k == "rej" for k in kinds) else "none"
