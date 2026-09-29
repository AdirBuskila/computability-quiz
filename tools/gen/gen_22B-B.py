# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-B.json (2022 סמסטר ב מועד ב, 24.7.2022, ד"ר רדאל בן-אב).
NO answer key exists (the no-sol file and its byte-duplicate in חומרים אחרים carry no marks; the
pen-like squiggle left of Q2 on p.2 is page content, not an answer). All answers are SOLVED
(tools/SOLVE_GUIDE.md stage 1, official: False). Transcribed from the rendered pages
tools/raw/22B-B-F0 (text layer used for wording only).
Run: PYTHONUTF8=1 py tools/gen/gen_22B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-B.json"
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

def J(*paras):
    return "\n".join(paras)

TRI = opts("אף פעם לא נכון", "תמיד נכון", "יכול להיות נכון ויכול להיות לא נכון.")
DEC4 = opts(
    "$L$ ניתנת להכרעה.",
    "$L$ ניתנת לקבלה אבל לא ניתנת להכרעה.",
    r"$L$ לא ניתנת לקבלה אבל $\overline{L}$ כן ניתנת לקבלה.",
    r"$L$ לא ניתנת לקבלה וגם $\overline{L}$ לא ניתנת לקבלה.",
)
YESNO = opts("כן", "לא")
NONE = "אף תשובה אינה נכונה"

def rel(x, y):
    return opts(("math", rf"{x} = {y}"), ("math", rf"{x} \subset {y}"), ("math", rf"{x} \supset {y}"), NONE)

def Q(num, topic, question, options, correct, explanation, **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "solved", "official": False,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

contexts = {
  "rel": {"kind": "text", "title": "יחסים בין שפות – הגדרות לשאלות 9–11",
          "text": r"ידוע כי $\overline{E_{TM}} \le_m A_{TM}$ וכמו כן $A_{TM} \le_m \overline{E_{TM}}$. השאלות בחלק זה מתייחסות להגדרות הבאות:" "\n"
                  r"$$A = \{L \mid E_{TM} \le_m \overline{L}\}$$"
                  r"$$B = \{L \mid A_{TM} \le_m L\}$$"
                  r"$$C = \{L \mid \overline{E_{TM}} \le_m L \ \vee\ \overline{L} \le_m E_{TM}\}$$"
                  "(בהגדרת $C$ מודפס \"או\" בין שני התנאים.)"},
  "map": {"kind": "text", "title": "רדוקציית מיפוי – הגדרות לשאלות 12–14",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n**שפות:**\n"
                  r"$$INF_{TM} = \{\langle M_1, M_2\rangle \mid L(M_1) \cup L(M_2) = \Sigma^*\}$$"
                  r"$$CE_{TM} = \{\langle M\rangle \mid \overline{L(M)} = \emptyset\}$$"
                  "**פונקציות מיפוי:**\n"
                  r"$$f(\langle M_1, M_2\rangle) = \langle T_{M_1,M_2}\rangle$$"
                  "כאשר המכונה $T_{M_1,M_2}$ מוגדרת באופן הבא:\n"
                  "$T_{M_1,M_2}$ על קלט $w$:\n"
                  "1. הרץ את $M_2$ ואת $M_1$ במקביל על הקלט $w$.\n"
                  "2. תוך כדי הריצה בדוק אם אחת מהמכונות סיימה במצב \"מקבל\" אזי סיים במצב \"מקבל\".\n"
                  "3. אם שתיהן סיימו במצב \"דוחה\" אזי סיים במצב \"דוחה\""},
  "poly": {"kind": "text", "title": "רדוקציה פולינומית – הגדרות לשאלות 15–17",
           "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\nבעיית הקבוצה הבלתי תלויה מוגדרת באפון הבא:\n"
                   r"$$GSAT = \{\langle \phi, k\rangle \mid (*)\}$$"
                   "(*): $\\phi$ נוסחה ספיקה בצורת $CNF$, $k$ מספר כלשהו, כך שיש בה לכל היותר $k$ משתנים בעלי ערך אמת\n"
                   "נגדיר בעיה נוספת:\n"
                   r"$$ESAT = \{\langle \phi, k\rangle \mid (**)\}$$"
                   "(**): $\\phi$ נוסחה ספיקה בצורת $CNF$, $k$ מספר זוגי, כך שיש בה לכל היותר $k$ משתנים בעלי ערך אמת\n"
                   r"רוצים להוכיח כי $GSAT \le_P ESAT$. נגדיר את $f$ פונקציית המיפוי הבאה:" "\n"
                   r"$$f(\langle \phi, k\rangle) = \langle \phi', k'\rangle$$"
                   r"אם $k$ זוגי: $\phi' = \phi$, $k' = k$" "\n"
                   r"אם $k$ איזוגי: $\phi' = \phi \wedge (x_n \vee x_f)$, $k' = k+1$" "\n"
                   r"$x_f$ הוא משתנה שמקבל ערך $x_f = F$ בכל ההצבות המינימליות של $\phi$," "\n"
                   r"$x_n$ הוא משתנה חדש שלא הופיע ב-$\phi$." "\n"
                   "לפניך מספר טענות. לכל טענה עליך לקבוע האם היא נכונה או לא."},
}

questions = [
Q(1, "closure",
  r"$L_1 \notin RE$ וגם $L_2 \in RE \setminus R$, אזי $\overline{L_1} \cup \overline{L_2} \ne \Sigma^*$.",
  TRI, "c",
  J(r"""לפי דה-מורגן $\overline{L_1} \cup \overline{L_2} = \overline{L_1 \cap L_2}$, ולכן הטענה שקולה ל-$L_1 \cap L_2 \ne \emptyset$ – וזה תלוי בבחירת השפות.""",
    r"""**יכול להיות לא נכון:** $L_2 = A_{TM}$, $L_1 = \overline{A_{TM}}$ (לא ניתנת לקבלה). אז $L_1 \cap L_2 = \emptyset$ ולכן $\overline{L_1} \cup \overline{L_2} = \Sigma^*$.""",
    r"""**יכול להיות נכון:** $L_2 = A_{TM}$, $L_1 = \overline{A_{TM}} \cup \{x_0\}$ עבור $x_0 \in A_{TM}$ כלשהו. $L_1 \notin RE$ (אחרת גם $\overline{A_{TM}} = L_1 \setminus \{x_0\}$ הייתה ניתנת לקבלה), ו-$L_1 \cap L_2 = \{x_0\} \ne \emptyset$.""",
    "לכן א ו-ב אינן נכונות, והתשובה ג.")),

Q(2, "closure",
  r"אם $L_1 \in R$ ו-$L_2 \in RE$, אזי $\overline{L_1} \cap L_2 \in RE$",
  TRI, "b",
  J(r"""$R$ סגורה למשלים ולכן $\overline{L_1} \in R \subseteq RE$. $RE$ סגורה לחיתוך, ולכן תמיד $\overline{L_1} \cap L_2 \in RE$ (מכונה מקבלת: הרץ את המכריעה של $L_1$ ודחה אם קיבלה; אחרת הרץ את המקבלת של $L_2$).""",
    "לכן הטענה תמיד נכונה, ו-א, ג אינן נכונות.")),

Q(3, "closure",
  r"נניח שקיימת קבוצה אין סופית של שפות $\{L_i \mid 1 \le i \le \infty\}$ כך ש-$L_i \in RE \setminus R$." "\n"
  r"נגדיר $L_\infty = \bigcup_{i=1}^{i=\infty} L_i$. איזה משפט מהבאים נכון?",
  opts(("math", r"L_\infty \in R"), ("math", r"L_\infty \notin RE"), ("math", r"L_\infty \in RE"), ("math", r"L_\infty \in P")),
  "c",
  J(r"""אין אף אפשרות שנכונה תמיד – כל ארבע האפשרויות יכולות להתקיים:""",
    r"""• $L_i = A_{TM} \cup \{x \mid |x| \le i\}$: כל $L_i \in RE \setminus R$, והאיחוד הוא $\Sigma^*$ – ב-$P$ וב-$R$.""",
    r"""• $L_i = 0A_{TM} \cup \{1^j \mid j \le i\}$: האיחוד $0A_{TM} \cup 1^*$ ב-$RE \setminus R$.""",
    r"""• $L_i = 0A_{TM} \cup \{1y_i\}$ כאשר $y_1, y_2, \dots$ הן המילים של $\overline{A_{TM}}$: האיחוד $0A_{TM} \cup 1\overline{A_{TM}}$ אינו ב-$RE$."""),
  hold="No option is always true: without the chain condition L_i ⊆ L_{i+1} (present in 22B-A Q5), the union "
       "of RE\\R languages can be Σ* (∈P, ∈R), RE\\R, or not RE (examples in the explanation). "
       "Likely intended ג (RE closed under union) but that is false for infinite unions -> hold.",
  note="Set printed as '{L_i  1 ≤ i ≤ ∞}' (no separator bar); a \\mid was added."),

Q(4, "np",
  r"אם $P \ne coNP$ אז $\overline{CLIQUE} \notin NP$.",
  opts("נכון", "לא נכון", "אין מספיק מידע"), "c",
  J(r"""$P$ סגורה למשלים, לכן $P = NP \Leftrightarrow P = coNP$; כלומר ההנחה שקולה ל-$P \ne NP$.""",
    r"""$CLIQUE \in NPC$, ולכן $\overline{CLIQUE} \in NP$ אם ורק אם $NP = coNP$ (אם $\overline{CLIQUE} \in NP$ אז לכל $L \in NP$: $\overline{L} \le_p \overline{CLIQUE}$ ולכן $coNP \subseteq NP$, ומכאן שוויון).""",
    r"""השאלה האם $NP = coNP$ פתוחה גם בהנחה ש-$P \ne NP$: הנחה זו לא מוכיחה $\overline{CLIQUE} \notin NP$ (לכן לא א) וגם לא מפריכה זאת (לכן לא ב). התשובה: אין מספיק מידע."""),
  note="Parallel of 22B-A Q4 (official א for 'אם P=coNP אז CLIQUE̅ ∈ NP'); here the conclusion is independent of the hypothesis."),

Q(5, "tm",
  r"תהי $M_1$ מכונת טיורינג לא דטרמיניסטית שמקבלת שפה שלא ניתנת להכרעה. ותהי $M_2$ מכונת טיורינג שבנויה מהמכונה $M_1$ "
  "על ידי החלפת המצבים הדוחה במצב מקבל והשארת המצב המקבל ללא שינוי. אזי "
  r"$|\overline{L(M_2)} \cap \overline{L(M_1)}| \ne \infty$",
  TRI, "c",
  J(r"""כל ענף מקבל של $M_1$ נשאר מקבל ב-$M_2$, לכן $L(M_1) \subseteq L(M_2)$ ו-$\overline{L(M_2)} \cap \overline{L(M_1)} = \overline{L(M_2)}$ – המילים שעליהן **אף** ענף של $M_1$ לא עוצר.""",
    r"""**יכול להיות לא נכון:** $M_1$ = המכונה (הדטרמיניסטית) הרגילה המקבלת את $A_{TM}$: מריצה את $M$ על $w$ ועונה כמוה. אז $\overline{L(M_2)} = \{\langle M,w\rangle \mid M(w)\uparrow\}$ (הזוגות שבהם $M$ לא עוצרת על $w$) – קבוצה אינסופית.""",
    r"""**יכול להיות נכון:** $M_1$ על קלט $x$ בוחרת באופן לא דטרמיניסטי: ענף אחד דוחה מיד, והענף השני מריץ מקבלת של $A_{TM}$. $L(M_1) = A_{TM}$ (לא כריעה), אבל ב-$M_2$ הענף הראשון מקבל, כלומר $L(M_2) = \Sigma^*$ והחיתוך ריק (גודל $0 \ne \infty$).""",
    "לכן התשובה ג."),
  note="Printed 'החלפת המצבים הדוחה במצב מקבל' (sic)."),

Q(6, "classification",
  "לפניך הגדרות של שפות. לכל שפה, עליך לשייך אותה לאחת מהמחלקות המפורטות.\n"
  r"$$L = \{\langle M_1, M_2, M_3\rangle \mid |L(M_1)| + |L(M_2)| + |L(M_3)| \ge 0\}$$",
  DEC4, "a",
  J(r"""גודל של שפה תמיד $\ge 0$ (גם אם הוא אינסופי), ולכן התנאי מתקיים לכל שלישיית מכונות. $L$ היא פשוט קבוצת הקידודים התקינים של שלשות מכונות – מכונה שבודקת תקינות תחבירית של הקלט מכריעה אותה.""",
    r"""לכן $L \in R$, ו-ב, ג, ד אינן נכונות.""")),

Q(7, "classification",
  r"$$L = \{\langle M_1, M_2, w\rangle \mid (*)\}$$"
  r"(*): $w \in \Sigma^*$, $|L(M_1) \cap L(M_2)| < |w|$",
  DEC4, "c",
  J(r"""**$\overline{L} \in RE$:** $\langle M_1,M_2,w\rangle \in \overline{L}$ (עבור קלט תקין) אם"ם $|L(M_1) \cap L(M_2)| \ge |w|$. מכונה מקבלת: מריצה את $M_1, M_2$ במקביל על כל המילים (שיבוץ – dovetailing) ומקבלת ברגע שמצאה $|w|$ מילים שונות ששתיהן מקבלות.""",
    r"""**$L \notin RE$:** רדוקציה $\overline{A_{TM}} \le_m L$: $f(\langle M,x\rangle) = \langle N_{M,x}, N_{M,x}, 0\rangle$, כאשר $N_{M,x}$ על כל קלט מריצה את $M$ על $x$ ומקבלת אם $M$ קיבלה. אם $M$ לא מקבלת את $x$: $L(N) = \emptyset$ ו-$0 < 1$, כלומר $f(\langle M,x\rangle) \in L$. אם $M$ מקבלת את $x$: $L(N) = \Sigma^*$ והחיתוך אינסופי, כלומר $f(\langle M,x\rangle) \notin L$.""",
    r"""לכן $L \notin RE$ ו-$\overline{L} \in RE$: התשובה ג (ובפרט $L \notin R$, כך ש-א, ב, ד שגויות)."""),
  note="Printed as '{<M1,M2,w> | w∈Σ*   |L(M1)∩L(M2)| < |w|}' (two conditions separated by spaces); split to a (*) line."),

Q(8, "classification",
  r"נגדיר $h(\langle M,w\rangle)$ לפי:" "\n"
  r"• $h(\langle M,w\rangle) = 1$ אם $M$ מקבלת את $w$" "\n"
  r"• $h(\langle M,w\rangle) = 0$ אם $M$ לא מקבלת את $w$" "\n"
  r"$$L_h = \{\langle M, w\rangle \mid h(\langle M, w\rangle) > |w|^2\}$$",
  DEC4, "b",
  J(r"""$h \in \{0,1\}$ ו-$|w|^2 \ge 0$, ולכן $h > |w|^2$ אם"ם $h = 1$ וגם $|w| = 0$. כלומר $L_h = \{\langle M, \varepsilon\rangle \mid (*)\}$, כאשר (*): $M$ מקבלת את $\varepsilon$.""",
    r"""**$L_h \in RE$:** בודקים ש-$w = \varepsilon$ ומריצים את $M$ על $\varepsilon$; מקבלים אם קיבלה.""",
    r"""**$L_h \notin R$:** $A_{TM} \le_m L_h$ על ידי $f(\langle M,x\rangle) = \langle M_x, \varepsilon\rangle$, כאשר $M_x$ מתעלמת מהקלט ומריצה את $M$ על $x$. $M$ מקבלת את $x$ אם"ם $M_x$ מקבלת את $\varepsilon$.""",
    "לכן התשובה ב."),
  note="h is printed as a two-case brace with Hebrew conditions; rewritten as two bullet lines. The options say 'L' although the language is named L_h (as printed)."),

Q(9, "mapping_reductions", "קבע מהו היחס בין $A$ ל-$B$:", rel("A", "B"), "a",
  J(r"""$E_{TM} \le_m \overline{L} \Leftrightarrow \overline{E_{TM}} \le_m L$, ולכן $A = \{L \mid \overline{E_{TM}} \le_m L\}$.""",
    r"""מהנתון $\overline{E_{TM}} \le_m A_{TM}$ ו-$A_{TM} \le_m \overline{E_{TM}}$, ומטרנזיטיביות: $\overline{E_{TM}} \le_m L \Leftrightarrow A_{TM} \le_m L$. לכן $A = B$."""),
  contextId="rel"),
Q(10, "mapping_reductions", "קבע מהו היחס בין $B$ ל-$C$:", rel("B", "C"), "b",
  J(r"""$\overline{L} \le_m E_{TM} \Leftrightarrow L \le_m \overline{E_{TM}}$, ולכן (בעזרת השקילות $\overline{E_{TM}} \equiv A_{TM}$) $C = B \cup \{L \mid L \le_m A_{TM}\}$, כלומר $B \subseteq C$.""",
    r"""**ההכלה ממש:** $\emptyset \in C$ (כי $\emptyset \le_m A_{TM}$ – ממפים הכול למילה שאינה ב-$A_{TM}$), אבל $\emptyset \notin B$ (אין רדוקציה מ-$A_{TM} \ne \emptyset$ ל-$\emptyset$). לכן $B \subset C$."""),
  contextId="rel"),
Q(11, "mapping_reductions", "מה מהמשפטים הבאים נכון", rel("A", "C"), "b",
  r"""משאלות 9–10: $A = B$ ו-$B \subset C$, ולכן $A \subset C$ (אותה דוגמה: $\emptyset \in C \setminus A$).""",
  contextId="rel"),

Q(12, "mapping_reductions",
  r"האם $f(\langle M_1, M_2\rangle) = \langle T_{M_1,M_2}\rangle$ היא פונקציה ניתנת לחישוב?",
  YESNO, "a",
  r"""כן. $f$ רק כותבת את הקידוד של $T_{M_1,M_2}$ (תבנית קבועה שמשולבים בה הקידודים של $M_1, M_2$) ואינה מריצה אף מכונה, ולכן היא מחושבת על ידי מכונה שעוצרת תמיד.""",
  contextId="map",
  note="Option ב 'לא' is printed bold (formatting artifact, as in 22B-A). Same stem as 22B-A Q12 but a different T box, so the 22B-A key was not reused — solved (same answer)."),
Q(13, "mapping_reductions",
  "אם $M_1$ וגם $M_2$ הן מכונות שלא מכריעות שפה. אזי האם מתקיים\n"
  r"$f(\langle M_1, M_2\rangle) \in CE_{TM} \Leftrightarrow \langle M_1, M_2\rangle \in INF_{TM}$?",
  YESNO, "a",
  J(r"""$T_{M_1,M_2}$ מריצה את שתי המכונות **במקביל** ומקבלת ברגע שאחת מהן מקבלת; לכן גם אם אחת מהן לא עוצרת, $T$ מקבלת את $w$ אם"ם $w \in L(M_1) \cup L(M_2)$. כלומר $L(T_{M_1,M_2}) = L(M_1) \cup L(M_2)$ לכל שתי מכונות (בפרט כאלה שלא מכריעות).""",
    r"""$\langle T\rangle \in CE_{TM} \Leftrightarrow \overline{L(T)} = \emptyset \Leftrightarrow L(M_1) \cup L(M_2) = \Sigma^* \Leftrightarrow \langle M_1,M_2\rangle \in INF_{TM}$. לכן כן."""),
  contextId="map"),
Q(14, "mapping_reductions",
  r"האם $f$ היא מקיימת את תנאי המיפוי ברדוקציה עבור $INF_{TM} \le_m CE_{TM}$?",
  opts("כן",
       "לא כי הכיוון של הרדוקציה הוא הפוך.",
       r"לא כי קיימת מילה $w = \langle M_1, M_2\rangle$ שמקיימת $w \in INF_{TM}$ אבל $f(w) \notin CE_{TM}$",
       r"לא כי קיימת מילה $w = \langle M_1, M_2\rangle$ שמקיימת $w \notin INF_{TM}$ אבל $f(w) \in CE_{TM}$"),
  "a",
  J(r"""$f$ ניתנת לחישוב (שאלה 12), ולכל זוג מכונות $L(T_{M_1,M_2}) = L(M_1) \cup L(M_2)$ (שאלה 13), ולכן $w \in INF_{TM} \Leftrightarrow f(w) \in CE_{TM}$. זו בדיוק רדוקציה בכיוון $INF_{TM} \le_m CE_{TM}$.""",
    "לכן ב (הכיוון נכון), ג ו-ד (אין מילה כזו) שגויות."),
  contextId="map", note="Stem prints 'אם ה f היא מקיימת' (sic); normalized to 'האם f היא מקיימת'."),

Q(15, "poly_reductions",
  r"אם $\langle \phi, k\rangle \in GSAT$ אז $f(\langle \phi, k\rangle) \in ESAT$.",
  opts("נכון רק אם מספר המשתנים ב-$\\phi$ הינו מספר זוגי",
       "נכון רק עבור $k$ זוגי.",
       "לא בהכרח נכון. כלומר לכל $k$ - יכול להיות נכון ויכול להיות לא נכון.",
       "נכון תמיד"),
  "d",
  J(r"""**$k$ זוגי:** $f$ היא הזהות ו-$k' = k$ זוגי, ולכן $f(\langle\phi,k\rangle) \in ESAT$.""",
    r"""**$k$ אי-זוגי:** יש הצבה מספקת ל-$\phi$ עם לכל היותר $k$ משתני אמת. נרחיב אותה ב-$x_n = T$: הפסוקית $(x_n \vee x_f)$ מסופקת, ויש לכל היותר $k+1 = k'$ משתני אמת, ו-$k'$ זוגי. לכן $f(\langle\phi,k\rangle) \in ESAT$.""",
    "הטענה נכונה תמיד, ללא תלות במספר המשתנים או בזוגיות של $k$."),
  contextId="poly"),
Q(16, "poly_reductions",
  r"אם $\langle \phi, k\rangle \notin GSAT$ אז $f(\langle \phi, k\rangle) \notin ESAT$.",
  opts("נכון רק אם מספר הקודקודים ב-$G$ זוגי",
       "נכון רק אם $k$ זוגי",
       "נכון תמיד",
       "המשפט לא מתקיים. כלומר יש מקרים שבהם נכון ויש מקרים בהם איננו נכון."),
  "c",
  J(r"""**$k$ זוגי:** $f$ היא הזהות, והטענה מיידית.""",
    r"""**$k$ אי-זוגי:** נניח בשלילה ש-$\phi'$ מסופקת על ידי הצבה $\sigma$ עם לכל היותר $k+1$ משתני אמת. הצמצום של $\sigma$ למשתני $\phi$ מספק את $\phi$. אם $\sigma(x_n) = T$ אז ב-$\phi$ יש לכל היותר $k$ משתני אמת – בסתירה ל-$\langle\phi,k\rangle \notin GSAT$. אחרת $\sigma(x_f) = T$, ו-$\sigma$ היא הצבה מספקת של $\phi$ עם לכל היותר $k+1$ משתני אמת; מכיוון שאין הצבה עם $\le k$, זו הצבה מינימלית (מספר משתני האמת בה מינימלי, ולכן היא גם מינימלית ביחס להכלה) שבה $x_f = T$ – בסתירה להגדרת $x_f$.""",
    "לכן הטענה נכונה תמיד."),
  contextId="poly",
  note="Option א mentions 'מספר הקודקודים ב G' — a copy-paste leftover from 22B-A (the section is about formulas); kept as printed."),
Q(17, "poly_reductions",
  r"האם ההוכחה הנ\"ל מוכיחה כי $GSAT \le_p ESAT$?",
  opts("לא נכון כי הפונקציה $f$ שהוגדרה לא מקיימת את כל תנאי הרדוקציה הפולינומיאלית",
       "נכון כי הפונקציה $f$ שהוגדרה מקיימת את כל תנאי הרדוקציה הפולינומיאלית",
       "למרות שהפונקציה $f$ שהוגדרה לא מקיימת את תנאי הרדוקציה הפולינומיאלית – ההוכחה נכונה",
       "הפונקציה $f$ שהוגדרה מקיימת את תנאי הרדוקציה ובכל זאת המשפט לא נכון."),
  "a",
  J(r"""תנאי ההתאמה ($x \in GSAT \Leftrightarrow f(x) \in ESAT$) מתקיימים (שאלות 15–16), אבל $f$ **אינה ניתנת לחישוב בזמן פולינומיאלי**: כדי לבחור את $x_f$ יש לדעת אילו משתנים שקריים בכל ההצבות המינימליות של $\phi$ – בפרט לדעת אם $\phi$ ספיקה בכלל, בעיה $NP$-קשה. יתרה מזו, משתנה כזה לא תמיד קיים (למשל $\phi = x_1$), ואז $f$ אפילו לא מוגדרת.""",
    r"""לכן $f$ אינה רדוקציה פולינומיאלית (א). ג שגויה – הוכחה שנשענת על $f$ פסולה אינה נכונה; ב ו-ד שגויות כי $f$ לא מקיימת את התנאים."""),
  contextId="poly",
  note="Same design as 22B-A Q15–17 (official 15ד 16ג 17א, where f used a maximum clique — not poly-time computable)."),

Q(18, "npc",
  r"נניח שקיימות שפות $A$ ו-$B$ כך שמתקיימים $B \le_P A$ וכן $A \in NPC$ ו-$B \notin P$. מה מהבאים הכרחי",
  opts(("math", r"NP = coNP"), ("math", r"NP \cap coNP = P"), ("math", r"P \ne NP"), ("math", r"P = NP")),
  "c",
  J(r"""אם $A \in P$ אז מ-$B \le_p A$ נקבל $B \in P$ – סתירה. לכן $A \notin P$, ומכיוון ש-$A \in NPC \subseteq NP$ נקבל $NP \ne P$ (ג).""",
    r"""**ד** סותרת את ג. **א, ב:** אינן נובעות מהנתונים – הנתונים שקולים ל-$P \ne NP$ (אם $P \ne NP$ ניקח $A = B = SAT$), ו-$P \ne NP$ אינו מכריע את השאלות הפתוחות $NP = coNP$ או $NP \cap coNP = P$.""")),
Q(19, "npc",
  r"תהיינה $A$ ו-$B$ שפות כך ש: $A \in NP$, $B \le_p \overline{A}$, $B \in NPC$." "\n"
  "האם נובע מנתונים אלה ש-$NP=coNP$?",
  opts("כן", "לא", r"רק אם $NP \cap coNP \ne P$.", r"רק אם $B \notin coNP$"),
  "a",
  J(r"""$B \le_p \overline{A} \Rightarrow \overline{B} \le_p A \in NP$, ולכן $\overline{B} \in NP$, כלומר $B \in coNP$.""",
    r"""לכל $L \in NP$: $L \le_p B$ (כי $B \in NPC$), ולכן $\overline{L} \le_p \overline{B} \in NP$, כלומר $L \in coNP$. קיבלנו $NP \subseteq coNP$, ומכאן גם $coNP \subseteq NP$ (אם $L \in coNP$ אז $\overline{L} \in NP \subseteq coNP$, כלומר $L \in NP$). לכן $NP = coNP$ נובע ללא תנאים נוספים (א); ג, ד מיותרות/שגויות, ו-ב שגויה.""")),
Q(20, "npc",
  "נגדיר את השפה $MCLIQUE$:\n"
  r"$$MIS2 = \{\langle \phi\rangle \mid (*)\}$$"
  r"(*): $G$ גרף לא מכוון, $V(G)$ = מספר הקודקודים ב-$G$, $\langle G, (V(G)-2)\rangle \in IS$" "\n"
  r"איזו מהטענות הבאות נכונה? (בהנחה ש-$P \ne NP$)",
  opts(("math", r"MIS2 \in NPC"), ("math", r"MIS2 \in P"), ("math", r"MIS2 \notin NP - NPC"), NONE),
  "b",
  J(r"""**$MIS2 \in P$:** יש בגרף עם $n$ קודקודים קבוצה בלתי תלויה בגודל $n-2$ אם"ם קיימים שני קודקודים שהסרתם משאירה קבוצה ללא צלעות. עוברים על כל $\binom{n}{2} = O(n^2)$ הזוגות, ולכל זוג בודקים בזמן פולינומיאלי שאין צלע בין הקודקודים הנותרים (אם $n \le 2$ – התשובה כן מיידית).""",
    r"""**הפרכת א:** אם $MIS2 \in NPC$ ו-$MIS2 \in P$ אז $P = NP$, בניגוד להנחה. **הפרכת ג:** $MIS2 \in P \subseteq NP$ ו-$MIS2 \notin NPC$, כלומר $MIS2 \in NP - NPC$. **ד** שגויה כי ב נכונה."""),
  note="Printed heading says 'נגדיר את השפה MCLIQUE' but defines MIS2, and the set is written over <φ> while the conditions are about a graph G (copy-paste from 22B-A); kept as printed — the intended language is {<G> | G has an independent set of size |V(G)|-2}."),
]

# --- RESOLUTIONS (ASK_ADIR items resolved by independent math check; Adir authorized 2026-09-29) ---
def _resolve(num, **kw):
    q = next(q for q in questions if q["num"] == num)
    q.pop("hold", None)
    q.update(kw)
# Stage-2 blind verification (tools/raw/_verify_22B-B.json): 18/20 agree.
_resolve(5, hold=r"""Stage-2 verifier not confident: c holds if M1 may be nondeterministic (an immediate-reject branch), but the intended deterministic reading gives a.""")

exam = {
  "examCode": "22B-B",
  "examLabel": "2022 סמסטר ב מועד ב",
  "year": 2022,
  "examDate": "24.7.2022",
  "sourceFile": "מבחנים/2022/סמסטר ב/2022-07-24-Exam-חישוביות-2022-moedB-גרסא-0 no-sol.pdf",
  "keyFile": "none — all answers solved (tools/SOLVE_GUIDE.md stage 1, unofficial)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 21))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
