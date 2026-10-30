# -*- coding: utf-8 -*-
"""M01 · מהי רדוקציית מיפוי — video script (build: tools/video/vid.py M01).

Source: tools/courses_src/map/M01.js (lesson + goal). Exam anchor: 23B-A-Q25 (a "step count or -1" function is not
computable), which no guided quiz uses. Not used on purpose: the five original quiz questions of M01 (their languages
and functions are not shown) and 23S-A-Q25 (the M01 quiz).
Both bridge pictures come from w_map.bridge_from(), and each function is brute-forced on every word up to length 10
exactly like the course checker (tools/verify/needhelp/map/check.py, kind brute-fn).
"""
from vid import P, Scene, Video, show, hide, BANK
from common import words
import stage as st
import w_map

W = words(10)


def brute(A, B, f):
    """-> (fail1, fail2) as in map/check.py: x in A with f(x) not in B / x not in A with f(x) in B"""
    return any(A(x) and not B(f(x)) for x in W), any((not A(x)) and B(f(x)) for x in W)


# ---------------------------------------------------------------- example 1: a real reduction
A1 = lambda x: x.count("1") % 2 == 0          # an even number of 1s
B1 = lambda y: y.count("1") % 2 == 1          # an odd number of 1s
f1 = lambda x: "1" + x                        # write 1 in front
assert brute(A1, B1, f1) == (False, False)
X1 = ["0", "11", "1", "10"]
G1, I1 = w_map.bridge_from("g1", X1, A1, B1, f1)
assert [I1[x][0] for x in X1] == [True, True, False, False] and all(I1[x][3] == "ok" for x in X1)
assert [I1[x][1] for x in X1] == ["10", "111", "11", "110"]

# ---------------------------------------------------------------- example 2: the negative direction breaks
A2 = lambda x: len(x) % 2 == 0                # even length
B2 = lambda y: y.endswith("0")                # ends with 0
f2 = lambda x: x + "0"                        # write 0 at the end
assert brute(A2, B2, f2) == (False, True)     # positive direction fine, negative direction fails
X2 = ["01", "1", "110"]
G2, I2 = w_map.bridge_from("g2", X2, A2, B2, f2)
assert [I2[x][3] for x in X2] == ["ok", "bad", "bad"]

# exam 23B-A-Q25
Q = BANK["23B-A-Q25"]
assert Q["correctId"] == "a"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]


def run(pfx, xs, info, lines):
    """one phrase per word: the dot on the left, its image on the right, the arrow"""
    ph, shown = [], set()
    for x, (sub, say) in zip(xs, lines):
        a, y, b, kind = info[x]
        lk, rk = x or "e", y or "e"
        do = show(f"{pfx}-L-{lk}", f"{pfx}-a-{lk}")
        if rk not in shown:
            do += show(f"{pfx}-R-{rk}")
            shown.add(rk)
        ph.append(P(sub, say=say, do=do))
    return ph


# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר את הכלי המרכזי של הקורס: רדוקציית מיפוי."),
    P("נראה מה צריך לבדוק כדי לדעת שפונקציה היא רדוקציה, ואיך מפילים רדוקציה שבורה.", hold=0.4),
], stage='<div class="kicker">M01 · רדוקציות מיפוי</div><h1>מהי רדוקציית מיפוי</h1>'
         '<p>להגדיר רדוקציה $A \\le_m B$ ולבדוק אותה: פונקציה שניתנת לחישוב, ושימור התשובה בשני הכיוונים.</p>',
   layout="title")

idea = Scene("idea", "הרעיון", [
    P("רדוקציה היא **מתרגם**. יש לנו שאלה על $A$, ואנחנו הופכים אותה לשאלה על $B$.", do=show("i-1")),
    P("לוקחים מילה $x$, ומחשבים ממנה מילה חדשה, $f(x)$.", do=show("i-2")),
    P("ואז, במקום לשאול אם $x$ שייכת ל-$A$, שואלים אם $f(x)$ שייכת ל-$B$.", do=show("i-c1")),
    P("כדי שהתרגום יהיה הוגן, התשובה צריכה להישאר אותה תשובה: כן הופך לכן, ולא הופך ללא.", do=show("i-c2"), hold=0.4),
    P("ככה כותבים את זה: $A \\le_m B$. האות $m$ היא מהמילה mapping, מיפוי.", do=show("i-3"),
      say="ככה כותבים את זה: אֵיי ניתנת לרדוקציה אל בִּי. האות אֶם היא מהמילה מֶאפִּינְג, מיפוי."),
], stage='<div class="stack">'
         '<div id="i-1" class="bigmath h">$x \\ \\in\\ ?\\ A$</div>'
         '<div id="i-2" class="bigmath h">$x \\ \\longmapsto\\ f(x)$</div>'
         '<div id="i-3" class="bigmath h">$A \\le_m B$</div></div>',
   panel=st.card("i-c1", "ex", "שאלה על $A$ ← שאלה על $B$")
         + st.card("i-c2", "rule", "🔑 כן ← כן, לא ← לא"))

defs = Scene("def", "ההגדרה", [
    P("פורמלית, $f$ היא רדוקציה מ-$A$ ל-$B$ אם מתקיימים שני תנאים.", do=show("d-m")),
    P("תנאי ראשון: $f$ **ניתנת לחישוב**. יש מכונה שעוצרת על כל קלט, ומשאירה את $f(x)$ על הסרט.", do=show("d-0")),
    P("תנאי שני: לכל $x$, $x$ שייכת ל-$A$ אם ורק אם $f(x)$ שייכת ל-$B$.", do=show("d-iff")),
    P("את ה״אם ורק אם״ בודקים כשני כיוונים נפרדים.", hold=0.2),
    P("הכיוון החיובי: אם $x$ ב-$A$, אז $f(x)$ חייבת לנחות בתוך $B$.", do=show("d-1")),
    P("והכיוון השלילי: אם $x$ לא ב-$A$, אז $f(x)$ חייבת לנחות מחוץ ל-$B$.", do=show("d-2")),
    P("כדי להפיל רדוקציה מספיקה **דוגמה אחת** שנכשלת באחד הכיוונים.", do=show("d-r1")),
    P("וכדי לאשר רדוקציה צריך לנמק את שני הכיוונים, ואת החישוביות.", do=show("d-r2"), hold=0.4),
], stage='<div class="stack"><div id="d-m" class="bigmath h">$f : \\Sigma^* \\to \\Sigma^*$</div>'
         '<div id="d-iff" class="bigmath h">$x \\in A \\iff f(x) \\in B$</div>'
         + st.card("d-r1", "rule", "🔑 להפריך: <b>דוגמה אחת</b> לכיוון שנכשל")
         + st.card("d-r2", "rule", "🔑 לאשר: שני הכיוונים + חישוביות") + "</div>",
   panel=st.card("d-0", "ex", "<b>1. חישוביות:</b> מכונה שעוצרת על <b>כל</b> קלט וכותבת את $f(x)$")
         + st.card("d-1", "plain", "<b>2א. כיוון חיובי:</b> $x \\in A \\Rightarrow f(x) \\in B$")
         + st.card("d-2", "plain", "<b>2ב. כיוון שלילי:</b> $x \\notin A \\Rightarrow f(x) \\notin B$"))

good = Scene("good", "דוגמה: רדוקציה", [
    P("דוגמה. $A$: המילים עם מספר **זוגי** של אחדות. $B$: המילים עם מספר **אי-זוגי** של אחדות.", do=show("g-c1", "g-c2")),
    P("והפונקציה: כותבים 1 בתחילת המילה.", do=show("g-c3")),
    *run("g1", X1, I1, [
        ("$0$: אין בה אחדות, וזה זוגי. התרגום, $10$, עם 1 יחיד: אי-זוגי. נחת בתוך $B$.",
         "אפס: אין בה אחדות, וזה זוגי. התרגום, אחת אפס, עם אחד בודד: אי זוגי. נחת בתוך בִּי."),
        ("$11$: שתי אחדות. הופכת ל-$111$, שלוש אחדות. שוב בתוך $B$.",
         "אחת אחת: שתי אחדות. הופכת לאחת אחת אחת, שלוש אחדות. שוב בתוך בִּי."),
        ("ועכשיו מילים מחוץ ל-$A$. $1$: 1 יחיד. הופכת ל-$11$, שתי אחדות, מחוץ ל-$B$.",
         "ועכשיו מילים מחוץ לאֵיי. אחת: אחד בודד. הופכת לאחת אחת, שתי אחדות, מחוץ לבִּי."),
        ("$10$: גם היא מחוץ ל-$A$, ו-$110$ נוחתת מחוץ ל-$B$.",
         "אחת אפס: גם היא מחוץ לאֵיי, ואחת אחת אפס נוחתת מחוץ לבִּי."),
    ]),
    P("וזה לא מקרה: האחד הנוסף הופך כל זוגי לאי-זוגי, וכל אי-זוגי לזוגי.", do=show("g-c4")),
    P("שני הכיוונים מתקיימים, ולהוסיף תו בהתחלה זו פעולה חשיבה. זו רדוקציה.", do=show("g-v"), hold=0.5),
], stage=G1,
   panel=st.card("g-c1", "plain", "$A$: מספר <b>זוגי</b> של 1")
         + st.card("g-c2", "plain", "$B$: מספר <b>אי-זוגי</b> של 1")
         + st.card("g-c3", "ex", "$f(x) = 1x$")
         + st.card("g-c4", "rule", "🔑 עוד 1 אחד הופך את הזוגיות")
         + '<div id="g-v" class="verdict ok h">רדוקציה ✓</div>')

bad = Scene("bad", "דוגמה: רדוקציה שבורה", [
    P("עכשיו פונקציה שנראית טוב ונופלת. $A$: המילים באורך זוגי. $B$: המילים שמסתיימות ב-0.", do=show("b-c1", "b-c2")),
    P("והפונקציה: כותבים 0 בסוף המילה.", do=show("b-c3")),
    *run("g2", X2, I2, [
        ("$01$ באורך זוגי. הופכת ל-$010$, שמסתיימת ב-0. הכיוון החיובי עובד, ותמיד יעבוד.",
         "אפס אחת באורך זוגי. הופכת לאפס אחת אפס, שמסתיימת באפס. הכיוון החיובי עובד, ותמיד יעבוד."),
        ("אבל $1$ באורך אי-זוגי, מחוץ ל-$A$. והתרגום, $10$, מסתיים ב-0: הוא **בתוך** $B$.",
         "אבל אחת באורך אי זוגי, מחוץ לאֵיי. והתרגום, אחת אפס, מסתיים באפס: הוא בתוך בִּי."),
        ("וגם $110$: מחוץ ל-$A$, ונוחתת בתוך $B$.",
         "וגם אחת אחת אפס: מחוץ לאֵיי, ונוחתת בתוך בִּי."),
    ]),
    P("הפונקציה שולחת **כל** מילה לתוך $B$. תשובת ״לא״ הופכת ל״כן״.", do=show("b-c4")),
    P("הכיוון השלילי נכשל, ודוגמה אחת מספיקה: זו לא רדוקציה.", do=show("b-v"), hold=0.5),
], stage=G2,
   panel=st.card("b-c1", "plain", "$A$: אורך <b>זוגי</b>")
         + st.card("b-c2", "plain", "$B$: מסתיימות ב-0")
         + st.card("b-c3", "ex", "$f(x) = x0$")
         + st.card("b-c4", "trap", "⚠️ הכיוון השלילי: $x \\notin A$ אבל $f(x) \\in B$")
         + '<div id="b-v" class="verdict bad h">לא רדוקציה ✗</div>')

comp = Scene("comp", "חישוביות", [
    P("ועכשיו התנאי הראשון, שקל לשכוח: $f$ צריכה להיות ניתנת לחישוב."),
    P("למה זה חשוב? כי בלי התנאי הזה יש רדוקציה טריוויאלית מכל שפה.", do=show("c-1")),
    P("פשוט מחליטים: אם $x$ ב-$A$, מחזירים מילה שבתוך $B$. אחרת, מילה שמחוץ ל-$B$.", do=show("c-2")),
    P("אבל פונקציה כזו **פותרת** את $A$ בעצמה. כש-$A$ לא כריעה, אי אפשר לחשב אותה.", do=show("c-3")),
    P("הרדוקציה רק מתרגמת. היא לא עונה על השאלה.", do=show("c-r"), hold=0.5),
], stage='<div class="stack">'
         + w_map.code("c", ["f(x):", "  if x ∈ A:  return y_in", "  else:      return y_out"])
         .replace('class="codebox"', 'class="codebox h"').replace('id="c"', 'id="c-1"')
         + "</div>",
   panel=st.card("c-2", "ex", "מחזירה מילה קבועה בתוך $B$ או מחוצה לה")
         + st.card("c-3", "trap", "⚠️ זו כבר הכרעה של $A$, לא תרגום")
         + st.card("c-r", "rule", "🔑 $f$ מתרגמת, לא פותרת"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן. פונקציה מקבלת מכונה $M$ ומילה $w$."),
    P("אם $M$ עוצרת על $w$ אחרי $k$ צעדים, היא מחזירה את $k$. ואם $M$ לא עוצרת, היא מחזירה מינוס אחד.",
      do=show("x-1"), say="אם אֵם עוצרת על דַּאבְּלְיוּ אחרי קֵיי צעדים, היא מחזירה את קֵיי. ואם אֵם לא עוצרת, היא מחזירה מינוס אחד."),
    P("האם אפשר לחשב אותה?"),
    P("הרעיון הראשון: מריצים את $M$ על $w$ וסופרים צעדים.", do=show("x-hl1")),
    P("אם $M$ עוצרת, זה עובד. אבל אם היא לא עוצרת, הספירה לא נגמרת, ולעולם לא נחזיר מינוס אחד.", do=hide("x-hl1") + show("x-hl3")),
    P("ובאופן כללי: מתוך התשובה של הפונקציה יודעים אם $M$ עוצרת על $w$. זו בעיית העצירה.", do=hide("x-hl3")),
    P("ולכן הפונקציה לא ניתנת לחישוב.", do=show("q-ok-a"), hold=0.3),
    P("וכל שאר האפשרויות אומרות שהיא כן ניתנת לחישוב, לפעמים או תמיד.", do=show("q-x-b", "q-x-c")),
    P("ומה עם הטענה שתלויה בשפה של $M$? גם מכונה של שפה כריעה יכולה להיתקע בלולאה על $w$.",
      do=show("q-x-d", "q-n-d")),
    P("המלכודת: נדמה שכתבנו אלגוריתם. אבל אלגוריתם שלא עוצר על כל קלט לא מחשב פונקציה.", do=show("x-t"), hold=0.6),
], stage='<div class="stack">'
         + w_map.code("x", ["f(⟨M⟩, w):", "  run M on w, count steps", "  halts after k steps → return k",
                            "  never halts → return −1  ✗"]).replace('class="codebox"', 'class="codebox h"')
         .replace('id="x"', 'id="x-1"')
         + st.card("x-t", "trap", "⚠️ ״להריץ ולספור״ לא עוצר כש-$M$ לא עוצרת")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$f$ מחזירה את מספר הצעדים עד ש-$M$ עוצרת על $w$, '
         'או $-1$ אם היא לא עוצרת. מה נכון?</div>'
         + st.options("q", OPTS, notes={"d": "לא תלוי בשפה"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $A \\le_m B$ אם יש פונקציה ניתנת לחישוב שמתרגמת מילים מ-$A$ למילים ב-$B$.", do=show("r-1")),
    P("ושומרת את התשובה בשני הכיוונים: כן הופך לכן, ולא הופך ללא.", do=show("r-2")),
    P("כדי להפיל רדוקציה מספיקה דוגמה אחת, ובדרך כלל היא מסתתרת בכיוון השלילי.", do=show("r-3")),
    P("והפונקציה רק מתרגמת: היא לא פותרת את הבעיה. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$x \\in A \\iff f(x) \\in B$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $f$ חשיבה על <b>כל</b> קלט")
         + st.card("r-2", "rule", "🔑 שני כיוונים: כן ← כן, לא ← לא")
         + st.card("r-3", "trap", "⚠️ דוגמה אחת מפילה")
         + st.card("r-4", "trap", "⚠️ $f$ מתרגמת, לא פותרת"))

VIDEO = Video("M01", "map", "מהי רדוקציית מיפוי", [title, idea, defs, good, bad, comp, exam, recap],
              bank={"23B-A-Q25": "a"})
