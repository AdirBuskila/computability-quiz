# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-A.json. Questions/option order from the exam
`מבחנים/2025/סמ ב מועד א 8.pdf`; key (yellow highlight) and explanations (blue boxes) from
`מבחנים/2025/סמ ב מועד א פתרון 8.pdf`. Option order was compared page by page: identical
except Q17, where the solution swaps the two options (see note there).
Run: PYTHONUTF8=1 py tools/gen/gen_25B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-A.json"
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
ALLFALSE = "כל הטענות האחרות לא נכונות"

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "highlighted-pdf", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

questions = [
Q(1, "mapping_reductions",
  r"אם $A \le_m B$ וגם $A \not\le_m C$ (כלומר, לא קיימת רדוקציית מיפוי מהשפה $A$ לשפה $C$)." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(r"$B \not\le_m C$ (כלומר, לא קיימת רדוקציית מיפוי מהשפה $B$ לשפה $C$).",
       ("math", r"C \le_m A"), ("math", r"B \le_m A"), ALLFALSE),
  "a",
  r"**הוכחת א:** נניח בשלילה שקיימת רדוקציית מיפוי מהשפה $B$ לשפה $C$ אז מטרנזיטיביות רדוקצית המיפוי "
  r"קיימת רדוקציית מיפוי מהשפה $A$ לשפה $C$. סתירה לנתון." "\n"
  r"**הפרכת ב:** $C = \overline{H_{TM}}$, $A = H_{TM}$" "\n"
  r"**הפרכת ג:** $A = 1\Sigma^*$, $B = H_{TM}$"),

Q(2, "classification",
  r"תהי $L$ שפה כך שמתקיים: $EQ_{TM} \le_m L$." "\nאיזו מהטענות הבאות נכונה?",
  DEC4, "d",
  r"**הוכחת ד:** ידוע שהשפה $EQ_{TM}$ לא-ניתנת לקבלה וגם $\overline{EQ_{TM}}$ לא-ניתנת לקבלה." "\n"
  r"ולכן ע\"פ משפט הרדוקציה אם מתקיים: $EQ_{TM} \le_m L$ אז $L$ לא-ניתנת לקבלה." "\n"
  r"בנוסף מתקיים $\overline{EQ_{TM}} \le_m \overline{L}$ ולכן ע\"פ משפט הרדוקציה $\overline{L}$ לא-ניתנת לקבלה"),

Q(3, "time_p",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. תהי $f: \Sigma^* \to \Sigma^*$ פונקציה המקיימת שלכל $x$ מתקיים $f(x) \in \{0, 1, 11, 111\}$, אזי $f$ ניתנת לחישוב" "\n"
  r"II. תהי $f: \Sigma^* \to \Sigma^*$ פונקציה המקיימת שלכל $x$ מתקיים $f(x) \in \{0, 1, 11, 111\}$, אזי $f$ ניתנת לחישוב **בזמן פולינומי**" "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "b",
  r"**הוכחת ב:** הראינו בהרצאה דוגמא לפונקציה בינארית (שהפלט שלה הוא 0 או 1, כלומר $f(x) \in \{0, 1\}$) שהיא "
  "לא-ניתנת לחישוב, בפרט היא לא-ניתנת לחישוב בזמן פולינומיאלי",
  note="'בזמן פולינומי' is underlined in the source; rendered bold."),

Q(4, "tm",
  "מכונת טיורינג נקראת \"משוגעת\" (crazy) היא מכונה שדומה מאוד למכונת טיורינג בסיסית דטרמיניסטית. ההבדל היחיד "
  "הוא שבמקום להישאר במקום כאשר זזים שמאלה מהתא הכי שמאלי, הראש הקורא של המכונה המשוגעת זז לתא הכי ימני בסרט "
  "שמכיל תו שהוא לא תו רווח (אם כל התאים על הסרט מכילים תווי רווח, הראש הקורא של המכונה המשוגעת נשאר במקום).\n"
  r"נגדיר: $RE_{crazy} = \{L(M) \mid M \text{ is a crazy } TM\}$" "\n"
  "איזו מהטענות הבאות נכונה?",
  opts("המחלקה $RE$ מוכלת ממש במחלקה $RE_{crazy}$",
       "המחלקה $RE_{crazy}$ מוכלת ממש במחלקה $RE$",
       ("math", r"RE = RE_{crazy}"), ALLFALSE),
  "c",
  r"**כיוון א':** תהי $C$ מ\"ט \"משוגעת\". נבנה מ\"ט בסיסית $M$ שקולה." "\n"
  r"$M$ = \"על קלט $x$:" "\n"
  r"1. נזיז את הקלט $x$ מקום אחד ימינה בסרט, ונוסיף תו $\#$ בתא השמאלי של הסרט. נסמן בתו $\text{\textdollar}$ את הקצה הימני של הקלט. "
  r"**הנחה:** תו $\#$ ותו $\text{\textdollar}$ אינם חלק מא\"ב הסרט של המכונה $C$" "\n"
  r"2. נסמלץ את מ\"ט $C$." "\n"
  r"- אם הראש של $C$ זז ימינה לתו $\text{\textdollar}$, נכתוב בתא זה תו רווח ונעתיק את ה-$\text{\textdollar}$ לתא הבא מימין, נחזיר את הראש להצביע לתא עם הרווח שהוספנו, "
  r"ונחזור למצב בו היינו כאשר זזנו ימינה לתו $\text{\textdollar}$ ונמשיך בסימולציה." "\n"
  r"- אם הראש של $C$ זז שמאלה לתו $\#$, נזוז ימינה עד תו ה-$\text{\textdollar}$ ואז נלך שמאלה עד שנגיע לתו שהוא לא-רווח." "\n"
  r"- בכל מקרה אחר נבצע בדיוק אותן הפעולות כמו $C$." "\n"
  r"3. אם $C$ עוצרת במצב ACCEPT – נקבל, אם $C$ עוצרת במצב REJECT – נדחה.\"" "\n"
  r"**הוכחת הנכונות:** לכל קלט $x$, מ\"ט הבסיסית $M$ מבצעת את הצעדים של $C$ ואם $C$ עוצרת, אז $M$ עוצרת ומחזירה תשובה בהתאם. "
  r"לכן $L(M) = L(C)$." "\n"
  r"**כיוון ב':** תהי $M$ מ\"ט דטרמיניסטית בסיסית עם סרט אחד. נבנה מ\"ט $C$ \"משוגעת\" שקולה." "\n"
  r"$C$ = \"על קלט $x$:" "\n"
  r"1. סמן את תחילת הסרט ב-$\#$ והזז את הקלט $x$ מקום אחד ימינה על הסרט." "\n"
  r"2. בצע סימולציה של $M$. אם הראש של $M$ זז שמאלה ומגיע לתו ה-$\#$, הזז את הראש תו אחד ימינה." "\n"
  r"3. אם $M$ עוצרת – עצור והחזר תשובה כמו התשובה של $M$.\"" "\n"
  r"**הוכחת הנכונות:** מ\"ט $C$ מבצעת את הצעדים של $M$. בריצה המקורית של $M$ על קלט $x$, אם הראש של $M$ היה זז שמאלה "
  r"מהקצה של הסרט, הוא היה נשאר במקום. בסימולציה של $M$ ע\"י $C$ הראש של $M$ זז לתו ה-$\#$, ו-$C$ מחזירה אותו למקום הקודם, "
  r"בדיוק כמו בריצה המקורית של $M$ על $x$. לפי הבניה, הראש של $C$ אף פעם לא מנסה לזוז שמאלה מהקצה של הסרט, לכן הסימולציה "
  r"של $M$ ע\"י $C$ מבצעת את אותם צעדי חישוב בדיוק כמו $M$ בריצה המקורית על $x$." "\n"
  r"לכן $L(C) = L(M)$, כנדרש.",
  note="Stem: 'M is a crazy TM' kept in English inside \\text{}. Solution box on sol p.4 (the yellow marks on M and C there are not answer marks)."),

Q(5, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$H^*_{TM} = \{\langle M\rangle \mid (*)\}$$"
  "(*): $M$ עוצרת על כל קלט\n"
  "איזו מהטענות הבאות נכונה?",
  opts(r"השפה $H^*_{TM}$ מוכלת ממש בשפה $ALL_{TM}$",
       r"השפה $ALL_{TM}$ מוכלת ממש בשפה $H^*_{TM}$",
       ("math", r"H^*_{TM} = \overline{ALL_{TM}}"), ALLFALSE),
  "b",
  r"תהי $M_{REJ}$ מכונה שעוצרת על כל קלט מיד ב-REJECT" "\n"
  r"תהי $M_{LOOP}$ מכונה שלא-עוצרת על אף קלט" "\n"
  r"**הפרכת א:** $\langle M_{REJ}\rangle$ שייכת לשפה $H^*_{TM}$ אבל לא-שייכת לשפה $ALL_{TM}$" "\n"
  r"**הוכחת ב:** אם המכונה עוצרת על כל קלט ב-ACCEPT אז היא עוצרת על כל קלט. "
  r"בנוסף, $\langle M_{REJ}\rangle$ שייכת לשפה $H^*_{TM}$ אבל לא-שייכת לשפה $ALL_{TM}$, ולכן זו הכלה ממש" "\n"
  r"**הפרכת ג:** המכונה $\langle M_{LOOP}\rangle$ שייכת לשפה $\overline{ALL_{TM}}$ אבל לא-שייכת לשפה $H^*_{TM}$"),

Q(6, "np",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. תהי $L \in P$ אזי מתקיים $L \in NP$." "\n"
  r"II. תהי $L \in NP$ אזי מתקיים $L \in RE$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  "**הוכחת א:** כל שפה שניתנת להכרעה בזמן פולינומי דטרמיניסטי היא שפה שניתנת להכרעה בזמן פולינומי לא-דטרמינסטי\n"
  "כל שפה שניתנת להכרעה בזמן פולינומי לא-דטרמינסטי היא שפה ניתנת להכרעה. בפרט, שפה הניתנת לקבלה.",
  note="Solution box on sol p.6 (top)."),

Q(7, "poly_reductions",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $A \le_m \overline{B}$ אזי מתקיים $\overline{A} \le_m B$." "\n"
  r"II. אם $A \le_p \overline{B}$ אזי מתקיים $\overline{A} \le_p B$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "a",
  r"**הוכחת א:** הראינו בהרצאה שמתקיים $L_1 \le_m L_2 \Leftrightarrow \overline{L_1} \le_m \overline{L_2}$" "\n"
  r"באותו האופן ניתן להראות $L_1 \le_p L_2 \Leftrightarrow \overline{L_1} \le_p \overline{L_2}$"),

Q(8, "npc",
  r"שתי שפות $A, B$ יקראו \"שקולות פולינומיאלית\" אם $A \le_p B$ וגם $B \le_p A$." "\n"
  "**נתבונן בטענה הבאה:** כל שתי שפות $NP$-שלמות הן שקולות פולינומיאלית.",
  CLAIM2, "a",
  r"**הטענה נכונה.** ע\"פ הגדרת $NP$-שלמות: אם $A, B \in NPC$" "\n"
  r"אז מתקיים $A \le_p B$ (כי $B \in NPC$ וגם $A \in NP$)" "\n"
  r"וגם מתקיים $B \le_p A$ (כי $A \in NPC$ וגם $B \in NP$)."),

Q(9, "npc",
  r"**נתבונן בטענה הבאה:** אם בעתיד מישהו יצליח להראות שמתקיים $SAT \le_p PATH$ אז ניתן יהיה להסיק שהמחלקה $NP$ סגורה למשלים.",
  CLAIM2, "a",
  r"**הטענה נכונה.** אם בעתיד מישהו יצליח להראות שמתקיים $SAT \le_p PATH$ אז ע\"פ משפט הרדוקציה הפולינומית נוכל להסיק "
  r"שהשפה $SAT$ שייכת ל-$P \cap NPC$ ולכן מתקיים $P = NP$." "\n"
  r"כידוע, המחלקה $P$ סגורה למשלים ולכן אם $P = NP$, אז נוכל להסיק שהמחלקה $NP$ סגורה למשלים"),

Q(10, "npc",
  "תהי $L$ שפה לא-טריוויאלית. איזו מהטענות הבאות היא נכונה?",
  opts(r"אם $P \ne NP$ וגם $L \in NPC$ אזי השפה $L$ היא סופית",
       r"אם $P = NP$ וגם השפה $L$ היא סופית אזי $L \in NPC$",
       r"אם $L \in NPC$ וגם $\overline{L} \in P$ אזי $P \ne NP$",
       ALLFALSE),
  "b",
  r"**הפרכת א:** שפה סופית היא רגולרית ולכן היא שייכת ל-$P$. "
  r"מתקיים $P \ne NP$ אם ורק אם $P \cap NPC = \emptyset$, ולכן כל השפות הסופיות הן לא $NP$-שלמות." "\n"
  r"**הוכחת ב:** אם $NP = P$ אז יש רדוקציה פולינומית מכל שפה ב-$P$ לכל שפה לא-טריוויאלית ב-$P$." "\n"
  r"**הפרכת ג:** המחלקה $P$ סגורה לחיתוך ולכן $L \in P$ ולכן $P \cap NPC \ne \emptyset$, ולכן $NP = P$. סתירה.",
  note="Refutation of ג says 'P סגורה לחיתוך' (presumably meant 'למשלים'); kept as printed."),

Q(11, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle A_1, A_2\rangle \mid (*)\}$$"
  r"(*): $A_1$ הוא אס\"ד וגם $A_2$ הוא אס\"ד כך שמתקיים $L(A_1) \cup L(A_2) = \Sigma^*$",
  DEC4, "a",
  "בהינתן קידוד של זוג אס\"דים ניתן לבנות את אוטומט המכפלה לשפת האיחוד.\n"
  "מאוטומט האיחוד ניתן לבנות את האוטומט לשפה המשלימה ואז לבדוק בזמן סופי האם השפה של האוטומט האחרון שבנינו היא ריקה\n"
  r"הבעיה $E_{DFA}$ ניתנת להכרעה."),

Q(12, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M, w\rangle \mid M \text{ accepts } w \text{ and the tape is empty at some point of the run}\}$$"
  r"כלומר, $\langle M, w\rangle \in L$ אם $M$ עוצרת על $w$ במצב מקבל וגם במהלך הריצה של $M$ על $w$ קיימת נקודת זמן "
  r"כלשהי שבה הסרט של המכונה $M$ מכיל רק תווי רווח." "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "b",
  r"**דוגמא:** המכונה $M_{01}$ = \"על קלט $y$, אם אורך $y$ הוא זוגי, מחק את תוכן הסרט והכנס ל-LOOP. "
  r"אחרת (אורך $y$ אי-זוגי), מחק את תוכן הסרט, כתוב על הסרט 01 ועצור ב-ACCEPT\"." "\n"
  r"אז מתקיים: $\langle M_{01}, 111\rangle \in L$ אבל $\langle M_{01}, \varepsilon\rangle \notin L$" "\n"
  r"**השפה $L$ ניתנת לקבלה** כי אפשר לבנות מכונה אוניברסלית \"מיוחדת\" שאחרי כל צעד סימולציה של $M$ על $w$ בודקת האם הסרט "
  r"של המכונה שהיא מסמלצת הוא ריק. ואז אם $M$ על $w$ עוצרת ב-ACCEPT **וגם** קרה האירוע שבמהלך הריצה של $M$ על $w$ "
  "הסרט של $M$ היה ריק אז המכונה האוניברסלית \"המיוחדת\" תעצור ב-ACCEPT אחרת, תיכנס ללולאה אינסופית. "
  "תזכורת: במצגת 2 הוכחנו את הטענה הבאה: **טענה:** האורך של כל קונפיגורציה במסלול החישוב של מ\"ט הוא **סופי.** "
  "ולכן ניתן לבנות את המכונה האוניברסלית ה\"מיוחדת\".\n"
  r"**השפה $L$ לא-ניתנת להכרעה** נראה רדוקציה $A_{TM} \le_m L$ כאשר $f(\langle M, w\rangle) = \langle M_{epsilon\_tape}, w\rangle$, ונגדיר:" "\n"
  r"המכונה $M_{epsilon\_tape}$ = \"על קלט $y$, הרץ את $M$ על $y$. אם הריצה $M(y)$ הסתיימה ב-ACCEPT, מחק את כל תוכן הסרט "
  "ועצור ב-ACCEPT. אחרת, הכנס ל-LOOP\".\n"
  r"ברור שאם $M$ מקבלת את $w$ אז $M_{epsilon\_tape}$ מקבלת את $w$ וגם לפני סוף הריצה הסרט של $M_{epsilon\_tape}$ יהיה ריק." "\n"
  r"בנוסף, ברור שאם $M$ לא-מקבלת את $w$ אז גם $M_{epsilon\_tape}$ לא-מקבלת את $w$",
  note="Stem set-builder is printed in English inside the formula; kept via \\text{}. Solution box spans sol pp.8-9."),

Q(13, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid 2024 \le |L(M)| \le 2025\}$$"
  "איזו טענה נכונה?",
  DEC4, "d",
  r"**נראה כי** $\overline{H_{TM}} \le_m L$. כיוון שמתקיים $\overline{H_{TM}} \notin RE$ אז נוכל להסיק שמתקיים $L \notin RE$" "\n"
  r"**תיאור הרדוקציה:** נגדיר את פונ' הרדוקציה כך: $f\langle M, w\rangle = \langle M^{2024}_w\rangle$" "\n"
  r"המכונה $M^{2024}_w$ = \"על קלט $y$:" "\n"
  r"• אם $y \in \{0, 00, \ldots, 0^{2024}\}$ אז עצור ב-ACCEPT" "\n"
  r"• אחרת, הרץ את $M$ על $w$" "\n"
  "• ACCEPT\"\n"
  r"**נראה כי** $\overline{H_{TM}} \le_m \overline{L}$. כיוון שמתקיים $\overline{H_{TM}} \notin RE$ אז נוכל להסיק שמתקיים $\overline{L} \notin RE$" "\n"
  r"**תיאור הרדוקציה:** נגדיר את פונ' הרדוקציה כך: $f\langle M, w\rangle = \langle K^{2024}_w\rangle$" "\n"
  r"המכונה $K^{2024}_w$ = \"על קלט $y$:" "\n"
  r"• הרץ את $M$ על $w$" "\n"
  r"• אם $y \in \{0, 00, \ldots, 0^{2024}\}$ אז ACCEPT אחרת, REJECT\""),

Q(14, "decidability",
  r"יהיו $M_1, M_2$ מ\"ט כך שמתקיים $L(M_1) \subseteq L(M_2)$." "\n"
  "**נתבונן בשתי הטענות הבאות:**\n"
  r"I. לכל קלט $w$, אם $M_1$ מקבלת את $w$ אזי $M_2$ עוצרת על $w$." "\n"
  r"II. לכל קלט $w$, אם $M_1$ עוצרת על $w$ אזי $M_2$ עוצרת על $w$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "c",
  r"**הוכחת I:** אם $M_1$ מקבלת את $w$ וגם $L(M_1) \subseteq L(M_2)$ אז $M_2$ מקבלת את $w$ ובפרט, $M_2$ עוצרת על $w$." "\n"
  r"**הפרכת II:** תהי $M_1 = M_{REJ}$ מכונה שעוצרת על כל קלט מיד ב-REJECT. תהי $M_2 = M_{LOOP}$ מכונה שלא-עוצרת על אף קלט. "
  r"השפה של שתי המכונות היא ריקה ולכן מתקיים בפרט $L(M_1) \subseteq L(M_2)$"),
]

contexts = {
  "blk": {"kind": "text", "title": "בלוק של שאלות 15–18",
          "text": r"בהינתן גרף $G$ לא-מכוון ומספר טבעי $k$, נגדיר את הפונקציה הבאה: $f(\langle G, k\rangle) = \langle \overline{G}, k\rangle$" "\n"
                  r"כאשר $\overline{G}$ הוא הגרף המשלים של הגרף $G$." "\n"
                  "בנוסף, נגדיר את השפה הבאה:\n"
                  r"$$L = \{\langle G, k\rangle \mid (*)\}$$"
                  r"(*): הגרף הלא מכוון $G$ מכיל תת קבוצה $S$ של קודקודים בגודל $k$ שהיא קליקה וגם $G$ מכיל תת קבוצה $T$ של קודקודים בגודל $k$ שהיא בלתי תלויה" "\n"
                  "**ענו נכון או לא נכון, לכל אחת מהטענות הבאות:**"},
}

questions += [
Q(15, "poly_reductions", r"אם $\langle G, k\rangle \in L$ אזי $f(\langle G, k\rangle) \in CLIQUE$", TF, "a",
  r"**הוכחה:** אם $\langle G, k\rangle \in L$ אז הגרף מכיל קבוצה ב\"ת של $k$ קודקודים אז הגרף המשלים מכיל קליקה של $k$ קודקודים",
  contextId="blk"),
Q(16, "poly_reductions", r"אם $\langle G, k\rangle \in IS$ אזי $f(\langle G, k\rangle) \in L$", TF, "b",
  r"**הפרכה ע\"י דוגמה נגדית:** יהי $G$ גרף עם $k > 1$ קדקודים וללא צלעות (גרף ריק)." "\n"
  r"מתקיים: $\langle G, k\rangle \in IS$." "\n"
  r"הגרף המשלים $\overline{G}$ הוא גרף מלא עם $k$ קדקודים, לכן אין בו קבוצה ב\"ת בגודל $k$. לכן $f(\langle G, k\rangle) \notin L$",
  contextId="blk"),
Q(17, "poly_reductions", r"אם $\langle G, k\rangle \notin CLIQUE$ אזי $f(\langle G, k\rangle) \notin L$", TF, "a",
  r"**הוכחה:** אם $\langle G, k\rangle \notin CLIQUE$ אז הגרף לא-מכיל קליקה של $k$ קודקודים אז הגרף המשלים לא-מכיל קבוצה ב\"ת של $k$ קודקודים",
  contextId="blk",
  note="OPTION ORDER DIFFERS: the exam prints 'א. נכון / ב. לא נכון'; the solution prints them swapped "
       "('א. לא נכון / ב. נכון') and highlights 'ב. נכון'. Matched by content: answer = 'נכון' = exam letter א."),
Q(18, "poly_reductions", r"אם $\langle G, k\rangle \notin L$ אזי $f(\langle G, k\rangle) \notin CLIQUE$", TF, "b",
  r"**הפרכה ע\"י דוגמה נגדית:** יהי $G$ גרף עם $k > 1$ קדקודים וללא צלעות (גרף ריק)." "\n"
  r"ב-$G$ אין קליקה בגודל $k$, לכן $\langle G, k\rangle \notin L$." "\n"
  r"הגרף המשלים $\overline{G}$ הוא גרף מלא עם $k$ קדקודים, ולכן יש בו קליקה בגודל $k$. לכן $f(\langle G, k\rangle) \in CLIQUE$.",
  contextId="blk"),
]

exam = {
  "examCode": "25B-A",
  "examLabel": "2025 סמסטר ב מועד א",
  "year": 2025,
  "examDate": "8.7.2025",
  "sourceFile": "מבחנים/2025/סמ ב מועד א 8.pdf",
  "keyFile": "מבחנים/2025/סמ ב מועד א פתרון 8.pdf (yellow highlights + blue proof boxes; Q17 options swapped vs exam)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 19))
def _fix(x):
    """raw strings keep the backslash of \\" (e.g. in מ\\"ט) -> literal backslash shown in the app; strip it."""
    if isinstance(x, str): return x.replace('\\"', '"')
    if isinstance(x, list): return [_fix(v) for v in x]
    if isinstance(x, dict): return {k: _fix(v) for k, v in x.items()}
    return x
exam = _fix(exam)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
