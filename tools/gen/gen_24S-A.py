# -*- coding: utf-8 -*-
"""Generator for tools/raw/24S-A.json (KEYLESS sitting, stage 1 of SOLVE_GUIDE.md).
Transcribed from `מבחנים/2024/סמסטר קיץ/2024-09-15-Exam-חישוביות-2024-moedA-טופס-0.pdf`
(form 000, no marks). Options kept in printed order. Answers = my own rigorous solutions
(answerSource "solved", official False); form-0 first option recorded in `note`.
`מבחן מעורבב.pdf` (web-shuffler retype, errors, key derived from form-0) is ignored.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24S-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24S-A.json"
IDS = "abcde"

def opts(*vals):
    out = []
    for i, v in enumerate(vals):
        if isinstance(v, tuple):
            out.append({"id": IDS[i], "type": v[0], "value": v[1]})
        else:
            out.append({"id": IDS[i], "type": "text", "value": v})
    return out

def ex(*paras):
    return "\n".join(paras)

ALLF = "כל הטענות האחרות לא נכונות."
DEC4 = opts(
    "השפה $L$ ניתנת להכרעה.",
    "השפה $L$ ניתנת לקבלה אבל לא ניתנת להכרעה.",
    r"השפה $L$ לא ניתנת לקבלה אבל $\overline{L}$ ניתנת לקבלה.",
    r"השפה $L$ לא ניתנת לקבלה וגם $\overline{L}$ לא ניתנת לקבלה.",
)
F0 = "form-0 (מבחן מס' 000) first option: א — agrees with my solution."

def Q(num, topic, question, options, correct, explanation, **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "solved", "official": False,
         "confidence": "high", "explanation": explanation, "note": F0}
    if "note" in kw:
        q["note"] = F0 + " " + kw.pop("note")
    q.update(kw)
    return q

questions = [
Q(1, "mapping_reductions",
  r"תהיינה $A, B$ שתי שפות לא טריוויאליות." "\n"
  "איזו מהטענות הבאות היא טענה נכונה?",
  opts(r"אם מתקיים $A \le_m B$ וגם $B \not\le_m A$ אז יתכן: $A \in R$ וגם $B \in RE \setminus R$.",
       r"אם מתקיים $A \le_m B$ וגם $B \not\le_m A$ אז יתכן: $A \in R$ וגם $B \in R$.",
       r"אם מתקיים $A \le_m B$ וגם $B \not\le_m A$ אז יתכן: $A \in RE \setminus R$ וגם $B \in R$.",
       ALLF),
  "a", ex(
  r"""**הוכחת א:** $A = PALINDROMES$ (ב-$R$, לא טריוויאלית), $B = A_{TM} \in RE \setminus R$. כל שפה ב-$R$ ניתנת לרדוקציה לכל שפה לא טריוויאלית, לכן $A \le_m B$; ואילו $B \le_m A$ הייתה נותנת $A_{TM} \in R$ – לכן $B \not\le_m A$.""",
  r"""**הפרכת ב:** אם $B \in R$ ו-$A$ לא טריוויאלית אז בהכרח $B \le_m A$, בסתירה ל-$B \not\le_m A$.""",
  r"""**הפרכת ג:** $A \le_m B$ ו-$B \in R$ נותנים (משפט הרדוקציה) $A \in R$, בסתירה ל-$A \notin R$.""",
  r"""**הפרכת ד:** א נכונה.""")),

Q(2, "closure",
  r"תהי $L$ שפה כך שמתקיים $L \in R$." "\n"
  "נגדיר את השפה הבאה:\n"
  r"$$A(L) = \{w \mid (*)\}$$"
  r"(*): $w \notin L$ וגם $|w|$ זוגי" "\n"
  "איזו מהטענות הבאות היא טענה נכונה?",
  opts("השפה $A(L)$ ניתנת להכרעה.",
       "השפה $A(L)$ ניתנת לקבלה וגם יתכן שהשפה $A(L)$ לא-ניתנת להכרעה.",
       "יתכן שהשפה $A(L)$ לא-ניתנת לקבלה.",
       ALLF),
  "a", ex(
  r"""**הוכחת א:** $A(L) = \overline{L} \cap \{w \mid |w| \text{ is even}\}$. $\overline{L} \in R$ (סגירות למשלים) ושפת המילים באורך זוגי רגולרית; $R$ סגורה לחיתוך. בפועל: על קלט $w$ – אם $|w|$ אי-זוגי דחה, אחרת הרץ את המכריע של $L$ והחזר את התשובה ההפוכה.""",
  r"""**הפרכת ב, ג, ד:** $A(L)$ תמיד ניתנת להכרעה."""),
  note="Printed set: 'A(L) = { w | w ∉ L וגם |w| זוגי }' — condition moved to a (*) line."),

Q(3, "tm",
  "נתבונן בשתי הטענות הבאות:\n"
  r"טענה I: אם קיימת מכונת טיורינג דטרמיניסטית בעלת שני סרטים שמכריעה שפה $L$ אז קיימת מכונה טיורינג לא דטרמיניסטית המכריעה את $L$." "\n"
  r"טענה II: אם $M$ מכונת טיורינג **לא** דטרמיניסטית ומכונה $K$ מתקבלת מהמכונה $M$ על ידי הפיכת המצב המקבל של $M$ למצב דוחה, והפיכת המצב הדוחה של $M$ למצב מקבל אזי $L(M)$ ו-$L(K)$ הן שפות משלימות." "\n"
  "איזה מהסעיפים הבאים נכון?",
  opts("טענה I נכונה וגם טענה II לא נכונה.",
       "שתי הטענות I, II הן נכונות.",
       "שתי הטענות I, II הן לא נכונות.",
       "טענה I לא נכונה וגם טענה II נכונה."),
  "a", ex(
  r"""**טענה I נכונה:** מכונה דו-סרטית שקולה למכונה חד-סרטית דטרמיניסטית שמכריעה את $L$ (הסימולציה עוצרת כשהמקורית עוצרת), ומכונה דטרמיניסטית היא בפרט לא דטרמיניסטית (עם בחירה יחידה בכל צעד).""",
  r"""**טענה II לא נכונה:** נניח ש-$M$ על קלט $w$ מתפצלת בצעד הראשון לענף שמקבל ולענף שדוחה. אז $w \in L(M)$, וב-$K$ הענף הדוחה הופך למקבל ולכן גם $w \in L(K)$ – השפות אינן משלימות.""")),

Q(4, "tm",
  "השלימו:\n"
  r"אם דיאגרמת המצבים של מ" '"' r"ט $M$ ______ מסלול מהמצב ההתחלתי $q_0$ למצב $q_{reject}$ אזי השפה $L(M)$ היא בהכרח ______.",
  opts(ALLF, "מכילה, ריקה.", "מכילה, שפה לא טריוויאלית.", r"לא מכילה, $\Sigma^*$."),
  "a", ex(
  r"""**הפרכת ב, ג:** קיום מסלול ל-$q_{reject}$ לא קובע את השפה: מכונה שדוחה מיד כל קלט (ושפתה $\emptyset$) ומכונה שדוחה רק את המילים המתחילות ב-$a$ ומקבלת את השאר (שפתה לא טריוויאלית) – בשתיהן יש מסלול כזה, לכן אף אחת מהמסקנות "ריקה" / "לא טריוויאלית" אינה בהכרח.""",
  r"""**הפרכת ד:** אם אין מסלול ל-$q_{reject}$ המכונה אף פעם לא דוחה, אבל היא יכולה לא לעצור: מכונה שזזה ימינה לעד על כל קלט (ללא מסלול למצב הדוחה) מקיימת $L(M) = \emptyset \ne \Sigma^*$.""",
  r"""**לכן א נכונה.**"""),
  note="Printed blanks are long underscores; rendered as '______'."),

Q(5, "mapping_reductions",
  r"תהיינה $A, B, C$ שפות." "\n"
  "איזו מהטענות הבאות היא טענה נכונה?",
  opts("כל הטענות האחרות לא נכונות",
       r"אם $A \cup B \le_m C$ אז מתקיים: $A \le_m C$ וגם $B \le_m C$.",
       r"אם $C \le_m A \cup B$ אז מתקיים: $A \le_m C$ או $B \le_m C$.",
       r"אם $A \cup B \le_m C$ אז מתקיים: $C \le_m A \cup B$."),
  "a", ex(
  r"""**הפרכת ב:** $A = A_{TM}$, $B = \overline{A_{TM}}$, $C = \Sigma^*$: $A \cup B = \Sigma^* \le_m \Sigma^*$ (זהות), אבל לשפה $\Sigma^*$ ניתנת לרדוקציה רק $\Sigma^*$ עצמה, ולכן $A_{TM} \not\le_m \Sigma^*$.""",
  r"""**הפרכת ג:** $A = B = A_{TM}$, $C = \{0\}$: $C \in R$ ו-$A_{TM}$ לא טריוויאלית, לכן $C \le_m A \cup B = A_{TM}$; אבל $A_{TM} \le_m \{0\}$ הייתה נותנת $A_{TM} \in R$.""",
  r"""**הפרכת ד:** $A = B = \emptyset$, $C = A_{TM}$: $\emptyset \le_m A_{TM}$ (ממפים הכול למילה קבועה שאינה ב-$A_{TM}$), אבל $A_{TM} \le_m \emptyset$ בלתי אפשרי (רק $\emptyset$ ניתנת לרדוקציה ל-$\emptyset$).""",
  r"""**לכן א נכונה.**""")),

Q(6, "decidability",
  "איזו מהטענות הבאות היא טענה **לא** נכונה?",
  opts(r"אם $L$ ניתנת לקבלה אז $\overline{L}$ ניתנת לקבלה.",
       r"קיימת שפה $L$ כך שגם $L$ וגם $\overline{L}$ אינן ניתנות להכרעה.",
       r"קיימת שפה $L$ כך שגם $L$ וגם $\overline{L}$ אינן ניתנות לקבלה.",
       r"אם $L$ ניתנת להכרעה אז $\overline{L}$ ניתנת לקבלה."),
  "a", ex(
  r"""**א אינה נכונה (ולכן היא התשובה):** $A_{TM}$ ניתנת לקבלה אבל $\overline{A_{TM}}$ אינה ניתנת לקבלה.""",
  r"""**ב נכונה:** $L = A_{TM}$ – גם היא וגם משלימתה אינן ב-$R$.""",
  r"""**ג נכונה:** $L = EQ_{TM}$ – גם היא וגם משלימתה אינן ב-$RE$.""",
  r"""**ד נכונה:** $R$ סגורה למשלים ו-$R \subseteq RE$.""")),

Q(7, "np", "איזו מהטענות הבאות היא טענה נכונה?",
  opts("לא ידוע האם הטענות האחרות נכונות.",
       "המחלקה $NP$ סגורה תחת שרשור אבל לא סגורה תחת השלמה.",
       "המחלקה $NP$ סגורה תחת איחוד אבל לא סגורה תחת השלמה.",
       "המחלקה $NP$ סגורה תחת איחוד וגם סגורה תחת השלמה."),
  "a", ex(
  r"""$NP$ סגורה תחת שרשור ותחת איחוד (ידוע), אבל השאלה אם $NP$ סגורה תחת השלמה היא השאלה הפתוחה $NP = coNP$ (אם $P = NP$ היא סגורה; אם $NP \ne coNP$ היא לא). לכן כל אחת מהטענות ב, ג, ד – שכולן קובעות משהו לגבי ההשלמה – אינה ידועה, ו-א היא הנכונה.""")),

Q(8, "mapping_reductions",
  r"תהיינה $L_1, L_2$ שפות." "\n"
  r"נניח כי קיימת פונקציה ניתנת לחישוב $f: \Sigma^* \to \Sigma^*$ כך שלכל $x \in \Sigma^*$ מתקיים:" "\n"
  r"$$x \notin L_1 \Leftrightarrow f(x) \in L_2$$"
  r"נתבונן בטענה הבאה: אם מתקיים $L_2 \in RE$ אזי מתקיים $L_1 \in RE$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  opts("הטענה לא נכונה.", "הטענה נכונה."),
  "a", ex(
  r"""**הטענה לא נכונה:** התנאי אומר ש-$f$ היא רדוקציה $\overline{L_1} \le_m L_2$, ולכן מ-$L_2 \in RE$ נובע רק $\overline{L_1} \in RE$.""",
  r"""**דוגמה נגדית:** $L_1 = \overline{A_{TM}}$, $L_2 = A_{TM}$, $f$ הזהות: $x \notin \overline{A_{TM}} \Leftrightarrow x \in A_{TM}$. אכן $L_2 \in RE$ אבל $L_1 \notin RE$.""")),

Q(9, "decidability",
  r"תהי $A$ שפה לא טריוויאלית שניתנת להכרעה, כלומר $A \in R$." "\n"
  "נגדיר את השפות הבאות:\n"
  r"$$L_1 = \{\langle M\rangle \mid (*)\}$$"
  r"(*): $M$ היא מכונת טיורינג וגם $L(M) = \overline{A}$" "\n"
  r"$$L_2 = \{\langle M\rangle \mid (**)\}$$"
  r"(**): $M$ היא מכונת טיורינג שמכריעה את $\overline{A}$" "\n"
  "איזו מהטענות הבאות היא טענה נכונה?",
  opts(r"השפה $L_2$ מוכלת ממש בשפה $L_1$.",
       r"השפה $L_1$ מוכלת ממש בשפה $L_2$.",
       r"השפה $L_1$ שווה לשפה $L_2$.",
       ALLF),
  "a", ex(
  r"""**$L_2 \subseteq L_1$:** מכונה שמכריעה את $\overline{A}$ מקבלת בדיוק את $\overline{A}$, כלומר $L(M) = \overline{A}$.""",
  r"""**ההכלה ממש:** $A$ לא טריוויאלית, לכן קיימת $x \in A$. יהי $D$ מכריע של $\overline{A}$ (קיים כי $A \in R$), ונבנה $M$: על קלט $y$ הרץ את $D$; אם $D$ מקבלת – קבל, אחרת היכנס ללולאה אינסופית. אז $L(M) = \overline{A}$ ולכן $\langle M\rangle \in L_1$, אבל $M$ לא עוצרת על $x$ ולכן אינה מכריעה – $\langle M\rangle \notin L_2$.""",
  r"""לכן א נכונה, ו-ב, ג, ד שגויות.""")),

Q(10, "tm", "מהו הגודל המינימלי של קבוצת המצבים $Q$ בהגדרה של מכונת טיורינג?",
  opts("2", "1", "3", "אין הגבלת מינימום על מספר המצבים."),
  "a", ex(
  r"""בהגדרת מ"ט $\langle Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej}\rangle$ נדרש $q_{acc} \ne q_{rej}$, ולכן $|Q| \ge 2$ (מה שפוסל את ב ו-ד). אין דרישה ש-$q_0$ יהיה שונה משניהם (למשל $q_0 = q_{acc}$ – מכונה שמקבלת מיד כל קלט), ולכן די ב-2 מצבים ו-ג שגויה."""),
  note="Course convention (q_acc ≠ q_rej, q0 may coincide with one of them) confirmed in the student summaries in סיכומים/ (|Q| ≥ 2)."),

Q(11, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{a^{n+1} b^{n-1} c^{n+1} \mid n \ge 0\}$$"
  "איזו מהטענות הבאות היא טענה נכונה?",
  DEC4, "a", ex(
  r"""**הוכחת א:** מכריע: בודקים שהקלט מהצורה $a^* b^* c^*$, סופרים $\#a, \#b, \#c$ ובודקים ש-$\#a = \#c = \#b + 2$. המכונה תמיד עוצרת, לכן $L \in R$ (ובפרט $L, \overline{L} \in RE$, ולכן ב, ג, ד שגויות)."""),
  note="As printed, n = 0 gives b^{-1} (print glitch); every reading (skip n=0 or treat as ε) leaves a decidable language, so the answer is unaffected. The explanation's check uses n ≥ 1."),

Q(12, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid (*)\}$$"
  r"(*): $M$ היא מכונת טיורינג וגם קיימת מילה $w \in \Sigma^*$ כך שהחישוב של $M$ על $w$ עוצר במצב דוחה על ידי ביצוע של לא יותר מ-$2|Q|$ צעדי חישוב, כאשר $Q$ היא קבוצת המצבים של $M$" "\n"
  "איזו מהטענות הבאות היא טענה נכונה?",
  DEC4, "a", ex(
  r"""**הוכחת א:** נסמן $k = 2|Q|$. ב-$k$ צעדים הראש מגיע לכל היותר לתאים $0..k$, ולכן ריצת $M$ על $w$ ב-$k$ הצעדים הראשונים תלויה רק ב-$k+1$ התווים הראשונים של $w$: אם $w$ ארוכה יותר, הרישא $w'$ שלה באורך $k+1$ מתנהגת זהה ב-$k$ צעדים. לכן די לבדוק את כל המילים באורך $\le k+1$ – מספר סופי.""",
  r"""מכריע: על קלט $\langle M\rangle$ מחשבים $k$, ולכל מילה באורך $\le k+1$ מסמלצים את $M$ לכל היותר $k$ צעדים; אם באחת הריצות $M$ עצרה במצב דוחה – קבל, אחרת דחה. הסימולציות סופיות, ולכן $L \in R$."""),
  note="Printed condition spans 4 lines inside the brace; moved to a (*) line."),

Q(13, "tm",
  r"תזכורת: המכונה $K_{M,w}$ מוגדרת כך: $K_{M,w}(x): \{M(w); accept\}$." "\n"
  "לפניכם שתי טענות:\n"
  r"טענה I: אם $K_{M,w}$ היא מכונה מכריעה אזי $M$ היא מכונה מכריעה" "\n"
  r"טענה II: אם $M$ היא מכונה מכריעה אזי $K_{M,w}$ היא מכונה מכריעה" "\n"
  "איזה מהסעיפים הבאים נכון?",
  opts("טענה I לא נכונה וגם טענה II נכונה.",
       "טענה I נכונה וגם טענה II לא נכונה.",
       "שתי הטענות I, II הן נכונות.",
       "שתי הטענות I, II הן לא נכונות."),
  "a", ex(
  r"""**טענה I לא נכונה:** $K_{M,w}$ עוצרת על כל קלט אם"ם $M$ עוצרת על $w$. ניקח $M$ שעוצרת על $w$ אבל לא עוצרת על מילה אחרת $w'$: אז $K_{M,w}$ מכריעה ו-$M$ אינה מכריעה.""",
  r"""**טענה II נכונה:** אם $M$ מכריעה היא עוצרת בפרט על $w$, ולכן $K_{M,w}$ עוצרת (ומקבלת) על כל קלט $x$.""")),

Q(14, "tm",
  "נרצה להגדיר וריאנט של מכונת טיורינג, שבו בכל צעד חישוב יכול הראש הקורא לקפוץ ימינה או שמאלה מספר תאים כלשהו לאורך הסרט (כולל 0). "
  "כמו במכונה בסיסית, אם מספר התאים לקפיצה שמאלה חורג מהגבול השמאלי של הסרט, הראש הקורא יגיע לתא הראשון. כל שאר הרכיבים מוגדרים כמו במכונת טיורינג בסיסית.\n"
  "איזו צורה פורמלית מתאימה לפונקציית המעברים של וריאנט זה?",
  opts(("math", r"\delta: Q \times \Gamma \to Q \times \Gamma \times \mathbb{Z}"),
       ("math", r"\delta: Q \times \Gamma \to Q \times \Gamma \times \mathbb{N} \times \mathbb{N}"),
       ("math", r"\delta: Q \times \Gamma \to Q \times \Gamma \times \{L,R\}^n"),
       "אף אחת מהתשובות האחרות אינה נכונה."),
  "a", ex(
  r"""**הוכחת א:** כל מעבר צריך לקבוע מצב חדש, תו לכתיבה וקפיצה אחת: מספר שלם $z \in \mathbb{Z}$ – הסימן קובע את הכיוון (שלילי = שמאלה, חיובי = ימינה) והערך המוחלט את מספר התאים, ו-$z = 0$ הוא הישארות במקום.""",
  r"""**הפרכת ב:** זוג מספרים טבעיים אינו מקודד כיוון תנועה – $\mathbb{N}$ לבדו לא מבחין בין ימינה לשמאלה, ורכיב שני לא מוגדר לו תפקיד בווריאנט.""",
  r"""**הפרכת ג:** $\{L,R\}^n$ עם $n$ קבוע מאפשר רק קפיצות שנקבעות מ-$n$ תזוזות בודדות (לכל היותר $n$ תאים, ובזוגיות של $n$) – לא "מספר תאים כלשהו".""",
  r"""**הפרכת ד:** א נכונה."""),
  note="Option ב (two naturals) could in principle be given a (left,right) semantics, but the variant has one jump per step and the printed form assigns no meaning to the pair; ℤ is the intended exact fit."),
]

contexts = {
  "blk": {"kind": "text", "title": "הגדרות לשאלות 15–18",
          "text": "4 השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  "נגדיר את השפות הבאות:\n"
                  r"$$S1_{TM} = \{\langle M\rangle \mid |L(M)| = 1\}$$"
                  r"$$H_{TM} = \{\langle M, w\rangle \mid (*)\}$$"
                  "(*): $M$ עוצרת על $w$\n"
                  "כעת נגדיר שתי פונקציות:\n"
                  r"$$f(x) = x$$"
                  r"$$g(\langle M, w\rangle) = \langle M_g\rangle$$"
                  r"כאשר $M_g$ היא מ" '"' r"ט אשר בהינתן קלט $y$:" "\n"
                  r"• אם $y$ היא לא המילה 101, אז $M_g$ דוחה את $y$." "\n"
                  r"• אם $y$ היא המילה 101, אז $M_g$ מריצה את $M$ על $w$ ואז עוצרת במצב מקבל." "\n"
                  "קבעו לכל אחת מהטענות הבאות האם היא נכונה או לא:"},
}
NO_YES = opts("לא נכון", "נכון")
YES_NO = opts("נכון", "לא נכון")

S1_NOT_RE = (r"""**עובדת עזר – $S1_{TM} \notin RE$:** $\overline{H_{TM}} \le_m S1_{TM}$ על ידי $\langle M, w\rangle \mapsto \langle M'\rangle$, כאשר $M'$ על קלט $y$: אם $y = 101$ קבל; אחרת הרץ את $M$ על $w$ וקבל. אם $M$ לא עוצרת על $w$ אז $L(M') = \{101\}$; אם עוצרת – $L(M') = \Sigma^*$. מכיוון ש-$\overline{H_{TM}} \notin RE$, גם $S1_{TM} \notin RE$.""")

questions += [
Q(15, "mapping_reductions", r"$f$ היא רדוקציה $H_{TM} \le_m S1_{TM}$.", NO_YES, "a", ex(
  r"""**לא נכון:** $f$ היא הזהות, ולכן היא רדוקציה $H_{TM} \le_m S1_{TM}$ רק אם $H_{TM} = S1_{TM}$ – ואז הזהות הייתה גם רדוקציה $S1_{TM} \le_m H_{TM}$, ומ-$H_{TM} \in RE$ היה נובע $S1_{TM} \in RE$. סתירה לעובדת העזר.""",
  S1_NOT_RE), contextId="blk"),
Q(16, "mapping_reductions", r"$f$ היא רדוקציה $S1_{TM} \le_m H_{TM}$.", NO_YES, "a", ex(
  r"""**לא נכון:** לא קיימת שום רדוקציה $S1_{TM} \le_m H_{TM}$: $H_{TM} \in RE$ ולכן לפי משפט הרדוקציה היינו מקבלים $S1_{TM} \in RE$.""",
  S1_NOT_RE), contextId="blk"),
Q(17, "mapping_reductions", r"$g$ היא רדוקציה $H_{TM} \le_m S1_{TM}$.", YES_NO, "a", ex(
  r"""**נכון:** $g$ ניתנת לחישוב (רק בונים את הקידוד של $M_g$).""",
  r"""אם $\langle M, w\rangle \in H_{TM}$ אז על $101$ המכונה $M_g$ מסיימת את הרצת $M$ על $w$ ומקבלת, ושאר המילים נדחות: $L(M_g) = \{101\}$, ולכן $\langle M_g\rangle \in S1_{TM}$.""",
  r"""אם $\langle M, w\rangle \notin H_{TM}$ אז על $101$ המכונה $M_g$ לא עוצרת: $L(M_g) = \emptyset$, ולכן $\langle M_g\rangle \notin S1_{TM}$."""),
  contextId="blk"),
Q(18, "mapping_reductions", r"$g$ היא רדוקציה $S1_{TM} \le_m H_{TM}$.", NO_YES, "a", ex(
  r"""**לא נכון:** לא קיימת שום רדוקציה $S1_{TM} \le_m H_{TM}$, כי $H_{TM} \in RE$ והיינו מקבלים $S1_{TM} \in RE$ (בנוסף, $g$ מוגדרת על זוגות $\langle M, w\rangle$ ומחזירה קידוד של מכונה בודדת, לא זוג).""",
  S1_NOT_RE), contextId="blk"),
]

exam = {
  "examCode": "24S-A",
  "examLabel": "2024 סמסטר קיץ מועד א",
  "year": 2024,
  "examDate": "15.9.2024",
  "sourceFile": "מבחנים/2024/סמסטר קיץ/2024-09-15-Exam-חישוביות-2024-moedA-טופס-0.pdf",
  "keyFile": "none — answers solved (stage 1 of tools/SOLVE_GUIDE.md); form-0 first-option used only as partial evidence",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 19))

def _fix(x):
    """raw strings keep the backslash of \\" -> strip it."""
    if isinstance(x, str): return x.replace('\\"', '"')
    if isinstance(x, list): return [_fix(v) for v in x]
    if isinstance(x, dict): return {k: _fix(v) for k, v in x.items()}
    return x
exam = _fix(exam)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
