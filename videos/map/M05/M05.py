# -*- coding: utf-8 -*-
"""M05 · בדיקת פונקציה: האם זו רדוקציה? — video script (build: tools/video/vid.py M05).

Source: tools/courses_src/map/M05.js (lesson + goal). Exam anchor: 23A-A-Q16 (T accepts 01 and 0110 before running M:
the negative direction of co-H_TM <=m L breaks), which no guided quiz uses. Not used on purpose: the five original
quiz questions of M05 (the "11 on short words" branch, the length examples, NEQ/CE, the 17/18 machine) and 24B-A-Q17
(the M05 quiz).
The toy picture is brute-forced on every word up to length 10 like map/check.py (kinds brute-fn / brute-fn2); the exam
machine T is evaluated on both cases of M (halts / does not halt), with machines run by common.run_tm.
"""
from vid import P, Scene, Video, show, hide, BANK
from common import words, run_tm
import stage as st
import w_map

W = words(10)

# ---------------------------------------------------------------- toy: an answer-flipping function
A = lambda x: x.count("1") % 2 == 0          # an even number of 1s
B = lambda y: y.count("1") % 2 == 0          # the same language
f = lambda x: x + "1"
to_B = all(A(x) == B(f(x)) for x in W)
to_coB = all(A(x) == (not B(f(x))) for x in W)
assert (to_B, to_coB) == (False, True)        # A <=m complement(B), not A <=m B
XS = ["0", "11", "1", "10"]
assert [f(x) for x in XS] == ["01", "111", "11", "101"]
G1, I1 = w_map.bridge_from("g1", XS, A, B, f)
assert all(I1[x][3] == "bad" for x in XS)
coB = lambda y: not B(y)
G2, I2 = w_map.bridge_from("g2", XS, A, coB, f, A="A", B="co:B")
assert all(I2[x][3] == "ok" for x in XS)

# ---------------------------------------------------------------- exam 23A-A-Q16
PAL_EVEN = lambda s: len(s) % 2 == 0 and s == s[::-1]
ZN1N = lambda s: len(s) % 2 == 0 and s == "0" * (len(s) // 2) + "1" * (len(s) // 2) and len(s) > 0
SAFE = {"01", "0110"}


def T_lang(M, start, w):
    """T(x): if x in {01, 0110} ACCEPT; else run M on w, ACCEPT. -> the words T accepts (up to length 10)"""
    halts = run_tm(M, start, w, 4000)[0] != "loop"
    return {x for x in W if x in SAFE or halts}


def in_L(lang):   # L: accepts at least one even palindrome and at least one 0^n1^n
    return any(PAL_EVEN(x) and x for x in lang) and any(ZN1N(x) for x in lang)


HALT = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): ("q_0", "1", "R")}                       # halts (rejects)
LOOP = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): ("q_1", "1", "L"), ("q_1", "0"): ("q_0", "0", "R")}  # bounces
assert T_lang(LOOP, "q_0", "01") == SAFE and in_L(SAFE)            # <M,w> in co-H  ->  T in L      (holds)
assert in_L(T_lang(HALT, "q_0", "011"))                             # <M,w> not in co-H -> T in L    (breaks)
Q = BANK["23A-A-Q16"]
assert Q["correctId"] == "d"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

STEPS = [
    ("1", "<b>כיוון:</b> קלט מסוג $A$, פלט מסוג $B$?"),
    ("2", "<b>חישוביות:</b> עוצרת על כל קלט? רק כותבת קוד?"),
    ("3", "<b>חיובי:</b> $x \\in A \\Rightarrow f(x) \\in B$"),
    ("4", "<b>שלילי:</b> $x \\notin A \\Rightarrow f(x) \\notin B$"),
]
T_CODE = ["T(x):", "  if x = 01 or x = 0110:", "    ACCEPT", "  else:", "    run M on w; ACCEPT"]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נלמד לבדוק פונקציה שמישהו טוען שהיא רדוקציה."),
    P("ארבעה שלבים קבועים, ושלוש מלכודות שחוזרות בכל מבחן.", hold=0.4),
], stage='<div class="kicker">M05 · רדוקציות מיפוי</div><h1>בדיקת פונקציה: האם זו רדוקציה?</h1>'
         '<p>לבדוק פונקציה נתונה ב-4 שלבים ולזהות את המלכודות הקבועות: ענף קבוע, כיוון הפוך, חישוב ששובר את התנאי.</p>',
   layout="title")

steps = Scene("steps", "ארבעה שלבים", [
    P("שאלת מבחן אופיינית נותנת פונקציה, ושואלת אם היא רדוקציה מ-$A$ אל $B$. בודקים לפי הסדר."),
    P("שלב ראשון, כיוון: האם הפונקציה מקבלת קלטים של $A$ ומחזירה קלטים של $B$? ולא להפך?", do=show("s-0")),
    P("שלב שני, חישוביות: האם היא עוצרת על כל קלט? בונה מכונה, ולא מריצה אותה?", do=show("s-1")),
    P("שלב שלישי, הכיוון החיובי: מילה ב-$A$ נוחתת בתוך $B$?", do=show("s-2")),
    P("ושלב רביעי, הכיוון השלילי: מילה מחוץ ל-$A$ נוחתת מחוץ ל-$B$?", do=show("s-3")),
    P("ברוב הרדוקציות השבורות, הכיוון השלילי הוא שנופל. שם מחפשים קודם.", do=show("s-c"), hold=0.4),
], stage='<div class="stack">' + w_map.rows("s", STEPS, cls="steps") + "</div>",
   panel=st.card("s-c", "trap", "⚠️ רוב הרדוקציות השבורות נופלות בשלב 4"))

flip = Scene("flip", "היפוך תשובה", [
    P("מלכודת ראשונה: היפוך תשובה. $A$ ו-$B$: המילים עם מספר זוגי של אחדות. והפונקציה מוסיפה 1 בסוף.",
      do=show("f-c1")),
    P("$0$: אין בה אחדות, וזה זוגי. אחרי התוספת, $01$: אחד בודד, אי-זוגי. מחוץ ל-$B$.",
      do=show("g1-L-0", "g1-R-01", "g1-a-0"),
      say="אפס: אין בה אחדות, וזה זוגי. אחרי התוספת, אפס אחת: אחד בודד, אי זוגי. מחוץ לבִּי."),
    P("ו-$1$, מחוץ ל-$A$, הופכת ל-$11$: שתי אחדות, בתוך $B$.", do=show("g1-L-1", "g1-R-11", "g1-a-1"),
      say="ואחת, מחוץ לאֵיי, הופכת לאחת אחת: שתי אחדות, בתוך בִּי."),
    P("כל חץ הופך את התשובה. כן הופך ללא, ולא הופך לכן.",
      do=show("g1-L-11", "g1-R-111", "g1-a-11", "g1-L-10", "g1-R-101", "g1-a-10")),
    P("אז זו לא רדוקציה אל $B$. אבל היא כן רדוקציה אל **המשלים** של $B$.", do=hide("g1") + show("g2-all")),
    P("עם המשלים, כל החצים ירוקים: $A$ ניתנת לרדוקציה אל המשלים של $B$.", do=show("f-c2"), hold=0.4),
    P("כלל: אם $x$ ב-$A$ בדיוק כש-$f(x)$ **לא** ב-$B$, זו רדוקציה אל המשלים.", do=show("f-c3"), hold=0.4),
], stage='<div class="swap" style="--swap-h:560px"><div>' + G1 + '</div><div id="g2-all" class="h">'
         + G2.replace('class="h"', 'class=""') + "</div></div>",
   panel=st.card("f-c1", "plain", "$A = B$: מספר <b>זוגי</b> של 1. $f(x) = x1$")
         + st.card("f-c2", "rule", "🔑 $A \\le_m \\overline{B}$, ולא $A \\le_m B$")
         + st.card("f-c3", "rule", "🔑 $x \\in A \\iff f(x) \\notin B$: רדוקציה אל $\\overline{B}$"))

traps = Scene("traps", "עוד מלכודות", [
    P("מלכודת שנייה: **ענף קבוע**. המכונה שנבנית מקבלת כמה מילים מיד, בלי להריץ כלום.", do=show("t-1")),
    P("אם המילים האלה כבר מכניסות אותה ליעד, היא ביעד תמיד. והכיוון השלילי נופל.", hold=0.3),
    P("מלכודת שלישית: **אמת ריקה**. יעד כמו ״כל מילה שהמכונה מקבלת מקיימת משהו״.", do=show("t-2")),
    P("מכונה שלא מקבלת אף מילה מקיימת את זה. אז מכונה ש״נתקעה״ עדיין נמצאת ביעד.", hold=0.3),
    P("וזכרו: מכונה שלא הגיעה לקבלה לא בהכרח דחתה. ייתכן שהיא פשוט לא עצרה.", do=show("t-3"), hold=0.4),
], stage='<div class="stack">'
         + st.card("t-1", "trap", "⚠️ ענף קבוע: מילים שמתקבלות תמיד, בלי קשר ל-$M$")
         + st.card("t-2", "trap", "⚠️ אמת ריקה: $L(Q) = \\emptyset$ מקיימת ״כל מילה ש-$Q$ מקבלת…״")
         + st.card("t-3", "trap", "⚠️ ״לא קיבלה״ אינו ״דחתה״")
         + "</div>")

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן. $L$: המכונות שמקבלות לפחות פלינדרום אחד באורך זוגי, ולפחות מילה אחת מהצורה $0^n1^n$.",
      do=show("x-l"), say="שאלה ממבחן. אֵל: המכונות שמקבלות לפחות פלינדרום אחד באורך זוגי, ולפחות מילה אחת מהצורה אפס בחזקת אֶן, אחת בחזקת אֶן."),
    P("מנסים לרדד את המשלים של $H_{TM}$ אל $L$, עם המכונה $T$ שבקוד.", do=show("x-code")),
    P("שלב ראשון ושני: מזוג של מכונה ומילה, למכונה. והפונקציה רק כותבת קוד. הכול תקין.", do=show("q-x-b")),
    P("שלב שלישי: $M$ לא עוצרת על $w$. אז $T$ מקבלת רק את $01$ ואת $0110$.", do=show("x-hl1"),
      say="שלב שלישי: אֵם לא עוצרת על דַּאבְּלְיוּ. אז טִי מקבלת רק את אפס אחת ואת אפס אחת אחת אפס."),
    P("$0110$ הוא פלינדרום באורך זוגי, ו-$01$ מהצורה $0^n1^n$. $T$ ב-$L$. הכיוון החיובי עובד.",
      do=show("x-1", "q-x-c"),
      say="אפס אחת אחת אפס הוא פלינדרום באורך זוגי, ואפס אחת מהצורה אפס בחזקת אֶן, אחת בחזקת אֶן. טִי באֵל. הכיוון החיובי עובד."),
    P("שלב רביעי: $M$ עוצרת על $w$. אז $T$ מקבלת **הכול**. ובפרט, את $01$ ואת $0110$.",
      do=hide("x-hl1") + show("x-hl4", "x-2"),
      say="שלב רביעי: אֵם עוצרת על דַּאבְּלְיוּ. אז טִי מקבלת הכול. ובפרט, את אפס אחת ואת אפס אחת אחת אפס."),
    P("אז $T$ ב-$L$ גם כאן. הענף הקבוע מכניס אותה ליעד בכל מקרה. הכיוון השלילי נופל.",
      do=show("q-ok-d", "q-x-a"), hold=0.3),
    P("וזה גם לא מפתיע: $L$ ניתנת לקבלה, אז אסור היה שתהיה אליה רדוקציה מהמשלים של $H_{TM}$.", do=show("x-t"),
      hold=0.6),
], stage='<div class="stack">'
         '<div id="x-l" class="bigmath h" style="font-size:36px">$L$: even palindrome $\\wedge$ $0^n1^n$</div>'
         + w_map.code("x", T_CODE).replace('class="codebox"', 'class="codebox h" style="font-size:27px"')
         .replace('id="x"', 'id="x-code"')
         + st.card("x-1", "ex", "$M$ לא עוצרת: $L(T) = \\{01, 0110\\}$, $T \\in L$ ✓")
         + st.card("x-2", "trap", "⚠️ $M$ עוצרת: $L(T) = \\Sigma^*$, $T \\in L$ ✗")
         + st.card("x-t", "rule", "🔑 $L \\in RE$: אין רדוקציה אליה מ-$\\overline{H_{TM}}$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$g(\\langle M,w\\rangle) = \\langle T\\rangle$, '
         'רדוקציה מ-$\\overline{H_{TM}}$ אל $L$?</div>'
         + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום, ארבעה שלבים: כיוון, חישוביות, כיוון חיובי, וכיוון שלילי.", do=show("r-1")),
    P("אם התשובה מתהפכת, זו רדוקציה אל המשלים.", do=show("r-2")),
    P("ענף קבוע ואמת ריקה שוברים את הכיוון השלילי.", do=show("r-3")),
    P("ומספיקה דוגמה אחת כדי להפיל. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack">' + w_map.rows("rs", STEPS, cls="steps").replace('class="row h"', 'class="row"') + "</div>",
   panel=st.card("r-1", "rule", "🔑 4 שלבים, השלילי אחרון וחשוב")
         + st.card("r-2", "rule", "🔑 היפוך: $A \\le_m \\overline{B}$")
         + st.card("r-3", "trap", "⚠️ ענף קבוע, אמת ריקה")
         + st.card("r-4", "trap", "⚠️ דוגמה אחת מפילה"))

VIDEO = Video("M05", "map", "בדיקת פונקציה: האם זו רדוקציה?", [title, steps, flip, traps, exam, recap],
              bank={"23A-A-Q16": "d"})
