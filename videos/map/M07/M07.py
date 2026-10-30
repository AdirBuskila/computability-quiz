# -*- coding: utf-8 -*-
"""M07 · מבחן גמר: רדוקציות מיפוי — video script (build: tools/video/vid.py M07).

Boss level: a walkthrough of three exam questions that no guided quiz uses (vid.py refuses quiz and boss ids):
23A-A-Q9 (three languages: classes flow, a decidable language reduces to anything non-trivial), 24B-A-Q6 (what a
missing reduction implies), 24A-A-Q13 (L(M) ⊆ PALINDROMES: a vacuous truth breaks the negative direction).
Not used on purpose: the six boss questions of M07 (22A-A-Q9, 23A-B-Q12, 24B-A-Q1, 24B-A-Q8, 25B-B-Q8, 26B-A-Q13)
and every question cited by the map lessons.
Q2 is brute-forced over all languages of a 3-word universe like map/check.py (kind brute-universe); Q3 runs both kinds
of M (halting / looping) with common.run_tm and checks Q against the target language on all words up to length 8.
"""
import itertools
from vid import P, Scene, Video, show, hide, BANK
from common import words, run_tm
from rules import rule
import stage as st
import w_map

# ---------------------------------------------------------------- Q1: 23A-A-Q9
assert rule("red.R_down") and rule("red.R_to_any_nontrivial") and rule("red.complement_same_f")
Q1 = BANK["23A-A-Q9"]
assert Q1["correctId"] == "d"
O1 = [(o["id"], f'${o["value"]}$' if o["type"] == "math" else o["value"]) for o in Q1["options"]]

# ---------------------------------------------------------------- Q2: 24B-A-Q6, brute force on a 3-word universe
N, FULL = 3, 7


def R(X, Y):
    return any(all(((X >> x) & 1) == ((Y >> f[x]) & 1) for x in range(N)) for f in itertools.product(range(N), repeat=N))


TRIPLES = list(itertools.product(range(FULL + 1), repeat=3))
a_holds = all(R(A, C) is False for A, B, C in TRIPLES if not R(A, B) and R(B, C))
b_holds = any(R(A, C) for A, B, C in TRIPLES if not R(A, B) and R(B, C))
c_holds = all(not R(C, B) for A, B, C in TRIPLES if not R(A, B) and not R(A, C))
assert (a_holds, b_holds, c_holds) == (False, True, False)
assert all(not R(B, C) for A, B, C in TRIPLES if R(A, B) and not R(A, C))       # the direction that does work
Q2 = BANK["24B-A-Q6"]
assert Q2["correctId"] == "b"
O2 = [(o["id"], o["value"].replace(r"\not\le_m", r"\nleq_m")) for o in Q2["options"]]   # Chrome puts \not's slash on the A

# ---------------------------------------------------------------- Q3: 24A-A-Q13
W8 = words(8)
PAL = lambda s: s == s[::-1]
HALT = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): ("q_0", "1", "R")}
LOOP = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): ("q_1", "1", "L"), ("q_1", "0"): ("q_0", "0", "R")}


def Q_lang(M, w):
    """Q(x): if x is a palindrome, run M on w and ACCEPT; else REJECT"""
    halts = run_tm(M, "q_0", w, 4000)[0] != "loop"
    return {x for x in W8 if PAL(x) and halts}


in_L = lambda lang: all(PAL(x) for x in lang)          # L(Q) ⊆ PALINDROMES
assert Q_lang(LOOP, "01") == set() and in_L(set())       # M loops (in co-H): L(Q) = ∅ ⊆ PAL, Q in L  (fine)
assert Q_lang(HALT, "011") == {x for x in W8 if PAL(x)} and in_L(Q_lang(HALT, "011"))   # M halts: Q in L (breaks)
Q3 = BANK["24A-A-Q13"]
assert Q3["correctId"] == "c"
O3 = [(o["id"], o["value"]) for o in Q3["options"]]
Q_CODE = ["Q(x):", "  if x is a palindrome:", "    run M on w; ACCEPT", "  else: REJECT"]


def stem(q, html):
    return f'<div class="qstem"><span class="qid">{q["id"]}</span>{html}</div>'


# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("זה מבחן הגמר של פרק הרדוקציות: שלוש שאלות אמיתיות ממבחנים, שלא הופיעו באף רמה."),
    P("לפני כל פתרון, עצרו את הסרטון ונסו לבד.", hold=0.4),
], stage='<div class="kicker">M07 · רדוקציות מיפוי</div><h1>מבחן גמר: רדוקציות מיפוי</h1>'
         '<p>שלוש שאלות מבחן: זרימה בין מחלקות, רדוקציה שלא קיימת, ובדיקת פונקציה.</p>', layout="title")

kit = Scene("kit", "ארגז הכלים", [
    P("קודם, ארגז הכלים. קלות זורמת מהיעד אל המקור, וקושי מהמקור אל היעד.", do=show("k-1")),
    P("רדוקציה עוברת למשלימים באותה פונקציה, והיא טרנזיטיבית.", do=show("k-2")),
    P("שפה כריעה ולא טריוויאלית מתרדדת לכל שפה לא טריוויאלית.", do=show("k-3")),
    P("ופונקציה בודקים בארבעה שלבים, עם תשומת לב מיוחדת לכיוון השלילי.", do=show("k-4"), hold=0.4),
], stage='<div class="stack">'
         + st.card("k-1", "rule", "🔑 קלות: מ-$B$ אל $A$. קושי: מ-$A$ אל $B$")
         + st.card("k-2", "rule", "🔑 $A \\le_m B \\iff \\overline{A} \\le_m \\overline{B}$, וטרנזיטיביות")
         + st.card("k-3", "rule", "🔑 כריעה ולא טריוויאלית: מתרדדת לכל לא טריוויאלית")
         + st.card("k-4", "rule", "🔑 כיוון, חישוביות, חיובי, שלילי") + "</div>",
   layout="full")

q1 = Scene("q1", "שאלה 1", [
    P("שאלה ראשונה: שלוש שפות לא טריוויאליות. $L_1$ כריעה, $L_3$ ב-$RE$ ולא כריעה.", do=show("a-0")),
    P("ונתונה רדוקציה מהמשלים של $L_2$ אל המשלים של $L_1$.", do=show("a-0b")),
    P("נתחיל מ-$L_1$: היא כריעה, ולכן גם המשלים שלה כריע.", do=show("a-1")),
    P("הקלות זורמת אל המקור: המשלים של $L_2$ כריע. ולכן גם $L_2$ עצמה כריעה.", do=show("a-2")),
    P("אז הטענה ש-$L_2$ לא כריעה נופלת.", do=show("p1-x-a")),
    P("הטענה שאין רדוקציה מהמשלים של $L_2$ אל $L_3$? אבל המשלים של $L_2$ כריע ולא טריוויאלי. הוא מתרדד לכל שפה כזו.",
      do=show("a-3", "p1-x-b")),
    P("ורדוקציה מ-$L_3$ אל $L_2$ הייתה הופכת את $L_3$ לכריעה. אבל היא לא. נופלת.", do=show("a-4", "p1-x-c")),
    P("אז אף אחת מהטענות האחרות לא נכונה.", do=show("p1-ok-d"), hold=0.5),
], stage='<div class="stack">'
         '<div id="a-0" class="bigmath h" style="font-size:40px">$L_1 \\in R,\\ \\ L_3 \\in RE \\setminus R$</div>'
         '<div id="a-0b" class="bigmath h" style="font-size:40px">$\\overline{L_2} \\le_m \\overline{L_1}$</div>'
         + st.card("a-1", "ex", "$L_1 \\in R$, ולכן $\\overline{L_1} \\in R$")
         + st.card("a-2", "ex", "קלות זורמת: $\\overline{L_2} \\in R$, ולכן $L_2 \\in R$")
         + st.card("a-3", "ex", "$\\overline{L_2}$ כריעה: $\\overline{L_2} \\le_m L_3$ קיימת")
         + st.card("a-4", "trap", "⚠️ $L_3 \\le_m L_2$ הייתה נותנת $L_3 \\in R$")
         + "</div>",
   panel=stem(Q1, "$\\overline{L_2} \\le_m \\overline{L_1}$, $L_3 \\in RE \\setminus R$, $L_1 \\in R$. מה נכון?")
         + st.options("p1", O1))

q2 = Scene("q2", "שאלה 2", [
    P("שאלה שנייה: הסימון עם הקו פירושו ש**אין** רדוקציה. מה אפשר להסיק מרדוקציה שחסרה?"),
    P("הטענה הראשונה: אין מ-$A$ אל $B$, יש מ-$B$ אל $C$. האם בהכרח אין מ-$A$ אל $C$?", do=show("b-1")),
    P("לא. $C$ יכולה להיות קשה הרבה יותר מ-$B$, ואז $A$ מתרדדת אליה בקלות.", hold=0.2),
    P("דוגמה: $A$ היא $A_{TM}$. $B$: המילים שמתחילות ב-1, שהיא כריעה. ו-$C$ היא $H_{TM}$.", do=show("b-2")),
    P("$A_{TM}$ לא מתרדדת לשפה כריעה. $B$ כריעה, ולכן מתרדדת ל-$H_{TM}$. ו-$A_{TM}$ כן מתרדדת ל-$H_{TM}$.",
      do=show("b-3"),
      say="אֵיי טִי אֶם לא מתרדדת לשפה כריעה. בִּי כריעה, ולכן מתרדדת לאֵייץ' טִי אֶם. ואֵיי טִי אֶם כן מתרדדת לאֵייץ' טִי אֶם."),
    P("אז הטענה ״בהכרח אין״ נופלת, והטענה ״ייתכן שיש״ נכונה.", do=show("p2-x-a", "p2-ok-b")),
    P("והשלישית: אין מ-$A$ אל $B$ ואין מ-$A$ אל $C$. בהכרח אין מ-$C$ אל $B$? קחו את $C$ שווה ל-$B$.",
      do=show("b-4")),
    P("כל שפה מתרדדת לעצמה, בפונקציית הזהות. אז גם השלישית נופלת.", do=show("p2-x-c"), hold=0.2),
    P("ומכיוון שהטענה השנייה נכונה, גם האחרונה, ״כל הטענות האחרות לא נכונות״, נופלת.", do=show("p2-x-d"),
      hold=0.3),
    P("זכרו: אם אין מ-$A$ אל $B$ ויש מ-$B$ אל $C$, לא מסיקים כלום על $A$ ו-$C$.", do=show("b-t")),
    P("הכיוון שכן עובד: אם יש מ-$A$ אל $B$ ואין מ-$A$ אל $C$, אז אין מ-$B$ אל $C$. אחרת, הרכבה הייתה נותנת מ-$A$ אל $C$.",
      do=show("b-t2"), hold=0.5),
], stage='<div class="stack">'
         '<div id="b-1" class="bigmath h" style="font-size:40px">$A \\nleq_m B,\\ \\ B \\le_m C \\ \\Rightarrow\\ ?$</div>'
         + st.card("b-2", "ex", "$A = A_{TM}$, $B = 1\\Sigma^*$, $C = H_{TM}$")
         + st.card("b-3", "ex", "$A_{TM} \\nleq_m 1\\Sigma^*$, $1\\Sigma^* \\le_m H_{TM}$, $A_{TM} \\le_m H_{TM}$")
         + st.card("b-4", "ex", "$C = B$: תמיד $B \\le_m B$")
         + st.card("b-t", "trap", "⚠️ $A \\nleq_m B$, $B \\le_m C$: על $A$ ו-$C$ לא מסיקים כלום")
         + st.card("b-t2", "rule", "🔑 $A \\le_m B$, $A \\nleq_m C$: ולכן $B \\nleq_m C$")
         + "</div>",
   panel=stem(Q2, "$A, B, C$ שפות. הקו מסמן שאין רדוקציה. איזו טענה נכונה?") + st.options("p2", O2))

q3 = Scene("q3", "שאלה 3", [
    P("שאלה שלישית. $L$: המכונות שכל מילה שהן מקבלות היא פלינדרום.", do=show("c-l")),
    P("מנסים לרדד את המשלים של $H_{TM}$ אל $L$, עם המכונה $Q$ שבקוד.", do=show("c-code")),
    P("הפונקציה רק כותבת קוד, אז היא ניתנת לחישוב.", do=show("p3-x-b")),
    P("כיוון חיובי: $M$ לא עוצרת על $w$. אז $Q$ תקועה על כל פלינדרום, ודוחה כל השאר. היא לא מקבלת כלום.",
      do=show("c-1")),
    P("והשפה הריקה מוכלת בפלינדרומים: אין בה אף מילה שמפרה את התנאי. $Q$ ב-$L$, כנדרש.", do=show("c-2", "p3-x-d")),
    P("כיוון שלילי: $M$ עוצרת על $w$. אז $Q$ מקבלת בדיוק את כל הפלינדרומים.", do=show("c-3")),
    P("וזה עדיין מוכל בפלינדרומים. $Q$ ב-$L$ גם כאן, אבל הייתה צריכה להיות מחוץ ל-$L$.", do=show("c-4")),
    P("הכיוון השלילי נופל. $Q$ ב-$L$ תמיד, בלי קשר ל-$M$.", do=show("p3-ok-c", "p3-x-a"), hold=0.3),
    P("המלכודת כאן כפולה: אמת ריקה בצד אחד, ושני המקרים נוחתים באותו צד.", do=show("c-t"), hold=0.6),
], stage='<div class="stack">'
         '<div id="c-l" class="bigmath h" style="font-size:38px">$L = \\{\\langle M\\rangle \\mid L(M) \\subseteq PAL\\}$</div>'
         + w_map.code("c", Q_CODE).replace('class="codebox"', 'class="codebox h" style="font-size:28px"')
         .replace('id="c"', 'id="c-code"')
         + st.card("c-1", "ex", "$M$ לא עוצרת: $L(Q) = \\emptyset$<span id=\"c-2\" class=\"h\">, $Q \\in L$ ✓</span>")
         + st.card("c-3", "trap", "⚠️ $M$ עוצרת: $L(Q) = PAL$<span id=\"c-4\" class=\"h\">, $Q \\in L$ ✗</span>")
         + st.card("c-t", "trap", "⚠️ אמת ריקה, ושני המקרים באותו צד")
         + "</div>",
   panel=stem(Q3, "$f(\\langle M,w\\rangle) = \\langle Q\\rangle$, רדוקציה מ-$\\overline{H_{TM}}$ אל $L$?")
         + st.options("p3", O3))

recap = Scene("recap", "סיכום", [
    P("סיכום הפרק. בכל שאלה על רדוקציה, שאלו קודם: מי המקור, ומי היעד?", do=show("r-1")),
    P("קלות זורמת אל המקור, קושי אל היעד, ובמשלים הכול עובר באותה פונקציה.", do=show("r-2")),
    P("שפה כריעה מתרדדת לכל שפה לא טריוויאלית, ולכן ממנה לא מסיקים כלום.", do=show("r-3")),
    P("ופונקציה מפילים בדוגמה אחת, בדרך כלל בכיוון השלילי. בהצלחה במבחן!", do=show("r-4"), hold=0.8),
], stage='<div class="stack"><div class="bigmath">$x \\in A \\iff f(x) \\in B$</div></div>',
   panel=st.card("r-1", "rule", "🔑 מי המקור? מי היעד?")
         + st.card("r-2", "rule", "🔑 קלות אל המקור, קושי אל היעד")
         + st.card("r-3", "rule", "🔑 כריעה: מתרדדת לכל לא טריוויאלית")
         + st.card("r-4", "trap", "⚠️ דוגמה אחת מפילה, בדרך כלל בכיוון השלילי"))

VIDEO = Video("M07", "map", "מבחן גמר: רדוקציות מיפוי", [title, kit, q1, q2, q3, recap],
              bank={"23A-A-Q9": "d", "24B-A-Q6": "b", "24A-A-Q13": "c"})
