# -*- coding: utf-8 -*-
"""D03 · השפות המפורסמות והמחלקה של כל אחת — video script (build: tools/video/vid.py D03).

Source: tools/courses_src/dec/D03.js (lesson + goal). Exam anchor: 23B-A-Q8 ({<M,w> | w ∉ L(M)}, the complement of
A_TM in disguise), which no guided quiz uses. Not used on purpose: the quiz questions of D03 (the five original ones
and 25B-B-Q5, H_TM vs the complement of A_TM), and 23A-B-Q16 / 22A-B-Q5 (cited by the lesson).
Every class comes from the course fact table (rules.FACTS). The dovetailing grid is a real run: the machine accepts the
words that contain a 1 and runs forever on the others (asserted with run_tm), so running it on ε alone never ends.
"""
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, BLANK, run_tm, words
from rules import FACTS, complement_class
import stage as st
import w_dec

# ---------------------------------------------------------------- facts and the dovetailing run (verified)
assert FACTS["A_TM"] == FACTS["H_TM"] == FACTS["notE_TM"] == "RE\\R"
assert FACTS["coA_TM"] == FACTS["coH_TM"] == FACTS["E_TM"] == "coRE\\R"
assert FACTS["EQ_TM"] == FACTS["ALL_TM"] == "none" and FACTS["A_DFA"] == "R"
assert complement_class(FACTS["notE_TM"]) == FACTS["E_TM"]

M = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): ("q_0", BLANK, "R")}
for w in words(6):
    assert run_tm(M, "q_0", w)[0] == ("accept" if "1" in w else "loop")
ORDER = ["", "0", "1"]                                    # the first three words in the standard order


def within(w, k):
    """M accepted w within k steps"""
    return run_tm(M, "q_0", w, k + 1)[0] == "accept"


# stage i runs i steps on the first i words; the first acceptance comes at stage 3, on the word 1
GRID = [[("✓" if within(w, i) else "…") if j < i else "" for j, w in enumerate(ORDER)] for i in (1, 2, 3)]
assert GRID == [["…", "", ""], ["…", "…", ""], ["…", "…", "✓"]]

# exam 23B-A-Q8: {<M,w> | w not in L(M)} is the complement of A_TM
Q = BANK["23B-A-Q8"]
assert Q["correctId"] == "a" and complement_class(FACTS["A_TM"]) == "coRE\\R"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נעבור על השפות המפורסמות של הקורס, ונשייך כל אחת למחלקה שלה."),
    P("ולכל שורה בטבלה נבין **למה** היא שם, כדי שלא נצטרך לשנן.", hold=0.4),
], stage='<div class="kicker">D03 · כריעות, סגירות וסיווג</div><h1>השפות המפורסמות והמחלקה של כל אחת</h1>'
         '<p>לזכור את הטבלה: לאיזו מחלקה שייכת כל אחת מהשפות A_TM, H_TM, E_TM, EQ_TM ושל המשלימות שלהן, ולנמק למה.</p>',
   layout="title")

ROWS = [
    ("d-a", "A_{TM}", "המכונה $M$ <b>מקבלת</b> את $w$"),
    ("d-h", "H_{TM}", "המכונה $M$ <b>עוצרת</b> על $w$"),
    ("d-e", "E_{TM}", "השפה $L(M)$ <b>ריקה</b>"),
    ("d-q", "EQ_{TM}", "$L(M_1) = L(M_2)$"),
    ("d-l", "ALL_{TM}", "$L(M) = \\Sigma^*$"),
]
defs = Scene("defs", "השפות", [
    P("חמש שפות, והשמות שלהן קבועים בכל שאלה."),
    P("$A_{TM}$: זוגות של מכונה ומילה, שבהם המכונה **מקבלת** את המילה.", do=show("d-a")),
    P("$H_{TM}$: זוגות שבהם המכונה **עוצרת** על המילה, גם אם היא דוחה.", do=show("d-h")),
    P("$E_{TM}$: מכונות שהשפה שלהן ריקה. הן לא מקבלות אף מילה.", do=show("d-e")),
    P("$EQ_{TM}$: זוגות של מכונות עם אותה שפה. ו-$ALL_{TM}$: מכונות שמקבלות כל מילה.", do=show("d-q", "d-l"),
      hold=0.4),
], stage='<div class="tuple">'
         + "".join(f'<div id="{i}" class="row h"><span class="sym">${s}$</span><span>{t}</span></div>' for i, s, t in ROWS)
         + "</div>")

atm = Scene("atm", "A_TM ו-H_TM", [
    P("נתחיל מ-$A_{TM}$. איך מקבלים אותה? פשוט מריצים את $M$ על $w$.", do=show("a-1")),
    P("אם $M$ קיבלה, מקבלים. אם דחתה, דוחים. ואם היא רצה לנצח, גם אנחנו.", do=show("a-2")),
    P("זה מותר במכונה מקבלת. לכן $A_{TM}$ ב-$RE$.", do=show("v-l-atm")),
    P("אבל היא לא כריעה. את ההוכחה נראה בקורס הרדוקציות.", do=show("a-3")),
    P("ומשפט פוסט נותן את השאר: המשלים של $A_{TM}$ לא ב-$RE$. הוא ב-$coRE$ בלבד.", do=show("v-l-coatm")),
    P("$H_{TM}$ עובדת אותו דבר: מריצים, ומקבלים ברגע שהמכונה עצרה, גם אם דחתה.", do=show("v-l-htm")),
    P("שימו לב: $H_{TM}$ אינה המשלים של $A_{TM}$.", do=show("a-4")),
    P("זוג שבו המכונה **דוחה** נמצא בשתיהן: ב-$H_{TM}$, כי היא עצרה, וגם במשלים של $A_{TM}$, כי היא לא קיבלה.",
      hold=0.4, say="זוג שבו המכונה דוחה נמצא בשתיהן: באֵייץ' טִי אֶם, כי היא עצרה, "
                    "וגם במשלים של אֵיי טִי אֶם, כי היא לא קיבלה."),
], stage=w_dec.venn("v", [("atm", "A_{TM}", "A_TM"), ("htm", "H_{TM}", "H_TM"),
                          ("coatm", "\\overline{A_{TM}}", "coA_TM")]),
   panel=st.card("a-1", "ex", "מריצים את $M$ על $w$")
         + st.card("a-2", "plain", "קיבלה ⇐ מקבלים. רצה לנצח ⇐ גם אנחנו")
         + st.card("a-3", "rule", "🔑 $A_{TM} \\in RE \\setminus R$")
         + st.card("a-4", "trap", "⚠️ $H_{TM}$ כוללת גם זוגות שבהם $M$ <b>דוחה</b>"))

GRIDTAB = w_dec.table("g", ["שלב", "$\\varepsilon$", "$0$", "$1$"],
                      [["1 צעד"] + GRID[0], ["2 צעדים"] + GRID[1], ["3 צעדים"] + GRID[2]], cls="big")
dove = Scene("dove", "שפה לא ריקה", [
    P("עכשיו $E_{TM}$. קל יותר להתחיל מהמשלים שלה: מכונות שמקבלות **לפחות מילה אחת**.", do=show("e-1")),
    P("כדי לענות כן, מספיק למצוא מילה אחת שהמכונה מקבלת. אבל איזו? ומה אם היא רצה לנצח על חלק מהמילים?"),
    P("ניקח מכונה שמקבלת מילים עם אחת, ורצה לנצח על כל השאר.", do=show("e-2")),
    P("אם נריץ אותה קודם על המילה הריקה, נחכה לנצח, ולא נגיע לשום מילה אחרת.", do=show("e-3")),
    P("הפתרון הוא **הרצה משולבת**: בשלב $i$ מריצים $i$ צעדים על $i$ המילים הראשונות.", do=show("g-r0"),
      say="הפתרון הוא הרצה משולבת: בשלב אַיי מריצים אַיי צעדים על אַיי המילים הראשונות."),
    P("בשלב השני, שני צעדים על הריקה ועל אפס. עדיין שום דבר.", do=show("g-r1")),
    P("בשלב השלישי מגיעים גם למילה אחת, והמכונה מקבלת אותה. מצאנו! מקבלים.", do=show("g-r2", "g-hl2")),
    P("כל מילה מתקבלת נמצאת בשלב סופי כלשהו. לכן המשלים של $E_{TM}$ ב-$RE$.", do=show("e-4")),
    P("ו-$E_{TM}$ עצמה ב-$coRE$, כי המשלים שלה ב-$RE$. אף אחת מהשתיים לא כריעה.", do=show("e-5"), hold=0.4),
], stage=GRIDTAB,
   panel=st.card("e-1", "plain", "$\\overline{E_{TM}}$: $L(M) \\ne \\emptyset$")
         + st.card("e-2", "ex", "$M$ מקבלת מילים עם $1$, ורצה לנצח על השאר")
         + st.card("e-3", "trap", "⚠️ מילה אחרי מילה: נתקעים על $\\varepsilon$")
         + st.card("e-4", "rule", "🔑 $\\overline{E_{TM}} \\in RE \\setminus R$")
         + st.card("e-5", "rule", "🔑 $E_{TM} \\in coRE \\setminus R$"))

ALLV = w_dec.venn("w", [("atm", "A_{TM}", "A_TM"), ("htm", "H_{TM}", "H_TM"), ("ne", "\\overline{E_{TM}}", "notE_TM"),
                        ("adfa", "A_{DFA}", "A_DFA"), ("coatm", "\\overline{A_{TM}}", "coA_TM"),
                        ("cohtm", "\\overline{H_{TM}}", "coH_TM"), ("etm", "E_{TM}", "E_TM"),
                        ("eq", "EQ_{TM}", "EQ_TM"), ("all", "ALL_{TM}", "ALL_TM")])
eq = Scene("eq", "המפה המלאה", [
    P("נשים הכול על המפה. $A_{TM}$, $H_{TM}$ והמשלים של $E_{TM}$ ב-$RE$, מחוץ ל-$R$.",
      do=show("w-l-atm", "w-l-htm", "w-l-ne")),
    P("המשלימים שלהן, וגם $E_{TM}$, ב-$coRE$ מחוץ ל-$R$.", do=show("w-l-coatm", "w-l-cohtm", "w-l-etm")),
    P("ו-$EQ_{TM}$ ו-$ALL_{TM}$? כדי לאשר שוויון צריך לבדוק **כל** מילה. זה לא נגמר.", do=show("w-l-eq", "w-l-all")),
    P("וכדי להפריך צריך מילה שאחת מקבלת והשנייה **לא**. ו״לא מקבלת״ כולל גם ריצה אינסופית, שלא רואים בזמן סופי.",
      do=show("w-c1")),
    P("זו האינטואיציה. שהן לא ב-$RE$ ולא ב-$coRE$ מוכיחים ברדוקציות, בקורס הרדוקציות.", do=show("w-f-none")),
    P("ומה כריע? כשהקלט הוא **אוטומט סופי**, כמו ב-$A_{DFA}$. האוטומט קורא את המילה ועוצר תמיד.",
      do=hide("w-f-none") + show("w-l-adfa", "w-c2"), hold=0.4),
], stage=ALLV,
   panel=st.card("w-c1", "rule", "🔑 שוויון והכלה: צריך גם ״קיים״ וגם ״לכל״")
         + st.card("w-c2", "rule", "🔑 הקלט אוטומט או דקדוק ⇐ כמעט תמיד $R$"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: סווגו את שפת הזוגות של מכונה ומילה, שבהם המילה **לא** בשפה של המכונה."),
    P("קודם מזהים אותה. מילה לא בשפה פירושו שהמכונה לא מקבלת אותה: דוחה, או רצה לנצח.", do=show("x-1")),
    P("זה בדיוק המשלים של $A_{TM}$, בתחפושת.", do=show("x-2")),
    P("המשלים של השפה הזו הוא $A_{TM}$, והיא ניתנת לקבלה.", do=show("x-3")),
    P("והשפה עצמה לא ניתנת לקבלה, אחרת לפי פוסט $A_{TM}$ הייתה כריעה.", do=show("q-ok-a"), hold=0.3),
    P("המלכודת היא להתבלבל בכיוון: ״לא כריעה אבל ניתנת לקבלה״ מתאר את $A_{TM}$, לא את המשלים.",
      do=show("q-x-b", "q-n-b")),
    P("והשתיים האחרות נופלות: היא לא כריעה, והמשלים שלה ניתן לקבלה.", do=show("q-x-c", "q-x-d"), hold=0.6),
], stage='<div class="stack">'
         + st.card("x-1", "plain", "$w \\notin L(M)$: $M$ דוחה <b>או</b> לא עוצרת")
         + '<div id="x-2" class="bigmath h" style="font-size:44px">$L = \\overline{A_{TM}}$</div>'
         + st.card("x-3", "rule", "🔑 $\\overline{L} = A_{TM} \\in RE$, ולכן $L \\in coRE \\setminus R$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>סווגו את השפה '
         '$L = \\{\\langle M, w\\rangle \\mid w \\notin L(M)\\}$</div>'
         + st.options("q", OPTS, notes={"b": "זו $A_{TM}$"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $A_{TM}$, $H_{TM}$ והמשלים של $E_{TM}$: מריצים ומחכים. $RE$ ולא כריעות.", do=show("r-1")),
    P("המשלימים שלהן, ו-$E_{TM}$: $coRE$ ולא כריעות.", do=show("r-2")),
    P("$EQ_{TM}$ ו-$ALL_{TM}$: באף אחת. וכשהקלט הוא אוטומט, השפה כריעה.", do=show("r-3")),
    P("וזכרו: $H_{TM}$ היא לא המשלים של $A_{TM}$. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage=w_dec.venn("rv", [("atm", "A_{TM}", "A_TM"), ("ne", "\\overline{E_{TM}}", "notE_TM"),
                           ("adfa", "A_{DFA}", "A_DFA"), ("coatm", "\\overline{A_{TM}}", "coA_TM"),
                           ("etm", "E_{TM}", "E_TM"), ("eq", "EQ_{TM}", "EQ_TM")], hidden=False),
   panel=st.card("r-1", "rule", "🔑 ״קיים״ ⇐ $RE \\setminus R$")
         + st.card("r-2", "rule", "🔑 המשלים ⇐ $coRE \\setminus R$")
         + st.card("r-3", "rule", "🔑 שוויון ⇐ אף אחת. אוטומט ⇐ $R$")
         + st.card("r-4", "trap", "⚠️ $H_{TM} \\ne A_{TM}$ ולא המשלים שלה"))

VIDEO = Video("D03", "dec", "השפות המפורסמות והמחלקה של כל אחת", [title, defs, atm, dove, eq, exam, recap],
              bank={"23B-A-Q8": "a"})
