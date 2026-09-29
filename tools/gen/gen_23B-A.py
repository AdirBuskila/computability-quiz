# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-A.json. Transcribed by hand from the rendered pages of
`מבחנים/2023/סמסטר א/2023-06-12-Exam-חישוביות-2023-moedA-גרסא-0 SOLUTION.pdf`
(key = yellow-highlighted option, explanations = the yellow "הסבר" paragraphs).
Filed under סמסטר א and the cover says "סמסטר א' תשפ"ג, מועד א'" (no date, lecturer Dr. Radel Ben-Av),
but the file date is 12.6.2023 and it is a different exam from the 9.2.2023 מועד א' -> treated as 23B-A.
Run: PYTHONUTF8=1 py tools/gen/gen_23B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-A.json"
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

# True/False and yes/no questions: the printed order varies per question.
TF = opts("נכון", "לא נכון")
FT = opts("לא נכון", "נכון")
YN = opts("כן", "לא")
NY = opts("לא", "כן")

R_ = "השפה $L$ ניתנת להכרעה"
RE_ = "השפה $L$ לא ניתנת להכרעה אך ניתנת לקבלה"
CO_ = r"השפה $L$ לא ניתנת לקבלה אך $\overline{L}$ ניתנת לקבלה"
NEI_ = r"גם $L$ וגם $\overline{L}$ לא ניתנות לקבלה"
NONE = "אף תשובה אינה נכונה"

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "highlighted-pdf", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

TF_INTRO = "קבע האם הטענה הבאה נכונה או לא:\n"

contexts = {
  "rel": {"kind": "text", "title": "הגדרות לשאלות 10–12",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  r"$$A = \{\langle M\rangle \mid L(M) \subseteq VC\}$$"
                  r"$$B = \{\langle M\rangle \mid L(M) \subseteq IS\}$$"
                  r"$$C = \{\langle M\rangle \mid L(M) \notin RE\}$$"},
  "map": {"kind": "text", "title": "הגדרות לשאלות 13–16",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות.\n"
                  "**שפות:**\n"
                  r"$$N_{TM} = \{\langle M,w\rangle \mid (*)\}$$"
                  "(*): $M$ מקבלת את $w$ אחרי יותר מ-$|w|$ צעדים\n"
                  r"$$B_{TM} = \{\langle M\rangle \mid (**)\}$$"
                  "(**): קיימת מילה $w$ כך ש-$M$ מקבלת אותה אחרי יותר מ-$|w|$ צעדים\n"
                  r"$$F_{TM} = \{\langle M\rangle \mid \infty > L(M) \ne \emptyset\}$$"
                  "($L(M)$ סופית ולא ריקה)\n"
                  "**פונקציות מיפוי:**\n"
                  r"$$f(\langle M,w\rangle) = \langle R_{Mw}\rangle \qquad g(\langle M\rangle) = \langle T_M\rangle$$"
                  "כאשר המכונות $R_{Mw}$ ו-$T_M$ מוגדרות באופן הבא:\n"
                  "**$R_{Mw}$ על קלט $y$:**\n"
                  "1. הרץ את $M$ על $w$ ורשום את מספר הצעדים $T_w$.\n"
                  "2. אם $M$ דחתה – אז דחה.\n"
                  r"3. אם $|y| < 2 \cdot T_w$ וגם $T_w > |w|$ קבל. אחרת דחה." "\n"
                  "**$T_M$ על קלט $y$:**\n"
                  "1. הרץ את $M$ על כל המילים שאורכן לכל היותר $|y|$ למשך $|y|$ צעדים.\n"
                  "2. אם בשלב 1 המכונה $M$ קיבלה לפחות מילה אחת: קבל. אחרת: דחה."},
  "poly": {"kind": "text", "title": "הגדרות לשאלות 17–19",
           "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                   r"נסמן ב-$F_f(\phi)$ את המספר המקסימלי של משתנים שמקבלים ערך $F$ בהצבה מספקת של $\phi$." "\n"
                   r"$$F2SAT = \{\langle \phi\rangle \mid (*)\}$$"
                   r"(*): $\phi \in 3CNF$ וגם $F_f(\phi) \ge n-2$; $n$ הוא מספר המשתנים השונים שמופיעים ב-$\phi$" "\n"
                   "נגדיר את הפונקציה הבאה:\n"
                   r"$$f(\langle \phi\rangle) = \phi \wedge (\neg z_1 \vee \neg z_2 \vee \neg z_3) \wedge (\neg z_4 \vee \neg z_5 \vee \neg z_6) \wedge \cdots \wedge (\neg z_{N-2} \vee \neg z_{N-1} \vee \neg z_N)$$"
                   "כאשר $z_i$ הינם המשתנים המקוריים שמופיעים ב-$\\phi$. ערכו של $N$ מתחלק ב-3 והוא הגדול ביותר "
                   "שעדיין קטן או שווה למספר המשתנים השונים המופיעים ב-$\\phi$."},
}

questions = [
Q(1, "decidability",
  TF_INTRO + r"נתונות שלוש שפות $A, B, C$ המקיימות $A \subseteq B \subseteq C$. אם $A, C \notin RE$ אזי נובע ש-$B \notin RE$.",
  FT, "a",
  r"עבור השפות הבאות מתקיים $A \subseteq B \subseteq C$:" "\n"
  r"$$A = \{\langle M, M\rangle \mid L(M) = \Sigma^*\}$$"
  r"לשפה $A$ התאמה חח\"ע ועל עם השפה $ALL_{TM}$ ומתקיים $A \notin RE$." "\n"
  r"$$B = \{\langle M, M\rangle \mid L(M) \ne \emptyset\}$$"
  r"לשפה $B$ התאמה חח\"ע ועל עם השפה $\overline{E_{TM}}$ ומתקיים $B \in RE$." "\n"
  r"$$C = EQ_{TM}$$"
  r"ומתקיים $C \notin RE$.",
  note="Explanation line for B literally says 'לשפה A התאמה … E_TM-bar' (copy typo) — written as B. Φ rendered as \\emptyset."),

Q(2, "npc",
  TF_INTRO + r"תחת ההנחה $NPC \ne P$: $A \in NPC \Rightarrow \forall B \in P \;\; B \le_p A$",
  TF, "a",
  r"גם בלי ההנחה, אם $A$ לא טריוויאלית (ונתון $A \in NPC$ ושפה טריוויאלית לא מקיימת זאת), אז יש רדוקציה פולינומיאלית ל-$A$ מכל שפה ב-$P$."),

Q(3, "closure",
  TF_INTRO + r"אם $B \in R$ וגם $A \in RE \setminus R$ אזי $A - B \in RE \setminus R$.",
  TF, "b",
  r"עבור $B = \Sigma^* \in R$ וכל $A \in RE \setminus R$, נקבל $A - B = \emptyset \in R$."),

Q(4, "decidability",
  TF_INTRO + r"נתון $L(M) \in R$, לא טריוויאלית, וכן נתון ש-$M$ **לא מכריעה** את $L(M)$, אזי $\exists w \in \Sigma^*$, "
  "כך שסדרת הקונפיגורציות של החישוב של $M$ על $w$ היא סופית.",
  TF, "a",
  r"השפה לא טריוויאלית, בפרט לא ריקה, ולכן $\exists w \in \Sigma^*$ כך ש-$w \in L(M)$. המכונה $M$ אמנם לא מכריעה את השפה, "
  "אבל היא מקבלת אותה, ולכן המילה $w$ תתקבל על ידה, כלומר, סדרת הקונפיגורציות של החישוב היא סדרה סופית המסתיימת בקבלה."),

Q(5, "tm",
  TF_INTRO + "נתון ש-$M$ מכונת טיורינג לא דטרמיניסטית רב סירטית שמכריעה את $L$, אז קיימת מכונת טיורינג דטרמיניסטית "
  "וחד סירטית שמקבלת את $L$ אך לא מכריעה אותה.",
  TF, "a",
  r"**לא נכון:** השפה $L = \Sigma^*$ מפריכה את הטענה (כל מכונה המקבלת את השפה בהכרח גם מכריעה אותה, כי אין מילים שלא מתקבלות שיכולות להיכנס ללולאה אינסופית)." "\n"
  "**נכון:** אם נתון שהשפה $L$ לא טריוויאלית, אזי קיימת לפחות מילה אחת שלא מתקבלת על ידי השפה, ואפשר לשנות את המכונה כך שעל מילה זו "
  "היא תיכנס ללולאה אינסופית, ולכן תהיה עדיין מקבלת את אותה שפה $L$ אבל לא מכריעה אותה.\n"
  "כוונת השאלה המקורית היתה ללא שפות טריוויאליות, לכן פורסמה התשובה \"נכון\", אך מכיוון שטעינו בניסוח השאלה ופרסמנו כבר את התשובה, "
  "הוחלט לקבל את שתי התשובות.\n"
  "(הרב סרטיות והחד סרטיות לא רלוונטיים פה, מכיוון שיש שקילות בין שני המודלים ביחס להכרעה-קבלה של שפות).",
  acceptedIds=["a", "b"], answerSource="solution-pdf",
  note="No option highlighted. The key's explanation says the published answer was 'נכון' (א) and after the appeal both answers were accepted."),

Q(6, "time_p",
  TF_INTRO + r"נתון ש-$L \notin P$ אזי לכל $M$ – מ\"ט רב סירטית שמכריעה את $L$, ולכל מספר שלם $n$, קיימת מילה $w$ כך שאורך סדרת "
  r"הקונפיגורציות שמקבלת את $w$ גדול מ-$|w|^n$.",
  TF, "a",
  "הוכחה בדרך השלילה: אם המסקנה לא היתה נכונה, אז היתה קיימת מכונת טיורינג בסיסית אחת לפחות (שאפשר להפוך אותה לרב סירטית שקולה לה) "
  r"שמכריעה את $L$, שעבורה היה קיים $n$ כך שלכל מילה $w$ אורך סדרת הקונפיגורציות שמקבלת את $w$ היא קטנה או שווה $|w|^n$ "
  "(זו השלילה הלוגית של מה שכתוב אחרי \"אזי\"). אבל זו ההגדרה של שייכות ל-$P$, בסתירה לנתון שהשפה לא שייכת ל-$P$."),

Q(7, "classification",
  "סווג את השפה הבאה לאחת מהמחלקות המפורטות:\n"
  r"$$L = \{\langle M, w\rangle \mid (*)\}$$"
  "(*): $M$ לא עוצרת על $w$ לאחר פחות מ-$e^{|w|}$ צעדים",
  opts(R_, RE_, CO_, NEI_), "a",
  "ניתן לבנות מכונת טיורינג המקבלת כקלט $M, w$ ופועלת כך:\n"
  r"תריץ את $M$ על $w$ למשך $e^{|w|}$ צעדים (לכל היותר)." "\n"
  "אם בזמן ההרצה $M$ עצרה (קבלה או דחייה של $w$), אז תדחה את הזוג.\n"
  "אחרת, תקבל את הזוג.",
  note="Printed as L = {<M,w> | M לא עוצרת על w לאחר פחות מ e^{|w|} צעדים}; condition moved to a (*) line."),

Q(8, "classification",
  "סווג את השפה הבאה לאחת מהמחלקות המפורטות:\n"
  r"$$L = \{\langle M, w\rangle \mid w \notin L(M)\}$$",
  opts(CO_, RE_, R_, NEI_), "a",
  r"השפה המשלימה: $\overline{L} = \{\langle M, w\rangle \mid w \in L(M)\}$ ניתנת לקבלה, כי ניתן לבנות מכונת טיורינג המקבלת כקלט זוג $M, w$ ופועלת כך:" "\n"
  "מריצה את $M$ על $w$.\nאם $M$ עוצרת במצב מקבל, תקבל את הזוג.\nאחרת תדחה את הזוג.\n"
  "מכונה זו מקבלת את השפה המשלימה, אבל לא מכריעה אותה: היא עלולה להיכנס ללולאה אינסופית, במקרה ש-$M$ עושה זאת.\n"
  r"לכן $\overline{L}$ ניתנת לקבלה." "\n"
  "ולכן $L$ לא ניתנת לקבלה (כי אם היא וגם המשלימה ניתנות לקבלה, אז היא ניתנת להכרעה, ומזה היינו מסיקים שלכל מכונת טיורינג "
  "יש מכונה שקולה שמכריעה את השפה שלה, כלומר, כל שפה היא כריעה, וזה לא נכון)."),

Q(9, "classification",
  "סווג את השפה הבאה לאחת מהמחלקות המפורטות:\n"
  r"$$L = \{\langle M_1, M_2, M_3\rangle \mid L(M_1) \ne L(M_2) \cup L(M_3)\}$$",
  opts(NEI_, R_, RE_, CO_), "a",
  "אפשר לעשות רדוקציה מבעיית השקילות לבעייה זו: בהינתן קלט לבעיית השקילות, נתרגם לקלט של השפה $L$ הנ\"ל על ידי הוספת המכונה "
  "שדוחה כל מילה, בתור המכונה השלישית.\n"
  "באותו אופן ניתן לעשות רדוקציה מהמשלימה של בעיית השקילות, למשלימה של $L$, ולכן חייב להיות ששתיהן לא ניתנות לקבלה "
  "(אחרת בעיית השקילות היתה ניתנת לקבלה, ואנחנו יודעים שהיא לא).",
  note="Option ד is printed without the leading L ('לא ניתנת לקבלה אך L̄ ניתנת לקבלה'); written with $L$ like Q7/Q8."),

Q(10, "classification", "קבע מהו היחס בין $A$ ל-$B$:",
  opts(("math", r"A \cap B \ne \emptyset"), ("math", r"A \cap B = \emptyset"), ("math", r"A \supset B"), NONE),
  "a",
  r"לפי הגדרת $A$, $\langle M\rangle \in A$ אםם לכל $\langle G,k\rangle \in L(M)$ מתקיים $\langle G,k\rangle \in VC$, כלומר יש כיסוי קדקודים ב-$G$ בגודל $k$." "\n"
  r"לפי הגדרת $B$, $\langle M\rangle \in B$ אםם לכל $\langle G,k\rangle \in L(M)$ מתקיים $\langle G,k\rangle \in IS$, כלומר יש קבוצת קדקודים בלתי תלויה ב-$G$ בגודל $k$." "\n"
  r"אזי המכונה $M$ שמקבלת את כל הזוגות $\langle G,k\rangle$ שעבורם יש כיסוי קדקודים בגודל $k$ וגם קבוצת קדקודים בלתי תלויה בגודל $k$ "
  "(גרפים דו צדדיים עם $k$ קדקודים בשני הצדדים וזיווג מושלם) שייכת גם ל-$A$ וגם ל-$B$, לכן החיתוך לא ריק.",
  contextId="rel", note="Options printed with the glyph ϕ; rendered as \\emptyset."),

Q(11, "classification", "קבע מהו היחס בין $B$ ל-$C$:",
  opts(("math", r"C \subset B"), ("math", r"B \subset C"), ("math", "C = B"), NONE),
  "a",
  "$C$ זו קבוצה ריקה (בהגדרה, שפה של כל מכונת טיורינג ניתנת לקבלה על ידי עצמה), לכן באופן ריק היא מוכלת בכל קבוצה אחרת, "
  "אך לא להפך. היא גם לא שווה ל-$B$ כי $B$ לא ריקה.",
  contextId="rel"),

Q(12, "classification", "קבע מהו היחס בין $C$ ל-$A$:",
  opts(("math", r"A \cap C = \emptyset"), ("math", r"A \cap C \ne \emptyset"), ("math", r"C \supset A"), NONE),
  "a",
  "אותו הסבר מהשאלה הקודמת, מכיוון ש-$C$ ריקה, החיתוך שלה עם כל קבוצה הוא ריק.",
  contextId="rel", note="Options printed with the glyph ϕ; rendered as \\emptyset."),

Q(13, "mapping_reductions", r"האם $f$ היא רדוקציה $N_{TM} \le_m B_{TM}$?", YN, "a",
  r"$f$ ניתנת לחישוב (ניתן לחשב את הקידוד של המכונה $R_{Mw}$ בזמן סופי)." "\n"
  r"נראה שמתקיים $\langle M,w\rangle \in N_{TM} \Leftrightarrow \langle R_{Mw}\rangle \in B_{TM}$:" "\n"
  r"**(כיוון 1):** אם $\langle M,w\rangle \in N_{TM}$ אז $M$ מקבלת את $w$ אחרי יותר מ-$|w|$ צעדים. נראה מה זה אומר על $R_{Mw}$: על קלט $y$ ל-$R_{Mw}$," "\n"
  r"1. $M$ תרוץ על $w$ ותעצור בקבלה אחרי מספר צעדים המקיים $T_w > |w|$." "\n"
  r"2. מכיוון ש-$M$ לא דחתה, אז $R_{Mw}$ לא תדחה בשלב זה, ותעבור ל-3." "\n"
  r"3. מכיוון שמתקיים $T_w > |w|$, אזי אם מתקיים גם $|y| < 2T_w$, $y$ תתקבל, ואם לא, $y$ תידחה." "\n"
  r"מכאן אנו רואים שהמילים $y$ שיתקבלו על ידי $R_{Mw}$ הן רק אלה המקיימות $|y| < 2T_w$." "\n"
  r"בפרט, עבור $y = w$, כשנריץ את המכונה $R_{Mw}$ על $w$, נראה שמתקיימים שני דברים:" "\n"
  r"1. המילה $w$ תתקבל, כי המכונה תגיע לשלב 3, ומתקיים $|w| < T_w < 2T_w$." "\n"
  r"2. מספר הצעדים שהמכונה רצה הוא לפחות $|w|$ (בשלב 1 של המכונה, זה מספר הצעדים הנדרש), ואז יש עוד צעדים בהמשך." "\n"
  r"לכן מתקיים התנאי של שייכות ל-$B_{TM}$, כלומר $\langle R_{Mw}\rangle \in B_{TM}$." "\n"
  r"**(כיוון 2):** אם $\langle R_{Mw}\rangle \in B_{TM}$ אז קיימת מילה $y$ כלשהי (נסמנה $y$, כדי להבדילה מ-$w$, שיש לה כבר תפקיד בדיון זה) "
  r"ש-$R_{Mw}$ מקבלת אחרי יותר מ-$|y|$ צעדים. נסמן נתון זה ב-(*)." "\n"
  r"אבל ראינו כבר לעיל, שהמילים המתקבלות על ידי $R_{Mw}$ הן רק אלה שמקיימות $|y| < 2T_w$." "\n"
  r"נבדוק האם $M$ מקבלת את $w$ אחרי יותר מ-$|w|$ צעדים:" "\n"
  r"אם לא, אז או ש-$M$ לא מקבלת את $w$, ואז המכונה $R_{Mw}$ אף פעם לא עוצרת ולכן לא מקבלת אף מילה, בניגוד למה שאמרנו שקיימת מילה שמתקבלת (לפי (*)). אז זה לא יתכן." "\n"
  r"או ש-$M$ מקבלת את $w$ אבל אחרי $T_w \le |w|$ צעדים, ואז תעבור לשלב 3 בו תידחה את המילה כי לא מתקיים התנאי $T_w > |w|$. "
  r"ואז שוב המכונה $R_{Mw}$ לא מקבלת אף מילה, בניגוד לנתון שקיימת מילה שמתקבלת (לפי (*))." "\n"
  r"לכן נסיק שאכן $M$ מקבלת את $w$ אחרי יותר מ-$|w|$ צעדים, ולכן $\langle M,w\rangle \in N_{TM}$.",
  contextId="map"),

Q(14, "mapping_reductions", r"האם $f$ היא רדוקציה $N_{TM} \le_m F_{TM}$?", YN, "a",
  r"$f$ ניתנת לחישוב (ניתן לחשב את הקידוד של המכונה $R_{Mw}$ בזמן סופי)." "\n"
  r"נראה שמתקיים $\langle M,w\rangle \in N_{TM} \Leftrightarrow \langle R_{Mw}\rangle \in F_{TM}$:" "\n"
  r"**(כיוון 1):** אם $\langle M,w\rangle \in N_{TM}$ אז $M$ מקבלת את $w$ אחרי יותר מ-$|w|$ צעדים. נראה מה זה אומר על $R_{Mw}$: "
  r"בכל מקרה השפה של $R_{Mw}$ סופית כי הוא לא מקבל מילים שהאורך שלהם גדול מ-$2 \cdot T_w$ ויש מספר סופי של מילים כאלה. "
  r"כמו כן היא תקבל לפחות את $w$. ולכן היא סופית ולא ריקה." "\n"
  r"**(כיוון 2):** אם $\langle M,w\rangle \notin N_{TM}$ אזי או ש-$M$ לא עוצרת על $w$ ואז $R_{Mw}$ לא עוצרת על אף קלט והשפה שלה ריקה, "
  r"או שהיא עוצרת אבל לא מקבלת את $w$ – אז תנאי 2 מתקיים ושוב השפה של $R_{Mw}$ ריקה, "
  r"או שהיא מקבלת את $w$ אבל אחרי פחות מ-$|w|$ צעדים ואז החלק השני בתנאי 3 לא מתקיים ושוב השפה של $R_{Mw}$ ריקה. "
  r"ולכן $f(\langle M,w\rangle) \notin F_{TM}$.",
  contextId="map", answerSource="explanation-inferred", confidence="med",
  note="No option highlighted. The explanation proves f(<M,w>) ∈ F_TM ⇔ <M,w> ∈ N_TM, i.e. כן (א). Its opening line "
       "copy-pasted from Q13 says '⇔ <R_Mw> ∈ B_TM' — written as F_TM."),

Q(15, "mapping_reductions", r"האם $g$ היא רדוקציה $F_{TM} \le_m B_{TM}$?", YN, "b",
  contextId="map"),

Q(16, "mapping_reductions", r"האם $g$ היא רדוקציה $F_{TM} \le_m \overline{B_{TM}}$?", NY, "a",
  contextId="map"),

Q(17, "poly_reductions", "קבע האם הטענה הבאה נכונה או לא:\n" r"$$\phi \in F2SAT \Rightarrow f(\phi) \in 3SAT$$", TF, "a",
  r"$f(\langle\phi\rangle) = \phi \wedge \phi_2$." "\n"
  r"$f(\langle\phi\rangle)$ הוא בצורה נכונה (כלומר בצורת 3CNF). $\phi$ ניתן לסיפוק כי הוא שייך ל-$F2SAT$. "
  r"$\phi_2$ ניתן לסיפוק כי בכל פסוקית יש שלושה משתנים שונים של הנוסחא המקורית. יש הצבה מספקת שבה יש 2 או פחות משתנים בעלי ערך $T$. "
  r"ולכן בכל שלשה יש לפחות משתנה אחד שיש לו ערך $F$. ולכן שלילה שלו תהיה בעלת ערך $T$. כלומר גם ל-$\phi_2$ יש ערך אמת בהצבה המספקת.",
  contextId="poly"),

Q(18, "poly_reductions", "קבע האם הטענה הבאה נכונה או לא:\n" r"$$f(\phi) \in 3SAT \Rightarrow \phi \in F2SAT$$", FT, "a",
  r"יכול להיות ש-$\phi \notin F2SAT$ ובכל זאת $f(\phi) \in 3SAT$. למשל יש הצבה מספקת ל-$\phi$ שבה רק למשתנים המקוריים "
  r"$z_1, z_4, z_7, z_{10}, \ldots$ יש ערך $F$, ולשאר המשתנים יש ערך $T$. במקרה זה $\phi \notin F2SAT$ אבל $\phi$ וגם $\phi_2$ ספיקות בו זמנית.",
  contextId="poly",
  note="א 'לא נכון' fully highlighted; a stray yellow mark covers only the 'ב.' label. The explanation supports א. "
       "The explanation is cut off after 'ולכן' followed by a leftover 'Type equation here.' placeholder — ended at 'בו זמנית.'"),

Q(19, "poly_reductions", r"האם המסקנה היא: $F2SAT \le_p 3SAT$?",
  opts("ההוכחה שנתונה כאן שגויה. אבל המסקנה נכונה", "ההוכחה שנתונה כאן נכונה", "ההוכחה שגויה וגם המסקנה שגויה."),
  "a",
  r"ההוכחה שגויה כי לא מתקיים תנאי הרדוקציה. אבל ניתן להראות ש-$F2SAT \in P$ כי צריך לבדוק רק מספר פולינומי של אפשרויות "
  r"(לכל היותר לשני משתנים יש ערך $T$). ולכן בודאי מתקיים $F2SAT \le_p 3SAT$ כמו עבור כל שפה ב-$P$.",
  contextId="poly"),

Q(20, "npc",
  r"נניח שקיימת שפה $A$ כך שמתקיים $VC \le_p A$ וגם $\overline{A} \le_p IS$. איזו מהטענות הבאות נכונה?",
  opts("$NP$ סגורה למשלים", ("math", r"A \in RE \setminus R"), "$NP$ לא סגורה למשלים", ("math", "P = NP")),
  "a",
  r"מהנתון $\overline{A} \le_p IS$ מתקיים גם $A \le_p \overline{IS}$. ולכן על פי טרנזיטיביות נקבל $VC \le_p A \le_p \overline{IS}$, "
  r"כלומר $VC \le_p \overline{IS}$ ומכיוון ש-$IS \in NP$ אזי $\overline{IS} \in coNP$ ולכן גם $VC \in coNP$." "\n"
  "ומספיקה שפה אחת ($VC$) שהיא ב-$NPC$ וגם ב-$coNP$ כדי להסיק ש-$NP$ סגורה למשלים."),

Q(21, "tm",
  r"תהא $M$ מ\"ט לא דטרמיניסטית שמכריעה שפה ותהא $M^*$ המכונה שמתקבלת מ-$M$ ע\"י כך שמחליפים בין המצבים $q_{acc}$ ו-$q_{rej}$. "
  "איזו מהטענות הבאות **אפשרית**?",
  opts("כל התשובות נכונות",
       "קיימות מילים שעבורן עץ הקונפיגורציות של $M^*$ מכיל מסלולים אינסופיים",
       "עבור כל מילה עץ הקונפיגורציות של $M^*$ הינו סופי",
       "גם $M^*$ מכריעה שפה."),
  "a",
  "**ב אפשרית:** במכונה לא דטרמיניסטית שמכריעה, כל מילה מתקבלת או נדחית. אם מילה מתקבלת, יש לפחות מצב מקבל אחד בעץ שלה, "
  "אבל יכולים להיות מסלולים אחרים אינסופיים, ומסלולים אחרים דוחים. לכן בעץ של אותה מילה עבור $M^*$, גם יהיו מסלולים אינסופיים.\n"
  "**ג אפשרית:** במכונה לא דטרמיניסטית יכולים להיות מסלולים אינסופיים בעץ, אבל לא חייבים להיות. אם המצב הוא שאין מסלולים אינסופיים "
  "לאף מילה עבור $M$, אז גם ב-$M^*$ כל העצים יהיו סופיים.\n"
  "**ד אפשרית:** למשל אם המכונה היא כמו באפשרות ג, ואין מסלולים אינסופיים, אז גם ב-$M^*$ תמיד כל מילה או תידחה או תתקבל.",
  lockOrder=True),

Q(22, "mapping_reductions",
  "נתונות שתי שפות $B, A$. האם יתכן שאותה פונקציה $f$ תהיה רדוקציה מ-$A$ ל-$B$ וגם רדוקציה מ-$B$ ל-$A$?",
  opts("כן", "רק אם הרדוקציה היא רדוקצית מיפוי אך לא עבור רדוקציה פולינומית", "לא יתכן", "רק אם שתי השפות סופיות"),
  "a",
  "ראינו דוגמא כזו, $IS$, $CLIQUE$."),

Q(23, "time_p",
  r"תהא $M$ מ\"ט **רב סירטית** דטרמיניסטית שמכריעה את השפה $L$ בזמן $O(n^2)$ כאשר $n$ הוא אורך מילת הקלט. מהי מחלקת הסיבוכיות של $L(M)$?",
  opts("$P$", "בהכרח לא ב-$NP$.", r"אם $P \ne NP$ אזי התשובה היא $NPC$", r"אם $P \ne NP$ אזי התשובה היא $coNP \cup NPC$"),
  "a",
  "על פי ההגדרה, שפה שייכת למחלקה $P$ אם יש לה מכונה מכריעה, לכל מילה המתקבלת על ידי המכונה, אורך סדרת הקונפיגורציות קטן או שווה "
  "לפולינום מדרגה חסומה. כאן החסם הוא 2, לכן ההגדרה מתקיימת. הרב סירטיות לא מעלה ולא מורידה, כי הוכחנו ששקילות בין המודלים במובן "
  "שאם יש פולינום חוסם עבור מכונה חד סירטית, יש גם עבור רב סירטית, ולהפך."),

Q(24, "tm",
  "איזו מהתכונות הבאות הינה תכונה שנכונה עבור מ\"ט לא דטרמיניסטית ולא נכונה עבור מ\"ט בסיסית?",
  opts("פונקצית המעברים יכולה למפות מצב אחד למספר מצבים.",
       "המכונה יכולה להיות במספר מצבים בו זמנית",
       "סרט העבודה יכול להיות במספר מצבים בו זמנית",
       "היא יכולה להכריע שפות ב-$P$ בזמן פולינומי."),
  "a",
  "זהו חלק מהגדרת מכונה לא דטרמיניסטית: האי דטרמיניזם בא לידי ביטוי במעברים, במקום שיהיה מצב אחד ויחיד שאליו עוברים מכל מצב נתון "
  "(כמו במכונה דטרמיניסטית), יש קבוצה של מצבים מתוכם המכונה יכולה לבחור לאן לעבור."),

Q(25, "mapping_reductions",
  r"תהי $f(\langle M\rangle, w)$ פונקציה המוגדרת באופן הבא:" "\n"
  r"$$f(\langle M\rangle, w) = \begin{cases} -1 & \text{if } M \text{ does not stop on } w \\ k & \text{if } M \text{ stops on } w \text{ after } k \text{ steps} \end{cases}$$"
  "איזו מהטענות הבאות נכונה?",
  opts("הפונקציה $f$ לא ניתנת לחישוב.",
       "הפונקציה $f$ ניתנת לחישוב בזמן פולינומיאלי.",
       "הפונקציה $f$ ניתנת לחישוב, אבל לא בהכרח בזמן פולינומיאלי.",
       r"הפונקציה $f$ ניתנת לחישוב רק אם מתקיים $L(M) \in R$."),
  "a",
  "על מנת ש-$f$ תהיה ניתנת לחישוב, בפרט היא צריכה להיות מסוגלת לחשב האם $M$ עוצרת על $w$, אבל זוהי בעיית העצירה, "
  "שאנו יודעים שלא קיימת עבורה מכונת טיורינג שתכריע אותה."),
]

# --- RESOLUTIONS (ASK_ADIR items resolved by independent math check; Adir authorized 2026-09-29) ---
def _resolve(num, **kw):
    q = next(q for q in questions if q["num"] == num)
    q.pop("hold", None)
    q.update(kw)
_resolve(14, confidence="high",
  note="No highlight; א read from the explanation and independently verified: if <M,w> in N_TM then L(R_Mw) = {y : |y| < 2T_w} (finite, non-empty), else ∅.")

exam = {
  "examCode": "23B-A",
  "examLabel": "2023 סמסטר ב מועד א",
  "year": 2023,
  "examDate": "12.6.2023",
  "sourceFile": "מבחנים/2023/סמסטר א/2023-06-12-Exam-חישוביות-2023-moedA-גרסא-0 SOLUTION.pdf",
  "keyFile": "same file (yellow-highlighted options + yellow 'הסבר' paragraphs). Cover says 'סמסטר א' תשפ\"ג, מועד א'' "
             "with no date (Dr. Radel Ben-Av) — mis-filed/unedited template; filename date 12.6.2023 → semester ב מועד א.",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 26))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
