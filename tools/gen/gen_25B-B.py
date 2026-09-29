# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-B.json. Questions/option order from the exam
`מבחנים/2025/סמ ב מועד ב 9.pdf`; key (yellow highlight) and explanations (blue boxes) from
`מבחנים/2025/סמ ב מועד ב פתרון 9.pdf`. Option order compared for every question: identical
in both files (Q17 prints 'א. לא נכון / ב. נכון' in BOTH files).
Run: PYTHONUTF8=1 py tools/gen/gen_25B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-B.json"
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
CLAIM2 = opts("הטענה נכונה", "הטענה לא נכונה")
TF = opts("נכון", "לא נכון")
FT = opts("לא נכון", "נכון")
ALLFALSE = "כל הטענות האחרות לא נכונות"

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "highlighted-pdf", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

questions = [
Q(1, "mapping_reductions",
  r"תהיינה $A, B$ שפות לא-טריוויאליות כך שמתקיים: $A \le_m B$." "\nאיזו מהטענות הבאות נכונה?",
  opts(r"אם $B \in RE \cup coRE$ אז $A \in RE \cup coRE$",
       r"אם $A \in RE \cap coRE$ אז $B \in RE \cap coRE$",
       r"אם $B \in coRE$ אז $A \in RE$",
       ALLFALSE),
  "a",
  r"**תזכורת:** $R = RE \cap coRE$" "\n"
  r"**הוכחת א:** נתון $A \le_m B$ ולכן ע\"פ משפט הרדוקציה אם $B$ ניתנת לקבלה אז גם $A$ ניתנת לקבלה. "
  r"מתקיים: $\overline{A} \le_m \overline{B}$ ולכן ע\"פ משפט הרדוקציה אם $\overline{B}$ ניתנת לקבלה אז גם $\overline{A}$ ניתנת לקבלה." "\n"
  r"**הפרכת ב:** $A = 1\Sigma^* \in R = RE \cap coRE$ אבל $B = H_{TM} \notin R$" "\n"
  r"**הפרכת ג:** עבור $A = B = \overline{H_{TM}}$ מתקיים $\overline{H_{TM}} \le_m \overline{H_{TM}}$ (הרדוקציה היא פונקציית הזהות). "
  r"בנוסף: $B = \overline{H_{TM}} \in coRE$ אבל $A = \overline{H_{TM}} \notin RE$"),

Q(2, "closure",
  r"תהיינה $A, B$ שפות לא-טריוויאליות כך שמתקיים: $A \in R$ וגם $A \cup B \in R$." "\n"
  "**נתבונן בטענה הבאה:** השפה $B$ ניתנת להכרעה.",
  CLAIM2, "b",
  r"**הפרכה:** $B = ALL_{TM} \notin R$, $A = \{\langle M\rangle \mid M \text{ is a Turing Machine}\}$" "\n"
  r"מתקיים: $A \cup B = A \in R$"),

Q(3, "time_p",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle \phi\rangle \mid (*)\}$$"
  "(*): $\\phi$ היא נוסחה בצורת $CNF$ כך שקיימת השמה מספקת ובה בדיוק שני משתנים מקבלים את הערך $TRUE$\n"
  r"לדוגמא, לנוסחה $\phi = (x_1 \vee x_2 \vee x_3) \wedge (x_3 \vee \overline{x_2}) \wedge (x_4 \vee x_5)$ "
  r"יש השמה מספקת שיש בה בדיוק 2 משתנים עם ערך $TRUE$: $x_1 = T,\ x_2 = F,\ x_3 = F,\ x_4 = T,\ x_5 = F$, "
  r"ולכן $\langle \phi\rangle \in L$.",
  opts(r"מתקיים $L \in P$",
       r"מתקיים $L \in P$, רק בתנאי שמתקיים $P = NP$",
       r"מתקיים $L \in NP$, רק בתנאי שמתקיים $P = NP$",
       ALLFALSE),
  "a",
  r"**הוכחת א:** קיימות $\binom{n}{2} = O(n^2)$ השמות אפשריות שיש בהן בדיוק שני משתנים שערכם $TRUE$. "
  "ניתן בזמן פולינומי דטרמיניסטי לעבור על כל ההשמות האלו ולבדוק האם יש ביניהן השמה מספקת לנוסחה נתונה שיש לה $n$ משתנים.",
  note="Printed stem: 'L = {<φ> | φ היא נוסחה בצורת CNF כך שקיימת השמה מספקת ...}' — condition moved to a (*) line."),

Q(4, "tm",
  r"יהיו $M_1, M_2$ מ\"ט לא-דטרמיניסטיות כך שמתקיים $L(M_1) = L(M_2)$." "\n"
  "**נתבונן בשתי הטענות הבאות:**\n"
  r"I. לכל קלט $w$, אם יש מסלול חישוב של $M_1$ על $w$ שמסתיים ב-ACCEPT אזי יש מסלול חישוב של $M_2$ על $w$ שמסתיים ב-ACCEPT או ב-REJECT." "\n"
  r"II. לכל קלט $w$, אם יש מסלול חישוב של $M_1$ על $w$ שמסתיים ב-ACCEPT או ב-REJECT אזי יש מסלול חישוב של $M_2$ על $w$ שמסתיים ב-ACCEPT." "\n"
  "**איזה מהסעיפים הבאים נכון:**",
  TWO_CLAIMS, "c",
  r"**הוכחת I:** אם מ\"ט לא-דטרמיניסטית $M_1$ מקבלת את $w$ אז יש מסלול חישוב של $M_1$ על $w$ שמסתיים ב-ACCEPT, ולכן $w \in L(M_1)$. "
  r"אם $L(M_1) = L(M_2)$ אז גם $M_2$ מקבלת את $w$. בפרט, יש מסלול חישוב של $M_2$ על $w$ שמסתיים ב-ACCEPT. "
  r"בפרט, יש מסלול חישוב של $M_2$ על $w$ שמסתיים ב-ACCEPT או ב-REJECT." "\n"
  r"**הפרכת II:** תהי $M_1 = M_{REJ}$ מכונה שעוצרת על כל קלט מיד ב-REJECT. תהי $M_2 = M_{LOOP}$ מכונה שלא-עוצרת על אף קלט. "
  r"השפה של שתי המכונות היא ריקה ולכן מתקיים בפרט $L(M_1) = L(M_2)$"),

Q(5, "undecidability",
  "איזו מהטענות הבאות נכונה?",
  opts(r"השפה $\overline{A_{TM}}$ מוכלת ממש בשפה $\overline{H_{TM}}$",
       r"השפה $\overline{H_{TM}}$ מוכלת ממש בשפה $\overline{A_{TM}}$",
       ("math", r"H_{TM} = \overline{A_{TM}}"),
       ALLFALSE),
  "b",
  r"**הוכחת ב:** על פי הגדרת השפות מתקיים $A_{TM} \subseteq H_{TM}$ וזוהי הכלה ממש. "
  r"לכן, השפה $\overline{H_{TM}}$ מוכלת ממש בשפה $\overline{A_{TM}}$"),

Q(6, "npc",
  "**נתבונן בשתי הטענות הבאות:**\n"
  r"I. אם $P \ne NP$ אזי מתקיים $SAT \notin NPC$." "\n"
  r"II. אם $P \ne NP$ אזי מתקיים $PATH \notin NPC$." "\n"
  "**איזה מהסעיפים הבאים נכון:**",
  TWO_CLAIMS, "d",
  r"**הפרכת I:** ע\"פ **משפט קוק-לוין** מתקיים $SAT \in NPC$ בלי תלות בשאלה האם $NP = P$." "\n"
  r"**הוכחת II:** נניח בשלילה $PATH \in NPC$ אבל אז מתקיים $NPC \cap P \ne \emptyset$ אבל אז מתקיים $P = NP$, בסתירה לנתון."),

Q(7, "poly_reductions",
  "תהיינה $A, B$ שפות לא-טריוויאליות. **נתבונן בשתי הטענות הבאות:**\n"
  r"I. אם $A \le_p B$ אזי מתקיים $A \le_m B$." "\n"
  r"II. אם $A \le_p B$ וגם $B \le_p A$ אזי מתקיים $A = B$." "\n"
  "**איזה מהסעיפים הבאים נכון:**",
  TWO_CLAIMS, "c",
  "**הוכחת I:** כל רדוקציה פולינומיאלית היא רדוקציית מיפוי.\n"
  r"**הפרכת II:** קיימת רדוקציה פולינומיאלית בין כל שתי שפות לא-טריוויאליות ששייכות למחלקה $P$, "
  r"ולכן ניתן לקחת כדוגמא נגדית את $A = PATH$, $B = 1\Sigma^*$",
  note="Claim I prints the subscript as capital P ('A ≤_P B'); written as \\le_p."),

Q(8, "mapping_reductions",
  r"**נתבונן בטענה הבאה:** מתקיים $ALL_{TM} \le_m EQ_{TM}$.",
  CLAIM2, "a",
  r"נגדיר את הפונקציה הבאה: $f(\langle M\rangle) = \langle M, M_{ALWAYS\_ACC}\rangle$, "
  r"כאשר $M_{ALWAYS\_ACC}$ היא מכונה שעוצרת מיד ב-ACCEPT על כל קלט."),

Q(9, "npc",
  r"**נתבונן בטענה הבאה:** תהי $L$ שפה כך שמתקיים: $L \le_p SAT$ וגם $CLIQUE \le_p L$." "\n"
  "אזי השפה $L$ היא NP-שלימה.",
  CLAIM2, "a",
  r"אם $L \le_p SAT$ אז ע\"פ משפט הרדוקציה הפולינומית $L \in NP$." "\n"
  r"אם $CLIQUE \le_p L$ וגם $L \in NP$ וגם $CLIQUE \in NPC$ אז ע\"פ משפט שהוכחנו בהרצאה: $L \in NPC$",
  note="Printed with capital-P subscripts ('≤_P'); written as \\le_p."),

Q(10, "tm",
  "תהי $M$ מכונת הטיורינג הבסיסית הבאה:\n"
  "איזו מהטענות הבאות היא נכונה?",
  opts(r"מתקיים $L(M) \in R$ וגם $M$ מכונה מכריעה",
       r"מתקיים $L(M) \notin R$ וגם $M$ מכונה מכריעה",
       r"מתקיים $L(M) \in R$ וגם $M$ מכונה לא-מכריעה",
       ALLFALSE),
  "a",
  r"במצב ההתחלה המכונה $M$ כותבת רווח בתא הראשון בסרט, הולכת שמאלה (כלומר, עומדת במקום), עוברת למצב $q_1$, ואז עוצרת במצב מקבל על כל קלט." "\n"
  r"לכן, המכונה $M$ מכריעה את השפה סיגמא כוכב, וברור שהשפה סיגמא כוכב ניתנת להכרעה.",
  image="images/exams/25B-B-Q10.png"),

Q(11, "decidability",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle A\rangle \mid (*)\}$$"
  "(*): $|L(A)| \\ge 2$ וגם $A$ הוא אס\"ד\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "a",
  "אם הקידוד הוא לא קידוד תקין של אס\"ד, אז נדחה.\n"
  "בהינתן קידוד תקין של אס\"ד, ניתן להכריע האם השפה של האס\"ד היא ריקה.\n"
  "אם השפה של האס\"ד היא ריקה, אז נדחה.\n"
  "אחרת, השפה של האס\"ד היא לא-ריקה. נריץ חיפוש לרוחב ונמצא מילה $w$ כלשהי שמתקבלת ע\"י האס\"ד.\n"
  r"נבנה אס\"ד מכפלה לשפת החיתוך $A \cap (\Sigma^* \setminus w)$" "\n"
  "ונבדוק האם השפה של האס\"ד החדש שבנינו היא ריקה, אם השפה ריקה, אז נדחה. אחרת, נקבל.",
  note="Printed stem: 'L = {<A> | |L(A)| ≥ 2 וגם A הוא אס\"ד}' — condition moved to a (*) line."),

Q(12, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid M \text{ accepts some } w \text{ where } |w| \ge 5\}$$"
  r"כלומר, $\langle M\rangle \in L$ אם קיימת מילה $w$ המכילה לפחות 5 תווים כך שהמכונה $M$ עוצרת על $w$ במצב מקבל." "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "b",
  r"השפה $L$ ניתנת לקבלה כי אפשר לנחש מילה $w$ המכילה לפחות 5 תווים ואז להריץ את $M$ על $w$ ולענות כמותה." "\n"
  r"נראה רדוקציה $A_{TM} \le_m L$ כאשר $f(\langle M, w\rangle) = \langle K_{M,w}\rangle$, ונגדיר: "
  r"המכונה $K_{M,w}$ = \"על קלט $y$, הרץ את $M$ על $w$. אם הריצה $M(w)$ הסתיימה ב-ACCEPT, עצור ב-ACCEPT. אחרת, היכנס ל-LOOP.\"" "\n"
  r"ברור שאם $M$ מקבלת את $w$ אז $K_{M,w}$ מקבלת כל קלט. בנוסף, ברור שאם $M$ לא-מקבלת את $w$ אז $K_{M,w}$ לא-מקבלת אף קלט."),

Q(13, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid L(M) = \Sigma^* \text{ and } M \text{ accepts every } w \text{ with more than } |w| \text{ steps}\}$$"
  r"כלומר, $\langle M\rangle \in L$ אם $L(M) = \Sigma^*$ וגם לכל $w$ המכונה $M$ עוצרת על $w$ במצב מקבל לאחר ביצוע של לפחות $|w|$ צעדי חישוב." "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "d",
  r"מספיק להראות רדוקציה $ALL_{TM} \le_m L$ כאשר $f(\langle M\rangle) = \langle M_{long}\rangle$, ונגדיר: "
  r"המכונה $M_{long}$ = \"על קלט $y$, לך לסוף הקלט וחזור להתחלה. הרץ את $M$ על $y$ וענה כמותה.\"" "\n"
  r"ברור שאם $M$ מקבלת את $w$ אז $M_{long}$ מקבלת את $w$ לאחר ביצוע של לפחות $|w|+1$ צעדי חישוב. "
  r"בנוסף, ברור שאם $M$ לא-מקבלת את $w$ אז גם $M_{long}$ לא-מקבלת את $w$"),

Q(14, "tm",
  r"**נתבונן בטענה הבאה:** לכל $k > 1$ קיימת שפה $L_k$, כך שקיימת מכונת טיורינג עם $k$ סרטים שמכריעה את $L_k$, "
  r"אבל לא-קיימת מכונה עם $k-1$ סרטים שמכריעה את $L_k$.",
  CLAIM2, "b",
  "קיימת שקילות חישובית בין כל הווריאנטים הסבירים של מכונות הטיורינג.\n"
  r"בפרט, לכל $k > 1$ קיימת מכונת טיורינג עם $k$ סרטים שמכריעה שפה $L$ אם ורק אם קיימת מכונה עם $k-1$ סרטים שמכריעה את $L$."),
]

contexts = {
  "blk": {"kind": "text", "title": "בלוק של שאלות 15–18",
          "text": r"בהינתן גרף $G$ לא-מכוון ומספר טבעי $k$, נגדיר את הפונקציה הבאה: $f(\langle G, k\rangle) = \langle G, k+1\rangle$." "\n"
                  "בנוסף, נגדיר את השפה הבאה:\n"
                  r"$$L = \{\langle G, k\rangle \mid (*)\}$$"
                  r"(*): הגרף הלא מכוון $G$ מכיל תת קבוצה $S$ של קודקודים בגודל $k$ שהיא קליקה או $G$ מכיל תת קבוצה $T$ של קודקודים בגודל $k$ שהיא בלתי תלויה" "\n"
                  r"כלומר, $\langle G, k\rangle \in L$ אם הגרף הלא-מכוון $G$ מכיל קליקה בגודל $k$ או מכיל קבוצה בלתי-תלויה של קודקודים בגודל $k$." "\n"
                  "**הערה חשובה:** שימו לב הגדרת השפה בשאלה זו שונה מהגדרת השפה $L$ שהופיעה בחלק זה של המבחן במועד א'.\n"
                  "**ענו נכון או לא נכון, לכל אחת מהטענות הבאות:**"},
}

questions += [
Q(15, "poly_reductions", r"אם $f(\langle G, k\rangle) \in CLIQUE$ אזי $\langle G, k\rangle \in L$", TF, "a",
  r"אם $\langle G, k+1\rangle \in CLIQUE$ אז הגרף מכיל קליקה של $k$ קודקודים",
  contextId="blk"),
Q(16, "poly_reductions", r"אם $f(\langle G, k\rangle) \in L$ אזי $\langle G, k\rangle \in IS$", TF, "b",
  r"**הפרכה ע\"י דוגמה נגדית:** יהי $k > 1$ ויהי $G$ גרף מלא עם $k+1$ קודקודים (כלומר, גרף שמכיל את כל הצלעות האפשריות)." "\n"
  r"אז מתקיים: $\langle G, k+1\rangle \in L$ אבל אין בו קבוצה ב\"ת בגודל $k$. לכן $\langle G, k\rangle \notin IS$.",
  contextId="blk"),
Q(17, "poly_reductions", r"אם $f(\langle G, k\rangle) \notin L$ אזי $\langle G, k\rangle \notin CLIQUE$", FT, "a",
  r"**הפרכה ע\"י דוגמה נגדית:** יהי $k > 1$ ויהי $G$ גרף שמכיל קליקה של $k$ קודקודים וקודקוד נוסף שאינו מחובר בצלע לאף קודקוד אחר "
  r"(כלומר, הגרף מכיל סה\"כ $k+1$ קודקודים)." "\n"
  r"אז $\langle G, k+1\rangle \notin L$ אבל $\langle G, k\rangle \in CLIQUE$",
  contextId="blk",
  note="Options printed 'א. לא נכון / ב. נכון' in both exam and solution; highlighted א = 'לא נכון'."),
Q(18, "poly_reductions", r"אם $f(\langle G, k\rangle) \notin CLIQUE$ אזי $\langle G, k\rangle \notin L$", TF, "b",
  r"**הפרכה ע\"י דוגמה נגדית:** יהי $k > 1$ ויהי $G$ גרף ריק שמכיל $k+1$ קדקודים (כלומר, גרף ללא צלעות)." "\n"
  r"אז $\langle G, k+1\rangle \notin CLIQUE$ אבל $\langle G, k\rangle \in L$",
  contextId="blk"),
]

def _unescape(o):
    """raw strings keep '\\"' literally (e.g. ע\\"פ) -> plain '"'."""
    if isinstance(o, str): return o.replace('\\"', '"')
    if isinstance(o, list): return [_unescape(x) for x in o]
    if isinstance(o, dict): return {k: _unescape(v) for k, v in o.items()}
    return o
questions = _unescape(questions)
contexts = _unescape(contexts)

exam = {
  "examCode": "25B-B",
  "examLabel": "2025 סמסטר ב מועד ב",
  "year": 2025,
  "examDate": "9.7.2025",
  "sourceFile": "מבחנים/2025/סמ ב מועד ב 9.pdf",
  "keyFile": "מבחנים/2025/סמ ב מועד ב פתרון 9.pdf (yellow highlights + blue proof boxes; option order identical to exam)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 19))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
