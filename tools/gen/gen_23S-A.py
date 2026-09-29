# -*- coding: utf-8 -*-
"""Generator for tools/raw/23S-A.json. Transcribed by hand from the rendered pages of
`מבחנים/2023/סמסטר קיץ/2023-08-23-Exam-חישוביות-2023-moedA-גרסא-0 SOLUTION.pdf` (render 23S-A-SOL).
The OPTIONS are NOT highlighted in this key file — only the "הסבר" paragraphs are yellow. Every answer is
therefore derived from its explanation (answerSource = explanation-inferred). Question text checked
against the clean student copy `מבחנים/2023/סמסטר קיץ/23-8-23.pdf` (render 23S-A-X), which is
identical in wording and option order except that the language E of Q13–16 is printed there as E_TM.
Run: PYTHONUTF8=1 py tools/gen/gen_23S-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23S-A.json"
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

TRUE, FALSE = "נכון", "לא נכון"
YES, NO = "כן", "לא"
TF = opts(TRUE, FALSE)      # א נכון, ב לא נכון
FT = opts(FALSE, TRUE)      # א לא נכון, ב נכון
YN = opts(YES, NO)
NY = opts(NO, YES)

# classification option texts (order differs per question)
C_R = "השפה $L$ ניתנת להכרעה"
C_RE = "השפה $L$ לא ניתנת להכרעה אך ניתנת לקבלה"
C_CO = r"השפה $L$ לא ניתנת לקבלה אך $\overline{L}$ ניתנת לקבלה"
C_NO = r"גם $L$ וגם $\overline{L}$ לא ניתנות לקבלה"
NONE_REL = "אף אחד מהנ\"ל"

CLAIMS2 = lambda neg: opts(f"טענה 1 נכונה וטענה 2 {neg}", f"טענה 2 נכונה וטענה 1 {neg}",
                           "שתי הטענות נכונות", "שתי הטענות שגויות")

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "explanation-inferred", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

contexts = {
  "rel": {"kind": "text", "title": "הגדרות לשאלות 10–12 (יחסים בין שפות)",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  r"$$A = \{\langle M\rangle \mid L(M) \in R\}$$"
                  r"$$B = \{\langle M\rangle \mid M \text{ halts on all } w \in \Sigma^*\}$$"
                  r"$$C = \{\langle M\rangle \mid L(M) \in RE\}$$"},
  "red": {"kind": "text", "title": "הגדרות לשאלות 13–16 (רדוקציית מיפוי)",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות.\n**שפות:**\n"
                  r"$$H_\varepsilon = \{\langle M\rangle \mid M \text{ is a T.M. and } M \text{ halts on } \varepsilon\}$$"
                  r"$$E_{TM} = \{\langle M\rangle \mid M \text{ is a T.M. and } L(M) = \emptyset\}$$"
                  "**פונקציות מיפוי:**\n"
                  r"$$f(\langle M\rangle) = \langle R_M\rangle \qquad g(\langle M\rangle) = \langle S_M\rangle$$"
                  "בהינתן מכונה $M$, המכונה $R_M$ מוגדרת באופן הבא:\n"
                  "$R_M$ על הקלט $w$:\n"
                  r"• אם $w \ne \varepsilon$, עצור וקבל." "\n"
                  "• אחרת, בלולאה על $i$, החל מ-$i=1$, ובכל סיבוב $i=i+1$:\n"
                  "  – ייצר את כל המילים באורך $0$ עד $i$.\n"
                  "  – הרץ את $M$ על כל המילים שנוצרו בשורה הקודמת, למשך $i$ צעדים.\n"
                  "  – אם $M$ עוצרת במצב מקבל על אחת מהמילים, עצור ו**דחה**.\n"
                  "בהינתן מכונה $M$, המכונה $S_M$ מוגדרת באופן הבא:\n"
                  "$S_M$ על הקלט $w$:\n"
                  r"• אם $w \ne \varepsilon$, עצור ודחה." "\n"
                  "• אחרת, בלולאה על $i$, החל מ-$i=1$, ובכל סיבוב $i=i+1$:\n"
                  "  – ייצר את כל המילים באורך $0$ עד $i$.\n"
                  "  – הרץ את $M$ על כל המילים שנוצרו בשורה הקודמת, למשך $i$ צעדים.\n"
                  "  – אם $M$ עוצרת במצב מקבל על אחת מהמילים, עצור ו**קבל**."},
  "poly": {"kind": "text", "title": "הגדרות לשאלות 17–19 (רדוקציה פולינומית)",
           "text": "תהיינה השפות הבאות:\n"
                   r"$$ALL_{DFA} = \{\langle A\rangle \mid A \text{ is a DFA and } L(A) = \Sigma^*\}$$"
                   r"$$ALL_{NFA} = \{\langle NA\rangle \mid NA \text{ is a NFA and } L(NA) = \Sigma^*\}$$"
                   r"$$R_G = \{\langle G, q_0, q_F\rangle \mid G \text{ is a directed graph, } q_0 \text{ and } q_F \text{ are vertices in } G \text{, and } q_F \text{ is } \textbf{not} \text{ reachable from } q_0\}$$"
                   "נגדיר את הפונקציות הבאות:\n"
                   r"$$f(\langle NA\rangle) = \langle A\rangle$$"
                   "כאשר $A$ הוא אוטומט החזקה של $NA$ (הנבנה בתהליך הדטרמינציה).\n"
                   r"$$g(\langle A\rangle) = \langle G, q_0, q_F\rangle$$"
                   "כאשר $G$ גרף המצבים של האס\"ד $A$, $q_0$ מצב ההתחלה של $A$, $q_F$ קדקוד חדש שמחוברים אליו "
                   "בצלע מכוונת כל הקדקודים של מצבים **לא** מקבלים של $A$."},
}

TF_INTRO = "שאלת נכון / לא-נכון. קבעו האם הטענה נכונה או לא.\n"

questions = [
Q(1, "time_p",
  TF_INTRO + r"תהי $L$ שפה הניתנת להכרעה על ידי מכונת טיורינג עם $k$ סרטים בזמן $\Theta(n)$. "
  r"אזי לכל מכונת טיורינג בסיסית המכריעה את $L$ יש סיבוכיות $\Theta(n^2)$.",
  FT, "a",
  "המשפט אומר ש**קיימת** מכונת טיורינג עם סרט אחד שתכריע בזמן **לכל היותר** ריבועי. אבל המשפט לא אומר שהחסם הדוק, "
  "וגם לא שולל את האפשרות שאולי קיימת מכונת טיורינג אחרת עם סרט אחד שיכולה לעשות את זה בזמן יותר טוב מאשר ריבועי."),

Q(2, "poly_reductions",
  TF_INTRO + r"תהי $L$ שפה $NP$-קשה המקיימת $\overline{L} \le_p 3SAT$. אזי $L \le_p \overline{L}$.",
  TF, "a",
  r"$3SAT$ היא שפה ב-$NPC$, ובפרט היא ב-$NP$, ולכן מהנתון $\overline{L} \le_p 3SAT$ נובע $\overline{L} \in NP$ (משפט הרדוקציה הפולינומית)." "\n"
  r"מהנתון ש-$L$ שפה $NP$-קשה, נובע שכל שפה $X$ ב-$NP$ ניתנת לרדוקציה פולינומיאלית אליה, כלומר $X \le_p L$, "
  r"וממילא $\overline{X} \le_p \overline{L}$. ניקח בתור $X$ את $\overline{L}$ ונקבל $\overline{\overline{L}} = L \le_p \overline{L}$."),

Q(3, "np",
  TF_INTRO + r"$A_{NFA} \in NP$",
  TF, "a",
  "אפשר להביא בתור עד את המסלול המקבל, ולבדוק אותו בזמן פולינומי בגודל הקלט. אורך המסלול המקבל, באוטומט, הוא כאורך המילה, "
  "ולכן הבדיקה לוקחת זמן כאורך המסלול כפול אורך הייצוג של האוטומט, כי צריך לבדוק שכל מעבר במסלול הוא מעבר חוקי – וזה זמן פולינומי בגודל הקלט."),

Q(4, "decidability",
  TF_INTRO + "כל מכונת טיורינג בסיסית המכריעה שפה $L$ לא טריוויאלית, ניתנת לתרגום למכונת טיורינג בסיסית "
  "המקבלת את אותה שפה $L$ אבל לא מכריעה אותה.",
  TF, "a",
  "ראינו (הרצאה על רדוקציות) איך להחליף את המצב הדוחה במצב מיוחד, שאם מגיעים אליו, נכנסים ללולאה אינסופית "
  "(בהנחה שקיימת מילה שנדחית – והרי נתון שהשפה לא טריוויאלית – ונקבל מילה שלא שייכת לשפה, שהמכונה לא עוצרת עליה)."),

Q(5, "mapping_reductions",
  TF_INTRO + r"קיימת שפה $L$ ניתנת לקבלה, שאינה ניתנת להכרעה, המקיימת $L \le_m \overline{L}$.",
  FT, "a",
  r"אילו זה היה נכון, היה מתקיים גם $\overline{L} \le_m L$, אבל אז לפי משפט הרדוקציה $\overline{L}$ ניתנת לקבלה. "
  "אבל שפה שגם היא וגם המשלימה שלה ניתנות לקבלה, בהכרח ניתנת להכרעה, בסתירה לנתון."),

Q(6, "np",
  TF_INTRO + r"אם $\overline{SAT} \in NP$ אזי $NP$ סגורה למשלים.",
  TF, "a",
  r"על פי המשפט $NP = coNP$ אם ורק אם $NPC \cap coNP \ne \emptyset$ (כי אם $\overline{SAT} \in NP$ אזי $SAT \in coNP$, "
  r"ומכיוון ש-$SAT \in NPC$ קיבלנו $NPC \cap coNP \ne \emptyset$ ולכן $NP = coNP$, כלומר $NP$ סגורה למשלים)."),

Q(7, "classification",
  "סווגו את השפה הבאה:\n"
  r"$$L = \{\langle M, w\rangle \mid M \text{ moves its head left on input } w \text{ (at some point)}\}$$",
  opts(C_R, C_RE, C_CO, C_NO), "a",
  "נריץ את $M$ על $w$, ואחרי לכל היותר $|Q|+|w|+1$ צעדים, נוכל לעצור את ההרצה של $M$ ולהחזיר תשובה:\n"
  "מקרה א: אם תוך מספר הצעדים הזה $M$ הזיזה את הראש הקורא שמאלה, נעצור ונגיד קבל.\n"
  "מקרה ב: אם תוך מספר הצעדים הזה $M$ לא הזיזה את הראש הקורא שמאלה, נעצור ונגיד דחה.\n"
  "ברור למה במקרה א התשובה נכונה, אבל למה במקרה ב אפשר לעצור ולדעת שאם עד עכשיו המכונה לא הזיזה את הראש הקורא שמאלה, זה גם לא יקרה בהמשך?\n"
  "נסביר: אחרי $|w|$ צעדים שבהם $M$ לא הזיזה את הראש הקורא שמאלה, היא הגיעה לרווח. מפה, כל עוד היא לא מזיזה את הראש הקורא שמאלה, "
  r"המעברים הם מהצורה $\delta(q_1, \sqcup) = (q_2, \sigma, R)$." "\n"
  "מכיוון שיש רק $|Q|$ מצבים, אחרי לכל היותר $|Q|$ צעדים המכונה תחזור למצב שבו היא הייתה, ותעמוד על רווח "
  "(אולי במעברים הקודמים היא כתבה משהו על הרווחים, אבל כל הזמן זזה ימינה אז לא חזרה אליהם, לכן כל הזמן קוראת רק רווחים ולא תווים אחרים). "
  "ברגע שחוזרים לקונפיגורציה שבה כבר היינו, וזזנו משם ימינה, אז המכונה תגיב כמו קודם – תזוז ימינה."),

Q(8, "classification",
  "סווגו את השפה הבאה:\n"
  r"$$L = \{\langle M_1, M_2\rangle : M_1, M_2 \text{ are T.M.s and } L(M_1) \subseteq L(M_2)\}$$",
  opts(C_NO, C_CO, C_RE, C_R), "a",
  r"אם $L$ הייתה ניתנת לקבלה, אז גם $EQ_{TM}$ הייתה ניתנת לקבלה: כדי לבדוק אם $\langle M_1, M_2\rangle \in EQ_{TM}$ יש לבדוק "
  r"$\langle M_1, M_2\rangle \in L$ וגם $\langle M_2, M_1\rangle \in L$." "\n"
  r"אם $\overline{L}$ הייתה ניתנת לקבלה, אז גם $\overline{EQ_{TM}}$ הייתה ניתנת לקבלה: כדי לבדוק $\langle M_1, M_2\rangle \notin EQ_{TM}$ "
  r"יש לבדוק $\langle M_1, M_2\rangle \notin L$ או $\langle M_2, M_1\rangle \notin L$ (אבל פה צריך להריץ בצורה \"מקבילה\", "
  "כדי שלא יקרה מצב שהתנאי השני מתקיים, אבל הבדיקה של התנאי הראשון לא עוצרת).",
  note="Key writes 'EQ_TM' / 'L משלים' / 'EQ_TM משלים' in plain text; rendered as EQ_{TM}, \\overline{L}, \\overline{EQ_{TM}}."),

Q(9, "classification",
  "סווגו את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid |L(M)| \ge 3\}$$",
  opts(C_RE, C_R, C_NO, C_CO), "a",
  "אפשר להריץ את $M$ על כל המילים בהרצה מבוקרת, בסדר מנייה לקסיקוגרפי. ברגע ש-3 מילים מתקבלות, נוכל לעצור ולהגיד קבל. "
  "לכן השפה ניתנת לקבלה.\n"
  r"אך המשלימה שלה (המשלימה היא $\{\langle M\rangle \mid |L(M)| < 3\}$) לא ניתנת לקבלה, ולכן השפה לא ניתנת להכרעה." "\n"
  r"הסבר למה המשלימה לא ניתנת לקבלה: ניתן לעשות רדוקציה מ-$\overline{H_{TM}}$ על ידי $f(\langle M, w\rangle) = \langle K_{M,w}\rangle$."),

Q(10, "decidability", "קבעו מהו היחס בין $A$ ל-$B$:",
  opts(("math", r"B \subset A"), ("math", r"A \subset B"), ("math", r"A = B"), NONE_REL), "a",
  "אם $M$ מכונה שעוצרת על כל קלט, אז וודאי שהיא מכריעה את השפה שלה. לכן כל מכונה ב-$B$ בהכרח שייכת גם ל-$A$. "
  "אבל יש מכונות שלא תמיד עוצרות, ובכל זאת השפה שלהן ניתנת להכרעה (על ידי מכונה אחרת, המקבלת אותה שפה, אבל כן תמיד עוצרת. "
  r"למשל, ראינו עבור השפה $0\Sigma^*$ גם מכונה מכריעה וגם מכונה לא מכריעה).",
  contextId="rel"),

Q(11, "decidability", "קבעו מהו היחס בין $B$ ל-$C$:",
  opts(("math", r"B \subset C"), ("math", r"C \subset B"), ("math", r"C = B"), NONE_REL), "a",
  "הקבוצה $C$ היא שפת כל הקידודים של מכונות טיורינג (בהגדרה, שפה של מכונת טיורינג ניתנת לקבלה). לכן ודאי $B$ מוכלת ב-$C$. "
  "אבל יש מכונות שלא תמיד עוצרות. לכן אין הכלה בכיוון השני.",
  contextId="rel",
  note="Key text: 'אבל יש מכונות שהשפה שלא תמיד עוצרות' (garbled); cleaned to 'אבל יש מכונות שלא תמיד עוצרות'."),

Q(12, "decidability", "קבעו מהו היחס בין $C$ ל-$A$:",
  opts(("math", r"A \subset C"), ("math", r"C \subset A"), ("math", r"A = C"), NONE_REL), "a",
  "הקבוצה $C$ היא שפת כל הקידודים של מכונות טיורינג (בהגדרה, שפה של מכונת טיורינג ניתנת לקבלה). לכן ודאי $A$ מוכלת ב-$C$. "
  "אבל יש מכונות שהשפה שלהן ניתנת לקבלה אבל המכונה לא תמיד עוצרת, לכן אין הכלה בכיוון השני.",
  contextId="rel"),

Q(13, "mapping_reductions", r"האם $f$ רדוקציה $E_{TM} \le_m \overline{H_\varepsilon}$?",
  YN, "a",
  r"**$\langle M\rangle \in E_{TM}$:** אזי $M$ מכונת טיורינג שהשפה שלה ריקה. נראה מה יקרה כאשר נריץ את $R_M$ על המילה הריקה: "
  "מכיוון שהשפה של $M$ ריקה, אף מילה שתיווצר לא תתקבל, ולכן $M$ לא תעצור על אף מילה, והמכונה $R_M$ תמשיך לייצר מילים בלולאה עד אינסוף, "
  r"כלומר, לא תעצור. כלומר, המכונה $R_M$ לא עוצרת על המילה הריקה, ולכן $\langle R_M\rangle \notin H_\varepsilon$, כלומר $\langle R_M\rangle \in \overline{H_\varepsilon}$." "\n"
  r"**$\langle M\rangle \notin E_{TM}$:** אזי או ש-$M$ לא קידוד של מכונת טיורינג, ואז $f(\langle M\rangle) = \langle M_{Acc}\rangle$, "
  r"ומתקיים $\langle M_{Acc}\rangle \in H_\varepsilon$ ולכן $\langle M_{Acc}\rangle \notin \overline{H_\varepsilon}$, "
  "או ש-$M$ מכונת טיורינג שהשפה שלה לא ריקה: נראה מה יקרה כאשר נריץ את $R_M$ על המילה הריקה: מכיוון שהשפה של $M$ לא ריקה, "
  "קיימת מילה אחת לפחות שתתקבל בלולאה (מכיוון שהריצה היא ריצה מבוקרת, נגיע למילה זו), והמכונה $R_M$ תעצור ותדחה. "
  "הדחייה לא מעניינת, אלא העובדה שהמכונה $R_M$ עצרה על המילה הריקה. "
  r"כלומר $\langle R_M\rangle \in H_\varepsilon$, כלומר $\langle R_M\rangle \notin \overline{H_\varepsilon}$.",
  contextId="red",
  note="Key file names the language 'E'; the student question paper (23-8-23.pdf) prints E_TM — used E_TM throughout Q13-16."),

Q(14, "mapping_reductions", r"האם $g$ רדוקציה $E_{TM} \le_m \overline{H_\varepsilon}$?",
  YN, "a",
  "ההסבר כנ\"ל (כמו בשאלה 13), השאלה אם המכונה מקבלת או דוחה לא רלוונטית, אלא רק שהיא עוצרת.",
  contextId="red",
  note="Explanation only says 'as above; accept/reject is irrelevant, only halting' — implies כן (א)."),

Q(15, "mapping_reductions", r"האם $f$ רדוקציה $E_{TM} \le_m H_\varepsilon$?",
  NY, "a",
  r"אם הייתה מתקיימת הרדוקציה, אזי $H_\varepsilon$ הייתה לא ניתנת לקבלה (לפי משפט הרדוקציה, ברדוקציה מ-$E_{TM}$ שכידוע לא ניתנת לקבלה). "
  "אך היא כן ניתנת לקבלה: בהינתן מכונה $M$, אפשר לסמלץ ריצה של $M$ על המילה הריקה, ואם הסימולציה תעצור, נעצור ונקבל.",
  contextId="red"),

Q(16, "mapping_reductions", r"האם $g$ רדוקציה $E_{TM} \le_m H_\varepsilon$?",
  NY, "a",
  "ההסבר כנ\"ל (כמו בשאלה 15).",
  contextId="red",
  note="Explanation only says 'הסבר כנ\"ל'; Q15's argument (no reduction E_TM -> H_eps exists at all) applies verbatim -> לא (א)."),

Q(17, "poly_reductions", "האם הטענה הבאה נכונה?\n"
  r"$$\langle NA\rangle \in ALL_{NFA} \iff f(\langle NA\rangle) \in ALL_{DFA}$$",
  TF, "a",
  "תהליך הדטרמינציה של אסל\"ד נותן אס\"ד שקול לו, כלומר, שניהם מקבלים אותה שפה, לכן השפה של האס\"ד היא כל המילים "
  "אם\"ם השפה של האסל\"ד היא כל המילים.",
  contextId="poly",
  note="Printed as 'f(<NA>) ∈ ALL_DFA ⇔ <NA> ∈ ALL_NFA' (visual RTL order of the same biconditional)."),

Q(18, "poly_reductions", "האם הטענה הבאה נכונה?\n"
  r"$$\langle A\rangle \in ALL_{DFA} \iff g(\langle A\rangle) \in R_G$$",
  TF, "a",
  "השפה של אס\"ד מכילה את כל המילים, אם\"ם כל מילה מגיעה למצב מקבל, כלומר, אין מילים שמגיעות למצבים לא מקבלים, "
  "כלומר בגרף של האוטומט, עם המצב החדש $q_F$, לא ניתן להגיע מ-$q_0$ ל-$q_F$.",
  contextId="poly"),

Q(19, "poly_reductions", r"האם המסקנה היא כי $ALL_{NFA} \le_p R_G$?",
  opts("לא, מכיוון שהפונקציה $f$ לא ניתנת לחישוב בזמן פולינומי",
       "לא, מכיוון שהפונקציה $g$ לא ניתנת לחישוב בזמן פולינומי",
       "כן",
       "לא, מכיוון שלא ניתן להרכיב את הפונקציות אחת על השנייה בכיוון הנכון"), "a",
  "הרכבת הרדוקציות נותנת רדוקציית מיפוי תקינה מאסל\"ד לגרף, אבל שלב הדטרמינציה הוא שלב אקספוננציאלי, "
  "ולכן הרדוקציה המתקבלת היא לא פולינומיאלית ($g$ לעומת זאת כן פולינומיאלית, על ידי הרצת $BFS$).",
  contextId="poly"),

Q(20, "npc",
  r"כדי להוכיח $3SAT \le_p IS$, הגדרנו רדוקציה $f(\langle \phi\rangle) = \langle G_\phi, n\rangle$, כאשר $\phi$ נוסחה לוגית, "
  r"ו-$G_\phi = (V, E)$ כאשר:" "\n"
  r"$V$: לכל מופע של ליטרל ב-$\phi$ נתאים קודקוד." "\n"
  "$E$:\n"
  "• צלעות פסוקית: נחבר בצלע קודקודים שמתאימים לליטרלים מאותה פסוקית.\n"
  "• צלעות משתנה: נחבר בצלע כל זוג קודקודים שמתאימים לליטרל ושלילתו.\n"
  "מהו $n$ בהגדרה זו?",
  opts(r"מספר הפסוקיות שמופיעות ב-$\phi$", r"מספר המשתנים שמופיעים ב-$\phi$",
       r"מספר הליטרלים שמופיעים ב-$\phi$", "אף תשובה אחרת אינה נכונה"), "a",
  "כך הגדרנו את הרדוקציה, ניתן לראות במצגת.",
  confidence="med",
  note="Explanation does not name an option. א (number of clauses) is the standard 3SAT<=p IS target size and "
       "matches the all-א pattern of this key, but it is inferred, not stated."),

Q(21, "undecidability",
  r"תהי $M$ מכונת טיורינג בסיסית. לפניכם הצעה לאלגוריתם שיכריע אם $L(M) = \emptyset$ (יחזיר $TRUE$ אם השפה ריקה, ו-$FALSE$ אחרת):" "\n"
  "• נבנה את הגרף $G$ שמייצג את המכונה $M$ (הקדקודים יהיו המצבים של $M$ והצלעות יהיו בהתאם לפונקציית המעברים של $M$).\n"
  r"• נריץ $BFS(G, q_0)$." "\n"
  r"• אם $d(q_{acc}) = \infty$ נענה $TRUE$, אחרת, נענה $FALSE$." "\n"
  "לפניכם שתי טענות:\n"
  "טענה 1: האלגוריתם לא מכריע את הבעיה, כי הוא עלול להחזיר $FALSE$ גם אם השפה ריקה.\n"
  "טענה 2: האלגוריתם לא מכריע את הבעיה, כי הוא עלול להחזיר $TRUE$ גם אם השפה לא ריקה.\n"
  "בחרו בתשובה הנכונה:",
  CLAIMS2("שגויה"), "a",
  "ודאי שאם לא ניתן להגיע למצב המקבל בגרף, אזי אף מילה לא תוכל להתקבל והשפה תהיה ריקה. אז טענה 2 לא נכונה. "
  "אבל, ייתכן שאפשר להגיע למצב המקבל, ועדיין השפה ריקה, למשל, אם המעבר שמוביל למצב המקבל הוא על ידי תו שלא נמצא בא\"ב הקלט, "
  "ובאף מצב התו הזה לא נכתב על הסרט – זה לא שיקול שאפשר לעשות על ידי בדיקת מבנה הגרף בלבד.\n"
  "הערה: הסיבה שבאוטומט האלגוריתם הזה (בווריאציה קלה, כפי שראינו בהרצאה) כן עובד, היא שבאוטומטים אין אפשרות לכתוב על מילת הקלט, "
  "בפרט, אין שתי קבוצות שונות של א\"ב הקלט וא\"ב הסרט, ומתקדמים בצורה סדרתית על תווי הקלט (בלי אפשרות לחזור אחורה, כמו במ\"ט).",
  note="Options printed 'שגוייה'; spelled 'שגויה'."),

Q(22, "mapping_reductions",
  "תזכורת: יחס $R$ מהווה יחס שקילות אם הוא סימטרי (אם $aRb$ אז $bRa$), טרנזיטיבי (אם $aRb$ וגם $bRc$ אז $aRc$) "
  "ורפלקסיבי (לכל $a$ מתקיים $aRa$).\n"
  r"יחס הרדוקציה $\le_m$ הוא יחס שקילות, נכון או לא נכון?",
  opts("לא נכון, מכיוון שהיחס אינו סימטרי", "לא נכון, מכיוון שהיחס אינו טרנזיטיבי",
       "לא נכון, מכיוון שהיחס אינו רפלקסיבי", "נכון"), "a",
  r"יחס הרדוקציה הוא יחס טרנזיטיבי ורפלקסיבי, אבל אינו סימטרי: ייתכן שמתקיים $A \le_m B$ אבל לא $B \le_m A$, "
  "למשל, אם $A$ ניתנת להכרעה ו-$B$ לא ניתנת להכרעה."),

Q(23, "np",
  r"האם קיימת שפה $L$ המקיימת $L \in NP \cap coNP$ וגם $L \notin P$?",
  opts("לא ידוע", "כן, השפה $SAT$", "כן, השפה $PRIME$", "לא"), "a",
  r"השפה $PRIME$ הוכחה לקיים גם $PRIME \in NP \cap coNP$ וגם $PRIME \in P$. לגבי השפה $SAT$, לא ידוע אם היא ב-$P$, "
  "וגם לא ידוע אם היא ב-$coNP$. אם $P=NP$, אז ודאי שהמקרה בשאלה לא אפשרי, אבל לא ידוע אם זה המצב."),

Q(24, "mapping_reductions",
  r"תהיינה $A, B \subseteq \Sigma^*$ שפות, ונניח כי $A \le_m \emptyset$ וגם $\emptyset \le_m B$. להלן שתי טענות:" "\n"
  r"1. בהכרח מתקיים כי $A = \emptyset$." "\n"
  r"2. בהכרח מתקיים כי $B = \emptyset$." "\n"
  "בחרו בתשובה הנכונה:",
  CLAIMS2("אינה נכונה"), "a",
  r"רדוקציה לא אפשרית משפה לא טריוויאלית לשפה טריוויאלית: עבור $A$ שאינה ריקה, קיים $x \in A$ אבל לכל $f: \Sigma^* \to \Sigma^*$ "
  r"יתקיים $f(x) \notin \emptyset$. לכן טענה 1 נכונה. לעומת זאת, מהקבוצה הריקה אפשר להגדיר רדוקציה ל-$B$, אם $B$ לא טריוויאלית: "
  r"אם קיים $w \notin B$, אזי נוכל להגדיר את הרדוקציה $f(x) = w$.",
  note="Empty set printed as Φ; rendered as \\emptyset."),

Q(25, "mapping_reductions",
  r"תהיינה שתי שפות $A, B$ מעל הא\"ב $\Sigma$, ונתון ש-$A$ שפה לא ניתנת להכרעה, $B$ שפה לא טריוויאלית, "
  r"לכן קיימים $x, y \in \Sigma^*$ כך ש-$x \in B, y \notin B$." "\n"
  r"נגדיר את הפונקציה $f: \Sigma^* \to \Sigma^*$:" "\n"
  r"$$f(w) = \begin{cases} x & \text{if } w \in A \\ y & \text{if } w \notin A \end{cases}$$"
  "בחרו בתשובה הנכונה:",
  opts("$f$ לא ניתנת לחישוב", "$f$ ניתנת לחישוב אבל לא בהכרח בזמן פולינומיאלי",
       "$f$ ניתנת לחישוב בזמן פולינומיאלי", "$f$ ניתנת לחישוב אם\"ם $A$ לא טריוויאלית"), "a",
  "הפונקציה הזו ניתנת לחישוב רק אם $A$ ניתנת להכרעה, מכיוון שההחלטה אם הפלט של $f$ הוא $x$ או $y$ תלויה ביכולת לבדוק "
  "האם $w$ שייכת ל-$A$ או לא. מכיוון שנתון ש-$A$ לא ניתנת להכרעה, הפונקציה $f$ לא ניתנת לחישוב."),
]

exam = {
  "examCode": "23S-A",
  "examLabel": "2023 סמסטר קיץ מועד א",
  "year": 2023,
  "examDate": "23.8.2023",
  "sourceFile": "מבחנים/2023/סמסטר קיץ/2023-08-23-Exam-חישוביות-2023-moedA-גרסא-0 SOLUTION.pdf",
  "keyFile": "same file — options NOT highlighted; answers inferred from the yellow 'הסבר' paragraphs "
             "(question text cross-checked with מבחנים/2023/סמסטר קיץ/23-8-23.pdf)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 26))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
