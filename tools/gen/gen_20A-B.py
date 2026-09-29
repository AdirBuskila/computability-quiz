# -*- coding: utf-8 -*-
"""Generator for tools/raw/20A-B.json. Transcribed by hand from the rendered pages of
`מבחנים/2020/סמסטר א/2020-03-11-Exam-חישוביות-2020-moedB-גרסא-0 SOLUTION.pdf` (key = yellow
highlight, explanations = red text). Q21 omitted: the solution's red box says "אף תשובה אינה נכונה"
but no such option exists (ASK_ADIR). Run: PYTHONUTF8=1 py tools/gen/gen_20A-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20A-B.json"
IDS = "abcde"

def opts(*vals):
    """vals: str (rich text) or ('math', tex) / ('image', path)."""
    out = []
    for i, v in enumerate(vals):
        if isinstance(v, tuple):
            out.append({"id": IDS[i], "type": v[0], "value": v[1]})
        else:
            out.append({"id": IDS[i], "type": "text", "value": v})
    return out

TF = opts("נכון", "לא נכון")
YN = opts("כן", "לא")
DEC4 = opts(
    "$L$ ניתנת להכרעה.",
    "$L$ ניתנת לקבלה אבל לא ניתנת להכרעה.",
    r"$L$ לא ניתנת לקבלה אבל $\overline{L}$ כן ניתנת לקבלה.",
    r"$L$ לא ניתנת לקבלה וגם $\overline{L}$ לא ניתנת לקבלה.",
)
NONE = "אף תשובה אינה נכונה"

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "highlighted-pdf", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

TFHEAD = "קבע האם הטענה הבאה נכונה או לא:\n"

questions = [
# ---- שאלות נכון / לא-נכון ----
Q(1, "closure", TFHEAD + r"אם $A \subseteq B \subseteq C$ וגם $A, C \in R$, אז $B \in R$.", TF, "b",
  r"**דוגמה:** $C = \Sigma^*$, $B = A_{TM}$, $A = \emptyset$."),

Q(2, "npc", TFHEAD + r"תחת ההנחה $P = NP$: אם $A, B \in NPC$ אז $A \cup B \in NPC$.", TF, "b",
  r"**דוגמה:** $A = SAT$, $B = \overline{A}$." "\n"
  r"אם $NP = P$ אזי $B \in NP$, $B \in P$ (כי $P$ סגורה למשלים) כמו כן $SAT \le_p \overline{SAT}$ ולכן $\overline{SAT} \in NPC$." "\n"
  r"אבל $SAT \cup \overline{SAT} = \Sigma^* \notin NPC$",
  note="Red text prints 'SAT <_p SAT‾' — written as \\le_p."),

Q(3, "closure", TFHEAD + r"אם $A \in RE$ ו-$B \in R$, אז $A - B \in RE - R$.", TF, "b",
  r"**דוגמה:** $B = \Sigma^*$, $A = \Sigma^*$. כעת: $A - B = \emptyset \notin RE - R$."),

Q(4, "tm", TFHEAD + r"נתון $L(M) \in R$ אזי בהכרח לכל $w \in \Sigma^*$ סדרת הקונפיגורציות של החישוב של $M$ על $w$ היא סופית.", TF, "b",
  r"**דוגמה:** $L(M_{loop}) = \emptyset \in R$. אבל סדרת הקונפיגורציות של החישוב של $M_{loop}$ על כל מילה היא אינסופית."),

Q(5, "decidability", TFHEAD + r"נתון $L \notin R$ אזי לכל מכונת טיורינג $M$ מתקיים:" "\n"
  r"אם $L(M) = L$ אז קיימת $w \in \Sigma^*$ כך שסדרת הקונפיגורציות של החישוב של $M$ על $w$ היא אין-סופית.", TF, "a",
  r"בהינתן מכונה $M$ - אם לכל מילה $w$ סידרת הקונפיגורציות של החישוב של $M$ על $w$ היא סופית אזי $M$ מכריעה את $L(M)$. "
  r"ולכן אם $L(M) \notin R$ לא קיימת מ\"ט $M$ שמכריעה אותה. ולכן אם $L(M) = L$ אזי חייבת להיות מילה $w$ אך שסדרת הקונפיגורציות איננה סופית."),

Q(6, "enumerators", TFHEAD + r"תהינה $A, B$ שפות כך ש-$A \in NPC$ ו-$B \in RE - NPC$. אזי קיים אנומרטור חד-ערכי "
  r"(כלומר כל מילה מודפסת פעם אחת בלבד) עבור השפה $A \cup B$.",
  opts("נכון", "לא נכון", "תלוי בתשובה לשאלה $NP = P$?"), "a",
  r"$RE$ סגורה לאיחוד. $B \in RE$, $A \in RE$ ולכן $A \cup B \in RE$ ולכל שפה ב-$RE$ קיים אנומרטור חד-ערכי."),

# ---- סיווג שפות ----
Q(7, "classification",
  r"$$L = \{\langle M\rangle \mid (*)\}$$"
  "(*): לכל מילה $w$, המכונה $M$ עוצרת על $w$ בתוך לכל היותר $|w|^2$ צעדים\n"
  "אזי:",
  DEC4, "c",
  r"$L$ לא ניתנת לקבלה על ידי רדוקציה מ-$E_{TM}$." "\n"
  r"$\overline{L}$ ניתנת לקבלה משום שאפשר לבנות מכונה שמורכבת מסימולציה מנוהלת שמקבלת את $\langle M\rangle$ ומריצה את כל המילים האפשריות "
  r"-$w$- כל מילה רק במשך של לכל היותר $|w|^2$ צעדים. אם קיימת מילה כך ש-$M$ לא עוצרת אחרי היותר $|w|^2$ צעדים אזי המכונה $\langle M\rangle$ "
  r"שייכת ל-$\overline{L}$. ולכן אם $\langle M\rangle \in \overline{L}$ המכונה תעצור ותאמר כן. אחרת המכונה לא תעצור.",
  note="Printed stem has the Hebrew condition inside the set braces; moved to a (*) line. First explanation line ('L לא ניתנת לקבלה על ידי רדוקציה מ ETM') is printed in black under the options."),

Q(8, "classification", r"$$L = \{\langle M\rangle \mid L(M) = A_{TM}\}$$" "\nאזי:", DEC4, "d",
  "לא ניתן לדעת האם מכונה מקבלת שפה נתונה או לא.\n"
  r"רק במקרה של השפה הריקה, ניתן לדעת כאשר השפה של המכונה איננה ריקה ($NotEmpty \in RE$)"),

Q(9, "classification", r"$$L = \{\langle M_1, M_2\rangle \mid L(M_1) \subset L(M_2)\}$$" "\nאזי:", DEC4, "d",
  r"רדוקציה $\overline{ALL_{TM}} \le_m L$: $f(\langle M\rangle) = \langle M, M_{\Sigma^*}\rangle$",
  note="Printed stem has a stray extra '}' — dropped."),
]

contexts = {
  "rel": {"kind": "text", "title": "הגדרות לשאלות 10–12 (יחסים בין שפות)",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  r"$$A = \{\langle M\rangle \mid (*)\}$$"
                  r"(*): $\overline{L(M)}$ סופית" "\n"
                  r"$$B = \{\langle M\rangle \mid (**)\}$$"
                  "(**): $L(M)$ אינסופית\n"
                  r"$$C = \{\langle M\rangle \mid L(M) \in R\}$$"},
  "map": {"kind": "text", "title": "הגדרות לשאלות 13–16 (רדוקציית מיפוי)",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  "**שפות:**\n"
                  r"$$H_{TM} = \{\langle M, w\rangle \mid (*)\}$$"
                  "(*): $M$ עוצרת על $w$\n"
                  r"$$NotEmpty_{TM} = \{\langle M\rangle \mid L(M) \ne \emptyset\}$$"
                  r"$$INF_{TM} = \{\langle M\rangle \mid (**)\}$$"
                  "(**): $L(M)$ אינסופית\n"
                  "**פונקציות מיפוי:**\n"
                  r"$$f(\langle M, w\rangle) = \langle R_{Mw}\rangle$$"
                  r"$$g(\langle M\rangle) = \langle T_M\rangle$$"
                  "כאשר המכונות $R_{Mw}$ ו-$T_M$ מוגדרות באופן הבא:\n"
                  "$R_{Mw}$ על קלט $y$:\n"
                  "1. הרץ את $M$ על $w$ למשך $|y|$ צעדים\n"
                  "2. אם בשלב 1 המכונה $M$ עצרה על $w$: **קבל**\n"
                  "אחרת: **דחה**\n"
                  "$T_M$ על קלט $y$:\n"
                  "1. הרץ את $M$ על כל המילים שאורכן לכל היותר $|y|$ למשך $|y|$ צעדים\n"
                  "2. אם בשלב 1 המכונה $M$ קיבלה לפחות מילה אחת: **קבל**\n"
                  "אחרת: **דחה**\n"
                  "ענה על השאלות הבאות"},
  "zsat": {"kind": "text", "title": "הגדרות לשאלות 17–19 (רדוקציה פולינומית)",
           "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                   r"$$ZSAT = \{\langle \phi\rangle \mid (*)\}$$"
                   "(*): $\\phi$ היא נוסחת $3CNF$ שניתנת לסיפוק באמצעות השמה שבה לפחות מחצית מהמשתנים מקבלים ערך $False$\n"
                   r"ניתן להראות כי $ZSAT \in NP$ – נדלג כאן על ההוכחה." "\n"
                   r"**טענה:** $3SAT \le_p ZSAT$." "\n"
                   "נגדיר את הפונקציה הבאה:\n"
                   r"$$f(\langle \phi\rangle) = \phi \wedge (\neg z_1 \vee \neg z_2 \vee \neg z_3) \wedge (\neg z_4 \vee \neg z_5 \vee \neg z_6) \wedge \cdots (\neg z_{N-2} \vee \neg z_{N-1} \vee \neg z_N)$$"
                   r"כאשר: $z_i$ הינם משתנים חדשים שלא מופיעים ב-$\phi$. ערכו של $N$ מתחלק ב-3 והוא הנמוך ביותר שעדיין גדול או שווה למספר המשתנים השונים המופיעים ב-$\phi$." "\n"
                   "ענה על השאלות הבאות:\n"
                   "נסמן את התוספת\n"
                   r"$$d(\phi) = (\neg z_1 \vee \neg z_2 \vee \neg z_3) \wedge (\neg z_4 \vee \neg z_5 \vee \neg z_6) \wedge \cdots (\neg z_{N-2} \vee \neg z_{N-1} \vee \neg z_N)$$"
                   r"$$f(\phi) = \phi \wedge d(\phi)$$"},
}

questions += [
Q(10, "classification", "קבע מהו היחס בין $A$ ל-$B$:",
  opts(("math", "A = B"), ("math", r"A \subset B"), ("math", r"A \supset B"), NONE), "b",
  r"אם $\overline{L(M)}$ סופית אז המשלים שלה הוא אינסופי כלומר $L(M)$ אינסופית. לכן כל איבר ששייך ל-$A$ שייך גם ל-$B$. "
  r"מצד שני יכול להיות איבר ב-$B$ שאיננו איבר ב-$A$. כלומר יכולה להיות מכונה שהשפה שלה $L(M)$ אינסופית וגם המשלים של $L(M)$ "
  r"הוא אין סופי וקיימת מ\"ט כך השפה שלה היא $\overline{L(M)}$ למשל $L(M_1) = \{w \mid |w| = 2p\}$ ברור קיימת כזו מ\"ט $M_1$. "
  r"ואז $\langle M_1\rangle \notin A$, $\langle M_1\rangle \in B$. ולכן התשובה הנכונה היא ב.",
  contextId="rel", note="Explanation transcribed as printed (its '{w | |w| = 2p}' example is loosely worded)."),
Q(11, "classification", "קבע מהו היחס בין $B$ ל-$C$:",
  opts(("math", "B = C"), ("math", r"B \subset C"), ("math", r"B \supset C"), NONE), "d",
  r"עבור $M_{loop}$ מתקיים $L(M_{loop}) = \emptyset$ ולכן $\langle M_{loop}\rangle \in C$ אבל $\langle M_{loop}\rangle \notin B$ ולכן גם א ובם ג לא נכונים." "\n"
  r"עבור $M_2 = U$ (המכונה האוניברסלית שמקבלת מכונה ומילה ומבצעת סימולציה של המכונה על המילה המתקבלת) מתקיים $L(M_2) = A_{TM}$ "
  r"ולכן $\langle M_2\rangle \in B$ אבל $\langle M_2\rangle \notin C$ כלומר ב לא נכון." "\n"
  "ולכן ד נכון.",
  contextId="rel"),
Q(12, "classification", "קבע מהו היחס בין $C$ ל-$A$:",
  opts(("math", "A = C"), ("math", r"A \subset C"), ("math", r"A \supset C"), NONE), "b",
  r"אם $\overline{L(M)}$ סופית אז היא ניתנת להכרעה ולכן גם $L(M)$ ניתנת להכרעה. ולכן $A \subset C$. "
  r"קיימות שפות ב-$C$ שלא נמצאות ב-$A$ למשל $M_1$ שמופיעה בתשובה לשאלה 10. ולכן ג לא נכון וגם א ל נכונים.",
  contextId="rel", note="Last sentence printed 'ולכן ג לא נכון וגם א ל נכונים' (typo, means א also wrong) — kept as printed."),

Q(13, "mapping_reductions", r"האם $f$ היא רדוקציה $H_{TM} \le_m NotEmpty_{TM}$?", YN, "a",
  "$f$ ניתנת לחישוב. כמו כן:\n"
  r"אם $\langle M,w\rangle \in H_{TM}$ אז קיים מספר צעדים סופי כלשהו $r$ שלאחריו $M$ עוצרת על $w$. ולכן קיימת מילה $y$ כך ש-$|y| = r$ "
  r"ואז $R_{Mw}$ יקבל את $y$, ולכן $\langle R_{Mw}\rangle \in NotEmpty_{TM}$." "\n"
  r"אם $\langle R_{Mw}\rangle \in NotEmpty_{TM}$, אזי קימת מילה $y$ ש-$R_{Mw}$ מקבלת. משמעות הדבר היא ש-$M$ עוצרת על $w$ אחרי $|y|$ צעדים או פחות, "
  r"ובפרט $M$ עוצרת על $w$, ולכן $\langle M,w\rangle \in H_{TM}$.",
  contextId="map"),
Q(14, "mapping_reductions", r"האם $f$ היא רדוקציה $H_{TM} \le_m INF_{TM}$?", YN, "a",
  "$f$ ניתנת לחישוב. כמו כן\n"
  r"אם $\langle M,w\rangle \in H_{TM}$, אז קיים מספר צעדים סופי כלשהו $r$ שלאחריו $M$ עוצרת על $w$. ולכן קיימת מילה $y$ כך ש-$|y| = r$ "
  r"ואז $R_{Mw}$ תקבל את $y$. בנוסף $R_{Mw}$ תקבל את **כל המילים** שאורכן גדול מ-$y$. יש אין סוף מילים כאלו, ולכן $\langle R_{Mw}\rangle \in INF_{TM}$." "\n"
  r"אם $\langle M,w\rangle \notin H_{TM}$, אז $M$ לא עוצרת על $w$ בשום מספר של צעדים. כלומר לכל $y$, המכונה $M$ לא עוצרת על $w$ התוך $|y|$ צעדים "
  r"ולכן $R_{Mw}$ לא מקבלת אף מילה ומתקיים $L(R_{Mw}) = \emptyset$ ואז $\langle R_{Mw}\rangle \notin INF_{TM}$.",
  contextId="map"),
Q(15, "mapping_reductions", r"האם $g$ היא רדוקציה $NotEmpty_{TM} \le_m INF_{TM}$?", YN, "a",
  "$g$ ניתנת לחישוב. כמו כן\n"
  r"אם $\langle M\rangle \in NotEmpty_{TM}$ אזי קיימת לפחות מילה אחת $w$ ש-$M$ מקבלת. נגדיר את האורך שלה $|w| = r$. "
  r"$g(\langle M\rangle) = \langle T_M\rangle$ ולפי הגדרה $T_M$ תקבל כל מילה $y$ שמקיימת $|y| \ge r$. קיימות אין סוף מילים כאלה. "
  r"ולכן $L(T_M)$ אינסופית, כלומר $\langle T_M\rangle \in INF_{TM}$." "\n"
  r"אם $\langle M\rangle \notin NotEmpty_{TM}$ אז $L(M) = \emptyset$, כלומר $M$ לא מקבלת אף מילה ולכן גם $T_M$ לא מקבלת אף מילה, "
  r"כלומר $L(T_M) = \emptyset$ ומתקיים $\langle T_M\rangle \notin INF_{TM}$.",
  contextId="map"),
Q(16, "mapping_reductions", r"האם $g$ היא רדוקציה $INF_{TM} \le_m NotEmpty_{TM}$?", YN, "b",
  r"$g$ ניתנת לחישוב. אבל יכולה להיות $\langle M\rangle \notin INF_{TM}$ אבל $\langle T_M\rangle \in NotEmpty_{TM}$." "\n"
  r"**לדוגמא:** $M$ מכונה שמקבלת רק את מילה אחת. ברור ש-$\langle M\rangle \notin INF_{TM}$ אבל $T_M$ מקבלת את כל המילים שהן \"ארוכות מספיק\": "
  r"(לפחות באורך של המילה ש-$M$ מקבלת וגם לפחות באורך של מספר הצעדים שלוקח ל-$M$ לקבל את המילה ההיא). ולכן $\langle T_M\rangle \in NotEmpty_{TM}$. "
  "סה\"כ, זו לא רדוקציה.",
  contextId="map"),

Q(17, "poly_reductions", TFHEAD + r"אם $\langle \phi\rangle \in 3SAT$ אז $f(\langle \phi\rangle) \in ZSAT$.", TF, "a",
  r"אם $\langle \phi\rangle \in 3SAT$ אז ב-$\phi$ כל פסוקית מכילה שלשה ליטרים וגם יש השמה מספקת עבור $\phi$." "\n"
  r"לפחות מחצית מהמשתנים ב-$f(\langle \phi\rangle)$ הם \"חדשים\"." "\n"
  r"לנוסחא $f(\langle \phi\rangle)$ יש השמה מספקת שמתקבלת מההשמה המספקת של $\phi$ וכן מהשמה של ערך $FALSE$ לכל המשתנים החדשים." "\n"
  r"ההשמה הזו מספקת את $f(\langle \phi\rangle)$ וגם לפחות מחצית מהמשתנים קיבלו בה השמה של ערך $FALSE$. סה\"כ $f(\langle \phi\rangle) \in ZSAT$.",
  contextId="zsat"),
Q(18, "poly_reductions", TFHEAD + r"אם $\langle \phi\rangle \notin 3SAT$ אז $f(\langle \phi\rangle) \notin ZSAT$.", TF, "a",
  r"אם $\langle \phi\rangle \notin 3SAT$ אז אין אף השמה שמספקת את $\phi$ ובוודאי שאין אף השמה שתספק את $f(\langle \phi\rangle)$ "
  r"(אפילו לא כזו שבה אין הגבלה על מספר המשתנים שמקבלים ערך $FALSE$ או $TRUE$) ובסה\"כ $f(\langle \phi\rangle) \notin ZSAT$",
  contextId="zsat"),
Q(19, "npc", r"האם המסקנה היא: $ZSAT \in NPC$?", YN, "a",
  r"$f$ ניתנת לחישוב בזמן פולינומי וכמו כן, לפי 17, 18 מתקיים $\langle \phi\rangle \in 3SAT$ אםם $f(\langle \phi\rangle) \in ZSAT$",
  contextId="zsat"),

# ---- שאלות שונות ----
Q(20, "npc", r"תהא $A$ שפה כך שמתקיים $SAT \le_p A$ וגם $\overline{SAT} \le_p A$. איזו מהטענות הבאות נכונה?",
  opts("$NP$ סגורה למשלים.", "$NP$ אינה סגורה למשלים.", r"$A \in R$.", "אף תשובה אינה נכונה."), "d",
  "לא ניתן להסיק כי שפה כלשהי שייכת או לא שייכת ל-$NP$ ולכן תשובות א וב אינן נכונות.\n"
  r"תשובה ג אינה נכונה. שימו לב, אם היתה רדוקציה מ-$A$ אל $SAT$ (אפילו לא פולינומית) אז ניתן היה להסיק כי $A \in R$."),

Q(22, "mapping_reductions",
  "תהינה $A$ ו-$B$ שפות ו-$f$ פונקצית רדוקציה מ-$A$ ל-$B$.\n"
  "נניח ש-$f$ פונקציה הפיכה. איזה מהאפשרויות הבאות **לא** מתקיימת?",
  opts(r"אם $B \in RE$ אז $A \in R$.", r"אם $B \notin RE$ אז $A \notin R$.", r"אם $B \notin R$ אז $A \notin R$.", "אף תשובה אינה נכונה."),
  "a",
  r"$A \le_m B$ ולכן לפי משפט הרדוקציה, האפשרות שמצויינת ב-ג כן מתקיימת." "\n"
  r"כמו כן, אם $B \notin RE$ אז $B \notin R$ ולכן לפי משפט הרדוקציה $A \notin R$ כלומר גם ג כן מתקיים." "\n"
  r"אם $f$ היא רדוקציה מ-$A$ ל-$B$ וכן $f$ הפיכה, אז $f^{-1}$ היא רדוקציה מ-$B$ ל-$A$ כלומר $B \le_m A$" "\n"
  "ולכן מה שמצויין בא' לא מתקיים.",
  note="Second explanation line says 'גם ג כן מתקיים' while arguing about option ב — kept as printed."),

Q(23, "np", r"תהיה $A, B \in NP$. איזו מהטענות הבאות לגבי $A - B$ נכונה?",
  opts(r"אם $B \in P$ אז $A - B \in NP$ ואם $B \notin P$ אז ייתכן $A - B \in NP$ וייתכן $A - B \notin NP$.",
       r"אם $B \in P$ אז $A - B \in NP$ ואם $B \notin P$ אז בהכרח $A - B \notin NP$.",
       r"אם $B \in P$ אז ייתכן $A - B \in NP$ וייתכן $A - B \notin NP$.",
       "אף תשובה אינה נכונה."),
  "a",
  r"אם $B \in P$ אז $\overline{B} \in P$ ולכן $\overline{B} \in NP$. $A - B = A \cap \overline{B}$. $NP$ סגורה לחיתוך ולכן $A - B \in NP$." "\n"
  "כלומר ג לא נכון.\n"
  r"בנוסף, אם $B \notin P$ אז לא ניתן לקבוע האם $A - B \in NP$ או לא. לכן א נכון וב לא נכון."),

Q(24, "decidability",
  r"תהי $M_1, M_2, M_3, \cdots$ קבוצה אינסופית של מכונות טיורינג שעוצרות תמיד." "\n"
  r"**טענה:** קיימת מ\"ט $MI$ שעוצרת תמיד ומקיימת: $w \in L(MI) \Leftrightarrow (\exists i : w \in L(M_i))$." "\n"
  "מה מהבאים נכון?",
  opts("הטענה לא נכונה.", "הטענה נכונה.", r"הטענה נכונה רק אם לכל $i$ מתקיים $L(M_i) \in R$.", "אף תשובה אינה נכונה."),
  "a",
  "הטענה לא נכונה.\n"
  r"נסמן $H_{TM} = \{x_1, x_2, x_3, \cdots\}$" "\n"
  r"$M_i$ היא מכונה שמקבלת רק את המילה $x_i$ ועל כל שאר המילים היא עוצרת ודוחה." "\n"
  r"כל המכונות $M_1, M_2, M_3, \cdots$ עוצרות תמיד." "\n"
  r"אילו הייתה קיימת מכונה $MI$ כמתואר, אז $MI$ היתה מכריעה את $H_{TM}$. אבל זה לא ייתכן.",
  note="Stem's equivalence printed as '(∃i : w ∈ L(M_i)) ⇔ w ∈ L(MI)' in RTL display order; written as w∈L(MI) ⇔ (∃i : w∈L(M_i)) (symmetric)."),

Q(25, "time_p",
  r"תהי $f$ פונקציה המוגדרת באופן הבא: הקלט הוא שלשה $\langle M, x, 1^k\rangle$ כאשר:" "\n"
  r"$M$ היא מ\"ט בסיסית, $x \in \Sigma^*$ היא מילה ו-$1^k$ הוא קידוד אונארי של מספר טבעי $k \ge 1$." "\n"
  r"וכן: אם $M$ מקבלת את $x$ בתוך לכל היותר $k$ צעדים, אז $f(\langle M, x, 1^k\rangle) = 1$" "\n"
  r"אחרת, $f(\langle M, x, 1^k\rangle) = 0$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts("הפונקציה $f$ ניתנת לחישוב בזמן פולינומיאלי.",
       "הפונקציה $f$ ניתנת לחישוב, אבל לא בהכרח בזמן פולינומיאלי.",
       "הפונקציה $f$ לא ניתנת לחישוב.",
       r"הפונקציה $f$ ניתנת לחישוב רק אם מתקיים $L(M) \in R$."),
  "a",
  r"ניתן לבנות מ\"ט שמחשבת את $M$ באמצעות מ\"ט אוניברסלית שמריצה את $M$ מספר צעדים $k$. "
  r"כל צעד בסימולציה לוקח לכל היותר כמות פולינומיאלית של צעדים כפונקציה של $|x|$. ובסך הכל מספר הצעדים הינו לינארי באורך הקלט "
  "ולכן סך כל מספר הצעדים הנידרשים לחישוב $f$ הוא פולינומיאלי באורך הקלט."),
]

exam = {
  "examCode": "20A-B",
  "examLabel": "2020 סמסטר א מועד ב",
  "year": 2020,
  "examDate": "11.3.2020",
  "sourceFile": "מבחנים/2020/סמסטר א/2020-03-11-Exam-חישוביות-2020-moedB-גרסא-0 SOLUTION.pdf",
  "keyFile": "same file (yellow highlights + red explanations)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == [n for n in range(1, 26) if n != 21]
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
