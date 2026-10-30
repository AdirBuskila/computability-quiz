# -*- coding: utf-8 -*-
"""T02 · קבלה, דחייה ולולאה — video script (build: tools/video/vid.py T02).

Source: tools/courses_src/tm/T02.js (lesson + goal). Exam anchor: 25A-A-Q10 (what follows from L(M) = ∅), which no
guided quiz uses. Not used on purpose: the T02 quiz (20A-B-Q4 and the five original questions, including the machine
of T02-Q3 that runs right forever) and 24B-B-Q3 (cited in the lesson).
One machine, three inputs, three outcomes: every run comes from w_tm.trace() (asserted against run_tm), and the
language claims are checked on all words up to length 7.
"""
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, REJ, BLANK, run_tm, words
import stage as st
import w_tm

# ---------------------------------------------------------------- machines (verified)
# M: scan right over 0s; a 1 accepts; at the end of the input turn back left over the 0s, forever (left edge)
D = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): ("q_1", BLANK, "L"),
     ("q_1", "0"): ("q_1", "0", "L")}
CA, RA = w_tm.trace(D, "q_0", "01")
CR, RR = w_tm.trace(D, "q_0", "")
CL, RL = w_tm.trace(D, "q_0", "00")
assert (RA, RR, RL) == ("accept", "reject", "loop")
assert len(CA) == 3 and len(CR) == 3 and CR[1][2] == 0          # ε: one step (head stays), then no transition
LOOP = CL[:7]
assert LOOP[4][:1] == LOOP[5][:1] and LOOP[4][2] == LOOP[5][2] == 0   # q_1 on cell 0 reading 0, again and again
for w in words(7):
    r = run_tm(D, "q_0", w)[0]
    assert r == ("accept" if "1" in w else "reject" if w == "" else "loop"), (w, r)
# M2: the same language, but the end of the input rejects at once: halts on every input
D2 = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): (REJ, BLANK, "R")}
for w in words(7):
    r = run_tm(D2, "q_0", w)[0]
    assert r == ("accept" if "1" in w else "reject"), (w, r)
# exam: L(M) = ∅ both for a machine that rejects at once (halts on everything) and one that loops on everything
for w in words(5):
    assert run_tm({}, "q_0", w)[0] == "reject"
    assert run_tm({("q_0", c): ("q_0", c, "R") for c in "01" + BLANK}, "q_0", w)[0] == "loop"

Q = BANK["25A-A-Q10"]
assert Q["correctId"] == "d"
OPTS = [(o["id"], f'${o["value"]}$' if o["type"] == "math" else o["value"]) for o in Q["options"]]

SYMS = ["0", "1", BLANK]
TA, VA = w_tm.tape("ta", CA, 4)
TR, VR = w_tm.tape("tr", CR, 4)
TL, VL = w_tm.tape("tl", LOOP, 4)


def table(p):
    return w_tm.delta_table(p, D, ["q_0", "q_1"], SYMS)


# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("ריצה של מכונת טיורינג יכולה להיגמר בשלוש דרכים."),
    P("נראה את שלושתן על מכונה אחת, ונבין למה ״לא מקבלת״ זה לא אותו דבר כמו ״דוחה״."),
    P("ובסוף נפתור שאלה ממבחן.", hold=0.4),
], stage='<div class="kicker">T02 · מכונות טיורינג</div><h1>קבלה, דחייה ולולאה</h1>'
         '<p>שלוש תוצאות של ריצה, ההבדל בין מכונה שמקבלת שפה למכונה שמכריעה אותה, '
         'ולמה ״לא מקבלת״ אינו ״דוחה״.</p>', layout="title")

three = Scene("three", "שלוש תוצאות", [
    P("ריצה של $M$ על מילה $w$ נגמרת באחת משלוש דרכים.", do=show("o-1")),
    P("**מקבלת**: המכונה מגיעה ל-$q_{acc}$ ועוצרת.", do=show("o-2")),
    P("**דוחה**: המכונה מגיעה ל-$q_{rej}$, או שאין לה מעבר, ועוצרת.", do=show("o-3")),
    P("והשלישית: המכונה **לא עוצרת**. היא רצה לנצח, בלולאה אינסופית.", do=show("o-4"), hold=0.4),
    P("הנה מכונה עם שני מצבים. נריץ אותה על שלוש מילים, ונקבל את שלוש התוצאות.", do=show("o-tab")),
], stage=f'<div class="stack"><div id="o-tab" class="h">{table("t0")}</div></div>',
   panel=st.card("o-1", "plain", "ריצה של $M$ על $w$:")
         + st.card("o-2", "rule", "✓ מקבלת: עוצרת ב-$q_{acc}$")
         + st.card("o-3", "rule", "✗ דוחה: עוצרת ב-$q_{rej}$ או במעבר חסר")
         + st.card("o-4", "trap", "∞ לא עוצרת: לולאה אינסופית"))

acc_ph = w_tm.run_phrases("ta", D, CA, VA)
w_tm.table_do(acc_ph, "a0", CA, D)
acc = Scene("acc", "קבלה", [
    P("ראשונה, המילה $01$.", do=show("a-tape")),
    *acc_ph,
    P("המכונה הגיעה ל-$q_{acc}$ ועצרה. היא **מקבלת** את $01$.", do=show("a-v"), hold=0.3),
], stage=f'<div class="stack">{table("a0")}<div id="a-tape" class="h">{TA}</div></div>',
   panel=st.card("a-v", "rule", "✓ $01 \\in L(M)$"))

rej_ph = w_tm.run_phrases("tr", D, CR, VR)
w_tm.table_do(rej_ph, "r0", CR, D)
rej = Scene("rej", "דחייה", [
    P("שנייה, המילה הריקה. על הסרט יש רק רווחים.", do=show("r-tape")),
    *rej_ph,
    P("מעבר חסר הוא **דחייה**: המכונה עצרה, והמילה הריקה לא בשפה שלה.", do=show("r-v"), hold=0.3),
], stage=f'<div class="stack">{table("r0")}<div id="r-tape" class="h">{TR}</div></div>',
   panel=st.card("r-v", "rule", "✗ המכונה <b>דוחה</b> את המילה הריקה: היא עצרה"))

loop_ph = w_tm.run_phrases("tl", D, LOOP, VL)
w_tm.table_do(loop_ph, "l0", LOOP, D)
loop = Scene("loop", "לולאה", [
    P("ושלישית, המילה $00$.", do=show("l-tape")),
    *loop_ph,
    P("ושוב אותו צעד: אותו מצב, אותו תא, אותו תו. וכך לנצח.", do=show("l-c1")),
    P("המכונה **לא עוצרת** על $00$. היא לא קיבלה, אבל גם לא דחתה.", do=show("l-c2"), hold=0.4),
], stage=f'<div class="stack">{table("l0")}<div id="l-tape" class="h">{TL}</div></div>',
   panel=st.card("l-c1", "plain", "$q_1$ בתא הראשון קורא $0$, זז שמאלה ונשאר במקום")
         + st.card("l-c2", "trap", "∞ לא מקבלת, לא דוחה: <b>לא עוצרת</b>"))

decide = Scene("decide", "מקבלת מול מכריעה", [
    P("אז מה השפה של המכונה? היא מקבלת בדיוק את המילים שיש בהן $1$.", do=show("d-1"),
      say="אז מה השפה של המכונה? היא מקבלת בדיוק את המילים שיש בהן אחת."),
    P("על שאר המילים היא דוחה, כמו במילה הריקה, או נתקעת בלולאה, כמו ב-$00$.", do=show("d-2")),
    P("לכן נגיד שהמכונה **מקבלת** את השפה: $L(M)$ היא בדיוק השפה הזו.", do=show("d-3")),
    P("אבל היא לא **מכריעה** אותה. מכריעה זה לקבל את השפה, וגם לעצור על **כל** קלט.", do=show("d-4")),
    P("והשפה עצמה כריעה בקלות. מספיק לשנות תא אחד בטבלה:", do=show("d-5")),
    P("בסוף הקלט עוברים ישר ל-$q_{rej}$. עכשיו המכונה עוצרת על כל קלט, ומכריעה את אותה שפה.", do=show("d-6")),
    P("כלומר, מכונה שלא עוצרת תמיד לא אומרת שהשפה לא כריעה. ייתכן שיש מכונה אחרת שמכריעה אותה.",
      do=show("d-7"), hold=0.4),
], stage='<div class="stack">'
         + st.card("d-1", "ex", "$L(M)$ = המילים שמכילות $1$")
         + st.card("d-2", "plain", "המילה הריקה: דחייה · $00$: לולאה")
         + st.card("d-5", "ex", "תא אחד משתנה: $\\delta(q_0, \\sqcup) = (q_{rej}, \\sqcup, R)$")
         + st.card("d-6", "rule", "המכונה החדשה עוצרת תמיד: היא <b>מכריעה</b> את אותה שפה")
         + "</div>",
   panel=st.card("d-3", "rule", "🔑 $M$ <b>מקבלת</b> את $L$: $L(M) = L$")
         + st.card("d-4", "rule", "🔑 $M$ <b>מכריעה</b> את $L$: $L(M) = L$, ועוצרת על <b>כל</b> קלט")
         + st.card("d-7", "trap", "⚠️ $M$ לא עוצרת תמיד, ובכל זאת $L(M)$ כריעה"))

notacc = Scene("notacc", "לא מקבלת ≠ דוחה", [
    P("ומכאן הכלל החשוב בסרטון: **לא מקבלת** זה לא **דוחה**.", do=show("n-1")),
    P("אם $w$ לא שייכת ל-$L(M)$, יש שתי אפשרויות: המכונה דחתה אותה, או שהיא לא עצרה עליה.", do=show("n-2")),
    P("במבחן, כשכתוב שמילה לא בשפה של המכונה, אל תניחו שהמכונה עצרה.", do=show("n-3"), hold=0.4),
], stage='<div class="stack"><div class="bigmath">$w \\notin L(M)$</div>'
         '<div id="n-2" class="h" style="font-size:40px;direction:rtl">דחייה ✗ &nbsp; או &nbsp; לולאה ∞</div></div>',
   panel=st.card("n-1", "rule", "🔑 לא מקבלת = דוחה <b>או</b> לא עוצרת")
         + st.card("n-3", "trap", "⚠️ ״לא בשפה״ לא אומר ״עצרה״"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: $M$ היא מכונת טיורינג בסיסית, והשפה שלה ריקה. מה נכון?"),
    P("האפשרות הראשונה: אין ל-$M$ אף מצב מקבל. אבל לכל מכונה יש $q_{acc}$, זה חלק מההגדרה.",
      do=show("q-x-a", "q-n-a")),
    P("שפה ריקה רק אומרת שאף ריצה לא **מגיעה** אליו.", do=show("x-1")),
    P("השנייה: אין אנומרטור לשפה. אבל אנומרטור שלא מדפיס אף מילה מונה בדיוק את הקבוצה הריקה.",
      do=show("q-x-b", "q-n-b")),
    P("והשלישית, המלכודת: $M$ לא עוצרת על אף קלט.", do=show("x-2")),
    P("זה ערבוב בין ״לא מקבלת״ לבין ״לא עוצרת״. מכונה שדוחה מיד כל קלט עוצרת תמיד, והשפה שלה ריקה.",
      do=show("q-x-c", "q-n-c", "x-3")),
    P("וגם מכונה שרצה ימינה לנצח מקבלת את השפה הריקה. השפה לא מגלה איך המכונה מתנהגת."),
    P("אז אף אחת מהטענות לא נכונה בהכרח, והתשובה היא ״אף אחת מהתשובות האחרות״.", do=show("q-ok-d"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$L(M) = \\emptyset$</div>'
         + st.card("x-1", "plain", "$q_{acc}$ קיים תמיד, רק לא מגיעים אליו")
         + st.card("x-2", "trap", "⚠️ ״לא מקבלת אף מילה״ אינו ״לא עוצרת״")
         + st.card("x-3", "ex", "דוחה מיד כל קלט: עוצרת תמיד, ו-$L(M) = \\emptyset$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$M$ מכונה בסיסית ו-$L(M) = \\emptyset$. '
         'איזה סעיף נכון?</div>'
         + st.options("q", OPTS, notes={"a": "$q_{acc}$ תמיד קיים", "b": "אנומרטור ריק", "c": "יכולה לדחות"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: ריצה מקבלת, דוחה, או לא עוצרת.", do=show("r-1")),
    P("מכונה מקבלת שפה אם $L(M)$ היא השפה. היא מכריעה אותה אם בנוסף היא עוצרת על כל קלט.", do=show("r-2")),
    P("ומילה שלא בשפה של המכונה: נדחתה, **או** שהמכונה לא עצרה עליה. נתראה ברמה הבאה.", do=show("r-3"),
      hold=0.6),
], stage='<div class="stack"><div class="bigmath" style="font-size:44px">✓ $q_{acc}$ &nbsp; ✗ $q_{rej}$ &nbsp; ∞</div></div>',
   panel=st.card("r-1", "rule", "🔑 שלוש תוצאות: מקבלת, דוחה, לא עוצרת")
         + st.card("r-2", "rule", "🔑 מכריעה = מקבלת + עוצרת תמיד")
         + st.card("r-3", "trap", "⚠️ לא מקבלת = דוחה <b>או</b> לולאה"))

VIDEO = Video("T02", "tm", "קבלה, דחייה ולולאה", [title, three, acc, rej, loop, decide, notacc, exam, recap],
              bank={"25A-A-Q10": "d"})
