# -*- coding: utf-8 -*-
"""Generator for tools/raw/23A-B.json. Transcribed by hand from the rendered pages of
`מבחנים/2023/סמסטר א/2023-03-05-Exam-חישוביות-2023-moedB-גרסא-0 SOLUTION.pdf`
(key = yellow highlight, explanations = the blue text under the options).
Run: PYTHONUTF8=1 py tools/gen/gen_23A-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23A-B.json"
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

NONE = "אף תשובה אחרת אינה נכונה"
NONE2 = "אף אחת מהתשובות האחרות אינה נכונה"
DEC4 = opts(
    "שפה $L$ ניתנת להכרעה",
    "שפה $L$ ניתנת לקבלה, אבל לא ניתנת להכרעה",
    "שפה $L$ לא ניתנת לקבלה, אבל המשלים שלה ניתן לקבלה",
    "שפה $L$ לא ניתנת לקבלה, וגם המשלים שלה לא ניתן לקבלה",
)

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "highlighted-pdf", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

questions = [
Q(1, "decidability",
  r"נתונות שפות $A, B, C$ כך שמתקיים $A \subseteq B \subseteq C$ וגם $A, C \in R$." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"בהכרח $B \in RE \setminus R$",
       r"בהכרח $B \notin R$",
       r"יתכן $B \notin RE \setminus R$ וגם $\overline{B} \notin RE \setminus R$",
       NONE),
  "c",
  r"נגדיר: $A = \emptyset$, $C = \Sigma^*$." "\n"
  r"**הפרכה של א' ושל ב':** $B = Prime$, שפה זו שייכת ל-$R$." "\n"
  r"**נכונות של ג':** $B = EQ_{TM}$."),

Q(2, "tm",
  r"נתון: $L \in RE \setminus R$." "\n"
  "אז לכל מכונת טיורינג אי-דטרמיניסטית $M$ המקבלת את $L$, ולכל מילה $w$ מתקיים:",
  opts("בהכרח קיים מסלול חישוב אינסופי של $M$ על $w$",
       "בהכרח כל מסלולי חישוב של $M$ על $w$ - סופיים",
       "אם $M$ מקבלת את $w$, אז כל מסלולי חישוב של $M$ על $w$ - סופיים",
       NONE),
  "d",
  "**הפרכת א:** למשל, אם $M$ דוחה את $w$, אז כל מסלולי חישוב של $M$ על $w$ - בהכרח סופיים ומסתיימים ב-$REJECT$.\n"
  "**הפרכת ב:** יתכן ש-$M$ לא מקבלת את $w$ כי כל מסלולי חישוב של $M$ על $w$ - אינסופיים.\n"
  "**הפרכת ג:** אם $M$ מקבלת את $w$, אז כמובן קיים מסלול חישוב סופי של $M$ על $w$ המסתיים ב-$ACCEPT$, "
  "ועדיין יכולים להתקיים מסלולי חישוב נוספים של $M$ על $w$ שהם אינסופיים."),

Q(3, "closure",
  r"נתונות שפות $A, B$ כך שמתקיים: $A \cap B \in R$ וגם $A \cup B \in R$." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"בהכרח $A \in R$ וגם $B \in R$",
       r"בהכרח $A \in RE$ וגם $B \in RE \setminus R$",
       r"בהכרח $A \notin RE \setminus R$ וגם $B \notin RE \setminus R$",
       NONE),
  "d",
  r"**דוגמה נגדית לתשובות א' ו-ב':** $A = H_{10}$, $B = \overline{H_{10}}$. מתקיים: $A \in RE \setminus R$, $B \notin RE$, "
  r"$A \cup B = \Sigma^*$, $A \cap B = \emptyset$." "\n"
  r"**דוגמה נגדית לתשובה ג':** $A = Path$, $B = \overline{Path}$; כאן שתי השפות שייכות ל-$R$. ושוב: "
  r"$A \cup B = \Sigma^*$, $A \cap B = \emptyset$.",
  note="Proof box labels the second counter-example only 'דוגמה נגדית' (placed under option ג); labelled here as refuting ג."),

Q(4, "tm",
  "נתונות שתי מכונות-טיורינג לא-דטרמיניסטיות $M_1$ ו-$M_2$.\n"
  "בונים מ\"ט $M$ עם האלגוריתם הבא:\n"
  "האלגוריתם של $M$ על קלט $w$:\n"
  "1. בחר באופן א\"ד האם לעבור לשלב 2 או לשלב 3.\n"
  "2. הרץ את $M_1$ על $w$ וענה כמותה\n"
  "3. הרץ את $M_2$ על $w$ וענה כמותה\n"
  "איזו מהטענות הבאות נכונה?",
  opts(r"בהכרח $L(M) \subset L(M_1) \cdot L(M_2)$",
       r"בהכרח $L(M) = L(M_1) \cdot L(M_2)$",
       r"בהכרח $L(M) \supset L(M_1) \cdot L(M_2)$",
       NONE),
  "d",
  r"עבור מכונה $M$ המתוארת בשאלה מתקיים: $L(M) = L(M_1) \cup L(M_2)$."),

Q(5, "npc",
  "מנסים להוכיח ש-$P = NP$.\nאיזו מהטענות הבאות נכונה:",
  opts(r"אם קיימת שפה $L \in NP$ כך ש-$L \le_p \overline{L}$, אז מתקיים $P = NP$",
       r"ידוע שהשפה $H_{TM}$ היא NP-קשה. לכן אם מתקיים $Primes \le_p H_{TM}$, אז $P = NP$",
       r"ידוע שהשפה $H_{TM}$ היא NP-קשה. לכן אם מתקיים $H_{TM} \le_p Primes$, אז $P = NP$",
       NONE),
  "d",
  r"**הפרכת א:** תהי $L$ שפה לא-טריוויאלית כלשהי השייכת ל-$P$ (ולכן גם ל-$NP$). במקרה זה, גם $\overline{L}$ היא שפה "
  r"לא-טריוויאלית, ולכן הרדוקציה $L \le_p \overline{L}$ מתקיימת – וזה בלי שום קשר לקיום או אי-קיום של השוויון $P = NP$." "\n"
  r"**הפרכת ב:** $Primes$ שייכת ל-$P$ והיא לא-טריוויאלית; גם $H_{TM}$ לא-טריוויאלית. ולכן, כמו במקרה של תשובה א': "
  r"הרדוקציה $Primes \le_p H_{TM}$ מתקיימת – בלי שום קשר לקיום או אי-קיום של השוויון $P = NP$." "\n"
  r"**הפרכת ג:** הטענה אינה נכונה: הרדוקציה $H_{TM} \le_p Primes$ לא מתקיימת (כי אחרת $H_{TM}$ הייתה שייכת ל-$P$, "
  r"בזמן שהיא אפילו לא ניתנת להכרעה), ולכן לא ניתן להסיק ש-$P = NP$.",
  note="Proof for ב literally repeats 'הרדוקציה L ≤p L̄' (copied from א); written as Primes ≤p H_TM."),

Q(6, "decidability",
  "רוצים להוכיח שהשפה $L$ **ניתנת לקבלה**. מה מהבאים יכול להוות הוכחה תקפה?",
  opts(r"קיים אנומרטור עבור שפה $A$ ומתקיים $L \le_m A$",
       r"קיימת מכונת טיורינג אי-דטרמיניסטית המקבלת את $\overline{L}$",
       r"גם $L$ וגם $\overline{L}$ הן שפות אינסופיות",
       NONE2),
  "a",
  r"**הוכחת א:** קיומו של אנומרטור עבור $A$ מבטיח ששפה זו ניתנת לקבלה. ואז לפי משפט רדוקציה, היחס $L \le_m A$ מבטיח שגם $L$ ניתנת לקבלה." "\n"
  r"**הפרכת ב:** זה רק מבטיח ש-$\overline{L}$ ניתנת לקבלה, אבל לא אומר שום דבר על השפה $L$ עצמה. למשל, ידוע ש-$\overline{E_{TM}}$ ניתנת לקבלה, אבל $E_{TM}$ לא ניתנת לקבלה." "\n"
  r"**הפרכת ג:** גם $E_{TM}$ וגם $\overline{E_{TM}}$ הן שפות אינסופיות, ועדיין $E_{TM}$ לא ניתנת לקבלה."),

Q(7, "enumerators",
  "נתונות שתי שפות:\n"
  r"$$A = \{L \mid (*)\}$$"
  "(*): קיים אנומרטור לקסיקוגרפי עבור $L$\n"
  r"$$B = \{L \mid (**)\}$$"
  r"(**): קיימת מכונת טיורינג $M$ המקבלת את $\overline{L}$" "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(("math", "A = B"), ("math", r"A \subset B"), ("math", r"A \supset B"), NONE),
  "b",
  r"$L$ שייכת ל-$A$ $\Leftarrow$ קיים עבורה אנומרטור לקסיקוגרפי $\Leftarrow$ $L$ ניתנת להכרעה $\Leftarrow$ גם $L$ וגם $\overline{L}$ ניתנות לקבלה "
  r"$\Leftarrow$ קיימת מכונת טיורינג $M$ המקבלת את $\overline{L}$ $\Leftarrow$ **$L$ שייכת ל-$B$**." "\n"
  r"כעת נגדיר $L = E_{TM}$ $\Leftarrow$ $\overline{L}$ ניתנת לקבלה $\Leftarrow$ קיימת מכונת טיורינג $M$ המקבלת את $\overline{L}$ $\Leftarrow$ **$L$ שייכת ל-$B$**. "
  r"**אבל:** $L$ לא ניתנת לקבלה $\Leftarrow$ $L$ לא ניתנת להכרעה $\Leftarrow$ לא קיים אנומרטור לקסיקוגרפי עבור $L$ $\Leftarrow$ **$L$ לא שייכת ל-$A$**." "\n"
  "**לסיכום:** התשובה הנכונה היא ב'.",
  note="Arrows in the key are drawn '←' in an RTL line (meaning 'implies', read right-to-left); rendered as \\Leftarrow to keep the printed visual direction."),

Q(8, "classification",
  "נתונה השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid (*)\}$$"
  "(*): $M$ עוצרת על כל הקלטים\n"
  "איזו מהטענות הבאות נכונה:",
  DEC4, "d",
  r"הוכחה מאוד דומה לזו עבור השפה $ALL_{TM}$ שמוצגת ב-Tirgul 8 באתר הקורס."),

Q(9, "classification",
  "נתונה השפה הבאה:\n"
  r"$$L = \{\langle M,k\rangle \mid (*)\}$$"
  "(*): קיימת מילה $w$ כך ש-$M$ לא עוצרת על $w$ תוך $k$ צעדים\n"
  "איזו מהטענות הבאות נכונה:",
  DEC4, "b",
  r"נסמן: $s_0, s_1, s_2, \ldots$ - סדרת כל המילים מעל הא\"ב הנתון, ממויינים לפי האורך, ובתוך קבוצת מילים באותו אורך – בסדר לקסיקוגרפי." "\n"
  r"**אלגוריתם $ALG$ המקבל את $L$** בהינתן $\langle M,k\rangle$:" "\n"
  "1. `i = 0`\n2. `run M(s_i) for k steps`\n3. `if not terminated then ALG stops and Accepts`\n4. `i = i + 1`\n5. `goto 2`\n"
  r"אם הזוג $\langle M,k\rangle$ לא שייך ל-$L$ (כלומר, הזוג שייך ל-$\overline{L}$), אז $ALG$ לא עוצר." "\n"
  r"**שימו לב:** משמעות השייכות של $\langle M,k\rangle$ ל-$\overline{L}$ היא שעל כל מילה $M$ עוצרת (מגיעה ל-$ACCEPT$ או $REJECT$) תוך $k$ צעדים. "
  "**אינטואיטיבית** ברור, שלא ניתן לוודא את קיומה של התכונה הזאת בזמן סופי, כי זה דורש אינסוף בדיקות (של $M$ על אינסוף מילים) – "
  r"ולכן השפה $\overline{L}$ לא ניתנת לקבלה, וכתוצאה, $L$ לא ניתנת להכרעה. כדי **להוכיח את זה פורמלית**, יש להגדיר רדוקציה ל-$L$ "
  r"משפה שידועה כלא ניתנת להכרעה (למשל מ-$H_{TM}$). לא נציג כאן רדוקציה כזאת.",
  confidence="med",
  note="Key (yellow) = ב, transcribed as-is. Doubt: in k steps M reads at most its first k input cells, so only words of length ≤ k need checking — "
       "which suggests L is actually decidable (א). The key's own 'proof' is only intuitive and says no reduction is given. ASK_ADIR."),

Q(10, "mapping_reductions",
  r"נתונות שלוש שפות לא טריוויאליות (כל אחת שונה מ-$\Sigma^*$ ומ-$\emptyset$). כמו כן נתון:" "\n"
  r"$$\overline{L_2} \le_m \overline{L_1} \;;\; L_3 \in RE \setminus R \;;\; L_1 \in R$$"
  "איזו מהטענות הבאות נכונה:",
  opts(r"$L_2 \in RE \setminus R$",
       r"מתקיימת רדוקציה: $\overline{L_3} \le_m L_1$",
       r"מתקיימת רדוקציה: $L_2 \le_m \overline{L_3}$",
       NONE2),
  "c",
  r"**הפרכה של א':** נתון ש-$L_1 \in R$, ולכן גם $\overline{L_1} \in R$. אז מהרדוקציה $\overline{L_2} \le_m \overline{L_1}$ נובע ש-$\overline{L_2} \in R$, ולכן גם $L_2 \in R$." "\n"
  r"**הפרכה של ב':** נניח שהרדוקציה $\overline{L_3} \le_m L_1$ אכן מתקיימת. אז מ-$L_1 \in R$ (נתון בשאלה) נובע ש-$\overline{L_3} \in R$ ולכן גם $L_3 \in R$ "
  r"- וזה בסתירה לכך שלפי הנתון מתקיים $L_3 \in RE \setminus R$." "\n"
  r"**נכונות של ג':** כפי כבר צוין, $L_2 \in R$. ולכן מתקיימת רדוקציה מ-$L_2$ לכל שפה לא-טריוויאלית אחרת, ובפרט ל-$\overline{L_3}$."),

Q(11, "mapping_reductions",
  "נגדיר את הפונקציה הבאה:\n"
  r"$f(\langle M,w\rangle) = 0$ אם $M$ עוצרת על $w$ אחרי מספר **אי זוגי** של צעדים" "\n"
  r"$f(\langle M,w\rangle) = 00$ אם $M$ **לא עוצרת** על $w$" "\n"
  r"$f(\langle M,w\rangle) = 1$ אם $M$ עוצרת על $w$ אחרי מספר **זוגי** של צעדים" "\n"
  "עבור איזו מהשפות הבאות מתקיים:\n"
  r"$$\langle M,w\rangle \notin H_{TM} \leftrightarrow f(\langle M,w\rangle) \notin L$$",
  opts(("math", r"\{0\}"), ("math", r"\{11, 1, 0\}"), ("math", r"\{00, 1, 0\}"), ("math", r"\{11, 1\}")),
  "b",
  r"**הפרכת א:** אם $M$ עוצרת על $w$ אחרי מספר זוגי של צעדים (כלומר, $\langle M,w\rangle \in H_{TM}$), אז $f(\langle M,w\rangle) = 1$. ערך זה חייב להיות בשפה, אבל הוא לא שייך לה." "\n"
  r"**הוכחת ב:** קל לבדוק שבכל אחד משלושה המקרים המוזכרים בהגדרה של הפונקציה, מתקיים $\langle M,w\rangle \notin H_{TM} \leftrightarrow f(\langle M,w\rangle) \notin L$ כאשר $L = \{11, 1, 0\}$." "\n"
  r"**הפרכת ג:** אם $M$ לא עוצרת על $w$ (כלומר, $\langle M,w\rangle \notin H_{TM}$), אז $f(\langle M,w\rangle) = 00$. ערך זה חייב להיות מחוץ לשפה, אבל הוא שייך לה." "\n"
  r"**הפרכת ד:** אם $M$ עוצרת על $w$ אחרי מספר אי-זוגי של צעדים (כלומר, $\langle M,w\rangle \in H_{TM}$), אז $f(\langle M,w\rangle) = 0$. ערך זה חייב להיות בשפה, אבל הוא לא שייך לה.",
  note="The function is printed as a piecewise-brace image; typed as three lines. Proof for ג literally says 'אם M עוצרת על w' — "
       "missing 'לא' (it continues '<M,w> ∉ H_TM', f=00); fixed."),

Q(12, "mapping_reductions",
  r"נתון שמתקיים $A \le_m B$, כאשר כל אחת מהשפות $A, B$ היא לא טריוויאלית." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"אם $B \in RE \cap coRE$ אז $A \in RE \cap coRE$.",
       r"אם $B$ שפה רגולרית אז $A$ שפה רגולרית.",
       r"אם $B \notin R$ אז $A \notin R$.",
       "אף טענה אחרת אינה נכונה"),
  "a",
  r"**נכונות סעיף א':** מתקיים $R = RE \cap coRE$ ולכן ע\"פ משפט רדוקצית המיפוי אם $B \in R$ אז $A \in R$." "\n"
  r"**הפרכת סעיף ב':** ניקח את השפה הרגולרית $B = \{1\}$, ואת השפה הלא רגולרית $A = \{0^n1^n \mid n \ge 0\}$ ונגדיר את הרדוקציה:" "\n"
  r"$$f(w) = \begin{cases} 1 & \text{if } w \in A \\ 0 & \text{if } w \notin A \end{cases}$$"
  r"ניתן לחשב את הפונקציה $f$ כיוון שמתקיים $A \in R$." "\n"
  "**הפרכת סעיף ג':** מכל שפה לא טריוויאלית הניתנת להכרעה קיימת רדוקציה **לכל** שפה לא טריוויאלית אחרת (כולל שפה שאינה ניתנת להכרעה).",
  note="In the proof box the '{1}' of B is displaced to the next line by bidi; reassembled as B = {1}."),

Q(13, "poly_reductions",
  "נתונה השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid (*)\}$$"
  "(*): המכונה $M$ מקבלת את כל הפלינדרומים באורך זוגי\n"
  "נגדיר פונקציה:\n"
  r"$$f(\langle M,w\rangle) = Q(x)$$"
  "כאשר המכונה $Q(x)$ מוגדרת כדלקמן:\n"
  "`Q(x) {`\n"
  "`  if (x is an even-length palindrome)`\n"
  "`  then { M(w); ACCEPT }`\n"
  "`  else REJECT`\n"
  "`}`\n"
  r"לבסוף, נזכיר שהשפה $H_{TM}$ היא שפה NP-קשה." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts("פונקציה $f$ לא ניתנת לחישוב",
       r"פונקציה $f$ היא רדוקצית מיפוי $H_{TM} \le_m L$, ולכן ניתן להסיק שהשפה $L$ שייכת למחלקה $RE$",
       r"פונקציה $f$ היא רדוקציה פולינומית $H_{TM} \le_p L$, ולכן ניתן להסיק שהשפה $L$ היא שפה NP-קשה",
       NONE2),
  "c",
  r"הפונקציה $f$ כן ניתנת לחישוב: בהינתן קידוד של מכונה $M$ ומילה $w$, ניתן לקודד את המכונה $Q$ הפועלת לפי ההגדרה הנ\"ל. "
  r"בפרט נזכיר שניתן לקודד את הבדיקה האם מילה $x$ מהווה פלינדרום באורך זוגי." "\n"
  r"יותר מזה, ברור שזמן הנדרש כדי לקודד את $Q$ הינו פולינומי יחסית לגודל של $\langle M,w\rangle$." "\n"
  r"הפונקציה $f$ מהווה רדוקציה $H_{TM} \le_m L$." "\n"
  r"בנוסף, בהתאם לסיבוכיות החישוב שלה היא מהווה גם רדוקציה פולינומית $H_{TM} \le_p L$. נבדוק שמתקיים: $\langle M,w\rangle \in H_{TM} \Leftrightarrow Q \in L$." "\n"
  r"נניח ש-$\langle M,w\rangle \in H_{TM}$, כלומר $M$ עוצרת על הקלט $w$. אז $Q$ מקבלת את כל הפלינדרומים באורך זוגי ורק אותם. בהתאם, במקרה זה מתקיים $Q \in L$." "\n"
  r"כעת נניח ש-$\langle M,w\rangle \notin H_{TM}$ כלומר $M$ **לא** עוצרת על הקלט $w$. במקרה זה, $Q$ לא מקבלת אף קלט "
  r"(לא עוצרת כאשר הקלט הוא פלינדרום באורך זוגי, ועוצרת במצב $REJECT$ עבור כל שאר הקלטים). בהתאם, $Q \notin L$." "\n"
  r"נציין גם שקיומה של רדוקציה $H_{TM} \le_m L$ (בלי קשר האם היא פולינומית או לא) **אינו מבטיח** ש-$L$ שייכת ל-$RE$; "
  r"משמעות הרדוקציה היא שדרגת הקושי של $L$ היא **לפחות** כמו דרגת קושי של $H_{TM}$." "\n"
  r"**לסיכום:** מתקיימת רדוקציה פולינומית $H_{TM} \le_p L$. ידוע שהשפה $H_{TM}$ היא NP-קשה, כלומר עבור כל שפה $A$ מ-$NP$ מתקיים $A \le_p H_{TM}$. "
  r"אבל אז לפי טרנזיטיביות של היחס $\le_p$ מתקיים גם $A \le_p L$ עבור כל $A$ מ-$NP$, ולכן $L$ היא שפה NP-קשה.",
  note="Q(x) code box prints the condition in Hebrew 'if (x הוא פלינדרום באורך זוגי)'; rendered in English inside the code lines "
       "to keep code LTR. Key writes H_tm in the proof; normalized to H_{TM}."),

Q(14, "npc",
  "נתון שהשפה $A$ היא שפה NP-**שלמה** ואילו השפה $B$ היא NP-**קשה**.\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"בהכרח מתקיים $A \le_p B$", r"בהכרח מתקיים $B \le_p A$", r"בהכרח מתקיים $B \in R$", NONE2),
  "a",
  r"**נכונות א:** נתון $A$ היא שפה NP-שלמה, אז היא שייכת ל-$NP$. נתון ש-$B$ היא NP-קשה, אז עבור כל שפה $L$ מ-$NP$ מתקיימת הרדוקציה $L \le_p B$. בפרט, היא מתקיימת עבור $A$." "\n"
  r"**הפרכת ב:** נתון ש-$A$ היא NP-שלמה; וזה אומר שבפרט היא שייכת ל-$R$. אם מתקיים $B \le_p A$ אז לפי משפט הרדוקציה גם $B$ בהכרח שייכת ל-$R$. "
  r"אבל לא כל שפה NP-קשה שייכת ל-$R$; למשל ידוע שהשפה $H_{TM}$ היא NP-קשה, אבל היא לא שייכת ל-$R$." "\n"
  r"**הפרכת ג:** השפה $H_{TM}$ היא NP-קשה, אבל היא לא שייכת ל-$R$."),

Q(15, "npc",
  r"תהי $A$ שפה כך שמתקיים $CLIQUE \le_P A$." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts("בהכרח $A$ היא שפה הניתנת להכרעה",
       "בהכרח $A$ היא שפה NP-שלמה",
       "בהכרח $A$ היא שפה NP-קשה",
       NONE2),
  "c",
  r"**הפרכת א:** אם מתקיים $CLIQUE \le_P A$, אז מתקיים גם $CLIQUE \le_m A$. היות ו-$CLIQUE$ היא שפה לא-טריוויאלית הניתנת להכרעה, "
  r"קיימת רדוקצית מיפוי ממנה **לכל** שפה לא-טריוויאלית, כך ש-$A$ לא חייבת להיות ניתנת להכרעה. למשל, מתקיים: $CLIQUE \le_P H_{TM}$." "\n"
  "**הפרכת ב:** היות ו-$A$ לא בהכרח ניתנת להכרעה, אז היא גם לא בהכרח NP-שלמה.\n"
  r"**הוכחת ג:** ידוע ש-$CLIQUE$ היא שפה NP-שלמה, ולכן עבור כל שפה $L$ ב-$NP$ מתקיים: $L \le_P CLIQUE$. "
  r"מכאן נובע (לפי טרנזיטיביות של היחס $\le_P$) שעבור כל שפה $L$ ב-$NP$ מתקיים: $L \le_P A$, ולכן $A$ היא שפה NP-קשה." "\n"
  r"**שימו לב:** לא נדרש ש-$A$ עצמה שייכת ל-$NP$. לכן המסקנה היא ש-$A$ בוודאות NP-קשה, אבל לא ניתן להסיק ש-$A$ היא NP-שלמה."),

Q(16, "decidability",
  "נתונה שפה הבאה:\n"
  r"$$L = \{\langle A,w\rangle \mid (*)\}$$"
  "(*): אס\"ד $A$ מקבל את המילה $w$ וקיימת מכונת טיורינג $M$ שגם היא מקבלת את $w$\n"
  "איזו מהטענות הבאות נכונה:",
  opts("$L$ ניתנת להכרעה",
       r"$L$ ניתנת לקבלה, אבל $\overline{L}$ לא ניתנת לקבלה",
       r"$L$ לא ניתנת לקבלה, אבל $\overline{L}$ ניתנת לקבלה",
       r"$L$ לא ניתנת לקבלה, וגם $\overline{L}$ לא ניתנת לקבלה"),
  "a",
  r"נגדיר $M$ כמכונה שמקבלת את כל הקלטים. אז למעשה $L$ היא שפת $A_{DFA}$, שהיא ניתנת להכרעה."),

Q(17, "poly_reductions",
  "נתונה השפה:\n"
  r"$$L = \{\langle \varphi, w\rangle \mid (*)\}$$"
  "(*): $\\varphi$ היא נוסחה בוליאנית השייכת לשפה $2SAT$ וגם המחרוזת $w$ מתחילה ב-0\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"מתקיימת הרדוקציה $H_{10} \le_p L$.",
       r"מתקיימת הרדוקציה $L \le_p H_{10}$.",
       ("math", r"L \in RE \setminus R"),
       NONE2),
  "b",
  r"גם השפה $2SAT$ וגם שפת המחרוזות המתחילות ב-0 הן שפות השייכות ל-$P$. לכן גם השפה $L$ שבשאלה שייכת ל-$P$, ובפרט ל-$R$. **וזה מפריך את התשובה ג'.**" "\n"
  r"**הפרכה של א':** לו הרדוקציה $H_{10} \le_p L$ הייתה מתקיימת, אז משייכות של השפה $L$ ל-$R$ היה נובע שגם $H_{10}$ שייכת ל-$R$ – וזה לא נכון." "\n"
  r"**נכונות של ב':** כבר הוכחנו שהשפה הלא-טריוויאלית $L$ שייכת ל-$P$; לכן קיימת רדוקציה פולינומית ממנה לכל שפה לא-טריוויאלית, ובפרט ל-$H_{10}$."),

Q(18, "poly_reductions",
  "נגדיר את שתי המחלקות הבאות (בשתי ההגדרות, $L$ היא שפה לא טריוויאלית):\n"
  r"$$A = \{L \mid CLIQUE \le_P L \text{ and } L \in NP\}$$"
  r"$$B = \{L \mid PATH \le_p L\}$$"
  "איזו מהטענות הבאות נכונה:",
  opts(("math", r"A \supset B"), ("math", r"A \subset B"),
       r"$A = B$ רק בתנאי שמתקיים $P = NP$", NONE),
  "b",
  "**המחלקה $A$ מכילה רק שפות NP-שלמות** "
  r"(לפי המשפט: אם $L \in NP$ ומתקיימת רדוקציה $Q \le_P L$ כאשר $Q$ היא שפה NP-שלמה, אז גם $L$ היא NP-שלמה)." "\n"
  "**לעומת זאת, $B$ מכילה את כל השפות הלא טריוויאליות** "
  "(לפי המשפט: אם $Q$ שייכת ל-$P$, אז קיימת ממנה רדוקצית פולינומית לכל שפה לא טריוויאלית אחרת).\n"
  "ולכן תשובה ב' היא הנכונה.",
  note="Definition of A prints 'וגם' between the conditions; written as \\text{and} to keep Hebrew out of math."),

Q(19, "npc",
  "אופרציית **xor** על שפות $A$ ו-$B$ מוגדרת כדלקמן:\n"
  r"$$A \text{ xor } B = (A \cup B) \setminus (A \cap B)$$"
  "נתון ש-$A$ היא שפה NP-שלמה, ו-$B$ שייכת ל-$NP$.\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"יתכן ש: $A \text{ xor } B$ היא שפה NP-שלמה",
       r"לא יתכן שהשפה $A \text{ xor } B$ שייכת ל-$P$",
       r"לא יתכן ש: $A \text{ xor } B$ היא שפה סופית",
       NONE),
  "a",
  r"**הוכחת א:** למשל: $A = SAT$, $B = \emptyset$; אז $A \text{ xor } B = SAT$." "\n"
  r"**הפרכה של ב' ו-ג':** נגדיר $A = B = SAT$, אז $A \text{ xor } B = \emptyset$."),

Q(20, "undecidability",
  r"נגדיר את הפונקציה $T(\langle M,w\rangle)$ באופן הבא:" "\n"
  r"- אם מכונה $M$ עוצרת על קלט $w$ אחרי **בדיוק** $k$ צעדים, אז: $T(\langle M,w\rangle) = k$" "\n"
  r"- אם מכונה $M$ לא עוצרת על קלט $w$, אז: $T(\langle M,w\rangle) = -|w|$." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"לא קיימת מכונת טיורינג בסיסית שמחשבת את הפונקציה $T(\langle M,w\rangle)$",
       r"קיימת מכונת טיורינג אי-דטרמיניסטית שמחשבת את הפונקציה $T(\langle M,w\rangle)$",
       r"קיימת מכונת טיורינג עם שני סרטים שמחשבת את הפונקציה $T(\langle M,w\rangle)$ בזמן אקספוננציאלי",
       NONE),
  "a",
  "פונקציה $T$ לא ניתנת לחישוב, ולכן התשובה הראשונה היא הנכונה.\n"
  r"אם פונקציה כלשהי ניתנת לחישוב, אז חישוב שלה על כל קלט חייב להסתיים. לו $T$ היה ניתנת לחישוב, אז ניתן היה להכריע את בעיית עצירה $H_{TM}$: "
  r"אם ערך של הפונקציה חיובי, אז $M$ עוצרת על $w$, ואם ערך שלילי – אז $M$ לא עוצרת על $w$. אבל $H_{TM}$ לא ניתנת להכרעה, ולכן $T$ לא ניתנת לחישוב.",
  note="'בדיוק' is underlined in the source; rendered bold."),

Q(21, "mapping_reductions",
  "נתונות שתי שפות:\n"
  r"$$Always\_Halt = \{\langle M\rangle \mid (*)\}$$"
  "(*): $M$ עוצרת על כל קלט\n"
  r"$$Never\_Halt = \{\langle M\rangle \mid (**)\}$$"
  "(**): $M$ לא עוצרת על אף קלט\n"
  "נגדיר את הפונקציה הבאה:\n"
  r"$$f(\langle M\rangle) = \langle Q_M\rangle$$"
  "כאשר $Q_M$ היא המכונה הבאה:\n"
  "$Q_M$ על קלט $y$:\n"
  "1. הרץ את $M$ על כל הקלטים שאורכם לכל היותר $|y|$ למשך $|y|$ צעדים.\n"
  "2. אם בשלב 1 היה קלט ש-$M$ עצרה עליו בתוך $|y|$ צעדים: עצור וקבל.\n"
  "3. הכנס ללולאה אינסופית.\n"
  "איזו מהטענות הבאות נכונה:",
  opts(("math", r"\langle M\rangle \in Never\_Halt \Longrightarrow \langle Q_M\rangle \in Always\_Halt"),
       ("math", r"\langle M\rangle \in Always\_Halt \Longrightarrow \langle Q_M\rangle \in Never\_Halt"),
       ("math", r"\langle M\rangle \in \overline{Always\_Halt} \Longrightarrow \langle Q_M\rangle \in \overline{Never\_Halt}"),
       NONE),
  "d",
  r"(להלן $AH$ = $Always\_Halt$, $NH$ = $Never\_Halt$.)" "\n"
  r"**הפרכת א:** אם $\langle M\rangle \in NH$ אז $M$ לא עוצרת על אף קלט. לכן התנאי בשורה 2 אף פעם לא מתקיים ו-$Q_M$ על כל הקלטים נכנסת ללולאה "
  r"ובוודאי שלא מתקיים $\langle Q_M\rangle \in AH$ (במקרה הזה אפילו $\langle Q_M\rangle \in NH$)." "\n"
  r"**הפרכת ב:** אם $\langle M\rangle \in AH$ אז $M$ עוצרת לכל קלט. בפרט, יש קלט באורך $k$ שעליו $M$ עוצרת בתוך $t$ צעדים. "
  r"לכל $y$ ארוך יותר מ-$k$ ו-$t$, המכונה $Q_M$ תעצור ותקבל. לכן $\langle Q_M\rangle \notin NH$." "\n"
  r"**הפרכת ג:** אם $\langle M\rangle \notin AH$, יש מקרים שבהם $\langle Q_M\rangle \in \overline{NH}$ ויש מקרים שבהם $\langle Q_M\rangle \notin \overline{NH}$. "
  r"אם יש קלט ש-$M$ עוצרת עליו, נניח שהאורך שלו $k$ ונניח כי $M$ עוצרת בתוך $t$ צעדים. לכל $y$ ארוך יותר מ-$k$ ו-$t$, המכונה $Q_M$ תעצור ותקבל. "
  r"לכן $\langle Q_M\rangle \notin NH$. אם אין אף קלט ש-$M$ עוצרת עליו, אז $Q_M$ לא תעצור על אף $y$ ואז $\langle Q_M\rangle \in NH$.",
  note="Languages printed as '{ M עוצרת על כל קלט }' (no ⟨⟩ or bar); written in (*) form. The key's proof for ג says '⟨Q_M⟩ ∉ NH' where the "
       "case analysis concludes; transcribed as printed. Abbreviations AH/NH are used in the key without definition — added a gloss line."),

Q(22, "npc",
  "תהי $L$ שפה NP-שלמה.\nאיזו מהטענות הבאות נכונה:",
  opts(r"אם קיים אנומרטור $E_L$ של $L$ כך ש-$E_L$ מדפיס כל $x \in L$ לאחר מספר פולינומי (יחסית ל-$|x|$) של צעדים, אז בהכרח $P = NP$.",
       r"מתקיים $H_{TM} \le_p L$",
       r"לא מתקיים $L \le_p H_{TM}$",
       NONE),
  "d",
  r"**הפרכת א:** לא בהכרח. אם $x \in L$, אז אכן ניתן לוודא את זה בזמן פולינומי (יחסית ל-$|x|$), על ידי הפעלה של $E_L$ והמתנה לרגע ש-$x$ יודפס. "
  r"אבל אם $x \notin L$, אז השימוש ב-$E_L$ לא מבטיח שניתן לגלות את זה בזמן פולינומי. גם אם $E_L$ הוא אנומרטור לקסיקוגרפי (קיומו מובטח, כי $L$ ניתנת להכרעה), "
  r"ניתן להסיק ש-$x \notin L$ רק אחרי ש-$E_L$ ידפיס את כל המילים ב-$L$ שהן לא יותר ארוכות מ-$|x|$ - וכמות מילים כאלה יכולה להיות אקספוננציאלית." "\n"
  r"**הפרכת ב:** לו הרדוקציה $H_{TM} \le_p L$ הייתה מתקיימת, אז משייכות של השפה $L$ ל-$R$ (זה נובע מכך ש-$L$ היא NP-שלמה) היה נובע שגם $H_{TM}$ שייכת ל-$R$ – וזה לא נכון." "\n"
  r"**הפרכת ג:** $L$ היא שפה NP-שלמה $\Leftarrow$ $L \in NP$ $\Leftarrow$ הרדוקציה $L \le_p H_{TM}$ מתקיימת, כי $H_{TM}$ היא שפה NP-קשה.",
  note="Arrows printed '←' in an RTL line (= implies); kept as \\Leftarrow."),

Q(23, "poly_reductions",
  r"תהי $L$ שפה כך שהרדוקציה $A \le_p L$ מתקיימת עבור כל שפה לא-טריוויאלית $A$ מ-$P$." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts("$L$ בהכרח NP-קשה", r"יתכן ש-$L \in NP$", r"בהכרח מתקיים $4SAT \le_p L$", NONE),
  "b",
  "**הפרכת א:** לא נכון. רדוקציה משפה לא-טריוויאלית ב-$P$ קיימת לכל שפה לא-טריוויאלית אחרת. "
  "לא מובטח שרדוקציה ל-$L$ קיימת עבור כל שפה ב-$NP$ (זה נדרש בכדי ש-$L$ תהיה NP-קשה).\n"
  "**הוכחת ב:** זה נכון, כי שוב - רדוקציה משפה לא-טריוויאלית ב-$P$ קיימת לכל שפה לא-טריוויאלית אחרת, בפרט לשפה ששייכת ל-$NP$.\n"
  "**הפרכת ג:** לא. למשל אם $L$ ב-$P$, אז הרדוקציה מתקיימת רק אם $P = NP$.",
  note="Proof for א reads 'זה מגרש' — typo for 'זה נדרש'; fixed."),

Q(24, "poly_reductions",
  "נתונה שפה:\n"
  r"$$CLIS = \{\langle G, k, t\rangle \mid (*)\}$$"
  "(*): $G$ גרף לא מכוון, יש ב-$G$ קליקה בגודל $k$ וגם קבוצה בלתי תלויה בגודל $t$\n"
  r"רוצים להראות שמתקיים $CLIQUE \le_P CLIS$ ולשם כך מגדירים פונקציה $f$:" "\n"
  r"$$f(\langle G,k\rangle) = \langle G, k, n-k\rangle$$"
  "כאשר $n$ הוא מספר הקדקדים ב-$G$.\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"מתקיים $f(\langle G,k\rangle) \in CLIS \Longleftarrow \langle G,k\rangle \in CLIQUE$",
       r"מתקיים $f(\langle G,k\rangle) \notin CLIS \Longleftarrow \langle G,k\rangle \notin CLIQUE$",
       r"מתקיים $f(\langle G,k\rangle) \notin CLIS \Longrightarrow \langle G,k\rangle \in CLIQUE$",
       NONE),
  "b",
  r"**הפרכת א:** אם $\langle G,k\rangle \in CLIQUE$ לא ניתן לדעת האם יש ב-$G$ קבוצה בלתי תלויה בגודל $n-k$." "\n"
  r"**הוכחת ב:** אם $\langle G,k\rangle \notin CLIQUE$ אז ב-$G$ אין קליקה בגודל $k$ ולכן $f(\langle G,k\rangle) \notin CLIS$ (ללא קשר לשאלה האם יש ב-$G$ קבוצה ב\"ת בגודל כלשהו)." "\n"
  r"**הפרכת ג:** זה לא תמיד נכון. למשל, אם $f(\langle G,k\rangle) \notin CLIS$ מהסיבה שבגרף $G$ לא קיימת קליקה בגודל $k$, אז ברור ש-$\langle G,k\rangle \notin CLIQUE$.",
  note="Options transcribed in printed visual (left-to-right) order: e.g. א reads 'f(<G,k>) ∈ CLIS ⟸ <G,k> ∈ CLIQUE', i.e. CLIQUE-membership implies CLIS-membership."),

Q(25, "npc",
  r"נתונות שתי שפות $A, B$ כך שמתקיימת הרדוקציה $A \le_P B$." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"בהכרח אם $A \in NPC$ אז $B \in NPC$",
       r"בהכרח אם $B \in NPC$ אז $A \in NPC$",
       r"בהכרח $A \setminus B \in NPC$",
       NONE),
  "d",
  r"**הפרכת א:** לא בהכרח. בכדי שיתקיים $B \in NPC$, חייב להיות $B \in NP$ - וזה לא מובטח." "\n"
  r"**הפרכת ב:** לא בהכרח. אם $B \in NPC$, אז הרדוקציה $A \le_P B$ מתקיימת עבור כל שפה $A$ ב-$NP$, גם אם היא לא NP-שלמה." "\n"
  r"**הפרכת ג:** לא נכון. למשל, אם $A = B$, אז הרדוקציה $A \le_P B$ כמובן מתקיימת, אבל $A \setminus B = \emptyset$, ושפה ריקה איננה NP-שלמה."),
]

# Held out of the bank (ASK_ADIR): official key disputed on the math.
HOLD = {9: "official key (ב) disputed: within k steps M reads only its first ~k input cells, "
           "so checking all words of length <= k+1 decides L -> looks like א. ASK_ADIR"}
for q in questions:
    if q["num"] in HOLD:
        q["hold"] = HOLD[q["num"]]

exam = {
  "examCode": "23A-B",
  "examLabel": "2023 סמסטר א מועד ב",
  "year": 2023,
  "examDate": "5.3.2023",
  "sourceFile": "מבחנים/2023/סמסטר א/2023-03-05-Exam-חישוביות-2023-moedB-גרסא-0 SOLUTION.pdf",
  "keyFile": "same file (yellow highlights + blue explanations)",
  "contexts": {},
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 26))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
