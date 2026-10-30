# -*- coding: utf-8 -*-
"""D01 · שלוש המחלקות: R, RE ו-coRE — video script (build: tools/video/vid.py D01).

Source: tools/courses_src/dec/D01.js (lesson + goal). Exam anchor: 24A-C-Q13 (a machine that accepts a decidable
language need not halt), which no guided quiz uses. Not used on purpose: the quiz questions of D01 (the four original
ones and 24B-B-Q6) and 23S-A-Q4 (cited by the lesson).
The two machines are run with w_tm.trace (asserted against the course checker's run_tm), and their languages are
checked on every word up to length 6.
"""
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, REJ, BLANK, run_tm, words
from rules import FACTS, RULES
import stage as st
import w_tm
import w_dec

# ---------------------------------------------------------------- machines (verified)
# both accept "words that contain a 1"; M1 runs right forever on a word with no 1, M2 rejects at the first blank
M1 = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): ("q_0", BLANK, "R")}
M2 = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): (REJ, BLANK, "R")}
for w in words(6):
    r1, r2 = run_tm(M1, "q_0", w)[0], run_tm(M2, "q_0", w)[0]
    assert r1 == ("accept" if "1" in w else "loop") and r2 == ("accept" if "1" in w else "reject"), w
C1, R1 = w_tm.trace(M1, "q_0", "00")
assert R1 == "loop"
C1 = C1[:5]                                                   # four steps, then "and so on forever"
C2, R2 = w_tm.trace(M2, "q_0", "00")
assert R2 == "reject" and len(C2) == 4
T1, V1 = w_tm.tape("m1", C1, 5)
T2, V2 = w_tm.tape("m2", C2, 5)

# course facts behind the class map
assert RULES["R_sub_RE"][0] and not RULES["RE_sub_R"][0] and not RULES["RE_eq_coRE"][0]
assert RULES["L_M_always_RE"][0] and not RULES["L_M_in_R_implies_M_decides"][0]
assert FACTS["A_TM"] == "RE\\R" and FACTS["coA_TM"] == "coRE\\R" and FACTS["EQ_TM"] == "none"

# exam 24A-C-Q13
Q = BANK["24A-C-Q13"]
assert Q["correctId"] == "b"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר את שלוש המחלקות של שפות: $R$, $RE$ ו-$coRE$."),
    P("נראה מה כל מחלקה מבטיחה על מילים שבשפה, ומה על מילים שלא."),
    P("ובסוף נפתור שאלה ממבחן על ההבדל בין שפה למכונה.", hold=0.4),
], stage='<div class="kicker">D01 · כריעות, סגירות וסיווג</div><h1>שלוש המחלקות: R, RE ו-coRE</h1>'
         '<p>להגדיר שפה כריעה, שפה הניתנת לקבלה ושפה ב-coRE, ולהבין מה כל אחת מבטיחה על מילים שבשפה ועל מילים שלא.</p>',
   layout="title")

idea = Scene("idea", "שלוש תוצאות", [
    P("נתחיל ממה שכבר ידוע: ריצה של מכונה על מילה נגמרת באחת משלוש דרכים."),
    P("היא יכולה לעצור ב-$q_{acc}$ ולקבל.", do=show("i-1")),
    P("היא יכולה לעצור ב-$q_{rej}$ ולדחות.", do=show("i-2")),
    P("ויש אפשרות שלישית: היא לא עוצרת בכלל, ורצה לנצח.", do=show("i-3")),
    P("שלוש המחלקות נבדלות בדיוק בשאלה: איזו מהתוצאות האלה מותרת, ועל אילו מילים.", do=show("i-4"), hold=0.4),
], stage='<div class="stack">'
         + st.card("i-1", "ex", "✓ עוצרת ומקבלת: $q_{acc}$")
         + st.card("i-2", "ex", "✗ עוצרת ודוחה: $q_{rej}$")
         + st.card("i-3", "trap", "∞ לא עוצרת: רצה לנצח")
         + "</div>",
   panel=st.card("i-4", "rule", "🔑 מחלקה = מה מותר למכונה לעשות על מילה <b>בשפה</b> ועל מילה <b>שלא בשפה</b>"))

TAB = w_dec.table("ct", ["מחלקה", "קיימת מכונה…", "מילה בשפה", "מילה שלא בשפה"], [
    ["$R$", "<b>מכריעה</b>", "עוצרת ומקבלת", "עוצרת ודוחה"],
    ["$RE$", "<b>מקבלת</b>", "עוצרת ומקבלת", "דוחה <b>או לא עוצרת</b>"],
    ["$coRE$", "המשלים ב-$RE$", "אולי לא עוצרת", "יש מכונה שעוצרת ומקבלת"],
])
classes = Scene("classes", "שלוש המחלקות", [
    P("המחלקה הראשונה: $R$, השפות הכריעות.", do=show("ct-r0")),
    P("שפה כריעה אם קיימת מכונה שמכריעה אותה: על כל קלט היא **עוצרת**, ועונה נכון.", do=show("c-1")),
    P("מילה בשפה היא מקבלת, ומילה שלא בשפה היא דוחה. תמיד יש תשובה."),
    P("המחלקה השנייה: $RE$, השפות הניתנות לקבלה.", do=show("ct-r1")),
    P("כאן מספיקה מכונה שמקבלת את השפה: על מילה בשפה היא עוצרת ומקבלת.", do=show("c-2")),
    P("אבל על מילה שלא בשפה מותר לה גם **לא לעצור**. אין שום הבטחה שתגיע תשובה."),
    P("והשלישית: $coRE$. שפה שייכת אליה אם **המשלים** שלה ב-$RE$.", do=show("ct-r2", "c-3")),
    P("כלומר יש מכונה שמזהה את המילים שלא בשפה, ועל מילים בשפה אולי לא נקבל תשובה.", hold=0.4),
], stage=TAB,
   panel=st.card("c-1", "rule", "🔑 $R$: קיימת מכונה <b>מכריעה</b>, שעוצרת על כל קלט")
         + st.card("c-2", "rule", "🔑 $RE$: קיימת מכונה <b>מקבלת</b>, ומחוץ לשפה מותר לה לא לעצור")
         + st.card("c-3", "rule", "🔑 $L \\in coRE$ אם ורק אם $\\overline{L} \\in RE$"))

m1 = Scene("m1", "שפה מול מכונה", [
    P("עכשיו המלכודת הכי חשובה: $L \\in R$ היא טענה על **השפה**, לא על מכונה מסוימת.", do=show("a-1")),
    P("ניקח את שפת המילים שיש בהן את התו אחת. והנה מכונה שמקבלת אותה.", do=show("a-2", "m1"),
      say="ניקח את שפת המילים שיש בהן את התו אחת. והנה מכונה שמקבלת אותה."),
    P("היא זזה ימינה עד שהיא רואה אחת, ואז מקבלת. נריץ אותה על המילה $00$.", say="היא זזה ימינה עד שהיא רואה אחת, ואז מקבלת. נריץ אותה על המילה אפס אפס."),
    *w_tm.run_phrases("m1", M1, C1, V1),
    P("וכך לנצח: אין אחת על הסרט, והראש ממשיך ימינה ברווחים בלי סוף.", do=show("a-3")),
    P("המכונה הזו מקבלת את השפה, אבל היא **לא מכריעה** אותה.", hold=0.3),
], stage=f'<div class="stack"><div id="m1" class="h">{T1}</div></div>',
   panel=st.card("a-1", "rule", "🔑 $L \\in R$: <b>קיימת</b> מכונה מכריעה")
         + st.card("a-2", "plain", "השפה: מילים שיש בהן $1$")
         + st.card("a-3", "trap", "∞ על $00$ המכונה לא עוצרת"))

m2 = Scene("m2", "מכונה אחרת", [
    P("נשנה מעבר אחד: כשהראש מגיע לרווח, המכונה עוברת ל-$q_{rej}$.", do=show("m2", "b-1")),
    *w_tm.run_phrases("m2", M2, C2, V2),
    P("הפעם היא עצרה ודחתה. והיא עוצרת על כל קלט, ולכן היא **מכריעה** את אותה שפה.", do=show("b-2")),
    P("אז השפה כריעה, למרות שהמכונה הראשונה רצה לנצח.", do=show("b-3")),
    P("ועוד עובדה שימושית: לכל מכונה $M$, השפה $L(M)$ תמיד ב-$RE$. המכונה עצמה מקבלת אותה.", do=show("b-4"),
      hold=0.4),
], stage=f'<div class="stack"><div id="m2" class="h">{T2}</div></div>',
   panel=st.card("b-1", "plain", "רווח: עוברים ל-$q_{rej}$")
         + st.card("b-2", "ex", "✓ עוצרת על כל קלט: מכריעה")
         + st.card("b-3", "rule", "🔑 שתי מכונות, שפה אחת, והיא ב-$R$")
         + st.card("b-4", "rule", "🔑 תמיד $L(M) \\in RE$"))

VENN = w_dec.venn("v", [("atm", "A_{TM}", "A_TM"), ("coatm", "\\overline{A_{TM}}", "coA_TM"),
                        ("emp", "\\emptyset", "R"), ("sig", "\\Sigma^*", "R"), ("eq", "EQ_{TM}", "EQ_TM")],
                  titles_hidden=True)
venn = Scene("venn", "המפה", [
    P("נצייר את המחלקות. כל מכונה מכריעה היא בפרט מקבלת, ולכן $R \\subseteq RE$.", do=show("v-t-RE", "v-t-R", "v-f-R")),
    P("וגם $R \\subseteq coRE$, כי $R$ סגורה למשלים: אם $L$ כריעה, המשלים שלה כריע, ולכן ב-$RE$.",
      do=show("v-t-coRE")),
    P("שפות פשוטות כמו הריקה ו-$\\Sigma^*$ נמצאות באמצע, ב-$R$.", do=show("v-l-emp", "v-l-sig")),
    P("$A_{TM}$ ניתנת לקבלה ולא כריעה: היא ב-$RE$ ומחוץ ל-$R$.", do=hide("v-f-R") + show("v-f-RE", "v-l-atm")),
    P("המשלים שלה ב-$coRE$, ומחוץ ל-$R$.", do=hide("v-f-RE") + show("v-f-coRE", "v-l-coatm")),
    P("ויש שפות שלא נמצאות באף אחת, כמו $EQ_{TM}$.", do=hide("v-f-coRE") + show("v-t-none", "v-f-none", "v-l-eq")),
    P("לכן $coRE$ היא **לא** כל מה שמחוץ ל-$RE$. היא אוסף המשלימים של שפות $RE$.", do=hide("v-f-none") + show("v-c1"),
      hold=0.4),
], stage=VENN,
   panel=st.card("v-c1", "trap", "⚠️ $coRE$ אינה ״כל מה שלא ב-$RE$״: שפה יכולה להיות בשתיהן, או באף אחת"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: $L$ כריעה, ו-$M$ מכונה עם $L(M) = L$. מה נכון?"),
    P("הנתון אומר ש-$M$ **מקבלת** את $L$. הוא לא אומר שהיא מכריעה אותה.", do=show("x-1")),
    P("לכן ״$M$ עוצרת על כל קלט״ לא בהכרח נכון: ראינו מכונה כזו שרצה לנצח.", do=show("q-x-a", "q-n-a")),
    P("ומה עם ״יתכן ש-$M$ לא עוצרת על אף קלט״? ניקח את השפה הריקה. היא כריעה.", do=show("x-2")),
    P("מכונה שרצה לנצח על כל קלט לא מקבלת אף מילה, ולכן $L(M)$ היא בדיוק הריקה.", do=show("x-3")),
    P("אז זה יתכן, והאפשרות הזו נכונה.", do=show("q-ok-b"), hold=0.3),
    P("במכונה אי-דטרמיניסטית מספיק **מסלול אחד** שמקבל. מסלולים אחרים יכולים לדחות או לרוץ לנצח.",
      do=show("q-x-c", "q-n-c")),
    P("וכיוון שהאפשרות ״יתכן שלא עוצרת על אף קלט״ נכונה, ״אף אחת מהתשובות״ נופלת.", do=show("q-x-d"), hold=0.6,
      say="וכיוון שהאפשרות יתכן שלא עוצרת על אף קלט נכונה, האפשרות אף אחת מהתשובות נופלת."),
], stage='<div class="stack">'
         + st.card("x-1", "rule", "🔑 $L(M) = L$: <b>מקבלת</b>, לא בהכרח מכריעה")
         + st.card("x-2", "ex", "$L = \\emptyset \\in R$")
         + st.card("x-3", "ex", "$M$ רצה לנצח על כל קלט, ולכן $L(M) = \\emptyset$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$L$ כריעה ו-$M$ מכונה עם $L(M) = L$. '
         'איזו טענה נכונה?</div>'
         + st.options("q", OPTS, notes={"a": "מקבלת ≠ מכריעה", "c": "מספיק מסלול אחד"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $R$ אם יש מכונה שעוצרת תמיד ועונה נכון.", do=show("r-1")),
    P("$RE$ אם יש מכונה שמקבלת, ומחוץ לשפה מותר לה לא לעצור.", do=show("r-2")),
    P("$coRE$ אם המשלים ב-$RE$. ו-$R$ מוכלת בשתיהן.", do=show("r-3")),
    P("וזכרו: כריעות היא תכונה של השפה, לא של מכונה אחת. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage=w_dec.venn("rv", [("atm", "A_{TM}", "A_TM"), ("coatm", "\\overline{A_{TM}}", "coA_TM"),
                           ("emp", "\\emptyset", "R")], hidden=False),
   panel=st.card("r-1", "rule", "🔑 $R$: מכונה מכריעה")
         + st.card("r-2", "rule", "🔑 $RE$: מכונה מקבלת")
         + st.card("r-3", "rule", "🔑 $coRE$: המשלים ב-$RE$")
         + st.card("r-4", "trap", "⚠️ שפה כריעה, ומכונה שלה עלולה לא לעצור"))

VIDEO = Video("D01", "dec", "שלוש המחלקות: R, RE ו-coRE", [title, idea, classes, m1, m2, venn, exam, recap],
              bank={"24A-C-Q13": "b"})
