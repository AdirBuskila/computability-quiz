# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-B.json (KEYLESS sitting, stage 1 of SOLVE_GUIDE.md).
Transcribed from `מבחנים/2024/סמסטר ב/2024-08-01-Exam-חישוביות-2024-moedB-טופס-0.pdf`
(form 000, no marks). Options kept in printed order. Answers = my own rigorous solutions
(answerSource "solved", official False); form-0 first option recorded in `note`.
The file `מועד ב מעורבב.pdf` (same PDF with pasted re-ordered option strips) is ignored.
Run: PYTHONUTF8=1 py -W error::SyntaxWarning tools/gen/gen_24B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-B.json"
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

ALLF = "כל הטענות האחרות לא נכונות"
DEC4 = opts(
    "השפה $L$ ניתנת להכרעה.",
    "השפה $L$ ניתנת לקבלה אבל לא-ניתנת להכרעה.",
    r"השפה $L$ לא-ניתנת לקבלה אבל $\overline{L}$ ניתנת לקבלה.",
    r"השפה $L$ לא-ניתנת לקבלה וגם $\overline{L}$ לא-ניתנת לקבלה.",
)
# Q12/Q13 print the first two DEC options swapped
DEC4_SW = opts(
    "השפה $L$ ניתנת לקבלה אבל לא-ניתנת להכרעה.",
    "השפה $L$ ניתנת להכרעה.",
    r"השפה $L$ לא-ניתנת לקבלה אבל $\overline{L}$ ניתנת לקבלה.",
    r"השפה $L$ לא-ניתנת לקבלה וגם $\overline{L}$ לא-ניתנת לקבלה.",
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
Q(1, "mapping_reductions", "איזו מהטענות הבאות נכונה?",
  opts(r"אם $L \in R$ אז מתקיים $L \le_m E_{TM}$",
       r"מתקיים $\overline{E_{TM}} \le_m E_{TM}$",
       r"אם $L \notin R$ אז מתקיים $L \le_m \overline{E_{TM}}$",
       ALLF),
  "a", ex(
  r"""**הוכחת א:** כל שפה ב-$R$ ניתנת לרדוקציית מיפוי לכל שפה לא טריוויאלית, ו-$E_{TM}$ לא טריוויאלית: מכריעים את $L$ על הקלט $x$, ואם $x \in L$ מחזירים קידוד קבוע של מכונה שדוחה הכול (ששייך ל-$E_{TM}$), אחרת קידוד קבוע של מכונה שמקבלת הכול.""",
  r"""**הפרכת ב:** $\overline{E_{TM}} \in RE$, ולכן מהרדוקציה היינו מקבלים $E_{TM} \in RE$ (כי $\overline{E_{TM}} \le_m E_{TM}$ שקול ל-$E_{TM} \le_m \overline{E_{TM}}$). אז $E_{TM} \in RE \cap coRE = R$ – סתירה.""",
  r"""**הפרכת ג:** $L = E_{TM}$: היא לא ב-$R$, ואילו $E_{TM} \le_m \overline{E_{TM}}$ הייתה נותנת $E_{TM} \in RE$ – סתירה כנ"ל.""",
  r"""**הפרכת ד:** א נכונה.""")),

Q(2, "np", "איזו מהטענות הבאות נכונה?",
  opts(r"מתקיים $\overline{PALINDROMES} \in NP$",
       r"מתקיים $\overline{A_{TM}} \in P$",
       r"אם $L_1 \cap L_2 \in NP$ אז מתקיים $L_1 \in NP$ וגם $L_2 \in NP$",
       r"אם $L_1 \cup L_2 \in NP$ אז מתקיים $L_1 \in NP$ וגם $L_2 \in NP$"),
  "a", ex(
  r"""**הוכחת א:** $PALINDROMES \in P$ (משווים את המילה להיפוכה בזמן פולינומי), $P$ סגורה למשלים ולכן $\overline{PALINDROMES} \in P \subseteq NP$.""",
  r"""**הפרכת ב:** $\overline{A_{TM}}$ אינה ניתנת לקבלה, ובפרט אינה ב-$P \subseteq R$.""",
  r"""**הפרכת ג:** $L_1 = A_{TM}$, $L_2 = \emptyset$: החיתוך $\emptyset \in NP$ אבל $A_{TM} \notin NP$ (כי $NP \subseteq R$).""",
  r"""**הפרכת ד:** $L_1 = A_{TM}$, $L_2 = \Sigma^*$: האיחוד $\Sigma^* \in NP$ אבל $A_{TM} \notin NP$.""")),

Q(3, "tm",
  r"יהיו $M_1, M_2$ מכונות טיורינג דטרמיניסטיות כך שמתקיים $L(M_1) = L(M_2)$." "\n"
  r"תהי $w$ מילה השייכת ל-$\Sigma^*$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(r"אם $M_1$ מקבלת את $w$ אז $M_2$ עוצרת על $w$",
       r"אם $M_1$ עוצרת על $w$ אז $M_2$ עוצרת על $w$",
       r"אם $M_1$ לא-עוצרת על $w$ אז $M_2$ לא-עוצרת על $w$",
       ALLF),
  "a", ex(
  r"""**הוכחת א:** אם $M_1$ מקבלת את $w$ אז $w \in L(M_1) = L(M_2)$, כלומר $M_2$ מקבלת את $w$ – ובפרט עוצרת עליה.""",
  r"""**הפרכת ב:** $M_1$ דוחה את כל המילים ו-$M_2$ לא עוצרת על אף מילה: $L(M_1) = L(M_2) = \emptyset$, $M_1$ עוצרת על $w$ ו-$M_2$ לא.""",
  r"""**הפרכת ג:** אותה דוגמה עם התפקידים הפוכים.""",
  r"""**הפרכת ד:** א נכונה.""")),

Q(4, "tm",
  r"תהי $M = \langle Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej}\rangle$ מכונת טיורינג, כאשר $\Sigma$ הוא א\"ב הקלט וכאשר $\Gamma$ הוא א\"ב הסרט." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(r"הא\"ב $\Sigma$ מוכל ממש בא\"ב $\Gamma$",
       r"יתכן שהא\"ב $\Sigma$ שווה לא\"ב $\Gamma$",
       r"יתכן שמתקיים $\Gamma \cap \Sigma = \emptyset$",
       ALLF),
  "a", ex(
  r"""**הוכחת א:** לפי ההגדרה $\Sigma \subseteq \Gamma$, ותו הרווח $\sqcup$ שייך ל-$\Gamma$ אך לא ל-$\Sigma$. לכן $\Sigma \subsetneq \Gamma$.""",
  r"""**הפרכת ב:** $\sqcup \in \Gamma \setminus \Sigma$, ולכן $\Sigma \ne \Gamma$.""",
  r"""**הפרכת ג:** $\Sigma \subseteq \Gamma$ ו-$\Sigma$ (אלפבית) אינו ריק, ולכן $\Gamma \cap \Sigma = \Sigma \ne \emptyset$.""",
  r"""**הפרכת ד:** א נכונה."""),
  note="Option ג relies on the course convention that an alphabet is non-empty (if Σ=∅ were allowed, ג would also hold)."),

Q(5, "np",
  r"תהיינה $A, B, C$ שפות לא-טריוויאליות כך שמתקיים: $A \le_p B \cap C$." "\n"
  r"בנוסף, מתקיים $C \in P$ וגם $B \in NP$." "\n"
  "איזו מהטענות הבאות נכונה?",
  opts(r"מתקיים $A \in NP$",
       r"יתכן שמתקיים $A \notin NP$",
       r"לא ידוע האם מתקיים $P = NP$ ולכן לא ניתן לקבוע בוודאות האם מתקיים $A \in NP$",
       ALLF),
  "a", ex(
  r"""**הוכחת א:** $C \in P \subseteq NP$, ו-$NP$ סגורה לחיתוך (מריצים את המוודא של $B$ ואת המכריע של $C$), לכן $B \cap C \in NP$. מאחר ש-$A \le_p B \cap C$ ו-$NP$ סגורה תחת רדוקציה פולינומית, $A \in NP$.""",
  r"""**הפרכת ב, ג:** לפי ההוכחה $A \in NP$ בוודאות, ללא תלות בשאלה $P = NP$.""",
  r"""**הפרכת ד:** א נכונה.""")),

Q(6, "decidability", "איזו מהטענות הבאות נכונה?",
  opts("קיימת שפה ניתנת לקבלה שאינה ניתנת להכרעה",
       "קיימת שפה ניתנת להכרעה שאינה ניתנת לקבלה",
       r"אם $L_2 \subseteq L_1$ וגם השפה $L_1$ ניתנת להכרעה אז מתקיים: השפה $L_2$ ניתנת לקבלה",
       r"אם $L_2 \subseteq L_1$ וגם השפה $L_1$ ניתנת לקבלה אז מתקיים: השפה $L_2$ ניתנת להכרעה"),
  "a", ex(
  r"""**הוכחת א:** $A_{TM} \in RE \setminus R$.""",
  r"""**הפרכת ב:** $R \subseteq RE$ – מכריע הוא בפרט מקבל.""",
  r"""**הפרכת ג:** $L_1 = \Sigma^*$ (כריעה), $L_2 = \overline{A_{TM}} \subseteq L_1$ שאינה ניתנת לקבלה.""",
  r"""**הפרכת ד:** $L_1 = \Sigma^*$, $L_2 = A_{TM}$ שאינה ניתנת להכרעה.""")),

Q(7, "time_p",
  r"תזכורת: אם $w = \sigma_1\sigma_2\cdots\sigma_n$ אז נגדיר $w^R = \sigma_n\sigma_{n-1}\cdots\sigma_1$. לכל שפה $L$ נגדיר את השפה ההופכית באופן הבא: $L^R = \{w \mid w^R \in L\}$." "\n"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $L \in P$ אזי מתקיים $L^R \in P$." "\n"
  r"II. אם $L \in NP$ אזי מתקיים $L^R \in NP$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  opts("שתי הטענות I, II הן נכונות.",
       "טענה I נכונה וגם טענה II לא נכונה.",
       "שתי הטענות I, II הן לא נכונות.",
       "טענה II נכונה וגם טענה I לא נכונה."),
  "a", ex(
  r"""**טענה I נכונה:** על קלט $w$ מחשבים את $w^R$ (בזמן $O(|w|^2)$ במ"ט בסיסית) ומריצים עליו את המכריע הפולינומי של $L$ (כאשר $|w^R| = |w|$). סה"כ זמן פולינומי, והמכונה מקבלת בדיוק כאשר $w^R \in L$.""",
  r"""**טענה II נכונה:** אותה בנייה עם מכונה לא דטרמיניסטית פולינומית עבור $L$ (או: מוודא של $L^R$ מקבל $\langle w, c\rangle$ ומריץ את המוודא של $L$ על $\langle w^R, c\rangle$).""")),

Q(8, "mapping_reductions",
  r"תהיינה $L_1, L_2$ שפות." "\n"
  r"נניח כי קיימת פונקציה ניתנת לחישוב $f: \Sigma^* \to \Sigma^*$ כך שלכל $x \in \Sigma^*$ מתקיים:" "\n"
  r"$$x \notin L_1 \Leftrightarrow f(x) \notin L_2$$"
  r"נתבונן בטענה הבאה: אם מתקיים $L_2 \in R$ אזי מתקיים $L_1 \in R$." "\n"
  "איזה מהסעיפים הבאים נכון?",
  opts("הטענה נכונה", "הטענה לא נכונה"),
  "a", ex(
  r"""**הטענה נכונה:** התנאי $x \notin L_1 \Leftrightarrow f(x) \notin L_2$ שקול ל-$x \in L_1 \Leftrightarrow f(x) \in L_2$, ולכן $f$ היא רדוקציה $L_1 \le_m L_2$. לפי משפט הרדוקציה, אם $L_2 \in R$ אז $L_1 \in R$.""")),

Q(9, "closure",
  r"תהי $L$ שפה ניתנת להכרעה, כלומר $L \in R$." "\n"
  "נגדיר את השפה הבאה:\n"
  r"$$A(L) = \{w \mid (*)\}$$"
  r"(*): $w \notin L$ וגם $|w| > 3$" "\n"
  "איזו מהטענות הבאות נכונה?",
  opts("השפה $A(L)$ ניתנת להכרעה",
       "השפה $A(L)$ ניתנת לקבלה וגם יתכן שהשפה $A(L)$ לא-ניתנת להכרעה",
       "יתכן שהשפה $A(L)$ לא-ניתנת לקבלה",
       ALLF),
  "a", ex(
  r"""**הוכחת א:** $A(L) = \overline{L} \cap \{w \mid |w| > 3\}$. $\overline{L} \in R$ (סגירות למשלים) והשפה $\{w \mid |w| > 3\}$ רגולרית ולכן ב-$R$; $R$ סגורה לחיתוך. בפועל: על קלט $w$ – אם $|w| \le 3$ דחה, אחרת הרץ את המכריע של $L$ והחזר את התשובה ההפוכה.""",
  r"""**הפרכת ב, ג, ד:** $A(L)$ תמיד ניתנת להכרעה."""),
  note="Printed set: 'A(L) = { w | w ∉ L וגם |w| > 3 }' — condition moved to a (*) line."),

Q(10, "np", "איזו מהטענות הבאות נכונה?",
  opts(r"קיימת מכונת טיורינג לא-דטרמיניסטית $M$ כך שמתקיים: $L(M) \notin R$",
       r"קיימת מכונת טיורינג לא-דטרמיניסטית $M$ כך שמתקיים: $L(M) \notin RE$",
       r"לכל מכונת טיורינג לא-דטרמיניסטית $M$ מתקיים: $L(M) \notin P$",
       r"לכל מכונת טיורינג לא-דטרמיניסטית $M$ מתקיים: $L(M) \notin NP$"),
  "a", ex(
  r"""**הוכחת א:** כל מ"ט דטרמיניסטית היא בפרט לא-דטרמיניסטית; המכונה האוניברסלית $U$ מקיימת $L(U) = A_{TM} \notin R$.""",
  r"""**הפרכת ב:** לכל מ"ט לא-דטרמיניסטית יש מ"ט דטרמיניסטית שקולה, ולכן תמיד $L(M) \in RE$.""",
  r"""**הפרכת ג, ד:** מכונה לא-דטרמיניסטית שדוחה מיד כל קלט מקיימת $L(M) = \emptyset \in P \subseteq NP$.""")),

Q(11, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{a^n b^{n+1} c^{n+2} \mid n \ge 0\}$$"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "a", ex(
  r"""**הוכחת א:** מכריע: בודקים שהקלט מהצורה $a^* b^* c^*$, סופרים את מספרי ה-$a$, ה-$b$ וה-$c$ ובודקים ש-$\#b = \#a + 1$ ו-$\#c = \#a + 2$. המכונה תמיד עוצרת, לכן $L \in R$ (ובפרט $L, \overline{L} \in RE$, ולכן ב, ג, ד שגויות).""")),

Q(12, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M, w\rangle \mid (*)\}$$"
  r"(*): $M$ היא מכונת טיורינג וגם החישוב של $M$ על $w$ עוצר במצב מקבל על ידי ביצוע של 3 צעדי חישוב או יותר" "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4_SW, "a", ex(
  r"""**$L \in RE$:** על קלט $\langle M, w\rangle$ מסמלצים את $M$ על $w$ וסופרים צעדים; אם $M$ מקבלת אחרי 3 צעדים או יותר – קבל, אם עצרה אחרת – דחה.""",
  r"""**$L \notin R$:** רדוקציה $A_{TM} \le_m L$: $f(\langle M, w\rangle) = \langle M', w\rangle$ כאשר $M'$ מבצעת תחילה 4 צעדי סרק (ימינה, שמאלה, ימינה, שמאלה – הראש חוזר למקום והסרט לא משתנה) ואז מריצה את $M$ על הקלט. $M'$ מקבלת את $w$ אם"ם $M$ מקבלת את $w$, ואם היא מקבלת – זה קורה אחרי יותר מ-3 צעדים. לכן $\langle M, w\rangle \in A_{TM} \Leftrightarrow f(\langle M, w\rangle) \in L$, ו-$A_{TM} \notin R$ נותן $L \notin R$.""",
  r"""לכן התשובה היא א ($RE \setminus R$); ב, ג, ד נפסלות."""),
  note="Options 1-2 printed in the order (RE\\R, R, ...). Printed stem condition in a 3-line brace; moved to (*)."),

Q(13, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M_1, M_2\rangle \mid \varepsilon \in L(M_1) \cup L(M_2)\}$$"
  "איזו מהטענות הבאות נכונה?",
  DEC4_SW, "a", ex(
  r"""**$L \in RE$:** מריצים את $M_1$ ואת $M_2$ על $\varepsilon$ במקביל (צעד-צעד לסירוגין) ומקבלים ברגע שאחת מהן מקבלת.""",
  r"""**$L \notin R$:** רדוקציה $A_{TM} \le_m L$: $f(\langle M, w\rangle) = \langle K_{M,w}, K_{M,w}\rangle$ כאשר $K_{M,w}$ על כל קלט מריצה את $M$ על $w$ ומחזירה את תשובתה. $\varepsilon \in L(K_{M,w})$ אם"ם $M$ מקבלת את $w$.""",
  r"""לכן התשובה היא א ($RE \setminus R$); ב, ג, ד נפסלות."""),
  note="Options 1-2 printed in the order (RE\\R, R, ...)."),

Q(14, "npc", "איזו מהטענות הבאות נכונה?",
  opts(ALLF,
       r"יתכן שמתקיים: $IS \in P$ וגם $CLIQUE \notin P$",
       r"יתכן שמתקיים: $CLIQUE \in P$ וגם $IS \notin P$",
       r"יתכן שמתקיים: $IS \notin NP$ וגם $CLIQUE \notin NP$"),
  "a", ex(
  r"""**הוכחת א:** $CLIQUE, IS \in NPC$.""",
  r"""**הפרכת ב:** אם $IS \in P$ אז, כיוון ש-$IS \in NPC$, מתקיים $P = NP$ ולכן $CLIQUE \in NP = P$ (ישירות: $CLIQUE \le_p IS$ על ידי מעבר לגרף המשלים).""",
  r"""**הפרכת ג:** סימטרי – $IS \le_p CLIQUE$.""",
  r"""**הפרכת ד:** ידוע ש-$CLIQUE, IS \in NP$ (הקליקה/הקבוצה הבלתי תלויה היא עד שנבדק בזמן פולינומי).""",
  r"""לכן ב, ג, ד שגויות ו-א נכונה.""")),
]

contexts = {
  "blk": {"kind": "text", "title": "הגדרות לשאלות 15–18",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
                  r"$$H^*_{TM} = \{\langle M\rangle \mid (*)\}$$"
                  "(*): $M$ היא מכונת טיורינג שעוצרת על כל קלט\n"
                  "כעת נגדיר שתי פונקציות:\n"
                  r"$$f(x) = x$$"
                  r"$$g(\langle M\rangle) = \langle M_g\rangle$$"
                  r"כאשר $M_g$ היא מ" '"' r"ט אשר בהינתן קלט $y$: היא מריצה את $M$ על $y$. אם ההרצה הנ" '"' r"ל של $M$ על $y$ עצרה (במצב מקבל או דוחה), אז $M_g$ עוצרת במצב מקבל." "\n"
                  "קבעו לכל אחת מהטענות הבאות האם היא נכונה או לא:"},
}
NO_YES = opts("לא נכון", "נכון")
YES_NO = opts("נכון", "לא נכון")

questions += [
Q(15, "mapping_reductions", r"$f$ היא רדוקציה $H^*_{TM} \le_m \Sigma^*$.", NO_YES, "a", ex(
  r"""**לא נכון:** $f$ היא הזהות, ולכן היא רדוקציה $H^*_{TM} \le_m \Sigma^*$ רק אם $H^*_{TM} = \Sigma^*$. אבל למשל קידוד של מכונה שלא עוצרת על אף קלט אינו ב-$H^*_{TM}$ (ובכלל – רק $\Sigma^*$ עצמה ניתנת לרדוקציה ל-$\Sigma^*$)."""),
  contextId="blk"),
Q(16, "mapping_reductions", r"$f$ היא רדוקציה $ALL_{TM} \le_m H^*_{TM}$.", NO_YES, "a", ex(
  r"""**לא נכון:** הזהות היא רדוקציה רק אם $ALL_{TM} = H^*_{TM}$. מכונה $M$ שדוחה מיד כל קלט עוצרת על כל קלט, לכן $\langle M\rangle \in H^*_{TM}$, אבל $L(M) = \emptyset$ ולכן $\langle M\rangle \notin ALL_{TM}$."""),
  contextId="blk"),
Q(17, "mapping_reductions", r"$g$ היא רדוקציה $H^*_{TM} \le_m ALL_{TM}$.", YES_NO, "a", ex(
  r"""**נכון:** $g$ ניתנת לחישוב (רק בונים את הקידוד של $M_g$). $L(M_g) = \{y \mid M \text{ halts on } y\}$.""",
  r"""אם $\langle M\rangle \in H^*_{TM}$ אז $M$ עוצרת על כל $y$, לכן $M_g$ מקבלת כל $y$ ו-$\langle M_g\rangle \in ALL_{TM}$.""",
  r"""אם $\langle M\rangle \notin H^*_{TM}$ יש $y$ ש-$M$ לא עוצרת עליו, ואז גם $M_g$ לא עוצרת עליו – $y \notin L(M_g)$ ולכן $\langle M_g\rangle \notin ALL_{TM}$."""),
  contextId="blk"),
Q(18, "mapping_reductions", r"$g$ היא רדוקציה $ALL_{TM} \le_m H^*_{TM}$.", NO_YES, "a", ex(
  r"""**לא נכון:** ניקח $M$ שדוחה מיד כל קלט: $\langle M\rangle \notin ALL_{TM}$, אבל $M$ עוצרת על כל קלט ולכן $M_g$ מקבלת כל קלט (ובפרט עוצרת תמיד), כלומר $g(\langle M\rangle) = \langle M_g\rangle \in H^*_{TM}$. תנאי הרדוקציה מופר."""),
  contextId="blk"),
]

exam = {
  "examCode": "24B-B",
  "examLabel": "2024 סמסטר ב מועד ב",
  "year": 2024,
  "examDate": "1.8.2024",
  "sourceFile": "מבחנים/2024/סמסטר ב/2024-08-01-Exam-חישוביות-2024-moedB-טופס-0.pdf",
  "keyFile": "none — answers solved (stage 1 of tools/SOLVE_GUIDE.md); form-0 first-option used only as partial evidence",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 19))

def _fix(x):
    """raw strings keep the backslash of \\" (e.g. in א\\"ב) -> strip it."""
    if isinstance(x, str): return x.replace('\\"', '"')
    if isinstance(x, list): return [_fix(v) for v in x]
    if isinstance(x, dict): return {k: _fix(v) for k, v in x.items()}
    return x
exam = _fix(exam)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
