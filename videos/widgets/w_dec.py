# -*- coding: utf-8 -*-
"""Decidability-course widgets: the class map (RE and coRE ellipses, R in the overlap, "none" outside), a table whose
rows/cells are revealed one by one, and run lanes (two machines run side by side or one after the other).

Every class a language is placed in comes from the course rule tables (tools/verify/needhelp/rules.py FACTS),
asserted when the widget is built; scripts check closure claims with rules.claim_truth / model_classes.

Ids for venn(pfx, items):
  {pfx}-f-<region>   a fill that highlights one region (region keys below: RE, coRE, R, none)
  {pfx}-t-<region>   the region's title
  {pfx}-l-<key>      a language chip placed in its region
Ids for table(pfx, ...): {pfx}-r{i} row i, {pfx}-c{i}-{j} cell content, {pfx}-hl{i} row highlight.
Ids for lane(pfx, ...): {pfx}-b{i} step box i, {pfx}-end the end marker.
"""
from rules import FACTS                       # course facts (SIM_PATHS)

W, H = 900, 620
CY, RX, RY = 300, 262, 212
CX_RE, CX_CO = 330, 570
# region -> chip slots (centre x, y) inside the region, in SVG pixels
SLOTS = {
    "RE\\R": [(205, 230), (185, 310), (205, 390)],
    "R": [(450, 230), (450, 310), (450, 390)],
    "coRE\\R": [(695, 230), (715, 310), (695, 390)],
    "none": [(150, 565), (750, 565), (450, 548)],
}
REGION_ID = {"RE\\R": "RE", "R": "R", "coRE\\R": "coRE", "none": "none"}


def venn(pfx, items, titles_hidden=False, hidden=True):
    """items: [(key, tex, fact_or_class)] — fact_or_class is a FACTS key (asserted) or a class name for a language
    the script argues itself (e.g. 'R' for the empty language). Chips start hidden."""
    used = {k: 0 for k in SLOTS}
    chips = []
    for key, tex, cls in items:
        cls = FACTS.get(cls, cls)
        assert cls in SLOTS, (key, cls)
        x, y = SLOTS[cls][used[cls]]
        used[cls] += 1
        chips.append(f'<span id="{pfx}-l-{key}" class="vchip{" h" if hidden else ""}" '
                     f'style="left:{x}px;top:{y}px">${tex}$</span>')
    th = " h" if titles_hidden else ""
    ell = (f'<ellipse cx="{CX_RE}" cy="{CY}" rx="{RX}" ry="{RY}"/>', f'<ellipse cx="{CX_CO}" cy="{CY}" rx="{RX}" ry="{RY}"/>')
    svg = (f'<svg class="venn" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
           f'<defs><clipPath id="{pfx}-cco">{ell[1]}</clipPath>'
           f'<mask id="{pfx}-mre"><rect width="{W}" height="{H}" fill="white"/>{ell[1].replace("/>", " fill=\"black\"/>")}</mask>'
           f'<mask id="{pfx}-mco"><rect width="{W}" height="{H}" fill="white"/>{ell[0].replace("/>", " fill=\"black\"/>")}</mask>'
           f'<mask id="{pfx}-mno"><rect width="{W}" height="{H}" fill="white"/>{ell[0].replace("/>", " fill=\"black\"/>")}'
           f'{ell[1].replace("/>", " fill=\"black\"/>")}</mask></defs>'
           f'<rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="22" class="vall"/>'
           f'<g id="{pfx}-f-none" class="h"><rect width="{W}" height="{H}" rx="22" class="vfill" mask="url(#{pfx}-mno)"/></g>'
           f'<g id="{pfx}-f-RE" class="h">{ell[0].replace("/>", f" class=\"vfill\" mask=\"url(#{pfx}-mre)\"/>")}</g>'
           f'<g id="{pfx}-f-coRE" class="h">{ell[1].replace("/>", f" class=\"vfill\" mask=\"url(#{pfx}-mco)\"/>")}</g>'
           f'<g id="{pfx}-f-R" class="h">{ell[0].replace("/>", f" class=\"vfill\" clip-path=\"url(#{pfx}-cco)\"/>")}</g>'
           f'{ell[0].replace("/>", " class=\"vre\"/>")}{ell[1].replace("/>", " class=\"vco\"/>")}</svg>')
    titles = (f'<span id="{pfx}-t-RE" class="vtitle re{th}" style="left:150px;top:62px">$RE$</span>'
              f'<span id="{pfx}-t-coRE" class="vtitle co{th}" style="left:750px;top:62px">$coRE$</span>'
              f'<span id="{pfx}-t-R" class="vtitle r{th}" style="left:450px;top:150px">$R$</span>'
              f'<span id="{pfx}-t-none" class="vtitle no{th}" style="left:450px;top:600px">לא ב-$RE$ ולא ב-$coRE$</span>')
    return f'<div class="vennwrap" id="{pfx}" dir="ltr" style="width:{W}px;height:{H}px">{svg}{titles}{"".join(chips)}</div>'


def table(pfx, head, rows, hide_rows=True, hide_cells=(), cls=""):
    """head: [html]; rows: [[html]]. Rows start hidden (hide_rows) and cells listed in hide_cells [(i, j)] start
    hidden inside a shown row. The first column is the row header (highlight slot {pfx}-hl{i})."""
    hc = set(hide_cells)
    th = "".join(f"<th>{h}</th>" for h in head)
    out = []
    for i, r in enumerate(rows):
        cells = []
        for j, c in enumerate(r):
            inner = f'<span id="{pfx}-c{i}-{j}"{" class=\"h\"" if (i, j) in hc else ""}>{c}</span>'
            if j == 0:
                cells.append(f'<th><i id="{pfx}-hl{i}" class="cell-hi h"></i>{inner}</th>')
            else:
                cells.append(f"<td>{inner}</td>")
        out.append(f'<tr id="{pfx}-r{i}"{" class=\"h\"" if hide_rows else ""}>{"".join(cells)}</tr>')
    return f'<table class="dtab {cls}" id="{pfx}"><thead><tr>{th}</tr></thead><tbody>{"".join(out)}</tbody></table>'


def lane(pfx, label_tex, n, end=None, end_kind="ok", hidden=True):
    """one machine's run as n step boxes and an end marker (end: html or None). Boxes start hidden."""
    h = " h" if hidden else ""
    boxes = "".join(f'<i id="{pfx}-b{i}" class="lbox{h}"></i>' for i in range(n))
    tail = f'<span id="{pfx}-end" class="lend {end_kind} h">{end}</span>' if end else ""
    return (f'<div class="lane" id="{pfx}" dir="ltr"><span class="lname">${label_tex}$</span>'
            f'<span class="lboxes">{boxes}</span>{tail}</div>')
