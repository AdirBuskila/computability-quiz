# -*- coding: utf-8 -*-
"""T04 · מה השפה של המכונה, ואיך בונים אחת — video script (build: tools/video/vid.py T04).

Source: tools/courses_src/tm/T04.js (lesson + goal). Exam anchor: 26B-B-Q2 (the language of a diagram over {a, b}),
which no guided quiz uses. Not used on purpose: the T04 quiz (the X/Y machine for 0ⁿ1ⁿ, the left-edge loop machine,
the parity machine) and 24B-A-Q4 / 25B-B-Q10 (cited in the lesson; 25B-B-Q10 is T03's exam).
The worked machine and the exam diagram are run with w_tm.trace() / run_tm on every word up to length 8 and compared
with the language the video names; the high-level algorithm is implemented below and checked the same way.
"""
import itertools
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, REJ, BLANK, run_tm, words, PREDS
import stage as st
import w_tm

# ---------------------------------------------------------------- machines (verified)
# M: q_1 = "the last symbol was 1"; a second 1 in a row has no transition (reject); the end of the input accepts
D = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): ("q_1", "1", "R"), ("q_0", BLANK): (ACC, BLANK, "R"),
     ("q_1", "0"): ("q_0", "0", "R"), ("q_1", BLANK): (ACC, BLANK, "R")}
for w in words(8):
    assert run_tm(D, "q_0", w)[0] == ("reject" if "11" in w else "accept"), w     # halts on every input
GRID = ["", "0", "1", "00", "01", "10", "11", "010", "011", "101", "110", "111"]
RES = {w: run_tm(D, "q_0", w)[0] == "accept" for w in GRID}
assert [w for w in GRID if not RES[w]] == ["11", "011", "110", "111"]
CR, RR = w_tm.trace(D, "q_0", "0110")
assert RR == "reject" and len(CR) == 4 and CR[2][0] == "q_1"     # 2 steps, then q_1 reads 1: no transition


# high-level decider for "as many 0s as 1s": mark the first unmarked symbol, then an unmarked one of the other kind
def eq_rounds(w):
    t, snaps = list(w), []
    while True:
        i = next((k for k, c in enumerate(t) if c != "X"), None)
        if i is None:
            return "accept", snaps
        want = "1" if t[i] == "0" else "0"
        t[i] = "X"
        snaps.append((t[:], i))
        j = next((k for k, c in enumerate(t) if c == want), None)
        if j is None:
            return "reject", snaps
        t[j] = "X"
        snaps.append((t[:], j))


for w in words(8):
    assert (eq_rounds(w)[0] == "accept") == PREDS["eqcount"](w), w
RA, SA = eq_rounds("0110")
RB, SB = eq_rounds("011")
assert RA == "accept" and len(SA) == 4 and RB == "reject" and len(SB) == 3


def pseudo(w, snaps):
    """configurations for the tape widget: no state badge, the head on the cell just marked"""
    return [("q_0", list(w), 0)] + [("q_0", t, i) for t, i in snaps]


PA, PB = pseudo("0110", SA), pseudo("011", SB)

# exam 26B-B-Q2, transcribed from the diagram (alphabet {a, b})
DX = {("q_0", "b"): ("q_1", "a", "R"), ("q_0", BLANK): (ACC, BLANK, "R"), ("q_1", "b"): ("q_1", "b", "R"),
      ("q_1", BLANK): ("q_2", BLANK, "L"), ("q_2", "b"): ("q_3", "b", "L"), ("q_3", "b"): ("q_2", "b", "L"),
      ("q_3", "a"): (ACC, "a", "R")}
AB = [""] + ["".join(p) for n in range(1, 9) for p in itertools.product("ab", repeat=n)]
for w in AB:
    r = run_tm(DX, "q_0", w)[0]
    assert r == ("accept" if set(w) <= {"b"} and len(w) % 2 == 0 else "reject"), (w, r)   # (bb)*, always halts
XG = ["", "b", "bb", "bbb", "bbbb", "ab"]
XRES = {w: run_tm(DX, "q_0", w)[0] == "accept" for w in XG}
assert XRES == {"": True, "b": False, "bb": True, "bbb": False, "bbbb": True, "ab": False}
CX, RX = w_tm.trace(DX, "q_0", "bb")
assert RX == "accept" and len(CX) - 1 == 5

Q = BANK["26B-B-Q2"]
assert Q["correctId"] == "a"
OPTS = [(o["id"], f'${o["value"]}$' if o["type"] == "math" else o["value"]) for o in Q["options"]]

TR, VR = w_tm.tape("tr", CR, 5, hidden=True)
TA, VA = w_tm.tape("ha", PA, 4, hidden=True)
TB, VB = w_tm.tape("hb", PB, 3, hidden=True)
TX, VX = w_tm.tape("tx", CX, 4, hidden=True)


def wtex(w):
    return "\\varepsilon" if w == "" else w


def grid(pfx, ws, res):
    cells = "".join(f'<div id="{pfx}-{i}" class="wc h"><span>${wtex(w)}$</span>'
                    f'<span class="v {"ok" if res[w] else "bad"}">{"✓" if res[w] else "✗"}</span></div>'
                    for i, w in enumerate(ws))
    return f'<div class="tmgrid">{cells}</div>'


# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה שני כיוונים: מקבלים מכונה ומגלים מה השפה שלה."),
    P("ומקבלים שפה, ומתארים אלגוריתם שמכריע אותה.", hold=0.3),
    P("ובסוף, שאלה ממבחן עם דיאגרמה.", hold=0.4),
], stage='<div class="kicker">T04 · מכונות טיורינג</div><h1>מה השפה של המכונה, ואיך בונים אחת</h1>'
         '<p>לגלות שפה של מכונה מהרצות על מילים קצרות, ולתאר ברמה גבוהה אלגוריתם שמכריע שפה.</p>',
   layout="title")

method = Scene("method", "השיטה", [
    P("איך מגלים את $L(M)$? בשלושה שלבים.", do=show("m-1")),
    P("מריצים את המכונה על המילים הקצרות, לפי הסדר: המילה הריקה, אפס, אחת, אפס אפס, וכן הלאה.", do=show("m-2")),
    P("רושמים מי התקבלה ומי לא, ומחפשים דפוס.", do=show("m-3")),
    P("ואז בודקים שהדפוס גם **מסביר** למה המילים האחרות נדחות.", do=show("m-4"), hold=0.4),
], stage='<div class="stack"><div class="bigmath">$L(M) = \\; ?$</div></div>',
   panel=st.card("m-1", "plain", "שלושה שלבים:")
         + st.card("m-2", "ex", "1. מריצים על מילים קצרות: $\\varepsilon, 0, 1, 00, \\dots$")
         + st.card("m-3", "ex", "2. רושמים ✓ / ✗ ומחפשים דפוס")
         + st.card("m-4", "rule", "🔑 3. בודקים שהדפוס מסביר את הדחיות"))

runs = Scene("runs", "מריצים", [
    P("הנה המכונה.", do=show("g-tab")),
    P("המילה הריקה מתקבלת: $q_0$ קורא רווח ועובר ל-$q_{acc}$. גם אפס ואחת מתקבלות.", do=show("g-0", "g-1", "g-2"),
      say="המילה הריקה מתקבלת: קְיוּ אפס קורא רווח ועובר לקְיוּ אַקְסֶפְּט. גם אפס ואחת מתקבלות."),
    P("באורך שתיים: אפס אפס, אפס אחת ואחת אפס מתקבלות. אבל אחת אחת נדחית.", do=show("g-3", "g-4", "g-5", "g-6")),
    P("באורך שלוש נדחות שלוש מילים, ובכולן מופיע אותו דבר: שתי אחדות צמודות.", do=show(*[f"g-{i}" for i in range(7, 12)])),
    P("הדפוס: המכונה מקבלת את המילים שאין בהן $11$.", do=show("g-p"),
      say="הדפוס: המכונה מקבלת את המילים שאין בהן אחת אחת."),
], stage=f'<div class="stack"><div id="g-tab" class="h">{w_tm.delta_table("g0", D, ["q_0", "q_1"], ["0", "1", BLANK])}</div>'
         f'{grid("g", GRID, RES)}</div>',
   panel=st.card("g-p", "rule", "🔑 $L(M)$ = המילים שאין בהן $11$"))

why_ph = w_tm.run_phrases("tr", D, CR, VR)
w_tm.table_do(why_ph, "w0", CR, D)
why = Scene("why", "למה זה הדפוס", [
    P("עכשיו שלב שלוש: למה? נריץ את $0110$.", do=show("w-tape", "tr-hd0", "tr-st-q_0")),
    *why_ph,
    P("המצב $q_1$ זוכר שהתו האחרון היה $1$. ואם מגיע עוד $1$, אין מעבר, והמכונה דוחה.", do=show("w-1"),
      say="המצב קְיוּ אחת זוכר שהתו האחרון היה אחת. ואם מגיעה עוד אחת, אין מעבר, והמכונה דוחה."),
    P("ובלי שתי אחדות צמודות, המכונה מגיעה לסוף הקלט ומקבלת. היא עוצרת על כל קלט, ולכן גם **מכריעה**.",
      do=show("w-2"), hold=0.4),
], stage=f'<div class="stack">{w_tm.delta_table("w0", D, ["q_0", "q_1"], ["0", "1", BLANK])}'
         f'<div id="w-tape" class="h">{TR}</div></div>',
   panel=st.card("w-1", "ex", "$q_1$ = ״התו האחרון היה $1$״")
         + st.card("w-2", "rule", "🔑 תמיד עוצרת: מכריעה את השפה"))

design = Scene("design", "בונים מכונה", [
    P("ועכשיו בכיוון ההפוך: נתונה שפה, ורוצים מכונה שמכריעה אותה.", do=show("d-L")),
    P("השפה: כל המילים שיש בהן אותו מספר של אפסים ושל אחדות, בכל סדר.", do=show("d-L2")),
    P("לא כותבים טבלה. מתארים אלגוריתם בשלבים, שכל אחד מהם אפשר לבצע על סרט.", do=show("d-1")),
    P("שלב אחד: מוצאים את התו הראשון שעוד לא סומן. אם אין כזה, מקבלים.", do=show("d-2")),
    P("שלב שתיים: מסמנים אותו ב-$X$, ומחפשים תו מהסוג השני שלא סומן. אם אין, דוחים.", do=show("d-3")),
    P("ואם יש, מסמנים גם אותו, חוזרים להתחלה, וחוזרים על הכול.", do=show("d-4"), hold=0.3),
], stage='<div class="stack"><div id="d-L" class="bigmath h">$L = \\{ w \\mid \\#_0(w) = \\#_1(w) \\}$</div>'
         + st.card("d-L2", "plain", "אותו מספר של $0$ ושל $1$, בכל סדר")
         + "</div>",
   panel=st.card("d-1", "plain", "אלגוריתם ברמה גבוהה:")
         + st.card("d-2", "ex", "1. התו הראשון שלא סומן. אין? <b>קבל</b>")
         + st.card("d-3", "ex", "2. סמן $X$, וחפש תו מהסוג השני. אין? <b>דחה</b>")
         + st.card("d-4", "ex", "3. סמן גם אותו, חזור להתחלה"))


def mark_do(pfx, confs, versions, s):
    """pseudo-run step: every cell whose symbol changed, and the head to the cell just marked"""
    do = []
    for i in range(len(versions)):
        k0, k1 = w_tm._version(versions, i, confs, s - 1), w_tm._version(versions, i, confs, s)
        if k0 != k1:
            do += hide(f"{pfx}-c{i}-{k0}") + show(f"{pfx}-c{i}-{k1}")
    h0, h1 = confs[s - 1][2], confs[s][2]
    if h0 != h1:
        do += hide(f"{pfx}-hd{h0}") + show(f"{pfx}-hd{h1}")
    return do


def mark_phrases(pfx, confs, versions, says):
    return [P(s, do=mark_do(pfx, confs, versions, k + 1)) for k, s in enumerate(says)]


demo = Scene("demo", "מריצים את האלגוריתם", [
    P("נריץ על $0110$.", do=show("ha-w", "ha-hd0")),
    *mark_phrases("ha", PA, VA, ["הראשון שלא סומן הוא אפס. מסמנים אותו.",
                                 "ומחפשים אחת: הנה, בתא השני. מסמנים.",
                                 "סיבוב שני: הראשון שלא סומן הוא אחת. מסמנים, ומחפשים אפס.",
                                 "מצאנו, בתא האחרון. מסמנים."]),
    P("סיבוב שלישי: אין תו שלא סומן, ולכן מקבלים.", do=show("ha-v")),
    P("ועכשיו $011$.", do=show("hb-w", "hb-hd0")),
    *mark_phrases("hb", PB, VB, ["מסמנים את האפס.", "ואת האחת הראשונה.",
                                 "סיבוב שני: מסמנים את האחת שנשארה, ומחפשים אפס."]),
    P("אין אפס שלא סומן, ולכן דוחים.", do=show("hb-v")),
    P("כל סיבוב מסמן תווים חדשים, אז האלגוריתם תמיד עוצר. לכן הוא **מכריע**, ולא רק מקבל.", do=show("d-k"),
      hold=0.4),
], stage=f'<div class="stack"><div id="ha-w" class="h">{TA}</div><div id="hb-w" class="h">{TB}</div></div>',
   panel=st.verdict("ha", True, "$0110$: מתקבלת ✓") + st.verdict("hb", False, no="$011$: נדחית ✗")
         + st.card("d-k", "rule", "🔑 מכריע = עוצר על כל קלט: כל סיבוב מסמן תווים"))

exph = w_tm.run_phrases("tx", DX, CX, VX)
exam1 = Scene("exam1", "שאלה ממבחן", [
    P("שאלה ממבחן: מכונה דטרמיניסטית בדיאגרמה, מעל $a$ ו-$b$. מעבר שלא מצויר הולך לדחייה."),
    P("איזה ביטוי רגולרי מתאר את השפה שלה? לא מנחשים. מריצים, קודם על $bb$.", do=show("x-tape", "tx-hd0", "tx-st-q_0")),
    *exph,
    P("ה-$b$ הראשון הפך ל-$a$. הוא מסמן את תחילת הסרט, וכך המכונה יודעת מתי חזרה עד ההתחלה.", do=show("x-1")),
], stage='<div class="stack">' + st.raster("xr", "images/exams/26B-B-Q2.png", 820, (1368, 547))
         + f'<div id="x-tape" class="h">{TX}</div></div>',
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>איזה ביטוי רגולרי מתאר את $L(M)$?</div>'
         + st.options("q", OPTS)
         + st.card("x-1", "ex", "$a$ בתא הראשון: סימן התחלה"))

exam2 = Scene("exam2", "הדפוס", [
    P("עכשיו מילים קצרות. המילה הריקה מתקבלת מיד, וגם $bb$, כמו שראינו.", do=show("xg-0", "xg-2")),
    P("בדרך חזרה, $q_2$ ו-$q_3$ מתחלפים בכל צעד. לכן הם סופרים זוגיות של ה-$b$.", do=show("y-1")),
    P("מילה עם $b$ אחד, או עם שלושה, נדחית. עם ארבעה היא מתקבלת.", do=show("xg-1", "xg-3", "xg-4")),
    P("ומילה שמתחילה ב-$a$ נדחית מיד: מ-$q_0$ אין מעבר עם $a$.", do=show("xg-5", "q-x-b", "q-x-c")),
    P("וגם מילה שבה $a$ מופיע אחרי $b$ נדחית: $q_1$ מכיר רק $b$ ורווח.", do=show("y-2")),
    P("אז השפה היא מספר זוגי של $b$, ותו לא: $bb$ בכוכבית.", do=show("q-ok-a", "q-x-d"), hold=0.6),
], stage='<div class="stack">' + st.raster("xr2", "images/exams/26B-B-Q2.png", 820, (1368, 547))
         + grid("xg", XG, XRES) + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>איזה ביטוי רגולרי מתאר את $L(M)$?</div>'
         + st.options("q", OPTS, notes={"b": "מתחילה ב-$a$", "c": "מתחילה ב-$a$"})
         + st.card("y-1", "ex", "$q_2 \\leftrightarrow q_3$: זוגיות של $b$")
         + st.card("y-2", "trap", "⚠️ $a$ אחרי $b$: גם דחייה"))

recap = Scene("recap", "סיכום", [
    P("לסיכום: כדי למצוא את $L(M)$, מריצים על מילים קצרות ומחפשים דפוס.", do=show("r-1")),
    P("ובודקים שהדפוס מסביר גם את הדחיות. כאן, מצב שזוכר את התו האחרון.", do=show("r-2")),
    P("וכדי לבנות מכונה: מתארים אלגוריתם בשלבים, מסמנים מה שכבר טופל, ומוודאים שהוא תמיד עוצר. נתראה ברמה הבאה.",
      do=show("r-3"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$L(M) = \\; ?$</div></div>',
   panel=st.card("r-1", "rule", "🔑 מריצים על מילים קצרות, מחפשים דפוס")
         + st.card("r-2", "rule", "🔑 הדפוס חייב להסביר את הדחיות")
         + st.card("r-3", "rule", "🔑 אלגוריתם: שלבים, סימון, עצירה תמיד"))

VIDEO = Video("T04", "tm", "מה השפה של המכונה, ואיך בונים אחת",
              [title, method, runs, why, design, demo, exam1, exam2, recap], bank={"26B-B-Q2": "a"})
