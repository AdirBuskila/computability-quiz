# -*- coding: utf-8 -*-
"""Generator for tools/raw/20A-A.json. Transcribed by hand from the rendered pages of
`מבחנים/2020/סמסטר א/2020-02-14-Exam-חישוביות-2020-moedA-גרסא-0 SOLUTION.pdf` (image-only;
key = yellow highlight, explanations = red text). Numbering = the solution's (form-0) numbering.
Appeal: `חומרים אחרים/MOED A - SOL.pdf` p10 green box "גם תשובה ג התקבלה" on Q23.
Run: PYTHONUTF8=1 py tools/gen/gen_20A-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20A-A.json"
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
Q(1, "mapping_reductions",
  TFHEAD + r"אם $A \le_m B$ וגם $A \le_m C$ אז $A \le_m (B \cup C)$.",
  TF, "b",
  r"**דוגמה נגדית:** $A = H_{TM}$, $B = EQ_{TM}$, $C = \overline{EQ_{TM}}$." "\n"
  r"מתקיים $H_{TM} \le_m EQ_{TM}$ וגם $H_{TM} \le_m \overline{EQ_{TM}}$. אבל $EQ_{TM} \cup \overline{EQ_{TM}} = \Sigma^*$ "
  r"וכמובן שלא מתקיים $H_{TM} \le_m \Sigma^*$."),

Q(2, "mapping_reductions",
  TFHEAD + r"אם $A \in RE$ ו-$B \notin RE$ אז $A \le_m B$.",
  TF, "b",
  r"**דוגמה נגדית:** $A = H_{TM} \in RE$, $B = \overline{H_{TM}} \notin RE$." "\n"
  r"נניח בשלילה שמתקיים $H_{TM} \le_m \overline{H_{TM}}$, אז מתקיים $\overline{H_{TM}} \le_m H_{TM}$, אבל זה לא ייתכן כי "
  r"$H_{TM} \in RE$ ואילו $\overline{H_{TM}} \notin RE$."),

Q(3, "npc",
  TFHEAD + r"קיימות שפות $A$ ו-$B$ כך שמתקיים: $P = NP$ אם ורק אם $A \le_p B$.",
  TF, "a",
  r"קיימות שפות כנדרש. למשל: $A = SAT$, $B = \{0\}$." "\n"
  r"($\Leftarrow$) נניח שמתקיים $P = NP$. אז $A \in P$ ולכן קיימת רדוקציה פולינומית $A \le_p B$." "\n"
  r"($\Rightarrow$) נניח $A \le_p B$. ידוע ש-$A \in NPC$ וכמו כן, $B \in NP$. ולכן, לפי משפט, מתקיים $B \in NPC$. "
  r"אבל גם מתקיים $B \in P$ ולכן $P \cap NPC \ne \emptyset$ ואז, לפי משפט, מתקיים $P = NP$.",
  note="Red text prints 'רדוקציה פולינומית A ≤_m B' — typo, written as ≤_p. Direction arrows kept as printed (⇐ then ⇒)."),

Q(4, "npc",
  TFHEAD + r"אם $P = NP$ אז $\overline{CLIQUE} \in P$.",
  TF, "a",
  r"נניח ש-$P = NP$." "\n"
  r"ידוע כי $CLIQUE \in NP$ ולכן $CLIQUE \in P$. $P$ סגורה למשלים ולכן $\overline{CLIQUE} \in P$."),

Q(5, "closure",
  TFHEAD + r"תהינה $A$ ו-$B$ שפות כך ש-$B \le_m A$ וגם $B \le_m \overline{A}$. אם $A \in RE$ אז $A, B \in R$.",
  TF, "b",
  r"**דוגמה נגדית:** $A = H_{TM}$, $B = \{0\}$." "\n"
  r"$B \in R$ ולכן מתקיים $B \le_m A$ וגם $B \le_m \overline{A}$." "\n"
  r"כמו כן, $A \in RE$ אבל לא מתקיים $A \in R$."),

Q(6, "closure",
  TFHEAD + r"תהינה $A$ ו-$B$ שפות כך ש-$B \le_m A$ וגם $A \le_m \overline{B}$. אם $A \in RE$ אז $A, B \in R$.",
  TF, "a",
  r"$A \in RE$ וגם $B \le_m A$, לכן $B \in RE$." "\n"
  r"$A \le_m \overline{B}$ לכן $\overline{A} \le_m B$." "\n"
  r"$B \in RE$ וגם $\overline{A} \le_m B$, לכן $\overline{A} \in RE$." "\n"
  r"סה\"כ $A \in RE$ וגם $\overline{A} \in RE$ לכן $A \in R$." "\n"
  r"$A \in R$ וגם $B \le_m A$ לכן $B \in R$." "\n"
  r"סה\"כ $A, B \in R$."),

# ---- סיווג שפות ----
Q(7, "classification",
  r"$$L = \{\langle M_1, M_2\rangle \mid |L(M_1) \cap L(M_2)| = 1\}$$" "\n"
  "אזי:",
  DEC4, "d",
  r"**אינטואיטיבית:** $L$ - לא ניתן לוודא שאין יותר מאשר מילה אחת שמתקבלת ע\"י שתי המכונות." "\n"
  r"$\overline{L}$ - לא ניתן לזהות את המקרה שבו החיתוך של שפות המכונות ריק."),

Q(8, "classification",
  r"$$L = \{\langle M, w\rangle \mid (*)\}$$"
  "(*): $M$ מכונת טיורינג אי דטרמיניסטית שדוחה את $w$\n"
  "אזי:",
  DEC4, "b",
  r"מ\"ט שמקבלת את $L$: על קלט $\langle M, w\rangle$: הרץ את $M$ על $w$. אם $M$ עצרה ודחתה: קבל. אחרת: דחה." "\n"
  r"**אינטואיטיבית:** $L$ לא ניתנת להכרעה מאותה סיבה ש-$A_{TM}$ לא ניתנת להכרעה.",
  note="Printed stem: 'L = {<M,w> : M מכונת טיורינג אי דטרמיניסטית שדוחה את w}' — condition moved to a (*) line. "
       "Red text literally says 'מ\"ט שמכריעה את L' although the machine described only recognizes L (and the key is RE−R); written as 'שמקבלת'."),

Q(9, "classification",
  r"$$L = \{\langle M\rangle \mid L(M) \ne \emptyset \wedge L(M) \ne \Sigma^*\}$$" "\n"
  "אזי:",
  DEC4, "d",
  r"**אינטואיטיבית:** לא ניתן לוודא שקיימת מילה ש-$M$ לא-מקבלת.",
  note="Printed with Hebrew 'וגם' between the two conditions; rendered as \\wedge inside math to keep Hebrew out of $…$."),
]

contexts = {
  "rel": {"kind": "text", "title": "הגדרות לשאלות 10–12 (יחסים בין שפות)",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  r"$$A = \{L \mid L \le_m A_{TM}\}$$"
                  r"$$B = \{L \mid \overline{L} \le_m A_{TM}\}$$"
                  r"$$C = \{L \mid A_{TM} \le_m L \wedge L \le_m A_{TM}\}$$"},
  "map": {"kind": "text", "title": "הגדרות לשאלות 13–16 (רדוקציית מיפוי)",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  "**שפות:**\n"
                  r"$$A_{TM} = \{\langle M, w\rangle \mid w \in L(M)\}$$"
                  r"$$ALL_{TM} = \{\langle M\rangle \mid L(M) = \Sigma^*\}$$"
                  r"$$INF_{TM} = \{\langle M\rangle \mid (*)\}$$"
                  "(*): $L(M)$ אינסופית\n"
                  "**פונקציות מיפוי:**\n"
                  r"$$f(\langle M, w\rangle) = \langle T_{M,w}\rangle$$"
                  r"$$g(\langle M\rangle) = \langle R_M\rangle$$"
                  "כאשר המכונות $T_{Mw}$, $R_M$ מוגדרות באופן הבא:\n"
                  "$T_{Mw}$ על קלט $y$:\n"
                  "1. אם $y = 11$: הרץ את $M$ על $w$ וענה כמותה\n"
                  "אחרת: קבל\n"
                  "$R_M$ על קלט $y$:\n"
                  r"1. $i \leftarrow 0$" "\n"
                  "2. הרץ את $M$ על כל המילים שהאורך שלהן לכל היותר $i$\n"
                  "3. אם בשלב 2 המכונה $M$ קיבלה את כל המילים: קבל\n"
                  "אחרת: $i{+}{+}$, חזור ל-2\n"
                  "לכל אחת מהטענות הבאות עליך לקבוע האם היא נכונה או לא."},
  "eclq": {"kind": "text", "title": "הגדרות לשאלות 17–19 (רדוקציה פולינומית)",
           "text": r"**קליקה** בגרף $G$ היא קבוצת קדקודים $C \subseteq V[G]$ כך שכל שני קדקודים מ-$C$ הם שכנים ב-$G$." "\n"
                   "בעיית הקליקה מוגדרת באופן הבא:\n"
                   r"$$CLIQUE = \{\langle G, k\rangle \mid (*)\}$$"
                   "(*): $G$ גרף לא מכוון, $k$ מספר, יש ב-$G$ קליקה בגודל $k$\n"
                   "נגדיר בעיה נוספת:\n"
                   r"$$ECLQ = \{\langle G, k\rangle \mid (**)\}$$"
                   "(**): $G$ גרף לא מכוון עם מספר קדקודים זוגי, $k$ מספר, יש ב-$G$ קליקה בגודל $k$\n"
                   r"רוצים להוכיח כי $CLIQUE \le_p ECLIQ$." "\n"
                   "נגדיר את פונקציית המיפוי הבאה:\n"
                   r"$$f(\langle G, k\rangle) = \begin{cases} \langle G, k\rangle & |V(G)| \text{ even} \\ \langle G', k+1\rangle & \text{otherwise} \end{cases}$$"
                   "כלומר $f(\\langle G,k\\rangle) = \\langle G,k\\rangle$ אם מספר הקדקודים ב-$G$ זוגי, ו-$\\langle G', k+1\\rangle$ אחרת,\n"
                   r"כאשר $G'$ מתקבל מ-$G$ ע\"י הוספה של קדקוד חדש $v_{new}$ וחיבור שלו בצלעות לכל הקדקודים המקוריים של $G$." "\n"
                   "לפניך מספר טענות. לכל טענה עליך לקבוע האם היא נכונה או לא."},
}

REL_EXPL = (r"• מתקיים $B \not\ni A_{TM} \in A, C$ וכן $B \ni \overline{A_{TM}} \notin A, C$." "\n"
            r"לכן $B$ לא מוכלת ולא מכילה את $A$ או את $B$. כלומר: $A \not\subseteq B$, $B \not\subseteq A$, $C \not\subseteq B$, $B \not\subseteq C$." "\n"
            r"• לכל $L \in C$ מתקיים $L \le_m A_{TM}$ לכן $L \in A$ כלומר $C \subseteq A$." "\n"
            r"כמו כן, $\{0\} \in A$ אבל $\{0\} \notin C$ ולכן $C \subsetneq A$.")
REL_NOTE = ("Shared red explanation for Q10–12 (printed once above the three questions). Its text says "
            "'לכן B לא מוכלת ולא מכילה את A או את B' — the second B is a typo for C; kept as printed.")

questions += [
Q(10, "mapping_reductions", "קבע מהו היחס בין $A$ ל-$B$:",
  opts(("math", "A = B"), ("math", r"A \subset B"), ("math", r"A \supset B"), NONE),
  "d", REL_EXPL, contextId="rel", note=REL_NOTE),
Q(11, "mapping_reductions", "קבע מהו היחס בין $B$ ל-$C$:",
  opts(("math", "B = C"), ("math", r"B \subset C"), ("math", r"B \supset C"), NONE),
  "d", REL_EXPL, contextId="rel", note=REL_NOTE),
Q(12, "mapping_reductions", "קבע מהו היחס בין $A$ ל-$C$:",
  opts(("math", "A = C"), ("math", r"A \subset C"), ("math", r"A \supset C"), NONE),
  "c", REL_EXPL, contextId="rel", note=REL_NOTE),
]

MAP_NOTE = ("Solution p5 also has a red 'אבחנות' block: L(T_Mw)=Σ* if <M,w>∈A_TM, else Σ*−{11}; "
            "L(R_M)=Σ* if M accepts ε, else ∅ — prepended to the explanation.")
TOBS = r"**אבחנה:** אם $\langle M,w\rangle \in A_{TM}$ אז $L(T_{Mw}) = \Sigma^*$. אם $\langle M,w\rangle \notin A_{TM}$ אז $L(T_{Mw}) = \Sigma^* - \{11\}$." "\n"
ROBS = r"**אבחנה:** אם $M$ מקבלת את $\varepsilon$ אז $L(R_M) = \Sigma^*$. אחרת, $L(R_M) = \emptyset$." "\n"

questions += [
Q(13, "mapping_reductions", r"האם $f$ היא רדוקציה $A_{TM} \le_m ALL_{TM}$?", YN, "a",
  TOBS +
  r"אם $\langle M,w\rangle \in A_{TM}$ אז $L(T_{Mw}) = \Sigma^*$ ומתקיים $\langle T_{Mw}\rangle \in ALL_{TM}$." "\n"
  r"אם $\langle M,w\rangle \notin A_{TM}$, אז $L(T_{Mw}) = \Sigma^* - \{11\} \ne \Sigma^*$ ומתקיים $\langle T_{Mw}\rangle \notin ALL_{TM}$.",
  contextId="map", note=MAP_NOTE),
Q(14, "mapping_reductions", r"האם $f$ היא רדוקציה $A_{TM} \le_m INF_{TM}$?", YN, "b",
  TOBS +
  r"אם $\langle M,w\rangle \notin A_{TM}$, אז $L(T_{Mw}) = \Sigma^* - \{11\}$. אבל זו שפה אינסופית ולכן לא מתקיים "
  r"$\langle T_{Mw}\rangle \notin INF_{TM}$.",
  contextId="map", note=MAP_NOTE),
Q(15, "mapping_reductions", r"האם $g$ היא רדוקציה $ALL_{TM} \le_m INF_{TM}$?", YN, "b",
  ROBS +
  r"אם $\langle M\rangle \notin ALL_{TM}$, אז ייתכן ש-$M$ מקבלת את $\varepsilon$ וייתכן שלא." "\n"
  r"במקרים שבהם $M$ מקבלת את $\varepsilon$, מתקיים $L(R_M) = \Sigma^*$, כלומר $L(R_M)$ אינסופית ולכן $\langle R_M\rangle \in INF_{TM}$. "
  r"כלומר: אם $\langle M\rangle \notin ALL_{TM}$, אז לא בהכרח מתקיים $\langle R_M\rangle \notin INF_{TM}$.",
  contextId="map", note=MAP_NOTE),
Q(16, "mapping_reductions", r"האם $g$ היא רדוקציה $INF_{TM} \le_m ALL_{TM}$?", YN, "b",
  ROBS +
  r"אם $\langle M\rangle \in INF_{TM}$ אז ייתכן ש-$M$ מקבלת את $\varepsilon$ וייתכן שלא." "\n"
  r"במקרים שבהם $M$ לא מקבלת את $\varepsilon$, מתקיים $L(R_M) = \emptyset \ne \Sigma^*$, ולכן $\langle R_M\rangle \notin ALL_{TM}$." "\n"
  r"(גם בכיוון ההפוך - ייתכן $\langle M\rangle \notin INF_{TM}$ אבל $M$ מקבלת את $\varepsilon$ ואז $L(R_M) = \Sigma^*$ ולכן $\langle R_M\rangle \in ALL_{TM}$.)",
  contextId="map", note=MAP_NOTE),

Q(17, "poly_reductions", TFHEAD + r"אם $\langle G,k\rangle \in CLIQUE$ אז $f(\langle G,k\rangle) \in ECLQ$.", TF, "a",
  r"אם $\langle G,k\rangle \in CLIQUE$ אז יש ב-$G$ קליקה בגודל $k$." "\n"
  r"אם ב-$G$ יש מספר זוגי של קדקודים אז $f(\langle G,k\rangle) = \langle G,k\rangle$." "\n"
  r"סה\"כ, ב-$G$ יש מספר זוגי של קדקודים וגם יש בו קליקה בגודל $k$, ולכן $f(\langle G,k\rangle) = \langle G,k\rangle \in ECLQ$." "\n"
  r"אם ב-$G$ יש מספר אי-זוגי של קדקודים אזי $f(\langle G,k\rangle) = \langle G',k\rangle$. ולכן ב-$G'$ יש מספר זוגי של קדקודים. "
  r"כמו כן, ב-$G'$ יש קליקה בגודל $k+1$ שמורכבת מ-$k$ הקדקודים שמהווים קליקה ב-$G$ בתוספת $v_{new}$ שהוא שכן של כולם. "
  r"סה\"כ, $f(\langle G,k\rangle) = \langle G',k+1\rangle \in ECLQ$.",
  contextId="eclq",
  note="Red text writes 'f(<G,k>) = <G',k>' once where <G',k+1> is meant — kept as printed. The context prints both ECLQ and ECLIQ — kept as printed."),
Q(18, "poly_reductions",
  TFHEAD + r"ייתכן ש-$f(\langle G,k\rangle) = \langle G',k+1\rangle \in ECLQ$ אבל $v_{new}$ לא שייך לקליקה בגודל $k+1$ שנמצאת ב-$G'$ "
  r"ולכן לא ניתן להסיק בוודאות שמתקיים $\langle G,k\rangle \in CLIQUE$.", TF, "b",
  r"אם $f(\langle G,k\rangle) = \langle G',k+1\rangle \in ECLQ$ אז יש ב-$G'$ קליקה בגודל $k+1$." "\n"
  r"במקרה שמתואר בשאלה, יתכן ש-$v_{new}$ אינו חלק מהקליקה בגודל $k+1$ שנמצאת ב-$G'$. "
  r"אבל אז ב-$G$ יש קליקה בגודל $k+1$, ולכן בוודאי שיש בו קליקה בגודל $k$.",
  contextId="eclq"),
Q(19, "poly_reductions",
  TFHEAD + r"ייתכן ש-$f(\langle G,k\rangle) = \langle G,k\rangle \in ECLQ$ אבל $v_{new}$ הוא חלק מהקליקה בגודל $k$ אשר נמצאת ב-$G$ "
  r"ולכן לא ניתן להסיק בוודאות שמתקיים $\langle G,k\rangle \in CLIQUE$.", TF, "b",
  r"אם $f(\langle G,k\rangle) = \langle G,k\rangle$ אז $v_{new}$ לא רלוונטי, כי לא הוספנו אותו במקרה הזה. "
  r"לכן המקרה המתואר בשאלה אינו דוגמא לכך שייתכן ש-$f(\langle G,k\rangle) \in ECLQ$ אבל לא מתקיים $\langle G,k\rangle \in CLIQUE$.",
  contextId="eclq"),

# ---- שאלות שונות ----
Q(20, "poly_reductions",
  r"תהינה $A$ ו-$B$ שפות כך שמתקיים $A \le_p B$ וגם $B \le_p A$. מה מהבאים **לא** ייתכן?",
  opts(r"$A \in R$ ו-$B \notin RE$", r"$A \in RE$ ו-$B \notin R$", r"$A \in P$ ו-$B \in NP$",
       "$A$ סופית ו-$B$ אינסופית"),
  "a",
  r"**א.** רדוקציה פולינומית היא בפרט רדוקציית מיפוי. לכן מתקיים $A \le_m B$ וגם $B \le_m A$. "
  r"לכן אם $A \in R$ אז $B \in R$ ולכן לא ייתכן שמתקיים $A \in R$ ו-$B \notin RE$." "\n"
  "תשובות ב, ג, ד לא נכונות (כלומר המקרים שמתוארים בהם ייתכנו):\n"
  r"**ב.** ייתכן $A \in RE$ וגם $B \notin R$: למשל, $A = B = H_{TM}$" "\n"
  r"**ג.** ייתכן $A \in P$ וגם $B \in NP$: למשל $A = B = \{0\}$" "\n"
  r"**ד.** ייתכן $A$ סופית ו-$B$ אינסופית: למשל $A = \{0\}$, $B = 0^*$."),

Q(21, "decidability",
  "רוצים להוכיח ששפה $A$ ניתנת להכרעה. מה מהבאים יכול להוות הוכחה תקפה?",
  opts(r"מתקיים $A \le_m A_{TM}$ וגם $A \le_m \overline{A}$",
       "קיים אנומרטור שמדפיס כל מילה של $A$ פעם אחת בדיוק",
       r"קיים אנומרטור שמדפיס את כל המילים של $\overline{A}$",
       r"מתקיים $A \le_m \overline{A}$ וגם $A_{TM} \le_m A$"),
  "a",
  "**א.** נראה שאם מתקיימים התנאים בתשובה א' אזי בהכרח $A$ ניתנת להכרעה:\n"
  r"אם $A \le_m A_{TM}$ אז $A \in RE$." "\n"
  r"כעת, אם $A \le_m \overline{A}$ אז $\overline{A} \le_m A$ ומכיוון ש-$A \in RE$ אז $\overline{A} \in RE$." "\n"
  r"סה\"כ: $A, \overline{A} \in RE$, ולפי משפט, $A \in R$." "\n"
  "תשובות ב, ג, ד לא נכונות:\n"
  "**ב.** כל אנומרטור ניתן להפוך לאנומרטור שמדפיס כל מילה רק פעם אחת (לפני שהוא מדפיס מילה, הוא ייבדוק שהיא עדיין לא מופיעה על סרט ההדפסה, "
  r"ורק אם היא לא מופיעה- הוא ידפיס אותה). לכן, קיומו של כזה אנומרטור לא מעיד על כך ש-$A \in R$." "\n"
  r"**ג.** אם קיים אנומרטור שמדפיס את כל המילים ב-$\overline{A}$, אזי $\overline{A}$ ניתנת לקבלה. אבל $A$ עצמה יכולה להיות "
  r"לא-ניתנת לקבלה (עם משלימה, $\overline{A}$, שכן ניתנת לקבלה)." "\n"
  r"**ד.** אם $A_{TM} \le_m A$ אז מתקיים דווקא $A \notin R$."),

Q(22, "np",
  r"תהינה $A$ ו-$B$ שפות כך ש-$A \in NP$ ו-$B \in P$. האם מתקיים $A - B \in NP$?",
  opts("בהכרח כן.", "תלוי בשאלה האם $P = NP$.", "תלוי בשאלה האם $NP$ סגורה למשלים.",
       "יש מקרים שבהם התשובה חיובית ומקרים בהם היא שלילית."),
  "a",
  r"**א.** $B \in P$. $P$ סגורה למשלים ולכן $\overline{B} \in P$. $P \subseteq NP$ ולכן $\overline{B} \in NP$. "
  r"$NP$ סגורה לחיתוך ולכן $A - B = A \cap \overline{B} \in NP$." "\n"
  r"תשובות ב, ג, ד לא נכונות משום שהתשובה אינה תלויה בשאלות $P = NP$ או סגירות למשלים של $NP$ וכמו כן, אין מקרים שבהם התשובה שלילית."),

Q(23, "npc",
  "השפה $LenPath$ מוגדרת בהמשך. מה מהבאים נכון? (בהנחה ש-$P \\ne NP$)\n"
  r"$$LenPath = \{\langle G, s, t, k\rangle \mid (*)\}$$"
  "(*): $G$ גרף לא מכוון, $s, t$ קדקודים ב-$G$, יש ב-$G$ מסלול מ-$s$ אל $t$ שאורכו לפחות $k$ צלעות",
  opts(("math", r"LenPath \in NPC"), ("math", r"LenPath \in NP - NPC"), ("math", r"LenPath \in P"), NONE),
  "a",
  r"**א.** ברור ש-$LenPath \in NP$: (אלגוריתם א\"ד: בחר באופן א\"ד סדרה של $k$ צלעות ובדוק שהן מהוות מסלול פשוט מ-$s$ אל $t$)." "\n"
  r"**$HAMPATH \le_p LenPath$:** בהגדרת השפה מופיע הדרישה \"יש ב-$G$ מסלול מ-$s$ אל $t$ שאורכו ....\"" "\n"
  r"**אם נשנה את ההגדרה של $LenPath$ ע\"י כך שנדרוש שהמסלול יהיה פשוט:** ניתן לראות שתחת השינוי הזה מתקיים $HAMPATH \le_p LenPath$, "
  r"ע\"י הפונקציה: $f(\langle G,s,t\rangle) = \langle G,s,t,n-1\rangle$ כאשר $n$ הוא מספר הקדקודים ב-$G$. "
  r"$HAMPATH \in NPC$, לכן $LenPath \in NPC$." "\n"
  "**לפי ההגדרה המקורית:** המסלול הנדרש עשוי להיות לא-פשוט (כלומר, מותר לבקר כמה פעמים באותו קדקוד אבל אסור לעבור יותר מאשר פעם אחת באותה הצלע). "
  r"עדיין מתקיים $HAMPATH \le_p LenPath$, אבל הרדוקציה במקרה הזה מורכבת יותר. $HAMPATH \in NPC$, לכן $LenPath \in NPC$." "\n"
  r"תחת ההנחה $P \ne NP$, תשובות ב, ג, ד אינן נכונות:" "\n"
  r"**ב.** $LenPath \in NPC$ לכן לא מתקיים $LenPath \in NP - NPC$." "\n"
  r"**ג.** $LenPath \in NPC$ לכן אם מתקיים גם $LenPath \in P$ אז $P \cap NPC \ne \emptyset$ ואז לפי משפט מתקיים $P = NP$, וזה לא ייתכן תחת ההנחה $P \ne NP$." "\n"
  "**ד.** תשובה א נכונה.\n"
  "**ערעור:** לפי הערת תיקון בקובץ הפתרון (\"גם תשובה ג התקבלה\"), גם תשובה ג התקבלה.",
  acceptedIds=["a", "c"],
  note="Solution text prints HAMPTH in two places (typo for HAMPATH) — normalized. Appeal: 'חומרים אחרים/MOED A - SOL.pdf' p10 "
       "(same solution, same numbering) has a green box next to Q23: 'גם תשובה ג התקבלה' → acceptedIds [a, c]. The canonical "
       "גרסא-0 SOLUTION file has no such box on its p10. Refutation of ג prints 'P ∩ NPC = ∅' (zoomed) — "
       "a typo for ≠ ∅ (the argument concludes P = NP); written as \\ne."),

Q(24, "classification",
  r"עבור שפה $L$ נגדיר את השפה $AccL$ באופן הבא: $AccL = \{\langle M\rangle \mid L(M) = L\}$. כלומר $AccL$ היא שפת כל המכונות שמקבלות את השפה $L$." "\n"
  r"האם יש שפה $L$ שעבורה מתקיים $AccL \in RE$?",
  opts(r"לא, אין אף שפה $L$ שעבורה $AccL \in RE$.",
       r"כן, רק השפה $L = \Sigma^*$.",
       r"כן, רק השפה $L = \emptyset$.",
       "אף תשובה אינה נכונה."),
  "a",
  r"**א. הסבר אינטואיטיבי:** לא ניתן לוודא עבור אינסוף מילים ש-$M$ מתייחסת אליהם כראוי: כלומר מקבלת מילים ששייכות ל-$L$ ולא-מקבלת את אלו שלא שייכות ל-$L$." "\n"
  "תשובות ב,ג,ד לא נכונות:\n"
  r"**ב.** $Acc\Sigma^* = ALL_{TM} \notin RE$" "\n"
  r"**ג.** $Acc\emptyset = E_{TM} \notin RE$" "\n"
  "**ד.** תשובה א נכונה.\n"
  r"**תיקון (מתוך קובץ הפתרון):** אם $L$ איננה ניתנת לקבלה, אז $AccL$ ריקה ולכן אפילו ניתנת להכרעה. תתקבלנה שתי התשובות: א ו-ד.",
  acceptedIds=["a", "d"],
  note="Green 'תיקון' box on solution p11: both א and ד accepted (ד also shaded)."),

Q(25, "time_p",
  r"תהי $A$ שפה שניתנת להכרעה, ונניח שקיימת מכונת טיורינג **עם שלושה סרטים** אשר מכריעה את $A$ בסיבוכיות זמן $O(n^3)$." "\n"
  r"האם בהכרח קיימת מכונת טיורינג **עם סרט אחד** שמכריעה את $A$? ואם כן- מהי סיבוכיות הזמן **הטובה ביותר** שבהכרח אפשרית?",
  opts(r"כן, בסיבוכיות זמן $O(n^6)$.", r"כן, בסיבוכיות זמן $O(n^3)$.", r"כן, בסיבוכיות זמן $O(n^9)$.",
       r"לא בהכרח קיימת מ\"ט דטרמיניסטית אשר מכריעה את $A$."),
  "a",
  r"**משפט:** אם קיימת מ\"ט $k$-סרטית ($k > 1$ קבוע) שמכריעה את $A$ בסיבוכיות זמן $O(t(n))$ אז יש מ\"ט עם סרט אחד שמכריעה את $A$ "
  r"בסיבוכיות זמן $O(t(n)^2)$."),
]

exam = {
  "examCode": "20A-A",
  "examLabel": "2020 סמסטר א מועד א",
  "year": 2020,
  "examDate": "14.2.2020",
  "sourceFile": "מבחנים/2020/סמסטר א/2020-02-14-Exam-חישוביות-2020-moedA-גרסא-0 SOLUTION.pdf",
  "keyFile": "same file (yellow highlights + red explanations; green תיקון box on Q24); Q23 appeal from חומרים אחרים/MOED A - SOL.pdf p10",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 26))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
