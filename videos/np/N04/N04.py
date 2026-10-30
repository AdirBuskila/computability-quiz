# -*- coding: utf-8 -*-
"""N04 · רדוקציה פולינומית, NP-קשה ו-NP-שלמה — video script (build: tools/video/vid.py N04).

Source: tools/courses_src/np/N04.js (lesson + goal). Exam anchor: 22A-A-Q12 (SAT-PATH: which argument proves it
NP-complete), which no guided quiz uses.
Not used on purpose: the quiz questions of N04 (22A-C-Q15 and the five original ones: what to check for f, the flow
table question, H_TM, which reduction suffices, NPC vs NP-hard). The anchor's reduction SAT -> SAT-PATH is checked
below on formulas, with a fixed one-edge graph.
"""
import itertools
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_np as g

# ---------------------------------------------------------------- facts (verified)
def has_path(V, E, s, t):
    seen, todo = {s}, [s]
    while todo:
        u = todo.pop()
        for e in E:
            if u in e:
                (w,) = e - {u} or {u}
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
    return t in seen


def sat_path(phi, V, E, s, t):
    return g.satisfiable(phi) and has_path(V, E, s, t)


G0 = (["s", "t"], g.E_(("s", "t")), "s", "t")            # the fixed graph the reduction writes
assert has_path(*G0)


def f(phi):
    return (phi,) + G0


FORMULAS = [
    [(("x1", True), ("x2", False)), (("x1", False),)],
    [(("x1", True),), (("x1", False),)],
    [(("x1", True), ("x2", True), ("x3", True)), (("x1", False), ("x2", False)), (("x3", False),)],
    [(("x1", True), ("x2", True)), (("x1", False), ("x2", True)), (("x1", True), ("x2", False)), (("x1", False), ("x2", False))],
]
for phi in FORMULAS:                                       # phi in SAT  <=>  f(phi) in SAT-PATH
    assert g.satisfiable(phi) == sat_path(*f(phi))
assert {g.satisfiable(p) for p in FORMULAS} == {True, False}   # both yes and no instances were tried

Q = BANK["22A-A-Q12"]
assert Q["correctId"] == "d" and len(Q["options"]) == 5
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

FLOW = '<table class="npt"><thead><tr><th>אם $A \\le_p B$ ו...</th><th>אז</th></tr></thead><tbody>' \
       '<tr id="w-r1" class="h"><td>$B \\in P$</td><td>$A \\in P$</td></tr>' \
       '<tr id="w-r2" class="h"><td>$B \\in NP$</td><td>$A \\in NP$</td></tr>' \
       '<tr id="w-r3" class="h"><td>$A \\notin P$</td><td>$B \\notin P$</td></tr>' \
       '<tr id="w-r4" class="h"><td>$A$ היא $NP$-קשה</td><td>$B$ היא $NP$-קשה</td></tr></tbody></table>'

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר רדוקציה פולינומית, הכלי שבעזרתו מוכיחים קושי."),
    P("נבדיל בין $NP$-קשה ל-$NP$-שלמה, ונבנה את המתכון להוכחת $NP$-שלמות.", hold=0.4),
], stage='<div class="kicker">N04 · P, NP ו-NP-שלמות</div><h1>רדוקציה פולינומית ו-NP-שלמות</h1>'
         '<p>להבין מה זה $\\le_p$, להבדיל בין $NP$-קשה ל-$NP$-שלמה, ולדעת מה צריך להוכיח כדי להראות $NP$-שלמות.</p>',
   layout="title")

defs = Scene("def", "ההגדרה", [
    P("$A \\le_p B$ היא רדוקציית מיפוי, עם דרישה אחת נוספת: $f$ רצה בזמן **פולינומי**.", do=show("d-r"),
      say="רדוקציה פולינומית מאֵיי לבִּי היא רדוקציית מיפוי, עם דרישה אחת נוספת: אֶף רצה בזמן פולינומי."),
    P("אז בודקים שלושה דברים. אחד: $f$ מחושבת על מכונה דטרמיניסטית בזמן פולינומי.", do=show("d-c1"),
      say="אז בודקים שלושה דברים. אחד: אֶף מחושבת על מכונה דטרמיניסטית בזמן פולינומי."),
    P("שתיים: מילה בשפה $A$ עוברת למילה בשפה $B$.", do=show("dr-yes", "d-c2"),
      say="שתיים: מילה בשפה אֵיי עוברת למילה בשפה בִּי."),
    P("ושלוש: מילה שלא ב-$A$ עוברת למילה שלא ב-$B$.", do=show("dr-no", "d-c3"),
      say="ושלוש: מילה שלא באֵיי עוברת למילה שלא בבִּי."),
    P("כל רדוקציה פולינומית היא גם רדוקציית מיפוי, אבל לא להפך.", do=show("d-c4"), hold=0.4),
], stage=f'<div id="d-r" class="h">{g.redux("dr", "$A$", "$B$")}</div>',
   panel=st.card("d-c1", "rule", "1️⃣ $f$ פולינומית")
         + st.card("d-c2", "rule", "2️⃣ $x \\in A \\Rightarrow f(x) \\in B$")
         + st.card("d-c3", "rule", "3️⃣ $x \\notin A \\Rightarrow f(x) \\notin B$")
         + st.card("d-c4", "plain", "$A \\le_p B \\Rightarrow A \\le_m B$, לא להפך"))

flow = Scene("flow", "קלות וקושי", [
    P("מה רדוקציה נותנת? בדיוק כמו ברדוקציות מיפוי: קלות זורמת **שמאלה**, וקושי זורם **ימינה**.", do=show("w-t")),
    P("אם $B$ ב-$P$, מחשבים את $f$ ומריצים את המכריע של $B$. אז גם $A$ ב-$P$.", do=show("w-r1"),
      say="אם בִּי בפִּי, מחשבים את אֶף ומריצים את המכריע של בִּי. אז גם אֵיי בפִּי."),
    P("אותו דבר עם $NP$.", do=show("w-r2"), say="אותו דבר עם אֶן פִּי."),
    P("ובכיוון השני, אם $A$ קשה, גם $B$ קשה. אחרת $A$ הייתה קלה דרכה.", do=show("w-r3", "w-r4"),
      say="ובכיוון השני, אם אֵיי קשה, גם בִּי קשה. אחרת אֵיי הייתה קלה דרכה."),
    P("ועוד דבר: אותה $f$ היא גם רדוקציה בין המשלימים.", do=show("w-c1"), hold=0.4,
      say="ועוד דבר: אותה אֶף היא גם רדוקציה בין המשלימים."),
], stage=f'<div class="stack"><div id="w-t" class="h">{FLOW}</div></div>',
   panel=st.card("w-c1", "rule", "🔑 $A \\le_p B \\iff \\overline{A} \\le_p \\overline{B}$, באותה $f$"))

hard = Scene("hard", "קשה מול שלמה", [
    P("שפה $L$ היא $NP$-**קשה** אם כל שפה ב-$NP$ ניתנת לרדוקציה פולינומית אליה.", do=show("h-1"),
      say="שפה, אֵל, היא אֶן פִּי קשה אם כל שפה באֶן פִּי ניתנת לרדוקציה פולינומית אליה."),
    P("שימו לב: שום דבר לא אומר ש-$L$ עצמה ב-$NP$. היא יכולה להיות אפילו לא כריעה.", do=show("h-c1"),
      say="שימו לב: שום דבר לא אומר שאֵל עצמה באֶן פִּי. היא יכולה להיות אפילו לא כריעה."),
    P("$L$ היא $NP$-**שלמה** אם היא $NP$-קשה, **וגם** שייכת ל-$NP$.", do=show("h-2"),
      say="אֵל היא אֶן פִּי שלמה אם היא אֶן פִּי קשה, וגם שייכת לאֶן פִּי."),
    P("הדוגמה: בעיית העצירה $H_{TM}$ היא $NP$-קשה. כל שפה כריעה מתרדדת אליה בזמן פולינומי.", do=show("h-c2"),
      say="הדוגמה: בעיית העצירה, אֵייץ' טִי אֶם, היא אֶן פִּי קשה. כל שפה כריעה מתרדדת אליה בזמן פולינומי."),
    P("הרדוקציה רק כותבת קוד של מכונה שעוצרת בדיוק על המילים שבשפה, ומעתיקה את הקלט. זמן ליניארי באורך הקלט, כלומר פולינומי.", do=show("h-c3")),
    P("אבל $H_{TM}$ לא כריעה, ולכן לא ב-$NP$. היא קשה, ולא שלמה. בלי קשר לשאלה אם $P = NP$.", do=show("h-c4"), hold=0.4,
      say="אבל אֵייץ' טִי אֶם לא כריעה, ולכן לא באֶן פִּי. היא קשה, ולא שלמה. בלי קשר לשאלה אם פִּי שווה אֶן פִּי."),
], stage='<div class="stack" style="gap:34px">'
         '<div id="h-1" class="bigmath h" style="font-size:42px">$NP$-קשה: $\\forall A \\in NP:\\ A \\le_p L$</div>'
         '<div id="h-2" class="bigmath h" style="font-size:42px">$NP$-שלמה: $NP$-קשה $+$ $L \\in NP$</div></div>',
   panel=st.card("h-c1", "trap", "⚠️ $NP$-קשה לא אומר $L \\in NP$, ולא אפילו $L \\in R$")
         + st.card("h-c2", "ex", "$H_{TM}$ היא $NP$-קשה")
         + st.card("h-c3", "plain", "$f$ כותבת קוד: זמן פולינומי")
         + st.card("h-c4", "rule", "🔑 $H_{TM} \\notin R$, לכן לא $NP$-שלמה"))

recipe = Scene("recipe", "המתכון", [
    P("איך מוכיחים ש-$L$ היא $NP$-שלמה? שני שלבים.", say="איך מוכיחים שאֵל היא אֶן פִּי שלמה? שני שלבים."),
    P("שלב ראשון: $L$ ב-$NP$. עד ומוודא, כמו שלמדנו.", do=show("c-1"), say="שלב ראשון: אֵל באֶן פִּי. עד ומוודא, כמו שלמדנו."),
    P("שלב שני: רדוקציה פולינומית **מ**שפה $NP$-שלמה ידועה, **אל** $L$.", do=show("c-2", "c-r"),
      say="שלב שני: רדוקציה פולינומית משפה אֶן פִּי שלמה ידועה, אל אֵל."),
    P("הכיוון קריטי. רדוקציה מ-$L$ אל $SAT$ מראה ש-$L$ **קלה** כמו $SAT$, לא קשה.", do=show("c-t1"),
      say="הכיוון קריטי. רדוקציה מאֵל אל סַאט מראה שאֵל קלה כמו סַאט, לא קשה."),
    P("ועוד מלכודת: רדוקציה **מ**שפה ב-$P$ לא מלמדת כלום. לכל שפה לא טריוויאלית יש כזו.", do=show("c-t2"),
      say="ועוד מלכודת: רדוקציה משפה בפִּי לא מלמדת כלום. לכל שפה לא טריוויאלית יש כזו."),
    P("והפוך: כל שפה ב-$NP$ מתרדדת לכל שפה $NP$-שלמה. זו ההגדרה, אז רדוקציה כזו קיימת תמיד.", do=show("c-t3"), hold=0.4,
      say="והפוך: כל שפה באֶן פִּי מתרדדת לכל שפה אֶן פִּי שלמה. זו ההגדרה, אז רדוקציה כזו קיימת תמיד."),
], stage='<div class="stack" style="gap:34px">'
         '<div id="c-1" class="card rule h" style="font-size:36px">1️⃣ $L \\in NP$</div>'
         '<div id="c-2" class="card rule h" style="font-size:36px">2️⃣ $NP$-שלמה ידועה $\\le_p L$</div>'
         f'<div id="c-r" class="h">{g.redux("cr", "$3SAT$", "$L$")}</div></div>',
   panel=st.card("c-t1", "trap", "⚠️ $L \\le_p SAT$: הכיוון ההפוך, מוכיח קלות")
         + st.card("c-t2", "trap", "⚠️ מ-$P$ אל $L$: תמיד קיימת, לא מוכיחה כלום")
         + st.card("c-t3", "plain", "$A \\in NP$, $C$ שלמה ← $A \\le_p C$ תמיד"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: שפת הזוגות של נוסחה ספיקה, וגרף שיש בו מסלול מ-$s$ ל-$t$. איזה טיעון מוכיח שהיא $NP$-שלמה?",
      say="שאלה ממבחן: שפת הזוגות של נוסחה ספיקה, וגרף שיש בו מסלול מאֶס לטִי. איזה טיעון מוכיח שהיא אֶן פִּי שלמה?"),
    P("קודם, השפה ב-$NP$: העד הוא השמה מספקת וגם מסלול, ושניהם נבדקים מהר.", do=show("q-x-a", "q-n-a"),
      say="קודם, השפה באֶן פִּי: העד הוא השמה מספקת וגם מסלול, ושניהם נבדקים מהר."),
    P("רדוקציה מ-$PATH$ לא עוזרת: $PATH$ ב-$P$, ומשפה ב-$P$ יש רדוקציה לכל שפה לא טריוויאלית.", do=show("q-x-b", "q-n-b"),
      say="רדוקציה מפַּאת' לא עוזרת: פַּאת' בפִּי, ומשפה בפִּי יש רדוקציה לכל שפה לא טריוויאלית."),
    P("רדוקציה אל $H_{TM}$ היא בכיוון ההפוך: היא מראה קלות, לא קושי.", do=show("q-x-c", "q-n-c"),
      say="רדוקציה אל אֵייץ' טִי אֶם היא בכיוון ההפוך: היא מראה קלות, לא קושי."),
    P("והטיעון הנכון: $SAT$ מתרדדת אליה. הנוסחה עוברת כמו שהיא, יחד עם גרף קבוע של צלע אחת מ-$s$ ל-$t$.", do=show("x-1"),
      say="והטיעון הנכון: סַאט מתרדדת אליה. הנוסחה עוברת כמו שהיא, יחד עם גרף קבוע של צלע אחת מאֶס לטִי."),
    P("המסלול תמיד קיים, אז הזוג בשפה בדיוק כשהנוסחה ספיקה. והבנייה מיידית.", do=show("q-ok-d"), hold=0.3),
    P("והטענה ש״לא ידוע, כי לא ידוע אם $P = NP$״: $NP$-שלמות מוכחת בלי לדעת את זה.", do=show("q-x-e"), hold=0.6,
      say="והטענה שלא ידוע, כי לא ידוע אם פִּי שווה אֶן פִּי: אֶן פִּי שלמות מוכחת בלי לדעת את זה."),
], stage='<div class="stack" style="gap:44px">'
         f'<div class="qstem"><span class="qid">{Q["id"]}</span>$SAT\\text{{-}}PATH$: '
         'נוסחת CNF ספיקה <b>וגם</b> גרף לא מכוון עם מסלול מ-$s$ ל-$t$. איזו טענה נכונה?</div>'
         '<div id="x-1" class="stack h" style="gap:12px"><div class="bigmath" style="font-size:40px">'
         '$\\varphi \\mapsto \\langle \\varphi, G_0, s, t \\rangle$</div>'
         '<div class="hint">$G_0$: צלע אחת בין $s$ ל-$t$</div></div></div>',
   panel='<div class="optsm">'
         + st.options("q", OPTS, notes={"a": "עד: השמה + מסלול", "b": "PATH ∈ P", "c": "כיוון הפוך"}) + '</div>')

recap = Scene("recap", "סיכום", [
    P("לסיכום: רדוקציה פולינומית היא $f$ פולינומית ששומרת על ״כן״ ועל ״לא״.", do=show("r-1"),
      say="לסיכום: רדוקציה פולינומית היא אֶף פולינומית ששומרת על כן ועל לא."),
    P("קלות זורמת שמאלה, קושי זורם ימינה.", do=show("r-2")),
    P("$NP$-שלמה היא $NP$-קשה שגם שייכת ל-$NP$.", do=show("r-3"), say="אֶן פִּי שלמה היא אֶן פִּי קשה שגם שייכת לאֶן פִּי."),
    P("ולהוכחה: $L$ ב-$NP$, ורדוקציה **מ**שפה שלמה ידועה **אל** $L$. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6,
      say="ולהוכחה: אֵל באֶן פִּי, ורדוקציה משפה שלמה ידועה אל אֵל. נתראה ברמה הבאה."),
], stage='<div class="stack"><div class="bigmath">$A \\le_p B$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $f$ פולינומית, ״כן״ ← ״כן״, ״לא״ ← ״לא״")
         + st.card("r-2", "rule", "🔑 קלות שמאלה, קושי ימינה")
         + st.card("r-3", "rule", "🔑 שלמה = קשה + ב-$NP$")
         + st.card("r-4", "trap", "⚠️ הכיוון: מהשלמה הידועה אל $L$"))

VIDEO = Video("N04", "np", "רדוקציה פולינומית ו-NP-שלמות", [title, defs, flow, hard, recipe, exam, recap],
              bank={"22A-A-Q12": "d"})
