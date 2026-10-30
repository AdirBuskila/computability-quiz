# -*- coding: utf-8 -*-
"""M06 · מלכודות: ∅, Σ* ומשלים — video script (build: tools/video/vid.py M06).

Source: tools/courses_src/map/M06.js (lesson + goal). Exam anchor: 23A-A-Q13 (a finite non-trivial language always
reduces to an infinite non-trivial one), which no guided quiz uses. Not used on purpose: the five original quiz
questions of M06 (the video shows the "no home" picture for B = ∅ and lets the viewer draw the rules about ∅ and Σ*;
the union example and A <=m co-A are left to the quiz) and 23S-A-Q24 (the M06 quiz).
The rules are brute-forced exactly like map/check.py (kind brute-universe): every pair of languages over a universe of
3 words, a reduction = any map of the 3 words that keeps the answer.
"""
import itertools
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_map

N = 3
FULL = (1 << N) - 1


def R(X, Y):
    """map/check.py reduction_exists: some f : U -> U with x in X <=> f(x) in Y"""
    return any(all(((X >> x) & 1) == ((Y >> f[x]) & 1) for x in range(N)) for f in itertools.product(range(N), repeat=N))


E, S = 0, FULL
ALL = range(FULL + 1)
assert all(R(A, E) == (A == E) for A in ALL)                     # A <=m ∅ only for A = ∅
assert all(R(A, S) == (A == S) for A in ALL)                     # A <=m Σ* only for A = Σ*
assert all(R(E, B) == (B != S) for B in ALL)                     # ∅ <=m B for every B ≠ Σ*
assert all(R(S, B) == (B != E) for B in ALL)                     # Σ* <=m B for every B ≠ ∅
NT = [X for X in ALL if X not in (E, S)]
assert all(R(A, B) for A in NT for B in NT)                      # (all decidable here) non-trivial to non-trivial

# the "nowhere to go" picture: A has words, B = ∅
EMPTY = w_map.bridge("z", [("1", "1", True), ("10", "10", True), ("0", "0", False)],
                     [("y", "y", False)], [("1", "y", "bad"), ("10", "y", "bad"), ("0", "y", "ok")], A="A", B="∅")
# decide-then-output: A = starts with 1 (decidable), B = A_TM; y_in ∈ A_TM, y_out ∉ A_TM
starts1 = lambda x: x.startswith("1")
XS = ["1", "10", "0", "01"]
DEC = w_map.bridge("d", [(x, x, starts1(x)) for x in XS], [("in", "y₊", True), ("out", "y₋", False)],
                   [(x, "in" if starts1(x) else "out", "ok") for x in XS], A="A", B="A_TM")

Q = BANK["23A-A-Q13"]
assert Q["correctId"] == "c"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר רדוקציות שהתשובה עליהן לא תלויה בחישוביות בכלל."),
    P("השפה הריקה, $\\Sigma^*$, ושפות כריעות. ובסוף שאלה ממבחן שנראית קשה, ונפתרת בשורה.", hold=0.4),
], stage='<div class="kicker">M06 · רדוקציות מיפוי</div><h1>מלכודות: $\\emptyset$, $\\Sigma^*$ ומשלים</h1>'
         '<p>לדעת אילו רדוקציות מותרות כשאחת השפות היא $\\emptyset$ או $\\Sigma^*$, ומה קורה עם שפות כריעות.</p>',
   layout="title")

home = Scene("home", "אין לאן למפות", [
    P("רדוקציה צריכה למצוא **בית** לכל מילה: מילה ב-$A$ צריכה לנחות בתוך $B$, ומילה מחוץ ל-$A$, מחוץ ל-$B$.",
      do=show("h-c1")),
    P("מה אם $B$ היא השפה הריקה? אין בה אף מילה.", do=show("z-L-1", "z-L-10", "z-L-0", "z-R-y")),
    P("המילים שמחוץ ל-$A$ מסתדרות: כל מילה מחוץ לשפה הריקה.", do=show("z-a-0")),
    P("אבל למילים שבתוך $A$ אין לאן לנחות. החצים האדומים לא מוצאים בית.", do=show("z-a-1", "z-a-10")),
    P("עצרו רגע ונסו לבד: אילו שפות $A$ בכל זאת מתרדדות אל השפה הריקה? ומה קורה כשהיעד הוא $\\Sigma^*$?",
      do=show("h-c2"), hold=1.5),
    P("בכל שאלה כזו, השאלה היא אחת: האם יש בית לכל מילה, גם לכן וגם ללא.", do=show("h-c3"), hold=0.3),
    P("ושפה היא **לא טריוויאלית** אם היא לא ריקה ולא $\\Sigma^*$. איתן אין בעיה של בית: יש מילה בפנים ויש בחוץ.",
      do=show("h-c5"), hold=0.4),
], stage=EMPTY,
   panel=st.card("h-c1", "rule", "🔑 כן צריך בית בתוך $B$, לא צריך בית מחוץ ל-$B$")
         + st.card("h-c2", "ex", "❓ $A \\le_m \\emptyset$ ? $A \\le_m \\Sigma^*$ ?")
         + st.card("h-c3", "rule", "🔑 יש בית לכל מילה?")
         + st.card("h-c5", "plain", "לא טריוויאלית: $\\emptyset \\ne B \\ne \\Sigma^*$"))

dec = Scene("dec", "שפה כריעה", [
    P("ועכשיו כלל חזק: שפה **כריעה** ולא טריוויאלית מתרדדת לכל שפה לא טריוויאלית.", hold=0.2),
    P("למשל $A$: המילים שמתחילות ב-1. ו-$B$: דווקא $A_{TM}$, שאינה כריעה.", do=show("d-c1")),
    P("בוחרים מראש שתי מילים קבועות: אחת בתוך $A_{TM}$, ואחת מחוץ לה. הן קיימות, כי $A_{TM}$ לא טריוויאלית.",
      do=show("d-R-in", "d-R-out")),
    P("הפונקציה **מכריעה** את $x$. אם $x$ מתחילה ב-1, היא מחזירה את המילה שבפנים.",
      do=show("d-L-1", "d-L-10", "d-a-1", "d-a-10")),
    P("ואחרת, את המילה שבחוץ.", do=show("d-L-0", "d-L-01", "d-a-0", "d-a-01")),
    P("זה מותר, כי $A$ כריעה: הפונקציה עוצרת תמיד. ושני הכיוונים נשמרים.", do=show("d-c2")),
    P("ולכן מרדוקציה אל שפה קשה לא מסיקים כלום על המקור. הוא יכול להיות קל לגמרי.", do=show("d-c3"), hold=0.4),
    P("ומילה על משלים: $L \\le_m \\overline{L}$ ו-$\\overline{L} \\le_m L$ הן אותה טענה, ובאותה פונקציה.",
      do=show("d-c4"), hold=0.4),
], stage=DEC,
   panel=st.card("d-c1", "plain", "$A$: מתחילות ב-1. $B = A_{TM}$")
         + st.card("d-c2", "rule", "🔑 $A$ כריעה ולא טריוויאלית: מתרדדת לכל $B$ לא טריוויאלית")
         + st.card("d-c3", "trap", "⚠️ $A \\le_m B$ עם $B$ קשה לא אומר ש-$A$ קשה")
         + st.card("d-c4", "ex", "$L \\le_m \\overline{L} \\iff \\overline{L} \\le_m L$"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: $L_1$ סופית, $L_2$ אינסופית, ושתיהן לא טריוויאליות. מה בהכרח נכון?"),
    P("הנקודה: שפה סופית היא תמיד כריעה. בודקים אם המילה נמצאת ברשימה.", do=show("e-1")),
    P("והיא לא טריוויאלית. לפי הכלל, היא מתרדדת לכל שפה לא טריוויאלית, ובפרט ל-$L_2$.", do=show("e-2", "q-ok-c"),
      hold=0.3),
    P("אז הטענה שבהכרח **אין** רדוקציה כזו נופלת.", do=show("q-x-a")),
    P("ובכיוון ההפוך? $L_2$ יכולה להיות $H_{TM}$, שהיא אינסופית ולא כריעה.", do=show("e-3")),
    P("אילו $H_{TM}$ הייתה מתרדדת לשפה סופית, היא הייתה כריעה. אז הרדוקציה ההפוכה לא בהכרח קיימת.",
      do=show("q-x-b")),
    P("אבל גם לא בהכרח חסרה: אם $L_2$ כריעה, למשל כל המילים באורך זוגי, היא כן מתרדדת ל-$L_1$.",
      do=show("e-4", "q-x-d"), hold=0.3),
    P("המלכודת: ״סופית״ מול ״אינסופית״ נשמע כמו הבדל בגודל. אבל מה שקובע הוא הכריעות.", do=show("e-t"), hold=0.6),
], stage='<div class="stack">'
         + st.card("e-1", "ex", "$L_1$ סופית, ולכן $L_1 \\in R$")
         + st.card("e-2", "rule", "🔑 $L_1 \\in R$, לא טריוויאלית: $L_1 \\le_m L_2$ תמיד")
         + st.card("e-3", "ex", "$L_2 = H_{TM}$: אין $L_2 \\le_m L_1$")
         + st.card("e-4", "ex", "$L_2$ = אורך זוגי: יש $L_2 \\le_m L_1$")
         + st.card("e-t", "trap", "⚠️ לא הגודל קובע, אלא הכריעות")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$L_1$ סופית, $L_2$ אינסופית, שתיהן לא טריוויאליות. '
         'מה נכון?</div>'
         + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: לכל מילה צריך בית, למילים של כן בתוך היעד, ולמילים של לא מחוצה לו.", do=show("r-1")),
    P("כשהיעד או המקור הם הריקה או $\\Sigma^*$, בודקים בדיוק את זה.", do=show("r-2")),
    P("ושפה כריעה ולא טריוויאלית מתרדדת לכל שפה לא טריוויאלית: מכריעים, ומחזירים מילה קבועה.", do=show("r-3")),
    P("ובפרט, כל שפה סופית ולא טריוויאלית. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$A \\le_m B$</div></div>',
   panel=st.card("r-1", "rule", "🔑 לכל מילה צריך בית")
         + st.card("r-2", "rule", "🔑 $\\emptyset$ או $\\Sigma^*$: יש בית לכן וללא?")
         + st.card("r-3", "rule", "🔑 כריעה: מכריעים ומחזירים מילה קבועה")
         + st.card("r-4", "trap", "⚠️ סופית = כריעה"))

VIDEO = Video("M06", "map", "מלכודות: ∅, Σ* ומשלים", [title, home, dec, exam, recap], bank={"23A-A-Q13": "c"})
