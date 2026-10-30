# -*- coding: utf-8 -*-
"""T05 · קונפיגורציות וריצה חסומה — video script (build: tools/video/vid.py T05).

Source: tools/courses_src/tm/T05.js (lesson + goal). Exam anchor: 26B-B-Q5 (reaching a configuration within k steps
is decidable), which no guided quiz uses. It is a decidability-topic question cited in this level's lesson.
Not used on purpose: the T05 quiz (4·6·3⁶, 7·3·4³, the n-cell language, …) and 23B-A-Q7 (cited in the lesson).
The counts are recomputed, the small count is brute-forced, and the repeating run comes from w_tm.trace().
"""
import itertools
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, REJ, BLANK, run_tm
import stage as st
import w_tm

# ---------------------------------------------------------------- facts (verified)
assert 5 * 4 * 3 ** 4 == 1620
# brute force: 2 states, tape alphabet {0, 1}, 2 cells -> 2 · 2 · 2² configurations
SMALL = list(itertools.product(["q_0", "q_1"], range(2), itertools.product("01", repeat=2)))
assert len(set(SMALL)) == 2 * 2 * 2 ** 2 == 16

# a machine that bounces between two cells: the third configuration is the first one again
D = {("q_0", "0"): ("q_1", "0", "R"), ("q_1", "0"): ("q_0", "0", "L")}
C, R = w_tm.trace(D, "q_0", "00", cap=40)
assert R == "loop" and max(h for _, _, h in C) <= 1                       # never leaves cells 0-1
assert (C[2][0], C[2][1], C[2][2]) == (C[0][0], C[0][1], C[0][2])
# that run has |Q| · n · |Γ|^n = 2 · 2 · 2² = 8 possible configurations ({0, ⊔} on 2 cells), so by step 9 one repeats
seen, rep = set(), None
for k, (q, t, h) in enumerate(C):
    key = (q, tuple(t[:2]), h)
    if key in seen:
        rep = k
        break
    seen.add(key)
assert rep == 2 <= 8


def bounded_halts(delta, w, n, cap):
    """the decider of the lesson: simulate at most cap steps inside n cells"""
    tape, pos, q = list(w) or [BLANK], 0, "q_0"
    for _ in range(cap + 1):
        if q in (ACC, REJ):
            return True
        if pos >= n:
            return False
        while pos >= len(tape):
            tape.append(BLANK)
        nxt = delta.get((q, tape[pos]))
        if nxt is None:
            return True
        q, b, d = nxt
        tape[pos] = b
        pos = max(0, pos - 1) if d == "L" else pos + 1
    return False


assert bounded_halts(D, "00", 2, 2 * 2 * 2 ** 2) is False
assert bounded_halts({("q_0", "0"): (ACC, "0", "R")}, "00", 2, 8) is True

Q = BANK["26B-B-Q5"]
assert Q["correctId"] == "a"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

T0, _ = w_tm.tape("t0", [("q_2", list("1X0"), 1)], 4, hidden=True)
TB, VB = w_tm.tape("tb", C[:3], 3, hidden=True)

FORM = "|Q| \\cdot n \\cdot |\\Gamma|^{n}"
FORM_SAY = "מספר המצבים, כפול אֶן, כפול גודל גמא בחזקת אֶן"

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("כמה תמונות מצב שונות יכולות להיות למכונה שנשארת בתוך מספר קבוע של תאים?"),
    P("נספור אותן, ונראה למה התשובה הופכת כל ריצה חסומה לבעיה כריעה.", hold=0.4),
], stage='<div class="kicker">T05 · מכונות טיורינג</div><h1>קונפיגורציות וריצה חסומה</h1>'
         '<p>לספור כמה קונפיגורציות יש למכונה שנשארת בתוך $n$ תאים, ולהבין למה ריצה חסומה היא תמיד כריעה.</p>',
   layout="title")

conf = Scene("conf", "קונפיגורציה", [
    P("**קונפיגורציה** היא תמונת מצב מלאה של המכונה ברגע אחד.", do=show("c-tape")),
    P("היא מורכבת משלושה דברים. המצב הנוכחי.", do=show("t0-st-q_2", "c-1")),
    P("מיקום הראש.", do=show("t0-hd1", "c-2")),
    P("ומה כתוב בכל תא על הסרט.", do=show("c-3")),
    P("אם יודעים את שלושתם, יודעים בדיוק מה המכונה תעשה מכאן והלאה.", do=show("c-4"), hold=0.3),
], stage=f'<div class="stack"><div id="c-tape" class="h">{T0}</div></div>',
   panel=st.card("c-1", "ex", "1. המצב: $q_2$")
         + st.card("c-2", "ex", "2. מיקום הראש: התא השני")
         + st.card("c-3", "ex", "3. תוכן הסרט: $1 X 0 \\sqcup$")
         + st.card("c-4", "rule", "🔑 קונפיגורציה קובעת את כל ההמשך"))

count = Scene("count", "כמה יש", [
    P("עכשיו נניח שהריצה כולה מתרחשת בתוך $n$ תאים. כמה קונפיגורציות שונות אפשריות?", do=show("n-q")),
    P("המצב: אחד מהמצבים של המכונה, כלומר $|Q|$ אפשרויות.", do=show("n-1"),
      say="המצב: אחד מהמצבים של המכונה, כלומר גודל קְיוּ אפשרויות."),
    P("מיקום הראש: אחד מתוך $n$ התאים, כלומר $n$ אפשרויות.", do=show("n-2")),
    P("ותוכן הסרט: בכל אחד מ-$n$ התאים יש $|\\Gamma|$ אפשרויות, ולכן $|\\Gamma|^{n}$.", do=show("n-3"),
      say="ותוכן הסרט: בכל אחד מאֶן התאים יש גודל גמא אפשרויות, ולכן גודל גמא בחזקת אֶן."),
    P("שלוש בחירות בלתי תלויות, ולכן כופלים.", do=hide("n-q") + show("n-f"), hold=0.3, say="שלוש בחירות בלתי תלויות, ולכן כופלים: " + FORM_SAY + "."),
    P("למשל, חמישה מצבים, שלושה תווים בסרט, וארבעה תאים: חמש, כפול ארבע, כפול שלוש בחזקת ארבע. זה אלף שש מאות עשרים.",
      do=show("n-ex")),
    P("שימו לב לחזקה: הבסיס הוא גודל גמא, והמעריך הוא מספר התאים. ההחלפה ביניהם היא הטעות הנפוצה.",
      do=show("n-t"), hold=0.4),
], stage=f'<div class="stack"><div id="n-q" class="bigmath h">?</div>'
         f'<div id="n-f" class="bigmath h">${FORM}$</div>'
         '<div id="n-ex" class="bigmath h" style="font-size:44px">$5 \\cdot 4 \\cdot 3^{4} = 1620$</div></div>',
   panel=st.card("n-1", "ex", "מצב: $|Q|$ אפשרויות")
         + st.card("n-2", "ex", "ראש: $n$ אפשרויות")
         + st.card("n-3", "ex", "סרט: $|\\Gamma|^{n}$ אפשרויות")
         + st.card("n-t", "trap", "⚠️ $|\\Gamma|^{n}$, לא $n^{|\\Gamma|}$"))

bph = w_tm.run_phrases("tb", D, C[:3], VB)
bounce = Scene("bounce", "חוזרים על עצמנו", [
    P("ולמה זה חשוב? בגלל עיקרון שובך היונים. הנה מכונה שנשארת בשני תאים.", do=show("b-tape", "tb-hd0", "tb-st-q_0")),
    *bph,
    P("זו בדיוק הקונפיגורציה שהתחלנו בה: אותו מצב, אותו ראש, אותו סרט.", do=show("b-1")),
    P("והמכונה דטרמיניסטית. מאותה קונפיגורציה היא תעשה שוב את אותם צעדים, ותחזור לכאן שוב ושוב.", do=show("b-2")),
    P("וזה קורה לכל מכונה: אם היא נשארת בתוך $n$ תאים ורצה יותר צעדים ממספר הקונפיגורציות,", do=show("b-3")),
    P("אחת מהן חייבת לחזור. ולכן המכונה בלולאה, ולעולם לא תעצור.", hold=0.4),
], stage=f'<div class="stack"><div id="b-tape" class="h">{TB}</div></div>',
   panel=st.card("b-1", "ex", "קונפיגורציה שחזרה: $q_0 \\; 0 0$")
         + st.card("b-2", "rule", "🔑 דטרמיניסטית + חזרה = לולאה")
         + st.card("b-3", "rule", f"🔑 יותר מ-${FORM}$ צעדים בתוך $n$ תאים: לולאה"))

decide = Scene("decide", "מכריעים ריצה חסומה", [
    P("ומכאן אלגוריתם. השאלה: האם $M$ עוצרת על $w$, בלי לצאת מ-$n$ תאים?", do=show("e-q")),
    P("מסמלצים את $M$ צעד אחר צעד, עד החסם של מספר הקונפיגורציות.", do=show("e-1")),
    P("אם היא עצרה, עונים כן. אם הראש יצא מ-$n$ התאים, עונים לא.", do=show("e-2")),
    P("ואם עברנו את החסם בלי עצירה, היא בלולאה, ועונים לא.", do=show("e-3")),
    P("הסימולציה תמיד נגמרת, ולכן הבעיה **כריעה**. וכך גם כל שאלה על ריצה עם חסם על מספר הצעדים.", do=show("e-4")),
    P("אבל בלי חסם, ״האם $M$ עוצרת על $w$״ היא בעיית העצירה, ואותה אי אפשר להכריע.", do=show("e-t"), hold=0.4),
], stage='<div class="stack">'
         + st.card("e-q", "plain", "האם $M$ עוצרת על $w$ בתוך $n$ תאים?")
         + st.card("e-1", "ex", f"סמלץ עד ${FORM}$ צעדים")
         + st.card("e-2", "ex", "עצרה: כן · הראש יצא: לא")
         + st.card("e-3", "ex", "עברה את החסם: לולאה, לא")
         + "</div>",
   panel=st.card("e-4", "rule", "🔑 חסם על הריצה = סימולציה סופית = כריע")
         + st.card("e-t", "trap", "⚠️ בלי חסם: בעיית העצירה, לא כריעה"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: קונפיגורציה $C$ **ישיגה** מ-$w$ אם הריצה של $M$ על $w$ מגיעה אליה."),
    P("והשפה: כל הרביעיות $M$, $k$, $w$, $C$, כך ש-$C$ ישיגה מ-$w$ אחרי לכל היותר $k$ צעדים. מה הסיווג?",
      say="והשפה: כל הרביעיות אֵם, קֵיי, דַּאבְּלְיוּ, סִי, כך שסִי ישיגה מדַּאבְּלְיוּ אחרי לכל היותר קֵיי צעדים. מה הסיווג?"),
    P("המלכודת: לראות ״ריצה של מכונה כלשהי״ ולחשוב על בעיית העצירה.", do=show("x-t")),
    P("אבל כאן יש חסם: $k$ צעדים, ו-$k$ חלק מהקלט.", do=show("x-1")),
    P("מסמלצים את $M$ על $w$ לכל היותר $k$ צעדים, ואחרי כל צעד משווים לקונפיגורציה $C$.", do=show("x-2")),
    P("הגענו ל-$C$? מקבלים. נגמרו $k$ הצעדים, או שהמכונה עצרה לפני? דוחים.", do=show("x-3")),
    P("הסימולציה תמיד עוצרת, ולכן השפה ניתנת להכרעה.", do=show("q-ok-a", "q-x-b", "q-x-c", "q-x-d"), hold=0.6),
], stage='<div class="stack">'
         + st.card("x-t", "trap", "⚠️ ״ריצה של $M$״ ≠ בעיית העצירה")
         + st.card("x-1", "rule", "🔑 חסם: $k$ צעדים")
         + st.card("x-2", "ex", "סמלץ $k$ צעדים, השווה ל-$C$ אחרי כל צעד")
         + st.card("x-3", "ex", "הגענו: קבל · לא הגענו: דחה")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$C$ ישיגה מ-$w$ ב-$M$ אחרי לכל היותר $k$ צעדים. '
         'מה נכון על $L$?</div>'
         + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: קונפיגורציה היא מצב, מיקום ראש ותוכן סרט.", do=show("r-1")),
    P("בתוך $n$ תאים יש לכל היותר $|Q| \\cdot n \\cdot |\\Gamma|^{n}$ קונפיגורציות.", do=show("r-2"),
      say="בתוך אֶן תאים יש לכל היותר " + FORM_SAY + " קונפיגורציות."),
    P("ריצה ארוכה מזה חוזרת על קונפיגורציה, ולכן היא לולאה. וכל ריצה חסומה כריעה: פשוט מסמלצים עד החסם. נתראה ברמה הבאה.",
      do=show("r-3"), hold=0.6),
], stage=f'<div class="stack"><div class="bigmath">${FORM}$</div></div>',
   panel=st.card("r-1", "rule", "🔑 קונפיגורציה = מצב + ראש + סרט")
         + st.card("r-2", "rule", f"🔑 ${FORM}$")
         + st.card("r-3", "rule", "🔑 חסם על הריצה: מסמלצים, ולכן כריע"))

VIDEO = Video("T05", "tm", "קונפיגורציות וריצה חסומה", [title, conf, count, bounce, decide, exam, recap],
              bank={"26B-B-Q5": "a"})
