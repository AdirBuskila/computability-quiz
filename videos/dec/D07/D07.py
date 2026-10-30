# -*- coding: utf-8 -*-
"""D07 · מבחן גמר: כריעות, סגירות וסיווג — boss video (build: tools/video/vid.py D07).

Source: tools/courses_src/dec/D07.js (the summary lesson). A boss video solves exam questions that no guided quiz uses
(the six of the D07 boss quiz stay unseen): 24A-B-Q11 (both differences decidable say nothing about A, B),
22B-B-Q2 (complement of R intersected with RE stays in RE), 24B-B-Q13 (ε in L(M1) ∪ L(M2): parallel run on ε, RE;
not decidable by a reduction from A_TM), 20A-A-Q9 (L(M) not empty and not Σ*: neither RE nor coRE).
Not used on purpose: 23A-B-Q9 (its step-bound argument is the one behind boss item 22A-B-Q2), and the "L2∖L1"
reading of 22B-B-Q2 (it is boss item 24B-A-Q2's true option).
Closure claims are decided by the course closure engine (rules.claim_truth, Mod model). The parallel run on ε of
24B-B-Q13 is run with two real machines (run_tm): the first never halts on ε, the second accepts it.
"""
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, REJ, BLANK, run_tm, words
from rules import claim_truth, Mod, FACTS, SHAPES
import stage as st

# ---------------------------------------------------------------- Q1 24A-B-Q11 (verified)
Q1 = BANK["24A-B-Q11"]
assert Q1["correctId"] == "d"
E, S, X, CX = 0b00, 0b11, 0b01, 0b10
assert (Mod(X) - Mod(X)).b == E                            # A = B = A_TM: both differences empty
assert FACTS["A_TM"] == "RE\\R"                            # not in R (a), not in coRE (c)
assert (Mod(E) - Mod(E)).b == E                            # A = B = ∅: both differences empty, ∅ ∉ RE∖R (b)
O1 = [(o["id"], o["value"]) for o in Q1["options"]]

# ---------------------------------------------------------------- Q2 22B-B-Q2 (verified)
Q2 = BANK["22B-B-Q2"]
assert Q2["correctId"] == "b"
assert claim_truth("~A & B", {"A": "R", "B": "RE"}, "always:RE")
assert claim_truth("B - A", {"A": "R", "B": "RE"}, "always:RE")
O2 = [(o["id"], o["value"]) for o in Q2["options"]]

# ---------------------------------------------------------------- Q3 24B-B-Q13 (verified)
Q3 = BANK["24B-B-Q13"]
assert Q3["correctId"] == "a" and FACTS["A_TM"] == "RE\\R"
# the parallel run on ε: M1 runs right forever on ε, M2 accepts ε; alternating single steps accepts
M1 = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): ("q_0", BLANK, "R")}
M2 = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (REJ, "1", "R"), ("q_0", BLANK): (ACC, BLANK, "R")}
assert run_tm(M1, "q_0", "")[0] == "loop" and run_tm(M2, "q_0", "")[:2] == ("accept", 1)
assert next(k for k in range(1, 50) if run_tm(M1, "q_0", "", k + 1)[0] == "accept"
            or run_tm(M2, "q_0", "", k + 1)[0] == "accept") == 1
O3 = [(o["id"], o["value"]) for o in Q3["options"]]

# ---------------------------------------------------------------- Q4 20A-A-Q9 (course facts)
Q4 = BANK["20A-A-Q9"]
assert Q4["correctId"] == "d"
assert FACTS["notE_TM"] == "RE\\R" and FACTS["coALL_TM"] == "none" and SHAPES["specific"] == "none"
O4 = [(o["id"], o["value"]) for o in Q4["options"]]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("זה סרטון ההכנה למבחן הגמר של הקורס: כריעות, סגירות וסיווג."),
    P("נפתור ארבע שאלות אמיתיות ממבחנים, ונראה איפה כל אחת מנסה להפיל.", hold=0.4),
], stage='<div class="kicker">D07 · כריעות, סגירות וסיווג</div><h1>מבחן גמר: כריעות, סגירות וסיווג</h1>'
         '<p>ארבע שאלות אמיתיות מהמבחנים: סגירות, הפרש מעורב, וסיווג של שפות מכונות.</p>', layout="title")

plan = Scene("plan", "איך ניגשים", [
    P("כלל ראשון לכל שאלת ״בהכרח״: קודם מנסים **להפריך**.", do=show("p-1")),
    P("מציבים את הריקה, את $\\Sigma^*$, את $A_{TM}$ ואת המשלים שלה.", do=show("p-2")),
    P("וכלל שני לשאלות סיווג: שואלים מה מספיק לראות כדי לענות כן, ומה כדי לענות לא.", do=show("p-3"), hold=0.4),
], stage='<div class="stack">'
         + st.card("p-1", "rule", "🔑 ״בהכרח״? קודם מפריכים")
         + st.card("p-2", "ex", "הצבות: $\\emptyset$, $\\Sigma^*$, $A_{TM}$, $\\overline{A_{TM}}$")
         + st.card("p-3", "rule", "🔑 סיווג: עדות סופית ל״כן״? ל״לא״?")
         + "</div>")

q1 = Scene("q1", "שאלה 1: סגירות", [
    P("שאלה ראשונה: שני ההפרשים, $A$ פחות $B$ ו-$B$ פחות $A$, כריעים. מה בהכרח נכון?",
      say="שאלה ראשונה: שני ההפרשים, אֵיי פחות בִּי ובִּי פחות אֵיי, כריעים. מה בהכרח נכון?"),
    P("שוב, נתונה רק התוצאה. ננסה להפריך.", do=show("a-1")),
    P("מה מרוקן את שני ההפרשים בבת אחת? לבחור $A$ ו-$B$ **שוות**.", do=show("a-2")),
    P("נבחר את שתיהן $A_{TM}$. שני ההפרשים ריקים, והריקה כריעה. הנתון מתקיים.", do=show("a-3")),
    P("אבל $A_{TM}$ לא כריעה, ולא ב-$coRE$. נפלו שתי טענות.", do=show("o1-x-a", "o1-x-c")),
    P("ואם שתיהן הריקה? שוב שני ההפרשים ריקים, והריקה כריעה, לא מחוץ ל-$R$. נפלה גם השלישית.",
      do=show("a-4", "o1-x-b")),
    P("התשובה: אף אחת מהטענות.", do=show("o1-ok-d"), hold=0.5),
], stage='<div class="stack">'
         + st.card("a-1", "trap", "⚠️ נתונה התוצאה: מפריכים בהצבה")
         + st.card("a-2", "plain", "$A = B$ ⇐ $A \\setminus B = B \\setminus A = \\emptyset$")
         + '<div id="a-3" class="bigmath h" style="font-size:42px">$A = B = A_{TM}$</div>'
         + '<div id="a-4" class="bigmath h" style="font-size:42px">$A = B = \\emptyset$</div>'
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q1["id"]}</span>$B \\setminus A \\in R$ וגם $A \\setminus B \\in R$. '
         'איזו טענה נכונה?</div>' + st.options("o1", O1))

q2 = Scene("q2", "שאלה 2: הפרש מעורב", [
    P("שאלה שנייה: $L_1$ כריעה ו-$L_2$ ב-$RE$. האם החיתוך של המשלים של $L_1$ עם $L_2$ ב-$RE$?",
      say="שאלה שנייה: אֵל אחת כריעה ואֵל שתיים באָר אִי. האם החיתוך של המשלים של אֵל אחת עם אֵל שתיים באָר אִי?"),
    P("שלוש אפשרויות: אף פעם, תמיד, או תלוי בשפות."),
    P("המשלים של שפה כריעה כריע, ולכן גם ב-$RE$.", do=show("b-1")),
    P("ועכשיו זה חיתוך של שתי שפות ב-$RE$, ו-$RE$ סגורה לחיתוך.", do=show("b-2")),
    P("אז הטענה נכונה תמיד.", do=show("o2-ok-b", "o2-x-a")),
    P("המלכודת היא ״יכול להיות״: סגירות נותנת תשובה לכל השפות, לא רק לחלק.", do=show("o2-x-c", "o2-n-c"), hold=0.5),
], stage='<div class="stack">'
         + '<div id="b-1" class="bigmath h" style="font-size:42px">$\\overline{L_1} \\in R \\subseteq RE$</div>'
         + '<div id="b-2" class="bigmath h" style="font-size:42px">$\\overline{L_1} \\cap L_2 \\in RE$</div>'
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q2["id"]}</span>אם $L_1 \\in R$ ו-$L_2 \\in RE$, '
         'אזי $\\overline{L_1} \\cap L_2 \\in RE$</div>' + st.options("o2", O2, notes={"c": "סגירות: תמיד"}))

q3 = Scene("q3", "שאלה 3: סיווג", [
    P("שאלה שלישית: זוגות של שתי מכונות, כך שהמילה הריקה בשפה של לפחות אחת מהן."),
    P("כדי לענות כן, מספיק לראות שאחת מהן מקבלת את המילה הריקה. זו עדות סופית.", do=show("c-1")),
    P("אבל אם נריץ קודם את $M_1$ והיא תרוץ לנצח, לעולם לא נגיע ל-$M_2$.", do=show("c-2")),
    P("לכן מריצים את שתיהן על המילה הריקה לסירוגין, ומקבלים כשאחת קיבלה. השפה ב-$RE$.", do=show("c-3")),
    P("והיא לא כריעה. את זה מוכיחים ברדוקציה מ-$A_{TM}$.", do=show("c-4")),
    P("לכל זוג של מכונה ומילה בונים מכונה שמתעלמת מהקלט שלה, מריצה את $M$ על $w$, ועונה כמוה.", do=show("c-5")),
    P("היא מקבלת את המילה הריקה בדיוק כש-$M$ מקבלת את $w$. אילו השפה הייתה כריעה, גם $A_{TM}$ הייתה כריעה.",
      do=show("o3-ok-a")),
    P("אז ניתנת לקבלה ולא כריעה. והאחרות נופלות: היא כן ניתנת לקבלה, ולא כריעה.",
      do=show("o3-x-b", "o3-x-c", "o3-x-d"), hold=0.5),
], stage='<div class="stack">'
         + st.card("c-1", "ex", "✓ כן: אחת מקבלת את $\\varepsilon$, עדות סופית")
         + st.card("c-2", "trap", "⚠️ בזו אחר זו: נתקעים בלולאה של $M_1$")
         + st.card("c-3", "rule", "🔑 לסירוגין על $\\varepsilon$ ⇐ $RE$")
         + st.card("c-4", "rule", "🔑 לא כריעה: רדוקציה מ-$A_{TM}$")
         + st.card("c-5", "ex", "$K$: מתעלמת מהקלט, מריצה את $M$ על $w$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q3["id"]}</span>'
         '$L = \\{\\langle M_1, M_2\\rangle \\mid \\varepsilon \\in L(M_1) \\cup L(M_2)\\}$. איזו טענה נכונה?</div>'
         + st.options("o3", O3, notes={"b": "מכונה עלולה לא לעצור"}))

q4 = Scene("q4", "שאלה 4: שני תנאים", [
    P("שאלה אחרונה: מכונות שהשפה שלהן לא ריקה, וגם לא כל $\\Sigma^*$."),
    P("שתי השאלות. כדי לענות כן, צריך מילה שמתקבלת: את זה אפשר לראות.", do=show("d-1")),
    P("אבל צריך גם מילה שלא מתקבלת. ו״לא מתקבלת״ כולל גם ריצה אינסופית, שאותה אי אפשר לראות בזמן סופי.",
      do=show("d-2")),
    P("וכדי לענות לא? השפה ריקה, או שהיא כל $\\Sigma^*$. שני אלה תנאי ״לכל״, בלי עדות סופית.", do=show("d-3")),
    P("אין עדות סופית לאף צד. זו האינטואיציה, וההוכחה היא ברדוקציה מהמשלים של $H_{TM}$, לשפה ולמשלים שלה.",
      say="אין עדות סופית לאף צד. זו האינטואיציה, וההוכחה היא ברדוקציה מהמשלים של אֵייץ' טִי אֶם, לשפה ולמשלים שלה."),
    P("אז השפה לא ניתנת לקבלה, וגם המשלים שלה לא.", do=show("o4-ok-d")),
    P("המלכודת: לראות רק את ״לא ריקה״, שהיא $RE$, ולשכוח את החצי השני.",
      do=show("o4-x-a", "o4-x-b", "o4-x-c", "o4-n-b"), hold=0.5),
], stage='<div class="stack">'
         + st.card("d-1", "ex", "$L(M) \\ne \\emptyset$: מילה מתקבלת, עדות סופית")
         + st.card("d-2", "trap", "$L(M) \\ne \\Sigma^*$: מילה שלא מתקבלת, אולי בלולאה")
         + st.card("d-3", "trap", "״לא״: $L(M) = \\emptyset$ או $L(M) = \\Sigma^*$, שניהם ״לכל״")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q4["id"]}</span>'
         '$L = \\{\\langle M\\rangle \\mid L(M) \\ne \\emptyset,\\ L(M) \\ne \\Sigma^*\\}$</div>'
         + st.options("o4", O4, notes={"b": "רק ״לא ריקה״"}))

recap = Scene("recap", "סיכום", [
    P("לסיכום: כשנתונה רק תוצאה, מפריכים בהצבה. שתי שפות שוות מרוקנות את שני ההפרשים.", do=show("r-1")),
    P("הפרש מעורב: הופכים לחיתוך עם משלים, ובודקים בטבלה.", do=show("r-2")),
    P("ובסיווג: ״קיים״ בודקים בהרצה לסירוגין, ואי-שייכות מוכיחים ברדוקציה.", do=show("r-3")),
    P("בהצלחה במבחן הגמר!", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$R = RE \\cap coRE$</div></div>',
   panel=st.card("r-1", "rule", "🔑 $A = B$: שני ההפרשים ריקים")
         + st.card("r-2", "rule", "🔑 $A \\setminus B = A \\cap \\overline{B}$")
         + st.card("r-3", "rule", "🔑 ״קיים״ ⇐ לסירוגין. ״לא שייכת״ ⇐ רדוקציה")
         + st.card("r-4", "ex", "🏆 בהצלחה!"))

VIDEO = Video("D07", "dec", "מבחן גמר: כריעות, סגירות וסיווג", [title, plan, q1, q2, q3, q4, recap],
              bank={"24A-B-Q11": "d", "22B-B-Q2": "b", "24B-B-Q13": "a", "20A-A-Q9": "d"})
