# -*- coding: utf-8 -*-
"""N03 · coNP, סגירות, ומה עדיין פתוח — video script (build: tools/video/vid.py N03).

Source: tools/courses_src/np/N03.js (lesson + goal). Exam anchor: 22B-A-Q4 ("if P = coNP then the complement of
CLIQUE is in NP"), which no guided quiz uses.
Not used on purpose: the quiz questions of N03 (20A-A-Q22, the A minus B difference, and the five original ones).
The difference rule (A in NP, B in P) is left to the quiz; the video proves the P = coNP collapse instead.
"""
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_np as g

# ---------------------------------------------------------------- facts (verified)
UNSAT = [(("x1", True), ("x2", True)), (("x1", False),), (("x2", False),)]
assert not g.satisfiable(UNSAT)
ALL = list(g.assignments(UNSAT))
assert len(ALL) == 4 and not any(g.satisfies(UNSAT, a) for a in ALL)
# which clause each assignment breaks (the first false clause), for the on-screen table
FAILS = []
for a in ALL:
    i = next(i for i, c in enumerate(UNSAT) if not any(g.lit_true(l, a) for l in c))
    FAILS.append((a, i))
assert [i for _, i in FAILS] == [0, 2, 1, 1]

Q = BANK["22B-A-Q4"]
assert Q["correctId"] == "a" and [o["id"] for o in Q["options"]] == ["a", "b", "c"]
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

F = g.cnf_row("u", UNSAT)
ROWS = "".join(
    f'<tr id="a-r{k}" class="h"><td>${g.assign_tex(a)}$</td><td>פסוקית {i + 1} נופלת</td></tr>' for k, (a, i) in enumerate(FAILS))
TAB = f'<table class="npt"><thead><tr><th>השמה</th><th>למה לא</th></tr></thead><tbody>{ROWS}</tbody></table>'

CL = '<table class="npt"><thead><tr><th>פעולה</th><th>$P$</th><th>$NP$</th></tr></thead><tbody>' \
     '<tr id="c-r1" class="h"><td>איחוד, חיתוך</td><td>✓</td><td>✓</td></tr>' \
     '<tr id="c-r2" class="h"><td>שרשור, כוכב</td><td>✓</td><td>✓</td></tr>' \
     '<tr id="c-r3" class="h"><td>משלים</td><td>✓</td><td>לא ידוע</td></tr></tbody></table>'

VENN = ('<svg class="npg" viewBox="0 0 900 470" width="860" height="450" direction="ltr">'
        '<ellipse cx="340" cy="235" rx="270" ry="190" class="vn a"/>'
        '<ellipse cx="560" cy="235" rx="270" ry="190" class="vn b"/>'
        '<text x="170" y="245" class="vl">NP</text><text x="730" y="245" class="vl">coNP</text>'
        '<g id="vn-p" class="h"><ellipse cx="450" cy="270" rx="78" ry="62" class="vn p"/>'
        '<text x="450" y="283" class="vl">P</text></g>'
        '<text id="vn-q" x="450" y="148" class="vl q h">?</text></svg>')

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר את $coNP$, נבדוק לאילו פעולות $P$ ו-$NP$ סגורות,"),
    P("ונעשה סדר במה שהוכח ובמה שעדיין פתוח. זה בדיוק מה ששאלות ״מה נכון״ בודקות.", hold=0.4),
], stage='<div class="kicker">N03 · P, NP ו-NP-שלמות</div><h1>coNP וסגירויות של P ו-NP</h1>'
         '<p>להגדיר $coNP$, לדעת לאילו פעולות $P$ ו-$NP$ סגורות, ולהבדיל בין מה שהוכח למה שפתוח.</p>', layout="title")

co = Scene("co", "coNP", [
    P("$coNP$ היא כל השפות שהמשלים שלהן ב-$NP$.", do=show("o-1"),
      say="קוֹ-אֶן-פִּי היא כל השפות שהמשלים שלהן באֶן פִּי."),
    P("ב-$NP$ עד קצר מוכיח שמילה **בשפה**. ב-$coNP$ עד קצר מוכיח שמילה **לא** בשפה.", do=show("o-c1"),
      say="באֶן פִּי עד קצר מוכיח שמילה בשפה. בקוֹ-אֶן-פִּי עד קצר מוכיח שמילה לא בשפה."),
    P("הדוגמה הקלאסית: המשלים של $SAT$, הנוסחאות שאין להן השמה מספקת.", do=show("o-f")),
    P("איך משכנעים שהנוסחה הזו לא ספיקה? צריך להראות שכל השמה נופלת.", do=show("o-t")),
    P("$x_1$ ו-$x_2$ שקר: הפסוקית הראשונה נופלת.", do=show("a-r0"),
      say="אִקְס אחת ואִקְס שתיים שקר: הפסוקית הראשונה נופלת."),
    P("ובכל שלוש ההשמות האחרות, אחת מהפסוקיות הקצרות נופלת.", do=show("a-r1", "a-r2", "a-r3")),
    P("כאן היו ארבע השמות. עם $n$ משתנים יש שתיים בחזקת $n$, ואין עד קצר ידוע לטענה הזו.", do=show("o-c2"), hold=0.4,
      say="כאן היו ארבע השמות. עם אֶן משתנים יש שתיים בחזקת אֶן, ואין עד קצר ידוע לטענה הזו."),
], stage=f'<div class="stack" style="gap:40px"><div id="o-1" class="bigmath h">$coNP = \\{{ L \\mid \\overline{{L}} \\in NP \\}}$</div>'
         f'<div id="o-f" class="h">{F}</div><div id="o-t" class="h">{TAB}</div></div>',
   panel=st.card("o-c1", "rule", "🔑 $NP$: עד ל״כן״ · $coNP$: עד ל״לא״")
         + st.card("o-c2", "trap", "⚠️ $\\overline{SAT} \\in coNP$, אבל לא ידוע אם $\\overline{SAT} \\in NP$"))

closure = Scene("closure", "סגירות", [
    P("לאילו פעולות $P$ ו-$NP$ סגורות?", do=show("c-t"), say="לאילו פעולות פִּי ואֶן פִּי סגורות?"),
    P("איחוד וחיתוך: שתיהן סגורות.", do=show("c-r1")),
    P("לאיחוד ב-$NP$: מריצים את המכונה הראשונה, ואם לא קיבלה, מריצים את השנייה. סך הכל פולינומי.", do=show("c-c1"),
      say="לאיחוד באֶן פִּי: מריצים את המכונה הראשונה, ואם לא קיבלה, מריצים את השנייה. סך הכל פולינומי."),
    P("שרשור וכוכב: גם כן. בשרשור, המכונה האי-דטרמיניסטית **מנחשת** איפה לחתוך את המילה.", do=show("c-r2", "c-c2")),
    P("ומשלים: $P$ סגורה, כי מחליפים קבלה ודחייה במכונה שתמיד עוצרת.", do=show("c-r3"),
      say="ומשלים: פִּי סגורה, כי מחליפים קבלה ודחייה במכונה שתמיד עוצרת."),
    P("אבל ב-$NP$ זה **לא ידוע**. החלפה כזו במכונה אי-דטרמיניסטית לא נותנת את המשלים.", do=show("c-c3"),
      say="אבל באֶן פִּי זה לא ידוע. החלפה כזו במכונה אי דטרמיניסטית לא נותנת את המשלים."),
    P("הטענה ש-$NP$ סגורה למשלים שקולה לשאלה הפתוחה אם $NP$ שווה ל-$coNP$.", hold=0.4,
      say="הטענה שאֶן פִּי סגורה למשלים שקולה לשאלה הפתוחה אם אֶן פִּי שווה לקוֹ-אֶן-פִּי."),
], stage=f'<div class="stack"><div id="c-t" class="h">{CL}</div></div>',
   panel=st.card("c-c1", "ex", "איחוד: $M_1$, ואם לא קיבלה, $M_2$")
         + st.card("c-c2", "ex", "שרשור: מנחשים נקודת חיתוך")
         + st.card("c-c3", "trap", "⚠️ במכונה אי-דטרמיניסטית, החלפת קבלה ודחייה לא נותנת את המשלים"))

known = Scene("known", "מה הוכח ומה פתוח", [
    P("עכשיו מפה של מה שידוע. $NP$ משמאל, $coNP$ מימין.", do=show("k-v"),
      say="עכשיו מפה של מה שידוע. אֶן פִּי משמאל, קוֹ-אֶן-פִּי מימין."),
    P("$P$ נמצאת בחיתוך שלהן: אם $L$ ב-$P$, גם המשלים ב-$P$, ולכן ב-$NP$.", do=show("vn-p", "k-c1"),
      say="פִּי נמצאת בחיתוך שלהן: אם אֵל בפִּי, גם המשלים בפִּי, ולכן באֶן פִּי."),
    P("ומה עוד יש בחיתוך? האם יש שם שפה שאינה ב-$P$? **לא ידוע**.", do=show("vn-q", "k-c2"),
      say="ומה עוד יש בחיתוך? האם יש שם שפה שאינה בפִּי? לא ידוע."),
    P("גם $P = NP$ פתוחה, וגם $NP = coNP$ פתוחה.", do=show("k-c4"),
      say="גם פִּי שווה אֶן פִּי פתוחה, וגם אֶן פִּי שווה קוֹ-אֶן-פִּי פתוחה."),
    P("קשר אחד כן הוכח: אם $P = NP$, אז $NP = coNP$, כי $P$ סגורה למשלים. ההפך לא ידוע.", do=show("k-c5"), hold=0.4,
      say="קשר אחד כן הוכח: אם פִּי שווה אֶן פִּי, אז אֶן פִּי שווה קוֹ-אֶן-פִּי, כי פִּי סגורה למשלים. ההפך לא ידוע."),
    P("ובשאלת ״מה נכון״, טענה שדורשת לפתור בעיה פתוחה היא טענה **שגויה**.", hold=0.5),
], stage=f'<div id="k-v" class="h">{VENN}</div>',
   panel=st.card("k-c1", "rule", "🔑 $P \\subseteq NP \\cap coNP$")
         + st.card("k-c2", "plain", "שפה ב-$NP \\cap coNP$ שאינה ב-$P$: לא ידוע")
         + st.card("k-c4", "plain", "פתוחות: $P = NP$ וגם $NP = coNP$")
         + st.card("k-c5", "rule", "🔑 $P = NP \\Rightarrow NP = coNP$, לא להפך"))

collapse = Scene("collapse", "קריסה", [
    P("עוד גרירה ששווה להכיר: אם $P = coNP$, אז $NP$ קורסת ל-$P$.", do=show("p-0"),
      say="עוד גרירה ששווה להכיר: אם פִּי שווה קוֹ-אֶן-פִּי, אז אֶן פִּי קורסת לפִּי."),
    P("ניקח $L$ ב-$NP$. המשלים שלה ב-$coNP$ לפי ההגדרה.", do=show("p-1"),
      say="ניקח אֵל באֶן פִּי. המשלים שלה בקוֹ-אֶן-פִּי לפי ההגדרה."),
    P("לפי ההנחה $coNP$ שווה ל-$P$, אז המשלים של $L$ ב-$P$.", do=show("p-2"),
      say="לפי ההנחה קוֹ-אֶן-פִּי שווה לפִּי, אז המשלים של אֵל בפִּי."),
    P("ו-$P$ סגורה למשלים, ולכן $L$ עצמה ב-$P$. כלומר $NP = P$.", do=show("p-3", "p-c1"), hold=0.4,
      say="ופִּי סגורה למשלים, ולכן אֵל עצמה בפִּי. כלומר אֶן פִּי שווה פִּי."),
], stage='<div class="stack" style="gap:30px">'
         '<div id="p-0" class="card plain h" style="font-size:40px">הנחה: $P = coNP$</div>'
         '<div id="p-1" class="bigmath h" style="font-size:44px">$L \\in NP \\Rightarrow \\overline{L} \\in coNP$</div>'
         '<div id="p-2" class="bigmath h" style="font-size:44px">$\\overline{L} \\in coNP = P$</div>'
         '<div id="p-3" class="bigmath h" style="font-size:44px">$\\Rightarrow L \\in P$</div></div>',
   panel=st.card("p-c1", "rule", "🔑 $P = coNP \\Rightarrow NP = P$"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: נכון או לא? אם $P = coNP$, אז המשלים של $CLIQUE$ שייך ל-$NP$.",
      say="שאלה ממבחן: נכון או לא? אם פִּי שווה קוֹ-אֶן-פִּי, אז המשלים של קְלִיק שייך לאֶן פִּי."),
    P("המלכודת: אנחנו לא יודעים אם המשלים של $CLIQUE$ ב-$NP$. אז אולי ״אין מספיק מידע״?", do=show("x-t"),
      say="המלכודת: אנחנו לא יודעים אם המשלים של קְלִיק באֶן פִּי. אז אולי אין מספיק מידע?"),
    P("אבל כאן יש **הנחה**, ומהנחה מותר להסיק.", do=show("x-1")),
    P("$CLIQUE$ ב-$NP$, ולכן המשלים שלה ב-$coNP$.", do=show("x-2"),
      say="קְלִיק באֶן פִּי, ולכן המשלים שלה בקוֹ-אֶן-פִּי."),
    P("לפי ההנחה זו בדיוק $P$, ו-$P$ מוכלת ב-$NP$. אז המשלים של $CLIQUE$ ב-$NP$.", do=show("x-3"),
      say="לפי ההנחה זו בדיוק פִּי, ופִּי מוכלת באֶן פִּי. אז המשלים של קְלִיק באֶן פִּי."),
    P("התשובה: נכון.", do=show("q-ok-a", "q-x-b", "q-x-c", "q-n-c"), hold=0.6),
], stage='<div class="stack" style="gap:30px">'
         '<div id="x-t" class="card trap h">⚠️ ״לא ידוע בלי הנחה״ ≠ ״לא נובע מההנחה״</div>'
         '<div id="x-1" class="card plain h" style="font-size:38px">הנחה: $P = coNP$</div>'
         '<div id="x-2" class="bigmath h" style="font-size:42px">$CLIQUE \\in NP \\Rightarrow \\overline{CLIQUE} \\in coNP$</div>'
         '<div id="x-3" class="bigmath h" style="font-size:42px">$coNP = P \\subseteq NP$</div></div>',
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>אם $P = coNP$ אז $\\overline{{CLIQUE}} \\in NP$.</div>'
         + st.options("q", OPTS, notes={"c": "ההנחה מספיקה"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $coNP$ היא השפות שהמשלים שלהן ב-$NP$. העד מוכיח ״לא״.", do=show("r-1"),
      say="לסיכום: קוֹ-אֶן-פִּי היא השפות שהמשלים שלהן באֶן פִּי. העד מוכיח לא."),
    P("$P$ ו-$NP$ סגורות לאיחוד, חיתוך, שרשור וכוכב. משלים ב-$NP$: פתוח.", do=show("r-2"),
      say="פִּי ואֶן פִּי סגורות לאיחוד, חיתוך, שרשור וכוכב. משלים באֶן פִּי: פתוח."),
    P("$P$ מוכלת בחיתוך של $NP$ ו-$coNP$, ו-$P = NP$ גורר $NP = coNP$.", do=show("r-3"),
      say="פִּי מוכלת בחיתוך של אֶן פִּי וקוֹ-אֶן-פִּי, ופִּי שווה אֶן פִּי גורר אֶן פִּי שווה קוֹ-אֶן-פִּי."),
    P("ומהנחה מותר להסיק, גם כשבלעדיה התשובה פתוחה. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$P \\subseteq NP \\cap coNP$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $coNP$: עד ל״לא״")
         + st.card("r-2", "rule", "🔑 משלים: $P$ כן, $NP$ פתוח")
         + st.card("r-3", "rule", "🔑 $P = NP \\Rightarrow NP = coNP$")
         + st.card("r-4", "trap", "⚠️ פתוח בלי הנחה, אבל נובע מהנחה"))

VIDEO = Video("N03", "np", "coNP וסגירויות של P ו-NP", [title, co, closure, known, collapse, exam, recap],
              bank={"22B-A-Q4": "a"})
