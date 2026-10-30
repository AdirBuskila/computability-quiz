# -*- coding: utf-8 -*-
"""N06 · לבנות רדוקציה, ולמצוא למה היא שבורה — video script (build: tools/video/vid.py N06).

Source: tools/courses_src/np/N06.js (lesson + goal). Exam anchor: 26B-B-Q15 (the identity as CLIQUE_3D <=p CLIQUE),
which no guided quiz uses.
Not used on purpose: the quiz questions of N06 (22A-A-Q14, f that finds the clique, and the five original ones: CLIS,
2CLIQUE, ECLQ, the identity CLIQUE -> IS, the F2SAT proof). The working gadget here is a new one (a universal vertex,
UCLIQUE), checked by brute force on every graph with up to 5 vertices.
"""
import itertools
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_np as g


# ---------------------------------------------------------------- facts (verified)
def all_graphs(nmax):
    for n in range(1, nmax + 1):
        Vn = [str(i) for i in range(n)]
        pairs = list(itertools.combinations(Vn, 2))
        for bits in range(1 << len(pairs)):
            yield Vn, frozenset(frozenset(p) for i, p in enumerate(pairs) if bits >> i & 1)


def clique(V, E, k):
    return g.has(V, E, k, g.is_clique)


def uclique(V, E, k):
    """UCLIQUE: G has a vertex adjacent to all others, and a clique of size k"""
    univ = any(all(frozenset((u, v)) in E for v in V if v != u) for u in V)
    return univ and clique(V, E, k)


def add_u(V, E):
    return V + ["u"], E | frozenset(frozenset((v, "u")) for v in V)


for Vn, En in all_graphs(5):                       # CLIQUE <=p UCLIQUE by <G, k> -> <G + u, k + 1>
    for k in range(1, len(Vn) + 1):
        assert clique(Vn, En, k) == uclique(*add_u(Vn, En), k + 1)


def deg_ok(V, E):
    return all(sum(1 for e in E if v in e) <= 3 for v in V)


def clique3d(V, E, k):
    return deg_ok(V, E) and clique(V, E, k)


# the counterexample on screen: a 4-clique, and vertex 5 hanging on vertex 1 (degree 4)
V = ["1", "2", "3", "4", "5"]
E = g.E_(("1", "2"), ("1", "3"), ("1", "4"), ("2", "3"), ("2", "4"), ("3", "4"), ("1", "5"))
assert clique(V, E, 4) and not clique3d(V, E, 4) and sum(1 for e in E if "1" in e) == 4
# identity fails exactly in the "no" direction: x in CLIQUE_3D -> x in CLIQUE always holds
for Vn, En in all_graphs(5):
    for k in range(1, len(Vn) + 1):
        if clique3d(Vn, En, k):
            assert clique(Vn, En, k)
# the repair: when some degree is above 3, output a fixed "no" instance (one vertex, k = 2)
NO = (["0"], frozenset(), 2)
assert not clique(*NO)


def fixed(Vn, En, k):
    return (Vn, En, k) if deg_ok(Vn, En) else NO


for Vn, En in all_graphs(5):
    for k in range(1, len(Vn) + 1):
        assert clique3d(Vn, En, k) == clique(*fixed(Vn, En, k))

# the broken example: f decides HAMPATH first, then writes a fixed yes / no instance of CLIQUE
def has_hampath(Vn, En):
    return len(Vn) == 1 or any(all(frozenset((S[i], S[i + 1])) in En for i in range(len(S) - 1))
                               for S in itertools.permutations(Vn))


YES_I, NO_I = (["a", "b"], g.E_(("a", "b")), 2), (["a"], frozenset(), 2)
assert clique(*YES_I) and not clique(*NO_I)
for Vn, En in all_graphs(4):                       # both directions hold; only the running time fails
    assert has_hampath(Vn, En) == clique(*(YES_I if has_hampath(Vn, En) else NO_I))

Q = BANK["26B-B-Q15"]
assert Q["correctId"] == "d"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

UV = ["1", "2", "3", "4", "u"]
UE = g.E_(("1", "2"), ("2", "3"), ("1", "3"), ("3", "4"))
UV2, UE2 = add_u(UV[:-1], UE)
UPOS = {"1": (150, 140), "2": (420, 110), "3": (300, 330), "4": (130, 470), "u": (560, 420)}
GU = g.graph_svg("gu", UV2, UE2, UPOS, w=700, h=580, hidden=[e for e in UE2 if "u" in e], scale=1.0)
assert clique(UV[:-1], UE, 3) and clique(UV2, UE2, 4)

POS = {"1": (300, 110), "2": (520, 210), "3": (470, 440), "4": (200, 400), "5": (90, 150)}
GX = g.graph_svg("gx", V, E, POS, w=620, h=540, scale=0.72)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נבנה רדוקציה עם גאדג'ט, ונלמד למצוא את המקום שבו רדוקציה נשברת."),
    P("לכל רדוקציה נשאל את אותן שלוש שאלות, בכל פעם.", hold=0.4),
], stage='<div class="kicker">N06 · P, NP ו-NP-שלמות</div><h1>בונים ושוברים רדוקציות פולינומיות</h1>'
         '<p>לבחור $f$ שעובדת, או להסביר איזה תנאי נופל: פולינומיות, הכיוון החיובי, או הכיוון השלילי.</p>',
   layout="title")

checks = Scene("checks", "שלוש בדיקות", [
    P("כל שאלה על רדוקציה פולינומית היא אחת משתיים: לבחור פונקציה שעובדת, או להסביר למה פונקציה שבורה."),
    P("ובשתיהן עוברים על אותן שלוש בדיקות.", do=show("k-1")),
    P("האם $f$ רצה בזמן פולינומי? מותר לה להכריע את שפת המקור, אבל רק אם זה פולינומי.", do=show("k-2"),
      say="האם אֶף רצה בזמן פולינומי? מותר לה להכריע את שפת המקור, אבל רק אם זה פולינומי."),
    P("ובשפה כמו $CLIQUE$, הכרעה בזמן פולינומי דורשת $P = NP$.",
      say="ובשפה כמו קְלִיק, הכרעה בזמן פולינומי דורשת שפִּי שווה אֶן פִּי."),
    P("אם יש פתרון במקור, האם יש פתרון בפלט?", do=show("k-3")),
    P("ואם **אין** פתרון במקור, האם בטוח שאין בפלט? זו הבדיקה שהכי קל לשכוח.", do=show("k-4"), hold=0.4),
], stage='<div class="stack" style="gap:26px">'
         '<div id="k-1" class="card plain h" style="font-size:38px">שלוש בדיקות לכל $f$:</div>'
         '<div id="k-2" class="card rule h" style="font-size:36px">1️⃣ $f$ רצה בזמן פולינומי</div>'
         '<div id="k-3" class="card rule h" style="font-size:36px">2️⃣ $x \\in A \\Rightarrow f(x) \\in B$</div>'
         '<div id="k-4" class="card rule h" style="font-size:36px">3️⃣ $x \\notin A \\Rightarrow f(x) \\notin B$</div></div>',
   layout="full")

gadget = Scene("gadget", "גאדג'ט שעובד", [
    P("נבנה רדוקציה. שפת היעד: גרפים שיש בהם קליקה בגודל $k$, **וגם** קודקוד שמחובר לכל השאר.", do=show("u-g", "u-c0"),
      say="נבנה רדוקציה. שפת היעד: גרפים שיש בהם קליקה בגודל קֵיי, וגם קודקוד שמחובר לכל השאר."),
    P("הגאדג'ט: מוסיפים קודקוד חדש, $u$, ומחברים אותו לכל הקודקודים. ומגדילים את $k$ באחד.",
      do=show(*[g.eid("gu", "u", v, UV2) for v in UV[:-1]], "u-c1"),
      say="הגאדג'ט: מוסיפים קודקוד חדש, יוּ, ומחברים אותו לכל הקודקודים. ומגדילים את קֵיי באחד."),
    P("בדיקה ראשונה: הבנייה פולינומית. קודקוד אחד ועוד צלע לכל קודקוד.", do=show("u-c2")),
    P("בדיקה שנייה: בגרף יש קליקה בגודל שלוש, אחת, שתיים ושלוש.",
      do=show(*g.hv("gu", "1", "2", "3"))),
    P("מוסיפים לה את $u$, שמחובר לכולם, ומקבלים קליקה בגודל ארבע. ו-$u$ הוא הקודקוד שמחובר לכל השאר.",
      do=show(*g.hv("gu", "u"), "u-c3"),
      say="מוסיפים לה את יוּ, שמחובר לכולם, ומקבלים קליקה בגודל ארבע. ויוּ הוא הקודקוד שמחובר לכל השאר."),
    P("בדיקה שלישית, הכיוון השלילי: נניח שבגרף החדש יש קליקה בגודל $k$ ועוד אחד.", do=show("u-c4"),
      say="בדיקה שלישית, הכיוון השלילי: נניח שבגרף החדש יש קליקה בגודל קֵיי ועוד אחד."),
    P("מוחקים ממנה קודקוד אחד: את $u$ אם הוא בפנים, ואחרת קודקוד כלשהו. נשארת קליקה בגודל $k$ בגרף המקורי.",
      say="מוחקים ממנה קודקוד אחד: את יוּ אם הוא בפנים, ואחרת קודקוד כלשהו. נשארת קליקה בגודל קֵיי בגרף המקורי."),
    P("שלוש הבדיקות עוברות, אז זו רדוקציה פולינומית.", hold=0.4),
], stage=f'<div id="u-g" class="h">{GU}</div>',
   panel=st.card("u-c0", "plain", "$UCLIQUE$: קליקה בגודל $k$ + קודקוד מחובר לכולם")
         + st.card("u-c1", "rule", "🔑 $\\langle G, k \\rangle \\mapsto \\langle G + u, k + 1 \\rangle$")
         + st.card("u-c2", "ex", "1️⃣ פולינומית ✓")
         + st.card("u-c3", "ex", "2️⃣ קליקה בגודל $k$ ← עם $u$, גודל $k + 1$ ✓")
         + st.card("u-c4", "ex", "3️⃣ קליקה בגודל $k + 1$ ← מוחקים קודקוד ✓"))

broken = Scene("broken", "איפה זה נשבר", [
    P("ועכשיו, איך רדוקציות נשברות. שתי דרכים חוזרות.", do=show("b-1")),
    P("הראשונה: $f$ שבודקת קודם אם יש פתרון. נגיד, רדוקציה מ-$HAMPATH$ אל $CLIQUE$:", do=show("b-c1"),
      say="הראשונה: אֶף שבודקת קודם אם יש פתרון. נגיד, רדוקציה מהָאם פַּאת' אל קְלִיק:"),
    P("אם בגרף יש מסלול המילטון, פולטים קלט קבוע של ״כן״, צלע אחת ו-$k$ שתיים. ואחרת, קלט קבוע של ״לא״.", do=show("b-2"),
      say="אם בגרף יש מסלול המילטון, פולטים קלט קבוע של כן, צלע אחת וקֵיי שתיים. ואחרת, קלט קבוע של לא."),
    P("שני הכיוונים נכונים. אבל כדי לחשב את $f$ צריך להכריע את $HAMPATH$, וזה לא פולינומי, אלא אם $P = NP$.", do=show("b-c2"),
      say="שני הכיוונים נכונים. אבל כדי לחשב את אֶף צריך להכריע את הָאם פַּאת', וזה לא פולינומי, אלא אם פִּי שווה אֶן פִּי."),
    P("השנייה: כיוון אחד עובד, והשני נופל. בדרך כלל הכיוון השלילי.", do=show("b-c3")),
    P("זה קורה כששפת המקור דורשת תנאי נוסף, ו-$f$ פשוט שוכחת אותו. בואו נראה את זה בשאלה אמיתית.", hold=0.4,
      say="זה קורה כששפת המקור דורשת תנאי נוסף, ואֶף פשוט שוכחת אותו. בואו נראה את זה בשאלה אמיתית."),
], stage='<div class="stack" style="gap:30px"><div id="b-1" class="bigmath h">$f$ ?</div>'
         '<div id="b-2" class="bigmath h" style="font-size:38px">$f(G) = \\langle K_2, 2 \\rangle$ או $\\langle K_1, 2 \\rangle$</div></div>',
   panel=st.card("b-c1", "trap", "⚠️ ״אם יש פתרון, פלט קבוע של כן״: $f$ מכריעה את המקור")
         + st.card("b-c2", "plain", "נופלת בדיקה 1️⃣: לא פולינומית, אלא אם $P = NP$")
         + st.card("b-c3", "trap", "⚠️ כיוון אחד עובד והשני נופל: בדיקה 3️⃣"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: השפה היא גרפים שבהם **כל** קודקוד בדרגה שלוש לכל היותר, ויש קליקה בגודל $k$.",
      say="שאלה ממבחן: השפה היא גרפים שבהם כל קודקוד בדרגה שלוש לכל היותר, ויש קליקה בגודל קֵיי."),
    P("ומציעים רדוקציה ממנה אל $CLIQUE$: פונקציית הזהות. האם זו רדוקציה פולינומית?",
      say="ומציעים רדוקציה ממנה אל קְלִיק: פונקציית הזהות. האם זו רדוקציה פולינומית?"),
    P("בדיקה ראשונה: הזהות מחושבת מיד. אז היא ניתנת לחישוב, ובזמן פולינומי.", do=show("q-x-a", "q-x-c")),
    P("בדיקה שנייה: אם יש קליקה והדרגות קטנות, יש קליקה. עובר."),
    P("בדיקה שלישית: הגרף הזה. יש בו קליקה בגודל ארבע.", do=show("x-g") + show(*g.hv("gx", "1", "2", "3", "4"))),
    P("אבל קודקוד אחת מחובר לארבעה קודקודים. הדרגה שלו ארבע.", say="אבל קודקוד מספר אחת מחובר לארבעה קודקודים. הדרגה שלו ארבע.", do=show(g.heid("gx", "1", "5", V), *g.hv("gx", "5"))),
    P("אז הקלט **לא** בשפת המקור, והפלט, אותו גרף, **כן** ב-$CLIQUE$. הכיוון השלילי נופל.", do=show("q-ok-d", "x-c2"),
      say="אז הקלט לא בשפת המקור, והפלט, אותו גרף, כן בקְלִיק. הכיוון השלילי נופל."),
    P("ולכן ״כן״ נופלת. ושימו לב לתיקון: אם יש דרגה גדולה משלוש, מוציאים קלט קבוע שאינו בשפה.", do=show("q-x-b", "x-c3"), hold=0.6),
], stage=f'<div class="stack" style="gap:18px"><div id="x-g" class="h">{GX}</div>'
         + st.card("x-c2", "trap", "⚠️ $x \\notin CLIQUE_{3D}$ אבל $f(x) \\in CLIQUE$")
         + st.card("x-c3", "rule", "🔑 תיקון: דרגה גדולה מ-$3$ ← קלט קבוע שאינו ב-$CLIQUE$") + '</div>',
   panel=f'<div class="qstem" style="font-size:30px"><span class="qid">{Q["id"]}</span>$CLIQUE_{{3D}}$: כל הדרגות '
         'לכל היותר 3, ויש קליקה בגודל $k$. האם $f_1(\\langle G, k \\rangle) = \\langle G, k \\rangle$ היא רדוקציה '
         'פולינומית אל $CLIQUE$?</div>'
         + '<div class="optsm">' + st.options("q", OPTS) + '</div>')

recap = Scene("recap", "סיכום", [
    P("לסיכום: לכל $f$ שלוש בדיקות. פולינומית, כיוון חיובי, וכיוון שלילי.", do=show("r-1"),
      say="לסיכום: לכל אֶף שלוש בדיקות. פולינומית, כיוון חיובי, וכיוון שלילי."),
    P("גאדג'ט טוב מוסיף משהו שלא משנה את התשובה, כמו קודקוד שמחובר לכולם.", do=show("r-2")),
    P("$f$ שצריכה למצוא קליקה אינה פולינומית, אלא אם $P = NP$.", do=show("r-3"),
      say="אֶף שצריכה למצוא קליקה אינה פולינומית, אלא אם פִּי שווה אֶן פִּי."),
    P("ותנאי נוסף בשפת המקור שובר בדרך כלל את הכיוון השלילי. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$x \\in A \\iff f(x) \\in B$</div></div>',
   panel=st.card("r-1", "rule", "🔑 פולינומית · ״כן״ ← ״כן״ · ״לא״ ← ״לא״")
         + st.card("r-2", "rule", "🔑 גאדג'ט שלא משנה את התשובה")
         + st.card("r-3", "trap", "⚠️ $f$ שמוצאת קליקה: לא פולינומית, אלא אם $P = NP$")
         + st.card("r-4", "trap", "⚠️ תנאי נוסף במקור ← בודקים את הכיוון השלילי"))

VIDEO = Video("N06", "np", "בונים ושוברים רדוקציות פולינומיות", [title, checks, gadget, broken, exam, recap],
              bank={"26B-B-Q15": "d"})
