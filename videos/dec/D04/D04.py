# -*- coding: utf-8 -*-
"""D04 · טבלת הסגירות — video script (build: tools/video/vid.py D04).

Source: tools/courses_src/dec/D04.js (lesson + goal). Exam anchor: 23A-B-Q3 (A∩B and A∪B decidable say nothing about A
and B), which no guided quiz uses. Not used on purpose: the quiz questions of D04 (the five original ones and 24A-A-Q4,
the A#B closure) and 22A-B-Q6 (cited by the lesson).
Every cell of the closure table is checked with the course closure engine (rules.claim_truth). The union run uses two
real machines (asserted with run_tm): A = words with a 1, B = words without a 1; on 00 the machine of A never halts.
The exam's counterexamples are evaluated in the engine's 4-language model (∅, Σ*, A_TM, its complement).
"""
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, BLANK, run_tm, words
from rules import claim_truth, Mod, FACTS
import stage as st
import w_dec

# ---------------------------------------------------------------- the closure table (verified)
OPS = [("A | B", "איחוד $A \\cup B$"), ("A & B", "חיתוך $A \\cap B$"), ("~A", "משלים $\\overline{A}$"),
       ("A @ B", "שרשור $AB$")]
CLS = ["R", "RE", "coRE"]
TRUTH = {(e, c): claim_truth(e, {"A": c, "B": c}, f"always:{c}") for e, _ in OPS for c in CLS}
assert TRUTH == {(e, c): not (e == "~A" and c != "R") for e, _ in OPS for c in CLS}
YES, NO = '<b class="yes">כן</b>', '<b class="no">לא</b>'
ROWS = [[label] + [YES if TRUTH[(e, c)] else NO for c in CLS] for e, label in OPS]

# ---------------------------------------------------------------- the union run (verified)
MA = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): ("q_0", BLANK, "R")}
MB = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): ("q_1", "1", "R"), ("q_0", BLANK): (ACC, BLANK, "R"),
      ("q_1", "0"): ("q_1", "0", "R"), ("q_1", "1"): ("q_1", "1", "R"), ("q_1", BLANK): ("q_1", BLANK, "R")}


def union_run(w, cap=60):
    for k in range(1, cap):                 # one step of each, alternately; accept when either accepted
        if run_tm(MA, "q_0", w, k + 1)[0] == "accept" or run_tm(MB, "q_0", w, k + 1)[0] == "accept":
            return "accept", k
    return "loop", cap


for w in words(6):
    assert run_tm(MA, "q_0", w)[0] == ("accept" if "1" in w else "loop")
    assert run_tm(MB, "q_0", w)[0] == ("loop" if "1" in w else "accept")
    assert union_run(w)[0] == "accept"                    # A ∪ B = Σ*
assert run_tm(MA, "q_0", "00")[0] == "loop" and union_run("00") == ("accept", 3)

# ---------------------------------------------------------------- exam 23A-B-Q3 (model counterexamples)
Q = BANK["23A-B-Q3"]
assert Q["correctId"] == "d"
E, S, X, CX = 0b00, 0b11, 0b01, 0b10                       # ∅, Σ*, A_TM, complement of A_TM
OKP = [(a, b) for a in (E, S, X, CX) for b in (E, S, X, CX)
       if (Mod(a) & Mod(b)).b in (E, S) and (Mod(a) | Mod(b)).b in (E, S)]
assert (X, CX) in OKP and (E, E) in OKP
assert FACTS["A_TM"] == "RE\\R"                            # A = A_TM: not in R (a), and in RE∖R (c)
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נבנה את טבלת הסגירות של $R$, $RE$ ו-$coRE$."),
    P("ולכל כניסה בטבלה נמצא רעיון אחד שמסביר אותה, כדי שלא נצטרך לשנן.", hold=0.4),
], stage='<div class="kicker">D04 · כריעות, סגירות וסיווג</div><h1>טבלת הסגירות</h1>'
         '<p>לדעת אילו פעולות משמרות R, RE ו-coRE, ולהסביר כל כניסה בטבלה ברעיון אחד.</p>', layout="title")

what = Scene("what", "מה זה סגירות", [
    P("מחלקה **סגורה** לפעולה, אם הפעולה על שפות מהמחלקה תמיד נשארת בתוכה.", do=show("w-1")),
    P("למשל: אם $A$ ו-$B$ ב-$RE$, האם האיחוד שלהן חייב להיות ב-$RE$?", do=show("w-2")),
    P("״חייב״ זו מילת המפתח: התשובה צריכה להיות נכונה לכל שתי שפות במחלקה.", do=show("w-3"), hold=0.4),
], stage='<div class="stack"><div id="w-2" class="bigmath h">$A, B \\in RE \\ \\Rightarrow\\ A \\cup B \\in RE\\ ?$</div></div>',
   panel=st.card("w-1", "rule", "🔑 סגורה: הרכיבים במחלקה ⇐ התוצאה <b>בהכרח</b> במחלקה")
         + st.card("w-3", "trap", "⚠️ ״בהכרח״: לכל שתי שפות, בלי יוצא מן הכלל"))

TAB = w_dec.table("t", ["פעולה", "$R$", "$RE$", "$coRE$"], ROWS, cls="big")
table = Scene("table", "הטבלה", [
    P("הנה הטבלה. איחוד: כל שלוש המחלקות סגורות לו.", do=show("t-r0")),
    P("חיתוך: גם כן, בכל השלוש.", do=show("t-r1")),
    P("משלים: רק $R$ סגורה. $RE$ ו-$coRE$ **לא**.", do=show("t-r2", "t-hl2")),
    P("ושרשור, וגם כוכב: שוב כל השלוש.", do=hide("t-hl2") + show("t-r3")),
    P("שורה אחת יוצאת דופן: המשלים. עכשיו נבין כל שורה.", hold=0.4),
], stage=TAB)

UN = ('<div class="lanes">'
      + w_dec.lane("u1", "M_A", 3, end="∞ לא עוצרת", end_kind="loop")
      + w_dec.lane("u2", "M_B", 3, end="✓ מקבלת", end_kind="ok")
      + '<div id="u-v" class="verdict ok h">$00 \\in A \\cup B$: מקבלים</div></div>')
union = Scene("union", "איחוד וחיתוך", [
    P("איחוד ב-$RE$: יש מכונה שמקבלת את $A$, ומכונה שמקבלת את $B$. איך מקבלים את האיחוד?", do=show("u-1")),
    P("ניקח $A$: מילים שיש בהן אחת, ו-$B$: מילים בלי אחת. והמילה $00$.", do=show("u-2"),
      say="ניקח אֵיי: מילים שיש בהן אחת, ובִּי: מילים בלי אחת. והמילה אפס אפס."),
    P("אם נריץ קודם את המכונה של $A$, היא תרוץ לנצח על $00$, ולא נגיע ל-$B$.",
      do=show("u1", "u1-b0", "u1-b1", "u1-b2", "u1-end"),
      say="אם נריץ קודם את המכונה של אֵיי, היא תרוץ לנצח על אפס אפס, ולא נגיע לבִּי."),
    P("לכן מריצים את שתיהן **במקביל**, צעד מכל אחת. המכונה של $B$ מקבלת אחרי שלושה צעדים.",
      do=show("u2", "u2-b0", "u2-b1", "u2-b2", "u2-end")),
    P("ברגע שאחת קיבלה, מקבלים. המילה באיחוד.", do=show("u-v")),
    P("ובחיתוך? כאן אפשר גם בזו אחר זו: אם אחת רצה לנצח, המילה ממילא לא בחיתוך.", do=show("u-3")),
    P("ושרשור וכוכב: מכונה אי-דטרמיניסטית מנחשת איפה לחתוך את המילה, ובודקת כל חלק.", do=show("u-4"),
      hold=0.4),
], stage=UN,
   panel=st.card("u-1", "plain", "$M_A$ מקבלת את $A$, $M_B$ מקבלת את $B$")
         + st.card("u-2", "ex", "$A$: מילים עם $1$. $B$: מילים בלי $1$")
         + st.card("u-3", "rule", "🔑 חיתוך: בזו אחר זו, ומקבלים אם שתיהן קיבלו")
         + st.card("u-4", "rule", "🔑 שרשור: מנחשים נקודת חיתוך $w = uv$"))

comp = Scene("comp", "משלים", [
    P("משלים ב-$R$: מחליפים בין $q_{acc}$ ל-$q_{rej}$ במכונה המכריעה. היא עוצרת תמיד, אז זה עובד.",
      do=show("c-1")),
    P("ב-$RE$ זה נשבר. $A_{TM}$ ב-$RE$, והמשלים שלה כבר לא.", do=show("v-l-atm", "v-l-coatm", "c-2")),
    P("אילו $RE$ הייתה סגורה למשלים, כל שפה ב-$RE$ הייתה כריעה, לפי משפט פוסט.", do=show("c-3")),
    P("משלים לא נשאר במקום: הוא **הופך** $RE$ ל-$coRE$, ו-$coRE$ ל-$RE$.", do=show("c-4"), hold=0.4),
], stage=w_dec.venn("v", [("atm", "A_{TM}", "A_TM"), ("coatm", "\\overline{A_{TM}}", "coA_TM")]),
   panel=st.card("c-1", "rule", "🔑 $R$: מחליפים $q_{acc}$ ו-$q_{rej}$")
         + st.card("c-2", "trap", "⚠️ $A_{TM} \\in RE$, אבל $\\overline{A_{TM}} \\notin RE$")
         + st.card("c-3", "plain", "סגורה למשלים ⇐ $RE = R$, וזה לא נכון")
         + st.card("c-4", "rule", "🔑 $A \\in RE \\iff \\overline{A} \\in coRE$"))

mirror = Scene("mirror", "coRE", [
    P("ומה עם $coRE$? היא תמונת מראה של $RE$, וכל סגירות עוברת אליה דרך המשלים.", do=show("m-1")),
    P("למשל איחוד: אם $A$ ו-$B$ ב-$coRE$, המשלימים שלהן ב-$RE$.", do=show("m-2")),
    P("החיתוך של המשלימים ב-$RE$. והמשלים שלו הוא בדיוק האיחוד, לפי דה-מורגן.", do=show("m-3")),
    P("לכן האיחוד ב-$coRE$. באותה דרך עובדים כל שאר התאים.", do=show("m-4"), hold=0.4),
], stage='<div class="stack">'
         '<div id="m-2" class="bigmath h" style="font-size:44px">$\\overline{A}, \\overline{B} \\in RE$</div>'
         '<div id="m-3" class="bigmath h" style="font-size:44px">$A \\cup B = \\overline{\\overline{A} \\cap \\overline{B}}$</div>'
         '</div>',
   panel=st.card("m-1", "rule", "🔑 $coRE$: תמונת מראה של $RE$")
         + st.card("m-4", "ex", "$\\overline{A} \\cap \\overline{B} \\in RE$ ⇐ $A \\cup B \\in coRE$"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: החיתוך של $A$ ו-$B$ כריע, וגם האיחוד שלהן כריע. מה נכון?"),
    P("שימו לב לכיוון: סגירות עובדת מהרכיבים אל התוצאה. כאן נתונה התוצאה, ושואלים על הרכיבים.", do=show("x-1")),
    P("ננסה להפריך. נציב $A = A_{TM}$, ו-$B$ המשלים שלה.", do=show("x-2")),
    P("החיתוך ריק והאיחוד הוא $\\Sigma^*$. שתיהן כריעות, אז הנתונים מתקיימים.", do=show("x-3")),
    P("אבל $A_{TM}$ לא כריעה. זה מפיל את ״שתיהן בהכרח כריעות״.", do=show("q-x-a")),
    P("ו-$A_{TM}$ היא בדיוק ב-$RE$ מחוץ ל-$R$, אז גם הטענה ששתיהן **לא** שם נופלת.", do=show("q-x-c")),
    P("והאפשרות האמצעית? ניקח $A$ ו-$B$ ריקות. הן לא ב-$RE$ מחוץ ל-$R$, והיא נופלת.", do=show("x-4", "q-x-b")),
    P("אז אף אחת מהטענות לא נכונה בהכרח.", do=show("q-ok-d"), hold=0.6),
], stage='<div class="stack">'
         + st.card("x-1", "trap", "⚠️ נתונה התוצאה, לא הרכיבים")
         + '<div id="x-2" class="bigmath h" style="font-size:42px">$A = A_{TM},\\ \\ B = \\overline{A_{TM}}$</div>'
         + '<div id="x-3" class="bigmath h" style="font-size:42px">$A \\cap B = \\emptyset,\\ \\ A \\cup B = \\Sigma^*$</div>'
         + st.card("x-4", "ex", "$A = B = \\emptyset$: גם כן חיתוך ואיחוד כריעים")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$A \\cap B \\in R$ וגם $A \\cup B \\in R$. '
         'איזו טענה נכונה?</div>'
         + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $R$ סגורה לכל הפעולות.", do=show("r-1")),
    P("$RE$ ו-$coRE$ סגורות לאיחוד, חיתוך, שרשור וכוכב. איחוד ב-$RE$ מריצים במקביל.", do=show("r-2")),
    P("משלים הופך $RE$ ל-$coRE$, ולכן הן לא סגורות לו.", do=show("r-3")),
    P("וסגירות עובדת רק מהרכיבים לתוצאה, לא להפך. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage=w_dec.table("rt", ["פעולה", "$R$", "$RE$", "$coRE$"], ROWS, hide_rows=False, cls="big"),
   panel=st.card("r-1", "rule", "🔑 $R$: הכול")
         + st.card("r-2", "rule", "🔑 $RE$, $coRE$: הכול חוץ ממשלים")
         + st.card("r-3", "rule", "🔑 משלים: $RE \\leftrightarrow coRE$")
         + st.card("r-4", "trap", "⚠️ תוצאה כריעה לא אומרת כלום על הרכיבים"))

VIDEO = Video("D04", "dec", "טבלת הסגירות", [title, what, table, union, comp, mirror, exam, recap],
              bank={"23A-B-Q3": "d"})
