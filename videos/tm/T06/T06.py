# -*- coding: utf-8 -*-
"""T06 · וריאנטים ומכונה אי-דטרמיניסטית — video script (build: tools/video/vid.py T06).

Source: tools/courses_src/tm/T06.js (lesson + goal). Exam anchor: 25A-A-Q17 (three claims about the paths of a
non-deterministic machine, all false), which no guided quiz uses. Not used on purpose: the T06 quiz (accept +
infinite path, "decides", the acc/rej swap, 5 tapes in O(n⁴), …), 24A-B-Q3 and 22A-B-Q11 (cited in the lesson), and the
"choose M₁ or M₂" construction (24A-C-Q17, 24A-B-Q4 in the T07 boss quiz, 23A-B-Q4).
The tree verdicts come from w_tm.ntm_verdict (exists an accepting branch / all branches reject); each exam
counterexample tree is checked the same way.
"""
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_tm

V = w_tm.ntm_verdict
# ---------------------------------------------------------------- facts (verified)
assert 5 * 2 == 10                                    # 3 tapes in O(n^5) -> one tape in O((n^5)^2) = O(n^10)
T_ACC = [("acc", 3), ("rej", 2), ("loop", 3)]         # one accepting branch, one rejecting, one infinite
T_REJ = [("rej", 2), ("rej", 3), ("rej", 2)]
T_NONE = [("rej", 2), ("loop", 3), ("rej", 3)]
assert V([k for k, _ in T_ACC]) == "accept"
assert V([k for k, _ in T_REJ]) == "reject"
assert V([k for k, _ in T_NONE]) == "none"
T_SW = [("acc", 2), ("rej", 3)]
SWAP = {"acc": "rej", "rej": "acc", "loop": "loop"}
assert V([k for k, _ in T_SW]) == "accept" and V([SWAP[k] for k, _ in T_SW]) == "accept"   # both accept w

# exam 25A-A-Q17: one counterexample tree per claim
X_A = [("acc", 2), ("loop", 2)]       # (a) accepts every input (this tree on every w), yet a path never halts
X_B = [("rej", 2), ("loop", 2)]       # (b) some paths reject, the rest never halt: M does NOT reject w
assert V([k for k, _ in X_A]) == "accept" and any(k == "loop" for k, _ in X_A)
assert V([k for k, _ in X_B]) == "none"
# (c) X_A on every input: a non-halting path on every w, and L(M) = Σ*, which is decidable

Q = BANK["25A-A-Q17"]
assert Q["correctId"] == "d"
SHORT = {"a": "מקבלת כל קלט ⇐ כל המסלולים על כל הקלטים עוצרים",
         "b": "חלק מהמסלולים דוחים והשאר לא עוצרים ⇐ $M$ דוחה את $w$",
         "c": "קיים $w$ עם מסלול שלא עוצר ⇐ $L(M)$ לא כריעה",
         "d": "אף אחת מהתשובות האחרות אינה נכונה"}
assert [o["id"] for o in Q["options"]] == list(SHORT)
OPTS = [(o["id"], SHORT[o["id"]]) for o in Q["options"]]

LBL = {"acc": "✓", "rej": "✗", "loop": "∞"}


def labelled(pfx, tree, w=320, h=330, cap=""):
    return (f'<div class="stack" style="gap:6px;width:auto">{w_tm.ntm_tree(pfx, tree, w, h)}'
            f'<div class="hint">{cap}</div></div>')


def show_tree(pfx, tree):
    return show(*[f"{pfx}-b{i}" for i in range(len(tree))], *[f"{pfx}-l{i}-{k}" for i, (k, _) in enumerate(tree)])


# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("מכונה עם כמה סרטים, סרט שאינסופי לשני הכיוונים, ומכונה אי-דטרמיניסטית."),
    P("נראה מה הן מוסיפות, ומה לא. ונבין מתי מכונה אי-דטרמיניסטית מקבלת, דוחה או מכריעה.", hold=0.4),
], stage='<div class="kicker">T06 · מכונות טיורינג</div><h1>וריאנטים ומכונה אי-דטרמיניסטית</h1>'
         '<p>כל הוריאנטים שקולים בכוח החישובי, אבל לא בזמן. ומתי מכונה אי-דטרמיניסטית מקבלת, דוחה ומכריעה.</p>',
   layout="title")

variants = Scene("variants", "וריאנטים", [
    P("שלושה וריאנטים מפורסמים: מכונה מרובת סרטים, מכונה עם סרט דו-כיווני, ומכונה אי-דטרמיניסטית.", do=show("v-1")),
    P("ולכולם אותו כוח: כל שפה שוריאנט מקבל, גם המכונה הבסיסית מקבלת. וכל שפה שהוא מכריע, גם היא מכריעה.",
      do=show("v-2")),
    P("ההבדל הוא רק בזמן. מכונה עם כמה סרטים בזמן $t$ הופכת למכונה עם סרט אחד בזמן $t$ בריבוע.", do=show("v-3"),
      say="ההבדל הוא רק בזמן. מכונה עם כמה סרטים בזמן טִי הופכת למכונה עם סרט אחד בזמן טִי בריבוע."),
    P("ומכונה אי-דטרמיניסטית בזמן $t$ הופכת לדטרמיניסטית בזמן אקספוננציאלי ב-$t$.", do=show("v-4"),
      say="ומכונה אי דטרמיניסטית בזמן טִי הופכת לדטרמיניסטית בזמן אקספוננציאלי בטִי."),
    P("דוגמה: שלושה סרטים, בזמן $O(n^5)$. בסרט אחד: מעלים את החסם בריבוע, ומקבלים $O(n^{10})$.",
      do=show("v-ex"),
      say="דוגמה: שלושה סרטים, בזמן או של אֶן בחזקת חמש. בסרט אחד: מעלים את החסם בריבוע, ומקבלים או של אֶן בחזקת עשר."),
    P("לא כופלים במספר הסרטים. מעלים בריבוע את החסם.", do=show("v-t"), hold=0.4),
], stage='<div class="stack">'
         '<table class="delta" dir="ltr"><thead><tr><th>מעבר</th><th>זמן</th></tr></thead><tbody>'
         '<tr id="v-3" class="h"><td style="direction:rtl">$k$ סרטים ← סרט אחד</td><td>$t(n) \\to O(t(n)^2)$</td></tr>'
         '<tr id="v-4" class="h"><td style="direction:rtl">אי-דטרמיניסטית ← דטרמיניסטית</td><td>$t(n) \\to 2^{O(t(n))}$</td></tr>'
         '</tbody></table>'
         '<div id="v-ex" class="bigmath h" style="font-size:44px">$O(n^5) \\to O\\big((n^5)^2\\big) = O(n^{10})$</div>'
         '</div>',
   panel=st.card("v-1", "plain", "מרובת סרטים · דו-כיווני · אי-דטרמיניסטית")
         + st.card("v-2", "rule", "🔑 כולם שקולים בכוח: אותן שפות ב-$R$ וב-$RE$")
         + st.card("v-t", "trap", "⚠️ מעלים בריבוע את החסם, לא כופלים ב-$k$"))

tree = Scene("tree", "עץ חישוב", [
    P("במכונה אי-דטרמיניסטית, $\\delta$ מחזירה **קבוצה** של אפשרויות, ולא אפשרות אחת.", do=show("t-1")),
    P("לכן לריצה על מילה יש **עץ חישוב**: כל ענף הוא מסלול אחר של בחירות.", do=show("ta-b0")),
    P("הענף הזה מגיע ל-$q_{acc}$.", do=show("ta-l0-acc")),
    P("הענף הזה דוחה.", do=show("ta-b1", "ta-l1-rej")),
    P("והענף הזה לא עוצר לעולם.", do=show("ta-b2", "ta-l2-loop")),
    P("אז מה התשובה? המכונה **מקבלת**: מספיק שקיים מסלול מקבל **אחד**.", do=show("t-2")),
    P("הענף הדוחה והענף האינסופי לא מפריעים לקבלה.", do=show("t-3"), hold=0.4),
], stage=labelled("ta", T_ACC, 560, 440),
   panel=st.card("t-1", "ex", "$\\delta$ מחזירה קבוצה של שלישיות")
         + st.card("t-2", "rule", "🔑 מקבלת = <b>קיים</b> מסלול מקבל")
         + st.card("t-3", "trap", "⚠️ ענף אינסופי לא מונע קבלה"))

rules = Scene("rules", "דוחה ומכריעה", [
    P("ומתי היא **דוחה**? רק כש**כל** המסלולים סופיים ודוחים.", do=show_tree("tb", T_REJ) + show("tb-c")),
    P("ואם אין מסלול מקבל, אבל יש ענף שלא עוצר?", do=show_tree("tc", T_NONE)),
    P("אז המילה לא בשפה, אבל המכונה גם לא דוחה אותה: יש לה ענף שלא עוצר.", do=show("tc-c")),
    P("ומכונה אי-דטרמיניסטית **מכריעה** שפה אם על **כל** קלט, **כל** המסלולים עוצרים.", do=show("u-1"), hold=0.4),
], stage='<div style="display:flex;gap:80px;justify-content:center;direction:ltr">'
         + labelled("tb", T_REJ, cap='<span id="tb-c" class="h">דוחה ✗</span>')
         + labelled("tc", T_NONE, cap='<span id="tc-c" class="h">לא מקבלת, לא דוחה</span>') + "</div>",
   panel=st.card("u-0", "plain", "<b>דוחה</b> = כל המסלולים סופיים ודוחים").replace(' h"', '"')
         + st.card("u-1", "rule", "🔑 <b>מכריעה</b> = על כל קלט, כל המסלולים עוצרים"))

swap = Scene("swap", "החלפת קבלה ודחייה", [
    P("ומלכודת קלאסית: מחליפים במכונה אי-דטרמיניסטית את $q_{acc}$ ואת $q_{rej}$. האם מקבלים את המשלים?",
      do=show_tree("ts", T_SW) + show("s-q")),
    P("כאן יש מסלול מקבל ומסלול דוחה, ולכן המכונה מקבלת את המילה.", do=show("s-1")),
    P("אחרי ההחלפה, המסלול הדוחה הפך למקבל.",
      do=hide("ts-l0-acc", "ts-l1-rej") + show("ts-l0-rej", "ts-l1-acc")),
    P("אז גם המכונה החדשה מקבלת את אותה מילה. היא בשתי השפות, ולכן השפה החדשה **אינה** המשלים.", do=show("s-2"),
      hold=0.4),
], stage=labelled("ts", T_SW, 460, 420),
   panel=st.card("s-q", "plain", "מחליפים $q_{acc} \\leftrightarrow q_{rej}$")
         + st.card("s-1", "ex", "לפני: יש מסלול מקבל, מקבלת")
         + st.card("s-2", "trap", "⚠️ אחרי: יש מסלול מקבל, <b>שוב</b> מקבלת. זה לא המשלים"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: $M$ מכונה אי-דטרמיניסטית. איזו טענה נכונה? נבדוק כל טענה עם עץ חישוב."),
    P("טענה ראשונה: אם $M$ מקבלת כל קלט, אז כל המסלולים עוצרים.", do=show("ea-b0", "ea-b1", "ea-l0-acc", "ea-l1-loop")),
    P("לא. העץ הזה מקבל, כי יש בו מסלול מקבל. ובכל זאת יש בו ענף שלא עוצר.", do=show("ea-c", "q-x-a")),
    P("טענה שנייה: אם חלק מהמסלולים דוחים, וכל השאר לא עוצרים, אז $M$ דוחה את $w$.",
      do=show("eb-b0", "eb-b1", "eb-l0-rej", "eb-l1-loop")),
    P("לא. דחייה דורשת שכל המסלולים יעצרו וידחו. כאן $w$ לא בשפה, אבל המכונה לא דוחה אותה.", do=show("eb-c", "q-x-b")),
    P("טענה שלישית: אם על קלט כלשהו יש מסלול שלא עוצר, השפה של $M$ לא כריעה.", do=show("x-c")),
    P("גם לא. נריץ את העץ הראשון על כל קלט: השפה היא כל המילים, וזו שפה כריעה.", do=show("x-c2", "q-x-c")),
    P("המלכודת: לבלבל בין המכונה לבין השפה. מכונה אחת שלא עוצרת לא אומרת שאין מכונה אחרת שמכריעה.",
      do=show("x-t")),
    P("אז אף טענה לא נכונה, והתשובה היא ״אף אחת מהתשובות האחרות״.", do=show("q-ok-d"), hold=0.6),
], stage='<div class="stack" style="gap:14px"><div style="display:flex;gap:70px;justify-content:center;direction:ltr">'
         + labelled("ea", X_A, 260, 260, '<span id="ea-c" class="h">מקבלת ✓ · ענף ∞</span>')
         + labelled("eb", X_B, 260, 260, '<span id="eb-c" class="h">לא מקבלת, לא דוחה</span>') + "</div>"
         + st.card("x-c", "plain", "טענה 3: מסלול שלא עוצר ⇐ השפה לא כריעה?")
         + st.card("x-c2", "ex", "העץ הראשון על כל קלט: $L(M) = \\Sigma^*$, כריעה")
         + st.card("x-t", "trap", "⚠️ מכונה שלא עוצרת ≠ שפה לא כריעה")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$M$ מכונה אי-דטרמיניסטית. איזו טענה נכונה?</div>'
         + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: כל הוריאנטים שקולים בכוח. סרטים: זמן בריבוע. אי-דטרמיניזם: זמן אקספוננציאלי.", do=show("r-1")),
    P("מכונה אי-דטרמיניסטית מקבלת אם **קיים** מסלול מקבל, ודוחה אם **כל** המסלולים דוחים.", do=show("r-2")),
    P("היא מכריעה אם כל המסלולים עוצרים. והחלפת $q_{acc}$ ו-$q_{rej}$ לא נותנת משלים. נתראה ברמה הבאה.",
      do=show("r-3"), hold=0.6),
], stage='<div class="stack"><div class="bigmath" style="font-size:46px">∃ ✓ &nbsp;·&nbsp; ∀ ✗</div></div>',
   panel=st.card("r-1", "rule", "🔑 שקולים בכוח · $t \\to t^2$ · $t \\to 2^{O(t)}$")
         + st.card("r-2", "rule", "🔑 מקבלת: קיים מסלול מקבל · דוחה: כולם דוחים")
         + st.card("r-3", "trap", "⚠️ מכריעה: כולם עוצרים · החלפה ≠ משלים"))

VIDEO = Video("T06", "tm", "וריאנטים ומכונה אי-דטרמיניסטית", [title, variants, tree, rules, swap, exam, recap],
              bank={"25A-A-Q17": "d"})
