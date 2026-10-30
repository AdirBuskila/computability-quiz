# -*- coding: utf-8 -*-
"""M03 · מה מוכיחים ברדוקציה, ואילו רדוקציות לא קיימות — video script (build: tools/video/vid.py M03).

Source: tools/courses_src/map/M03.js (lesson + goal). Exam anchor: 26B-B-Q1 (I: co-ALL_TM <=m co-EQ_TM holds;
II: H_10 <=m co-A_TM cannot exist), which no guided quiz uses. Not used on purpose: the five original quiz questions
of M03 (the impossible pairs H_TM->E_TM and EQ_TM->A_TM are not shown, and the L <=m co-L rule is left to the quiz)
and 22A-A-Q10 (the M03 quiz).
Every arrow of the class picture is judged by the course checker's monotonicity rule (map/check.py impossible()) on
the course facts (rules.FACTS), and the allowed ones are reductions the course lists or "decidable to anything".
"""
from vid import P, Scene, Video, show, hide, BANK
from rules import FACTS, rule
import stage as st
import w_map

FL = {"R": {"R", "RE", "coRE"}, "RE\\R": {"RE"}, "coRE\\R": {"coRE"}, "none": set()}


def impossible(src, dst):
    """map/check.py: a class the target is in and the source is not"""
    fs, fd = FL[FACTS[src]], FL[FACTS[dst]]
    return any(g in fd and g not in fs for g in ("R", "RE", "coRE"))


LANGS = [("A_TM", "A_TM", "RE\\R", 0, -70), ("H_TM", "H_TM", "RE\\R", 0, 70), ("coA_TM", "co:A_TM", "coRE\\R", 0, -20),
         ("A_DFA", "A_DFA", "R", 0, 160), ("ALL_TM", "ALL_TM", "none", -300, 0)]
for k, _, region, _, _ in LANGS:
    assert FACTS[k] == region, k
ARROWS = [("ALL_TM", "H_TM", "bad", 0.25), ("coA_TM", "H_TM", "bad", -0.12), ("H_TM", "coA_TM", "bad", -0.12),
          ("A_DFA", "A_TM", "ok", 0.0), ("A_TM", "ALL_TM", "ok", 0.3)]
for s, d, kind, _ in ARROWS:
    assert impossible(s, d) == (kind == "bad"), (s, d)
assert rule("red.R_to_any_nontrivial") and rule("red.RE_RE_to_coRE") is False
assert ("A_TM", "ALL_TM") in {("A_TM", "ALL_TM"), ("H_TM", "ALL_TM")}            # listed in map/check.py KNOWN
VENN = w_map.venn("v", LANGS, ARROWS)

# exam 26B-B-Q1: I holds (ALL_TM <=m EQ_TM, complemented), II is impossible (H_10 in RE\R, co-A_TM in coRE\R)
assert not impossible("coALL_TM", "coEQ_TM") and impossible("H10", "coA_TM")
assert rule("red.complement_same_f")
Q = BANK["26B-B-Q1"]
assert Q["correctId"] == "c"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

PROVE = [
    ("$L \\notin R$", "$A_{TM} \\le_m L$"),
    ("$L \\notin RE$", "$\\overline{A_{TM}} \\le_m L$"),
    ("$L \\notin coRE$", "$A_{TM} \\le_m L$"),
]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נלמד לבחור את כיוון הרדוקציה כדי להוכיח שפה קשה."),
    P("ונלמד לזהות רדוקציה שפשוט לא יכולה להתקיים.", hold=0.4),
], stage='<div class="kicker">M03 · רדוקציות מיפוי</div><h1>מה מוכיחים ברדוקציה</h1>'
         '<p>לבחור את הכיוון הנכון כדי להוכיח ש-$L$ לא כריעה או לא ניתנת לקבלה, ולזהות רדוקציה שאי אפשר שתתקיים.</p>',
   layout="title")

prove = Scene("prove", "הכיוון", [
    P("נזכור: קושי זורם מהמקור אל היעד.", do=show("p-m")),
    P("לכן כדי להוכיח ש-$L$ קשה, מרדדים **אל** $L$, משפה שכבר ידוע שהיא קשה."),
    P("כדי להוכיח ש-$L$ לא כריעה: מרדדים את $A_{TM}$ אל $L$.", do=show("t-0")),
    P("כדי להוכיח ש-$L$ לא ניתנת לקבלה: מרדדים את המשלים של $A_{TM}$ אל $L$, כי הוא לא ב-$RE$.", do=show("t-1")),
    P("ואותה רדוקציה מ-$A_{TM}$ נותנת גם ש-$L$ לא ב-$coRE$.", do=show("t-2")),
    P("למה? כי היא נותנת רדוקציה בין המשלימים: המשלים של $A_{TM}$ אל המשלים של $L$.", do=show("p-c1")),
    P("והמשלים של $A_{TM}$ לא ב-$RE$. לכן גם המשלים של $L$ לא ב-$RE$, כלומר $L$ לא ב-$coRE$.", hold=0.4),
    P("המלכודת: רדוקציה **מ**-$L$ אל $A_{TM}$ לא מוכיחה שום קושי.", do=show("p-c2")),
    P("היא מוכיחה רק ש-$L$ ניתנת לקבלה, כי קלות זורמת חזרה אל המקור.", hold=0.5),
], stage='<div class="stack"><div id="p-m" class="bigmath h">$\\text{known} \\le_m L$</div>'
         + st.card("p-c1", "ex", "$\\overline{A_{TM}} \\le_m \\overline{L}$, ולכן $\\overline{L} \\notin RE$")
         + st.card("p-c2", "trap", "⚠️ $L \\le_m A_{TM}$ מוכיחה רק $L \\in RE$") + "</div>",
   panel='<div class="hint">רוצים להוכיח &larr; מרדדים</div>' + w_map.rows("t", PROVE))

venn = Scene("venn", "רדוקציה שלא קיימת", [
    P("עכשיו הצד השני: יש רדוקציות שלא יכולות להתקיים בכלל. נסדר כמה שפות לפי המחלקות.", hold=0.2),
    P("$A_{TM}$ ו-$H_{TM}$: ניתנות לקבלה, ולא כריעות.", do=show("v-n-A_TM", "v-n-H_TM")),
    P("המשלים של $A_{TM}$: ב-$coRE$, ולא ב-$RE$.", do=show("v-n-coA_TM")),
    P("$A_{DFA}$ כריעה, ולכן היא בחיתוך.", do=show("v-n-A_DFA")),
    P("ו-$ALL_{TM}$ לא בשום מחלקה מהשלוש.", do=show("v-n-ALL_TM"), hold=0.3),
    P("הכלל: אם היעד ב-$RE$, גם המקור חייב להיות ב-$RE$. וכך גם עם $coRE$ ועם $R$.", do=show("v-c1")),
    P("$ALL_{TM}$ אל $H_{TM}$? היעד ב-$RE$, והמקור לא. אין רדוקציה כזו.",
      do=show("v-a-ALL_TM-H_TM", "v-x-ALL_TM-H_TM"),
      say="אוֹל טִי אֶם אל אֵייץ' טִי אֶם? היעד באָר אִי, והמקור לא. אין רדוקציה כזו."),
    P("ומהמשלים של $A_{TM}$ אל $H_{TM}$? אותה סיבה בדיוק.", do=show("v-a-coA_TM-H_TM", "v-x-coA_TM-H_TM")),
    P("ובכיוון ההפוך? היעד ב-$coRE$, ו-$H_{TM}$ לא. גם בלתי אפשרי.",
      do=show("v-a-H_TM-coA_TM", "v-x-H_TM-coA_TM")),
    P("בין שפה ב-$RE$ פחות $R$ לשפה ב-$coRE$ פחות $R$ אין רדוקציה, **באף כיוון**.", do=show("v-c2"), hold=0.4),
    P("לעומת זאת, $A_{DFA}$ כריעה מתרדדת לכל שפה לא טריוויאלית. מכריעים, ומחזירים מילה קבועה.",
      do=show("v-a-A_DFA-A_TM")),
    P("ו-$A_{TM}$ אל $ALL_{TM}$? כאן אין מניעה מצד המחלקות: היעד לא נמצא באף מחלקה שהמקור חסר.",
      do=show("v-a-A_TM-ALL_TM")),
    P("אבל זה רק תנאי הכרחי, לא הוכחה. הרדוקציה הזו באמת קיימת, ונבנה אותה ברמה הבאה עם $K_{M,w}$.",
      do=show("v-c3"), hold=0.5),
], stage=VENN,
   panel=st.card("v-c1", "rule", "🔑 היעד ב-$RE$? אז גם המקור. כך גם $coRE$ ו-$R$")
         + st.card("v-c2", "trap", "⚠️ בין $RE \\setminus R$ ל-$coRE \\setminus R$: אין רדוקציה באף כיוון")
         + st.card("v-c3", "ex", "מחלקות מתאימות: תנאי <b>הכרחי</b> בלבד. את הרדוקציה עצמה צריך לבנות"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: שתי טענות. נבדוק כל אחת בנפרד."),
    P("טענה ראשונה: המשלים של $ALL_{TM}$ ניתן לרדוקציה אל המשלים של $EQ_{TM}$.", do=show("e-1")),
    P("ידוע ש-$ALL_{TM} \\le_m EQ_{TM}$: משווים את המכונה למכונה שמקבלת הכול.", do=show("e-1b")),
    P("ורדוקציה עוברת למשלימים באותה פונקציה. אז טענה ראשונה נכונה.", do=show("e-ok1"), hold=0.3),
    P("טענה שנייה: $H_{10}$ אל המשלים של $A_{TM}$.", do=show("e-2"),
      say="טענה שנייה: אֵייץ' עשר אל המשלים של אֵיי טִי אֶם."),
    P("$H_{10}$ היא הבעיה העשירית של הילברט: האם לפולינום יש שורש שלם. היא ב-$RE$, ולא כריעה.", do=show("e-2b"),
      say="אֵייץ' עשר היא הבעיה העשירית של הילברט: האם לפולינום יש שורש שלם. היא באָר אִי, ולא כריעה."),
    P("והמשלים של $A_{TM}$ ב-$coRE$, ולא כריעה. זה בדיוק הזוג שאין ביניהם רדוקציה.", do=show("e-x2"), hold=0.3),
    P("אז הראשונה נכונה והשנייה לא.", do=show("q-ok-c", "q-x-a", "q-x-b", "q-x-d"), hold=0.5),
    P("שימו לב: לא היינו צריכים לדעת שום דבר על $H_{10}$ חוץ מהמחלקה שלה.", do=show("e-t"),
      say="שימו לב: לא היינו צריכים לדעת שום דבר על אֵייץ' עשר חוץ מהמחלקה שלה."),
], stage='<div class="stack">'
         '<div id="e-1" class="bigmath h" style="font-size:44px">I. $\\overline{ALL_{TM}} \\le_m \\overline{EQ_{TM}}$ '
         '<span id="e-ok1" class="h" style="color:var(--ok)">✓</span></div>'
         + st.card("e-1b", "ex", "$ALL_{TM} \\le_m EQ_{TM}$, ואותה $f$ למשלימים")
         + '<div id="e-2" class="bigmath h" style="font-size:44px">II. $H_{10} \\le_m \\overline{A_{TM}}$ '
         '<span id="e-x2" class="h" style="color:var(--bad)">✗</span></div>'
         + st.card("e-2b", "ex", "$H_{10} \\in RE \\setminus R$, $\\overline{A_{TM}} \\in coRE \\setminus R$")
         + st.card("e-t", "rule", "🔑 מספיק לדעת את המחלקות") + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>I. $\\overline{{ALL_{{TM}}}} \\le_m \\overline{{EQ_{{TM}}}}$'
         '<br>II. $H_{10} \\le_m \\overline{A_{TM}}$<br>איזה סעיף נכון?</div>'
         + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: כדי להוכיח קושי, מרדדים **אל** השפה החדשה, משפה קשה ידועה.", do=show("r-1")),
    P("$A_{TM}$ אל $L$ נותנת: לא כריעה, ולא ב-$coRE$. המשלים של $A_{TM}$ אל $L$ נותן: לא ב-$RE$.", do=show("r-2")),
    P("רדוקציה לא יכולה להוציא שפה ממחלקה שהיעד שלה נמצא בה.", do=show("r-3")),
    P("ובפרט, בין $RE$ פחות $R$ ל-$coRE$ פחות $R$ אין רדוקציה באף כיוון. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$\\text{known} \\le_m L$</div></div>',
   panel=st.card("r-1", "rule", "🔑 קושי: מרדדים <b>אל</b> $L$")
         + st.card("r-2", "rule", "🔑 $A_{TM} \\le_m L$: $L \\notin R$, $L \\notin coRE$")
         + st.card("r-3", "rule", "🔑 היעד במחלקה? אז גם המקור")
         + st.card("r-4", "trap", "⚠️ $RE \\setminus R$ ו-$coRE \\setminus R$: אין רדוקציה"))

VIDEO = Video("M03", "map", "מה מוכיחים ברדוקציה, ואילו רדוקציות לא קיימות", [title, prove, venn, exam, recap],
              bank={"26B-B-Q1": "c"})
