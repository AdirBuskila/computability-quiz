# -*- coding: utf-8 -*-
"""Generator for tools/raw/SAMP-2.json (sample exam תש"פ, 29 Q). Transcribed by hand from the
rendered pages of `מבחנים/מבחנים לדוגמה/בחינה לדוגמה עם הסברים.pdf` (key = yellow highlight,
explanations = the red "הסבר" text). Every answer was cross-checked against the review deck
`מצגות חזרה למבחן/ פתרון מבחן לדוגמא תשפ אלישבע סמסטר ב 2025.pdf` slides 1-82 (yellow
highlight on each "תשובה" slide); the deck's fuller explanations / "הרחבות" are transcribed in
where they add to the PDF. Run: PYTHONUTF8=1 py tools/gen/gen_SAMP-2.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "SAMP-2.json"
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

TF = opts("נכון", "לא נכון")
DEC4 = opts(
    "$L$ ניתנת להכרעה.",
    "$L$ ניתנת לקבלה אבל לא ניתנת להכרעה.",
    "$L$ לא ניתנת לקבלה אבל המשלימה שלה ניתנת לקבלה.",
    "$L$ לא ניתנת לקבלה וגם המשלימה שלה לא ניתנת לקבלה.",
)
NONE_REL = 'אף אחד מהנ"ל'
BOTH = "תשובות א ו-ב נכונות"
NONE_ANS = "אף תשובה אינה נכונה"

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "highlighted-pdf", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

TFHEAD = "קבע האם הטענה הבאה נכונה או לא:\n"

contexts = {
  "g": {"kind": "text", "title": "הגדרות לשאלות 10–12",
        "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                r"$$G_1 = \{\langle M\rangle \mid L(M) \in R\}$$"
                r"$$G_2 = \{\langle M\rangle \mid (*)\}$$"
                "(*): $L(M)$ אינסופית\n"
                r"$$G_3 = \{\langle M\rangle \mid (**)\}$$"
                r"(**): $\overline{L(M)}$ סופית"},
  "d": {"kind": "text", "title": "הגדרות לשאלות 13–20",
        "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                r"$$E_{TM} = \{\langle M\rangle \mid L(M) = \emptyset\}$$"
                "נגדיר את השפות הבאות:\n"
                r"$$L_1 = \{\langle M_1, M_2\rangle \mid L(M_1) \cap L(M_2) = \emptyset\}$$"
                r"$$L_2 = \{\langle M_1, M_2\rangle \mid (*)\}$$"
                "(*): $L(M_1) \\cap L(M_2)$ אינסופית\n"
                "נגדיר את פונקציות המיפוי הבאות:\n"
                r"$$f(\langle M\rangle) = \langle R_M, M\rangle \qquad g(\langle M\rangle) = \langle R_M, T_M\rangle$$"
                "כאשר בהינתן מ\"ט $M$, המכונות $T_M$ ו-$R_M$ הן המכונות הבאות:\n"
                "**$T_M$ על קלט $y$:**\n"
                "1. הרץ את $M$ על כל המילים שהאורך שלהן הוא לכל היותר $|y|$ למשך $|y|$ צעדים.\n"
                "2. אם $M$ קיבלה לפחות אחת מהמילים: קבל. אחרת: דחה.\n"
                "**$R_M$ על קלט $y$:**\n"
                "1. אם $y = 00$ או $y = 11$: קבל.\n"
                "2. הרץ את $M$ על $y$ וענה כמו $M$.\n"
                "לכל אחת מהטענות הבאות עליך לקבוע האם היא נכונה או לא."},
  "e": {"kind": "text", "title": "הגדרות לשאלות 21–24",
        "text": "ראה את הגדרת כיסוי קדקודים והשפה $VC$ בדף העזר. השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                r"$$VCM = \{\langle G, k\rangle \mid (*)\}$$"
                "(*): יש ב-$G$ לכל היותר קדקוד אחד עם דרגה אי-זוגית, וכן יש ב-$G$ כיסוי קדקודים בגודל $k$\n"
                "ידוע כי $VC$ היא $NP$-שלמה. רוצים להוכיח כי גם $VCM$ היא $NP$-שלמה ע\"י כך שמראים כי $VC \\le_p VCM$.\n"
                "נגדיר את פונקציית המיפוי הבאה:\n"
                r"$$f(\langle G, k\rangle) = \langle G', k\rangle$$"
                "כאשר $G'$ הוא גרף שמתקבל מ-$G$ באופן הבא: מוסיפים קדקוד $v_{new}$ ומחברים אותו בצלע לכל הקדקודים ב-$G$ שיש להם דרגה אי-זוגית.\n"
                "לפניך מספר טענות. לכל טענה בנפרד עליך לקבוע האם היא נכונה או לא."},
}

questions = [
# ---------------- חלק א: נכון / לא נכון ----------------
Q(1, "mapping_reductions",
  TFHEAD + r"אם $A$ היא שפה כך ש-$A \le_m \overline{A}$, אזי בהכרח מתקיים $A \notin RE - R$.",
  TF, "a",
  r"נניח בשלילה ש-$A \in RE - R$, כלומר מתקיים $A \in RE$ וגם $A \notin R$." "\n"
  r"כעת, מכיוון ש-$A \le_m \overline{A}$ אז $\overline{A} \le_m A$." "\n"
  r"$\overline{A} \le_m A$ וגם $A \in RE$ ולכן $\overline{A} \in RE$." "\n"
  r"סה\"כ: $A, \overline{A} \in RE$ ולפי משפט, מתקיים $A \in R$. אבל $A \notin R$. סתירה." "\n"
  r"**הרחבה (מצגת החזרה):** באופן דומה ניתן להוכיח על כל שתי שפות $A \in RE - R$, $B \in coRE - R$ שהן לא ניתנות לרדוקציה אחת לשנייה. "
  r"נניח שכן: אם $B \le_m A$, אז $B \in RE$, ואז $B \in RE \cap coRE$, ולכן $B \in R$, בסתירה. "
  r"ובאופן דומה: אם $A \le_m B$, אז $\overline{A} \le_m \overline{B}$, אז $\overline{A} \in RE$, אז $A \in RE \cap coRE$ ולכן $A \in R$, בסתירה." "\n"
  "באיזו אופציה **יכולה** להיות רדוקציה משפה למשלימה שלה? ב-$R$: כן! מחוץ ל-$RE$ ול-$coRE$: כן! בתוך $RE$ ומחוץ ל-$R$: לא!"),

Q(2, "closure",
  TFHEAD + r"בהינתן שפה $A$ נגדיר את השפה הבאה: $D(A) = \{x \mid 0x \in A\}$." "\n"
  r"טענה: אם $A \in R$ אז $D(A) \in R$.",
  TF, "a",
  r"אם $A \in R$ אז יש מ\"ט $M_A$ שמכריעה את $A$." "\n"
  r"נבנה מ\"ט שתכריע את $D(A)$: על קלט $x$: שרשר $0$ משמאל ל-$x$, הרץ את $M_A$ על $0x$ וענה כמותה.",
  note="PDF explanation writes the input as y ('על קלט y ... על 0y'); the deck writes x, matching the definition — used x."),

Q(3, "closure",
  TFHEAD + r"אם השפות $A$ וגם $B$ ניתנות לקבלה, אזי בהכרח השפה $A \,\Delta\, B$ ניתנת לקבלה, "
  r"כאשר $A \,\Delta\, B$ מסמן הפרש סימטרי, כלומר: $A \,\Delta\, B = (A - B) \cup (B - A)$.",
  TF, "b",
  r"דוגמה נגדית: $A = H_{TM}$, $B = \Sigma^*$. מתקיים $A, B \in RE$ אבל "
  r"$A \Delta B = (H_{TM} - \Sigma^*) \cup (\Sigma^* - H_{TM}) = \emptyset \cup \overline{H_{TM}} = \overline{H_{TM}} \notin RE$." "\n"
  r"**הרחבות (מצגת החזרה):** הגדרה שקולה להפרש סימטרי: $A \Delta B = (A \cup B) - (A \cap B)$. "
  r"המחלקה $RE - R$ סגורה לחיתוך ואיחוד, לא סגורה למשלים ולהפרש." "\n"
  "כדי להוכיח שאין סגירות של קבוצה תחת פעולה, יש להראות שקיימת אפשרות שתוצאת הפעולה לא נשארת בתוך הקבוצה — וזה מה שעשינו. "
  "אבל!!! זה לא אומר ש**תמיד** תוצאת הפעולה מתקבלת **מחוץ** לקבוצה: למשל, עבור "
  r"$A = H_{TM}$, $B = \overline{E_{TM}}$: $A \Delta B = (H_{TM} - \overline{E_{TM}}) \cup (\overline{E_{TM}} - H_{TM}) = H_{TM} \cup \overline{E_{TM}} \in RE$." "\n"
  "תזכורת: $RE$ לא סגורה למשלים! אם $RE$ כן הייתה סגורה למשלים, אז היא גם הייתה סגורה להפרש סימטרי. ההפך גם נכון! מדוע? "
  "(רמז: המשלים מתקבל על ידי פעולת הפרש סימטרי עם...?)",
  note="Deck slide 16's example equation is transcribed as printed (it simplifies the symmetric difference loosely). "
       "Deck slide 14 prints 'המחלקה RE − R סגורה לחיתוך ואיחוד' — kept as printed."),

Q(4, "closure",
  TFHEAD + r"אם $A, B$ הן שפות כך ששלוש השפות $A$, $A \cup B$ ו-$A \cap B$ ניתנות להכרעה, אזי גם השפה $B$ ניתנת להכרעה.",
  TF, "a",
  r"$B = \big((A \cup B) - A\big) \cup (A \cap B)$. המחלקה $R$ סגורה להפרש ולאיחוד."),

Q(5, "npc",
  TFHEAD + r"אם קיימת שפה $L \in NP$ כך ש-$L \le_p \overline{L}$ אזי מתקיים $P = NP$.",
  TF, "b",
  r"קיומה של כזו שפה אינו מעיד על כך ש-$P = NP$ או $P \ne NP$." "\n"
  r"למשל: $L = 0^*$: ברור ש-$0^* \in NP$ וכן $L \le_p \overline{L}$, ובכל זאת, עדיין לא ידוע האם מתקיים $P = NP$ או $P \ne NP$."),

Q(6, "poly_reductions",
  TFHEAD + r"תהא $A$ שפה כך שמתקיים $CLIQUE \le_p A$, אזי מתקיים $IS \le_p A$.",
  TF, "a",
  r"ראינו $IS \le_p CLIQUE$. לכן, מטרנזיטיביות של היחס $\le_p$ מתקיים גם $IS \le_p A$." "\n"
  r"(ניתן לומר כי $IS \le_p CLIQUE$ גם משום ש-$IS \in NP$, $CLIQUE \in NPC$.)"),

# ---------------- חלק ב: סיווג ----------------
Q(7, "classification",
  "שייך את השפה לאחת מהמחלקות המפורטות:\n"
  r"$$L = \{\langle M\rangle \mid L(M) \in RE\}$$",
  DEC4, "a",
  r"$RE$ היא מחלקת השפות שיש מ\"ט שמקבלת אותן. לכן, בהגדרה, מתקיים:" "\n"
  r"$$L = \{\langle M\rangle \mid (*)\}$$"
  "(*): $M$ היא מכונת טיורינג\n"
  "וניתן להכריע האם מחרוזת היא קידוד של מ\"ט."),

Q(8, "classification",
  "שייך את השפה לאחת מהמחלקות המפורטות:\n"
  r"$$B = \{\langle M_1, M_2\rangle \mid L(M_1) \ne L(M_2)\}$$",
  DEC4, "d",
  r"$L = \overline{EQ_{TM}}$.",
  note="The language is named B but the printed options speak of 'L' (as in all of part ב) — kept. "
       "Printed option ג reads 'המשלימה שניתנת לקבלה' (missing 'שלה'); normalized to Q7's wording."),

Q(9, "classification",
  "שייך את השפה לאחת מהמחלקות המפורטות:\n"
  r"$$C = \{\langle M\rangle \mid (*)\}$$"
  "(*): יש אינסוף מילים ש-$M$ מקבלת בתוך $5$ צעדים או פחות",
  DEC4, "a",
  "אם $M$ מקבלת מילה $w$ בתוך $5$ צעדים או פחות, אז היא מתייחסת לכל היותר ל-$5$ האותיות הראשונות של $w$.\n"
  "לכן: $M$ מקבלת אינסוף מילים בתוך $5$ צעדים או פחות אם ורק אם היא מקבלת מילה $w$ שהאורך שלה הוא $5$, בתוך $5$ צעדים או פחות "
  "(אינסוף המילים הן כל המילים שהרישא שלהן היא אותה $w$).\n"
  "לכן, המכונה הבאה מכריעה את $L$: על קלט $\\langle M\\rangle$: הרץ את $M$ על כל המילים שאורכן $5$ למשך $5$ צעדים לכל מילה. "
  "אם יש מילה שהתקבלה: קבל. אחרת: דחה.",
  note="The language is named C but the printed options speak of 'L' — kept. Option ג normalized as in Q8. "
       "Explanation follows the deck (slide 31: words of length exactly 5); the PDF says 'שהאורך שלה לכל היותר 5' / "
       "'על כל המילים שאורכן לכל היותר 5' and lacks the parenthetical."),

# ---------------- חלק ג: יחסים ----------------
Q(10, "decidability", "קבע מהו היחס בין $G_1$ ו-$G_2$:",
  opts(("math", "G_1 = G_2"), ("math", r"G_1 \subset G_2"), ("math", r"G_1 \supset G_2"), NONE_REL),
  "d",
  "$G_1$ – מכונות שהשפות שלהן ניתנות להכרעה.\n$G_2$ – מכונות שהשפות שלהן אינסופיות.\n"
  r"יש שפות אינסופיות שלא ניתנות להכרעה ולכן $G_2 \not\subseteq G_1$." "\n"
  r"יש שפות שניתנות להכרעה אבל הן סופיות ולכן $G_1 \not\subseteq G_2$.",
  contextId="g"),

Q(11, "decidability", "קבע מהו היחס בין $G_3$ ו-$G_1$:",
  opts(("math", "G_1 = G_3"), ("math", r"G_1 \subset G_3"), ("math", r"G_1 \supset G_3"), NONE_REL),
  "c",
  "$G_3$ – מכונות שהשפה המשלימה לשפה שהן מקבלות היא סופית.\n"
  "כל שפה סופית היא ניתנת להכרעה (שייכת ל-$R$). המחלקה $R$ סגורה למשלים.\n"
  r"לכן, השפה של כל מכונה ששייכת ל-$G_3$ היא שפה שניתנת להכרעה, ולכן $G_3 \subseteq G_1$." "\n"
  r"כמו כן, זו הכלה ממש: למשל, המכונה שדוחה כל קלט שלה שייכת ל-$G_1$ אבל לא ל-$G_3$. לכן $G_3 \subsetneq G_1$.",
  contextId="g"),

Q(12, "decidability", "קבע מהו היחס בין $G_2$ ו-$G_3$:",
  opts(("math", "G_2 = G_3"), ("math", r"G_2 \subset G_3"), ("math", r"G_2 \supset G_3"), NONE_REL),
  "c",
  r"אם שפה היא סופית, אז המשלימה שלה היא בהכרח אינסופית. לכן, כל מכונה ששייכת ל-$G_3$ שייכת גם ל-$G_2$, כלומר $G_3 \subseteq G_2$." "\n"
  "כמו כן, זו הכלה ממש: למשל, המכונה שמקבלת את כל המילים שהאורך שלהן זוגי ודוחה את המילים שהאורך שלהן אי-זוגי, "
  r"שייכת ל-$G_2$ אבל לא ל-$G_3$. לכן $G_3 \subsetneq G_2$.",
  contextId="g"),
]

# ---------------- חלק ד: R_M, T_M ----------------
questions += [
Q(13, "mapping_reductions", r"אם $\langle M\rangle \in E_{TM}$ אז $\langle R_M, M\rangle \in L_1$.", TF, "a",
  r"אם $\langle M\rangle \in E_{TM}$ אז $L(M) = \emptyset$ ולכן $L(R_M) \cap L(M) = \emptyset$ ולכן $\langle R_M, M\rangle \in L_1$." "\n"
  "שימו לב: המהות והמשמעות של $R_M$ כלל לא רלוונטיות לתשובה...",
  contextId="d"),

Q(14, "mapping_reductions", r"אם $\langle M\rangle \in E_{TM}$ אז $\langle R_M, M\rangle \in L_2$.", TF, "b",
  r"מהשאלה הקודמת קיבלנו שהחיתוך הוא ריק, לכן ודאי שאינו אינסופי, לכן $\langle R_M, M\rangle \notin L_2$." "\n"
  "שימו לב: גם כאן, המהות והמשמעות של $R_M$ כלל לא רלוונטיות לתשובה...",
  contextId="d"),

Q(15, "mapping_reductions", r"אם $\langle M\rangle \in E_{TM}$ אז $\langle R_M, T_M\rangle \in L_1$.", TF, "a",
  r"אם $\langle M\rangle \in E_{TM}$ אז $L(M) = \emptyset$, כלומר $M$ לא מקבלת אף מילה, ולכן $L(T_M) = \emptyset$, "
  r"ולכן $L(R_M) \cap L(T_M) = \emptyset$ ולכן $\langle R_M, T_M\rangle \in L_1$.",
  contextId="d"),

Q(16, "mapping_reductions", r"אם $\langle M\rangle \in E_{TM}$ אז $\langle R_M, T_M\rangle \in L_2$.", TF, "b",
  r"מהשאלה הקודמת קיבלנו שהחיתוך הוא ריק, לכן ודאי שאינו אינסופי, לכן $\langle R_M, T_M\rangle \notin L_2$.",
  contextId="d"),

Q(17, "mapping_reductions", r"אם $\langle M\rangle \notin E_{TM}$ אז $\langle R_M, M\rangle \notin L_1$.", TF, "a",
  r"אם $\langle M\rangle \notin E_{TM}$ אז $L(M) \ne \emptyset$." "\n"
  r"נשים לב כי תמיד $L(R_M) = \{00, 11\} \cup L(M)$ ולכן $L(R_M) \cap L(M) = L(M)$." "\n"
  r"במקרה שלנו $\langle M\rangle \notin E_{TM}$ ולכן $L(M) \ne \emptyset$, לכן $L(R_M) \cap L(M) \ne \emptyset$, כלומר $\langle R_M, M\rangle \notin L_1$.",
  contextId="d"),

Q(18, "mapping_reductions", r"אם $\langle M\rangle \notin E_{TM}$ אז $\langle R_M, M\rangle \notin L_2$.", TF, "b",
  r"כמו קודם, $L(R_M) = \{00, 11\} \cup L(M)$ ולכן $L(R_M) \cap L(M) = L(M)$." "\n"
  r"אנחנו יודעים שהשפה של $M$ לא ריקה, אבל איננו יודעים אם היא אינסופית או סופית, ולכן לא נוכל להסיק $\langle R_M, M\rangle \notin L_2$." "\n"
  r"**דוגמה:** אם $M$ היא המכונה הבאה: $M(x)\{accept\}$, אז $L(R_M) \cap L(M) = L(M) = \Sigma^*$ ואז **לא** מתקיים $\langle R_M, M\rangle \notin L_2$.",
  contextId="d"),

Q(19, "mapping_reductions", r"אם $\langle M\rangle \notin E_{TM}$ אז $\langle R_M, T_M\rangle \notin L_1$.", TF, "b",
  r"לפי הנתון $L(M) \ne \emptyset$, כלומר קיימת לפחות מילה אחת, $w$, ש-$M$ מקבלת. "
  r"ואז, $T_M$ מקבלת אינסוף מילים: למשל, את כל המילים $y$ כך ש-$|y|$ גדול גם מ-$|w|$ וגם ממספר הצעדים שלוקח ל-$M$ לקבל את $w$." "\n"
  r"נסביר: תהי $w$ מילה המתקבלת על ידי $M$ (מהנתון, יש לפחות אחת כזו). נסמן $|w| = k_1$, ונסמן $k_2$ את מספר הצעדים של המכונה $M$ עד שהיא מקבלת את $w$. "
  r"אזי, אם נתבונן בקבוצה $S = \{y \mid |y| > \max(k_1, k_2)\}$, אזי $S \subseteq L(T_M)$ וכן $|S| = \infty$ ולכן $|L(T_M)| = \infty$." "\n"
  r"כעת, נשים לב, כי תמיד $L(R_M) \cap L(T_M) = (\{00, 11\} \cup L(M)) \cap L(T_M)$. "
  r"אז אנחנו יודעים שהשפה של $T_M$ אינסופית, והשפה של $M$ לא ריקה... ועדיין, זה לא מחייב שום דבר לגבי החיתוך $L(R_M) \cap L(T_M)$. "
  "כלומר, אי אפשר להסיק שהחיתוך לא ריק.\n"
  r"**דוגמה:** אם $M$ היא מ\"ט שמקבלת את $\varepsilon$ בתוך 3 צעדים ולא מקבלת אף מילה אחרת, אזי $L(R_M) = \{00, 11, \varepsilon\}$ "
  r"אבל $00 \notin L(T_M)$, $11 \notin L(T_M)$, $\varepsilon \notin L(T_M)$ ולכן $L(R_M) \cap L(T_M) = \emptyset$. "
  r"כלומר, $\langle R_M, T_M\rangle \in L_1$, ואי אפשר להסיק את המסקנה שבשאלה.",
  contextId="d"),

Q(20, "mapping_reductions", r"אם $\langle M\rangle \notin E_{TM}$ אז $\langle R_M, T_M\rangle \notin L_2$.", TF, "b",
  "כמו בשאלה הקודמת, גם אי אפשר להסיק שהחיתוך הוא אינסופי.\n"
  r"**דוגמה:** אם $M$ היא המ\"ט הבאה: $M(x)\{accept\}$, אז מתקיים $L(R_M) = \{00, 11\} \cup L(M) = L(M) = \Sigma^*$, "
  r"וכן כפי שהסברנו בשאלה הקודמת, $L(T_M)$ אינסופית, ולכן גם החיתוך $L(R_M) \cap L(T_M)$ אינסופי, ומתקיים $\langle R_M, T_M\rangle \in L_2$, "
  "ולכן לא ניתן להסיק את המסקנה שבשאלה.\n"
  "**סיכום חלק ד — האם מתקיימות הרדוקציות הבאות:** $f$ רדוקציה מ-$E_{TM}$ ל-$L_1$? (שאלות 13, 17); "
  "$f$ רדוקציה מ-$E_{TM}$ ל-$L_2$? (14, 18); $g$ רדוקציה מ-$E_{TM}$ ל-$L_1$? (15, 19); $g$ רדוקציה מ-$E_{TM}$ ל-$L_2$? (16, 20).",
  contextId="d",
  note="PDF gives one joint explanation for Q13-20 (p.6); per-question explanations transcribed from the deck (slides 41-61), "
       "which agree with the PDF's analysis. Deck's part-ד summary slide (62) only pairs the questions per function; rendered as a short line."),
]

# ---------------- חלק ה: VCM ----------------
questions += [
Q(21, "poly_reductions",
  r"הכיוון של הרדוקציה שגוי: אם רוצים להראות ש-$VCM$ היא $NP$-שלמה אז יש להראות שמתקיים $VCM \le_p VC$.",
  TF, "b",
  "כדי להוכיח שייכות ל-$NPC$, יש לקחת שפה ששייכותה ל-$NPC$ ידועה, ולעשות רדוקציה **ממנה**. "
  "ואז, לפי הטרנזיטיביות, נקבל שגם שפת ה\"יעד\" היא $NPC$.",
  contextId="e", note="Printed with '(2 נקודות)'; point weights omitted. PDF has no explanation; explanation from deck slide 64."),

Q(22, "poly_reductions",
  r"ההוכחה מיותרת מכיוון ש-$VCM$ היא מקרה פרטי של $VC$.",
  TF, "b",
  "אכן זהו מקרה פרטי, או תת-קבוצה, של שפה $NPC$. אבל תכונה זו לא עוברת \"בירושה\".\n"
  "למשל, גם $2SAT$ היא מקרה פרטי של $SAT$, אבל $SAT$ היא $NPC$ ו-$2SAT$ היא ב-$P$.",
  contextId="e", note="Printed with '(2 נקודות)'. PDF has no explanation; explanation from deck slide 66."),

Q(23, "poly_reductions",
  r"אם $\langle G, k\rangle \in VC$ אז מתקיים $\langle G', k\rangle \in VCM$.",
  TF, "b",
  r"אם $\langle G, k\rangle \in VC$ אז קיים ב-$G$ כיסוי קדקודים בגודל $k$." "\n"
  r"ב-$G'$ הדרגה של כל הקדקודים \"המקוריים\" של $G$ היא זוגית. ולכן יש לכל היותר קדקוד אחד שהדרגה שלו אי-זוגית. "
  r"(אגב, משפט מתורת הגרפים מבטיח שגם הדרגה של $v_{new}$ היא זוגית, אבל זה לא נדרש כאן...)" "\n"
  r"אבל לא בהכרח קיים ב-$G'$ כיסוי קדקודים בגודל $k$, משום שלא ברור האם הכיסוי של $G$ מכסה את כל הצלעות החדשות שהוספנו." "\n"
  r"(ברור שיש ב-$G'$ כיסוי קדקודים בגודל $k+1$, ע\"י הוספה של $v_{new}$ ל-$k$ הקדקודים מ-$G$ שמהווים כיסוי ב-$G$.)" "\n"
  r"לכן לא בהכרח $\langle G', k\rangle \in VCM$.",
  contextId="e",
  note="Printed with '(4 נקודות)'. The PDF's first explanation sentence is garbled ('אם <G,k>∈VC אז ב-G יש לכל היותר קדקוד אחד "
       "שהדרגה שלו זוגית וכן יש ב-G כיסוי קדקודים בגודל k'); replaced by the deck's (slide 68) first sentence. Deck slide 68 "
       "also draws an example graph (not reproduced)."),

Q(24, "poly_reductions",
  r"אם $\langle G', k\rangle \in VCM$ אז מתקיים $\langle G, k\rangle \in VC$.",
  TF, "a",
  r"אם ב-$G'$ יש כיסוי קדקודים $C$ בגודל $k$, אז יש שתי אפשרויות:" "\n"
  r"אפשרות 1: $v_{new} \notin C$, ואז $C$ הוא כיסוי קדקודים ב-$G$ שגודלו $k$." "\n"
  r"אפשרות 2: $v_{new} \in C$, ואז $C - v_{new}$ הוא כיסוי קדקודים ב-$G$ בגודל $k-1$, ולכן יש גם כיסוי בגודל $k$ "
  "(אפשר לבחור קדקוד כלשהו ולהוסיף אותו לכיסוי).\n"
  r"בשני המקרים $\langle G, k\rangle \in VC$." "\n"
  r"**הערות (מצגת החזרה):** 1. העובדה שב-$G'$ יש לכל היותר קדקוד אחד בדרגה אי-זוגית, היא לא רלוונטית בכיוון הזה. "
  r"2. אם ב-$G$ יש רק $k-1$ קדקודים, אז הטענה לא נכונה. מכיוון שזה לא צוין מפורשות בשאלה, יש מקום לענות \"לא נכון\"...",
  contextId="e", confidence="low",
  note="Key (PDF highlight and deck slide 70) = נכון, but the PDF carries a green author note: 'הערה: אם ב-G יש רק k−1 קדקודים "
       "אז זה לא נכון... האם לשנות את התשובה ???', and the deck (slide 71) says 'יש מקום לענות \"לא נכון\"'. Kept the highlighted "
       "answer; confidence low. Printed with '(4 נקודות)'."),

# ---------------- חלק ו: שאלות אמריקאיות ----------------
Q(25, "mapping_reductions",
  r"נאמר ששפה $A$ היא $R$-שלמה אם $A$ ניתנת להכרעה וכן כל שפה ב-$R$ ניתנת לרדוקציה אל $A$ "
  r"(כלומר: $A$ היא $R$-שלמה אם $A \in R$ וכן לכל $B \in R$ מתקיים $B \le_m A$)." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts("כל שפה ב-$R$ היא $R$-שלמה",
       "אין אף שפה שהיא $R$-שלמה",
       "יש אינסוף שפות שהן $R$-שלמות",
       "יש ב-$R$ שפות שאינן $R$-שלמות, אבל מספרן סופי."),
  "d",
  r"יש רדוקציה מכל שפה ב-$R$ אל כל שפה אחרת פרט ל-$\emptyset$ ו-$\Sigma^*$." "\n"
  r"**מצגת החזרה:** ד: כל שפה לא טריוויאלית ב-$R$ היא $R$-שלמה, אבל ישנן שתי שפות טריוויאליות שלגביהן זה לא נכון... "
  r"ג: אם מספר השפות ב-$R$ שאינן $R$-שלמות הוא סופי, אז מספר השפות ב-$R$ שהינן $R$-שלמות הוא אינסופי. "
  "(כנראה שיש טעות, ושתי התשובות נכונות.)",
  acceptedIds=["d", "c"], confidence="med",
  note="DISAGREEMENT: the PDF highlights only ד; the review deck (slide 75) highlights both ג and ד and says "
       "'כנראה שיש טעות, ושתי התשובות נכונות'. correctId = ד (PDF key), ג accepted per the deck. Deck typo 'R-דלימות' fixed."),

Q(26, "tm",
  r"נתונה מ\"ט $M$ עם: $\Sigma = \{0,1\}$, $\Gamma = \{0,1,\sqcup\}$, $Q = \{q_0, q_1, q_2, q_{acc}, q_{rej}\}$." "\n"
  r"נניח שנתונה מילת קלט $w \in \Sigma^*$." "\n"
  "כמה קונפיגורציות שונות ייתכנו בריצה של $M$ על $w$ אם **ידוע** שהראש של המכונה לא מגיע לתא ה-$20$ משמאל?",
  opts(("math", r"5 \cdot 3^{20}"), ("math", r"5 \cdot 2^{20} \cdot 3^{20}"), ("math", r"20^3 \cdot 5"),
       ("math", r"3^{20} \cdot 20 \cdot 5"), ("math", r"3^{5 \cdot 20}"),
       "לא ניתן לקבוע בלי לדעת האם $M$ דטרמיניסטית או א\"ד."),
  "d",
  "מספר האפשרויות הוא:\n$3^{20}$ אפשרויות לתוכן הסרט.\n$5$ אפשרויות למצב הנוכחי.\n$20$ אפשרויות למיקום הראש.\n"
  r"לכן, סה\"כ: $3^{20} \cdot 20 \cdot 5$." "\n"
  "(קונפיגורציה היא שלשה של מצב, מיקום הראש הקורא ותוכן הסרט.)"),

Q(27, "npc",
  r"יהיו $A, B \in NP$ ו-$C \in NPC$. איזו מהטענות הבאות בהכרח מתקיימת?",
  opts(("math", r"A \le_p B"), ("math", r"A \le_p C"), BOTH, NONE_ANS),
  "b",
  r"$C \in NPC$, לכן יש רדוקציה פולינומית אל $C$ מכל שפה ששייכת ל-$NP$." "\n"
  r"אין אינפורמציה לגבי $A$ ו-$B$ שלפיה ניתן לקבוע האם מתקיים $A \le_p B$.",
  lockOrder=True),

Q(28, "npc",
  r"אם $A, B \in NP$ ומתקיים $A \le_p B$, אזי בהכרח:",
  opts(r"אם $B \in NPC$ אז $A \in NPC$.", r"אם $A \in NPC$ אז $B \in NPC$.", BOTH, NONE_ANS),
  "b",
  r"לפי משפט: אם $A \in NPC$ וגם $B \in NP$ אז $B \in NPC$." "\n"
  r"(מתוך הגדרת $NPC$ — שכל שפה אחרת ב-$NP$ ניתנת לרדוקציה אליה — ומתוך הטרנזיטיביות של יחס הרדוקציה.)",
  lockOrder=True),

Q(29, "npc",
  r"יהיו $A \in NP$, ו-$B, C \in NPC$. אילו מהרדוקציות הבאות בהכרח מתקיימות:" "\n"
  r"(1) $A \le_p B$" "\n" r"(2) $B \le_p A$" "\n" r"(3) $B \le_p C$",
  opts("(1)", "(2)", "(1), (2) ו-(3)", "(1) ו-(3)", "(2) ו-(3)"),
  "d",
  r"לפי ההגדרה, אם $L \in NPC$ אז $L \in NP$ וגם לכל $L' \in NP$ מתקיים $L' \le_p L$." "\n"
  r"$B, C \in NPC$ וכן $A \in NP$, לכן קיימות רדוקציות פולינומיות מכל אחת משלוש השפות אל $B$ וגם אל $C$."),
]

exam = {
  "examCode": "SAMP-2",
  "examLabel": "מבחן לדוגמה 2 (תש\"פ)",
  "year": 2020,
  "sourceFile": "מבחנים/מבחנים לדוגמה/בחינה לדוגמה עם הסברים.pdf",
  "keyFile": "same file (yellow highlights + red explanations); cross-checked and enriched from "
             "'מצגות חזרה למבחן/ פתרון מבחן לדוגמא תשפ אלישבע סמסטר ב 2025.pdf' slides 1-82",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 30))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
