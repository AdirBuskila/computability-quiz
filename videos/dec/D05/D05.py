# -*- coding: utf-8 -*-
"""D05 · הפרש מעורב והצבת ∅ ו-Σ* — video script (build: tools/video/vid.py D05).

Source: tools/courses_src/dec/D05.js (lesson + goal). Exam anchor: 22A-A-Q3 (A ∈ RE∖R, B ∈ R: B = Σ* refutes every
claim), which no guided quiz uses. Not used on purpose: the quiz questions of D05 (the five original ones and
26B-B-Q9), and 23B-A-Q3 / 20A-B-Q3 / 22A-C-Q3 (cited by the lesson).
Every table row and every "necessarily" claim is decided by the course closure engine (rules.claim_truth, with the
4-language model ∅, Σ*, A_TM and its complement).
"""
from vid import P, Scene, Video, show, hide, BANK
from rules import claim_truth, model_classes, Mod
import stage as st
import w_dec

# ---------------------------------------------------------------- the difference table (verified)
DIFF = [("RE", "R", "RE"), ("RE", "coRE", "RE"), ("R", "RE", "coRE")]
for a, b, c in DIFF:
    assert claim_truth("A - B", {"A": a, "B": b}, f"always:{c}")
    other = {"RE": "coRE", "coRE": "RE"}[c]
    assert not claim_truth("A - B", {"A": a, "B": b}, f"always:{other}")
for c in ("R", "RE", "coRE"):                                   # RE ∖ RE: no guarantee at all
    assert not claim_truth("A - B", {"A": "RE", "B": "RE"}, f"always:{c}")

# worked example: A ∈ R, B ∈ coRE -> A∖B ∈ RE; not necessarily decidable, not necessarily undecidable
# (not RE∖coRE: that one is the D07 boss item 26B-A-Q9)
assert claim_truth("A - B", {"A": "R", "B": "coRE"}, "always:RE")
assert model_classes("A - B", {"A": "R", "B": "coRE"}) == {"R", "RE\\R"}

# substitution: B = Σ* empties a difference; A = A_TM, B = ∅ keeps A_TM
E, S, X, CX = 0b00, 0b11, 0b01, 0b10
assert (Mod(X) - Mod(S)).b == E and (Mod(X) - Mod(E)).b == X

# both tools: A ∈ coRE, B ∈ R -> A∖B ∈ coRE always; B = Σ* gives ∅ (R), A = co-A_TM, B = ∅ gives co-A_TM (not R)
assert claim_truth("A - B", {"A": "coRE", "B": "R"}, "always:coRE")
assert not claim_truth("A - B", {"A": "coRE", "B": "R"}, "always:coRE\\R")
assert not claim_truth("A - B", {"A": "coRE", "B": "R"}, "always:R")
assert (Mod(CX) - Mod(S)).b == E and (Mod(CX) - Mod(E)).b == CX

# exam 22A-A-Q3: A ∈ RE∖R, B ∈ R. A = A_TM, B = Σ*: union Σ* (in R), difference ∅ (in R), and A ⊆ B
Q = BANK["22A-A-Q3"]
assert Q["correctId"] == "d"
assert (Mod(X) | Mod(S)).b == S and (Mod(X) - Mod(S)).b == E and (Mod(X) & Mod(S)).b == X
assert not claim_truth("A | B", {"A": "RE\\R", "B": "R"}, "always:RE\\R")
assert not claim_truth("A - B", {"A": "RE\\R", "B": "R"}, "always:RE\\R")
OPTS = [(o["id"], f'${o["value"]}$' if o["type"] == "math" else o["value"]) for o in Q["options"]]

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("בסרטון הזה נפתור את סוג השאלות הנפוץ ביותר בנושא: מה **בהכרח** נכון על הפרש של שתי שפות."),
    P("שני כלים: להפוך הפרש לחיתוך, ולהציב שפות פשוטות כדי להפריך.", hold=0.4),
], stage='<div class="kicker">D05 · כריעות, סגירות וסיווג</div><h1>הפרש מעורב והצבת ∅ ו-Σ*</h1>'
         '<p>לפתור שאלת "מה בהכרח נכון על A∖B" בשני כלים: המרת הפרש לחיתוך עם משלים, והצבת שפות פשוטות כדי להפריך.</p>',
   layout="title")

tool1 = Scene("tool1", "הפרש = חיתוך", [
    P("הכלי הראשון: הפרש הוא חיתוך עם משלים.", do=show("a-f")),
    P("מה שב-$A$ ולא ב-$B$, זה מה שב-$A$ וגם במשלים של $B$."),
    P("והמשלים **הופך כיוון**: מ-$RE$ ל-$coRE$, ומ-$coRE$ ל-$RE$. ו-$R$ נשארת $R$.", do=show("a-1")),
    P("אחרי ההמרה נשארת שאלה על חיתוך, ואת טבלת החיתוך כבר מכירים.", do=show("a-2"), hold=0.4),
], stage='<div class="stack"><div id="a-f" class="bigmath h">$A \\setminus B = A \\cap \\overline{B}$</div></div>',
   panel=st.card("a-1", "rule", "🔑 משלים: $RE \\leftrightarrow coRE$, ו-$R$ נשארת")
         + st.card("a-2", "rule", "🔑 חיתוך של שתי שפות מאותה מחלקה נשאר בה"))

work = Scene("work", "דוגמה", [
    P("דוגמה: $A$ כריעה ו-$B$ ב-$coRE$. מה בהכרח נכון על ההפרש?", do=show("b-0")),
    P("נמיר: $A$ חיתוך המשלים של $B$.", do=show("b-1"), say="נמיר: אֵיי חיתוך המשלים של בִּי."),
    P("$B$ ב-$coRE$, ולכן המשלים שלה ב-$RE$. ו-$A$ כריעה, אז בפרט גם היא ב-$RE$.", do=show("b-2")),
    P("עכשיו זה חיתוך של שתי שפות ב-$RE$. וחיתוך כזה נשאר ב-$RE$.", do=show("b-3")),
    P("אז ההפרש ב-$RE$ בהכרח. אבל לא בהכרח כריע, ולא בהכרח לא כריע.", do=show("b-4"), hold=0.4),
], stage='<div class="stack">'
         '<div id="b-0" class="bigmath h" style="font-size:44px">$A \\in R,\\ \\ B \\in coRE$</div>'
         '<div id="b-1" class="bigmath h" style="font-size:44px">$A \\setminus B = A \\cap \\overline{B}$</div>'
         '<div id="b-2" class="bigmath h" style="font-size:44px">$A \\in RE,\\ \\ \\overline{B} \\in RE$</div>'
         '<div id="b-3" class="bigmath h" style="font-size:44px">$A \\cap \\overline{B} \\in RE$</div>'
         '</div>',
   panel=st.card("b-4", "rule", "🔑 $A \\in R,\\ B \\in coRE \\Rightarrow A \\setminus B \\in RE$"))

TAB = w_dec.table("t", ["$A$", "$B$", "$A \\setminus B$ בהכרח ב-"], [
    ["$RE$", "$R$", "$RE$"],
    ["$RE$", "$coRE$", "$RE$"],
    ["$R$", "$RE$", "$coRE$"],
    ["$RE$", "$RE$", "אין הבטחה"],
], cls="big")
table = Scene("table", "הטבלה", [
    P("באותה דרך ממלאים טבלה שלמה. $A$ ב-$RE$ ו-$B$ כריעה: המשלים של $B$ כריע, וההפרש ב-$RE$.", do=show("t-r0")),
    P("$A$ ב-$RE$ ו-$B$ ב-$coRE$: אותו רעיון כמו בדוגמה, המשלים של $B$ ב-$RE$. ב-$RE$.", do=show("t-r1")),
    P("$A$ כריעה ו-$B$ ב-$RE$: המשלים של $B$ ב-$coRE$, ו-$A$ כריעה ולכן גם היא ב-$coRE$. ההפרש ב-$coRE$.",
      do=show("t-r2")),
    P("ושתיהן ב-$RE$: המשלים של $B$ ב-$coRE$, וחיתוך של $RE$ עם $coRE$ לא מבטיח כלום.", do=show("t-r3", "t-hl3"),
      hold=0.4),
], stage=TAB)

SUBS = w_dec.table("s", ["מה רוצים להפריך", "מה מציבים", "התוצאה"], [
    ["״בהכרח לא כריעה״", "$B = \\Sigma^*$", "$A \\setminus B = \\emptyset$"],
    ["״בהכרח כריעה״", "$A = A_{TM},\\ B = \\emptyset$", "$A \\setminus B = A_{TM}$"],
])
tool2 = Scene("tool2", "הצבה", [
    P("הכלי השני: **הצבה**. הריקה ו-$\\Sigma^*$ כריעות, ולכן הן שייכות ל-$R$, ל-$RE$ ול-$coRE$.", do=show("c-1")),
    P("לכן מותר להציב אותן כשהנתון הוא $R$, $RE$ או $coRE$. כשהנתון הוא ״ב-$RE$ ולא כריעה״, מציבים את $A_{TM}$.",
      do=show("c-2"),
      say="לכן מותר להציב אותן כשהנתון הוא אָר, אָר אִי או קוֹאוּ אָר אִי. כשהנתון הוא באָר אִי ולא כריעה, "
          "מציבים את אֵיי טִי אֶם."),
    P("רוצים להפריך ״בהכרח לא כריעה״? מציבים $B$ שווה $\\Sigma^*$. ההפרש מתרוקן, והריקה כריעה.",
      do=show("s-r0"), say="רוצים להפריך בהכרח לא כריעה? מציבים בִּי שווה סיגמא כוכבית. ההפרש מתרוקן, והריקה כריעה."),
    P("רוצים להפריך ״בהכרח כריעה״? מציבים $A_{TM}$ ב-$A$ והריקה ב-$B$. ההפרש הוא $A_{TM}$ עצמה.", do=show("s-r1"),
      say="רוצים להפריך בהכרח כריעה? מציבים אֵיי טִי אֶם באֵיי והריקה בבִּי. ההפרש הוא אֵיי טִי אֶם עצמה."),
    P("ושימו לב לניסוח: ״בהכרח״ צריך לעבוד בכל הצבה. ״יתכן״ צריך רק דוגמה אחת.", do=show("c-3"), hold=0.4),
], stage=SUBS,
   panel=st.card("c-1", "rule", "🔑 $\\emptyset$, $\\Sigma^*$: מותר כשהנתון $R$, $RE$ או $coRE$")
         + st.card("c-2", "ex", "נתון $RE \\setminus R$? מציבים $A_{TM}$. נתון $coRE \\setminus R$? $\\overline{A_{TM}}$")
         + st.card("c-3", "trap", "⚠️ ״בהכרח״: כל הצבה. ״יתכן״: הצבה אחת"))

both = Scene("both", "שני הכלים יחד", [
    P("נשלב את שני הכלים. $A$ ב-$coRE$ ו-$B$ כריעה. מה בהכרח נכון על ההפרש?", do=show("y-0")),
    P("כלי ראשון: $A$ חיתוך המשלים של $B$. המשלים של כריעה כריע, ולכן גם ב-$coRE$.", do=show("y-1"),
      say="כלי ראשון: אֵיי חיתוך המשלים של בִּי. המשלים של כריעה כריע, ולכן גם בקוֹאוּ אָר אִי."),
    P("חיתוך של שתי שפות $coRE$ נשאר ב-$coRE$. זה מה שבהכרח נכון.", do=show("y-2")),
    P("ואם מישהו טוען ״בהכרח לא כריעה״? כלי שני: $B = \\Sigma^*$, וההפרש ריק.", do=show("y-3"),
      say="ואם מישהו טוען בהכרח לא כריעה? כלי שני: בִּי שווה סיגמא כוכבית, וההפרש ריק."),
    P("ו״בהכרח כריעה״? נציב ב-$A$ את המשלים של $A_{TM}$, וב-$B$ את הריקה. ההפרש לא כריע.", do=show("y-4"),
      say="ובהכרח כריעה? נציב באֵיי את המשלים של אֵיי טִי אֶם, ובבִּי את הריקה. ההפרש לא כריע."),
    P("אז רק ״ב-$coRE$״ שורד. כך פותרים כמעט כל שאלה כזו.", hold=0.4,
      say="אז רק בקוֹאוּ אָר אִי שורד. כך פותרים כמעט כל שאלה כזו."),
], stage='<div class="stack">'
         '<div id="y-0" class="bigmath h" style="font-size:44px">$A \\in coRE,\\ \\ B \\in R$</div>'
         '<div id="y-1" class="bigmath h" style="font-size:44px">$A \\cap \\overline{B},\\ \\ \\overline{B} \\in R \\subseteq coRE$</div>'
         '<div id="y-2" class="bigmath h" style="font-size:44px">$A \\setminus B \\in coRE$</div>'
         '</div>',
   panel=st.card("y-3", "ex", "$B = \\Sigma^*$: $A \\setminus B = \\emptyset \\in R$")
         + st.card("y-4", "ex", "$A = \\overline{A_{TM}},\\ B = \\emptyset$: $A \\setminus B \\notin R$"))

exam = Scene("exam", "שאלה ממבחן", [
    P("שאלה ממבחן: $A$ ב-$RE$ ולא כריעה, ו-$B$ כריעה. איזו טענה נכונה?",
      say="שאלה ממבחן: אֵיי באָר אִי ולא כריעה, ובִּי כריעה. איזו טענה נכונה?"),
    P("כל שלוש הטענות הראשונות אומרות ״בהכרח״. ננסה להפריך את כולן בהצבה אחת.", do=show("x-1")),
    P("$A$ חייבת להיות לא כריעה, אז $A = A_{TM}$. ו-$B$ כריעה: נבחר $B = \\Sigma^*$.", do=show("x-2")),
    P("האיחוד הוא $\\Sigma^*$, כריעה. אז האיחוד לא בהכרח מחוץ ל-$R$.", do=show("x-3", "q-x-a")),
    P("ההפרש ריק, גם הוא כריע. נופלת גם הטענה על ההפרש.", do=show("x-4", "q-x-b")),
    P("ו-$A_{TM}$ מוכלת ב-$\\Sigma^*$, כמו כל שפה. נופלת הטענה ש-$A$ איננה תת-קבוצה של $B$.", do=show("x-5", "q-x-c")),
    P("הצבה אחת הפילה שלוש טענות. התשובה: אף אחת מהן.", do=show("q-ok-d"), hold=0.6),
], stage='<div class="stack">'
         + st.card("x-1", "trap", "⚠️ שלוש טענות ״בהכרח״: מחפשים הצבה שמפילה")
         + '<div id="x-2" class="bigmath h" style="font-size:42px">$A = A_{TM},\\ \\ B = \\Sigma^*$</div>'
         + '<div id="x-3" class="bigmath h" style="font-size:40px">$A \\cup B = \\Sigma^* \\in R$</div>'
         + '<div id="x-4" class="bigmath h" style="font-size:40px">$A \\setminus B = \\emptyset \\in R$</div>'
         + '<div id="x-5" class="bigmath h" style="font-size:40px">$A \\subseteq \\Sigma^* = B$</div>'
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q["id"]}</span>$A \\in RE \\setminus R$ וגם $B \\in R$. '
         'איזו טענה נכונה?</div>'
         + st.options("q", OPTS))

recap = Scene("recap", "סיכום", [
    P("לסיכום: הפרש הוא חיתוך עם המשלים, והמשלים הופך $RE$ ל-$coRE$.", do=show("r-1")),
    P("כך מקבלים: $RE$ פחות כריעה, או פחות $coRE$, נשאר ב-$RE$. כריעה פחות $RE$ נמצאת ב-$coRE$.", do=show("r-2"),
      say="כך מקבלים: אָר אִי פחות כריעה, או פחות קוֹאוּ אָר אִי, נשאר באָר אִי. כריעה פחות אָר אִי נמצאת בקוֹאוּ אָר אִי."),
    P("ולהפרכה: מציבים את הריקה, את $\\Sigma^*$ ואת $A_{TM}$.", do=show("r-3")),
    P("״בהכרח לא כריעה״ כמעט תמיד נופל עם $\\Sigma^*$. נתראה ברמה הבאה.", do=show("r-4"), hold=0.6),
], stage='<div class="stack"><div class="bigmath">$A \\setminus B = A \\cap \\overline{B}$</div></div>',
   panel=st.card("r-1", "rule", "🔑 משלים: $RE \\leftrightarrow coRE$")
         + st.card("r-2", "rule", "🔑 $A \\in RE,\\ B \\in R$ או $coRE \\Rightarrow A \\setminus B \\in RE$")
         + st.card("r-3", "ex", "הצבות: $\\emptyset$, $\\Sigma^*$, $A_{TM}$, $\\overline{A_{TM}}$")
         + st.card("r-4", "trap", "⚠️ ״בהכרח לא כריעה״: נסו $B = \\Sigma^*$"))

VIDEO = Video("D05", "dec", "הפרש מעורב והצבת ∅ ו-Σ*", [title, tool1, work, table, tool2, both, exam, recap],
              bank={"22A-A-Q3": "d"})
