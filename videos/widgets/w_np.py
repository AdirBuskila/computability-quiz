# -*- coding: utf-8 -*-
"""P / NP widgets for the computability videos: small graphs (CLIQUE, IS, VC, the 3SAT gadget), CNF formulas with an
assignment, nested complexity classes and a reduction diagram. Every graph fact a script states is checked here by
brute force (the graphs are tiny), so a script asserts instead of trusting a drawing.

Ids for graph_svg(pfx, ...):
  {pfx}-v-{v}        vertex group (always visible)
  {pfx}-hv-{v}       highlight ring around vertex v (hidden)
  {pfx}-e-{a}-{b}    edge a-b, a < b in the vertex order (visible unless listed in hidden=)
  {pfx}-he-{a}-{b}   highlighted copy of edge a-b (hidden)
"""
import html as _html
import itertools
import re


# ----------------------------------------------------------------------------- graph facts (brute force)
def E_(*pairs):
    return frozenset(frozenset(p) for p in pairs)


def is_clique(E, S):
    return all(frozenset(p) in E for p in itertools.combinations(S, 2))


def is_indep(E, S):
    return not any(frozenset(p) in E for p in itertools.combinations(S, 2))


def is_cover(E, S):
    return all(e & set(S) for e in E)


def complement(V, E):
    return frozenset(frozenset(p) for p in itertools.combinations(V, 2)) - E


def has(V, E, k, pred):
    return any(pred(E, S) for S in itertools.combinations(V, k))


def best(V, E, pred, largest=True):
    sizes = [k for k in range(len(V) + 1) if has(V, E, k, pred)]
    return max(sizes) if largest else min(sizes)


# ----------------------------------------------------------------------------- CNF
# a literal is (var, positive); a clause a tuple of literals; a formula a list of clauses
def lit_true(l, a):
    return a[l[0]] == l[1]


def satisfies(phi, a):
    return all(any(lit_true(l, a) for l in c) for c in phi)


def variables(phi):
    return sorted({v for c in phi for v, _ in c})


def assignments(phi):
    vs = variables(phi)
    for bits in itertools.product([False, True], repeat=len(vs)):
        yield dict(zip(vs, bits))


def satisfiable(phi):
    return any(satisfies(phi, a) for a in assignments(phi))


def sat_to_is(phi):
    """the 3SAT -> IS graph: a vertex (i, j) per literal occurrence; clause triangles; contradictory pairs"""
    V = [(i, j) for i, c in enumerate(phi) for j in range(len(c))]
    E = set()
    for u, v in itertools.combinations(V, 2):
        lu, lv = phi[u[0]][u[1]], phi[v[0]][v[1]]
        if u[0] == v[0] or (lu[0] == lv[0] and lu[1] != lv[1]):
            E.add(frozenset((u, v)))
    return V, frozenset(E)


def lit_tex(l):
    v = re.sub(r"(\d+)$", r"_{\1}", l[0])
    return v if l[1] else f"\\lnot {v}"


def cnf_tex(phi):
    return " \\land ".join("(" + " \\lor ".join(lit_tex(l) for l in c) + ")" for c in phi)


# ----------------------------------------------------------------------------- drawing
def _esc(s):
    return _html.escape(str(s), quote=True)


def _label(name):
    """'x1' -> x with subscript 1; '¬x2' -> ¬x₂; anything else as is (SVG holds no TeX)"""
    m = re.fullmatch(r"(¬?)([a-zA-Z])(\d+)", name)
    if m:
        return f'{m.group(1)}{m.group(2)}<tspan dy="8" font-size="20">{m.group(3)}</tspan>'
    return _esc(name)


def _key(v):
    return re.sub(r"[^0-9A-Za-z_]", "", str(v).replace("¬", "n").replace("(", "").replace(", ", "_"))


def graph_svg(pfx, V, E, pos, names=None, w=900, h=560, hidden=(), alt=(), r=34, scale=1.0, bend=0.16):
    """V: vertices in order; E: set of frozenset pairs; pos: {v: (x, y)}; names: {v: label}; hidden: edges (pairs)
    drawn with class h (shown later); alt: edges drawn in the second color (e.g. complement edges)."""
    names = names or {v: str(v) for v in V}
    order = {v: i for i, v in enumerate(V)}
    hidden = {frozenset(p) for p in hidden}
    alt = {frozenset(p) for p in alt}
    out = [f'<svg class="npg" id="{pfx}" viewBox="0 0 {w} {h}" width="{w * scale:.0f}" height="{h * scale:.0f}" direction="ltr">']
    hi = []
    mid_y = sum(y for _, y in pos.values()) / len(pos)
    for e in sorted(E, key=lambda e: sorted(order[x] for x in e)):
        a, b = sorted(e, key=lambda x: order[x])
        (x1, y1), (x2, y2) = pos[a], pos[b]
        eid = f"{pfx}-e-{_key(a)}-{_key(b)}"
        cls = "ge" + (" alt" if e in alt else "") + (" h" if e in hidden else "")
        # an edge whose straight line would run through another vertex is drawn as a curve, away from the middle
        dx, dy = x2 - x1, y2 - y1
        L2 = dx * dx + dy * dy or 1
        blocked = any(((px - x1) * dx + (py - y1) * dy) / L2 > 0.02 and ((px - x1) * dx + (py - y1) * dy) / L2 < 0.98
                      and abs((px - x1) * dy - (py - y1) * dx) / L2 ** 0.5 < r + 8
                      for v, (px, py) in pos.items() if v not in (a, b))
        if blocked:
            L = L2 ** 0.5
            nx, ny = -dy / L, dx / L                   # a normal; point it away from the drawing's middle
            if (ny > 0) != ((y1 + y2) / 2 >= mid_y):
                nx, ny = -nx, -ny
            k = bend * L + 30
            cx, cy = (x1 + x2) / 2 + nx * k, (y1 + y2) / 2 + ny * k
            d = f"M{x1},{y1} Q{cx:.1f},{cy:.1f} {x2},{y2}"
            out.append(f'<path id="{eid}" d="{d}" class="{cls}" fill="none"/>')
            hi.append(f'<path id="{pfx}-he-{_key(a)}-{_key(b)}" d="{d}" class="ge-hi h" fill="none"/>')
            continue
        out.append(f'<line id="{eid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"/>')
        hi.append(f'<line id="{pfx}-he-{_key(a)}-{_key(b)}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ge-hi h"/>')
    out += hi
    for v in V:
        x, y = pos[v]
        out.append(f'<circle id="{pfx}-hv-{_key(v)}" cx="{x}" cy="{y}" r="{r + 9}" class="gv-hi h"/>'
                   f'<g id="{pfx}-v-{_key(v)}"><circle cx="{x}" cy="{y}" r="{r}" class="gv"/>'
                   f'<text x="{x}" y="{y + 10}" class="gl">{_label(names[v])}</text></g>')
    out.append("</svg>")
    return "".join(out)


def eid(pfx, a, b, V):
    """id of edge a-b in a graph drawn with vertex order V"""
    a, b = sorted((a, b), key=V.index)
    return f"{pfx}-e-{_key(a)}-{_key(b)}"


def heid(pfx, a, b, V):
    a, b = sorted((a, b), key=V.index)
    return f"{pfx}-he-{_key(a)}-{_key(b)}"


def hv(pfx, *vs):
    return [f"{pfx}-hv-{_key(v)}" for v in vs]


def circle_pos(V, cx=450, cy=280, rad=210, start=-90):
    import math
    n = len(V)
    return {v: (round(cx + rad * math.cos(math.radians(start + 360 * i / n))),
                round(cy + rad * math.sin(math.radians(start + 360 * i / n)))) for i, v in enumerate(V)}


def classes(pfx, rings):
    """nested complexity classes, outermost first: rings = [(key, label_html)]. Ids {pfx}-{key}; all hidden but the
    outermost. Labels may hold $TeX$ (HTML, not SVG)."""
    html_ = ""
    for i, (key, label) in enumerate(reversed(rings)):
        last = i == len(rings) - 1
        html_ = (f'<div id="{pfx}-{key}" class="ncls{"" if last else " h"}"><span class="nlab">{label}</span>'
                 f'{html_}</div>')
    return f'<div class="nclswrap" dir="ltr">{html_}</div>'


def redux(pfx, left, right, fn="f", A="A", B="B"):
    """A --f--> B with yes/no rows: ids {pfx}-yes, {pfx}-no (hidden rows), {pfx}-arr (the arrow)"""
    return (f'<div class="redux" id="{pfx}" dir="ltr">'
            f'<div class="rbox">{left}</div><div id="{pfx}-arr" class="rarr">${fn}$<span>⟶</span></div>'
            f'<div class="rbox">{right}</div>'
            f'<div id="{pfx}-yes" class="rrow ok h"><span>$x \\in {A}$</span><span>⟶</span><span>${fn}(x) \\in {B}$</span></div>'
            f'<div id="{pfx}-no" class="rrow bad h"><span>$x \\notin {A}$</span><span>⟶</span><span>${fn}(x) \\notin {B}$</span></div>'
            f'</div>')


def cnf_row(pfx, phi):
    """a CNF formula, one box per clause: ids {pfx}-c{i} (box), {pfx}-ok{i} / {pfx}-bad{i} (hidden marks under it)"""
    boxes = []
    for i, c in enumerate(phi):
        tex = "(" + r" \lor ".join(lit_tex(l) for l in c) + ")"
        boxes.append(f'<span class="cbox" id="{pfx}-c{i}">${tex}$<b id="{pfx}-ok{i}" class="cmark ok h">✓</b>'
                     f'<b id="{pfx}-bad{i}" class="cmark bad h">✗</b></span>')
    sep = r'<span class="cand">$\land$</span>'
    return f'<div class="cnfrow" id="{pfx}" dir="ltr">{sep.join(boxes)}</div>'


def assign_tex(a):
    return r",\ ".join(re.sub(r"(\d+)$", r"_{\1}", v) + " = " + ("T" if b else "F") for v, b in sorted(a.items()))
