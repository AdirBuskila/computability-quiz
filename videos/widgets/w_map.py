# -*- coding: utf-8 -*-
"""Mapping-reduction widgets for the computability videos.

bridge(pfx, ...)   the picture of a reduction: two universes Σ*, the source language A on the left, the target B on the
                   right, words as dots, f as arrows (green = the answer is kept, red = it flips). Every arrow is
                   computed from python predicates by bridge_from(), so the picture is the verified function.
venn(pfx, ...)     the classes R ⊂ RE, coRE with named languages as dots, and reduction arrows between them.
code(pfx, ...)     an exam-style pseudo-code machine, one id per line and a highlight bar per line.
rows(pfx, ...)     a list of rule rows (math on the left, Hebrew on the right), one id per row.

SVG never contains TeX: names like A_TM are drawn with <tspan> subscripts and a drawn bar for complements.
"""
import html as _html

INK, OK, BAD, MUTED, BRAND2 = "#eaedff", "#34d399", "#fb7185", "#9aa0cf", "#38bdf8"


def esc(s):
    return _html.escape(s, quote=True)


def _defs(pfx):
    m = []
    for k, c in (("ok", OK), ("bad", BAD), ("ink", "#c9cdf0")):
        m.append(f'<marker id="{pfx}-ah-{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
                 f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    return f'<defs>{"".join(m)}</defs>'


def _shorten(x1, y1, x2, y2, a, b):
    import math
    d = math.hypot(x2 - x1, y2 - y1) or 1
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    return x1 + ux * a, y1 + uy * a, x2 - ux * b, y2 - uy * b


def _arrow(pfx, aid, p, q, kind, gap=(14, 16), bend=0.0, hidden=True):
    x1, y1, x2, y2 = _shorten(*p, *q, *gap)
    col = {"ok": OK, "bad": BAD}.get(kind, "#c9cdf0")
    mk = kind if kind in ("ok", "bad") else "ink"
    if bend:
        mx, my = (x1 + x2) / 2 - (y2 - y1) * bend, (y1 + y2) / 2 + (x2 - x1) * bend
        d = f"M{x1:.0f},{y1:.0f} Q{mx:.0f},{my:.0f} {x2:.0f},{y2:.0f}"
    else:
        d = f"M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f}"
    dash = ' stroke-dasharray="14 9"' if kind == "bad" else ""
    return (f'<path id="{pfx}-{aid}" class="{"h" if hidden else ""}" d="{d}" fill="none" stroke="{col}" stroke-width="5"'
            f'{dash} marker-end="url(#{pfx}-ah-{mk})"/>')


# ----------------------------------------------------------------------------- bridge
def bridge(pfx, left, right, arrows, A="A", B="B", w=1000, h=560):
    """left/right: [(key, label, inside)]; arrows: [(lkey, rkey, kind)] kind ok|bad.
    Ids: {pfx}-L-<key>, {pfx}-R-<key> word dots (hidden), {pfx}-a-<lkey> arrows (hidden), {pfx}-A / {pfx}-B the
    language ellipses (shown)."""
    U = [(20, 420), (w - 440, w - 20)]
    cy, ry, rx = 230, 150, 175
    pos, out = {}, [f'<svg class="mapsvg" id="{pfx}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" dir="ltr">', _defs(pfx)]
    for side, (x0, x1), name, items in (("L", U[0], A, left), ("R", U[1], B, right)):
        cx = (x0 + x1) / 2
        out.append(f'<rect x="{x0}" y="20" width="{x1 - x0}" height="{h - 40}" rx="26" class="univ"/>')
        out.append(f'<text x="{x1 - 18}" y="58" class="ulabel" text-anchor="end">Σ*</text>')
        out.append(f'<ellipse id="{pfx}-{"A" if side == "L" else "B"}" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="lang"/>')
        t, co = name_svg(name)
        lx, ly = cx - rx + 26, cy - ry + 46
        out.append(f'<text x="{lx}" y="{ly}" class="lname">{t}</text>')
        if co:
            out.append(f'<line x1="{lx}" x2="{lx + 30 + 22 * (len(name) - 4)}" y1="{ly - 40}" y2="{ly - 40}" '
                       f'stroke="#2dd4bf" stroke-width="3"/>')
        ins = [it for it in items if it[2]]
        outs = [it for it in items if not it[2]]
        for i, (k, lab, _) in enumerate(ins):
            y = cy - 80 + (160 * (i + 0.5) / len(ins)) if len(ins) > 1 else cy
            pos[(side, k)] = (cx + (30 if side == "L" else -30), y)
        # words outside the language: a column under the ellipse, on the side facing the other universe, so that
        # no arrow crosses another word
        step = min(55, 150 / max(1, len(outs)))
        for i, (k, lab, _) in enumerate(outs):
            y = h - 60 - step * (len(outs) - 1 - i)
            pos[(side, k)] = (x1 - 50 if side == "L" else x0 + 50, y)
        for k, lab, _ in items:
            x, y = pos[(side, k)]
            tx, anc = (x - 18, "end") if side == "L" else (x + 18, "start")
            out.append(f'<g id="{pfx}-{side}-{k}" class="h"><circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{INK}"/>'
                       f'<text x="{tx:.0f}" y="{y + 11:.0f}" class="wlabel" text-anchor="{anc}">{esc(lab)}</text></g>')
    for lk, rk, kind in arrows:
        out.append(_arrow(pfx, f"a-{lk}", pos[("L", lk)], pos[("R", rk)], kind))
    out.append("</svg>")
    return "".join(out)


def bridge_from(pfx, xs, inA, inB, f, show_label=None, **kw):
    """the verified picture of f on the words xs: A, B predicates, f a python function on words.
    Returns (svg, info) where info[x] = (in_A, f(x), in_B(f(x)), kind)."""
    lab = show_label or (lambda s: s if s else "ε")
    info, left, right, arrows, seen = {}, [], [], [], {}
    for x in xs:
        y = f(x)
        a, b = inA(x), inB(y)
        kind = "ok" if a == b else "bad"
        info[x] = (a, y, b, kind)
        lk = "e" if x == "" else x
        left.append((lk, lab(x), a))
        rk = "e" if y == "" else y
        if rk not in seen:
            seen[rk] = True
            right.append((rk, lab(y), b))
        arrows.append((lk, rk, kind))
    return bridge(pfx, left, right, arrows, **kw), info


# ----------------------------------------------------------------------------- language names in SVG
def name_svg(n):
    """'A_TM' -> A<sub>TM</sub>; 'co:A_TM' -> the same with a bar over it (drawn by .bar via text-decoration)"""
    co = n.startswith("co:")
    n = n[3:] if co else n
    base, _, sub = n.partition("_")
    t = esc(base) + (f'<tspan dy="9" font-size="24">{esc(sub)}</tspan>' if sub else "")
    return t, co


# ----------------------------------------------------------------------------- venn of the classes
REGION = {"R": (500, 250), "RE\\R": (180, 250), "coRE\\R": (820, 250), "none": (500, 505)}


def venn(pfx, langs, arrows=(), w=1000, h=580):
    """langs: [(key, name, region, dx, dy)] region in R | RE\\R | coRE\\R | none; arrows: [(src, dst, kind, bend)].
    Ids: {pfx}-n-<key> a language dot (hidden), {pfx}-a-<src>-<dst> an arrow (hidden), {pfx}-x-<src>-<dst> a red ✗
    on a forbidden arrow (hidden). The RE / coRE ellipses and the labels are shown."""
    out = [f'<svg class="mapsvg" id="{pfx}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" dir="ltr">', _defs(pfx)]
    out.append(f'<rect x="10" y="10" width="{w - 20}" height="{h - 20}" rx="26" class="univ"/>')
    out.append(f'<ellipse cx="390" cy="250" rx="320" ry="205" class="cls re"/>')
    out.append(f'<ellipse cx="610" cy="250" rx="320" ry="205" class="cls core"/>')
    out.append(f'<text x="120" y="110" class="cname">RE</text>')
    out.append(f'<text x="880" y="110" class="cname" text-anchor="end">coRE</text>')
    out.append(f'<text x="500" y="110" class="cname r" text-anchor="middle">R</text>')
    pos = {}
    for key, name, region, dx, dy in langs:
        x, y = REGION[region]
        x, y = x + dx, y + dy
        pos[key] = (x, y)
        t, co = name_svg(name)
        ty = y + 46 if region in ("R", "none") else y - 18          # below the dot where arrows come from above
        bar = (f'<line x1="{x - 26}" x2="{x + 26}" y1="{ty - 32}" y2="{ty - 32}" stroke="{INK}" stroke-width="3"/>'
               if co else "")
        out.append(f'<g id="{pfx}-n-{key}" class="h"><circle cx="{x}" cy="{y}" r="9" fill="{INK}"/>'
                   f'<text x="{x}" y="{ty}" class="vlabel" text-anchor="middle">{t}</text>{bar}</g>')
    for src, dst, kind, bend in arrows:
        out.append(_arrow(pfx, f"a-{src}-{dst}", pos[src], pos[dst], kind, gap=(16, 18), bend=bend))
        if kind == "bad":
            (x1, y1), (x2, y2) = pos[src], pos[dst]
            mx, my = (x1 + x2) / 2 - (y2 - y1) * bend / 2, (y1 + y2) / 2 + (x2 - x1) * bend / 2   # on the curve
            out.append(f'<text id="{pfx}-x-{src}-{dst}" class="h xmark" x="{mx:.0f}" y="{my + 16:.0f}" '
                       f'text-anchor="middle">✗</text>')
    out.append("</svg>")
    return "".join(out)


# ----------------------------------------------------------------------------- pseudo-code
def code(pfx, lines, head=None):
    """lines: plain strings (may hold $TeX$); indentation by leading spaces. Ids: {pfx}-l<i> line, {pfx}-hl<i> highlight
    bar (hidden)."""
    rows = []
    if head:
        rows.append(f'<div class="chead">{head}</div>')
    for i, ln in enumerate(lines):
        ind = len(ln) - len(ln.lstrip(" "))
        rows.append(f'<div class="cline" id="{pfx}-l{i}" style="padding-left:{18 + ind * 16}px">'
                    f'<i id="{pfx}-hl{i}" class="chl h"></i><span>{ln.strip()}</span></div>')
    return f'<div class="codebox" id="{pfx}" dir="ltr">{"".join(rows)}</div>'


# ----------------------------------------------------------------------------- rule rows
def rows(pfx, items, cls=""):
    """items: [(math_html, hebrew_html)] -> ids {pfx}-<i> (hidden)"""
    r = "".join(f'<div id="{pfx}-{i}" class="row h"><span class="sym">{m}</span><span>{t}</span></div>'
                for i, (m, t) in enumerate(items))
    return f'<div class="tuple mrows {cls}">{r}</div>'


# ----------------------------------------------------------------------------- pipeline of boxes
def pipe(pfx, items):
    """a left-to-right chain of boxes joined by arrows: items [(html, kind)] kind '' | 'f' | 'solver' | 'ans'.
    Ids: {pfx}-<i> each box with the arrow before it (hidden)."""
    out = []
    for i, (h, kind) in enumerate(items):
        arr = '<span class="parr">→</span>' if i else ""
        out.append(f'<div id="{pfx}-{i}" class="pstep h">{arr}<div class="pbox {kind}">{h}</div></div>')
    return f'<div class="pipe" dir="ltr">{"".join(out)}</div>'
