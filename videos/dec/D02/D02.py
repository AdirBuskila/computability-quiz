# -*- coding: utf-8 -*-
"""D02 · משפט פוסט והרצה מקבילה — video script (build: tools/video/vid.py D02).

Source: tools/courses_src/dec/D02.js (lesson + goal). Exam anchor: 25S-B-Q12 (A∩B and its complement both in RE
does not make A and B decidable), which no guided quiz uses. Not used on purpose: the quiz questions of D02 (the four
original ones and 20A-B-Q1, the inclusion sandwich), and 20A-B-Q24 / 23S-A-Q4 (cited by the lesson).
The two machines of the parallel run are real: L = words with a 1. M1 accepts L (runs right forever on a word with no
1), M2 accepts its complement (runs right forever after a 1). Alternating single steps decides L on every word up to
length 6 (asserted with the course checker's run_tm). The swap trap uses M1 too.
"""
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, REJ, BLANK, run_tm, words
from rules import FACTS, RULES, model_classes
import stage as st
import w_dec

# ---------------------------------------------------------------- machines (verified)
M1 = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): ("q_0", BLANK, "R")}
M2 = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): ("q_1", "1", "R"), ("q_0", BLANK): (ACC, BLANK, "R"),
      ("q_1", "0"): ("q_1", "0", "R"), ("q_1", "1"): ("q_1", "1", "R"), ("q_1", BLANK): ("q_1", BLANK, "R")}


def alternate(w, cap=60):
    """one step of M1, one step of M2, ...: the first to accept decides"""
    for k in range(1, cap):
        if run_tm(M1, "q_0", w, k + 1)[0] == "accept":   # halted within k steps
            return "accept", k
        if run_tm(M2, "q_0", w, k + 1)[0] == "accept":
            return "reject", k
    return "loop", cap


for w in words(6):
    in_L = "1" in w
    assert run_tm(M1, "q_0", w)[0] == ("accept" if in_L else "loop")
    assert run_tm(M2, "q_0", w)[0] == ("loop" if in_L else "accept")
    assert alternate(w)[0] == ("accept" if in_L else "reject"), w
# on 00: M1 never halts, M2 accepts after 3 steps -> the alternation stops after M2's 3rd step and rejects
assert run_tm(M1, "q_0", "00")[0] == "loop" and run_tm(M2, "q_0", "00")[:2] == ("accept", 3)
assert alternate("00") == ("reject", 3)

# swap q_acc and q_rej in M1: the words with no 1 still loop, so the new language is empty, not the complement
SW = {k: ({ACC: REJ, REJ: ACC}.get(v[0], v[0]),) + v[1:] for k, v in M1.items()}
assert run_tm(SW, "q_0", "01")[0] == "reject" and run_tm(SW, "q_0", "00")[0] == "loop"
assert all(run_tm(SW, "q_0", w)[0] != "accept" for w in words(6))

# course facts
assert RULES["post.both_RE"][0] and RULES["swap.decider"][0] and not RULES["swap.nonhalting"][0]
assert RULES["compl.RE_notR_not_RE"][0] and RULES["compl.R_closed"][0] and not RULES["compl.RE_closed"][0]
assert FACTS["A_TM"] == "RE\\R" and FACTS["coA_TM"] == "coRE\\R"

# exam 25S-B-Q12: A = A_TM, B = its complement: A∩B is empty (in R), yet A is not decidable
Q = BANK["25S-B-Q12"]
assert Q["correctId"] == "a"
assert model_classes("A & B", {"A": "RE\\R", "B": "coRE\\R"}) == {"R"}
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר את משפט פוסט: הקשר בין $R$, $RE$ ו-$coRE$."),
    P("נראה למה מריצים שתי מכונות לסירוגין, ואיזו טעות נפוצה מסתתרת בהחלפת מצבים.", hold=0.4),
], stage='<div class="kicker">D02 · כריעות, סגירות וסיווג</div><h1>משפט פוסט והרצה מקבילה</h1>'
         '<p>לדעת ש-R הוא בדיוק RE ∩ coRE, להסביר למה מריצים שתי מכונות לסירוגין, ולא ליפול במלכודות של "הכלה" '
         'ו"החלפת מצבים".</p>', layout="title")

thm = Scene("thm", "המשפט", [
    P("המשפט: $L$ כריעה אם ורק אם גם $L$ וגם המשלים שלה ניתנות לקבלה.", do=show("t-f")),
    P("במילים אחרות, $R$ היא בדיוק החיתוך של $RE$ ו-$coRE$.", do=show("t-g")),
    P("הכיוון הקל: נניח שיש מכונה שמכריעה את $L$. היא בפרט מקבלת אותה.", do=show("t-1")),
    P("ואם נחליף בה בין $q_{acc}$ ל-$q_{rej}$, נקבל מכונה שמכריעה את המשלים.", do=show("t-2")),
    P("זה עובד רק כי המכונה **עוצרת** על כל קלט. נחזור לזה בהמשך.", do=show("t-3"), hold=0.4),
], stage='<div class="stack"><div id="t-f" class="bigmath h">'
         '$L \\in R \\iff L \\in RE,\\ \\overline{L} \\in RE$</div>'
         '<div id="t-g" class="bigmath h">$R = RE \\cap coRE$</div></div>',
   panel=st.card("t-1", "ex", "מכריעה ⇐ בפרט מקבלת")
         + st.card("t-2", "ex", "מחליפים $q_{acc}$ ו-$q_{rej}$: מכריעה למשלים")
         + st.card("t-3", "trap", "⚠️ ההחלפה עובדת רק במכונה שעוצרת תמיד"))

SEQ = ('<div class="lanes">'
       + w_dec.lane("s1", "M_1", 7, end="∞ לא עוצרת", end_kind="loop")
       + w_dec.lane("s2", "M_2", 0, end="לא מגיעים אליה", end_kind="bad")
       + "</div>")
seq = Scene("seq", "הכיוון המעניין", [
    P("הכיוון המעניין: יש $M_1$ שמקבלת את $L$, ו-$M_2$ שמקבלת את המשלים.", do=show("q-1")),
    P("ניקח דוגמה: $L$ היא המילים שיש בהן אחת. $M_1$ זזה ימינה עד שהיא רואה אחת, ואז מקבלת.", do=show("q-2"),
      say="ניקח דוגמה: אֵל היא המילים שיש בהן אחת. אֵם אחת זזה ימינה עד שהיא רואה אחת, ואז מקבלת."),
    P("$M_2$ זזה ימינה עד הרווח ומקבלת, אבל אחרי אחת היא רצה לנצח.", do=show("q-3")),
    P("רעיון ראשון: להריץ את $M_1$ עד הסוף, ורק אחר כך את $M_2$. ננסה על המילה $00$.", do=show("s1"),
      say="רעיון ראשון: להריץ את אֵם אחת עד הסוף, ורק אחר כך את אֵם שתיים. ננסה על המילה אפס אפס."),
    P("$M_1$ לא רואה אחת אף פעם, וממשיכה ימינה ברווחים.", do=show(*[f"s1-b{i}" for i in range(7)])),
    P("היא לא עוצרת, ולכן לעולם לא מגיעים ל-$M_2$, שהייתה עונה אחרי שלושה צעדים.", do=show("s1-end", "s2-end")),
    P("ריצה בזו אחר זו נתקעת בדיוק כשהמכונה הראשונה בלולאה.", do=show("q-4"), hold=0.4),
], stage=SEQ,
   panel=st.card("q-1", "plain", "$L(M_1) = L$, $L(M_2) = \\overline{L}$")
         + st.card("q-2", "ex", "$L$: מילים שיש בהן $1$")
         + st.card("q-3", "ex", "$M_2$: מקבלת מילים בלי $1$")
         + st.card("q-4", "trap", "⚠️ בזו אחר זו: נתקעים בלולאה של $M_1$"))

ALT = ('<div class="lanes">'
       + w_dec.lane("p1", "M_1", 3, end="עדיין רצה", end_kind="loop")
       + w_dec.lane("p2", "M_2", 3, end="✓ מקבלת", end_kind="ok")
       + '<div id="p-v" class="verdict bad h">המילה לא ב-$L$: דוחים</div></div>')
par = Scene("par", "לסירוגין", [
    P("הפתרון: מריצים את שתיהן **לסירוגין**, צעד אחד מכל אחת.", do=show("p1", "p2")),
    P("צעד של $M_1$.", do=show("p1-b0")),
    P("צעד של $M_2$.", do=show("p2-b0")),
    P("עוד צעד של $M_1$, ועוד צעד של $M_2$.", do=show("p1-b1", "p2-b1")),
    P("ושוב $M_1$, ושוב $M_2$, והפעם $M_2$ הגיעה לרווח וקיבלה.", do=show("p1-b2", "p2-b2", "p2-end", "p1-end")),
    P("מכיוון ש-$M_2$ קיבלה, המילה במשלים, והמכונה המשולבת דוחה.", do=show("p-v")),
    P("ולמה זה תמיד נגמר? כל מילה נמצאת ב-$L$ או במשלים שלה.", do=show("p-c1")),
    P("לכן אחת משתי המכונות **חייבת** לקבל אחרי מספר סופי של צעדים, והמכונה המשולבת עוצרת תמיד.",
      do=show("p-c2"), hold=0.4),
], stage=ALT,
   panel=st.card("p-c1", "rule", "🔑 כל מילה: ב-$L$ או ב-$\\overline{L}$")
         + st.card("p-c2", "rule", "🔑 אחת מהן מקבלת בזמן סופי, ולכן המשולבת <b>מכריעה</b>"))

VENN = w_dec.venn("v", [("atm", "A_{TM}", "A_TM"), ("coatm", "\\overline{A_{TM}}", "coA_TM")])
cons = Scene("cons", "מסקנות", [
    P("מסקנה ראשונה: $A_{TM}$ ב-$RE$ ולא כריעה.", do=show("v-l-atm")),
    P("אם גם המשלים שלה היה ב-$RE$, לפי המשפט היא הייתה כריעה. סתירה.", do=show("c-1")),
    P("לכן המשלים של $A_{TM}$ **לא** ב-$RE$. הוא ב-$coRE$ בלבד.", do=show("v-l-coatm", "v-f-coRE")),
    P("מסקנה שנייה: $RE$ לא סגורה למשלים. המשלים הוציא אותנו ממנה.", do=hide("v-f-coRE") + show("c-2")),
    P("ואילו $R$ סגורה למשלים: זה הכיוון הקל, החלפת המצבים.", do=show("v-f-R", "c-3"), hold=0.4),
], stage=VENN,
   panel=st.card("c-1", "rule", "🔑 $L \\in RE \\setminus R$ ⇐ $\\overline{L} \\notin RE$")
         + st.card("c-2", "trap", "⚠️ $RE$ ו-$coRE$ לא סגורות למשלים")
         + st.card("c-3", "rule", "🔑 $R$ סגורה למשלים"))

SWT = w_dec.table("sw", ["מילה", "$M_1$", "אחרי ההחלפה"], [
    ["$01$", "מקבלת", "דוחה"],
    ["$00$", "∞ לא עוצרת", "∞ לא עוצרת"],
], hide_cells=[(0, 2), (1, 2)])
swap = Scene("swap", "מלכודת ההחלפה", [
    P("ועכשיו המלכודת. מה קורה אם מחליפים את $q_{acc}$ ו-$q_{rej}$ במכונה שלא עוצרת תמיד?"),
    P("ניקח שוב את $M_1$. על $01$ היא מקבלת, ואחרי ההחלפה היא דוחה. עד כאן טוב.", do=show("sw-r0", "sw-c0-2"),
      say="ניקח שוב את אֵם אחת. על אפס אחת היא מקבלת, ואחרי ההחלפה היא דוחה. עד כאן טוב."),
    P("אבל על $00$ היא רצה לנצח. ההחלפה לא נוגעת בזה: היא עדיין רצה לנצח.", do=show("sw-r1", "sw-c1-2"),
      say="אבל על אפס אפס היא רצה לנצח. ההחלפה לא נוגעת בזה: היא עדיין רצה לנצח."),
    P("אז המכונה החדשה לא מקבלת אף מילה. השפה שלה ריקה, ולא המשלים של $L$.", do=show("w-1")),
    P("החלפת מצבים נותנת משלים **רק** במכונה שעוצרת על כל קלט.", do=show("w-2"), hold=0.4),
], stage=SWT,
   panel=st.card("w-1", "ex", "אחרי ההחלפה: $L(M') = \\emptyset$, ולא $\\overline{L}$")
         + st.card("w-2", "trap", "⚠️ החלפת $q_{acc}$ ו-$q_{rej}$: משלים רק במכונה מכריעה"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: $A$ ו-$B$ לא טריוויאליות. החיתוך שלהן ב-$RE$, וגם המשלים של החיתוך ב-$RE$.",
      say="שאלה ממבחן: אֵיי ובִּי לא טריוויאליות. החיתוך שלהן באָר אִי, וגם המשלים של החיתוך באָר אִי."),
    P("הטענה: אז גם $A$ וגם $B$ כריעות. נכון?"),
    P("לפי משפט פוסט, החיתוך עצמו כריע. אבל זה לא אומר כלום על כל אחת לבד.", do=show("x-1")),
    P("נציב $A = A_{TM}$, ו-$B$ המשלים שלה. שתיהן לא טריוויאליות.", do=show("x-2")),
    P("החיתוך שלהן ריק, כי אין זוג שגם בשפה וגם במשלים שלה.", do=show("x-3")),
    P("הריקה ב-$RE$, והמשלים שלה, $\\Sigma^*$, גם ב-$RE$. הנתונים מתקיימים.", do=show("x-4")),
    P("אבל $A_{TM}$ לא כריעה. לכן הטענה לא נכונה.", do=show("q-ok-a", "q-x-b"), hold=0.6),
], stage='<div class="stack">'
         + st.card("x-1", "rule", "🔑 פוסט: $A \\cap B \\in R$, ולא יותר")
         + '<div id="x-2" class="bigmath h" style="font-size:42px">$A = A_{TM},\\ \\ B = \\overline{A_{TM}}$</div>'
         + '<div id="x-3" class="bigmath h" style="font-size:42px">$A \\cap B = \\emptyset$</div>'
         + st.card("x-4", "ex", "$\\emptyset \\in RE$ וגם $\\Sigma^* \\in RE$, אבל $A_{TM} \\notin R$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$A, B$ לא טריוויאליות, $A \\cap B \\in RE$ '
         'וגם $\\overline{A \\cap B} \\in RE$. אזי $A \\in R$ וגם $B \\in R$.</div>'
         + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $L$ כריעה אם ורק אם גם $L$ וגם המשלים שלה ב-$RE$.", do=show("r-1")),
    P("ההוכחה מריצה שתי מכונות לסירוגין, כי אחת מהן עלולה לרוץ לנצח.", do=show("r-2")),
    P("מכאן: המשלים של שפה ב-$RE$ שאינה כריעה לא ב-$RE$.", do=show("r-3")),
    P("והחלפת מצבים נותנת משלים רק במכונה מכריעה. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$R = RE \\cap coRE$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $L \\in R \\iff L, \\overline{L} \\in RE$")
         + st.card("r-2", "rule", "🔑 לסירוגין, לא בזו אחר זו")
         + st.card("r-3", "rule", "🔑 $\\overline{A_{TM}} \\notin RE$")
         + st.card("r-4", "trap", "⚠️ החלפת מצבים: רק במכונה מכריעה"))

VIDEO = Video("D02", "dec", "משפט פוסט והרצה מקבילה", [title, thm, seq, par, cons, swap, exam, recap],
              bank={"25S-B-Q12": "a"})
