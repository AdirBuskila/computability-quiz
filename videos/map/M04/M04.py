# -*- coding: utf-8 -*-
"""M04 · בניית המכונה K ורדוקציות מ-H ו-A — video script (build: tools/video/vid.py M04).

Source: tools/courses_src/map/M04.js (lesson + goal). Exam anchor: 24A-C-Q5 (T accepts the words uu after running M
on w: a reduction H_TM <=m L, but it does not show L in RE), which no guided quiz uses. Not used on purpose: the
five original quiz questions of M04 (the two printed machines, the step-counting R_{M,w}, the two "why" questions)
and 20A-A-Q13 (the M04 quiz). The two machines below are new; the "safe words" and step-counting variants are left
to the lesson and the quiz.
Both machines are run by the course simulator (common.run_tm); the language of K_{M,w} is decided exactly as the
course checker does it (map/check.py, kind red-K: Sigma* if M halts on w, else empty).
"""
from vid import P, Scene, Video, show, hide, BANK
from common import run_tm, BLANK, ACC, REJ
import stage as st
import w_map


def K_lang(delta, start, w):
    res, steps, _ = run_tm(delta, start, w, 4000)
    return ("Sigma*" if res != "loop" else "empty"), res, steps


# M1: walks right over the input; no move on the blank -> rejects
M1 = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): ("q_0", "1", "R")}
assert K_lang(M1, "q_0", "011") == ("Sigma*", "reject", 3)
# M2: bounces between the 0 and the 1 forever
M2 = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): ("q_1", "1", "L"), ("q_1", "0"): ("q_0", "0", "R")}
assert K_lang(M2, "q_0", "01")[0] == "empty"


def table(pfx, delta):
    syms = ["0", "1", BLANK]
    sts = sorted({q for q, _ in delta})
    def cell(q, a):
        if (q, a) not in delta:
            return "—"
        p, b, d = delta[(q, a)]
        return f"$({p}, {r'\sqcup' if b == BLANK else b}, {d})$"
    head = "".join(f"<th>{'$\\sqcup$' if a == BLANK else a}</th>" for a in syms)
    rows = "".join(f"<tr><td>${q}$</td>" + "".join(f"<td>{cell(q, a)}</td>" for a in syms) + "</tr>" for q in sts)
    return (f'<div id="{pfx}" class="stack h"><div class="bigmath" style="font-size:44px">${"M_1" if pfx == "t1" else "M_2"}$</div>'
            f'<table class="delta" dir="ltr"><thead><tr><th></th>{head}</tr></thead><tbody>{rows}</tbody></table></div>')


K_CODE = ["K(x):", "  ignore x", "  run M on w", "  if it halted: ACCEPT"]

Q = BANK["24A-C-Q5"]
assert Q["correctId"] == "d"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נבנה את הכלי שמופיע כמעט בכל רדוקציה מ-$H_{TM}$: המכונה $K_{M,w}$."),
    P("נריץ אותה על שתי מכונות אמיתיות, ונראה למה היא נותנת ״הכול או כלום״.", hold=0.4),
], stage='<div class="kicker">M04 · רדוקציות מיפוי</div><h1>בניית המכונה $K$</h1>'
         '<p>להבין איך בונים רדוקציה מ-$H_{TM}$ או $A_{TM}$ לשפה של מכונות, בעזרת מכונת עזר שרצה על מילה קבועה.</p>',
   layout="title")

idea = Scene("idea", "המכונה K", [
    P("הקלט של הרדוקציה הוא זוג: מכונה $M$ ומילה $w$. הפלט הוא **קוד** של מכונה חדשה.", do=show("i-f")),
    P("המכונה החדשה, $K_{M,w}$, מקבלת קלט $x$.", do=show("k-l0")),
    P("היא מתעלמת מ-$x$ לגמרי.", do=show("k-hl1")),
    P("מריצה את $M$ על $w$, שכתובה בתוכה.", do=hide("k-hl1") + show("k-hl2")),
    P("ואם הריצה הזו נגמרה, היא מקבלת.", do=hide("k-hl2") + show("k-hl3"), hold=0.3),
    P("שימו לב: לא משנה **איך** $M$ עצרה. גם אם היא דחתה את $w$, $K$ מקבלת.", do=hide("k-hl3") + show("i-c1")),
], stage='<div class="stack"><div id="i-f" class="bigmath h">$f(\\langle M,w\\rangle) = \\langle K_{M,w}\\rangle$</div>'
         + w_map.code("k", K_CODE) + "</div>",
   panel=st.card("i-c1", "trap", "⚠️ עצירה, לא קבלה: גם דחייה של $w$ נחשבת"))

run = Scene("run", "שתי מכונות", [
    P("נבדוק על מכונה אמיתית. $M_1$ רצה ימינה על הקלט. כשהיא מגיעה לרווח, אין לה מעבר, והיא דוחה.", do=show("t1")),
    P("על $w$ שווה $011$: שלושה צעדים ימינה, ואז דחייה. היא **עצרה**.", do=show("r-1"),
      say="על דַּאבְּלְיוּ שווה אפס אחת אחת: שלושה צעדים ימינה, ואז דחייה. היא עצרה."),
    P("אז $K$ מקבלת כל $x$: $x$ שווה אפס, $x$ שווה $11$, גם המילה הריקה. השפה שלה היא $\\Sigma^*$.", do=show("r-2"),
      say="אז קֵיי מקבלת כל אִקְס: אפס, אחת אחת, וגם המילה הריקה. השפה שלה היא סיגמא כוכבית."),
    P("ועכשיו $M_2$, על $w$ שווה $01$.", do=hide("t1", "r-1", "r-2") + show("t2"),
      say="ועכשיו אֵם שתיים, על דַּאבְּלְיוּ שווה אפס אחת."),
    P("היא קוראת אפס וזזה ימינה. רואה אחת, וחוזרת שמאלה. רואה אפס, וזזה ימינה. וחוזר חלילה.", do=show("r-3")),
    P("$M_2$ לא עוצרת על $w$. אז $K$ תקועה בשלב הזה על **כל** $x$, ולא מקבלת אף מילה.", do=show("r-4")),
    P("השפה שלה ריקה. הכול או כלום.", do=show("r-5"), hold=0.5),
], stage='<div class="swap" style="--swap-h:300px"><div>' + table("t1", M1) + "</div><div>" + table("t2", M2)
         + "</div></div>",
   panel=st.card("r-1", "ex", "$M_1$ על $011$: עוצרת אחרי 3 צעדים (דוחה)")
         + st.card("r-2", "rule", "🔑 $L(K) = \\Sigma^*$")
         + st.card("r-3", "ex", "$M_2$ על $01$: ימינה, שמאלה, ימינה… לנצח")
         + st.card("r-4", "rule", "🔑 $L(K) = \\emptyset$")
         + st.card("r-5", "trap", "⚠️ $\\Sigma^*$ או $\\emptyset$, שום דבר באמצע"))

ROWS = [
    ("$H_{TM} \\le_m \\overline{E_{TM}}$", "עוצרת ⟺ השפה לא ריקה"),
    ("$\\overline{H_{TM}} \\le_m E_{TM}$", "אותה $f$, משלימים"),
    ("$H_{TM} \\le_m ALL_{TM}$", "עוצרת ⟺ השפה היא $\\Sigma^*$"),
]
use = Scene("use", "מה זה נותן", [
    P("ולמה זה שימושי? כי עכשיו שאלה על $M$ ו-$w$ הפכה לשאלה על השפה של מכונה אחת.", hold=0.2),
    P("$M$ עוצרת על $w$ בדיוק כשהשפה של $K$ לא ריקה. זו רדוקציה מ-$H_{TM}$ אל המשלים של $E_{TM}$.", do=show("u-0")),
    P("משלימים בשני הצדדים, ובאותה פונקציה: המשלים של $H_{TM}$ אל $E_{TM}$.", do=show("u-1")),
    P("ו-$M$ עוצרת על $w$ בדיוק כשהשפה של $K$ היא כל $\\Sigma^*$. זו רדוקציה מ-$H_{TM}$ אל $ALL_{TM}$.",
      do=show("u-2")),
    P("ועוד דבר חשוב: $f$ רק **כותבת** את הקוד של $K$. היא לא מריצה את $M$, ולא את $K$.", do=show("u-c1")),
    P("לכן $f$ ניתנת לחישוב, גם כש-$K$ עצמה נתקעת בלולאה.", hold=0.5),
], stage='<div class="stack">' + w_map.code("k2", K_CODE).replace('class="codebox"', 'class="codebox" style="font-size:28px"')
         + st.card("u-c1", "trap", "⚠️ $f$ כותבת קוד, לא מריצה אותו") + "</div>",
   panel=w_map.rows("u", ROWS))

T_CODE = ["T(x):", "  if x = uu for some u:", "    run M on w", "    ACCEPT", "  else: REJECT"]
exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן. $L$ היא קבוצת המכונות שמקבלות את כל המילים מהצורה $uu$: מילה שכתובה פעמיים ברצף.",
      do=show("x-l"), say="שאלה ממבחן. אֵל היא קבוצת המכונות שמקבלות את כל המילים מהצורה יוּ יוּ: מילה שכתובה פעמיים ברצף."),
    P("והפונקציה מחזירה את המכונה $T$: על קלט כזה היא מריצה את $M$ על $w$ ומקבלת, ועל כל השאר דוחה.",
      do=show("x-code")),
    P("קודם, חישוביות: $f$ רק כותבת את הקוד של $T$. היא ניתנת לחישוב.", do=show("q-x-a")),
    P("אם $M$ עוצרת על $w$, אז $T$ מקבלת את כל המילים מהצורה $uu$, ולכן היא ב-$L$.", do=show("x-1"),
      say="אם אֵם עוצרת על דַּאבְּלְיוּ, אז טִי מקבלת את כל המילים מהצורה יוּ יוּ, ולכן היא באֵל."),
    P("ואם $M$ לא עוצרת, $T$ לא מקבלת אף מילה, ולכן היא לא ב-$L$.", do=show("x-2")),
    P("אז זו באמת רדוקציה מ-$H_{TM}$ אל $L$. אבל מה מותר להסיק ממנה?", hold=0.2),
    P("קושי זורם אל $L$: $L$ **לא** כריעה. ממנה אי אפשר להסיק ש-$L$ ניתנת לקבלה.", do=show("q-x-b")),
    P("והמסקנה ש-$L$ שלמה ב-$NP$ לא מתאימה: $L$ אפילו לא כריעה, ושפות ב-$NP$ כריעות.", do=show("q-x-c"),
      say="והמסקנה שאֵל שלמה באֶן פִּי לא מתאימה: אֵל אפילו לא כריעה, ושפות באֶן פִּי כריעות."),
    P("לכן אף אחת מהטענות האחרות לא נכונה.", do=show("q-ok-d"), hold=0.3),
    P("המלכודת: הרדוקציה נכונה, והמסקנה הפוכה. רדוקציה **אל** $L$ מוכיחה קושי, לא קלות.", do=show("x-t"), hold=0.6),
], stage='<div class="stack">'
         '<div id="x-l" class="bigmath h" style="font-size:40px">$L = \\{\\langle M\\rangle \\mid M \\text{ accepts every } uu\\}$</div>'
         + w_map.code("x", T_CODE).replace('class="codebox"', 'class="codebox h"').replace('id="x"', 'id="x-code"')
         + st.card("x-1", "ex", "$M$ עוצרת על $w$: $T \\in L$")
         + st.card("x-2", "ex", "$M$ לא עוצרת: $L(T) = \\emptyset$, $T \\notin L$")
         + st.card("x-t", "trap", "⚠️ $H_{TM} \\le_m L$ נותנת $L \\notin R$, לא $L \\in RE$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$f(\\langle M,w\\rangle) = \\langle T\\rangle$. '
         'מה נכון?</div>'
         + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $K_{M,w}$ מתעלמת מהקלט, מריצה את $M$ על $w$, ומקבלת אם הריצה נגמרה.", do=show("r-a")),
    P("אם $M$ עוצרת, השפה של $K$ היא $\\Sigma^*$. אם לא, היא ריקה.", do=show("r-b")),
    P("וכך מקבלים רדוקציה מ-$H_{TM}$ לכל שפה של מכונות שמבדילה בין השניים.", do=show("r-c")),
    P("והפונקציה רק כותבת קוד, ולכן היא תמיד ניתנת לחישוב. נתראה ברמה הבאה.", do=show("r-d"), hold=0.6),
], stage='<div class="stack">' + w_map.code("k3", K_CODE) + "</div>",
   panel=st.card("r-a", "rule", "🔑 התעלם, הרץ, קבל")
         + st.card("r-b", "rule", "🔑 עוצרת: $\\Sigma^*$. לא עוצרת: $\\emptyset$")
         + st.card("r-c", "rule", "🔑 $H_{TM} \\le_m \\overline{E_{TM}}$, $H_{TM} \\le_m ALL_{TM}$")
         + st.card("r-d", "trap", "⚠️ $f$ כותבת קוד, לא מריצה"))

VIDEO = Video("M04", "map", "בניית המכונה K ורדוקציות מ-H ו-A", [title, idea, run, use, exam, recap],
              bank={"24A-C-Q5": "d"})
