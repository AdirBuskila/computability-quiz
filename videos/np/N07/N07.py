# -*- coding: utf-8 -*-
"""N07 · מה נובע מ-P = NP, ומה נובע מ-P ≠ NP — video script (build: tools/video/vid.py N07).

Source: tools/courses_src/np/N07.js (lesson + goal). Exam anchor: 25B-B-Q6 (if P != NP: SAT not NPC? PATH not NPC?),
which no guided quiz uses.
Not used on purpose: the quiz questions of N07 (26B-B-Q10 and the five original ones: L in NPC and in P, PATH when
P = NP, which-is-true, SAT <=p PATH, L and its complement in NP). The "every nontrivial language in P" construction
is shown with a finite language, not PATH.
"""
from vid import P, Scene, Video, show, hide, BANK
import stage as st

# ---------------------------------------------------------------- facts (verified)
# A <=p B for any A in P and any nontrivial B: decide x in A, then write a fixed yes- or no-instance of B.
B = {"ab", "b"}                                  # a finite, nontrivial language over {a, b}
YES, NO = "ab", "a"
assert YES in B and NO not in B


def in_A(x):                                     # A = words with an even number of a's: in P
    return x.count("a") % 2 == 0


def f(x):
    return YES if in_A(x) else NO


import itertools
for n in range(7):
    for t in itertools.product("ab", repeat=n):
        x = "".join(t)
        assert in_A(x) == (f(x) in B)

Q = BANK["25B-B-Q6"]
assert Q["correctId"] == "d"
OPTS = [(o["id"], o["value"]) for o in Q["options"]]

WORLD1 = ('<div class="ncls" style="min-width:380px;min-height:300px;justify-content:center;flex-direction:row;gap:26px">'
          '<span class="nlab">$NP$</span>'
          '<div class="ncls" style="min-width:110px;padding:54px 24px 20px"><span class="nlab">$P$</span></div>'
          '<div class="ncls" style="min-width:110px;padding:54px 24px 20px;border-color:var(--bad)"><span class="nlab">$NPC$</span></div>'
          '</div>')
WORLD2 = ('<div class="ncls" style="min-width:380px;min-height:300px;justify-content:center">'
          '<span class="nlab">$P = NP$</span>'
          '<div class="hint" style="font-size:30px;text-align:center;line-height:1.5">כל שפה לא טריוויאלית<br>בה היא $NP$-שלמה</div>'
          '</div>')

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("שאלות ״מה נובע״ על $P$ ו-$NP$ נפתרות בכמה משפטים קבועים.",
      say="שאלות מה נובע על פִּי ואֶן פִּי נפתרות בכמה משפטים קבועים."),
    P("בסרטון הזה נלמד אותם, ונראה את המלכודות שחוזרות.", hold=0.4),
], stage='<div class="kicker">N07 · P, NP ו-NP-שלמות</div><h1>מה גורר P = NP ומה גוררת NP-שלמות</h1>'
         '<p>לגזור מסקנות נכונות מהנחה על $P$ ו-$NP$, ולזהות טענות שנראות נכונות ואינן.</p>', layout="title")

key = Scene("key", "המשפט המרכזי", [
    P("המשפט המרכזי: $P \\ne NP$ **אם ורק אם** אף שפה $NP$-שלמה אינה ב-$P$.", do=show("k-1"),
      say="המשפט המרכזי: פִּי שונה מאֶן פִּי אם ורק אם אף שפה אֶן פִּי שלמה אינה בפִּי."),
    P("למה? נניח ששפה שלמה $L$ ב-$P$. כל שפה ב-$NP$ מתרדדת אל $L$ בזמן פולינומי.", do=show("k-c1"),
      say="למה? נניח ששפה שלמה, אֵל, בפִּי. כל שפה באֶן פִּי מתרדדת אל אֵל בזמן פולינומי."),
    P("אז מחשבים את הרדוקציה, ומריצים את המכריע של $L$. כל שפה ב-$NP$ נכנסת ל-$P$.", do=show("k-c2"),
      say="אז מחשבים את הרדוקציה, ומריצים את המכריע של אֵל. כל שפה באֶן פִּי נכנסת לפִּי."),
    P("ומכאן שתי תמונות של העולם. אם $P \\ne NP$, אז $P$ והשפות השלמות **זרות**.", do=show("w-1"),
      say="ומכאן שתי תמונות של העולם. אם פִּי שונה מאֶן פִּי, אז פִּי והשפות השלמות זרות."),
    P("ואם $P = NP$, הכל מתמזג.", do=show("w-2"), say="ואם פִּי שווה אֶן פִּי, הכל מתמזג."),
    P("ובאותו אופן: $P \\ne NP$ אם ורק אם $CLIQUE$ לא ב-$P$, כי $CLIQUE$ שלמה.", do=show("k-c3"), hold=0.4,
      say="ובאותו אופן: פִּי שונה מאֶן פִּי אם ורק אם קְלִיק לא בפִּי, כי קְלִיק שלמה."),
], stage='<div class="stack" style="gap:30px">'
         '<div id="k-1" class="bigmath h" style="font-size:44px">$P \\ne NP \\iff P \\cap NPC = \\emptyset$</div>'
         f'<div style="display:flex;gap:40px;justify-content:center" dir="ltr"><div id="w-1" class="h">{WORLD1}'
         '<div class="hint" style="text-align:center">$P \\ne NP$</div></div>'
         f'<div id="w-2" class="h">{WORLD2}<div class="hint" style="text-align:center">$P = NP$</div></div></div></div>',
   panel=st.card("k-c1", "plain", "$L \\in NPC \\cap P$, וכל $A \\in NP$: $A \\le_p L$")
         + st.card("k-c2", "ex", "מחשבים $f$, מריצים את המכריע של $L$ ← $A \\in P$")
         + st.card("k-c3", "rule", "🔑 $P \\ne NP \\iff CLIQUE \\notin P$"))

collapse = Scene("collapse", "אם P = NP", [
    P("עכשיו נניח $P = NP$. מה קורה לשפות ב-$P$?", say="עכשיו נניח פִּי שווה אֶן פִּי. מה קורה לשפות בפִּי?"),
    P("טענה מפתיעה: אז אפילו שפה **סופית**, עם שתי מילים, היא $NP$-שלמה.", do=show("c-1"),
      say="טענה מפתיעה: אז אפילו שפה סופית, עם שתי מילים, היא אֶן פִּי שלמה."),
    P("קחו את השפה הסופית הזו, שתי מילים בלבד. נראה ששפה מ-$P$ מתרדדת אליה.", do=show("c-b"),
      say="קחו את השפה הסופית הזו, שתי מילים בלבד. נראה ששפה מפִּי מתרדדת אליה."),
    P("הרדוקציה פשוט **מכריעה** את הקלט, כי זה לוקח זמן פולינומי.", do=show("c-f1")),
    P("אם הקלט בשפת המקור, היא כותבת מילה מתוך השפה הסופית. ואם לא, מילה מחוצה לה.", do=show("c-f2")),
    P("וכש-$P = NP$, כל שפה ב-$NP$ היא כזו. אז השפה הסופית $NP$-קשה, והיא ב-$NP$. כלומר שלמה.", do=show("c-c1"),
      say="וכשפִּי שווה אֶן פִּי, כל שפה באֶן פִּי היא כזו. אז השפה הסופית אֶן פִּי קשה, והיא באֶן פִּי. כלומר שלמה."),
    P("ולמה לא כל שפה? רדוקציה מ-$SAT$ חייבת לשלוח נוסחאות ספיקות פנימה, ונוסחאות לא ספיקות החוצה.", do=show("c-c2"),
      say="ולמה לא כל שפה? רדוקציה מסַאט חייבת לשלוח נוסחאות ספיקות פנימה, ונוסחאות לא ספיקות החוצה."),
    P("לקבוצה הריקה ולסיגמא כוכבית אין לאן לשלוח אחת מהן. לכן הן **לעולם** לא שלמות.", hold=0.4),
], stage='<div class="stack" style="gap:30px">'
         '<div id="c-1" class="card rule h" style="font-size:34px">🔑 $P = NP$ ← גם שפה סופית יכולה להיות $NP$-שלמה</div>'
         '<div id="c-b" class="bigmath h" style="font-size:44px">$B = \\{ ab,\\ b \\}$</div>'
         '<div id="c-f1" class="card ex h" style="font-size:32px">$f(x)$: מכריעים אם $x \\in A$, בזמן פולינומי</div>'
         '<div id="c-f2" class="bigmath h" style="font-size:38px">$x \\in A \\mapsto ab \\in B$ · $x \\notin A \\mapsto a \\notin B$</div></div>',
   panel=st.card("c-c1", "plain", "$P = NP$: כל שפה ב-$NP$ מתרדדת אל $B$")
         + st.card("c-c2", "trap", "⚠️ $\\emptyset$ ו-$\\Sigma^*$ אינן $NP$-שלמות לעולם: אין לאן למפות"))

traps = Scene("traps", "מלכודות", [
    P("שתי מלכודות שחוזרות במבחנים."),
    P("הראשונה: אלגוריתם פולינומי לשפה כלשהי ב-$NP$ לא מוכיח ש-$P = NP$.", do=show("t-1"),
      say="הראשונה: אלגוריתם פולינומי לשפה כלשהי באֶן פִּי לא מוכיח שפִּי שווה אֶן פִּי."),
    P("הרבה שפות ב-$NP$ הן כבר ב-$P$. זה עובד רק אם השפה $NP$-**שלמה**.", do=show("t-1b"),
      say="הרבה שפות באֶן פִּי הן כבר בפִּי. זה עובד רק אם השפה אֶן פִּי שלמה."),
    P("השנייה: ״שפה $NP$-שלמה היא הכי קשה שיש״. לא נכון.", do=show("t-2"),
      say="השנייה: שפה אֶן פִּי שלמה היא הכי קשה שיש. לא נכון."),
    P("כל שפה $NP$-שלמה כריעה. יש שפות קשות ממנה בהרבה, כמו שפות שאינן כריעות בכלל.", do=show("t-2b"), hold=0.4),
], stage='<div class="stack" style="gap:24px">'
         '<div id="t-1" class="card trap h" style="font-size:34px">⚠️ אלגוריתם פולינומי ל-$A \\in NP$ ⇏ $P = NP$</div>'
         '<div id="t-1b" class="card plain h" style="font-size:32px">רק אם $A$ היא $NP$-שלמה</div>'
         '<div id="t-2" class="card trap h" style="font-size:34px">⚠️ ״$NPC$ הן הקשות ביותר״</div>'
         '<div id="t-2b" class="card plain h" style="font-size:32px">$NPC \\subseteq NP \\subseteq R$: כולן כריעות</div></div>',
   layout="full")

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: שתי טענות. הראשונה: אם $P \\ne NP$, אז $SAT$ אינה $NP$-שלמה.",
      say="שאלה ממבחן: שתי טענות. הראשונה: אם פִּי שונה מאֶן פִּי, אז סַאט אינה אֶן פִּי שלמה."),
    P("השנייה: אם $P \\ne NP$, אז $PATH$ אינה $NP$-שלמה.",
      say="השנייה: אם פִּי שונה מאֶן פִּי, אז פַּאת' אינה אֶן פִּי שלמה."),
    P("הראשונה שגויה. ש-$SAT$ שלמה הוכח בלי שום הנחה, במשפט קוק-לוין.", do=show("x-1"),
      say="הראשונה שגויה. שסַאט שלמה הוכח בלי שום הנחה, במשפט קוק לוין."),
    P("השנייה נכונה. $PATH$ ב-$P$. אילו הייתה שלמה, הייתה שפה שלמה ב-$P$, ואז $P = NP$. סתירה להנחה.", do=show("x-2"),
      say="השנייה נכונה. פַּאת' בפִּי. אילו הייתה שלמה, הייתה שפה שלמה בפִּי, ואז פִּי שווה אֶן פִּי. סתירה להנחה."),
    P("אז השנייה נכונה והראשונה לא.", do=show("q-ok-d", "q-x-a", "q-x-b", "q-x-c"), hold=0.6),
], stage='<div class="stack" style="gap:30px">'
         '<div id="x-1" class="card trap h" style="font-size:34px">I. $SAT \\in NPC$ תמיד: קוק-לוין ✗</div>'
         '<div id="x-2" class="card rule h" style="font-size:34px">II. $PATH \\in P$, ו-$P \\cap NPC = \\emptyset$ כש-$P \\ne NP$ ✓</div></div>',
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>I. אם $P \\ne NP$ אז $SAT \\notin NPC$.<br>'
         'II. אם $P \\ne NP$ אז $PATH \\notin NPC$.</div>' + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: שפה שלמה אחת ב-$P$, ו-$P = NP$. ולהפך.", do=show("r-1"),
      say="לסיכום: שפה שלמה אחת בפִּי, ופִּי שווה אֶן פִּי. ולהפך."),
    P("אם $P \\ne NP$, $P$ והשפות השלמות זרות.", do=show("r-2"),
      say="אם פִּי שונה מאֶן פִּי, פִּי והשפות השלמות זרות."),
    P("אם $P = NP$, כל שפה לא טריוויאלית ב-$P$ שלמה. הקבוצה הריקה וסיגמא כוכבית אף פעם לא.", do=show("r-3"),
      say="אם פִּי שווה אֶן פִּי, כל שפה לא טריוויאלית בפִּי שלמה. הקבוצה הריקה וסיגמא כוכבית אף פעם לא."),
    P("ו-$SAT$ שלמה בלי שום הנחה. ברמה הבאה: מבחן גמר.", do=show("r-4"), hold=0.6,
      say="וסַאט שלמה בלי שום הנחה. ברמה הבאה: מבחן גמר."),
], stage='<div class="stack"><div class="bigmath">$P \\cap NPC \\ne \\emptyset \\iff P = NP$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $P \\cap NPC \\ne \\emptyset \\iff P = NP$")
         + st.card("r-2", "rule", "🔑 $P \\ne NP$: $P$ ו-$NPC$ זרות")
         + st.card("r-3", "rule", "🔑 $P = NP$: כל לא טריוויאלית ב-$P$ שלמה")
         + st.card("r-4", "trap", "⚠️ $SAT \\in NPC$ בלי תנאי"))

VIDEO = Video("N07", "np", "מה גורר P = NP ומה גוררת NP-שלמות", [title, key, collapse, traps, exam, recap],
              bank={"25B-B-Q6": "d"})
