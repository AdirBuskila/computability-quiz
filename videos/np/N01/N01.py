# -*- coding: utf-8 -*-
"""N01 · זמן ריצה והמחלקה P — video script (build: tools/video/vid.py N01).

Source: tools/courses_src/np/N01.js (lesson + goal). Exam anchor: 24A-B-Q2 (SMALL_SAT: a CNF formula with a satisfying
assignment in which exactly 10 variables are TRUE), which no guided quiz uses (vid.py refuses quiz ids).
Not used on purpose: the quiz questions of N01 (22A-B-Q14 and the five original ones: 3 tapes O(n^5), C(20,3),
binary k, vertex cover of size 3, the 2^|x| machine). The constant-parameter example here is a 4-clique, the
encoding example is the unary simulation of the lesson (20A-B-Q25 family), not the quiz's binary counter.
"""
import math
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_np as g

# ---------------------------------------------------------------- facts (verified)
# models: k tapes -> one tape squares the bound; 4 tapes O(n^3) -> one tape O(n^6)
assert (3 * 2) == 6
# a constant parameter: clique of size 4 by brute force over all 4-subsets
V = ["1", "2", "3", "4", "5", "6"]
E = g.E_(("1", "2"), ("1", "3"), ("1", "4"), ("2", "3"), ("2", "4"), ("3", "4"), ("4", "5"), ("5", "6"), ("3", "6"))
assert math.comb(6, 4) == 15 and g.has(V, E, 4, g.is_clique) and not g.has(V, E, 5, g.is_clique)
K4 = ["1", "2", "3", "4"]
assert g.is_clique(E, K4)
BAD = ["1", "2", "4", "5"]                     # a 4-subset that is not a clique (missing 1-5)
assert not g.is_clique(E, BAD)
for n in range(4, 60):
    assert math.comb(n, 4) <= n ** 4
# the parameter that grows: C(n, n/2) is not polynomial (>= 2^(n/2) from n = 2)
for n in range(2, 60, 2):
    assert math.comb(n, n // 2) >= 2 ** (n // 2)
# encoding: k = 1000 in binary is 10 characters, in unary 1000
assert len(bin(1000)[2:]) == 10 and bin(1000)[2:] == "1111101000"
# exam 24A-B-Q2: choose 10 of at most n variables, each check O(n)
Q = BANK["24A-B-Q2"]
assert Q["correctId"] == "a" and "SMALL" in Q["options"][0]["value"]
OPTS = [(o["id"], f'${o["value"]}$' if o["type"] == "math" else o["value"]) for o in Q["options"]]
for n in range(10, 80):
    assert math.comb(n, 10) * n <= n ** 11

POS = {"1": (170, 120), "2": (430, 90), "3": (430, 330), "4": (170, 350), "5": (640, 470), "6": (700, 200)}
GR = g.graph_svg("cg", V, E, POS, w=820, h=540, scale=0.95)


def clique_on(S):
    return g.hv("cg", *S) + [g.heid("cg", a, b, V) for a, b in __import__("itertools").combinations(S, 2)
                             if frozenset((a, b)) in E]


# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("עד עכשיו שאלנו אם אפשר להכריע שפה. מעכשיו נשאל כמה זמן זה לוקח."),
    P("נגדיר זמן ריצה ואת המחלקה $P$, ונראה מה עולה מעבר בין מודלים."),
    P("ונלמד שני כלים שחוזרים במבחנים: פרמטר קבוע, וקידוד של מספרים.", hold=0.4),
], stage='<div class="kicker">N01 · P, NP ו-NP-שלמות</div><h1>זמן ריצה והמחלקה P</h1>'
         '<p>למדוד זמן ריצה, לדעת מה עולה מעבר בין מודלים, ולזהות מתי שפה היא ב-$P$: '
         'גם כשהפרמטר קבוע וגם עם קידוד אונארי.</p>', layout="title")

idea = Scene("idea", "זמן ריצה", [
    P("זמן הריצה $t(n)$ הוא מספר הצעדים של המכונה על קלט באורך $n$.", do=show("i-1")),
    P("ולוקחים את המקרה **הגרוע**: הקלט הכי איטי מבין כל הקלטים באורך הזה.", do=show("i-c1")),
    P("$P$ היא כל השפות שמכונה **דטרמיניסטית** מכריעה בזמן $O(n^k)$, עבור $k$ קבוע.", do=show("i-2")),
    P("המעריך יכול להיות גדול, נגיד מאה. כל עוד הוא לא תלוי בקלט, זה פולינום.", do=show("i-c2"), hold=0.4),
    P("ושימו לב: $L \\notin P$ היא טענה על **כל** המכונות, לא על מכונה אחת איטית.", do=show("i-c3"),
      say="ושימו לב: אֵל לא שייכת לפִּי היא טענה על כל המכונות, לא על מכונה אחת איטית."),
], stage='<div class="stack"><div id="i-1" class="big h">$t(n)$</div>'
         '<div id="i-2" class="bigmath h">$P = \\{ L \\mid L \\text{ decided in } O(n^k) \\}$</div></div>',
   panel=st.card("i-c1", "plain", "המקרה הגרוע על קלטים באורך $n$")
         + st.card("i-c2", "rule", "🔑 $k$ קבוע: $n^2$, $n^{10}$, $n^{100}$ כולם פולינום")
         + st.card("i-c3", "trap", "⚠️ מכונה איטית אחת לא מוכיחה $L \\notin P$"))

ROWS = '<table class="npt" dir="rtl"><thead><tr><th>מעבר</th><th>הזמן</th></tr></thead><tbody>' \
       '<tr id="m-r1" class="h"><td>$k$ סרטים ← סרט אחד</td><td>$t(n) \\to O(t(n)^2)$</td></tr>' \
       '<tr id="m-r2" class="h"><td>אי-דטרמיניסטית ← דטרמיניסטית</td><td>$t(n) \\to 2^{O(t(n))}$</td></tr>' \
       '</tbody></table>'
models = Scene("models", "מעבר בין מודלים", [
    P("מה קורה לזמן כשמחליפים מודל? שני מעברים חשובים.", do=show("m-t")),
    P("הראשון: מכונה עם כמה סרטים הופכת למכונה עם סרט אחד, והזמן עולה **בריבוע**.", do=show("m-r1"),
      say="הראשון: מכונה עם כמה סרטים הופכת למכונה עם סרט אחד, והזמן עולה בריבוע."),
    P("למשל, ארבעה סרטים בזמן $O(n^3)$ נותנים סרט אחד בזמן $O(n^6)$.", do=show("m-c1")),
    P("ריבוע של פולינום הוא פולינום. לכן $P$ לא תלויה במספר הסרטים.", do=show("m-c2"), hold=0.4,
      say="ריבוע של פולינום הוא פולינום. לכן פִּי לא תלויה במספר הסרטים."),
    P("השני: מכונה אי-דטרמיניסטית הופכת לדטרמיניסטית, והזמן הופך **לאקספוננט**.", do=show("m-r2")),
    P("הסימולציה עוברת על כל הענפים של עץ החישוב, ויש מהם מספר אקספוננציאלי.", do=show("m-c3")),
    P("כאן בדיוק נמצא הפער בין $P$ ל-$NP$, שנפגוש ברמה הבאה.", hold=0.5),
], stage=f'<div class="stack"><div id="m-t" class="h">{ROWS}</div></div>',
   panel=st.card("m-c1", "ex", "$4$ סרטים, $O(n^3)$ ← סרט אחד, $O(n^6)$")
         + st.card("m-c2", "rule", "🔑 $P$ לא תלויה במספר הסרטים")
         + st.card("m-c3", "trap", "⚠️ אי-דטרמיניזם ← דטרמיניזם: פולינום הופך לאקספוננט"))

const = Scene("const", "פרמטר קבוע", [
    P("עכשיו כלי שחוזר המון: שפה שבה הגודל המבוקש הוא **קבוע**.", do=show("c-g")),
    P("נגיד: גרפים שיש בהם קליקה בגודל ארבע. ארבעה קודקודים שכולם מחוברים זה לזה."),
    P("האלגוריתם הכי פשוט: לעבור על כל רביעייה של קודקודים, ולבדוק אם היא קליקה.", do=show("c-c1")),
    P("הרביעייה הזו נכשלת: אין צלע בין אחת לחמש.", do=show(*g.hv("cg", *BAD)), say="הרביעייה הזו נכשלת: אין צלע בין אחת לחמש."),
    P("והרביעייה הזו מצליחה: כל שש הצלעות ביניהן קיימות.", do=hide(*g.hv("cg", *BAD)) + show(*clique_on(K4))),
    P("כמה רביעיות יש? בגרף עם $n$ קודקודים, פחות מ-$n^4$.", do=show("c-c2")),
    P("וכל בדיקה זולה. סך הכל זמן פולינומי, ולכן השפה ב-$P$.", do=show("c-c3"), hold=0.4),
    P("אבל אם הגודל המבוקש הוא חצי ממספר הקודקודים, הוא **גדל** עם הקלט.", do=show("c-c4")),
    P("והשפה הזו $NP$-שלמה: מוכיחים את זה ברדוקציה מ-$CLIQUE$. חיפוש ממצה כבר לא עוזר כאן.", hold=0.4,
      say="והשפה הזו אֶן פִּי שלמה: מוכיחים את זה ברדוקציה מקְלִיק. חיפוש ממצה כבר לא עוזר כאן."),
], stage=f'<div id="c-g" class="h">{GR}</div>',
   panel=st.card("c-c1", "ex", "קליקה בגודל $4$: עוברים על כל הרביעיות")
         + st.card("c-c2", "plain", "מספר הרביעיות: לכל היותר $n^4$")
         + st.card("c-c3", "rule", "🔑 גודל קבוע בהגדרת השפה ← חיפוש ממצה פולינומי ← $P$")
         + st.card("c-c4", "trap", "⚠️ גודל $\\lfloor n/2 \\rfloor$ גדל עם הקלט: $NP$-שלמה, ברדוקציה מ-$CLIQUE$"))

enc = Scene("enc", "קידוד", [
    P("הכלי השני: זמן נמדד ביחס **לאורך הקידוד** של הקלט, לא לערך של המספרים בו.", do=show("e-1")),
    P("המספר אלף בבינארי הוא עשרה תווים בלבד.", do=show("e-2")),
    P("כלומר הערך של מספר גדל אקספוננציאלית באורך הכתיבה שלו. ריצה לפי הערך איננה ריצה פולינומית.", do=show("e-c1")),
    P("ובאונארי, אלף כתוב כאלף אחדות. כאן אלף צעדים זה רק ליניארי באורך הקלט.", do=show("e-3", "e-c2")),
    P("לכן סימולציה של $M$ על $x$ למשך $k$ צעדים, כש-$k$ נתון באונארי, היא חישוב פולינומי.", do=show("e-c3"), hold=0.5,
      say="לכן סימולציה של אֵם על אִקְס למשך קֵיי צעדים, כשקֵיי נתון באונארי, היא חישוב פולינומי."),
], stage='<div class="stack">'
         '<div id="e-1" class="bigmath h">$k = 1000$</div>'
         '<div id="e-2" class="card ex h" style="font-size:36px">בינארי: <span dir="ltr">1111101000</span> · 10 תווים</div>'
         '<div id="e-3" class="card ex h" style="font-size:36px">אונארי: <span dir="ltr">111…1</span> · 1000 תווים</div>'
         '</div>',
   panel=st.card("e-c1", "trap", "⚠️ ערך המספר גדול אקספוננציאלית מאורך הקידוד הבינארי שלו")
         + st.card("e-c2", "plain", "$1^k$ באונארי: האורך הוא $k$ עצמו")
         + st.card("e-c3", "rule", "🔑 $\\langle M, x, 1^k \\rangle$: לסמלץ $k$ צעדים זה פולינומי"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: נוסחת CNF שיש לה השמה מספקת עם **בדיוק עשרה** משתנים אמת. לאיזו מחלקה השפה שייכת?",
      say="שאלה ממבחן: נוסחת סי אן אף שיש לה השמה מספקת עם בדיוק עשרה משתנים אמת. לאיזו מחלקה השפה שייכת?"),
    P("זה נראה כמו $SAT$, ולכן מתפתה לענות $NP$-שלמה. אבל המספר עשר **קבוע**.", do=show("x-1")),
    P("בנוסחה באורך $n$ יש לכל היותר $n$ משתנים. בוחרים עשרה מהם שיהיו אמת, ואת כל השאר שקר.", do=show("x-2")),
    P("יש פחות מ-$n$ בחזקת עשר בחירות כאלה, וכל בחירה נבדקת בסריקה אחת של הנוסחה.", do=show("x-3"),
      say="יש פחות מאֶן בחזקת עשר בחירות כאלה, וכל בחירה נבדקת בסריקה אחת של הנוסחה."),
    P("סך הכל זמן פולינומי, ולכן השפה ב-$P$.", do=show("q-ok-a"), hold=0.3),
    P("״לא ב-$NP$״ נופלת מיד: כל שפה ב-$P$ היא גם ב-$NP$.", do=show("q-x-c", "q-n-c"),
      say="לא באֶן פִּי נופלת מיד: כל שפה בפִּי היא גם באֶן פִּי."),
    P("ו-$NP$-שלמה לא נובע: שפה ב-$P$ היא $NP$-שלמה רק אם $P = NP$.", do=show("q-x-b", "q-n-b")),
    P("וכיוון שיש תשובה נכונה, גם ״אף אחת״ נופלת.", do=show("q-x-d"), hold=0.6,
      say="וכיוון שיש תשובה נכונה, גם אף אחת נופלת."),
], stage='<div class="stack">'
         '<div id="x-1" class="card trap h">⚠️ נראה כמו $SAT$, אבל $10$ קבוע</div>'
         '<div id="x-2" class="bigmath h" style="font-size:40px">$\\le n^{10}$ בחירות</div>'
         '<div id="x-3" class="bigmath h" style="font-size:40px">$n^{10} \\cdot O(n) = O(n^{11})$</div>'
         '</div>',
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>נוסחת CNF, וקיימת השמה מספקת עם <b>בדיוק 10</b> '
         'משתנים בערך TRUE. לאיזו מחלקה שייכת השפה?</div>'
         + st.options("q", OPTS, notes={"b": "רק אם P = NP", "c": "P ⊆ NP"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $P$ היא מה שמכונה דטרמיניסטית מכריעה בזמן פולינומי, במקרה הגרוע.", do=show("r-1")),
    P("כמה סרטים לסרט אחד: ריבוע. אי-דטרמיניסטית לדטרמיניסטית: אקספוננט.", do=show("r-2")),
    P("גודל קבוע בהגדרת השפה נותן חיפוש ממצה פולינומי.", do=show("r-3")),
    P("ומספר בבינארי שווה אקספוננציאלית יותר מאורכו. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="big">$P$</div><div class="bigmath">$O(n^k)$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $P$: דטרמיניסטית, $O(n^k)$, $k$ קבוע")
         + st.card("r-2", "rule", "🔑 סרטים: $t^2$ · אי-דטרמיניזם: $2^{O(t)}$")
         + st.card("r-3", "rule", "🔑 פרמטר קבוע ← $P$")
         + st.card("r-4", "trap", "⚠️ בינארי מול אונארי"))

VIDEO = Video("N01", "np", "זמן ריצה והמחלקה P", [title, idea, models, const, enc, exam, recap],
              bank={"24A-B-Q2": "a"})
