# -*- coding: utf-8 -*-
"""Generator for tools/raw/26B-A.json. Transcribed by hand from the rendered pages of
`מבחנים/2026/חישוביות 2026 מועד א מעורבל עם תשובות.pdf` (renders: tools/raw/26B-A-SRC).
Shuffled form; its own order is canonical. Key = yellow highlight, explanations = blue proof boxes.
Q2 has no highlight: answer taken from its proof box ("הוכחת א") and verified against the diagram.
Run: PYTHONUTF8=1 py tools/gen/gen_26B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "26B-A.json"
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

TWO_CLAIMS = opts(
    "שתי הטענות I, II הן נכונות.",
    "שתי הטענות I, II הן לא-נכונות.",
    "טענה I נכונה וגם טענה II לא-נכונה.",
    "טענה II נכונה וגם טענה I לא-נכונה.",
)
DEC4 = opts(
    "השפה $L$ ניתנת להכרעה.",
    "השפה $L$ ניתנת לקבלה אבל לא-ניתנת להכרעה.",
    r"השפה $L$ לא-ניתנת לקבלה אבל $\overline{L}$ ניתנת לקבלה.",
    r"השפה $L$ לא-ניתנת לקבלה וגם $\overline{L}$ לא-ניתנת לקבלה.",
)
NONE = "אף אחת מהתשובות האחרות אינה נכונה"

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "highlighted-pdf", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

contexts = {
  "abc": {"kind": "text", "title": "הגדרות לשאלות 17–19",
          "text": "שלוש השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  r"$$A = \{\langle M\rangle \mid L(M) \in RE\}$$"
                  r"$$B = \{\langle M\rangle \mid L(M) \in REG\}$$"
                  r"$$C = \{\langle M\rangle \mid \overline{A_{TM}} \le_m L(M)\}$$"},
}

def rel(x, y):
    return opts(("math", rf"{x} \subset {y}"), ("math", rf"{y} \subset {x}"), ("math", rf"{x} = {y}"), NONE)

questions = [
Q(1, "mapping_reductions",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. $ALL_{TM} \le_m EQ_{TM}$" "\n"
  r"II. $EQ_{TM} \le_m \overline{A_{TM}}$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "c",
  r"**טענה I נכונה:** נסתכל על $f(\langle M\rangle) = \langle M_{acc}, M\rangle$ כאשר $M_{acc}$ היא מ\"ט המקבלת כל מילה. "
  r"ניתן לראות שהפונקציה חשיבה ומקיימת $\langle M\rangle \in ALL_{TM} \Leftrightarrow \langle M_{acc}, M\rangle \in EQ_{TM}$." "\n"
  r"**טענה II אינה נכונה:** אם $EQ_{TM} \le_m \overline{A_{TM}}$ אזי $\overline{EQ_{TM}} \le_m A_{TM}$ וזו סתירה למשפט הרדוקציה "
  r"מכיוון ש-$A_{TM} \in RE$ אולם $\overline{EQ_{TM}} \notin RE$."),

Q(2, "tm",
  "נתונה מכונת טיורינג $M$ המתוארת על ידי דיאגרמת המצבים הבאה. זוהי מכונה דטרמיניסטית "
  "(בכל מקום שלא מוגדר מעבר, יש להניח שהמעבר הוא ל-$q_{rej}$ והוא לא צויר רק לשם פשטות הדיאגרמה). "
  "א\"ב הקלט של $M$ הוא הא\"ב הבינארי וא\"ב הסרט כולל בנוסף גם את תו הרווח.\n"
  "איזה מהביטויים הרגולריים הבאים מתאר את $L(M)$?",
  opts(("math", r"0^*11^*01(0+1)^*"), ("math", r"(0+\sqcup)^*11^*0\sqcup^*1(0+1)^*"),
       ("math", r"0^*11^*01"), NONE),
  "a",
  r"**הוכחת א:** בשביל שמילה תתקבל היא צריכה לעבור במסלול מ-$q_0$ עד $q_{acc}$, כלומר על ידי קריאת $1$ ואז $01$ "
  r"כאשר ייתכן קריאת תווים נוספים של $0$ בהתחלה ותווים נוספים של $1$ אחרי ה-$1$ הראשון. "
  r"כמו כן, כל מילה שמכילה את הרישא $0^*11^*01$ מתקבלת, ולכן נקבל $0^*11^*01(0+1)^*$." "\n"
  r"**הפרכת ב:** $\sqcup$ אינו מא\"ב הקלט, ולכן מילה המכילה את התו $\sqcup$ אינה יכולה להיות בשפת המכונה." "\n"
  r"**הפרכת ג:** המילה $1011$ שייכת לשפת המכונה אבל לא לשפת הביטוי הנתון.",
  image="images/exams/26B-A-Q2.png", answerSource="explanation-inferred",
  note="No option is highlighted for Q2 in the key file; answer א taken from the proof box ('הוכחת א') "
       "and checked by hand against the diagram (q0 loops on 0 and ⊔; 1->q1; q1 loops on 1; 0->q2; q2 loops on ⊔; 1->acc)."),

Q(3, "decidability",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M, w\rangle \mid (*)\}$$"
  r"(*): $M$ מקבלת את $w$ ב-$k$ צעדים כאשר $k$ מקיים $|w| \le k \le 2|w|$" "\n"
  "אזי מתקיים:",
  DEC4, "a",
  r"**הוכחת א (והפרכת כל השאר):** נבנה מ\"ט $S$ שמכריעה את $L$ באופן הבא:" "\n"
  r"בהינתן קלט $\langle M, w\rangle$:" "\n"
  r"• חשב את גודל המילה $|w|$" "\n"
  r"• הרץ את $M$ על $w$ עד $2|w|$ צעדים." "\n"
  r"• אם $M$ קבלה את $w$ במספר צעדים גדול מ-$|w|$ קבל, אחרת דחה" "\n"
  r"קל לראות שהמכונה תמיד עוצרת, וכי אם $\langle M, w\rangle \in L$ אזי $S$ מקבלת את $\langle M, w\rangle$ אחרת $S$ דוחה אותה.",
  note="Printed stem: 'L = { <M,w> | M מקבלת את w ב k צעדים כאשר k מקיים |w| ≤ k ≤ 2|w| }' — condition moved to a (*) line."),

Q(4, "closure",
  "תהי $L$ שפה.\nנתבונן בשתי הטענות הבאות:\n"
  r"I. אם $L \le_m A_{TM}$ וגם $L \le_m E_{TM}$ אזי $L \in R$" "\n"
  r"II. אם $L \in RE$ וגם $L \le_m \overline{L}$ אזי $L \in R$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  r"**טענה I נכונה:** $L \le_m A_{TM}$ וממשפט הרדוקציה נקבל $L \in RE$. ומכיוון ש-$L \le_m E_{TM}$ ו-$E_{TM} \in coRE$ אזי $L \in coRE$. "
  r"ממשפט שראינו בהרצאה אם $L, \overline{L} \in RE$ אזי $L \in R$." "\n"
  r"**טענה II נכונה:** מכך ש-$L \le_m \overline{L}$ אזי $\overline{L} \le_m L$. ונקבל כי $\overline{L} \in RE$. "
  r"ממשפט שראינו בהרצאה אם $L, \overline{L} \in RE$ אזי $L \in R$."),

Q(5, "classification",
  r"תהי $M$ מ\"ט, ויהיו $C_1, C_2$ קונפיגורציות שלה. נאמר ש-$C_2$ **ישיגה** מ-$C_1$ ב-$M$ אם ריצתה של $M$ מ-$C_1$ מגיעה ל-$C_2$." "\n"
  "נגדיר את השפה:\n"
  r"$$L = \{\langle M, C_1, C_2\rangle \mid (*)\}$$"
  r"(*): $C_2$ ישיגה מ-$C_1$ ב-$M$" "\n"
  "אזי מתקיים:",
  DEC4, "b",
  r"**$L \in RE$:** בעזרת מ\"ט אוניברסלית, ניתן לסמלץ את ריצת $M$ מ-$C_1$ ובכל צעד לבדוק אם הריצה הגיעה ל-$C_2$. "
  "במידה והיא מגיעה לשם לעצור ולקבל.\n"
  r"**$L \notin R$:** נוכיח ע\"י רדוקציה מ-$A_{TM} \le_m L$." "\n"
  r"בהינתן קלט $\langle M, w\rangle$ הפונקצייה תתן $\langle M', \varepsilon q_0 w, \varepsilon q_{acc} \sqcup\rangle$ כאשר $M'$ היא המ\"ט "
  r"המתקבלת מ-$M$ ע\"י הוספת מצבים, כך ש-$M'$ פועלת בצורה דומה ל-$M$, מלבד ההבדל שלפני הגעה למצב מקבל, $M'$ תנקה את תוכן הסרט, "
  "תזיז את הראש לקצה השמאלי של הסרט, ורק אז תקבל.\n"
  r"הרדוקציה ניתנת לחישוב כי בניית $M'$ כרוכה בהוספת תו המסמן את הקצה השמאלי של הסרט, ומצבים אשר לפני המצב המקבל המקורי "
  "מוחקים את תוכן הסרט, ומזיזים את הראש הקורא לסימן המיוחד (הכי שמאלי) ומוחקים גם אותו. ניתן לממש זאת עם מ\"ט.\n"
  r"כעת, אם $\langle M, w\rangle \in A_{TM}$ אזי $M$ מקבלת את $w$, כלומר ריצתה מהקונפיגורציה ההתחלתית $\varepsilon, q_0, w$ מגיעה לקונפיגורציה מקבלת. "
  r"לכן ריצת $M'$ מהקונפיגורציה $\varepsilon, q_0, w$ מגיעה ג\"כ ל-$q_{accept}$ כאשר הסרט ריק והראש בקצה השמאלי, "
  r"כלומר הקונפיגורציה המקבלת היא $\varepsilon, q_{acc}, \sqcup$ ולכן $\langle M', \varepsilon q_0 w, \varepsilon q_{acc} \sqcup\rangle \in L$." "\n"
  r"מהצד השני, אם $\langle M, w\rangle \notin A_{TM}$ אזי $M$ לא מקבלת את $w$ ולכן $M'$ לא מקבלת את $w$, "
  r"ובפרט לא מגיעה מהקונפיגורציה ההתחלתית $\varepsilon, q_0, w$ לקונפיגורציה מקבלת, ובפרט לא לקונפיגורציה המקבלת $\varepsilon, q_{acc}, \sqcup$. "
  r"ולכן $\langle M', \varepsilon q_0 w, \varepsilon q_{acc} \sqcup\rangle \notin L$.",
  note="Printed stem: 'L = {<M,C1,C2> | C2 ישיגה מ C1 ב M}' — condition moved to a (*) line."),

Q(6, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid (*)\}$$"
  "(*): $M$ היא מ\"ט שמקבלת את $00$ ואת $11$\n"
  "אזי מתקיים:",
  DEC4, "b",
  r"**$L \in RE$:** נבנה מ\"ט המקבלת את $L$:" "\n"
  r"על קלט $\langle M\rangle$:" "\n"
  r"• הרץ את $M$ על שתי המילים $00$ ו-$11$ (למשל, בשני סרטים)" "\n"
  "• אם שתי ההרצות הסתיימו בקבלה קבל, ואם אחת ההרצות הסתיימה בדחייה דחה\n"
  r"המכונה שתיארנו מקבלת את $\langle M\rangle$ $\Leftrightarrow$ $M$ מקבלת את שתי המילים $00$ ו-$11$. ולכן $L$ ניתנת לקבלה." "\n"
  r"**$L \notin R$:** נוכיח ע\"י רדוקציה מ-$H_{TM} \le_m L$." "\n"
  r"$f(\langle M, w\rangle) = \langle K_{m,w}\rangle$ כך ש-$K_{m,w}$ המכונה שמוגדרת כך:" "\n"
  "בהינתן קלט $x$:\n"
  r"• הרץ את $M$ על $w$" "\n"
  "• קבל\n"
  r"ניתן לראות שהפונקציה חשיבה. כמו כן, אם $\langle M, w\rangle \in H_{TM}$ אזי $L(K_{m,w}) = \Sigma^*$ ולכן $\langle K_{m,w}\rangle \in L$." "\n"
  r"מהצד השני, אם $\langle M, w\rangle \notin H_{TM}$ אזי $L(K_{m,w}) = \emptyset$ ולכן $\langle K_{m,w}\rangle \notin L$.",
  note="Printed stem: 'L = {<M> | M היא מ\"ט שמקבלת את 00 ואת 11}' — condition moved to a (*) line."),

Q(7, "mapping_reductions",
  r"יהיו $A, B$ שפות מעל הא\"ב הבינארי $\Sigma = \{0,1\}$. ותהי $f: \Sigma^* \to \Sigma^*$ ניתנת לחישוב." "\n"
  r"נניח כי לכל $x \in \Sigma^*$ מתקיים כי $x \in A$ אמ\"מ $f(x) \notin B$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts("קיימת רדוקציית מיפוי מ-$A$ ל-$B$",
       r"אם $B \in RE$ אזי $A \in RE$",
       r"אם $B \in RE$ אזי $A \in coRE$",
       r"אם $A \in R$ אזי $B \in R$"),
  "c",
  r"הפונקצייה הנתונה מהווה רדוקציה $A \le_m \overline{B}$. לכן:" "\n"
  r"**הוכחת ג:** אם $B \in RE$ אזי $\overline{B} \in coRE$ ולכן ע\"פ משפט הרדוקציה נקבל כי $A \in coRE$." "\n"
  r"**הפרכת א:** $A = H_{TM}, B = E_{TM}$" "\n"
  r"**הפרכת ב:** $A = \overline{H_{TM}}, B = \overline{E_{TM}}$" "\n"
  r"**הפרכת ד:** לכל שפה $A \in R$ וכל שפה $B \in RE - R$ קיימת רדוקציה $A \le_m \overline{B}$ (לפי משפט שלמדנו בקורס)."),

Q(8, "poly_reductions",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $A \le_m \overline{B}$ וגם $\overline{B} \le_p C$ אזי מתקיים $A \le_m C$." "\n"
  r"II. אם $A \le_p \overline{B}$ וגם $A \not\le_p C$ אזי מתקיים $\overline{B} \not\le_p C$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  r"**טענה I נכונה:** אם $\overline{B} \le_p C$ אזי בפרט $\overline{B} \le_m C$. ומטרנזיטיביות של רדוקציית המיפוי "
  r"אם $A \le_m \overline{B}$ וגם $\overline{B} \le_m C$ נקבל $A \le_m C$." "\n"
  r"**טענה II נכונה:** נניח בשלילה ש-$\overline{B} \le_p C$. מכיוון ש-$A \le_p \overline{B}$ ומטרנזיטיביות רדוקציה פולינומיאלית "
  r"נקבל כי $A \le_p C$ בסתירה לכך ש-$A \not\le_p C$.",
  note="Proof box literally ends 'A ≤p C̄ בסתירה' — typo (overline on C); written as A ≤p C."),

Q(9, "closure",
  r"יהיו $L_1, L_2$ שתי שפות המקיימות $L_1 \in RE$ וגם $L_2 \in coRE$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(("math", r"L_1 \setminus L_2 \in R"), ("math", r"L_1 \setminus L_2 \in RE"),
       ("math", r"L_1 \setminus L_2 \in coRE"), ("math", r"L_1 \setminus L_2 \in \overline{RE \cup coRE}")),
  "b",
  r"**הוכחת ב והפרכת ד:** נתון $L_2 \in coRE$, לכן $\overline{L_2} \in RE$, ולכן $L_1 \setminus L_2 = L_1 \cap \overline{L_2} \in RE$ כי $RE$ סגורה לחיתוך." "\n"
  r"**הפרכת א:** אם $L_1 \in RE \setminus R$ וגם $L_2 = \overline{L_1} \in coRE$, אז $L_1 \setminus L_2 = L_1$ לא שייך ל-$R$." "\n"
  r"**הפרכת ג:** ולכן גם ג לא נכון, כי אם $L_1 \setminus L_2 \in coRE$ וגם $L_1 \setminus L_2 \in RE$, אז $L_1 \setminus L_2 \in R$ (ואת זה הפרכנו לעיל)."),

Q(10, "npc",
  "תהי $L$ שפה לא-טריוויאלית.\nאיזו מהטענות הבאות נכונה?",
  opts(r"אם $\overline{L} \in P$ וגם $P = NP$ אזי $L \in NPC$",
       r"אם $P \ne NP$ וגם $L \in P$ אזי $L \in NPC$",
       r"אם $L \in NPC$ וגם $\overline{L} \in P$ אזי $P \ne NP$",
       NONE),
  "a",
  r"**הוכחת א:** אם $\overline{L} \in P$ אז גם $L \in P$ ($P$ סגורה למשלים), ולכן אם $NP = P$, אז $NPC = P = NP$ ולכן $L \in NPC$." "\n"
  r"**הפרכת ב:** אם $P \ne NP$, אז $P$ ו-$NPC$ הן מחלקות זרות." "\n"
  r"**הפרכת ג:** אם $\overline{L} \in P$ אז גם $L \in P$, כך שאם גם $L \in NPC$, אז $NP = NPC = P$."),

Q(11, "closure",
  r"תהי $L \subseteq \Sigma^*$. נגדיר לכל $k \in \mathbb{N}$, את השפה $L_k = \{w \in L \mid |w| \le k\}$." "\n"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם לכל $k \in \mathbb{N}$, השפה $L_k \in R$ אזי $L \in R$" "\n"
  r"II. אם לכל $k \in \mathbb{N}$, השפה $L_k \in coRE$ אזי $L \in coRE$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "b",
  r"טענות I ו-II לא נכונות כי $L_k \in R$ ולכן $L_k \in coRE$ לכל שפה $L$ בכלל כי $L_k$ הן שפות סופיות." "\n"
  r"ולכן הרישא בשתי הטענות נכון למרות ש-$L$ יכולה להיות לא ב-$R$ ולא ב-$coRE$. כלומר הסיפא לא נובעת מהרישא באף אחת משתי הטענות."),

Q(12, "closure",
  r"תהיינה $A, B$ שפות כך שמתקיים: $A \in RE$ וגם $B \in coRE$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(("math", r"A \cap B \in R"), ("math", r"A \cup B \in R"),
       r"$EQ_{TM} \le_m A$ וגם $EQ_{TM} \le_m B$", NONE),
  "d",
  r"**הפרכת א:** עבור $A = \Sigma^*, B = E_{TM}$ נקבל $A \cap B = E_{TM} \notin R$" "\n"
  r"**הפרכת ב:** עבור $A = \emptyset, B = E_{TM}$ נקבל $A \cup B = E_{TM} \notin R$" "\n"
  r"**הפרכת ג:** מהנתון $EQ_{TM} \le_m A$ נובע ש-$EQ_{TM}$ שייכת ל-$RE$, וזה לא נכון."),

Q(13, "mapping_reductions",
  "איזו מהטענות הבאות נכונה?",
  opts("קיימת שפה סופית שאינה ניתנת להכרעה",
       r"אם $A \le_m B$ אזי $\overline{A} \le_m \overline{B}$",
       r"$P \subseteq NP$ אם ורק אם $P = NP$",
       NONE),
  "b",
  "**הפרכת א:** כל שפה סופית ניתנת להכרעה (שפה סופית היא רגולרית, קיים עבורה אוטומט, אז קיימת גם מכונת טיורינג מכריעה עבורה).\n"
  "**הוכחת ב:** משפט שלמדנו (ומופיע בדף הנוסחאות)\n"
  r"**הפרכת ג:** $P \subseteq NP$ בכל מקרה, אם קיימת מכונת טיורינג דטרמיניסטית המכריעה בזמן פולינומי, "
  "אז קיימת גם מכונה אי-דטרמיניסטית המכריעה בזמן פולינומי."),

Q(14, "poly_reductions",
  "נתונה הטענה הבאה:\n"
  r"לכל $A, B \in NP$ שאינן טריוויאליות מתקיים כי $A \le_p B$ וגם $B \le_p A$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  opts(r"הטענה נכונה אם ורק אם $P = NP$",
       r"הטענה נכונה אם ורק אם $P \ne NP$",
       r"הטענה נכונה (ללא קשר ליחס בין המחלקות $P, NP$)",
       r"הטענה אינה נכונה (ללא קשר ליחס בין המחלקות $P, NP$)"),
  "a",
  r"**הוכחת א (והפרכת שכל השאר):** אם $A \in P$ ו-$B \in NPC$, אז $A \le_p B$ בכל מקרה. אך $B \le_p A$ אם ורק אם $P = NP$."),

Q(15, "classification",
  r"נתונה השפה $L = \{\langle M_1, M_2\rangle \mid L(M_1) \subseteq L(M_2) \text{ or } L(M_2) \subseteq L(M_1)\}$." "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "d",
  "**הוכחת ד (והפרכת כל השאר):**\n"
  r"**$L \notin RE$:** נראה ע\"י רדוקציה מ-$\overline{H_{TM}}$." "\n"
  r"בהינתן קלט $\langle M, w\rangle$ הרדוקציה תחזיר $\langle M_1, M_2\rangle$ כאשר $M_1$ ו-$M_2$ הן מ\"ט המוגדרות באופן הבא:" "\n"
  r"המ\"ט $M_1$ בהינתן קלט $x$ בודקת האם $x = \varepsilon$ אם כן היא **דוחה**. אחרת היא מריצה את $M$ על $w$ ואחר כך מקבלת את $x$." "\n"
  r"המ\"ט $M_2$ בהינתן קלט $x$ בודקת האם $x \ne \varepsilon$. אם כן היא **דוחה**. אחרת היא מריצה את $M$ על $w$, ואז מקבלת את $x$." "\n"
  "ניתן לראות שהפונקצייה ניתנת לחישוב (לא מריצים את המכונות אלא רק מקודדים אותן).\n"
  r"כמו כן, אם $\langle M, w\rangle \in \overline{H_{TM}}$ אזי $L(M_1) = L(M_2) = \emptyset$ ולכן $\langle M_1, M_2\rangle \in L$." "\n"
  r"לעומת זאת אם $\langle M, w\rangle \notin \overline{H_{TM}}$ אזי $L(M_1) = \Sigma^* \setminus \{\varepsilon\}$ ומאידך $L(M_2) = \{\varepsilon\}$. "
  r"ולכן $\langle M_1, M_2\rangle \notin L$." "\n"
  r"**$L \notin coRE$:** נראה רדוקציה מ-$H_{TM}$." "\n"
  r"בהינתן קלט $\langle M, w\rangle$ הרדוקציה תחזיר $\langle M_1, M_2\rangle$ כאשר $M_1$ ו-$M_2$ הן מ\"ט המוגדרות באופן הבא:" "\n"
  r"המ\"ט $M_1$ בהינתן קלט $x$ בודקת האם $x = \varepsilon$ אם כן היא **מקבלת**. אחרת היא מריצה את $M$ על $w$ ואחר כך מקבלת את $x$." "\n"
  r"המ\"ט $M_2$ בהינתן קלט $x$ בודקת האם $x \ne \varepsilon$. אם כן היא **מקבלת**. אחרת היא מריצה את $M$ על $w$, ואז מקבלת את $x$." "\n"
  "ניתן לראות שהפונקצייה ניתנת לחישוב (לא מריצים את המכונות אלא רק מקודדים אותן).\n"
  r"כמו כן, אם $\langle M, w\rangle \in H_{TM}$ אזי $L(M_1) = L(M_2) = \Sigma^*$ ולכן $\langle M_1, M_2\rangle \in L$." "\n"
  r"לעומת זאת אם $\langle M, w\rangle \notin H_{TM}$ אזי $L(M_1) = \{\varepsilon\}$ ומאידך $L(M_2) = \Sigma^* \setminus \{\varepsilon\}$. "
  r"ולכן $\langle M_1, M_2\rangle \notin L$.",
  note="Proof box writes '<M1,w> ∈ H̄tm' / '<M1,M2> ∉ H̄tm' (L∉RE part) and '<M1,w> ∈ H_TM' / '<M1,M2> ∉ H_TM' (L∉coRE part) — typos for <M,w>; corrected."),

Q(16, "tm",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם קיימת מכונת טיורינג לא דטרמיניסטית שמכריעה שפה $L$ אז בהכרח קיימת מכונת טיורינג דטרמיניסטית בעלת סרט דו כיווני המכריעה את $L$" "\n"
  r"II. אם $M$ מכונת טיורינג לא דטרמיניסטית ו-$N$ מכונה המתקבלת מ-$M$ על ידי החלפת המצב המקבל והדוחה אזי מתקיים כי $L(M) \ne L(N)$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "c",
  "**טענה I נכונה:** כי לכל מכונה לא דטרמיניסטית קיימת מכונה שקולה דטרמיניסטית בסיסית, ולכל מכונה דטרמיניסטית בסיסית "
  "קיימת מכונה שקולה בעלת סרט דו כיווני.\n"
  r"**טענה II לא נכונה:** דוגמא נגדית: כאשר המכונה הלא דטרמיניסטית לא עוצרת אף פעם ב-$ACCEPT$ או ב-$REJECT$. "
  "השפה של המכונה המקורית וגם של המוחלפת נשארת אותו דבר: ריקה."),

Q(17, "classification", "מהו היחס בין $A$ ל-$B$?", rel("A", "B"), "b",
  "**הוכחת ב והפרכת כל השאר:**\n"
  r"תחילה נוכיח $B \subseteq A$." "\n"
  r"לפי ההגדרה כל מ\"ט $M$ מקבלת את השפה שלה, ולכן לכל מ\"ט $M$ מתקיים $L(M) \in RE$. לכן השפה $A$ היא שפה של כל הקידודים של מ\"ט." "\n"
  r"לכן לפי ההגדרה של השפות $A$ ו-$B$ מתקיים $B \subseteq A$." "\n"
  r"כעת נוכיח $B \ne A$. קיימת מ\"ט $T$ שמקבלת את השפה $a^nb^n$. השפה $a^nb^n$ ניתנת לקבלה, אך אינה רגולרית. כלומר:"
  r"$$a^nb^n \in RE \setminus REG$$"
  r"לכן לפי ההגדרה של השפות $A$ ו-$B$ מתקיים"
  r"$$\langle T\rangle \in A \setminus B$$"
  r"מכאן $A \ne B$.",
  contextId="abc"),

Q(18, "classification", "מהו היחס בין $A$ ל-$C$?", rel("A", "C"), "b",
  "**הוכחת ב והפרכת כל השאר:**\n"
  r"לפי ההגדרה כל מ\"ט $M$ מקבלת את השפה שלה, ולכן לכל מ\"ט $M$ מתקיים $L(M) \in RE$. "
  r"לכן השפה $A$ היא שפה של כל הקידודים של מ\"ט. מתקיים: $\langle UTM\rangle \in A$ לכן $A \ne \emptyset$." "\n"
  r"כעת נוכיח: $C = \emptyset$. נניח בשלילה שקיים קידוד של מ\"ט $T$ כך ש-$\langle T\rangle \in C$. אזי לפי ההגדרה של השפה $C$"
  r"$$\overline{A_{TM}} \le_m L(T) \in RE$$"
  r"לפי משפט הרדוקציה, $\overline{A_{TM}} \in RE$ – סתירה." "\n"
  "קבלנו:"
  r"$$\emptyset = C \subset A \ne \emptyset$$",
  contextId="abc"),

Q(19, "classification", "מהו היחס בין $B$ ל-$C$?", rel("B", "C"), "b",
  "**הוכחת ב והפרכת כל השאר:**\n"
  r"נוכיח: $C = \emptyset$. נניח בשלילה שקיים קידוד של מ\"ט $T$ כך ש-$\langle T\rangle \in C$. אזי לפי ההגדרה של השפה $C$"
  r"$$\overline{A_{TM}} \le_m L(T) \in RE$$"
  r"לפי משפט הרדוקציה, $\overline{A_{TM}} \in RE$ – סתירה." "\n"
  r"תהי $T$ = \"על קלט $x$ קבל\". מתקיים $L(T) = \Sigma^* \in REG$ ולכן $\langle T\rangle \in B \ne \emptyset$. קבלנו:"
  r"$$\emptyset = C \subset B \ne \emptyset$$",
  contextId="abc"),

Q(20, "mapping_reductions",
  r"תהיינה $L_1, L_2$ שפות מעל הא\"ב $\Sigma$. ונניח כי קיימות פונקציות ניתנות לחישוב $f, g: \Sigma^* \to \Sigma^*$ כך שלכל $x \in \Sigma^*$ שמתקיים כי:"
  r"$$x \in L_1 \Leftrightarrow (f(x) \in L_2 \wedge g(x) \notin L_2)$$"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $L_2 \in R$ אזי $L_1 \in R$" "\n"
  r"II. אם $L_2 \in RE$ אזי $L_1 \in RE$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "c",
  r"**טענה I נכונה:** תהי $L_2 \in R$. נגדיר מ\"ט $T$ = \"על קלט $x$" "\n"
  r"אם $f(x) \in L_2 \wedge g(x) \notin L_2$ קבל." "\n"
  "אחרת דחה.\"\n"
  r"מ\"ט $T$ קיימת מכיוון שהפונקציות $f$ ו-$g$ ניתנות לחישוב והמחלקה של השפות הרגולריות $R$ סגורה למשלים, לכן $\overline{L_2} \in R$. "
  r"בנוסף, $T$ עוצרת על כל קלט." "\n"
  r"נוכיח שמ\"ט $T$ מכריעה את השפה $L_1$." "\n"
  r"יהי $x \in L_1$. אזי לפי ההגדרה של הפונקציות $f$ ו-$g$ מתקיים $f(x) \in L_2 \wedge g(x) \notin L_2$ ולפי ההגדרה של מ\"ט $T$ היא מקבלת את $x$." "\n"
  r"יהי $x \notin L_1$. אזי לפי ההגדרה של הפונקציות $f$ ו-$g$ מתקיים $(f(x) \in L_2 \wedge g(x) \notin L_2) \equiv F$ ולפי ההגדרה של מ\"ט $T$ היא דוחה את $x$." "\n"
  r"קבלנו: $T$ מכריעה את השפה $L_1$, לכן $L_1 \in R$ כנדרש." "\n"
  "**טענה II לא נכונה:** נפריך על ידי דוגמא נגדית:\n"
  r"נבחר $L_1 = \overline{H_{TM}}$ ו-$L_2 = H_{TM}$. ונגדיר פונקציות $f$ ו-$g$ באופן הבא:"
  r"$$f(x) = \langle T: \{accept\}\rangle$$"
  r"(כלומר, $f$ מחזירה את הקידוד של המכונה $T$ שהיא מכונה המקבלת כל קלט)"
  r"$$g(x) = x$$"
  "אזי מתקיים:"
  r"$$x \in L_1 \Leftrightarrow x \in \overline{H_{TM}} \Leftrightarrow (\langle T(x): \{accept\}\rangle \in H_{TM} \wedge x \notin H_{TM}) \Leftrightarrow (f(x) \in L_2 \wedge g(x) \notin L_2)$$"
  r"אך המסקנה לא נובעת: $L_2 = H_{TM} \in RE$ אבל $L_1 = \overline{H_{TM}} \in coRE$.",
  note="Proof box says 'המחלקה של השפות הרגולריות R סגורה למשלים' (R is the decidable class) — transcribed as printed. "
       "The 4-line chain of ⟺ in the box is joined into one display line."),

Q(21, "classification",
  r"בהינתן מכונת טיורינג $M$ נאמר כי הסימן $\alpha$ מא\"ב הסרט **מיותר** אם $M$ אף פעם אינה כותבת את $\alpha$ במהלך ריצתה על אף קלט." "\n"
  "נגדיר את השפה:\n"
  r"$$L = \{\langle M, \alpha\rangle \mid (*)\}$$"
  r"(*): $M$ מ\"ט וגם $\alpha$ הוא סימן מיותר מא\"ב הסרט של $M$" "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "c",
  "**הוכחת ג והפרכת כל השאר:**\n"
  r"**נוכיח: $L \notin RE$.** על ידי רדוקציה $\overline{H_{TM}} \le_m L$. ומכיוון שמתקיים: $\overline{H_{TM}} \notin RE$, נוכל להסיק לפי משפט הרדוקציה $L \notin RE$." "\n"
  r"נגדיר רדוקציה $f$ מ-$\overline{H_{TM}}$ ל-$L$ באופן הבא:"
  r"$$f(\langle M, w\rangle) = \langle T_{M,w}, \alpha\rangle$$"
  r"כאשר $\alpha \notin \Gamma_M$ ו-$T_{M,w}$ מ\"ט שמוגדרת באופן הבא: \"על קלט $x$" "\n"
  r"הרץ את $M$ על $w$" "\n"
  r"כתוב תו $\alpha$ על הסרט\"" "\n"
  r"פונקציה $f$ ניתנת לחישוב (היא לא מריצה את $M$ על $w$, רק יוצרת קידוד של $T_{M,w}$)." "\n"
  r"נוכיח ש-$f$ משמרת שייכות:" "\n"
  r"אם $\langle M, w\rangle \in \overline{H_{TM}}$, אזי $M$ לא עוצרת על $w$. לכן $T_{M,w}$ לא כותבת את $\alpha$ במהלך הריצה על אף קלט, ולכן $\langle T_{M,w}, \alpha\rangle \in L$" "\n"
  r"אם $\langle M, w\rangle \notin \overline{H_{TM}}$, אזי $M$ עוצרת על $w$. לכן $T_{M,w}$ כותבת את $\alpha$ במהלך הריצה על כל קלט, ולכן $\langle T_{M,w}, \alpha\rangle \notin L$" "\n"
  r"**נוכיח: $\overline{L} \in RE$.** נגדיר מ\"ט א\"ד $N$ שמקבלת את $\overline{L}$ באופן הבא: \"על קלט $\langle M, \alpha\rangle$:" "\n"
  r"ננחש מילה $w$." "\n"
  r"נריץ $M$ על $w$. בכל צעד של $M$:" "\n"
  r"אם בצעד זה $M$ כתבה על סרט תו $\alpha$, קבל." "\n"
  "אחרת תמשיך את הסימולציה לצעד הבא.\"\n"
  r"אם $\langle M, \alpha\rangle \in \overline{L}$, אזי קיים קלט $w$ כך שבריצה של $M$ על $w$ היא כותבת את $\alpha$ על הסרט, ולכן ל-$N$ יש ריצה שמקבלת את $\langle M, \alpha\rangle$, ולכן $\langle M, \alpha\rangle \in L(N)$." "\n"
  r"אם $\langle M, \alpha\rangle \notin \overline{L}$, אזי על אף קלט $w$, $M$ לא כותבת את $\alpha$ על סרט, ולכן ל-$N$ אין ריצה שמקבלת את $\langle M, \alpha\rangle$, ולכן $\langle M, \alpha\rangle \notin L(N)$." "\n"
  r"קבלנו שמ\"ט א\"ד $N$ מקבלת את $\overline{L}$. לכן קיימת גם מ\"ט בסיסית שמקבלת את $\overline{L}$, ולכן $\overline{L} \in RE$.",
  note="Printed stem: 'L = {<M,α> | M מ\"ט וגם α הוא סימן מיותר מא\"ב הסרט של M}' — condition moved to a (*) line."),

Q(22, "classification",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. $SAT \le_m A_{TM}$" "\n"
  r"II. $SAT \in NP$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  "**הוכחת טענה I:**\n"
  r"השפה $SAT \in NP \subseteq R$" "\n"
  r"השפה $A_{TM}$ אינה טריוויאלית. לפי משפט שלמדנו בקורס, לכל שפה ב-$R$ יש רדוקציה לכל שפה לא טריוויאלית." "\n"
  "**הוכחת טענה II:**\n"
  r"ראינו בהרצאה שקיימת מ\"ט א\"ד שמכריעה את $SAT$: בהינתן נוסחה $\phi$ ב-CNF, היא מנחשת הצבה $\alpha$ ומקבלת אם ההצבה מספקת את הנוסחה. "
  r"המכונה עובדת בזמן פולינומי באורך הקלט. לכן $SAT \in NP$."),

Q(23, "tm",
  "מכונת טיורינג נקראת **סימפטית** אם היא בעלת 3 סרטים כאשר שלושת הראשים הקוראים זזים יחד ימינה או שמאלה. "
  "פורמלית, פונקציית המעברים היא מהצורה:"
  r"$$\delta: Q \times \Gamma^3 \to Q \times \Gamma^3 \times \{L, R\}$$"
  r"תהי $C$ מחלקת השפות להן קיימת מ\"ט סימפטית המכריעה אותן." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(("math", r"R \subset C"), ("math", r"C \supset R"), ("math", r"R = C"), NONE),
  "c",
  "**הוכחת ג והפרכת השאר:**\n"
  r"נוכיח: $R \subseteq C$. לפי ההגדרה, לכל שפה $L \in R$ קיימת מ\"ט סטנדרטית $M$ שמכריעה את $L$. "
  r"ניתן לסמלץ את המכונה $M$ ע\"י מ\"ט סימפטית $T$ באופן הבא: נתעלם מפעילות של $T$ על 2 הסרטים האחרונים, ונבצע את כל המעברים של $M$ על הסרט הראשון של $T$. "
  r"לכן גם $T$ מכריעה את $L$, ולכן $L \in C$. קבלנו: $R \subseteq C$." "\n"
  r"נוכיח: $C \subseteq R$. תהי $L \in C$ ותהי $T$ מ\"ט סימפטית שמכריעה את $L$. ניתן לסמלץ את $T$ ע\"י מ\"ט סטנדרטית $M$ "
  r"(למשל, ע\"י הגדרה של א\"ב סרט $\Gamma_M = \Gamma_T^3$ ופונקציית המעברים $\delta_M(q, (\alpha, \beta, \gamma)) = \delta_T(q, (\alpha, \beta, \gamma))$).",
  note="Proof box header reads 'הוכחת א והפרכת השאר' but the highlighted option (and the proof, R ⊆ C and C ⊆ R) is ג (R = C); header corrected to ג. Options א (R ⊂ C) and ב (C ⊃ R) are the same statement as printed (zoom-verified)."),

Q(24, "time_p",
  r"תהי $M$ מ\"ט דטרמיניסטית. להלן שתי טענות:" "\n"
  r"I. אם קיימת מילה $w$ עבורה המכונה $M$ לא עוצרת, אזי $L(M) \notin R$" "\n"
  r"II. אם לכל $n$ טבעי קיימת מילה $w$ באורך $n$ עבורה המכונה $M$ עוצרת אחרי $2^n$ צעדים, אזי $L(M) \notin P$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "b",
  r"**טענה I לא נכונה:** תהי $M = loop$ מ\"ט $M$ לא עוצרת על אף מילה, אבל $L(M) = \emptyset \in R$." "\n"
  r"**טענה II לא נכונה:** תהי $M$ = \"על קלט $x$ בצע $2^{|x|}$ צעדים קבל\"" "\n"
  r"המכונה $M$ על כל קלט $x$ עוצרת אחרי $2^{|x|}$ צעדים, אבל היא מקבלת כל מילה, ולכן השפה $L(M) = \Sigma^* \in P$."),

Q(25, "decidability",
  r"תהי $f: \Sigma^* \to \Sigma^*$ פונקציה כלשהי. לכל $y \in \Sigma^*$ נסמן:"
  r"$$A_y = \{x \in \Sigma^* \mid f(x) = y\}$$"
  r"ונתון כי $A_y = \emptyset$ לכל $y \ne \varepsilon, 00, 11$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(r"$f$ ניתנת לחישוב אם $A_{11}, A_{00}, A_\varepsilon$ הן שפות ניתנות להכרעה",
       "$f$ ניתנת לחישוב בכל מקרה",
       r"$f$ לא ניתנת לחישוב אם $A_{11}, A_{00}, A_\varepsilon$ הן שפות ניתנות לקבלה",
       "$f$ לא ניתנת לחישוב בכל מקרה"),
  "a",
  r"**הוכחת א והפרכת ד:** נוכל לבנות מכונה $F$ המחשבת את $f$, מתוך השיקול הבא: מכיוון שנתונה $f$ \"פונקציה\", הקבוצות $A_y$ מוגדרות היטב "
  r"(כלומר, לכל $x$ בתחום יש רק $y$ אחד בטווח המותאם לו על ידי הפונקציה, ומהנתון ה-$y$ הזה הוא או $00$ או $11$ או אפסילון.) "
  r"לכן כל $x$ בתחום שייך לאחת ורק לאחת משלוש הקבוצות $A_{11}, A_{00}, A_\varepsilon$. כדי לחשב את $f$ צריך רק לזהות לאיזו קבוצה מהשלוש $x$ שייך. "
  r"נסמן $M_{11}, M_{00}, M_\varepsilon$ את המכונות המכריעות את השפות, בהתאמה, שקיומן נתון, ונוכל להפעיל את שלוש המכונות כדי לזהות לאן $x$ שייך וכך לדעת מה הערך של $f(x)$." "\n"
  r"המכונה $F$ המחשבת את $f$ תפעל באופן הבא:" "\n"
  "על קלט $x$:\n"
  r"• אם $M_\varepsilon(x) = accept$ כתוב אפסילון על הסרט" "\n"
  r"• אם $M_{00}(x) = accept$ כתוב $00$ על הסרט" "\n"
  r"• אם $M_{11}(x) = accept$ כתוב $11$ על הסרט" "\n"
  r"**הפרכת ב:** אם $f$ ניתנת לחישוב בכל מקרה, אפשר להשתמש בה כדי להכריע כל אחת מהשפות $A_{11}, A_{00}, A_\varepsilon$, "
  "לכן היותן של שפות אלה ניתנות להכרעה הוא הכרחי.\n"
  r"**הפרכת ג:** שפות ניתנות להכרעה הן גם ניתנות לקבלה, והראנו שבמקרה זה $f$ כן ניתנת לחישוב. "
  "לכן היותן של השפות ניתנות לקבלה לא יכולה להיות גורם לכך שהפונקציה לא תהיה ניתנת לחישוב."),
]

exam = {
  "examCode": "26B-A",
  "examLabel": "2026 סמסטר ב מועד א",
  "year": 2026,
  "examDate": "16.6.2026",
  "sourceFile": "מבחנים/2026/חישוביות 2026 מועד א מעורבל עם תשובות.pdf",
  "keyFile": "same file (shuffled form; yellow highlights + proof boxes; Q2 unhighlighted, key from its proof box)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 26))
def _fix(x):
    """raw strings keep the backslash of \\" (e.g. in מ\\"ט) -> literal backslash shown in the app; strip it."""
    if isinstance(x, str): return x.replace('\\"', '"')
    if isinstance(x, list): return [_fix(v) for v in x]
    if isinstance(x, dict): return {k: _fix(v) for k, v in x.items()}
    return x
exam = _fix(exam)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
