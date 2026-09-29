# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-A.json. Transcribed by hand from the rendered pages of
`מבחנים/2024/סמסטר ב/מועד א פתרון מתוקן.pdf` (corrected key: yellow highlight for Q1-14,
red "נכון/לא נכון" text for Q15-18; explanations = the blue solution boxes).
The file `2024-07-08-...-moedA-no-sol.pdf` is a web-shuffler retype with a wrong key and was IGNORED.
Run: PYTHONUTF8=1 py tools/gen/gen_24B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-A.json"
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
    "שתי הטענות I, II הן לא נכונות.",
    "טענה I נכונה וגם טענה II לא נכונה.",
    "טענה II נכונה וגם טענה I לא נכונה.",
)
DEC4 = opts(
    "השפה $L$ ניתנת להכרעה.",
    "השפה $L$ ניתנת לקבלה אבל לא ניתנת להכרעה.",
    r"השפה $L$ לא ניתנת לקבלה אבל $\overline{L}$ ניתנת לקבלה.",
    r"השפה $L$ לא ניתנת לקבלה וגם $\overline{L}$ לא ניתנת לקבלה.",
)
TF = opts("נכון", "לא נכון")
ALLFALSE = "כל הטענות האחרות לא נכונות"

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "corrected-key", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

questions = [
Q(1, "mapping_reductions",
  "תהיינה $A, B$ שתי שפות שונות זו מזו.\nאיזו מהטענות הבאות נכונה?",
  opts(r"אם מתקיים $A \le_m B$ וגם $B \le_m A$ אז מתקיים: $A \in R$ וגם $B \in R$.",
       r"אם מתקיים $A \le_m B$ וגם $B \le_m A$ אז מתקיים: $A \in RE \setminus R$ וגם $B \in R$.",
       r"אם מתקיים $A \le_m B$ וגם $B \le_m A$ אז מתקיים: $A \in R$ וגם $B \in RE \setminus R$.",
       ALLFALSE + "."),
  "d",
  r"**הפרכת סעיפים א, ב, ג:** מתקיים $A_{TM} \le_m H_{TM}$ וגם $H_{TM} \le_m A_{TM}$ אבל $A_{TM} \in RE \setminus R$ וגם $H_{TM} \in RE \setminus R$."),

Q(2, "closure",
  r"תהיינה $L_1 \in R$ וגם $L_2 \in RE$ שפות. מה מהבאים **לא** בהכרח מתקיים?",
  opts(("math", r"L_2 \setminus L_1 \in RE"), ("math", r"L_1 \setminus L_2 \in RE"),
       ("math", r"L_1 \cap L_2 \in RE"), ("math", r"L_1 \cup L_2 \in RE")),
  "b",
  r"**הוכחת א:** מתקיים $L_2 \setminus L_1 = L_2 \cap \overline{L_1}$. זהו חיתוך של שתי שפות, שכל אחת מהן היא ב-$RE$. "
  r"ולכן $L_2 \setminus L_1$ שייך ל-$RE$ (כי המחלקה $RE$ סגורה לחיתוך)." "\n"
  r"**הפרכת ב:** $L_1 = \Sigma^*$, $L_2 = A_{TM}$." "\n"
  r"**הוכחת ג, ד:** המחלקה $RE$ סגורה לחיתוך ואיחוד."),

Q(3, "tm",
  "נתבונן בשתי הטענות הבאות:\n"
  "I. אם קיימת מכונת טיורינג **לא** דטרמיניסטית בעלת סרט אחד שמכריעה שפה $L$ אז בהכרח קיימת מכונת טיורינג "
  "דטרמיניסטית בעלת שני סרטים המכריעה את $L$.\n"
  "II. אם $M$ מכונת טיורינג **לא** דטרמיניסטית וגם $K$ מכונה המתקבלת מהמכונה $M$ על ידי הפיכת המצב המקבל של $M$ "
  "למצב דוחה, ועל ידי הפיכת המצב הדוחה של $M$ למצב מקבל, אזי מתקיים כי $L(M) \\ne L(K)$.\n"
  "איזה מהסעיפים הבאים נכון?",
  TWO_CLAIMS, "c",
  "**הוכחת הטענה הראשונה:** כל הוואריאנטים שקולים זה לזה. בפרט, מ\"ט ל\"ד בעלת סרט אחד שקולה למכונה בסיסית. "
  "בנוסף, מכונה דטרמיניסטית בעלת שני סרטים שקולה גם למכונה בסיסית.\n"
  r"**הפרכת הטענה השנייה:** נניח שהמכונה $M$ לא-עוצרת על אף קלט. אז $L(M) = \emptyset = L(K)$.",
  note="Printed claim II reads 'וע\"י על ידי הפיכת' (doubled word) — cleaned to 'ועל ידי הפיכת'."),

Q(4, "tm",
  "השלימו:\n"
  "אם דיאגרמת המצבים של מ\"ט $M$ ______ מסלול מהמצב ההתחלתי $q_0$ למצב $q_{acc}$ אזי השפה $L(M)$ היא בהכרח ______",
  opts("מכילה, ריקה", "מכילה, לא ריקה", "לא מכילה, ריקה", "לא מכילה, לא ריקה"),
  "c",
  "**רעיון ההוכחה:** אם לא קיים מסלול בדיאגרמה של המכונה מהמצב ההתחלתי למצב המקבל אז לא קיים מסלול חישוב "
  "שמסתיים במצב מקבל ולכן השפה של המכונה היא ריקה.\n"
  "**הפרכת ב:** (בפתרון מצוירת דיאגרמה: מעבר מ-$q_0$ ל-$q_1$ בתוויות "
  r"$1 \to \sqcup, L$, $0 \to \sqcup, L$, $\sqcup \to \sqcup, L$; מעבר מ-$q_1$ ל-$ACC$ בתווית $0 \to 0, R$; "
  r"ומעבר מ-$q_1$ ל-$REJ$ בתווית $\sqcup \to \sqcup, R$.)" "\n"
  "בדיאגרמת המצבים של מכונה זו יש מסלול מכוון מהמצב ההתחלתי למקבל, אבל השפה היא ריקה (כי המצב ההתחלתי הופך את "
  "התו בתא הראשון לרווח, ואז \"הראש\" הולך שמאלה אבל בפועל \"הראש\" נשאר במקום. כעת, בתא הראשון כתוב רווח, ולכן "
  "בצעד החישוב הבא החישוב יסתיים תמיד בדחייה).",
  note="The refutation of ב contains a drawn TM diagram (sol p.4); its transitions are transcribed in text in the explanation (parenthetical)."),

Q(5, "mapping_reductions",
  "תהיינה $A, B, C$ שפות.",
  opts(r"אם $A \cap B \le_m C$ אז מתקיים: $A \le_m C$ וגם $B \le_m C$.",
       r"אם $A \cap B \le_m C$ אז מתקיים: $A \le_m C$ או $B \le_m C$.",
       r"אם $A \cap B \le_m C$ אז מתקיים: $C \le_m A \cap B$",
       ALLFALSE),
  "d",
  r"**הפרכת א', ב':** ניקח $A = A_{TM}$, $B = \overline{A_{TM}}$, $C = (\Sigma\Sigma\Sigma)^*$. "
  r"אז מתקיים $\emptyset \le_m (\Sigma\Sigma\Sigma)^*$ כי יש רדוקציה מכל שפה ניתנת להכרעה לכל שפה לא טריוויאלית. "
  r"אבל, לא מתקיים $A_{TM} \le_m (\Sigma\Sigma\Sigma)^*$ וגם לא מתקיים $\overline{A_{TM}} \le_m (\Sigma\Sigma\Sigma)^*$." "\n"
  r"**הפרכת ג':** ניקח $A = B = (\Sigma\Sigma\Sigma)^*$, $C = A_{TM}$.",
  note="Stem as printed has no explicit question line ('איזו מהטענות הבאות נכונה?' is absent in the source)."),

Q(6, "mapping_reductions",
  "תהיינה $A, B, C$ שפות.\n"
  r"**הערה:** הסימון $L_1 \not\le_m L_2$ מציין שלא קיימת רדוקציה מהשפה $L_1$ לשפה $L_2$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(r"אם $A \not\le_m B$ וגם $B \le_m C$ אז בהכרח מתקיים: $A \not\le_m C$",
       r"אם $A \not\le_m B$ וגם $B \le_m C$ אז יתכן שמתקיים: $A \le_m C$",
       r"אם $A \not\le_m B$ וגם $A \not\le_m C$ אז בהכרח מתקיים: $C \not\le_m B$",
       ALLFALSE),
  "b",
  r"**הפרכת א:** $A = 1\Sigma^*$, $B = \emptyset$, $C = 0\Sigma^*$." "\n"
  r"**הוכחת ב:** $A = A_{TM}$, $B = 1\Sigma^*$, $C = H_{TM}$." "\n"
  r"**הפרכת ג:** $A = A_{TM}$, $C = B = 1\Sigma^*$."),

Q(7, "np",
  "איזו מהטענות הבאות נכונה?",
  opts("המחלקה $NP$ סגורה תחת שרשור אבל לא סגורה תחת איחוד",
       "המחלקה $NP$ סגורה תחת איחוד אבל לא סגורה תחת שרשור",
       "המחלקה $NP$ סגורה תחת איחוד וגם סגורה תחת שרשור",
       ALLFALSE),
  "c",
  r"תהיינה $L_1, L_2$ שתי שפות השייכות ל-$NP$, ותהיינה $M_1, M_2$ מכונות א\"ד המכריעות אותן (בהתאמה) בזמן פולינומי." "\n"
  r"מכונה א\"ד $M$ המכריעה את $L_1 \cup L_2$ בזמן פולינומי פועלת כדלקמן: על קלט $x$:" "\n"
  r"1) $M$ מריצה את $M_1$ על $x$; אם חישוב זה עצר במצב מקבל, אז $M$ מקבלת את $x$" "\n"
  r"2) $M$ מריצה את $M_2$ על $x$; אם חישוב זה עצר במצב מקבל, אז $M$ מקבלת את $x$" "\n"
  r"3) אחרת, $M$ דוחה את $x$" "\n"
  "ברור שהמכונה שבנינו מכריעה את שפת האיחוד. נראה שהחישוב הוא פולינומי בגודל הקלט. "
  "**בכל אחד משלבים 1 ו-2 קיים מסלול באורך פולינומי (יחסית לגודל של $x$) המוביל למצב מקבל או דוחה.** "
  "האורך של מסלול החישוב של $M$ הוא סכום האורכים של כל אחד מהמסלולים שחושבו בשלבים 1-2, ולכן גם הוא פולינומי.\n"
  "כעת נראה שהמחלקה $NP$ סגורה לשרשור.\n"
  r"מכונה $N$ המכריעה את שפת השרשור $L_1 \cdot L_2$ פועלת כדלקמן: על קלט $w = \sigma_1\sigma_2\cdots\sigma_n$:" "\n"
  r"1) מפצלים באופן לא דטרמיניסטי את $w$ לרישא $\sigma_1\sigma_2\cdots\sigma_k$ ולסיפא $\sigma_{k+1}\sigma_{k+2}\cdots\sigma_n$" "\n"
  r"2) $N$ מריצה את $M_1$ על הרישא" "\n"
  r"3) אם חישוב זה עצר במצב מקבל, אז $N$ מריצה את $M_2$ על הסיפא;" "\n"
  r"4) אם גם חישוב זה עצר במצב מקבל, אז $N$ מקבלת את $w$" "\n"
  r"5) אחרת, $N$ דוחה את $w$" "\n"
  r"בדומה לניתוח הסיבוכיות של המכונה שמכריעה את שפת האיחוד, מגיעים למסקנה ש-$N$ מכריעה את $L_1 \cdot L_2$ בזמן פולינומי.",
  note="Source writes concatenation as 'L1.L2' and step 3 of N says 'אז M מריצה' — rendered as L_1 \\cdot L_2 and N."),

Q(8, "mapping_reductions",
  r"תהיינה $L_1, L_2$ שפות. נניח כי קיימת פונקציה ניתנת לחישוב $f: \Sigma^* \to \Sigma^*$ כך שלכל $x \in \Sigma^*$ מתקיים:" "\n"
  r"$$x \in L_1 \Leftrightarrow f(x) \notin L_2$$"
  r"**נתבונן בטענה הבאה:** אם מתקיים $L_2 \in RE$ אזי מתקיים $L_1 \in RE$",
  opts("הטענה נכונה", "הטענה לא נכונה"),
  "b",
  r"**הפרכה:** $x \in L_1 \Leftrightarrow f(x) \notin L_2 \Leftrightarrow f(x) \in \overline{L_2}$" "\n"
  r"כלומר, יש רדוקציה: $L_1 \le_m \overline{L_2}$ (ע\"פ הנתון הפונקציה ניתנת לחישוב)." "\n"
  r"ניקח $L_1 = \overline{H_{TM}}$" "\n"
  r"ניקח $L_2 = \overline{E_{TM}} \in RE$" "\n"
  r"אז מתקיים $\overline{L_2} = E_{TM}$" "\n"
  r"קיימת רדוקציה $\overline{H_{TM}} \le_m E_{TM}$ אבל $\overline{H_{TM}} \notin RE$"),

Q(9, "decidability",
  r"תהי $A$ שפה ניתנת להכרעה, כלומר $A \in R$." "\n"
  "נגדיר את השפות הבאות:\n"
  r"$$L_1 = \{\langle M\rangle \mid (*)\}$$"
  "(*): $M$ היא מכונת טיורינג **וגם** $L(M) = A$\n"
  r"$$L_2 = \{\langle M\rangle \mid (**)\}$$"
  "(**): $M$ היא מכונת טיורינג **וגם** $M$ מכריעה את $A$\n"
  "איזו מהטענות הבאות נכונה?",
  opts("השפה $L_1$ מוכלת ממש בשפה $L_2$",
       "השפה $L_2$ מוכלת ממש בשפה $L_1$",
       "השפה $L_1$ שווה לשפה $L_2$",
       ALLFALSE),
  "d",
  "השפה $L_1$ מכילה את כל קידודי המכונות **שמקבלות** את $A$\n"
  "השפה $L_2$ מכילה את כל קידודי המכונות **שמכריעות** את $A$\n"
  r"לכן תמיד מתקיים $L_2 \subseteq L_1$." "\n"
  r"כאשר $A \ne \Sigma^*$ זוהי הכלה ממש (כי יש מכונות מקבלות שאינן מכריעות), ולכן תשובה ב נכונה כמעט תמיד. "
  "תשובה זו התקבלה כנכונה במבחן.\n"
  r"אמנם, יש מקרה אחד, כאשר $A = \Sigma^*$, שעבורו מתקיים $L_1 = L_2$, ולכן מצד האמת, מכיוון שתשובה ב לא נכונה תמיד, "
  "קיבלנו גם את תשובה ד.",
  acceptedIds=["d", "b"],
  note="Corrected key highlights BOTH ב and ד. Per the key's own text, ד is the strictly correct answer "
       "(ב fails for A=Σ*) and ב was accepted in the exam — hence correctId=d, acceptedIds=[d,b] "
       "(the key's own text already states both were accepted)."),

Q(10, "time_p",
  r"נגדיר $f: \mathbb{N} \times \mathbb{N} \to \{0,1\}$ בצורה הבאה:" "\n"
  r"אם במספר הטבעי $k$ ובמספר הטבעי $n$ יש את אותה כמות אפסים אז $f(k,n) = 1$, אחרת $f(k,n) = 0$." "\n"
  r"לדוגמא, $f(1020408, 5000) = 1$ כי כל אחד מהמספרים מכיל 3 אפסים" "\n"
  r"$f(11, 2024) = 0$" "\n"
  r"**הנחה:** הא\"ב של הקלט הוא $\{\#, 0, 1, \ldots, 9\}$. שימו לב שע\"י הא\"ב של הקלט ניתן לקודד את הקלט $11, 2024$ באופן הבא: $11\#2024$" "\n"
  r"**הגדרה:** נאמר שפונקציה $f$ **ניתנת לחישוב בזמן פולינומיאלי** אם קיימת מכונת טיורינג דטרמיניסטית $F$ וקיים קבוע $c \ge 0$ "
  r"כך שעל כל קלט $x$ המכונה $F$ מסיימת את הריצה שלה תוך ביצוע של לכל היותר $|x|^c$ צעדי חישוב ועל הסרט שלה מופיע רק $f(x)$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts("הפונקציה $f$ ניתנת לחישוב בזמן פולינומיאלי",
       "הפונקציה $f$ ניתנת לחישוב אבל לא בזמן פולינומיאלי",
       "הפונקציה $f$ ניתנת לחישוב בזמן פולינומיאלי רק כאשר $n$ הוא קבוע",
       "הפונקציה $f$ ניתנת לחישוב בזמן פולינומיאלי רק כאשר $k$ הוא קבוע"),
  "a",
  "נשתמש במכונה דטרמיניסטית בעלת 3 סרטים.\n"
  "המכונה תכתוב תו המסמן את תחילת הסרט השני ואת תחילת הסרט השלישי.\n"
  "המכונה תסרוק את הקלט משמאל לימין עד לתו הרווח הראשון.\n"
  r"**שלב א:** המכונה תסרוק את הקלט משמאל לימין עד לתו המפריד בין המספר הראשון $k$ לשני $n$: ותעתיק את כל תווי האפס השייכים למספר $k$ לסרט השני" "\n"
  r"**שלב ב:** המכונה תמשיך לסרוק את הקלט משמאל לימין, החל מהתו המפריד בין המספר הראשון $k$ לשני $n$ עד לסימן הרווח: ותעתיק את כל תווי האפס השייכים במספר $n$ לסרט השלישי" "\n"
  "**שלב ג:** המכונה תשווה בין כמות האפסים בסרט השני והשלישי, אם הכמות שווה אז המכונה תמחק את תוכן הסרט ותכתוב 1 ותעצור. "
  "אחרת, המכונה תמחק את תוכן הסרט ותכתוב 0 ותעצור\n"
  "**המכונה הרב-סרטית מכריעה בזמן ליניארי (יש מספר קבוע של שלבים, וכל שלב מבצע בסיבוכיות ליניארית)** "
  "הראינו בהרצאה שמכונה דטרמיניסטית מרובת סרטים שקולה פולינומיאלית למכונה דטרמיניסטית בסיסית.",
  note="Solution box spans sol pp.9-10."),

Q(11, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle A, w\rangle \mid (*)\}$$"
  r"(*): $A$ הוא אס\"ד **וגם** $w \notin L(A)$",
  DEC4, "a",
  r"נבנה מכונה שתכריע את השפה באופן הבא: על קלט $\langle A, w\rangle$" "\n"
  r"1) בדוק האם הקידוד $A$ הוא אס\"ד" "\n"
  "2) אם הבדיקה בשלב 1 נכשלה, עצור ודחה\n"
  r"3) סמלץ את ריצת האס\"ד $A$ על המילה $w$," "\n"
  "4) אם הסימולציה בשלב 3 הסתיימה במצב דוחה של האס\"ד עצור ונקבל, אחרת דחה."),

Q(12, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid (*)\}$$"
  r"(*): $M$ היא מכונת טיורינג **וגם** קיימת מילה $w \in \Sigma^*$ כך שהחישוב של $M$ על $w$ עוצר במצב דוחה "
  r"ע\"י ביצוע של בדיוק $|Q|$ צעדי חישוב, כאשר $Q$ היא קבוצת המצבים של $M$." "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "a",
  r"**רעיון ההוכחה:** במהלך ביצוע של $|Q|$ צעדים, המכונה $M$ יכולה \"לבקר\" לכל היותר $|Q|$ התאים בקצה השמאלי של הסרט. "
  r"**לכן**, מספיק לבחון את $M$ רק על קלטים באורך עד $|Q|$" "\n"
  r"יש מספר סופי של מילים **באורך קטן או שווה** $|Q|$ מעל הא\"ב $\Sigma$, ולכן ניתן **להכריע** שייכות של הקלט $\langle M\rangle$ "
  r"לשפה $L$ ע\"י הרצת $M$ על כל מילה **באורך קטן או שווה** $|Q|$ למשך $|Q|$ צעדי חישוב. "
  r"אם קיימת סימולציה שעצרה במצב דוחה ע\"י ביצוע של בדיוק $|Q|$ צעדי חישוב אז נקבל, אחרת נדחה.",
  note="Proof box typo 'בלכל היותר' cleaned to 'לכל היותר'."),

Q(13, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M_1, M_2\rangle \mid (*)\}$$"
  r"(*): $\langle M_1\rangle \in L(M_2)$ וגם $\langle M_2\rangle \in L(M_1)$" "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "b",
  "**נראה שהשפה $L$ ניתנת לקבלה:**\n"
  r"נבנה מכונה שתקבל השפה באופן הבא, על קלט $\langle M_1, M_2\rangle$:" "\n"
  r"1) סמלץ את $M_2$ על $\langle M_1\rangle$, אם הסימולציה עצרה במצב דוחה, דחה" "\n"
  r"2) סמלץ את $M_1$ על $\langle M_2\rangle$, אם הסימולציה עצרה במצב דוחה, דחה" "\n"
  "3) קבל\n"
  r"**נראה את אי-כריעותה של $L$ ע\"י רדוקציה מבעיית $A_{TM}$:**" "\n"
  r"יהי $\langle M, w\rangle$ הקלט לבעיה $A_{TM}$." "\n"
  r"נגדיר $f(\langle M, w\rangle) = \langle K_{M,w}, K_{M,w}\rangle$" "\n"
  r"כאשר $K_{M,w}$ מוגדרת באופן הבא: \"על קלט $y$: התעלם מהקלט $y$, הרץ את $M$ על $w$ וענה כמוה\"" "\n"
  "זוהי פונקציה הניתנת לחישוב, ומתקיים גם:\n"
  r"• אם $\langle M, w\rangle \in A_{TM}$ אז $M$ מקבלת את $w$, אז המכונה $K_{M,w}$ מקבלת כל מילה, ולכן היא גם מקבלת את $K_{M,w}$, "
  r"לכן $\langle K_{M,w}, K_{M,w}\rangle \in L$." "\n"
  r"• אם $\langle M, w\rangle \notin A_{TM}$ אז $M$ לא מקבלת את $w$, אז המכונה $K_{M,w}$ לא מקבלת אף מילה, ולכן היא גם לא מקבלת את $K_{M,w}$, "
  r"לכן $\langle K_{M,w}, K_{M,w}\rangle \notin L$.",
  note="Printed stem: 'L = { <M1,M2> | <M1> ∈ L(M2) וגם <M2> ∈ L(M1) }' — condition moved to a (*) line to keep Hebrew out of math."),

Q(14, "np",
  "תהי שפה $L$ לא טריוויאלית. איזו מהטענות הבאות נכונה?",
  opts(r"אם מתקיים $L \in NP$ אז יתכן שהשפה $L$ לא ניתנת להכרעה.",
       r"אם מתקיים $L \in P$ אז יתכן שמתקיים $L \notin NP$.",
       r"אם מתקיים $L \in NP$ אז בהכרח מתקיים $L \le_m H_{TM}$.",
       ALLFALSE),
  "c",
  r"**הפרכת א:** כל שפה ב-$NP$ היא שפה ניתנת להכרעה" "\n"
  r"**הפרכת ב:** המחלקה $P$ מוכלת במחלקה $NP$" "\n"
  r"**הוכחת ג:** כל שפה ב-$NP$ היא שפה ניתנת להכרעה ולכן קיימת רדוקציה מהשפה $L$ לכל שפה לא-טריוויאלית, "
  r"בפרט יש רדוקציה מהשפה $L$ לבעיית העצירה"),
]

contexts = {
  "blk": {"kind": "text", "title": "בלוק של שאלות 15–18",
          "text": "נגדיר את השפה הבאה:\n"
                  r"$$L = \{\langle M\rangle \mid (*)\}$$"
                  r"(*): $M$ היא מכונת טיורינג **וגם** **לכל** מילה $w \in L(M)$ מתקיים שהחישוב של $M$ על $w$ עוצר במצב מקבל "
                  r"ע\"י ביצוע של לכל היותר $2^{|w|}$ צעדי חישוב." "\n"
                  "ונגדיר את השפה הבאה:\n"
                  r"$$L_\varepsilon = \{\langle M\rangle \mid \varepsilon \in L(M)\}$$"
                  "כעת נגדיר שתי פונקציות:\n"
                  r"$$f(\langle M\rangle) = \langle M_f\rangle$$"
                  r"$$g(\langle M\rangle) = \langle M_g\rangle$$"
                  "כאשר:\n"
                  r"$\langle M_f\rangle$ קידוד של מ\"ט אשר בהינתן קלט $x$:" "\n"
                  r"- $M_f$ מתעלמת מהקלט שלה. היא מריצה את $M$ על $\varepsilon$ למשך 2 צעדים. $M_f$ מקבלת אם ההרצה הנ\"ל של $M$ על $\varepsilon$ הסתיימה במצב מקבל. אחרת, $M_f$ דוחה." "\n"
                  r"$\langle M_g\rangle$ קידוד של מ\"ט אשר בהינתן קלט $x$:" "\n"
                  r"- אם $|x| > 0$ אז $M_g$ דוחה." "\n"
                  r"- אחרת, היא מריצה את $M$ על $\varepsilon$. אם $M$ על $\varepsilon$ עוצרת ומקבלת אזי $M_g$ מחכה 3 צעדים ואז מקבלת. אחרת, $M_g$ דוחה."},
}

questions += [
Q(15, "mapping_reductions", r"האם $f$ היא רדוקציה $L_\varepsilon \le_m L$?", TF, "b",
  "תזכורת. האורך של המילה הריקה הוא אפס.\n"
  r"אם $\langle M\rangle \in L_\varepsilon$ ונניח $M$ עוצרת על $\varepsilon$ במצב מקבל תוך בדיוק 2 צעדים. אזי $M_f$ על $\varepsilon$ עוצרת "
  r"תוך לפחות 3 צעדים. אבל $1 = 2^0 < 3$, לכן קיים קלט $w$ אותו $M_f$ מקבלת ביותר מ-$2^{|w|}$ צעדי חישוב, ולכן $\langle M_f\rangle \notin L$",
  contextId="blk"),
Q(16, "mapping_reductions", r"האם $f$ היא רדוקציה $\overline{L_\varepsilon} \le_m \overline{L}$?", TF, "b",
  r"הראינו בשאלה 15 שהפונקציה $f$ היא לא רדוקציה $L_\varepsilon \le_m L$" "\n"
  r"לכן, $f$ היא לא רדוקציה $\overline{L_\varepsilon} \le_m \overline{L}$",
  contextId="blk"),
Q(17, "mapping_reductions", r"האם $g$ היא רדוקציה $L_\varepsilon \le_m \overline{L}$?", TF, "a",
  r"הפונקציה $g$ ניתנת לחישוב (ניתן לחשב את הקידוד של המכונה $M_g$ בזמן סופי)." "\n"
  r"אם $\langle M\rangle \in L_\varepsilon$ אז $M$ על $\varepsilon$ עוצרת ומקבלת אזי $M_g$ על $\varepsilon$ מחכה 3 צעדים ולכן קיים קלט $w$ "
  r"אותו $M_g$ מקבלת ביותר מ-$2^{|w|}$ צעדי חישוב, ולכן $\langle M_g\rangle \in \overline{L}$" "\n"
  r"אם $\langle M\rangle \notin L_\varepsilon$ אז $M$ לא-מקבלת את $\varepsilon$ אזי $M_g$ דוחה או לא עוצרת על **כל** קלט. "
  r"לכן, לא קיים קלט $w$ אותו $M_g$ **מקבלת** ביותר מ-$2^{|w|}$ צעדי חישוב, כלומר, $\langle M_g\rangle \in L$ ולכן $\langle M_g\rangle \notin \overline{L}$",
  contextId="blk"),
Q(18, "mapping_reductions", r"האם $g$ היא רדוקציה $L_\varepsilon \le_m L$?", TF, "b",
  r"אם $\langle M\rangle \in L_\varepsilon$ אז $M$ על $\varepsilon$ עוצרת ומקבלת אזי $M_g$ על $\varepsilon$ מחכה 3 צעדים ולכן קיים קלט $w$ "
  r"אותו $M_g$ מקבלת ביותר מ-$2^{|w|}$ צעדי חישוב, ולכן $\langle M_g\rangle \notin L$",
  contextId="blk"),
]

for q in questions:
    if q["num"] >= 15:
        q["note"] = "Key for Q15-18 = red-coloured option text (no yellow highlight)."

exam = {
  "examCode": "24B-A",
  "examLabel": "2024 סמסטר ב מועד א",
  "year": 2024,
  "examDate": "8.7.2024",
  "sourceFile": "מבחנים/2024/סמסטר ב/מועד א פתרון מתוקן.pdf",
  "keyFile": "same file (corrected key: yellow highlights Q1-14, red text Q15-18, blue solution boxes)",
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
