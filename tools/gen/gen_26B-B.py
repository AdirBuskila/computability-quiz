# -*- coding: utf-8 -*-
"""Generator for tools/raw/26B-B.json (flagship). Transcribed by hand from the rendered pages
of `מבחנים/2026/חישוביות 2026 מועד ב עם תשובות מתוקן שאלה 17.pdf` (key = yellow highlight,
explanations = the blue proof boxes). Run: PYTHONUTF8=1 py tools/gen/gen_26B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "26B-B.json"
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

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "highlighted-pdf", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

questions = [
Q(1, "mapping_reductions",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. $\overline{ALL_{TM}} \le_m \overline{EQ_{TM}}$" "\n"
  r"II. $H_{10} \le_m \overline{A_{TM}}$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "c",
  "**טענה I נכונה:** נגדיר פונקציה $f(\\langle M\\rangle) = \\langle M, TOTAL\\rangle$ כאשר המכונה $TOTAL$ "
  "היא מכונה העוצרת במצב מקבל על כל קלט. זוהי פונקציה ניתנת לחישוב המקיימת "
  r"$x \in \overline{ALL_{TM}} \Leftrightarrow f(x) \in \overline{EQ_{TM}}$." "\n"
  r"**טענה II אינה נכונה:** $H_{10} \in RE - R$, $\overline{A_{TM}} \in coRE - R$ ושתי שפות כאלה לא ניתנות לרדוקציה אחת לשנייה."),

Q(2, "tm",
  "נתונה מכונת טיורינג $M$ המתוארת על ידי דיאגרמת המצבים הבאה. זוהי מכונה דטרמיניסטית "
  "(בכל מקום שלא מוגדר מעבר, יש להניח שהמעבר הוא ל-$q_{rej}$ והוא לא צויר רק לשם פשטות הדיאגרמה). "
  "א\"ב הקלט של $M$ הוא $\\{a,b\\}$ וא\"ב הסרט כולל בנוסף גם את תו הרווח.\n"
  "איזה מהביטויים הרגולריים הבאים מתאר את $L(M)$?",
  opts(("math", "(bb)^*"), ("math", "(ab)^*"), ("math", "ab^*"), "אף אחת מהתשובות האחרות אינה נכונה"),
  "a",
  "בשביל שמילה תתקבל, היא צריכה להיות או ריקה (ומיד מתקבלת) או מתחילה ב-$b$ (ואז התו הראשון יוחלף ב-$a$). "
  "משם יכולים להיות רק תווי $b$ עד הרווח. ואז מתחילים לחזור אחורה – מספר אי-זוגי של תווי $b$ עד ה-$a$ הראשונה "
  "(שהחליפה את ה-$b$), ואז המילה מתקבלת. כלומר, מילת הקלט המתקבלת באופן זה מורכבת ממספר זוגי של תווי $b$ בלבד.\n"
  "**הפרכת ב:** מילה המתחילה ב-$a$ מיד נדחית על ידי המכונה.\n**הפרכת ג:** כנ\"ל.",
  image="images/exams/26B-B-Q2.png"),

Q(3, "mapping_reductions",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M, w\rangle \mid (*)\}$$"
  "(*): $M$ מקבלת את $w$ ב-$k$ צעדים כאשר $k$ מתקיים $|w| \\le k$\n"
  "אזי מתקיים:",
  opts(("math", r"L \le_m A_{TM}"), ("math", r"EQ_{TM} \le_m L"),
       ("math", r"L \le_m PALINDROMES"), ("math", r"\overline{A_{TM}} \le_m L")),
  "a",
  "**הוכחת א:** נגדיר פונקציה $f(\\langle M,w\\rangle) = \\langle M^*, w\\rangle$ כאשר $M^*$ היא המכונה הבאה: "
  "על קלט $\\langle M,w\\rangle$: אם $M(w) = accept$ וגם מספר הצעדים עד לעצירה הוא גדול מ-$|w|$ אזי קבל, אחרת דחה. "
  r"זוהי פונקציה ניתנת לחישוב המקיימת $\langle M,w\rangle \in L \Leftrightarrow f(\langle M,w\rangle) \in A_{TM}$." "\n"
  "**הפרכת ב:** השפה $L$ היא שפה הניתנת לקבלה (בהינתן $M,w$ ניתן לסמלץ את $M$ על $w$; אם $M$ עוצרת אחרי $k$ צעדים "
  "ומתקיים $|w| \\le k$ אזי קבל, אחרת דחה), ולכן סעיף ב מהווה סתירה למשפט הרדוקציה (כי $EQ_{TM}$ לא ניתנת לקבלה).\n"
  "**הפרכת ג:** כנ\"ל, סתירה למשפט הרדוקציה כי $PALINDROMES$ היא שפה ניתנת להכרעה.\n"
  r"**הפרכת ד:** כנ\"ל, סתירה למשפט הרדוקציה כי $\overline{A_{TM}}$ היא שפה לא ניתנת לקבלה.",
  note="Printed stem: 'L = { <M,w> | M מקבלת את w ב k צעדים כאשר k מתקיים |w| ≤ k }' — condition moved to a (*) line to keep Hebrew out of math."),

Q(4, "closure",
  "תהי $L$ שפה. נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $L \le_m A_{TM}$ וגם $L \le_m E_{TM}$ אזי $L \in R$" "\n"
  r"II. אם $L \in RE$ וגם $L \le_m \overline{L}$ אזי $L \in R$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  r"**טענה I נכונה:** אם $L \le_m A_{TM}$ אזי $L \in RE$ (כי $A_{TM} \in RE$). כמו כן $L \le_m E_{TM}$ ולכן גם "
  r"$\overline{L} \le_m \overline{E_{TM}}$. כמו כן $\overline{E_{TM}} \in RE$ ולכן $\overline{L} \in RE$. "
  r"כעת גם $L$ וגם $\overline{L}$ שייכים ל-$RE$, ולכן $L \in R$." "\n"
  r"**טענה II נכונה:** אם $L \le_m \overline{L}$ ניתן להפעיל משלים על שני האגפים ולקבל $\overline{L} \le_m L$ ולכן גם "
  r"$\overline{L} \in RE$. כעת גם $L$ וגם $\overline{L}$ שייכים ל-$RE$, ולכן $L \in R$."),

Q(5, "decidability",
  "תהי $M$ מ\"ט, ותהי $w$ מילה ($w \\in \\Sigma^*$) ותהי $C$ קונפיגורציה. נאמר ש-$C$ **ישיגה** מ-$w$ ב-$M$ "
  "אם ריצתה של $M$ כאשר הקלט הוא המילה $w$ מגיעה ל-$C$.\n"
  "נגדיר את השפה:\n"
  r"$$L = \{\langle M, k, w, C\rangle \mid (*)\}$$"
  "(*): $C$ ישיגה מ-$w$ ב-$M$ אחרי לכל היותר $k$ צעדים\n"
  "אזי מתקיים:",
  DEC4, "a",
  "ניתן לסמלץ (על ידי מכונת טיורינג אוניברסלית) את ריצת $M$ על המילה $w$ למשך $k$ צעדים (סימולציה בזמן סופי). "
  "אחרי כל צעד ניתן לבדוק אם הגענו לקונפיגורציה $C$. במידה וכן הסימולציה תחזיר $ACCEPT$. במידה ולא (לאחר זמן סופי) "
  "הסימולציה תחזיר $REJECT$. התוכנית הזו רצה בזמן סופי ונותנת את התשובה הנכונה תמיד. ולכן $L$ ניתנת להכרעה.",
  note="Printed stem: 'L = {<M,k,w,C> | C ישיגה מ w ב M אחרי לכל היותר k צעדים}' — split so Hebrew stays out of math."),

Q(6, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid L(M) = \{000, 0000\}\}$$"
  "אזי מתקיים:",
  DEC4, "d",
  r"**$L \notin RE$:** נוכיח ע\"י רדוקציה $\overline{H_{TM}} \le_m L$. נגדיר $f(\langle M,w\rangle) = \langle O1_{M,w}\rangle$ "
  "כך ש-$O1_{M,w}$ המכונה שמוגדרת כך: בהינתן קלט $x$: אם $x=000$ או $x=0000$ קבל; הרץ את $M$ על $w$; קבל. "
  "זוהי פונקציה ניתנת לחישוב (רק מייצרים את הקידוד, לא מריצים אותה). "
  r"כמו כן, אם $\langle M,w\rangle \in \overline{H_{TM}}$ אזי $L(O1_{M,w}) = \{000,0000\}$ ולכן $\langle O1_{M,w}\rangle \in L$. "
  r"מהצד השני, אם $\langle M,w\rangle \notin \overline{H_{TM}}$ אזי $L(O1_{M,w}) = \Sigma^*$ ולכן $\langle O1_{M,w}\rangle \notin L$." "\n"
  r"**$L \notin coRE$:** נוכיח ע\"י רדוקציה $H_{TM} \le_m L$ ולכן גם $\overline{H_{TM}} \le_m \overline{L}$. "
  r"נגדיר $f(\langle M,w\rangle) = \langle O2_{M,w}\rangle$ כך ש-$O2_{M,w}$ המכונה שמוגדרת כך: בהינתן קלט $x$: הרץ את $M$ על $w$; "
  "אם $x=000$ או $x=0000$ קבל, אחרת דחה. זוהי פונקציה ניתנת לחישוב. "
  r"כמו כן, אם $\langle M,w\rangle \in H_{TM}$ אזי $L(O2_{M,w}) = \{000,0000\}$ ולכן $\langle O2_{M,w}\rangle \in L$. "
  r"מהצד השני, אם $\langle M,w\rangle \notin H_{TM}$ אזי $L(O2_{M,w}) = \emptyset$ ולכן $\langle O2_{M,w}\rangle \notin L$.",
  note="Source proof box has typos: '{00,0000}' for {000,0000} and '<K_{m,w}>' for <O1_{m,w}>; corrected in the explanation."),

Q(7, "mapping_reductions",
  "יהיו $A, B$ שפות לא טריוויאליות מעל הא\"ב הבינארי $\\Sigma = \\{0,1\\}$. נתון שלא קיימת "
  r"$f: \Sigma^* \to \Sigma^*$ ניתנת לחישוב שעבורה לכל $x \in \Sigma^*$ מתקיים $x \in A$ אם\"ם $f(x) \notin B$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts("קיימת רדוקציית מיפוי מ-$A$ ל-$B$",
       r"לא קיימת רדוקציית מיפוי מ-$A$ ל-$\overline{B}$",
       r"יתכן ש-$A \in R$ ו-$B \in coRE$",
       r"אם $B \in RE$ אזי $A \in coRE$"),
  "b",
  "**הוכחת ב:** הפונקציה הנתונה (לו הייתה קיימת) מהווה רדוקציה $A \\le_m \\overline{B}$. כלומר לא קיימת רדוקציית מיפוי "
  "מ-$A$ ל-$\\overline{B}$.\n"
  r"**הפרכת א:** $A = H_{TM}$, $B = PALINDROMES$." "\n"
  r"**הפרכת ג:** אם $A \in R$ והשפה $B$ לא טריוויאלית, אזי קיימת רדוקציה $A \le_m \overline{B}$, בסתירה לנתון." "\n"
  r"**הפרכת ד:** $A = A_{TM}$, $B = \overline{E_{TM}}$."),

Q(8, "poly_reductions",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $A \le_p \overline{B}$ וגם $B \le_p \overline{C}$ אזי מתקיים $A \le_p C$." "\n"
  r"II. אם $A \le_p \overline{B}$ וגם $A \not\le_p C$ אזי מתקיים $\overline{B} \not\le_p C$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  r"**טענה I נכונה:** אם $B \le_p \overline{C}$ אזי מתקיים גם $\overline{B} \le_p C$. ומטרנזיטיביות של רדוקציה פולינומיאלית, "
  r"אם $A \le_p \overline{B}$ ו-$\overline{B} \le_p C$ אזי $A \le_p C$." "\n"
  r"**טענה II נכונה:** נניח בשלילה ש-$\overline{B} \le_p C$. מכיוון ש-$A \le_p \overline{B}$, מטרנזיטיביות נקבל כי "
  r"$A \le_p C$, בסתירה לכך ש-$A \not\le_p C$."),
]

NONE = "אף אחת מהתשובות האחרות אינה נכונה"

questions += [
Q(9, "closure",
  r"יהיו $L_1, L_2$ שתי שפות המקיימות $L_1 \in RE$ וגם $L_2 \in RE$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(("math", r"L_1 \setminus L_2 \in RE \setminus R"),
       r"יתכן $L_1 \setminus L_2 \in R$",
       ("math", r"L_1 \setminus L_2 \in coRE \setminus R"),
       ("math", r"L_1 \setminus L_2 \notin \overline{RE \cup coRE}")),
  "b",
  r"**הוכחת ב:** $L_1 = \Sigma^*$, $L_2 = \emptyset$. אזי מתקיים כי $L_1, L_2 \in RE$ ו-$L_1 \setminus L_2 = \Sigma^*$, ואכן $\Sigma^* \in R$." "\n"
  "**הפרכת א, ג, ד:** הדוגמה הנ\"ל.",
  note="Proof box literally says 'הפרכת א, ב, ג' — a typo (ב is the answer); written as א, ג, ד."),

Q(10, "npc",
  "תהי $L$ שפה לא-טריוויאלית.\nאיזו מהטענות הבאות נכונה?",
  opts(r"אם $\overline{L} \notin P$ וגם $L \in NPC$ אזי $P \ne NP$",
       r"אם $P \ne NP$ וגם $L \in P$ אזי $L \in NPC$",
       r"אם $L \in NPC$ וגם $\overline{L} \in P$ אזי $P \ne NP$",
       NONE),
  "a",
  r"**הוכחת א:** אם $\overline{L} \notin P$ אז גם $L \notin P$ ($P$ סגורה למשלים ולכן אם $L \in P$ אזי $\overline{L} \in P$ בסתירה להנחה). "
  r"אם $L \in NPC$ אזי בפרט $L \in NP$. מכיוון ש-$L \notin P$ נקבל כי $P \ne NP$." "\n"
  r"**הפרכת ב:** אם $P \ne NP$, אז $P$ ו-$NPC$ הן מחלקות זרות." "\n"
  r"**הפרכת ג:** אם $\overline{L} \in P$ אז גם $L \in P$, כך שאם גם $L \in NPC$, אז $P = NP$."),

Q(11, "closure",
  r"תהי $L \subseteq \Sigma^*$. נגדיר לכל $k \in \mathbb{N}$ את השפה $L_k = \{w \in L \mid |w| \ge k\}$." "\n"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם לכל $k \in \mathbb{N}$, השפה $L_k \in R$ אזי $L \in R$" "\n"
  r"II. אם $L \in coRE$ אזי לכל $k \in \mathbb{N}$ $L_k \in coRE$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  r"**טענה I נכונה:** נשים לב כי מתקיים $L = L_0$, לכן לפי הנתון $L_0$ ניתנת להכרעה, ולכן גם $L$." "\n"
  r"**טענה II נכונה:** לכל $k$ מתקיים $L_k = L \cap \{w \mid |w| \ge k\}$ וזו שפה ב-$coRE$ כי היא חיתוך של שתי שפות ב-$coRE$."),

Q(12, "decidability",
  r"תהיינה $A, B$ שפות כך שמתקיים: $A \in RE \setminus R$ וגם $B \in coRE \setminus R$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(("math", r"A \cap B = \emptyset"), ("math", r"A \cup B = \Sigma^*"),
       r"$EQ_{TM} \le_m A$ וגם $EQ_{TM} \le_m B$", NONE),
  "d",
  r"**הפרכת א:** עבור $A = H_{TM}$, $B = \overline{A_{TM}}$, אזי עבור מכונה $M$ כלשהי אשר מקבלת $x$ כלשהו מתקיים: "
  r"$\langle M, x\rangle \in A \cap B$." "\n"
  r"**הפרכת ב:** עבור $A = A_{TM}$, $B = \overline{H_{TM}}$, אזי עבור מכונה $M$ כלשהי אשר דוחה $x$ כלשהו מתקיים: "
  r"$\langle M, x\rangle \notin A \cup B$." "\n"
  r"**הפרכת ג:** $EQ_{TM}$ לא ניתנת לקבלה וגם המשלימה שלה לא ניתנת לקבלה, ולכן (לפי משפט הרדוקציה) לא קיימת רדוקציה ממנה לא ל-$A$ ולא ל-$B$.",
  note="Option א printed with the glyph ϕ (empty set); rendered as \\emptyset."),

Q(13, "npc",
  "איזו מהטענות הבאות נכונה?",
  opts("קיימת שפה סופית שאינה ניתנת להכרעה",
       r"אם $A \le_m B$ אזי $\overline{B} \le_m \overline{A}$",
       r"$P \ne NP$ אם ורק אם $CLIQUE \notin P$",
       NONE),
  "c",
  "**הפרכת א:** כל שפה סופית היא רגולרית (קיים עבורה אוטומט) ולכן גם ניתנת להכרעה.\n"
  r"**הפרכת ב:** עבור $A \in R$, $B \in RE - R$, נקבל שמתקיים $A \le_m B$ אבל $\overline{B} \not\le_m \overline{A}$ (אחרת נקבל סתירה למשפט הרדוקציה)." "\n"
  r"**הוכחת ג:** לפי המשפט $P \cap NPC \ne \emptyset \Leftrightarrow P = NP$ והעובדה ש-$CLIQUE \in NPC$."),

Q(14, "npc",
  "נתונה הטענה הבאה:\n"
  r"לכל $A, B \in NPC$ שאינן טריוויאליות מתקיים כי $A \le_p B$ וגם $B \le_p A$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  opts(r"הטענה נכונה אם ורק אם $P = NP$",
       r"הטענה נכונה אם ורק אם $P \ne NP$",
       r"הטענה נכונה (ללא קשר ליחס בין המחלקות $P, NP$)",
       r"הטענה אינה נכונה (ללא קשר ליחס בין המחלקות $P, NP$)"),
  "c",
  r"**הפרכת א:** ראו הוכחת ג שאינה תלויה ב-$P = NP$." "\n"
  r"**הפרכת ב:** ראו הוכחת ג שאינה תלויה ב-$P \ne NP$." "\n"
  r"**הוכחת ג:** מהגדרת $NPC$ והנתון נובע: $A \in NPC, B \in NP \Rightarrow B \le_p A$ וגם $B \in NPC, A \in NP \Rightarrow A \le_p B$." "\n"
  "**הפרכת ד:** ראו הוכחת ג."),

Q(15, "poly_reductions",
  "נגדיר שפה:\n"
  r"$$CLIQUE_{3D} = \{\langle G, k\rangle \mid (*)\}$$"
  "(*): $G$ גרף לא מכוון עם דרגת כל קדקוד לכל היותר 3, ויש ב-$G$ קליקה בגודל $k$\n"
  "ונגדיר פונקציה:\n"
  r"$$f_1(\langle G, k\rangle) = \langle G, k\rangle$$"
  r"האם הפונקציה $f_1$ מקיימת את תנאי הרדוקציה הפולינומיאלית $CLIQUE_{D3} \le_P CLIQUE$?",
  opts("לא, כי $f_1$ לא ניתנת לחישוב",
       "כן",
       "לא, כי הפונקציה ניתנת לחישוב אבל בזמן לא פולינומיאלי",
       r"לא, כי הפונקציה לא מקיימת את התנאי $f_1(x) \in CLIQUE \Leftrightarrow x \in CLIQUE_{D3}$"),
  "d",
  r"**הוכחת ד והפרכת השאר:** נוכיח שהפונקציה ניתנת לחישוב בזמן פולינומיאלי אך לא מקיימת: $f_1(x) \in CLIQUE \Leftrightarrow x \in CLIQUE_{D3}$." "\n"
  "• מכיוון שמדובר בפונקציית הזהות, אין צורך לעשות שום שינוי לקלט, והמכונה יכולה ישר לעצור ולסיים את החישוב עם הפלט הנדרש.\n"
  "• אם יש לכל קדקוד דרגה לכל היותר 3 וגם יש קליקה בגודל $k$ בגרף המקורי, אז בגרף ה\"חדש\" (שהוא זהה לגרף המקורי) יש קליקה בגודל $k$, כיוון זה של תנאי הרדוקציה מתקיים.\n"
  "• אם בגרף המתקבל מהפונקציה יש קליקה בגודל $k$ אז בגרף המקור (שהוא זהה לגרף שעליו הפונקציה פעלה) בוודאי יש קליקה בגודל $k$, אבל אין שום הכרח שדרגת כל קדקוד היא לכל היותר 3 "
  "(למשל גרף עם קליקה בגודל $k=4$ שבו לקדקוד כלשהו דרגה גדולה מ-3).",
  note="Stem prints CLIQUE_{3D} in the definition and CLIQUE_{D3} / ≤_P in the question — kept as printed. "
       "Proof box ends with a drawn example graph (not reproduced); last bullet's example text paraphrased from it."),

Q(16, "poly_reductions",
  "נגדיר שפה:\n"
  r"$$2CLIQUE = \{\langle G, k\rangle \mid (*)\}$$"
  "(*): $G$ גרף לא מכוון, ויש ב-$G$ שתי קליקות זרות, כל אחת בגודל $k$\n"
  "ונגדיר פונקציה:\n"
  r"$$f_2(\langle G, k\rangle) = \langle G2, k\rangle$$"
  "כאשר $G2$ הינו גרף שמכיל שני עותקים נפרדים של הגרף $G$.\n"
  r"האם הפונקציה $f_2$ מקיימת את תנאי הרדוקציה הפולינומיאלית $CLIQUE \le_P 2CLIQUE$?",
  opts("לא, כי $f_2$ לא ניתנת לחישוב",
       "כן",
       "לא, כי הפונקציה ניתנת לחישוב אבל בזמן לא פולינומיאלי.",
       r"לא, כי הפונקציה לא מקיימת את התנאי $f_2(x) \in 2CLIQUE \Leftrightarrow x \in CLIQUE$"),
  "b",
  r"**הוכחת ב והפרכת השאר:** נוכיח שהפונקציה ניתנת לחישוב בזמן פולינומיאלי ומקיימת: $f_2(x) \in 2CLIQUE \Leftrightarrow x \in CLIQUE$." "\n"
  "• המכונה המחשבת פועלת כך: עבור הקדקוד הראשון רצה עד סוף רשימת הקדקודים, מסיטה את כל הקלט הצידה כדי לפנות מקום לכתיבה של קדקוד חדש (העתק של הקדקוד הראשון); "
  "כך עבור כל שאר הקדקודים; כנ\"ל עבור הצלע הראשונה עד האחרונה, יוצרת העתקים התואמים לקדקודים החדשים שהוספו.\n"
  "• אם יש קליקה בגודל $k$ בגרף שהתקבל כקלט לפונקציה, אז בגרף שהפונקציה מחזירה יהיו שתי קליקות נפרדות כל אחת בגודל $k$, אחת בכל עותק.\n"
  "• אם יש שתי קליקות נפרדות בגרף שהפונקציה מחזירה, כל אחת בגודל $k$, אזי מכיוון שמדובר בשני עותקים שונים, מתקיים אחד משני המקרים הבאים: "
  "בגרף שהתקבל כקלט לפונקציה יש שתי קליקות זרות בגודל $k$, ובפרט יש קליקה אחת בגודל $k$ בגרף זה; "
  "או בכל אחד מהעותקים יש קליקה נפרדת בגודל $k$, ובפרט יש קליקה אחת בגודל $k$ בגרף שהתקבל כקלט לפונקציה."),

Q(17, "classification",
  r"נתונה השפה $L = \{\langle M\rangle \mid (*)\}$ כאשר (*): $M$ לא עוצרת על אף מילה." "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "c",
  r"**הוכחת ג והפרכת השאר:**" "\n"
  r"• **$\overline{L}$ ניתנת לקבלה:** ניתן לבנות מכונה לא דטרמיניסטית, אשר בהינתן $\langle M\rangle$ תנחש מילה $w$ ותריץ את $M$ על $w$. "
  "אם $M$ עוצרת על $w$, המכונה עוצרת ב\"קבל\".\n"
  r"• **$L$ לא-ניתנת לקבלה:** ניתן לעשות רדוקציה מהמשלימה של $H_{TM}$ על ידי שימוש במכונה $K_{M,w}$.",
  note="File name: 'מתוקן שאלה 17' — the corrected version; no in-document note on what changed (ASK_ADIR #9)."),
]

# Q18-Q20 share a definitions block.
contexts = {
  "abc": {"kind": "text", "title": "הגדרות לשאלות 18–20",
          "text": "שלוש השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  r"$$A = \{\langle M, N\rangle \mid L(M) = L(N)\}$$"
                  r"$$B = \{\langle M, N\rangle \mid L(M) \le_p L(N)\}$$"
                  r"$$C = \{\langle M, N\rangle \mid L(M) \le_m L(N)\}$$"},
}

def rel(x, y):
    return opts(("math", rf"{x} \subset {y}"), ("math", rf"{y} \subset {x}"), ("math", rf"{x} = {y}"), NONE)

questions += [
Q(18, "poly_reductions", "מהו היחס בין $A$ ל-$B$?", rel("A", "B"), "a",
  "**הוכחת א והפרכת השאר:** יחס הרדוקציה הפולינומיאלית הוא רפלקסיבי (כל שפה ניתנת לרדוקציה פולינומיאלית לעצמה). "
  "אך יש שפות שיש ביניהן רדוקציה פולינומיאלית ובכל זאת אינן שוות.", contextId="abc"),
Q(19, "mapping_reductions", "מהו היחס בין $A$ ל-$C$?", rel("A", "C"), "a",
  "**הוכחת א והפרכת השאר:** כנ\"ל, לגבי רדוקציית מיפוי.", contextId="abc"),
Q(20, "poly_reductions", "מהו היחס בין $B$ ל-$C$?", rel("B", "C"), "a",
  "**הוכחת א והפרכת השאר:** אם קיימת רדוקציה פולינומיאלית, אזי קיימת גם רדוקציית מיפוי. "
  "אך יש מצבים שקיימת רדוקציית מיפוי ולא קיימת רדוקציה פולינומיאלית (ראינו דוגמה בקורס).", contextId="abc"),

Q(21, "decidability",
  "רוצים להוכיח ש-$L$ ניתנת להכרעה. איזה מהסעיפים הבאים מספיק כדי להוכיח את הטענה?",
  opts(r"קיימת מ\"ט בסיסית $M$ שמקיימת $L(M) = L$",
       r"קיימת מ\"ט לא דטרמיניסטית $M$ שמקיימת $L(M) = L$",
       r"קיימת מ\"ט בסיסית $M$ שמקיימת $L(M) = \overline{L}$",
       r"קיימת מ\"ט בסיסית $M$ שמקיימת $L(M) = \overline{L}$ וגם מתקיים $\overline{L} \le_m L$."),
  "d",
  r"**הפרכת א:** $L = A_{TM}$." "\n**הפרכת ב:** דוגמה כנ\"ל.\n"
  r"**הפרכת ג:** $L = E_{TM}$." "\n"
  r"**הוכחת ד:** מהנתון הראשון $\overline{L}$ ניתנת לקבלה. מהנתון השני, ועל פי משפט, מתקיים גם $L \le_m \overline{L}$, "
  r"ולפי משפט הרדוקציה נקבל שגם $L$ ניתנת לקבלה. שפה שגם היא וגם המשלימה שלה ניתנות לקבלה, היא אכן שפה ניתנת להכרעה."),

Q(22, "classification",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. $CLIQUE \le_m \overline{H_{10}}$" "\n"
  r"II. $H_{10} \in NP$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "c",
  r"**טענה I נכונה:** $CLIQUE \in R$ וגם $\overline{H_{10}}$ לא טריוויאלית, ולכן על פי משפט קיימת רדוקציה כנדרש." "\n"
  r"**טענה II לא נכונה:** $H_{10} \in RE - R$, $NP \subseteq R$."),

Q(23, "np",
  "תהי $L \\in NPC$.\nנתבונן בשתי הטענות הבאות:\n"
  r"I. קיימת מ\"ט לא דטרמיניסטית שמקבלת כל מילה $w \in L$" "\n"
  r"II. קיימת מ\"ט לא דטרמיניסטית עם מסלול מקבל באורך לכל היותר $|w|!$ עבור כל מילה ששייכת ל-$L$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  "**טענה I נכונה:** מהנתון קיימת מכונה לא דטרמיניסטית המקבלת את $L$ בזמן פולינומיאלי.\n"
  "**טענה II נכונה:** מהנתון קיימת מכונה לא דטרמיניסטית המקבלת את $L$ בזמן פולינומיאלי. ולכן בוודאי שקיים מסלול באורך לכל היותר $|w|!$ המקבל כל מילה ב-$L$."),

Q(24, "closure",
  r"תהיינה $A \ne B$ ניתנות לקבלה ($A \in RE$ וגם $B \in RE$)." "\n"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. יתכן ש-$A \subset B$" "\n"
  r"II. יתכן ש-$(A \in RE \setminus R) \wedge (B \in RE \setminus R) \wedge (A \setminus B \in R)$" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  r"**טענה I נכונה:** $A = A_{TM}$, $B = H_{TM}$." "\n**טענה II נכונה:** אותה דוגמה הנ\"ל."),

Q(25, "decidability",
  r"תהי $M$ מ\"ט. נסמן $M(x) = y$ כאשר על הקלט $x$, $M$ עוצרת והמילה $y$ רשומה על הסרט בסוף הריצה. ונגדיר:" "\n"
  r"$$A_y = \{x \in \Sigma^* \mid M(x) = y\}$$"
  r"ונתון כי $A_y \ne \emptyset$ לכל $y$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts("$M$ מכריעה את $L(M)$",
       "$A_y$ ניתנת להכרעה לכל $y$",
       r"$\overline{A_y}$ ניתנת לקבלה לכל $y$",
       "$A_y$ ניתנת לקבלה לכל $y$"),
  "d",
  r"**הוכחת ד:** נבנה מכונה מקבלת עבור $A_y$ באופן הבא: על קלט $x$: הרץ את $M$ על $x$. אם $M$ עוצרת וכתוב $y$ על הסרט, קבל. אחרת דחה." "\n"
  r"**הפרכת א:** דוגמה נגדית: המכונה $M$ אשר לכל $x$, אם $x$ זוגי רושמת על הסרט $y = x/2$ ועוצרת בקבל, ואם $x$ אי-זוגי רצה עד אינסוף. "
  r"זוהי מכונה המקבלת את השפה של כל המספרים הזוגיים, אבל לא מכריעה אותה. ולכל $y$ מתקיים $A_y = \{2y\} \ne \emptyset$." "\n"
  r"**הפרכת ב:** דוגמה נגדית: נגדיר מכונה $M$ ונראה שעבורה השפה $A_\varepsilon$ לא ניתנת להכרעה. המכונה $M$ על קלט $x$ פועלת כך: "
  r"אם $x = \langle 0, y\rangle$ כתוב $y$ על הסרט ועצור; אם $x = \langle 1, M', w\rangle$ אזי אם $M'(w) = accept$ עצור וכתוב $\varepsilon$ על הסרט, אחרת כתוב $x$ על הסרט; "
  r"אחרת עצור וכתוב $x$ על הסרט. לכל $y$ מתקיים $\langle 0, y\rangle \in A_y$ ולכן $A_y \ne \emptyset$. "
  r"כמו כן מתקיים $A_{TM} \le_m A_\varepsilon$ על ידי פונקציית הרדוקציה $f(\langle M', w\rangle) = \langle 1, M', w\rangle$ ולכן $A_\varepsilon$ לא ניתנת להכרעה." "\n"
  "**הפרכת ג:** אם ג היה נכון, מכיוון שד' נכון, היינו מקבלים שגם ב נכון. אבל הפרכנו את ב. לכן גם ג לא נכון."),
]

exam = {
  "examCode": "26B-B",
  "examLabel": "2026 סמסטר ב מועד ב",
  "year": 2026,
  "examDate": "8.7.2026",
  "sourceFile": "מבחנים/2026/חישוביות 2026 מועד ב עם תשובות מתוקן שאלה 17.pdf",
  "keyFile": "same file (yellow highlights + proof boxes; corrected Q17 version)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 26))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
