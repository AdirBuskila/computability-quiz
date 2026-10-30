# -*- coding: utf-8 -*-
"""T01 · מה יש בתוך מכונת טיורינג — video script (build: tools/video/vid.py T01).

Source: tools/courses_src/tm/T01.js (lesson + goal). Exam anchor: 24S-A-Q14 (δ of a jumping-head variant), which no
guided quiz uses (vid.py refuses quiz ids). Not used on purpose: the quiz questions of T01 (24S-A-Q10 and the four
original ones) and 24B-B-Q4 (the T07 boss).
Every run below comes from w_tm.trace(), which asserts it ends exactly like the course checker's run_tm.
"""
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, BLANK
import stage as st
import w_tm

# ---------------------------------------------------------------- machines (verified)
# scene "step": three steps that show R, L and a halt
D1 = {("q_0", "0"): ("q_1", "X", "R"), ("q_1", "1"): ("q_2", "Y", "L"), ("q_2", "X"): (ACC, "X", "R")}
C1, R1 = w_tm.trace(D1, "q_0", "0110")
assert R1 == "accept" and len(C1) == 4
assert [c[2] for c in C1] == [0, 1, 0, 1]                       # head: 0 -> 1 -> 0 -> 1
assert "".join(C1[2][1]).rstrip(BLANK) == "XY10"                # after two steps the tape reads X Y 1 0

# scene "edge": a move L from the first cell keeps the head there, and the step still happens
D2 = {("q_0", "1"): ("q_1", "Z", "L"), ("q_1", "Z"): (ACC, "Z", "R")}
C2, R2 = w_tm.trace(D2, "q_0", "10")
assert R2 == "accept" and C2[1][2] == 0 and C2[1][0] == "q_1" and C2[1][1][0] == "Z"

# exam 24S-A-Q14
Q = BANK["24S-A-Q14"]
assert Q["correctId"] == "a" and r"\mathbb{Z}" in Q["options"][0]["value"]
OPTS = [(o["id"], f'${o["value"]}$' if o["type"] == "math" else o["value"]) for o in Q["options"]]

T1, V1 = w_tm.tape("t1", C1, 6)
T2, V2 = w_tm.tape("t2", C2, 5)
T0, _ = w_tm.tape("t0", [("q_0", list("0110"), 0)], 7, hidden=True)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נפרק מכונת טיורינג לרכיבים שלה."),
    P("נראה מה מותר ומה אסור בכל רכיב, ונריץ כמה צעדים על הסרט."),
    P("ובסוף נפתור שאלה אמיתית ממבחן.", hold=0.4),
], stage='<div class="kicker">T01 · מכונות טיורינג</div><h1>מה יש בתוך מכונת טיורינג</h1>'
         '<p>לקרוא את שבעת רכיבי ההגדרה ולדעת מה מותר ומה אסור בהם: א״ב הקלט מול א״ב הסרט, מספר המצבים המינימלי, '
         'והראש בקצה השמאלי.</p>', layout="title")

idea = Scene("idea", "הרעיון", [
    P("מכונת טיורינג היא אוטומט סופי שקיבל סרט אינסופי.", do=show("i-tape")),
    P("הקלט נכתב בתחילת הסרט, וכל שאר התאים מלאים ב**רווח**.", do=show("i-c1")),
    P("הראש מתחיל בתא הראשון, והמכונה במצב ההתחלה $q_0$.", do=show("t0-hd0", "t0-st-q_0")),
    P("בכל צעד היא קוראת את התו שמתחת לראש, וכותבת תו במקומו.", do=show("i-c2")),
    P("אחר כך היא עוברת למצב חדש, וזזה תא אחד שמאלה או ימינה.", do=show("i-c3"), hold=0.4),
    P("אין לה זיכרון אחר: רק המצב, הסרט, ומקום הראש."),
], stage=f'<div id="i-tape" class="h">{T0}</div>',
   panel=st.card("i-c1", "plain", "רווח: $\\sqcup$, סוף הקלט")
         + st.card("i-c2", "ex", "צעד: קוראים תו, כותבים תו")
         + st.card("i-c3", "ex", "ועוד בצעד: מצב חדש, תזוזה $L$ או $R$"))

ROWS = [
    ("d-q", "Q", "קבוצה <b>סופית</b> של מצבים"),
    ("d-s", "\\Sigma", "א״ב הקלט. הרווח $\\sqcup$ <b>לא</b> בו"),
    ("d-g", "\\Gamma", "א״ב הסרט: מכיל את $\\Sigma$ וגם את $\\sqcup$"),
    ("d-d", "\\delta", "פונקציית המעברים"),
    ("d-0", "q_0", "מצב ההתחלה"),
    ("d-h", "q_{acc} \\ne q_{rej}", "שני מצבי העצירה, שונים זה מזה"),
]
defs = Scene("def", "ההגדרה", [
    P("ההגדרה הפורמלית: שבעה רכיבים.", do=show("d-m")),
    P("$Q$: קבוצה סופית של מצבים.", do=show("d-q")),
    P("$\\Sigma$: הא״ב של הקלט. הרווח לא שייך אליו, כי הרווח מסמן איפה הקלט נגמר.", do=show("d-s")),
    P("$\\Gamma$: הא״ב של הסרט. הוא מכיל את $\\Sigma$, וגם את הרווח.", do=show("d-g")),
    P("ולכן $\\Sigma$ מוכל ב-$\\Gamma$ **ממש**. תמיד, בכל מכונה.", do=show("d-r1")),
    P("$\\delta$: פונקציית המעברים. נחזור אליה עוד רגע.", do=show("d-d")),
    P("$q_0$ הוא מצב ההתחלה.", do=show("d-0")),
    P("ו-$q_{acc}$ ו-$q_{rej}$ הם שני מצבי העצירה: מקבל ודוחה.", do=show("d-h")),
    P("שני מצבי העצירה שונים זה מזה. לכן בכל מכונת טיורינג יש **לפחות שני מצבים**.", do=show("d-r2"), hold=0.5),
], stage='<div class="stack"><div id="d-m" class="bigmath h">'
         '$M = \\langle Q, \\Sigma, \\Gamma, \\delta, q_0, q_{acc}, q_{rej} \\rangle$</div><div class="tuple">'
         + "".join(f'<div id="{i}" class="row h"><span class="sym">${s}$</span><span>{t}</span></div>' for i, s, t in ROWS)
         + "</div></div>",
   panel=st.card("d-r1", "rule", "🔑 $\\Sigma \\subsetneq \\Gamma$: מוכל <b>ממש</b>, בגלל הרווח")
         + st.card("d-r2", "rule", "🔑 $q_{acc} \\ne q_{rej}$, ולכן <b>לפחות 2</b> מצבים"))

step = Scene("step", "צעד אחד", [
    P("עכשיו $\\delta$. היא מקבלת מצב ותו שנקרא.", do=show("s-sig")),
    P("ומחזירה שלישייה אחת: המצב הבא, התו לכתיבה, וכיוון התזוזה.", say="ומחזירה שלישייה אחת: המצב הבא, התו לכתיבה, וכיוון התזוזה."),
    P("נריץ שלושה מעברים על הקלט $0110$.", do=show("s-tape")),
    *w_tm.run_phrases("t1", D1, C1, V1),
    P("שימו לב לתווים $X$ ו-$Y$: הם לא אותיות של הקלט.", do=show("s-c1")),
    P("הם **סימני עבודה** שהמכונה כותבת לעצמה. הם שייכים ל-$\\Gamma$, ולא ל-$\\Sigma$.", hold=0.4),
    P("ולכן $\\delta$ מוגדרת על כל $\\Gamma$: על הסרט יכול להופיע כל תו כזה.", do=show("s-c2")),
], stage='<div class="stack"><div id="s-sig" class="bigmath h">'
         '$\\delta : Q \\times \\Gamma \\to Q \\times \\Gamma \\times \\{L, R\\}$</div>'
         f'<div id="s-tape" class="h">{T1}</div></div>',
   panel=st.card("s-c1", "ex", "$X, Y \\in \\Gamma$ אבל $X, Y \\notin \\Sigma$")
         + st.card("s-c2", "rule", "🔑 $\\delta$ מוגדרת על $Q \\times \\Gamma$, לא רק על $Q \\times \\Sigma$"))

edge = Scene("edge", "הקצה השמאלי", [
    P("ועכשיו הכלל שמבלבל הכי הרבה: הסרט אינסופי רק **ימינה**.", do=show("e-tape")),
    P("הראש בתא הראשון, ו-$\\delta$ אומרת לזוז שמאלה. מה קורה?", do=show("e-q")),
    *w_tm.run_phrases("t2", D2, C2[:2], V2),
    P("התו נכתב, המצב התחלף, והראש **נשאר במקום**.", do=show("e-c1")),
    P("המכונה לא נדחית ולא קורסת. זה פשוט צעד רגיל, בלי תזוזה.", do=show("e-c2"), hold=0.4),
    *w_tm.run_phrases("t2", D2, C2, V2)[1:],
], stage=f'<div class="stack"><div id="e-tape" class="h">{T2}</div></div>',
   panel=st.card("e-q", "plain", "ראש בתא 0, ו-$\\delta$ אומרת $L$")
         + st.card("e-c1", "rule", "🔑 שמאלה מהתא הראשון: הראש <b>נשאר</b>, כל השאר קורה כרגיל")
         + st.card("e-c2", "trap", "⚠️ לא דחייה ולא קריסה"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: וריאנט שבו הראש יכול לקפוץ בכל צעד מספר תאים כלשהו, ימינה או שמאלה, וגם אפס."),
    P("ואם הקפיצה שמאלה עוברת את התחלת הסרט, הראש נעצר בתא הראשון. איך נראית $\\delta$?"),
    P("רק החלק השלישי משתנה: במקום כיוון אחד, $L$ או $R$, צריך לקודד קפיצה.", do=show("x-1"),
      say="רק החלק השלישי משתנה: במקום כיוון אחד, שמאלה או ימינה, צריך לקודד קפיצה."),
    P("מספר **שלם** עושה את זה: הסימן הוא הכיוון, והגודל הוא מספר התאים.", do=show("x-2")),
    P("מינוס שלוש זה שלושה תאים שמאלה, חמש זה חמישה ימינה, ואפס זה להישאר במקום.", do=show("x-3")),
    P("לכן החלק השלישי הוא קבוצת המספרים השלמים.", do=show("q-ok-a"), hold=0.3),
    P("זוג מספרים **טבעיים** לא מקודד כיוון: טבעי לא יכול להיות שלילי.", do=show("q-x-b", "q-n-b")),
    P("וזו המלכודת: רצף של $n$ תזוזות, $L$ או $R$, נראה כמו קפיצה.", do=show("x-t"),
      say="וזו המלכודת: רצף של אֶן תזוזות, שמאלה או ימינה, נראה כמו קפיצה."),
    P("אבל $n$ קבוע: אי אפשר לקפוץ יותר מ-$n$ תאים, וגם לא לעמוד במקום כש-$n$ אי-זוגי.", do=show("q-x-c", "q-n-c"),
      say="אבל אֶן קבוע: אי אפשר לקפוץ יותר מאֶן תאים, וגם לא לעמוד במקום כשאֶן אי זוגי."),
    P("אז התשובה היא $\\delta$ עם המספרים השלמים, והאפשרות ״אף אחת״ נופלת.", do=show("q-x-d"), hold=0.6,
      say="אז התשובה היא דלתא עם המספרים השלמים, והאפשרות אף אחת נופלת."),
], stage='<div class="stack">'
         '<div id="x-1" class="bigmath h">$Q \\times \\Gamma \\to Q \\times \\Gamma \\times \\, ?$</div>'
         '<div id="x-2" class="bigmath h">$z \\in \\mathbb{Z}$</div>'
         '<div id="x-3" class="bigmath h" style="font-size:40px">$z = -3,\\ \\ z = 0,\\ \\ z = 5$</div>'
         + st.card("x-t", "trap", "⚠️ $\\{L,R\\}^n$: לכל היותר $n$ תאים, ולא כל מספר")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>וריאנט שבו הראש קופץ בכל צעד מספר תאים כלשהו '
         '(כולל 0). איזו צורה מתאימה לפונקציית המעברים?</div>'
         + st.options("q", OPTS, notes={"b": "אין כיוון", "c": "קפיצה חסומה"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: שבעה רכיבים. $Q$ סופית, ו-$\\Sigma$ מוכל ב-$\\Gamma$ ממש בגלל הרווח.", do=show("r-1")),
    P("$\\delta$ מקבלת מצב ותו, ומחזירה מצב, תו וכיוון.", do=show("r-2")),
    P("שני מצבי עצירה שונים, ולכן לפחות שני מצבים.", do=show("r-3")),
    P("ושמאלה מהתא הראשון: הראש נשאר במקום, וכל השאר קורה כרגיל. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">'
         '$M = \\langle Q, \\Sigma, \\Gamma, \\delta, q_0, q_{acc}, q_{rej} \\rangle$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $\\Sigma \\subsetneq \\Gamma$")
         + st.card("r-2", "rule", "🔑 $\\delta(q, a) = (p, b, D)$")
         + st.card("r-3", "rule", "🔑 לפחות 2 מצבים")
         + st.card("r-4", "trap", "⚠️ $L$ מהתא הראשון: הראש נשאר"))

VIDEO = Video("T01", "tm", "מה יש בתוך מכונת טיורינג", [title, idea, defs, step, edge, exam, recap],
              bank={"24S-A-Q14": "a"})
