# -*- coding: utf-8 -*-
"""M02 · לאן זורמות קלות וקושי — video script (build: tools/video/vid.py M02).

Source: tools/courses_src/map/M02.js (lesson + goal). Exam anchor: 25B-B-Q1 (A <=m B between non-trivial languages:
B in RE ∪ coRE gives A in RE ∪ coRE), which no guided quiz uses. Not used on purpose: the five original quiz
questions of M02 (they ask the rules one by one; the video teaches the rules, never in that question form) and
25S-B-Q1 (the M02 quiz).
Every rule the video states is checked against the rule table of the course checker (tools/verify/needhelp/rules.py).
"""
from vid import P, Scene, Video, show, hide, BANK
from rules import rule
import stage as st
import w_map

# the rules the narration states, as the course checker knows them
for rid, truth in [("red.R_down", True), ("red.RE_down", True), ("red.coRE_down", True), ("red.notR_flows", True),
                   ("red.notRE_flows", True), ("red.notcoRE_flows", True), ("red.R_up", False),
                   ("red.complement_same_f", True), ("red.transitive", True), ("red.symmetric", False),
                   ("red.coRE_down_to_RE", False)]:
    assert rule(rid) is truth, rid

# the counterexample picture: A = ∅ maps everything to one fixed word outside B = A_TM
ZERO = w_map.bridge("z", [("0", "0", False), ("1", "1", False), ("01", "01", False)],
                    [("y", "y₀", False)], [("0", "y", "ok"), ("1", "y", "ok"), ("01", "y", "ok")], A="∅", B="A_TM")

Q = BANK["25B-B-Q1"]
assert Q["correctId"] == "a"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

FLOW = [
    ("$B \\in R \\Rightarrow A \\in R$", "קלות"),
    ("$B \\in RE \\Rightarrow A \\in RE$", "קלות"),
    ("$B \\in coRE \\Rightarrow A \\in coRE$", "קלות"),
    ("$A \\notin R \\Rightarrow B \\notin R$", "קושי"),
    ("$A \\notin RE \\Rightarrow B \\notin RE$", "קושי"),
    ("$A \\notin coRE \\Rightarrow B \\notin coRE$", "קושי"),
]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נלמד מה מותר להסיק מרדוקציה, ומה אסור."),
    P("כלל אחד, בשני כיוונים: קלות זורמת שמאלה, וקושי זורם ימינה.", hold=0.4),
], stage='<div class="kicker">M02 · רדוקציות מיפוי</div><h1>לאן זורמות קלות וקושי</h1>'
         '<p>לדעת מה מותר להסיק מ-$A \\le_m B$ על המחלקות של $A$ ושל $B$, ומה אסור.</p>', layout="title")

idea = Scene("idea", "הרעיון", [
    P("נניח ש-$A \\le_m B$, ויש לנו מכונה שמכריעה את $B$. איך נכריע את $A$?", do=show("p-0")),
    P("מקבלים מילה $x$, ומחשבים את $f(x)$.", do=show("p-1", "p-2")),
    P("שואלים את המכונה של $B$ על $f(x)$.", do=show("p-3")),
    P("והתשובה שלה היא בדיוק התשובה על $x$, כי הרדוקציה שומרת על התשובה.", do=show("p-4"), hold=0.4),
    P("כלומר: פתרון ל-$B$ נותן פתרון ל-$A$. $A$ לא קשה יותר מ-$B$.", do=show("i-c1")),
    P("ואותו טיעון עובד גם עם מכונה שרק מקבלת את $B$: נקבל מכונה שמקבלת את $A$.", do=show("i-c2"), hold=0.4),
], stage='<div class="stack">'
         + w_map.pipe("p", [("$x$", ""), ("$f$", "f"), ("$f(x)$", ""), ("מכריעה ל-$B$", "solver"), ("כן / לא", "ans")])
         + "</div>",
   panel=st.card("i-c1", "rule", "🔑 פתרון ל-$B$ נותן פתרון ל-$A$")
         + st.card("i-c2", "ex", "גם עם מכונה שמקבלת: $B \\in RE \\Rightarrow A \\in RE$"))

flow = Scene("flow", "הכלל", [
    P("מכאן הכלל. **קלות** זורמת מ-$B$ אל $A$: אם $B$ כריעה, גם $A$ כריעה.", do=show("t-0")),
    P("ואותו דבר עם $RE$: אם $B$ ניתנת לקבלה, גם $A$.", do=show("t-1")),
    P("ועם $coRE$: אם $B$ ב-$coRE$, גם $A$ ב-$coRE$.", do=show("t-2"), hold=0.3),
    P("ו**קושי** זורם הפוך, מ-$A$ אל $B$: אם $A$ לא כריעה, גם $B$ לא כריעה.", do=show("t-3")),
    P("כי אילו $B$ הייתה כריעה, היינו מכריעים גם את $A$. סתירה.", hold=0.2),
    P("ובאותו אופן עם $RE$ ועם $coRE$.", do=show("t-4", "t-5"), hold=0.4),
    P("שימו לב: כל שורה עובדת **רק** בכיוון שלה.", do=show("f-c1")),
], stage='<div class="stack"><div class="bigmath">$A \\le_m B$</div>'
         + st.card("f-c1", "trap", "⚠️ כל שורה עובדת רק בכיוון שלה") + "</div>",
   panel=w_map.rows("t", FLOW))

wrong = Scene("wrong", "הכיוון ההפוך", [
    P("למשל: $A$ כריעה. האם $B$ כריעה? לא בהכרח.", do=show("w-c1")),
    P("קחו את השפה הריקה, ואת $A_{TM}$, שאינה כריעה.", do=show("w-c2")),
    P("נגדיר פונקציה שמחזירה תמיד אותה מילה, מילה קבועה שלא שייכת ל-$A_{TM}$.",
      do=show("z-L-0", "z-L-1", "z-L-01", "z-R-y")),
    P("כל מילה נשלחת אל מחוץ ל-$A_{TM}$, ואף מילה לא שייכת לשפה הריקה. התשובה ״לא״ נשמרת תמיד.",
      do=show("z-a-0", "z-a-1", "z-a-01")),
    P("אז השפה הריקה ניתנת לרדוקציה אל $A_{TM}$. המקור כריע, והיעד לא.", do=show("w-c3"), hold=0.4),
    P("רדוקציה אומרת רק שהיעד **לפחות** קשה כמו המקור. הוא יכול להיות קשה הרבה יותר.", do=show("w-c4"), hold=0.4),
], stage=ZERO,
   panel=st.card("w-c1", "plain", "$A \\in R \\Rightarrow B \\in R$ ?")
         + st.card("w-c2", "ex", "$A = \\emptyset$, $B = A_{TM}$")
         + st.card("w-c3", "trap", "⚠️ $\\emptyset \\le_m A_{TM}$: מקור כריע, יעד לא")
         + st.card("w-c4", "rule", "🔑 $B$ לפחות קשה כמו $A$"))

more = Scene("more", "עוד תכונות", [
    P("ועוד שלוש תכונות. משלים: אם $A \\le_m B$, אז גם $\\overline{A} \\le_m \\overline{B}$.", do=show("m-1")),
    P("ובאותה פונקציה בדיוק: מי שלא ב-$A$ נשלח אל מחוץ ל-$B$, כלומר אל המשלים של $B$.", do=show("m-1b")),
    P("בזכות זה, שורות ה-$coRE$ בטבלה נובעות משורות ה-$RE$.", hold=0.3),
    P("טרנזיטיביות: $A \\le_m B$ ו-$B \\le_m C$ נותנים $A \\le_m C$. פשוט מרכיבים את שתי הפונקציות.", do=show("m-2")),
    P("ואין סימטריה: $A_{TM} \\le_m ALL_{TM}$, אבל $ALL_{TM}$ לא ניתנת לרדוקציה אל $A_{TM}$.", do=show("m-3"),
      say="ואין סימטריה: אֵיי טִי אֶם ניתנת לרדוקציה אל אוֹל טִי אֶם, אבל אוֹל טִי אֶם לא ניתנת לרדוקציה אל אֵיי טִי אֶם."),
    P("לכן רדוקציה היא לא יחס שקילות.", do=show("m-4"), hold=0.4),
], stage='<div class="stack">'
         '<div id="m-1" class="bigmath h">$A \\le_m B \\iff \\overline{A} \\le_m \\overline{B}$</div>'
         '<div id="m-2" class="bigmath h" style="font-size:44px">$A \\le_m B,\\ B \\le_m C \\Rightarrow A \\le_m C$</div>'
         '<div id="m-3" class="bigmath h" style="font-size:44px">$A_{TM} \\le_m ALL_{TM},\\ \\ ALL_{TM} \\nleq_m A_{TM}$</div>'
         "</div>",
   panel=st.card("m-1b", "rule", "🔑 משלים: אותה $f$ בדיוק")
         + st.card("m-4", "trap", "⚠️ טרנזיטיבי, אבל <b>לא</b> סימטרי"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: $A$ ו-$B$ לא טריוויאליות, ו-$A \\le_m B$. איזו טענה נכונה?"),
    P("הטענה הראשונה: אם $B$ ב-$RE$ איחוד $coRE$, אז גם $A$.", do=show("q-o-a")),
    P("נבדוק את שני המקרים. אם $B$ ב-$RE$, הקלות זורמת, ו-$A$ ב-$RE$.", do=show("e-1")),
    P("ואם $B$ ב-$coRE$, אז $A$ ב-$coRE$. בכל מקרה, $A$ באיחוד.", do=show("e-2", "q-ok-a"), hold=0.3),
    P("הטענה השנייה מניחה משהו על $A$, ומסיקה על $B$. זה הכיוון ההפוך.", do=show("q-x-b", "q-n-b")),
    P("דוגמה נגדית: $A$ המילים שמתחילות ב-1, שהיא כריעה, ו-$B$ היא $H_{TM}$, שאינה כריעה.", do=show("e-3"),
      say="דוגמה נגדית: אֵיי המילים שמתחילות באחת, שהיא כריעה, ובִּי היא אֵייץ' טִי אֶם, שאינה כריעה."),
    P("והרדוקציה קיימת: בודקים אם $x$ מתחילה ב-1, ומחזירים מילה קבועה בתוך $H_{TM}$, או מילה קבועה מחוצה לה.",
      hold=0.2),
    P("והשלישית מחליפה מחלקה: מ-$B$ ב-$coRE$ היא מסיקה ש-$A$ ב-$RE$.", do=show("q-x-c", "q-n-c")),
    P("אבל $coRE$ זורם רק ל-$coRE$. קחו $A$ ו-$B$ שתיהן המשלים של $H_{TM}$, עם פונקציית הזהות.", do=show("e-4"),
      say="אבל קוֹאוּ אָר אִי זורם רק לקוֹאוּ אָר אִי. קחו אֵיי ובִּי שתיהן המשלים של אֵייץ' טִי אֶם, עם פונקציית הזהות."),
    P("והאפשרות ״כל הטענות האחרות לא נכונות״ נופלת, כי הטענה הראשונה נכונה. זו התשובה.", do=show("q-x-d"),
      hold=0.5),
], stage='<div class="stack">'
         + st.card("e-1", "ex", "$B \\in RE \\Rightarrow A \\in RE$")
         + st.card("e-2", "ex", "$B \\in coRE \\Rightarrow A \\in coRE$")
         + st.card("e-3", "trap", "⚠️ $1\\Sigma^* \\le_m H_{TM}$: מקור כריע, יעד לא")
         + st.card("e-4", "trap", "⚠️ $\\overline{H_{TM}} \\le_m \\overline{H_{TM}}$: ב-$coRE$, לא ב-$RE$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$A, B$ לא טריוויאליות ו-$A \\le_m B$. '
         'איזו טענה נכונה?</div>'
         + st.options("q", OPTS, notes={"b": "כיוון הפוך", "c": "מחלקה אחרת"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $A \\le_m B$ אומר ש-$A$ לא קשה יותר מ-$B$.", do=show("r-1")),
    P("קלות זורמת מ-$B$ אל $A$: כריעה, $RE$ ו-$coRE$.", do=show("r-2")),
    P("קושי זורם מ-$A$ אל $B$. ובכיוון ההפוך, לא מסיקים כלום.", do=show("r-3")),
    P("ורדוקציה עוברת למשלימים באותה פונקציה, וגם טרנזיטיבית, אבל לא סימטרית. נתראה ברמה הבאה.", do=show("r-4"),
      hold=0.6),
], stage='<div class="stack"><div class="bigmath">$A \\le_m B$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $A$ לא קשה יותר מ-$B$")
         + st.card("r-2", "rule", "🔑 קלות: מ-$B$ אל $A$")
         + st.card("r-3", "rule", "🔑 קושי: מ-$A$ אל $B$")
         + st.card("r-4", "trap", "⚠️ משלים: אותה $f$. טרנזיטיבי, לא סימטרי"))

VIDEO = Video("M02", "map", "לאן זורמות קלות וקושי", [title, idea, flow, wrong, more, exam, recap],
              bank={"25B-B-Q1": "a"})
