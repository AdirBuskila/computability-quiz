# -*- coding: utf-8 -*-
"""T03 · מעקב אחרי מכונה בטבלת מעברים — video script (build: tools/video/vid.py T03).

Source: tools/courses_src/tm/T03.js (lesson + goal). Exam anchor: 25B-B-Q10 (a diagram whose δ seems to reject on 0,
but the first move erases the cell and stays at the left edge), which no guided quiz uses. Not used on purpose: the
T03 quiz (the bit-flip and binary +1 machines, 26B-B-Q2 is T04's exam) and 26B-A-Q2 (cited in the lesson).
Every run comes from w_tm.trace() (asserted against run_tm); the exam diagram is transcribed into a δ and run on
every word up to length 6.
"""
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, REJ, BLANK, run_tm, words
import stage as st
import w_tm

# ---------------------------------------------------------------- machines (verified)
# M: zeros become X; q_1 remembers "the last symbol read was 1"; the end of the input in q_1 accepts
D = {("q_0", "0"): ("q_0", "X", "R"), ("q_0", "1"): ("q_1", "1", "R"),
     ("q_1", "0"): ("q_0", "X", "R"), ("q_1", "1"): ("q_1", "1", "R"), ("q_1", BLANK): (ACC, BLANK, "R")}
C1, R1 = w_tm.trace(D, "q_0", "101")
assert R1 == "accept" and len(C1) - 1 == 4 and "".join(C1[-1][1]).strip(BLANK) == "1X1"
C2, R2 = w_tm.trace(D, "q_0", "10")
assert R2 == "reject" and "".join(C2[-1][1]).strip(BLANK) == "1X" and len(C2) - 2 == 2   # 2 steps, then no transition
for w in words(7):
    assert (run_tm(D, "q_0", w)[0] == "accept") == w.endswith("1"), w
assert w_tm.conf_tex(C1[2]) == "1 X \\; q_0 \\; 1"

# exam 25B-B-Q10, transcribed from the diagram
DX = {("q_0", c): ("q_1", BLANK, "L") for c in ("0", "1", BLANK)}
DX.update({("q_1", "0"): (REJ, BLANK, "L"), ("q_1", "1"): (ACC, BLANK, "L"), ("q_1", BLANK): (ACC, BLANK, "L")})
for w in words(6):
    assert run_tm(DX, "q_0", w)[:2] == ("accept", 2), w          # every input: accepted after exactly 2 steps
CX, RX = w_tm.trace(DX, "q_0", "01")
assert RX == "accept" and CX[1][2] == 0 and CX[1][1][0] == BLANK

Q = BANK["25B-B-Q10"]
assert Q["correctId"] == "a"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

SYMS = ["0", "1", "X", BLANK]
T1, V1 = w_tm.tape("t1", C1, 5, hidden=True)
T2, V2 = w_tm.tape("t2", C2, 4, hidden=True)
TX, VX = w_tm.tape("tx", CX, 4)


def table(p):
    return w_tm.delta_table(p, D, ["q_0", "q_1"], SYMS)


def with_confs(ph, pfx, n):
    for s in range(1, n):
        ph[s - 1].do += show(f"{pfx}-cf{s}")
    return ph


# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("במבחן נותנים מכונה בטבלה או בדיאגרמה, ושואלים מה היא עושה על קלט מסוים."),
    P("הדרך היחידה לענות בבטחה: להריץ אותה ביד, צעד אחר צעד. נלמד לעשות את זה בלי לטעות.", hold=0.4),
], stage='<div class="kicker">T03 · מכונות טיורינג</div><h1>מעקב אחרי מכונה בטבלת מעברים</h1>'
         '<p>להריץ מכונה ביד: מה נכתב על הסרט, כמה צעדים עברו, ובמה נגמרה הריצה.</p>', layout="title")

read = Scene("read", "קוראים טבלה", [
    P("טבלת מעברים היא פשוט $\\delta$, כתובה כטבלה.", do=show("k-tab")),
    P("השורה היא המצב, והעמודה היא התו שהראש קורא.", do=show("k-1")),
    P("למשל, במצב $q_1$ כשהראש קורא $0$:", do=show("k0-hi-q_1-0")),
    P("כותבים $X$, עוברים ל-$q_0$, וזזים ימינה.", do=show("k-2")),
    P("וקו בתא, במקום שלישייה, אומר שאין מעבר. מעבר חסר הוא **דחייה**.", do=hide("k0-hi-q_1-0") + show("k0-hi-q_0-_", "k-3")),
], stage=f'<div class="stack"><div id="k-tab" class="h">{table("k0")}</div></div>',
   panel=st.card("k-1", "plain", "שורה = מצב · עמודה = התו שנקרא")
         + st.card("k-2", "ex", "תא: (המצב הבא, התו לכתיבה, הכיוון)")
         + st.card("k-3", "trap", "⚠️ קו בתא: אין מעבר, המכונה <b>דוחה</b>"))

conf = Scene("conf", "קונפיגורציה", [
    P("כדי לא ללכת לאיבוד, רושמים בכל צעד **קונפיגורציה**: תמונת מצב של המכונה.", do=show("c-1")),
    P("מה שמשמאל לראש, אחריו המצב, ואחריו מה שמהראש והלאה.", do=show("c-2"),
      say="מה שמשמאל לראש, אחריו המצב, ואחריו מה שמהראש והלאה."),
    P("כאן כתוב על הסרט $1X1$. המכונה במצב $q_0$, והראש על ה-$1$ השנייה.", do=show("c-3"),
      say="כאן כתוב על הסרט אחת, אֶקְס, אחת. המכונה במצב קְיוּ אפס, והראש על האחת השנייה."),
    P("והמונה הוא פשוט: כל מעבר הוא **צעד** אחד, גם המעבר האחרון אל מצב העצירה.", do=show("c-4"), hold=0.3),
], stage='<div class="stack"><div id="c-1" class="bigmath h">$u \\; q \\; v$</div>'
         f'<div id="c-3" class="bigmath h">${w_tm.conf_tex(C1[2])}$</div></div>',
   panel=st.card("c-2", "ex", "$u$: משמאל לראש · $q$: המצב · $v$: מהראש והלאה")
         + st.card("c-4", "rule", "🔑 כל מעבר = צעד, כולל הכניסה ל-$q_{acc}$"))

ph1 = with_confs(w_tm.run_phrases("t1", D, C1, V1), "f1", len(C1))
w_tm.table_do(ph1, "a0", C1, D)
run1 = Scene("run1", "הרצה: 101", [
    P("נריץ את המכונה על $101$. זו הקונפיגורציה ההתחלתית.", do=show("t1-w", "f1-cf0", "t1-hd0", "t1-st-q_0")),
    *ph1,
    P("ארבעה מעברים, כלומר ארבעה צעדים. על הסרט כתוב $1X1$, והמכונה מקבלת.", do=show("r1-v"),
      say="ארבעה מעברים, כלומר ארבעה צעדים. על הסרט כתוב אחת, אֶקְס, אחת, והמכונה מקבלת.", hold=0.3),
    P("שימו לב לסדר בכל צעד: קודם **כותבים** על התא הנוכחי, ורק אחר כך **זזים**.", do=show("r1-r")),
], stage=f'<div class="stack">{table("a0")}<div id="t1-w" class="h">{T1}</div></div>',
   panel=w_tm.conf_lines("f1", C1)
         + st.card("r1-v", "rule", "✓ 4 צעדים · הסרט: $1X1$ · מקבלת")
         + st.card("r1-r", "rule", "🔑 כותבים, ורק אז זזים"))

ph2 = with_confs(w_tm.run_phrases("t2", D, C2, V2), "f2", len(C2) - 1)
w_tm.table_do(ph2, "b0", C2, D)
run2 = Scene("run2", "הרצה: 10", [
    P("ועכשיו $10$.", do=show("t2-w", "f2-cf0", "t2-hd0", "t2-st-q_0")),
    *ph2,
    P("המכונה **דחתה**, אחרי שני צעדים. אבל הסרט לא ריק: כתוב עליו $1X$.", do=show("r2-v"),
      say="המכונה דחתה, אחרי שני צעדים. אבל הסרט לא ריק: כתוב עליו אחת, אֶקְס."),
    P("וזו המלכודת: **תוכן הסרט** זה דבר אחד, ו**התשובה** של המכונה זה דבר אחר.", do=show("r2-t")),
    P("מכונה יכולה לכתוב הרבה על הסרט, ובכל זאת לדחות.", hold=0.4),
], stage=f'<div class="stack">{table("b0")}<div id="t2-w" class="h">{T2}</div></div>',
   panel=w_tm.conf_lines("f2", C2[:-1])
         + st.card("r2-v", "plain", "✗ מעבר חסר מ-$q_0$ עם $\\sqcup$: דחייה, הסרט: $1X$")
         + st.card("r2-t", "trap", "⚠️ תוכן הסרט אינו התשובה"))

phx = w_tm.run_phrases("tx", DX, CX, VX)
exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: מכונה בסיסית בדיאגרמה. האם היא מכריעה, והאם השפה שלה כריעה?"),
    P("במבט ראשון: מ-$q_1$, קריאת $0$ מובילה לדחייה, אז נראה שיש מילים שנדחות.", do=show("x-1")),
    P("אבל אל תנחשו, תריצו. נריץ על $01$.", do=show("x-tape")),
    phx[0],
    P("הראש היה בתא הראשון וזז שמאלה, אז הוא **נשאר** במקום. ועכשיו הוא קורא את הרווח שנכתב שם.",
      do=show("x-2")),
    phx[1],
    P("וכך על כל קלט: הצעד הראשון מוחק את התא הראשון, ו-$q_1$ תמיד קורא רווח ומקבל.", do=show("x-3")),
    P("המעבר לדחייה אף פעם לא מתבצע. המכונה עוצרת תמיד, ומקבלת את כל המילים.", do=show("q-x-b", "q-x-c")),
    P("אז $M$ מכריעה, והשפה שלה, $\\Sigma^*$, ודאי כריעה. התשובה: $L(M) \\in R$ ו-$M$ מכריעה.",
      do=show("q-ok-a", "q-x-d"), hold=0.6,
      say="אז אֵם מכריעה, והשפה שלה, סיגמא כוכבית, ודאי כריעה. התשובה: השפה כריעה, ואֵם מכריעה."),
], stage='<div class="stack">'
         + st.raster("xr", "images/exams/25B-B-Q10.png", 760, (1011, 369))
         + f'<div id="x-tape" class="h">{TX}</div>'
         + st.card("x-3", "rule", "🔑 כל קלט: 2 צעדים ו-$q_{acc}$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>המכונה הבסיסית בדיאגרמה. איזו טענה נכונה?</div>'
         + st.options("q", OPTS)
         + st.card("x-1", "trap", "⚠️ נראה ש-$0$ מוביל ל-$q_{rej}$")
         + st.card("x-2", "rule", "🔑 שמאלה מהתא הראשון: הראש נשאר"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: שורה היא מצב, עמודה היא התו שנקרא, ותא ריק הוא דחייה.", do=show("s-1")),
    P("בכל צעד: קוראים, כותבים, עוברים מצב, ורק אז זזים. וכל מעבר נספר כצעד.", do=show("s-2")),
    P("תוכן הסרט אינו התשובה. ובשאלות כאלה במבחן, לא מנחשים: מריצים. נתראה ברמה הבאה.", do=show("s-3"),
      hold=0.6),
], stage='<div class="stack"><div class="bigmath">$u \\; q \\; v$</div></div>',
   panel=st.card("s-1", "rule", "🔑 תא ריק = דחייה")
         + st.card("s-2", "rule", "🔑 כותבים ואז זזים · כל מעבר = צעד")
         + st.card("s-3", "trap", "⚠️ הסרט אינו התשובה · מריצים, לא מנחשים"))

VIDEO = Video("T03", "tm", "מעקב אחרי מכונה בטבלת מעברים", [title, read, conf, run1, run2, exam, recap],
              bank={"25B-B-Q10": "a"})
