# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-C.json (2022 סמסטר ב מועד ג, 21.8.2022, ד"ר רדאל בן-אב).
NO official key. Text transcribed from the clean copy `מבחנים/2022/סמסטר ב/סמסטר  ב מועד ג 21-8-22.pdf`
(renders tools/raw/22B-C-HEB). The "SOLUTION" file (renders tools/raw/22B-C-SOL) holds a tutor's
2024 handwritten ink (circled 1ב 2א 3א 5ב 6ב 7ג 8ג 9ג 10א 11ג 12א 13ב 14ד; Q4 and Q15–20 crossed
out / unanswered) — used as partial evidence only (see `note`). All answers SOLVED
(tools/SOLVE_GUIDE.md stage 1, official: False).
Run: PYTHONUTF8=1 py tools/gen/gen_22B-C.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-C.json"
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
    # 22B-C prints the third option as "y ⊂ x" (not "x ⊃ y" as in 22B-A/B)
    return opts(("math", rf"{x} = {y}"), ("math", rf"{x} \subset {y}"), ("math", rf"{y} \subset {x}"), NONE)

def Q(num, topic, question, options, correct, explanation, **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "solved", "official": False,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

TUT = "tutor's 2024 ink (22B-C SOLUTION file) circled "

contexts = {
  "rel": {"kind": "text", "title": "יחסים בין שפות – הגדרות לשאלות 9–11",
          "text": r"ידוע כי $\overline{E_{TM}} \le_m A_{TM}$ וכמו כן $A_{TM} \le_m \overline{E_{TM}}$. השאלות בחלק זה מתייחסות להגדרות הבאות:" "\n"
                  r"$$A = \{L \mid \overline{E_{TM}} \le_m L \ \vee\ L \le_m \overline{E_{TM}}\}$$"
                  r"$$B = \{L \mid E_{TM} \le_m \overline{L}\}$$"
                  r"$$C = \{L \mid A_{TM} \le_m L\}$$"
                  "(בהגדרת $A$ מודפס \"או\" בין שני התנאים.)"},
  "map": {"kind": "text", "title": "רדוקציית מיפוי – הגדרות לשאלות 12–14",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n**שפות:**\n"
                  r"$$ALL_{TM} = \{\langle M_1, M_2\rangle \mid L(M_1) \cup L(M_2) = \Sigma^*\}$$"
                  r"$$CE_{TM} = \{\langle M\rangle \mid \overline{L(M)} = \emptyset\}$$"
                  "**פונקציות מיפוי:**\n"
                  r"$$f(\langle M_1, M_2\rangle) = \langle T_{M_1,M_2}\rangle$$"
                  "כאשר המכונה $T_{M_1,M_2}$ מוגדרת באופן הבא:\n"
                  "$T_{M_1,M_2}$ על קלט $w$:\n"
                  "1. הרץ את $M_1$ על $w$\n"
                  "2. אם $M_2$ קיבלה אזי עצור וקבל\n"
                  "3. הרץ את $M_2$ על $w$\n"
                  "4. אם $M_1$ קיבלה אזי עצור וקבל.\n"
                  "5. אם שתיהן סיימו במצב \"דוחה\" אזי סיים במצב \"דוחה\""},
  "poly": {"kind": "text", "title": "רדוקציה פולינומית – הגדרות לשאלות 15–17",
           "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\nבעיית הקבוצה הבלתי תלויה מוגדרת באפון הבא:\n"
                   r"$$GSAT = \{\langle \phi, k\rangle \mid (*)\}$$"
                   "(*): $\\phi$ נוסחה ספיקה בצורת $CNF$, $k$ מספר כלשהו, כך שיש בה לכל היותר $k$ משתנים בעלי ערך אמת\n"
                   "נגדיר בעיה נוספת:\n"
                   r"$$ESAT = \{\langle \phi, k\rangle \mid (**)\}$$"
                   "(**): $\\phi$ נוסחה ספיקה בצורת $CNF$, $k$ מספר זוגי, כך שיש בה לכל היותר $k$ משתנים בעלי ערך אמת\n"
                   r"רוצים להוכיח כי $GSAT \le_P ESAT$. נגדיר את $f$ פונקציית המיפוי הבאה:" "\n"
                   r"$$f(\langle \phi, k\rangle) = \langle \phi', k'\rangle$$"
                   r"אם $k$ איזוגי: $k' = 2k$, $\phi' = \phi \wedge \phi''$" "\n"
                   r"$\phi''$ היא נוסחא שזהה ל-$\phi$ אבל בסט משתנים חדש לחלוטין" "\n"
                   "לפניך מספר טענות. לכל טענה עליך לקבוע האם היא נכונה או לא."},
}

questions = [
Q(1, "closure",
  r"$L_1 \in RE$ וגם $L_2 \in RE \setminus R$, אזי $|\overline{L_1} \cup \overline{L_2}| = \infty$.",
  TRI, "b",
  J(r"""$L_2 \notin R$ ולכן גם $\overline{L_2} \notin R$ ($R$ סגורה למשלים). כל שפה סופית ניתנת להכרעה, ולכן $\overline{L_2}$ אינסופית.""",
    r"""$\overline{L_2} \subseteq \overline{L_1} \cup \overline{L_2}$, ולכן גם האיחוד אינסופי – תמיד. א, ג שגויות."""),
  note=TUT + "ב — agrees."),

Q(2, "closure",
  r"אם $L_1 \in R$ ו-$L_2 \in RE \setminus R$, אזי $\overline{L_1} \cap L_2 \notin RE$",
  TRI, "a",
  J(r"""$\overline{L_1} \in R \subseteq RE$ ו-$L_2 \in RE$, ו-$RE$ סגורה לחיתוך; לכן תמיד $\overline{L_1} \cap L_2 \in RE$.""",
    "הטענה $\\overline{L_1} \\cap L_2 \\notin RE$ לעולם אינה נכונה (א); ב, ג שגויות."),
  note=TUT + "א — agrees."),

Q(3, "closure",
  r"נניח שקיימת קבוצה אין סופית של שפות $\{L_i \mid 1 \le i \le \infty\}$ כך ש-$|L_i| \ne \infty$, כלומר כל השפות סופיות." "\n"
  r"נגדיר $L_\infty = \bigcap_{i=1}^{i=\infty} L_i$. איזה משפט מהבאים נכון?",
  opts(("math", r"L_\infty \in R"), ("math", r"L_\infty \notin RE"), ("math", r"L_\infty \in RE \setminus R"), ("math", r"L_\infty \notin R")),
  "a",
  J(r"""$L_\infty \subseteq L_1$ ו-$L_1$ סופית, לכן $L_\infty$ סופית. כל שפה סופית ניתנת להכרעה (מכונה עם טבלה סופית של המילים), ולכן $L_\infty \in R$.""",
    r"""מכאן $L_\infty \in RE$ (ב שגויה), $L_\infty \notin RE \setminus R$ (ג שגויה) ו-$L_\infty \in R$ (ד שגויה)."""),
  note=TUT + "א — agrees. Set printed as '{L_i  1 ≤ i ≤ ∞}' (no separator bar); a \\mid was added."),

Q(4, "np",
  r"אם $P = coNP$ אז $\overline{CLIQUE} \notin NP$.",
  opts("נכון", "לא נכון", "אין מספיק מידע"), "b",
  J(r"""$P$ סגורה למשלים, ולכן אם $P = coNP$ אז $NP = coP = P$. אז $\overline{CLIQUE} \in coNP = P \subseteq NP$ – כלומר תחת ההנחה המסקנה $\overline{CLIQUE} \notin NP$ **שגויה**, ולכן \"לא נכון\" (ב)."""),
  hold="Two readings give different answers: as 'assume P=coNP; is CLIQUE̅∉NP?' the conclusion is refuted -> ב; "
       "as a material implication the statement is equivalent to P≠coNP (i.e. P≠NP), an open problem -> ג (אין מספיק מידע). "
       "The tutor's ink crosses Q4 out with no circle.",
  note="Tutor's 2024 ink: Q4 crossed out with a red X, no answer circled. Parallel of 22B-A Q4 (official א for 'אם P=coNP אז CLIQUE̅ ∈ NP')."),

Q(5, "tm",
  r"תהי $M_1$ מכונת טיורינג לא דטרמיניסטית שמקבלת שפה שלא ניתנת להכרעה. ותהי $M_2$ מכונת טיורינג שבנויה מהמכונה $M_1$ "
  "על ידי החלפת המצב המקבל במצב דוחה והשארת המצב הדוחה ללא שינוי. אזי "
  r"$|\overline{L(M_2)} \cap \overline{L(M_1)}| = \infty$",
  TRI, "b",
  J(r"""ב-$M_2$ אין מצב מקבל, ולכן $L(M_2) = \emptyset$ ו-$\overline{L(M_2)} = \Sigma^*$. לכן $\overline{L(M_2)} \cap \overline{L(M_1)} = \overline{L(M_1)}$.""",
    r"""$L(M_1) \notin R$, ולכן גם $\overline{L(M_1)} \notin R$; שפה סופית ניתנת להכרעה, ולכן $\overline{L(M_1)}$ אינסופית – תמיד (ב)."""),
  note=TUT + "ב — agrees."),

Q(6, "classification",
  "לפניך הגדרות של שפות. לכל שפה, עליך לשייך אותה לאחת מהמחלקות המפורטות.\n"
  r"$$L = \{\langle M_1, M_2, M_3\rangle \mid |L(M_1)| + |L(M_2)| + |L(M_3)| > 0\}$$",
  DEC4, "b",
  J(r"""התנאי שקול ל\"לפחות אחת מהשפות $L(M_i)$ לא ריקה\".""",
    r"""**$L \in RE$:** מריצים את שלוש המכונות במקביל על כל המילים (שיבוץ) ומקבלים ברגע שאחת מקבלת מילה כלשהי.""",
    r"""**$L \notin R$:** $\overline{E_{TM}} \le_m L$ על ידי $f(\langle M\rangle) = \langle M, M, M\rangle$: $L(M) \ne \emptyset$ אם"ם הסכום חיובי. $\overline{E_{TM}} \notin R$, ולכן $L \notin R$ (ב)."""),
  note=TUT + "ב — agrees."),

Q(7, "classification",
  r"$$L = \{\langle M_1, M_2, w\rangle \mid (*)\}$$"
  r"(*): $w \in \Sigma^*$, $|L(M_1) \cap L(M_2)| < |w|^2$",
  DEC4, "c",
  J(r"""**$\overline{L} \in RE$:** קלט תקין שייך ל-$\overline{L}$ אם"ם $|L(M_1) \cap L(M_2)| \ge |w|^2$. מריצים את $M_1, M_2$ במקביל על כל המילים (שיבוץ) ומקבלים ברגע שנמצאו $|w|^2$ מילים שונות ששתיהן מקבלות.""",
    r"""**$L \notin RE$:** $\overline{A_{TM}} \le_m L$ על ידי $f(\langle M,x\rangle) = \langle N_{M,x}, N_{M,x}, 0\rangle$, כאשר $N_{M,x}$ על כל קלט מריצה את $M$ על $x$ ומקבלת אם $M$ קיבלה. אם $M$ לא מקבלת את $x$: $L(N) = \emptyset$ ו-$0 < 1$, כלומר בתמונה ב-$L$; אם $M$ מקבלת את $x$: החיתוך הוא $\Sigma^*$ (אינסופי) ולכן לא ב-$L$.""",
    "לכן התשובה ג."),
  note=TUT + "ג — agrees. Printed as '{<M1,M2,w> | w∈Σ*   |L(M1)∩L(M2)| < |w|^2}'; split to a (*) line."),

Q(8, "classification",
  r"נגדיר $h(\langle M,w\rangle)$ לפי:" "\n"
  r"• $h(\langle M,w\rangle) = 1$ אם $M$ מקבלת את $w$" "\n"
  r"• $h(\langle M,w\rangle) = 0$ אם $M$ לא מקבלת את $w$" "\n"
  r"$$L_h = \{\langle M, w\rangle \mid h(\langle M, w\rangle) < |w|^2\}$$",
  DEC4, "c",
  J(r"""$h \in \{0,1\}$. אם $|w| \ge 2$ אז $|w|^2 \ge 4 > h$ – תמיד ב-$L_h$. אם $|w| = 0$ – לעולם לא. אם $|w| = 1$: ב-$L_h$ אם"ם $h = 0$, כלומר $M$ לא מקבלת את $w$.""",
    r"""**$\overline{L_h} \in RE$:** $\overline{L_h}$ (בקלטים תקינים) = הזוגות עם $w = \varepsilon$, או עם $|w| = 1$ ו-$M$ מקבלת את $w$ – מכונה בודקת את האורך ומריצה את $M$ על $w$.""",
    r"""**$L_h \notin RE$:** $\overline{A_{TM}} \le_m L_h$ על ידי $f(\langle M,x\rangle) = \langle M_x, a\rangle$ ($a$ תו כלשהו), כאשר $M_x$ מתעלמת מהקלט ומריצה את $M$ על $x$: $M$ לא מקבלת את $x$ אם"ם $M_x$ לא מקבלת את $a$ אם"ם $h = 0 < 1$.""",
    "לכן התשובה ג."),
  note=TUT + "ג — agrees. h is printed as a two-case brace; rewritten as two bullet lines. Options say 'L' for L_h (as printed)."),

Q(9, "mapping_reductions", "קבע מהו היחס בין $A$ ל-$B$:", rel("A", "B"), "c",
  J(r"""$E_{TM} \le_m \overline{L} \Leftrightarrow \overline{E_{TM}} \le_m L$, ולכן $B = \{L \mid \overline{E_{TM}} \le_m L\}$, וזה בדיוק התנאי הראשון בהגדרת $A$. לכן $B \subseteq A$.""",
    r"""**ההכלה ממש:** $\emptyset \le_m \overline{E_{TM}}$ (ממפים הכול לקידוד של מכונה ששפתה ריקה), ולכן $\emptyset \in A$; אבל $\emptyset \notin B$ כי אין רדוקציה מ-$\overline{E_{TM}} \ne \emptyset$ ל-$\emptyset$. לכן $B \subset A$ (ג)."""),
  contextId="rel", note=TUT + "ג (ב crossed out) — agrees."),
Q(10, "mapping_reductions", "קבע מהו היחס בין $B$ ל-$C$:", rel("B", "C"), "a",
  r"""$B = \{L \mid \overline{E_{TM}} \le_m L\}$. מהנתון $\overline{E_{TM}} \le_m A_{TM}$ ו-$A_{TM} \le_m \overline{E_{TM}}$, ומטרנזיטיביות $\overline{E_{TM}} \le_m L \Leftrightarrow A_{TM} \le_m L$. לכן $B = C$.""",
  contextId="rel", note=TUT + "א — agrees."),
Q(11, "mapping_reductions", "מה מהמשפטים הבאים נכון", rel("A", "C"), "c",
  r"""משאלות 9–10: $C = B \subset A$, ולכן $C \subset A$ (אותה דוגמה: $\emptyset \in A \setminus C$).""",
  contextId="rel", note=TUT + "ג — agrees."),

Q(12, "mapping_reductions",
  r"האם $f(\langle M_1, M_2\rangle) = \langle T_{M_1,M_2}\rangle$ היא פונקציה ניתנת לחישוב?",
  YESNO, "a",
  r"""כן. $f$ רק כותבת את הקידוד של $T_{M_1,M_2}$ (תבנית קבועה שמשולבים בה הקידודים של $M_1, M_2$) ואינה מריצה אף מכונה, ולכן היא מחושבת על ידי מכונה שעוצרת תמיד.""",
  contextId="map",
  note=TUT + "א — agrees. Option ב 'לא' is printed bold (formatting artifact)."),
Q(13, "mapping_reductions",
  r"נתון ש-$M_1$ מכריעה שפה אבל $M_2$ לא מכריעה שפה, אזי האם עבור מכונות אלה מתקיים" "\n"
  r"$f(\langle M_1, M_2\rangle) \in CE_{TM} \Leftrightarrow \langle M_1, M_2\rangle \in ALL_{TM}$?",
  YESNO, "a",
  J(r"""בקריאה המתבקשת של המכונה (שלב 2 בודק אם $M_1$ קיבלה ושלב 4 אם $M_2$ קיבלה – המספרים הוחלפו בהדפסה): $M_1$ עוצרת תמיד, ולכן $T$ מגיעה להרצת $M_2$ בכל פעם ש-$M_1$ דוחה. $T$ מקבלת את $w$ אם"ם $M_1$ או $M_2$ מקבלת את $w$, כלומר $L(T) = L(M_1) \cup L(M_2)$.""",
    r"""לכן $f(\langle M_1,M_2\rangle) \in CE_{TM} \Leftrightarrow L(T) = \Sigma^* \Leftrightarrow \langle M_1,M_2\rangle \in ALL_{TM}$ – כן (א)."""),
  contextId="map",
  hold="Tutor circled ב (several times) — DISAGREES with the solved א. Also the T box has a print error (step 2 tests "
       "'M2 accepted' before M2 runs, step 4 tests M1): with the intended M1/M2 order the answer is א; read literally "
       "(accept only in step 4 when M1 accepted, after M2 halted) L(T)=L(M1)∩halt(M2) and the answer is ב.",
  note="Tutor's 2024 ink: ב circled; the tutor also wrote 1/2 over the M-indices in steps 2 and 4 (acknowledging the swap)."),
Q(14, "mapping_reductions",
  r"האם $f$ היא מקיימת את תנאי המיפוי ברדוקציה עבור $ALL_{TM} \le_m CE_{TM}$?",
  opts("כן",
       "לא כי הכיוון של הרדוקציה הוא הפוך.",
       r"לא כי קיימת מילה $w = \langle M_1, M_2\rangle$ שמקיימת $w \in ALL_{TM}$ אבל $f(w) \notin CE_{TM}$",
       r"לא כי קיימת מילה $w = \langle M_1, M_2\rangle$ שמקיימת $w \notin ALL_{TM}$ אבל $f(w) \in CE_{TM}$"),
  "c",
  J(r"""$T$ מריצה את $M_1$ ו-$M_2$ **בזו אחר זו**. אם $M_1$ לא עוצרת על $w$, $T$ לא עוצרת גם אם $M_2$ מקבלת את $w$.""",
    r"""**דוגמה (ג):** $M_1$ לא עוצרת על אף קלט, $M_2$ מקבלת כל קלט. אז $L(M_1) \cup L(M_2) = \Sigma^*$, כלומר $w \in ALL_{TM}$, אבל $L(T) = \emptyset$ ולכן $f(w) \notin CE_{TM}$.""",
    r"""**הפרכת ד:** בכל קריאה $L(T) \subseteq L(M_1) \cup L(M_2)$, ולכן $f(w) \in CE_{TM}$ (כלומר $L(T) = \Sigma^*$) גורר $w \in ALL_{TM}$. **הפרכת א:** הדוגמה לעיל. **הפרכת ב:** הבעיה איננה בכיוון אלא בתנאי ההתאמה."""),
  contextId="map",
  hold="Tutor circled ד (א, ב, ג crossed out) — DISAGREES with the solved ג. ד is impossible under any reading of the T box "
       "(L(T) ⊆ L(M1) ∪ L(M2)), but per protocol a disagreeing circle -> hold.",
  note="Stem prints 'אם ה f היא מקיימת' (sic); normalized to 'האם f היא מקיימת'."),

Q(15, "poly_reductions",
  r"אם $\langle \phi, k\rangle \in GSAT$ אז $f(\langle \phi, k\rangle) \in ESAT$.",
  opts("נכון רק אם מספר המשתנים ב-$\\phi$ הינו מספר זוגי",
       "נכון רק עבור $k$ זוגי.",
       "לא בהכרח נכון. כלומר לכל $k$ - יכול להיות נכון ויכול להיות לא נכון.",
       "נכון תמיד"),
  "d",
  J(r"""**$k$ אי-זוגי:** יש הצבה מספקת ל-$\phi$ עם לכל היותר $k$ משתני אמת. נציב אותה גם בעותק $\phi''$ (על המשתנים החדשים המתאימים): $\phi' = \phi \wedge \phi''$ מסופקת עם לכל היותר $2k = k'$ משתני אמת, ו-$k'$ זוגי. לכן $f(\langle\phi,k\rangle) \in ESAT$.""",
    r"""**$k$ זוגי:** המקרה לא מודפס בתיבה; בהשלמה הטבעית ($f$ = זהות, כמו במועד ב) הטענה מיידית.""",
    "לכן הטענה נכונה תמיד (ד); א, ב, ג שגויות."),
  contextId="poly",
  note="The f box prints only the odd-k case (22B-B's box also has 'אם k זוגי: φ'=φ, k'=k'); the answer here is the same under the natural identity completion. Q15–17 were crossed out in the tutor's ink with no answer."),
Q(16, "poly_reductions",
  r"אם $\langle \phi, k\rangle \notin GSAT$ אז $f(\langle \phi, k\rangle) \notin ESAT$.",
  opts("נכון רק אם מספר הקודקודים ב-$G$ זוגי",
       "נכון רק אם $k$ זוגי",
       "נכון תמיד",
       "המשפט לא מתקיים. כלומר יש מקרים שבהם נכון ויש מקרים בהם איננו נכון."),
  "c",
  J(r"""**$k$ אי-זוגי:** נניח ש-$\phi'$ מסופקת על ידי הצבה עם לכל היותר $2k$ משתני אמת. $\phi$ ו-$\phi''$ על קבוצות משתנים זרות, ולכן ההצבה מספקת כל אחת מהן בנפרד, ובאחת מהן יש לכל היותר $k$ משתני אמת. $\phi''$ זהה ל-$\phi$ עד כדי שינוי שמות, ולכן ל-$\phi$ יש הצבה מספקת עם לכל היותר $k$ משתני אמת – סתירה ל-$\langle\phi,k\rangle \notin GSAT$. (אם $\phi$ לא ספיקה, גם $\phi'$ לא ספיקה.)""",
    r"""**$k$ זוגי:** בהשלמה הטבעית ($f$ = זהות) מיידי. לכן נכון תמיד (ג)."""),
  contextId="poly",
  note="Option א mentions 'מספר הקודקודים ב G' — a copy-paste leftover from 22B-A; kept as printed. Even-k case not printed (see Q15 note)."),
Q(17, "poly_reductions",
  r"האם ההוכחה הנ\"ל מוכיחה כי $GSAT \le_p ESAT$?",
  opts("לא נכון כי הפונקציה $f$ שהוגדרה לא מקיימת את כל תנאי הרדוקציה הפולינומיאלית",
       "נכון כי הפונקציה $f$ שהוגדרה מקיימת את כל תנאי הרדוקציה הפולינומיאלית",
       "למרות שהפונקציה $f$ שהוגדרה לא מקיימת את תנאי הרדוקציה הפולינומיאלית – ההוכחה נכונה",
       "הפונקציה $f$ שהוגדרה מקיימת את תנאי הרדוקציה ובכל זאת המשפט לא נכון."),
  "b",
  J(r"""בהשלמה הטבעית ($f$ = זהות עבור $k$ זוגי): $f$ מחושבת בזמן פולינומיאלי (העתקת $\phi$ עם שמות משתנים חדשים והכפלת $k$), ותנאי ההתאמה מתקיימים (שאלות 15–16). לכן ההוכחה נכונה (ב)."""),
  contextId="poly",
  hold="Print omission changes the answer: the f box defines f only for odd k. With the natural completion "
       "(identity for even k, as printed in 22B-B) f is a valid poly-time reduction -> ב; read literally f is not "
       "defined on inputs with even k, so it is not a (total) reduction -> א.",
  note="Tutor's ink: section crossed out, no answer."),

Q(18, "npc",
  r"נניח שקיימות שפות $A$ ו-$B$ ו-$C$ כך שמתקיימים $B \le_P C$, $A \le_P B$ וכן $C \in NPC$, $A \in P$. "
  r"מה מהבאים הכרחי (בהנחה $P \ne NP$)",
  opts(("math", r"B \in P"), ("math", r"B \in NPC"), ("math", r"B \notin NP"), ("math", r"B \in NP")),
  "d",
  J(r"""**ד הכרחי:** $B \le_p C$ ו-$C \in NPC \subseteq NP$, ו-$NP$ סגורה לרדוקציות פולינומיאליות, לכן $B \in NP$. ומכאן ג שגויה.""",
    r"""**א לא הכרחי:** $A = \{0\}$, $B = C = SAT$: כל התנאים מתקיימים (שפה ב-$P$ מתרדדת לכל שפה לא טריוויאלית) ו-$B \notin P$ (כי $P \ne NP$).""",
    r"""**ב לא הכרחי:** $A = B = \{0\}$, $C = SAT$: $B \in P$ ולכן (כי $P \ne NP$) $B \notin NPC$."""),
  note="Tutor's ink: section crossed out, no answer. Printed order of the hypotheses: 'B ≤P C  A ≤P B וכן C∈NPC A∈P'."),
Q(19, "npc",
  r"תהיינה $A$ ו-$B$ שפות כך ש: $A \in NP$, $B \le_p \overline{A}$, $B \in NPC$." "\n"
  "האם נובע מנתונים אלה ש-$NP=coNP$?",
  opts("כן", "לא", r"רק אם $NP \cap coNP \ne P$.", r"רק אם $B \notin coNP$"),
  "a",
  J(r"""$B \le_p \overline{A} \Rightarrow \overline{B} \le_p A \in NP$, ולכן $\overline{B} \in NP$, כלומר $B \in coNP$.""",
    r"""לכל $L \in NP$: $L \le_p B$ (כי $B \in NPC$), ולכן $\overline{L} \le_p \overline{B} \in NP$, כלומר $L \in coNP$. קיבלנו $NP \subseteq coNP$, ומכאן גם $coNP \subseteq NP$ (אם $L \in coNP$ אז $\overline{L} \in NP \subseteq coNP$, כלומר $L \in NP$). לכן $NP = coNP$ נובע ללא תנאים נוספים (א); ג, ד מיותרות/שגויות, ו-ב שגויה."""),
  note="Tutor's ink: section crossed out, no answer. Stem and options identical to 22B-B Q19 (also solved, no key)."),
Q(20, "npc",
  "נגדיר את השפה $FPhi$:\n"
  r"$$FPhi = \{\langle \phi\rangle \mid (*)\}$$"
  r"(*): $\phi$ נוסחא בצורת $CNF$, $K$ = (מספר המשתנים ב-$\phi$ פחות 2), $\langle \phi\rangle \in KSAT$" "\n"
  r"איזו מהטענות הבאות נכונה? (בהנחה ש-$P \ne NP$)",
  opts(("math", r"FPhi \in NP \setminus NPC"), ("math", r"FPhi \in NPC"), ("math", r"FPhi \in P"), NONE),
  "b",
  J(r"""בקריאה \"$KSAT$ = נוסחאות שיש להן הצבה מספקת עם לכל היותר $K$ משתני אמת\" (כמו $GSAT$): $FPhi \in NP$ (עד = ההצבה), ו-$SAT \le_p FPhi$ על ידי $\phi \mapsto \phi \wedge (y_1 \vee \neg y_1) \wedge (y_2 \vee \neg y_2)$ עם שני משתנים חדשים $y_1, y_2$ (נציב בהם שקר): ל-$\phi$ על $n$ משתנים יש הצבה מספקת אם"ם לנוסחה החדשה (על $n+2$ משתנים) יש הצבה מספקת עם לכל היותר $n$ משתני אמת. לכן $FPhi \in NPC$."""),
  hold="KSAT is never defined in the exam. Read as 'satisfiable with ≤K true variables' (like GSAT) FPhi is NP-complete -> ב; "
       "read as K-CNF-SAT (every clause has K = n-2 literals) it is in P (each clause kills only 4 of 2^n assignments, so an "
       "unsatisfiable input must have ≥2^(n-2) clauses and brute force is polynomial in the input) -> ג, which is also what the "
       "parallel questions 22B-A Q20 / 22B-B Q20 (…∈P) suggest. Ambiguous -> hold.",
  note="Tutor's ink: section crossed out, no answer."),
]

# --- RESOLUTIONS (ASK_ADIR items resolved by independent math check; Adir authorized 2026-09-29) ---
def _resolve(num, **kw):
    q = next(q for q in questions if q["num"] == num)
    q.pop("hold", None)
    q.update(kw)
# Stage-2 blind verification (tools/raw/_verify_22B-C.json).
# Q14: both stages independently get ג; the tutor's circled ד is impossible because L(T) is always a subset of L(M1) ∪ L(M2) under either reading of the machine box -> released.
_resolve(14, correctId="c", confidence="high",
  note=r"""Released after stage 2: both solvers get ג; tutor circled ד, which is impossible since L(T) ⊆ L(M1) ∪ L(M2).""")

exam = {
  "examCode": "22B-C",
  "examLabel": "2022 סמסטר ב מועד ג",
  "year": 2022,
  "examDate": "21.8.2022",
  "sourceFile": "מבחנים/2022/סמסטר ב/סמסטר  ב מועד ג 21-8-22.pdf",
  "keyFile": "none official — answers solved (tools/SOLVE_GUIDE.md stage 1); tutor's 2024 ink in "
             "מבחנים/2022/סמסטר ב/2022-08-21-Exam-חישוביות-2022-moedC-גרסא-0 SOLUTION.pdf used as partial evidence",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 21))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
