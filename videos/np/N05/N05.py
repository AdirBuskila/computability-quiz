# -*- coding: utf-8 -*-
"""N05 · הרדוקציות הקלאסיות — video script (build: tools/video/vid.py N05).

Source: tools/courses_src/np/N05.js (lesson + goal). Exam anchor: SAMP-2-Q6 (CLIQUE <=p A implies IS <=p A?), which
no guided quiz uses.
Not used on purpose: the quiz questions of N05 (23S-A-Q20 and the five original ones: which f for CLIQUE->IS and
IS->VC, the edge counts of the 3SAT gadgets for the quiz's formula, the 2-literal unsatisfiable formula). The
gadget here is built for a different formula and no edge count is stated.
"""
import itertools, random
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_np as g

# ---------------------------------------------------------------- facts (verified)
V = ["1", "2", "3", "4", "5"]
E = g.E_(("1", "2"), ("1", "3"), ("2", "3"), ("3", "4"), ("4", "5"))
EC = g.complement(V, E)
S = ["1", "2", "3"]
assert g.is_clique(E, S) and g.is_indep(EC, S) and not g.has(V, E, 4, g.is_clique)
# CLIQUE <-> IS by the complement graph, IS -> VC by n - k, on every graph with up to 5 vertices
for n in range(1, 6):
    Vn = [str(i) for i in range(n)]
    pairs = list(itertools.combinations(Vn, 2))
    for bits in range(1 << len(pairs)):
        En = frozenset(frozenset(p) for i, p in enumerate(pairs) if bits >> i & 1)
        Cn = g.complement(Vn, En)
        for k in range(n + 1):
            assert g.has(Vn, En, k, g.is_clique) == g.has(Vn, Cn, k, g.is_indep)
            assert g.has(Vn, En, k, g.is_indep) == g.has(Vn, En, n - k, g.is_cover)
# the IS of the example and its complement as a cover (in G itself)
IS_G = ["1", "4"]
VC_G = [v for v in V if v not in IS_G]
assert g.is_indep(E, IS_G) and g.is_cover(E, VC_G) and len(VC_G) == len(V) - len(IS_G)

# 3SAT -> IS: the gadget for PHI, and the iff on random 3CNF formulas
PHI = [(("x1", True), ("x2", False), ("x3", True)), (("x1", False), ("x2", True), ("x3", True)),
       (("x1", True), ("x2", True), ("x3", False))]
GV, GE = g.sat_to_is(PHI)
PICK = [(0, 0), (1, 2), (2, 0)]                    # x1 from clause 1, x3 from clause 2, x1 from clause 3
assert g.is_indep(GE, PICK) and len(PICK) == len(PHI)
A = {"x1": True, "x2": False, "x3": True}           # the assignment the pick defines (x2 free; set false)
assert g.satisfies(PHI, A)
rng = random.Random(5)
for _ in range(400):
    m = rng.randint(1, 4)
    phi = [tuple((f"x{rng.randint(1, 3)}", rng.random() < .5) for _ in range(3)) for _ in range(m)]
    gv, ge = g.sat_to_is(phi)
    assert g.satisfiable(phi) == g.has(gv, ge, m, g.is_indep)

Q = BANK["SAMP-2-Q6"]
assert Q["correctId"] == "a"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

POS = {"1": (130, 120), "2": (360, 90), "3": (250, 300), "4": (120, 470), "5": (380, 480)}
G1 = g.graph_svg("g1", V, E, POS, w=500, h=560, scale=0.92)
G2 = g.graph_svg("g2", V, EC, POS, w=500, h=560, scale=0.92, alt=EC)

# gadget layout: one triangle per clause
TP = {}
for i, cx in enumerate((170, 500, 830)):
    TP[(i, 0)] = (cx, 70)
    TP[(i, 1)] = (cx - 110, 270)
    TP[(i, 2)] = (cx + 110, 270)
NAMES = {(i, j): ("" if l[1] else "¬") + l[0] for i, c in enumerate(PHI) for j, l in enumerate(c)}
TRI = {e for e in GE if len({u[0] for u in e}) == 1}
CON = GE - TRI
GS = g.graph_svg("gs", GV, GE, TP, names=NAMES, w=1000, h=600, hidden=GE, alt=CON, r=40, scale=1.0, bend=0.36)
assert len(TRI) == 9


def edge_ids(pfx, es, Vord):
    return [g.eid(pfx, *sorted(e, key=Vord.index), Vord) for e in es]


# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נראה את הרדוקציות הקלאסיות בין בעיות גרפים, ואת הרדוקציה מ-$3SAT$.",
      say="בסרטון הזה נראה את הרדוקציות הקלאסיות בין בעיות גרפים, ואת הרדוקציה משָׁלוֹשׁ סַאט."),
    P("אלה אבני הבניין של כמעט כל הוכחת $NP$-שלמות במבחן.", hold=0.4),
], stage='<div class="kicker">N05 · P, NP ו-NP-שלמות</div><h1>הרדוקציות הקלאסיות</h1>'
         '<p>$CLIQUE$, $IS$ ו-$VC$ זו לזו, ו-$3SAT$ אל $IS$: מה $f$ בונה, ולמה היא שומרת על ״כן״ ועל ״לא״.</p>',
   layout="title")

comp = Scene("comp", "גרף משלים", [
    P("קליקה: קבוצת קודקודים שכולם מחוברים. קבוצה בלתי תלויה: קבוצה שאף שניים בה לא מחוברים.", do=show("p-g1")),
    P("בגרף הזה, אחת, שתיים ושלוש הם קליקה.", do=show(*g.hv("g1", *S)) + show(*[g.heid("g1", a, b, V) for a, b in itertools.combinations(S, 2)])),
    P("עכשיו נבנה את **הגרף המשלים**: אותם קודקודים, וצלע בדיוק איפה שלא הייתה צלע.", do=show("p-g2", "c-c1")),
    P("והקליקה הפכה לקבוצה בלתי תלויה: אף צלע ביניהם.", do=show(*g.hv("g2", *S))),
    P("וזה עובד לכל קבוצה: קליקה בגרף היא בדיוק קבוצה בלתי תלויה במשלים שלו, באותו גודל.", do=show("c-c2")),
    P("ואותה פונקציה עובדת גם בכיוון ההפוך. בניית המשלים לוקחת זמן ריבועי במספר הקודקודים.", do=show("c-c3"), hold=0.4),
], stage=f'<div style="display:flex;gap:30px;align-items:center;justify-content:center">'
         f'<div id="p-g1" class="h">{G1}<div class="hint" style="text-align:center">$G$</div></div>'
         f'<div id="p-g2" class="h">{G2}<div class="hint" style="text-align:center">$\\overline{{G}}$</div></div></div>',
   panel=st.card("c-c1", "plain", "$\\overline{G}$: צלע בדיוק היכן שאין ב-$G$")
         + st.card("c-c2", "rule", "🔑 $S$ קליקה ב-$G$ $\\iff$ $S$ בלתי תלויה ב-$\\overline{G}$")
         + st.card("c-c3", "ex", "$CLIQUE \\le_p IS$ וגם $IS \\le_p CLIQUE$"))

cover = Scene("cover", "כיסוי קודקודים", [
    P("כיסוי קודקודים: קבוצה שנוגעת בכל צלע.", do=show("v-g")),
    P("קחו קבוצה בלתי תלויה, כאן אחת וארבע.", do=show(*g.hv("g1b", *IS_G), "v-c1")),
    P("כל צלע יוצאת מקודקוד שמחוץ לקבוצה, כי בתוך הקבוצה אין צלעות.", do=show("v-c2")),
    P("אז שאר הקודקודים, שתיים, שלוש וחמש, נוגעים בכל צלע. זה כיסוי.",
      do=hide(*g.hv("g1b", *IS_G)) + show(*g.hv("g1b", *VC_G), *[g.heid("g1b", *sorted(e, key=V.index), V) for e in E])),
    P("וגם להפך: מה שנשאר מחוץ לכיסוי הוא קבוצה בלתי תלויה. הגדלים של שתיהן מסתכמים במספר הקודקודים.", do=show("v-c3")),
    P("אז כשעוברים בין שתי הבעיות, חייבים לתרגם גם את הגודל המבוקש. טעות בפרמטר שוברת את הרדוקציה.", do=show("v-c4"), hold=0.4),
], stage=f'<div id="v-g" class="h">{g.graph_svg("g1b", V, E, POS, w=500, h=560, scale=1.15)}</div>',
   panel=st.card("v-c1", "plain", "קבוצה בלתי תלויה: $\\{1, 4\\}$")
         + st.card("v-c2", "ex", "כל צלע נוגעת בקודקוד מחוץ לקבוצה")
         + st.card("v-c3", "rule", "🔑 $S$ בלתי תלויה $\\iff$ $V \\setminus S$ כיסוי")
         + st.card("v-c4", "trap", "⚠️ לבדוק תמיד מה קורה לגודל המבוקש"))

TRI_IDS = edge_ids("gs", TRI, GV)
CON_IDS = edge_ids("gs", CON, GV)
gadget = Scene("gadget", "מ-3SAT אל IS", [
    P("ועכשיו הרדוקציה החשובה מכולן: מנוסחת $3SAT$ לגרף.", do=show("s-f"),
      say="ועכשיו הרדוקציה החשובה מכולן: מנוסחת שָׁלוֹשׁ סַאט לגרף."),
    P("לכל **מופע** של ליטרל בנוסחה יש קודקוד. שלוש פסוקיות, אז תשעה קודקודים.", do=show("s-g")),
    P("כל שלושה קודקודים מאותה פסוקית מחוברים במשולש. כך בוחרים לכל היותר ליטרל אחד מכל פסוקית.",
      do=show(*TRI_IDS, "s-c1")),
    P("ומחברים כל שני ליטרלים **סותרים**, כמו $x_1$ ו״לא $x_1$״. כך אי אפשר לבחור את שניהם.", do=show(*CON_IDS, "s-c2"),
      say="ומחברים כל שני ליטרלים סותרים, כמו אִקְס אחת ולא אִקְס אחת. כך אי אפשר לבחור את שניהם."),
    P("המספר המבוקש הוא מספר הפסוקיות, כאן שלוש.", do=show("s-c3")),
    P("קבוצה בלתי תלויה בגודל שלוש: $x_1$ מהראשונה, $x_3$ מהשנייה, ו-$x_1$ מהשלישית.", do=show(*g.hv("gs", *PICK)),
      say="קבוצה בלתי תלויה בגודל שלוש: אִקְס אחת מהראשונה, אִקְס שלוש מהשנייה, ואִקְס אחת מהשלישית."),
    P("אין ביניהם סתירה, אז הם מגדירים השמה: $x_1$ ו-$x_3$ אמת. והיא מספקת את כל הפסוקיות.", do=show("s-c4"),
      say="אין ביניהם סתירה, אז הם מגדירים השמה: אִקְס אחת ואִקְס שלוש אמת. והיא מספקת את כל הפסוקיות."),
    P("ולהפך: השמה מספקת נותנת ליטרל אמת אחד מכל פסוקית, ואלה לא סותרים. זו קבוצה בלתי תלויה.", hold=0.4),
], stage=f'<div class="stack" style="gap:16px"><div id="s-f" class="npf h">${g.cnf_tex(PHI)}$</div>'
         f'<div id="s-g" class="h">{GS}</div></div>',
   panel=st.card("s-c1", "plain", "משולש בכל פסוקית: ליטרל אחד לכל היותר")
         + st.card("s-c2", "plain", "צלע בין $x$ ל-$\\lnot x$: אין סתירה")
         + st.card("s-c3", "rule", "🔑 $\\varphi \\mapsto \\langle G_\\varphi, m \\rangle$, $m$ = מספר הפסוקיות")
         + st.card("s-c4", "ex", "$x_1 = T,\\ x_3 = T$ מספקת את $\\varphi$"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: נתון ש-$CLIQUE$ מתרדדת פולינומית לשפה $A$. האם בהכרח גם $IS$ מתרדדת ל-$A$?",
      say="שאלה ממבחן: נתון שקְלִיק מתרדדת פולינומית לשפה אֵיי. האם בהכרח גם אַיי אֶס מתרדדת לאֵיי?"),
    P("לא צריך לבנות רדוקציה חדשה. יש לנו כבר רדוקציה מ-$IS$ ל-$CLIQUE$: הגרף המשלים.", do=show("x-1"),
      say="לא צריך לבנות רדוקציה חדשה. יש לנו כבר רדוקציה מאַיי אֶס לקְלִיק: הגרף המשלים."),
    P("ורדוקציות פולינומיות מתחברות: קודם $f$, ואחר כך הרדוקציה הנתונה. הרכבה של פולינומים היא פולינום.", do=show("x-2")),
    P("אז כן, $IS$ מתרדדת ל-$A$. הטענה נכונה.", do=show("q-ok-a", "q-x-b"), hold=0.6,
      say="אז כן, אַיי אֶס מתרדדת לאֵיי. הטענה נכונה."),
], stage='<div class="stack" style="gap:34px">'
         '<div id="x-1" class="bigmath h" style="font-size:44px">$IS \\le_p CLIQUE$</div>'
         '<div id="x-2" class="bigmath h" style="font-size:44px">$IS \\le_p CLIQUE \\le_p A$</div></div>',
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>תהא $A$ שפה כך ש-$CLIQUE \\le_p A$. '
         'אזי $IS \\le_p A$.</div>' + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: קליקה בגרף היא קבוצה בלתי תלויה בגרף המשלים.", do=show("r-1")),
    P("והמשלים של קבוצה בלתי תלויה הוא כיסוי קודקודים.", do=show("r-2")),
    P("מ-$3SAT$: קודקוד לכל מופע, משולשים בפסוקיות, צלעות בין סותרים, ו-$k$ שווה למספר הפסוקיות.", do=show("r-3"),
      say="משָׁלוֹשׁ סַאט: קודקוד לכל מופע, משולשים בפסוקיות, צלעות בין סותרים, וקֵיי שווה למספר הפסוקיות."),
    P("ורדוקציות מתחברות זו לזו. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$3SAT \\le_p IS \\le_p CLIQUE$</div>'
         '<div class="bigmath">$IS \\le_p VC$</div></div>',
   panel=st.card("r-1", "rule", "🔑 קליקה ב-$G$ = בלתי תלויה ב-$\\overline{G}$")
         + st.card("r-2", "rule", "🔑 בלתי תלויה $S$ ← כיסוי $V \\setminus S$")
         + st.card("r-3", "rule", "🔑 $\\varphi \\mapsto \\langle G_\\varphi, m \\rangle$")
         + st.card("r-4", "plain", "$\\le_p$ טרנזיטיבית"))

VIDEO = Video("N05", "np", "הרדוקציות הקלאסיות", [title, comp, cover, gadget, exam, recap],
              bank={"SAMP-2-Q6": "a"})
