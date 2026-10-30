# -*- coding: utf-8 -*-
"""N02 · המחלקה NP: עד ומוודא — video script (build: tools/video/vid.py N02).

Source: tools/courses_src/np/N02.js (lesson + goal). Exam anchor: 24A-A-Q2 (a polynomial machine of unknown kind
decides L: what follows?), which no guided quiz uses.
Not used on purpose: the quiz questions of N02 (25B-A-Q6 and the five original ones: verifier definition, CLIQUE
witness, which-is-true, NTM view, the A_NFA witness). The worked verifier here runs on a SAT formula, not CLIQUE.
"""
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_np as g

# ---------------------------------------------------------------- facts (verified)
PHI = [(("x1", True), ("x2", False), ("x3", True)), (("x1", False), ("x2", True)), (("x3", False), ("x2", True))]
GOOD = {"x1": True, "x2": True, "x3": False}
BAD = {"x1": True, "x2": False, "x3": False}
assert g.satisfies(PHI, GOOD) and not g.satisfies(PHI, BAD) and g.satisfiable(PHI)
TRUE_IN = [[g.lit_true(l, GOOD) for l in c] for c in PHI]
assert all(any(r) for r in TRUE_IN)
assert [any(g.lit_true(l, BAD) for l in c) for c in PHI] == [True, False, True]   # BAD fails clause 2 only
# an unsatisfiable formula: no certificate at all
UNSAT = [(("x1", True),), (("x1", False),)]
assert not g.satisfiable(UNSAT)

Q = BANK["24A-A-Q2"]
assert Q["correctId"] == "d"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

F1 = g.cnf_row("f1", PHI)
G1 = f'<div class="npf">$c_1:\\ {g.assign_tex(GOOD)}$</div>'
G2 = f'<div class="npf">$c_2:\\ {g.assign_tex(BAD)}$</div>'

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נכיר את $NP$: השפות שקל **לוודא**, גם אם לא ידוע איך קל **לפתור**."),
    P("נריץ מוודא על נוסחה, נראה את שלוש השאלות שכל הוכחה צריכה,"),
    P("ונמקם את $NP$ בין המחלקות שאנחנו כבר מכירים.", hold=0.4),
], stage='<div class="kicker">N02 · P, NP ו-NP-שלמות</div><h1>המחלקה NP: מוודא ועד</h1>'
         '<p>להוכיח ש-$L \\in NP$ בעזרת עד קצר ומוודא פולינומי, ולמקם את $NP$ בין $P$ ל-$R$.</p>', layout="title")

defs = Scene("def", "ההגדרה", [
    P("$L$ שייכת ל-$NP$ אם יש לה **מוודא**: מכונה דטרמיניסטית $V$ שרצה בזמן פולינומי.", do=show("d-v"),
      say="אֵל שייכת לאֶן פִּי אם יש לה מוודא: מכונה דטרמיניסטית, וִי, שרצה בזמן פולינומי."),
    P("המוודא מקבל את המילה $w$, וגם **רמז** $c$, שנקרא עד.", do=show("d-in"),
      say="המוודא מקבל את המילה דַּאבְּלְיוּ, וגם רמז, סִי, שנקרא עד."),
    P("אם $w$ בשפה, **קיים** עד באורך פולינומי שהמוודא מקבל.", do=show("d-yes"),
      say="אם דַּאבְּלְיוּ בשפה, קיים עד באורך פולינומי שהמוודא מקבל."),
    P("ואם $w$ לא בשפה, **אין** אף עד שהמוודא מקבל. אי אפשר לרמות אותו.", do=show("d-no"), hold=0.4,
      say="ואם דַּאבְּלְיוּ לא בשפה, אין אף עד שהמוודא מקבל. אי אפשר לרמות אותו."),
    P("המוודא לא צריך למצוא את העד. הוא רק בודק עד שקיבל.", do=show("d-c1")),
], stage='<div class="stack"><div id="d-v" class="big h">$V(w, c)$</div>'
         '<div id="d-in" class="card plain h" style="font-size:34px">$w$: הקלט · $c$: העד, באורך פולינומי ב-$|w|$</div>'
         '<div id="d-yes" class="verdict ok h">$w \\in L$ ← קיים $c$ ש-$V$ מקבלת</div>'
         '<div id="d-no" class="verdict bad h">$w \\notin L$ ← לכל $c$, $V$ דוחה</div></div>',
   panel=st.card("d-c1", "rule", "🔑 $NP$: קל <b>לבדוק</b> פתרון. לא בהכרח קל <b>למצוא</b> אותו"))

verify = Scene("verify", "מוודא בפעולה", [
    P("נראה מוודא אמיתי, לשפה $SAT$: נוסחאות שיש להן השמה מספקת.", do=show("v-f")),
    P("העד הוא השמה: ערך אמת או שקר לכל משתנה.", do=show("v-g1")),
    P("המוודא עובר על הפסוקיות אחת אחת. בראשונה, $x_1$ אמת, אז היא מסופקת.", do=show("f1-ok0"),
      say="המוודא עובר על הפסוקיות אחת אחת. בראשונה, אִקְס אחת אמת, אז היא מסופקת."),
    P("בשנייה, $x_2$ אמת. מסופקת.", do=show("f1-ok1"), say="בשנייה, אִקְס שתיים אמת. מסופקת."),
    P("ובשלישית, $x_3$ שקר, ולכן ״לא $x_3$״ אמת. מסופקת.", do=show("f1-ok2"),
      say="ובשלישית, אִקְס שלוש שקר, ולכן לא אִקְס שלוש אמת. מסופקת."),
    P("כל הפסוקיות מסופקות, והמוודא מקבל. סריקה אחת, זמן פולינומי.", do=show("v-ok"), hold=0.4),
    P("עכשיו עד אחר, שבו $x_2$ שקר.", do=hide("f1-ok0", "f1-ok1", "f1-ok2", "v-g1", "v-ok") + show("v-g2"),
      say="עכשיו עד אחר, שבו אִקְס שתיים שקר."),
    P("הפסוקית השנייה נופלת, והמוודא דוחה את **העד הזה**.", do=show("f1-ok0", "f1-bad1", "f1-ok2", "v-c1")),
    P("זה לא אומר שהנוסחה לא ספיקה. ראינו שיש לה עד טוב. דחייה של עד אחד לא מוכיחה כלום.", do=show("v-c2"), hold=0.4),
], stage='<div class="stack" style="gap:76px">'
         f'<div id="v-f" class="h">{F1}</div>'
         f'<div class="swap" style="--swap-h:150px"><div id="v-g1" class="h">{G1}'
         '<div id="v-ok" class="verdict ok h">$V$ מקבלת ✓</div></div>'
         f'<div id="v-g2" class="h">{G2}<div class="verdict bad">$V$ דוחה את $c_2$</div></div></div>'
         '</div>',
   panel=st.card("v-c1", "plain", "עד שנכשל: המוודא דוחה <b>אותו</b>")
         + st.card("v-c2", "trap", "⚠️ $w \\in L$ אם <b>קיים</b> עד טוב. עד רע אחד לא מוכיח $w \\notin L$"))

ROWS = '<table class="npt"><thead><tr><th>שפה</th><th>העד</th></tr></thead><tbody>' \
       '<tr id="t-r1" class="h"><td>$SAT$</td><td>השמה מספקת</td></tr>' \
       '<tr id="t-r2" class="h"><td>$CLIQUE$, $IS$, $VC$</td><td>רשימת הקודקודים</td></tr>' \
       '<tr id="t-r3" class="h"><td>$HAMPATH$</td><td>סדר הקודקודים במסלול</td></tr></tbody></table>'
three = Scene("three", "שלוש שאלות", [
    P("כל הוכחה ש-$L$ ב-$NP$ עונה על שלוש שאלות.", say="כל הוכחה שאֵל באֶן פִּי עונה על שלוש שאלות."),
    P("אחת: מה העד?", do=show("h-1")),
    P("שתיים: למה הוא באורך פולינומי?", do=show("h-2")),
    P("ושלוש: איך בודקים אותו בזמן פולינומי?", do=show("h-3"), hold=0.3),
    P("ב-$SAT$ העד הוא השמה: ערך אחד לכל משתנה, אז הוא קצר מהנוסחה.", do=show("t"),
      say="בסַאט העד הוא השמה: ערך אחד לכל משתנה, אז הוא קצר מהנוסחה."),
    P("בבעיות של קבוצות קודקודים בגרף, העד הוא רשימת הקודקודים, ובודקים את הזוגות.", do=show("t-r1", "t-r2")),
    P("ובמסלול המילטון, העד הוא סדר הקודקודים. בודקים שכל אחד מופיע פעם אחת ושיש צלעות ביניהם.", do=show("t-r3"), hold=0.4),
], stage=f'<div class="stack"><div id="t" class="h">{ROWS}</div></div>',
   panel=st.card("h-1", "rule", "1️⃣ מה העד?")
         + st.card("h-2", "rule", "2️⃣ למה הוא באורך פולינומי?")
         + st.card("h-3", "rule", "3️⃣ איך בודקים אותו בזמן פולינומי?"))

ntm = Scene("ntm", "ניחוש ובדיקה", [
    P("יש עוד דרך להסתכל על $NP$: מכונה **אי-דטרמיניסטית** שמכריעה בזמן פולינומי.", do=show("n-1")),
    P("בכל ענף היא מנחשת עד אחר, ומריצה עליו את המוודא.", do=show("n-c1")),
    P("אם באחד הענפים המוודא מקבל, המכונה מקבלת. שתי ההגדרות שקולות.", do=show("n-c2"), hold=0.3),
    P("ומכאן הסדר בין המחלקות. $P$ מוכלת ב-$NP$: מכריע הוא מוודא שמתעלם מהעד.", do=show("cl-w", "cl-np", "cl-p", "n-c3"),
      say="ומכאן הסדר בין המחלקות. פִּי מוכלת באֶן פִּי: מכריע הוא מוודא שמתעלם מהעד."),
    P("ו-$NP$ מוכלת ב-$R$: אפשר לנסות את כל העדים. זה אקספוננציאלי, אבל תמיד עוצר.", do=show("n-c4"),
      say="ואֶן פִּי מוכלת באָר: אפשר לנסות את כל העדים. זה אקספוננציאלי, אבל תמיד עוצר."),
    P("לכן אין שפה ב-$NP$ שאינה כריעה.", hold=0.3, say="לכן אין שפה באֶן פִּי שאינה כריעה."),
    P("ושימו לב: עד מוכיח ״כן״. אין עד קצר ידוע לכך שנוסחה **לא** ספיקה.", do=show("n-c5")),
    P("לכן לא ידוע אם המשלים של $SAT$ שייך ל-$NP$.", hold=0.4, say="לכן לא ידוע אם המשלים של סַאט שייך לאֶן פִּי."),
], stage='<div class="stack">'
         + '<div id="cl-w" class="h">' + g.classes("cl", [("r", "$R$"), ("np", "$NP$"), ("p", "$P$")]) + '</div>'
         + '<div id="n-1" class="bigmath h" style="font-size:40px">$NP$ = מכונה אי-דטרמיניסטית, זמן פולינומי</div></div>',
   panel=st.card("n-c1", "ex", "כל ענף: ניחוש של $c$, ואז $V(w, c)$")
         + st.card("n-c2", "plain", "מקבלת אם ענף אחד לפחות מקבל")
         + st.card("n-c3", "rule", "🔑 $P \\subseteq NP$")
         + st.card("n-c4", "rule", "🔑 $NP \\subseteq R$")
         + st.card("n-c5", "trap", "⚠️ עד מוכיח שייכות, לא אי-שייכות: $\\overline{SAT} \\in NP$ לא ידוע"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: מכונה $M$ שרצה בזמן פולינומי מכריעה את $L$. לא אומרים לנו איזו מכונה. מה נכון?",
      say="שאלה ממבחן: מכונה, אֵם, שרצה בזמן פולינומי מכריעה את אֵל. לא אומרים לנו איזו מכונה. מה נכון?"),
    P("אם $M$ דטרמיניסטית, אז $L$ ב-$P$. ואם היא אי-דטרמיניסטית, אז $L$ ב-$NP$.", do=show("x-1"),
      say="אם אֵם דטרמיניסטית, אז אֵל בפִּי. ואם היא אי-דטרמיניסטית, אז אֵל באֶן פִּי."),
    P("בכל מקרה $L$ ב-$NP$, ולכן הטענה שהיא לא ב-$P$ וגם לא ב-$NP$ נופלת.", do=show("q-x-b"),
      say="בכל מקרה אֵל באֶן פִּי, ולכן הטענה שהיא לא בפִּי וגם לא באֶן פִּי נופלת."),
    P("הטענה ש-$M$ דטרמיניסטית ולכן $L$ לא ב-$NP$ הפוכה: $P$ מוכלת ב-$NP$.", do=show("q-x-c"),
      say="הטענה שאֵם דטרמיניסטית ולכן אֵל לא באֶן פִּי הפוכה: פִּי מוכלת באֶן פִּי."),
    P("והמלכודת: מכונה אי-דטרמיניסטית עם שלושה סרטים. האם $L$ בהכרח ב-$P$?", do=show("x-2"),
      say="והמלכודת: מכונה אי דטרמיניסטית עם שלושה סרטים. האם אֵל בהכרח בפִּי?"),
    P("מספר הסרטים לא משנה כלום. הבעיה היא האי-דטרמיניזם, והסימולציה שלו אקספוננציאלית.", do=show("q-x-a", "q-n-a")),
    P("אז אף אחת מהטענות לא נכונה, וזו התשובה.", do=show("q-ok-d"), hold=0.6),
], stage='<div class="stack">'
         '<div id="x-1" class="card ex h">דטרמיניסטית ← $P$ · אי-דטרמיניסטית ← $NP$</div>'
         '<div id="x-2" class="card trap h">⚠️ סרטים: ריבוע · אי-דטרמיניזם: אקספוננט</div></div>',
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>מכונה $M$ שרצה בזמן פולינומי מכריעה את $L$. '
         'איזו טענה נכונה?</div>'
         + st.options("q", OPTS, notes={"a": "לא ידוע"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: $L$ ב-$NP$ אם יש לה עד קצר ומוודא דטרמיניסטי פולינומי.", do=show("r-1"),
      say="לסיכום: אֵל באֶן פִּי אם יש לה עד קצר ומוודא דטרמיניסטי פולינומי."),
    P("שלוש שאלות: מה העד, למה הוא קצר, ואיך בודקים אותו.", do=show("r-2")),
    P("$P$ מוכלת ב-$NP$, ו-$NP$ מוכלת ב-$R$.", do=show("r-3"),
      say="פִּי מוכלת באֶן פִּי, ואֶן פִּי מוכלת באָר."),
    P("ועד מוכיח ״כן״, לא ״לא״. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="big">$V(w, c)$</div><div class="bigmath">$P \\subseteq NP \\subseteq R$</div></div>',
   panel=st.card("r-1", "rule", "🔑 עד קצר + מוודא פולינומי")
         + st.card("r-2", "rule", "🔑 מה העד · למה קצר · איך בודקים")
         + st.card("r-3", "rule", "🔑 $P \\subseteq NP \\subseteq R$")
         + st.card("r-4", "trap", "⚠️ עד מוכיח שייכות בלבד"))

VIDEO = Video("N02", "np", "המחלקה NP: מוודא ועד", [title, defs, verify, three, ntm, exam, recap],
              bank={"24A-A-Q2": "d"})
