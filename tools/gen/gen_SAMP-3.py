# -*- coding: utf-8 -*-
"""Generator for tools/raw/SAMP-3.json. Source (question paper + key in one file):
`מבחנים/מבחנים לדוגמה/פתרון מבחן לדוגמא.pdf` (2021 sample, two one-hour parts; numbering
restarts in part B). Key = cyan highlight on the correct option (part A Q1-9, part B Q1-4);
part B Q5 (DOUBLE-CLIQUE) has 7 true/false claims א-ז answered in blue text ("לא." / "כן.")
under each claim. Explanations = the blue text.
Numbered here sequentially 1..20 in printed order; original numbering is in `note`.
Run: PYTHONUTF8=1 py tools/gen/gen_SAMP-3.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "SAMP-3.json"
IDS = "abcdef"

def opts(*vals):
    """vals: str (rich text) or ('math', tex) / ('image', path)."""
    out = []
    for i, v in enumerate(vals):
        if isinstance(v, tuple):
            out.append({"id": IDS[i], "type": v[0], "value": v[1]})
        else:
            out.append({"id": IDS[i], "type": "text", "value": v})
    return out

YESNO = opts("כן", "לא")
TF = opts("נכון", "לא נכון")
NONE = "אף תשובה אינה נכונה."

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "highlighted-pdf", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

contexts = {
  "rel": {"kind": "text", "title": "יחסים בין שפות (חלק א, שאלות 3–5)",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  r"$$A = \{L \mid L \le_m A_{TM}\}$$"
                  r"$$B = \{L \mid \overline{L} \le_m A_{TM}\}$$"
                  r"$$C = \{L \mid A_{TM} \le_m L \wedge L \le_m A_{TM}\}$$"},
  "map": {"kind": "text", "title": "רדוקציית מיפוי (חלק א, שאלות 6–9)",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  "**שפות:**\n"
                  r"$$H_{TM} = \{\langle M, w\rangle \mid (*)\}$$"
                  "(*): $M$ עוצרת על $w$\n"
                  r"$$NotEmpty_{TM} = \{\langle M\rangle \mid L(M) \ne \emptyset\}$$"
                  r"$$INF_{TM} = \{\langle M\rangle \mid (**)\}$$"
                  "(**): $L(M)$ אינסופית\n"
                  "**פונקציות מיפוי:**\n"
                  r"$$f(\langle M, w\rangle) = \langle R_{Mw}\rangle \qquad g(\langle M\rangle) = \langle T_M\rangle$$"
                  "כאשר המכונות $R_{Mw}$ ו-$T_M$ מוגדרות באופן הבא:\n"
                  "$R_{Mw}$ על קלט $y$:\n"
                  "1. הרץ את $M$ על $w$ למשך $|y|$ צעדים\n"
                  "2. אם בשלב 1 המכונה $M$ עצרה על $w$: **קבל**; אחרת: **דחה**\n"
                  "$T_M$ על קלט $y$:\n"
                  "1. הרץ את $M$ על כל המילים שאורכן לכל היותר $|y|$ למשך $|y|$ צעדים\n"
                  "2. אם בשלב 1 המכונה $M$ קיבלה לפחות מילה אחת: **קבל**; אחרת: **דחה**\n"
                  "**ענה על השאלות הבאות**"},
  "dc": {"kind": "text", "title": "רדוקציה פולינומית: DOUBLE-CLIQUE (חלק ב, שאלה 5)",
         "text": "נתונה שפה DOUBLE-CLIQUE הבאה:\n"
                 r"$$DOUBLE{-}CLIQUE = \{\langle G, k\rangle \mid (*)\}$$"
                 "(*): $G$ גרף לא מכוון, ב-$G$ יש שתי קליקות זרות בקדקדים בגודל $k$\n"
                 r"מנסים להוכיח שהשפה היא NP-שלמה בעזרת הרדוקציה $CLIQUE \le_p DOUBLE{-}CLIQUE$, "
                 r"המתבססת על המיפוי $f(\langle G, k\rangle) = \langle G', k\rangle$ כאשר:" "\n"
                 "אם ב-$G$ יש קליקה בגודל $k$, אז $G'$ הוא גרף המכיל שני עותקים של $G$, בלי שום חיבורים ביניהם,\n"
                 "אחרת $G'$ זהה ל-$G$.\n"
                 "**לפניך מספר טענות. עליך לסמן לכל טענה האם היא נכונה או לא.**"},
}

questions = [
Q(1, "np",
  r"תהיה $A, B \in NP$. איזו מהטענות הבאות לגבי $A - B$ נכונה?",
  opts(r"אם $B \in P$ אז $A - B \in NP$ ואם $B \notin P$ אז ייתכן $A - B \in NP$ וייתכן $A - B \notin NP$.",
       r"אם $B \in P$ אז $A - B \in NP$ ואם $B \notin P$ אז בהכרח $A - B \notin NP$.",
       r"אם $B \in P$ אז ייתכן $A - B \in NP$ וייתכן $A - B \notin NP$.",
       NONE),
  "a",
  r"אם $B \in P$ אז $\overline{B} \in P$ ולכן $\overline{B} \in NP$. $A - B = A \cap \overline{B}$. NP סגורה לחיתוך ולכן $A - B \in NP$." "\n"
  "כלומר ג לא נכון.\n"
  r"בנוסף, אם $B \notin P$ אז לא ניתן לקבוע האם $A - B \in NP$ או לא:" "\n"
  r"בפרט, ייתכן שמתקיים $A = B$ ואז $A - B = \emptyset \in P$." "\n"
  "לכן א נכון וב לא נכון.",
  note="Original: חלק א שאלה 1."),

Q(2, "decidability",
  "תהא $M$ מ\"ט דטרמיניסטית ותהא $M'$ המכונה שמתקבלת מ-$M$ ע\"י כך שמחליפים בין המצבים $q_{rej}$ ו-$q_{acc}$. "
  "איזו מהטענות הבאות נכונה?",
  opts(r"בהכרח מתקיים: אם $L(M) \in R$ אז $L(M') \in R$.",
       r"בהכרח מתקיים: $L(M) \ne L(M')$.",
       r"ייתכן ש-$L(M) \in RE$ אבל $L(M') \notin RE$.",
       "כל התשובות נכונות.",
       NONE),
  "e",
  "אף תשובה אינה נכונה\n"
  r"**א לא נכונה:** $M$ מכונה שעל קלט $\langle N, w\rangle$ מריצה את $N$ על $w$ ואם $N$ עוצרת, אז $M$ דוחה. "
  r"במקרה כזה $L(M) = \emptyset \in R$ אבל $L(M') = H_{TM}$." "\n"
  r"**ב לא נכונה:** למשל $M = M_{loop}$" "\n"
  r"**ג לא נכונה:** לא ייתכן שיתקיים $L(M') \notin RE$ כי **בהגדרה**, כל שפה של מכונה **כלשהי** שייכת ל-RE.",
  lockOrder=True,
  note="Original: חלק א שאלה 2. Option ד ('כל התשובות נכונות') refers to siblings -> lockOrder."),

Q(3, "mapping_reductions", "קבע מהו היחס בין $A$ ל-$B$:",
  opts(("math", "A = B"), ("math", r"A \subset B"), ("math", r"A \supset B"),
       ("math", r"A \cap B = \emptyset"), "אף תשובה אינה נכונה"),
  "e",
  r"מתקיים $B \not\ni A_{TM} \in A, C$ וכן $B \ni \overline{A_{TM}} \notin A, C$" "\n"
  r"לכן $B$ לא מוכלת ולא מכילה את $A$ או את $C$. כלומר: $A \not\subseteq B$, $B \not\subseteq A$, $C \not\subseteq B$, $B \not\subseteq C$." "\n"
  r"כמו כן, $A \cap B \ne \emptyset$ מכיוון ש-$R \subseteq A \cap B$ (למעשה $R = A \cap B$)",
  contextId="rel",
  note="Original: חלק א שאלה 3. Explanation = the shared blue box printed above Q3-5 (first bullet); key box text says 'את A או את B' — typo for C, fixed."),

Q(4, "mapping_reductions", "קבע מהו היחס בין $B$ ל-$C$:",
  opts(("math", "B = C"), ("math", r"B \subset C"), ("math", r"B \supset C"), "אף תשובה אינה נכונה"),
  "d",
  r"מתקיים $B \not\ni A_{TM} \in A, C$ וכן $B \ni \overline{A_{TM}} \notin A, C$" "\n"
  r"לכן $B$ לא מוכלת ולא מכילה את $A$ או את $C$. כלומר: $A \not\subseteq B$, $B \not\subseteq A$, $C \not\subseteq B$, $B \not\subseteq C$.",
  contextId="rel",
  note="Original: חלק א שאלה 4. Explanation = first bullet of the shared blue box above Q3-5."),

Q(5, "mapping_reductions", "קבע מהו היחס בין $C$ ל-$A$:",
  opts(("math", "A = C"), ("math", r"A \subset C"), ("math", r"A \supset C"), "אף תשובה אינה נכונה"),
  "c",
  r"לכל $L \in C$ מתקיים $L \le_m A_{TM}$ לכן $L \in A$ כלומר $C \subseteq A$." "\n"
  r"כמו כן, $\{0\} \in A$ אבל $\{0\} \notin C$ ולכן $C \subsetneq A$.",
  contextId="rel",
  note="Original: חלק א שאלה 5. Explanation = second bullet of the shared blue box above Q3-5."),

Q(6, "mapping_reductions", r"האם $f$ היא רדוקציה $H_{TM} \le_m NotEmpty_{TM}$?",
  YESNO, "a",
  "$f$ ניתנת לחישוב. כמו כן:\n"
  r"אם $\langle M, w\rangle \in H_{TM}$ אז קיים מספר צעדים סופי כלשהו $r$ שלאחריו $M$ עוצרת על $w$. "
  r"ולכן קיימת מילה $y$ כך ש-$|y| = r$ ואז $R_{Mw}$ יקבל את $y$, ולכן $\langle R_{Mw}\rangle \in NotEmpty_{TM}$." "\n"
  r"אם $\langle R_{Mw}\rangle \in NotEmpty_{TM}$, אזי קיימת מילה $y$ ש-$R_{Mw}$ מקבלת. משמעות הדבר היא ש-$M$ עוצרת על $w$ "
  r"אחרי $|y|$ צעדים או פחות, ובפרט $M$ עוצרת על $w$, ולכן $\langle M, w\rangle \in H_{TM}$.",
  contextId="map", note="Original: חלק א שאלה 6."),

Q(7, "mapping_reductions", r"האם $f$ היא רדוקציה $H_{TM} \le_m INF_{TM}$?",
  YESNO, "a",
  "$f$ ניתנת לחישוב. כמו כן\n"
  r"אם $\langle M, w\rangle \in H_{TM}$, אז קיים מספר צעדים סופי כלשהו $r$ שלאחריו $M$ עוצרת על $w$. "
  r"ולכן קיימת מילה $y$ כך ש-$|y| = r$ ואז $R_{Mw}$ תקבל את $y$. בנוסף $R_{Mw}$ תקבל את **כל המילים** שאורכן גדול מ-$y$. "
  r"יש אין סוף מילים כאלו, ולכן $\langle R_{Mw}\rangle \in INF_{TM}$." "\n"
  r"אם $\langle M, w\rangle \notin H_{TM}$, אז $M$ לא עוצרת על $w$ בשום מספר של צעדים. כלומר לכל $y$, המכונה $M$ לא עוצרת על $w$ "
  r"בתוך $|y|$ צעדים ולכן $R_{Mw}$ לא מקבלת אף מילה ומתקיים $L(R_{Mw}) = \emptyset$ ואז $\langle R_{Mw}\rangle \notin INF_{TM}$.",
  contextId="map", note="Original: חלק א שאלה 7."),

Q(8, "mapping_reductions", r"האם $g$ היא רדוקציה $NotEmpty_{TM} \le_m INF_{TM}$?",
  YESNO, "a",
  "$g$ ניתנת לחישוב. כמו כן\n"
  r"אם $\langle M\rangle \in NotEmpty_{TM}$ אזי קיימת לפחות מילה אחת $w$ ש-$M$ מקבלת. נגדיר את האורך שלה $|w| = r$. "
  r"$g(\langle M\rangle) = \langle T_M\rangle$ ולפי הגדרה $T_M$ תקבל כל מילה $y$ שמקיימת $|y| \ge r$. "
  r"קיימות אין סוף מילים כאלה. ולכן $L(T_M)$ אינסופית, כלומר $\langle T_M\rangle \in INF_{TM}$." "\n"
  r"אם $\langle M\rangle \notin NotEmpty_{TM}$ אז $L(M) = \emptyset$, כלומר $M$ לא מקבלת אף מילה ולכן גם $T_M$ לא מקבלת אף מילה, "
  r"כלומר $L(T_M) = \emptyset$ ומתקיים $\langle T_M\rangle \notin INF_{TM}$.",
  contextId="map", note="Original: חלק א שאלה 8."),

Q(9, "mapping_reductions", r"האם $g$ היא רדוקציה $INF_{TM} \le_m NotEmpty_{TM}$?",
  YESNO, "b",
  r"$g$ ניתנת לחישוב. אבל יכולה להיות $\langle M\rangle \notin INF_{TM}$ אבל $\langle T_M\rangle \in NotEmpty_{TM}$." "\n"
  "לדוגמא:\n"
  r"$M$ מכונה שמקבלת רק את מילה אחת. ברור ש-$\langle M\rangle \notin INF_{TM}$ אבל $T_M$ מקבלת את כל המילים שהן \"ארוכות מספיק\": "
  "(לפחות באורך של המילה ש-$M$ מקבלת וגם לפחות באורך של מספר הצעדים שלוקח ל-$M$ לקבל את המילה ההיא). "
  r"ולכן $\langle T_M\rangle \in NotEmpty_{TM}$. סה\"כ, זו לא רדוקציה.",
  contextId="map", note="Original: חלק א שאלה 9."),

Q(10, "poly_reductions",
  r"תהינה $A$ ו-$B$ שפות כך שמתקיים $A \le_p B$ וגם $B \le_p A$. מה מהבאים **לא** ייתכן?",
  opts(r"$A \in R$ ו-$B \notin RE$",
       r"$A \in RE$ ו-$B \notin R$",
       r"$A \in P$ ו-$B \in NP$",
       r"$A$ סופית ו-$B$ אינסופית"),
  "a",
  r"**א:** רדוקציה פולינומית היא בפרט רדוקציית מיפוי. לכן מתקיים $A \le_m B$ וגם $B \le_m A$." "\n"
  r"$B \le_m A$, לכן אם $A \in R$ אז $B \in R$ ולכן לא ייתכן שמתקיים $A \in R$ ו-$B \notin RE$." "\n"
  "תשובות ב, ג, ד לא נכונות (כלומר המקרים שמתוארים בהם **ייתכנו**):\n"
  r"**ב.** ייתכן $A \in RE$ וגם $B \notin R$: למשל, $A = B = H_{TM}$" "\n"
  r"**ג.** ייתכן $A \in P$ וגם $B \in NP$: למשל $A = B = \{0\}$" "\n"
  r"**ד.** ייתכן $A$ סופית ו-$B$ אינסופית: למשל $A = \{0\}$, $B = 0^*$.",
  note="Original: חלק ב שאלה 1. Stem prints capital-P subscripts ('≤_P'); written as \\le_p."),

Q(11, "decidability",
  "רוצים להוכיח ששפה $A$ ניתנת להכרעה. מה מהבאים יכול להוות הוכחה תקפה?",
  opts(r"מתקיים $A \le_m \overline{A}$ וגם $A \le_m A_{TM}$",
       "קיים אנומרטור (מ\"ט מונה) שמדפיס כל מילה של $A$ פעם אחת בדיוק",
       r"קיים אנומרטור (מ\"ט מונה) שמדפיס את כל המילים של $\overline{A}$",
       r"מתקיים $A \le_m \overline{A}$ וגם $A_{TM} \le_m A$"),
  "a",
  "**א.** נראה שאם מתקיימים התנאים בתשובה א' אזי בהכרח $A$ ניתנת להכרעה:\n"
  r"אם $A \le_m A_{TM}$ אז $A \in RE$." "\n"
  r"כעת, אם $A \le_m \overline{A}$ אז $\overline{A} \le_m A$ ומכיוון ש-$A \in RE$ אז $\overline{A} \in RE$." "\n"
  r"סה\"כ: $A, \overline{A} \in RE$, ולפי משפט, $A \in R$." "\n"
  "תשובות ב, ג, ד לא נכונות:\n"
  "**ב.** כל אנומרטור ניתן להפוך לאנומרטור שמדפיס כל מילה רק פעם אחת (לפני שהוא מדפיס מילה, הוא ייבדוק שהיא עדיין לא מופיעה "
  "על סרט ההדפסה, ורק אם היא לא מופיעה - הוא ידפיס אותה). לכן, קיומו של כזה אנומרטור לא מעיד על כך ש-$A \\in R$.\n"
  r"**ג.** אם קיים אנומרטור שמדפיס את כל המילים ב-$\overline{A}$, אזי $\overline{A}$ ניתנת לקבלה. אבל $A$ עצמה יכולה להיות "
  r"לא-ניתנת לקבלה (עם משלימה, $\overline{A}$, שכן ניתנת לקבלה)." "\n"
  r"**ד.** אם $A_{TM} \le_m A$ אז מתקיים דווקא $A \notin R$",
  note="Original: חלק ב שאלה 2. Overlines verified on a zoomed render (text layer drops them)."),

Q(12, "time_p",
  r"תהי $f$ פונקציה המוגדרת באופן הבא: הקלט הוא שלשה $\langle M, x, 1^k\rangle$ כאשר: "
  r"$M$ היא מ\"ט בסיסית, $x \in \Sigma^*$ היא מילה ו-$1^k$ הוא קידוד אונארי של מספר טבעי $k \ge 1$." "\n"
  r"וכן: אם $M$ מקבלת את $x$ בתוך לכל היותר $k$ צעדים, אז $f(\langle M, x, 1^k\rangle) = 1$" "\n"
  r"אחרת, $f(\langle M, x, 1^k\rangle) = 0$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts("הפונקציה $f$ ניתנת לחישוב בזמן פולינומיאלי.",
       "הפונקציה $f$ ניתנת לחישוב, אבל לא בהכרח בזמן פולינומיאלי.",
       "הפונקציה $f$ לא ניתנת לחישוב.",
       r"הפונקציה $f$ ניתנת לחישוב רק אם מתקיים $L(M) \in R$."),
  "a",
  "ניתן לבנות מ\"ט שמחשבת את $f$ באמצעות מ\"ט אוניברסלית שמריצה את $M$ מספר צעדים $k$.\n"
  "כל צעד בסימולציה לוקח לכל היותר כמות פולינומיאלית של צעדים כפונקציה של $|x|$. ובסך הכל מספר הצעדים הינו לינארי באורך הקלט "
  "ולכן סך כל מספר הצעדים הנדרשים לחישוב $f$ הוא פולינומיאלי באורך הקלט.",
  note="Original: חלק ב שאלה 3. Key text says 'מ\"ט שמחשבת את M' — typo for f, fixed."),

Q(13, "decidability",
  r"תהי $M_1, M_2, M_3, \cdots$ קבוצה אינסופית של מכונות טיורינג שעוצרות תמיד." "\n"
  r"**טענה:** קיימת מ\"ט $MI$ שעוצרת תמיד ומקיימת: $(\exists i : w \in L(M_i)) \Leftrightarrow w \in L(MI)$." "\n"
  "מה מהבאים נכון?",
  opts("הטענה לא נכונה.", "הטענה נכונה.",
       r"הטענה נכונה רק אם לכל $i$ מתקיים $L(M_i) \in R$.", NONE),
  "a",
  "הטענה לא נכונה.\n"
  r"נסמן $H_{TM} = \{x_1, x_2, x_3, \cdots\}$" "\n"
  "$M_i$ היא מכונה שמקבלת רק את המילה $x_i$ ועל כל שאר המילים היא עוצרת ודוחה.\n"
  r"כל המכונות $M_1, M_2, M_3, \cdots$ עוצרות תמיד." "\n"
  "אילו הייתה קיימת מכונה $MI$ כמתואר, אז $MI$ היתה מכריעה את $H_{TM}$. אבל זה לא ייתכן.",
  note="Original: חלק ב שאלה 4."),
]

# Part B Q5: seven true/false claims about the proposed reduction.
DC = [
  ("א", "ההוכחה תקיפה כי הפונקציה $f$ עומדת בכל הדרישות של רדוקציה פולינומית.", "b",
   "לא. זה לא ידוע, כי לצורך החישוב של $f$ יש לבדוק האם יש בגרף קליקה בגודל נתון ולא ידוע האם זה ניתן לביצוע בסיבוכיות פולינומית."),
  ("ב", r"ההוכחה אינה תקיפה כי $f$ לא מבצעת מיפוי $\Sigma^* \to \Sigma^*$.", "b",
   r"לא. כן מתבצע מיפוי $\Sigma^* \to \Sigma^*$, אבל זו לא דרישה של רדוקציה."),
  ("ג", "ההוכחה אינה תקיפה כי $f$ אינה ניתנת לחישוב.", "b",
   "לא. $f$ כן ניתנת לחישוב."),
  ("ד", "ההוכחה אינה תקיפה כי לא מובטח ש-$f$ ניתנת לחישוב בזמן פולינומי.", "a",
   "כן."),
  ("ה", "ההוכחה אינה תקיפה כי $f$ ניתנת לחישוב בזמן פולינומי על מכונה רב-סרטית אך לא בהכרח על מכונה חד-סרטית.", "b",
   "לא. אילו $f$ היתה ניתנת לחישוב בזמן פולינומי על מכונה רב-סרטית אזי היא היתה ניתנת לחישוב בזמן פולינומי גם על מכונה חד-סרטית"),
  ("ו", r"ההוכחה אינה תקיפה כי לא מתקיים $\langle G', k\rangle \in DOUBLE{-}CLIQUE \Longleftarrow \langle G, k\rangle \in CLIQUE$.", "b",
   r"לא. כן מתקיים $\langle G', k\rangle \in DOUBLE{-}CLIQUE \Longleftarrow \langle G, k\rangle \in CLIQUE$."),
  ("ז", r"ההוכחה אינה תקיפה כי לא מתקיים $\langle G', k\rangle \in DOUBLE{-}CLIQUE \Longrightarrow \langle G, k\rangle \in CLIQUE$.", "b",
   r"לא. כן מתקיים $\langle G', k\rangle \in DOUBLE{-}CLIQUE \Longrightarrow \langle G, k\rangle \in CLIQUE$."),
]
for i, (letter, claim, ans, expl) in enumerate(DC):
    note = f"Original: חלק ב שאלה 5, טענה {letter}. Key = blue answer text under the claim ('לא.'/'כן.'), not a highlight."
    if letter in "וז":
        note += (" Implication arrow transcribed in the visual left-to-right order of the printed formula "
                 "(math spans inside an RTL line); both directions actually hold, so the answer is order-independent.")
    questions.append(Q(14 + i, "poly_reductions", claim, TF, ans, expl, contextId="dc",
                       answerSource="solution-pdf", note=note))

def _unescape(o):
    """raw strings keep '\\"' literally (e.g. מ\\"ט) -> plain '"'."""
    if isinstance(o, str): return o.replace('\\"', '"')
    if isinstance(o, list): return [_unescape(x) for x in o]
    if isinstance(o, dict): return {k: _unescape(v) for k, v in o.items()}
    return o
questions = _unescape(questions)
contexts = _unescape(contexts)

exam = {
  "examCode": "SAMP-3",
  "examLabel": "מבחן לדוגמה 3 (2021)",
  "year": 2021,
  "sourceFile": "מבחנים/מבחנים לדוגמה/פתרון מבחן לדוגמא.pdf",
  "keyFile": "same file (cyan highlights + blue explanations; part B Q5 claims answered in blue text)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 21))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
