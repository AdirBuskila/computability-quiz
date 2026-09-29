# -*- coding: utf-8 -*-
"""Generator for tools/raw/25A-A.json (2025 סמסטר א מועד א, 6.2.2025, ד"ר מרק טרכטנברוט).
Transcribed by hand from the rendered pages of `מבחנים/2025/סמ א מועד א 6.2.25.pdf`
(10 pages; p1 = cover with OMR sheet, p10 blank). NO answer key exists: every answer below is
SOLVED (stage 1 of tools/SOLVE_GUIDE.md) — answerSource "solved", official False.
Run: PYTHONUTF8=1 py tools/gen/gen_25A-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25A-A.json"
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

NONE = "אף אחת מהתשובות האחרות אינה נכונה"

def J(*paras):
    return "\n".join(paras)

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "solved", "official": False,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

questions = [
Q(1, "closure",
  "נתבונן בשתי הטענות הבאות:\n"
  "(1) משפחת שפות ש**לא** ניתנות לקבלה סגורה למשלים\n"
  "(2) משפחת שפות ש**לא** ניתנות לקבלה סגורה לאיחוד\n"
  "איזה מהסעיפים הבאים נכון:",
  opts("שתי הטענות (1), (2) הן נכונות.",
       "שתי הטענות (1), (2) הן לא נכונות.",
       "טענה (1) נכונה וגם טענה (2) לא נכונה.",
       "טענה (2) נכונה וגם טענה (1) לא נכונה."),
  "b",
  J(r"""**טענה (1) לא נכונה:** $\overline{A_{TM}} \notin RE$ אבל המשלימה שלה $A_{TM} \in RE$.""",
    r"""**טענה (2) לא נכונה:** נגדיר $L_1 = \{0w \mid w \in \overline{A_{TM}}\} \cup \{1w \mid w \in A_{TM}\}$ ו-$L_2 = \{0w \mid w \in A_{TM}\} \cup \{1w \mid w \in \overline{A_{TM}}\}$. שתיהן לא ניתנות לקבלה (אחרת $\overline{A_{TM}} \le_m L_i$ ע"י $w \mapsto 0w$ או $w \mapsto 1w$ הייתה נותנת $\overline{A_{TM}} \in RE$), אבל $L_1 \cup L_2 = 0\Sigma^* \cup 1\Sigma^*$ – שפה ניתנת להכרעה."""),
  note="'לא' is bold+underlined in the source; rendered bold."),

Q(2, "mapping_reductions",
  r"תהי שפה $L$ כלשהי, כך שמתקיימת הרדוקציה $H_{TM} \le_m L$." "\n"
  "איזה מהסעיפים הבאים נכון:",
  opts("יתכן ש-$L$ שייכת ל-$P$",
       "יתכן ש-$L$ שייכת ל-$NP$, אבל לא שייכת ל-$P$",
       "יתכן ש-$L$ שפה $NP$-שלמה",
       NONE),
  "d",
  J(r"""**הוכחת ד:** $H_{TM} \notin R$. לפי משפט הרדוקציה, אם $L \in R$ אז גם $H_{TM} \in R$ – סתירה. לכן $L \notin R$.""",
    r"""**הפרכת א, ב, ג:** $P \subseteq NP \subseteq R$ וכל שפה $NP$-שלמה שייכת ל-$NP$, ולכן אף אחת מהאפשרויות לא יכולה להתקיים עבור $L \notin R$.""")),

Q(3, "classification",
  "נתונה השפה $L$ הבאה:\n"
  r"$$L = \{\langle M\rangle \mid (*)\}$$"
  "(*): $M$ היא מכונת טיורינג דטרמיניסטית, ומתקיים: $M$ מקבלת לפחות מילה אחת באורך זוגי, וגם $M$ מקבלת לפחות מילה אחת באורך אי-זוגי\n"
  "איזה מהסעיפים הבאים נכון:",
  opts("השפה $L$ ניתנת להכרעה",
       "השפה $L$ ניתנת לקבלה, אבל לא ניתנת להכרעה",
       "השפה $L$ לא ניתנת לקבלה, אבל המשלים שלה היא שפה שניתנת לקבלה",
       NONE),
  "b",
  J(r"""**$L \in RE$:** בהינתן $\langle M\rangle$ נריץ את $M$ במקביל (dovetailing) על כל המילים – בשלב $i$ נריץ $i$ צעדים על $i$ המילים הראשונות. נקבל ברגע שנמצאו מילה זוגית ומילה אי-זוגית ש-$M$ מקבלת.""",
    r"""**$L \notin R$:** רדוקציה $A_{TM} \le_m L$: $f(\langle M,w\rangle) = \langle M'\rangle$ כאשר $M'$ על קלט $x$ מתעלמת מ-$x$, מריצה את $M$ על $w$ ומקבלת אם $M$ קיבלה. אם $M$ מקבלת את $w$ אז $L(M') = \Sigma^*$ ובפרט יש בה מילים באורך זוגי ואי-זוגי; אחרת $L(M') = \emptyset$. לכן $L \notin R$ והתשובה ב (ולכן גם ג, ד לא נכונות – ג אומרת $L \notin RE$)."""),
  note="Printed as one set-builder spanning two lines: 'L = { <M> | M היא מכונת טיורינג דטרמיניסטית, ומתקיים: M מקבלת לפחות מילה אחת באורך זוגי, וגם M מקבלת לפחות מילה אחת באורך אי-זוגי }' — condition moved to a (*) line."),

Q(4, "poly_reductions",
  r"נתונות שפות $A, B, C$ כך שמתקיים $A \le_p B$ וגם $B \le_p C$." "\n"
  "איזה מהסעיפים הבאים נכון:",
  opts(r"מתקיים $\overline{A} \le_m \overline{C}$ וגם מתקיים $\overline{A} \le_p \overline{C}$",
       r"מתקיים $\overline{A} \le_m \overline{C}$, אבל לא מתקיים $\overline{A} \le_p \overline{C}$",
       r"מתקיים $\overline{A} \le_p \overline{C}$, אבל לא מתקיים $\overline{A} \le_m \overline{C}$",
       NONE),
  "a",
  J(r"""**הוכחת א:** מטרנזיטיביות הרדוקציה הפולינומית $A \le_p C$ (הרכבת שתי פונקציות פולינומיות היא פולינומית). אותה פונקציה $f$ מקיימת $x \in A \Leftrightarrow f(x) \in C$, כלומר $x \in \overline{A} \Leftrightarrow f(x) \in \overline{C}$, ולכן $\overline{A} \le_p \overline{C}$. כל רדוקציה פולינומית היא בפרט רדוקציית מיפוי, ולכן גם $\overline{A} \le_m \overline{C}$.""",
    r"""**הפרכת ב, ג:** כל אחת טוענת שאחת מהרדוקציות לא מתקיימת – בסתירה להוכחה."""),
  note="All four complements verified at 4x zoom (overlines on A and C in every option)."),

Q(5, "npc",
  "איזה מהסעיפים הבאים נכון:",
  opts(r"הרדוקציה $PRIME \le_p 3SAT$ מתקיימת רק בתנאי $P = NP$",
       r"אם מתקיימת הרדוקציה $3SAT \le_p PRIME$, אז $P \ne NP$",
       r"אם $PRIME$ היא שפה $NP$-שלמה, אז השפה $3SAT$ שייכת ל-$P$",
       NONE),
  "c",
  J(r"""**הוכחת ג:** $PRIME \in P$. אם $PRIME$ היא $NP$-שלמה אז $P \cap NPC \ne \emptyset$ ולכן $P = NP$, ובפרט $3SAT \in NP = P$.""",
    r"""**הפרכת א:** $PRIME \in P$ ו-$3SAT$ לא טריוויאלית, ולכן $PRIME \le_p 3SAT$ מתקיימת ללא שום תנאי (הפונקציה מכריעה את $PRIME$ בזמן פולינומי ומחזירה מילה קבועה ב-$3SAT$ או מחוץ לה).""",
    r"""**הפרכת ב:** אם $3SAT \le_p PRIME$ אז, כיוון ש-$PRIME \in P$, נקבל $3SAT \in P$ ולכן $P = NP$ – ההפך מהמסקנה הנטענת."""),
  note="Printed 'PRIME' plain in option ג and italic elsewhere; same language."),

Q(6, "tm",
  "תהי $L$ שפה הניתנת להכרעה, ותהי $M$ מכונת טיורינג לא-דטרמיניסטית עם 3 סרטים המכריעה את $L$.\n"
  "איזה מהסעיפים הבאים נכון:",
  opts("קיימת מכונה דטרמיניסטית עם 2 סרטים שמקבלת את $L$, אבל לא קיימת מכונה דטרמיניסטית עם 2 סרטים שמכריעה את $L$",
       r"קיימת מכונה דטרמיניסטית עם סרט אחד שמקבלת את $\overline{L}$",
       r"לא ידוע האם קיימת מכונה דטרמיניסטית עם סרט אחד המכריעה את $\overline{L}$, כי לא ידוע האם מתקיים $P = NP$",
       NONE),
  "b",
  J(r"""**הוכחת ב:** $L \in R$ ולכן גם $\overline{L} \in R$ (מחליפים בין מצב מקבל למצב דוחה במכריע של $L$). מכונה בסיסית (דטרמיניסטית, סרט אחד) המכריעה את $\overline{L}$ היא בפרט מקבלת את $\overline{L}$.""",
    r"""**הפרכת א:** $L \in R$ ולכן קיימת מכונה דטרמיניסטית בסיסית (ובפרט עם 2 סרטים) המכריעה את $L$.""",
    r"""**הפרכת ג:** קיום מכריע ל-$\overline{L}$ נובע מכך ש-$\overline{L} \in R$, ללא קשר לשאלת $P$ מול $NP$ (שעוסקת בזמן ריצה בלבד).""")),

Q(7, "closure",
  r"יהיו $A, B$ שפות כך שמתקיים: $A \in RE \setminus R$ וגם $B \in R$." "\n"
  "איזו מהטענות הבאות היא טענה נכונה:",
  opts(r"בהכרח $B \setminus A \in RE \setminus R$",
       r"יתכן $B \setminus A \in R$",
       r"יתכן $\overline{B} = A$",
       NONE),
  "b",
  J(r"""**הוכחת ב:** עבור $B = \emptyset$ (ו-$A = A_{TM}$) מתקיים $B \setminus A = \emptyset \in R$.""",
    r"""**הפרכת א:** אותה דוגמה.""",
    r"""**הפרכת ג:** $R$ סגורה למשלים ולכן $\overline{B} \in R$, בעוד ש-$A \notin R$. לכן $\overline{B} \ne A$.""")),

Q(8, "decidability",
  "נתונות שפה $L$ הניתנת להכרעה ומכונת טיורינג $M$ כך שמתקיים $L(M) = L$.\n"
  "איזו מהטענות הבאות נכונה:",
  opts("$M$ היא בהכרח מכונה דטרמיניסטית",
       "אם $M$ היא מכונה לא-דטרמיניסטית, אז מתקיים $P = NP$",
       r"אם $M$ עוצרת על כל קלט, אז $\overline{L} \in RE \setminus R$",
       NONE),
  "d",
  J(r"""**הפרכת א:** לכל שפה ב-$R$ קיימת גם מכונה לא-דטרמיניסטית המקבלת אותה (כל מכונה דטרמיניסטית היא מקרה פרטי של לא-דטרמיניסטית).""",
    r"""**הפרכת ב:** קיום מכונה לא-דטרמיניסטית שמקבלת שפה כריעה לא אומר דבר על היחס בין $P$ ל-$NP$ (לכל שפה כריעה יש מכונה כזו); המסקנה $P = NP$ לא נובעת מהנתון.""",
    r"""**הפרכת ג:** $L \in R$ ולכן $\overline{L} \in R$, בפרט $\overline{L} \notin RE \setminus R$.""",
    "לכן אף אחת מהטענות א–ג אינה נכונה."),
  note="Option ב is refuted as 'does not follow' (its truth would hinge on the open P vs NP question) — the course's convention for such claims."),

Q(9, "classification",
  "נתונה השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid (*)\}$$"
  "(*): המכונה $M$ מקבלת את כל מילים מהצורה $0^n1^n$, ורק אותן\n"
  "איזה מהסעיפים הבאים נכון:",
  opts(r"השפה $\{0^n1^n\}$ שייכת ל-$P$, ולכן גם $L$ שייכת ל-$P$",
       "השפה $L$ שייכת ל-$NP$, אבל לא ידוע האם היא שייכת ל-$P$",
       "קיים אנומרטור של שפה $L$",
       NONE),
  "d",
  J(r"""**$L \notin RE$:** רדוקציה $\overline{H_{TM}} \le_m L$: $f(\langle M,w\rangle) = \langle M'\rangle$ כאשר $M'$ על קלט $x$: אם $x$ מהצורה $0^n1^n$ קבל; אחרת הרץ את $M$ על $w$ וקבל. אם $M$ לא עוצרת על $w$ אז $L(M') = \{0^n1^n\}$; אחרת $L(M') = \Sigma^*$.""",
    r"""**הפרכת א, ב:** $P \subseteq NP \subseteq R$ ו-$L \notin R$.""",
    r"""**הפרכת ג:** לשפה יש אנומרטור אם"ם היא ב-$RE$, ו-$L \notin RE$."""),
  note="Printed as 'L = { <M> | המכונה M מקבלת את כל מילים מהצורה 0^n1^n , ורק אותן }' — condition moved to a (*) line."),

Q(10, "tm",
  r"נסמן $M$ – מכונת טיורינג בסיסית (דטרמיניסטית, עם סרט אחד), ומתקיים: $L(M) = \emptyset$." "\n"
  "איזה מהסעיפים הבאים נכון:",
  opts("ב-$M$ אין אף מצב מקבל",
       "לא קיים אנומרטור עבור $L(M)$",
       "$M$ לא עוצרת על אף קלט",
       NONE),
  "d",
  J(r"""**הפרכת א:** לפי ההגדרה הפורמלית לכל מכונת טיורינג יש מצב מקבל $q_{acc}$; $L(M) = \emptyset$ רק אומר שאף ריצה לא מגיעה אליו.""",
    r"""**הפרכת ב:** אנומרטור שלא מדפיס אף מילה (למשל נכנס מיד ללולאה) מונה את $\emptyset$.""",
    r"""**הפרכת ג:** מכונה שדוחה מיד כל קלט עוצרת על כל קלט ו-$L(M) = \emptyset$.""")),

Q(11, "npc",
  "תהי $L$ שפה לא טריוויאלית כלשהי.\n"
  "איזו מהטענות הבאות נכונה:",
  opts(r"אם $L$ שייכת ל-$NP$, אז יתכן ש-$L$ ניתנת לקבלה אבל $\overline{L}$ לא ניתנת לקבלה",
       "אם מתקיים $P = NP$, אז $L$ בהכרח שייכת ל-$P$",
       r"אם מתקיים $P \ne NP$, אז $L$ היא בהכרח שפה $NP$-שלמה",
       NONE),
  "d",
  J(r"""**הפרכת א:** $NP \subseteq R$, ולכן אם $L \in NP$ אז $L \in R$ וגם $\overline{L} \in R \subseteq RE$.""",
    r"""**הפרכת ב:** $L = A_{TM}$ לא טריוויאלית ו-$A_{TM} \notin R$, ולכן $A_{TM} \notin P$ בלי קשר ל-$P = NP$.""",
    r"""**הפרכת ג:** אותה דוגמה – $A_{TM} \notin NP$ ולכן אינה $NP$-שלמה.""")),

Q(12, "npc",
  "רוצים להוכיח ששפה $L$ היא שפה $NP$-שלמה.\n"
  "מה מהבאים יכול להוות הוכחה תקפה?",
  opts(r"מתקיים $L \le_p SAT$",
       r"מתקיים $SAT \le_p L$",
       r"קיימות שפות $L_1, L_2$ השייכות ל-$NP$, כך שמתקיים $L = L_1 \cup L_2$ וגם $3SAT \le_p L$",
       NONE),
  "c",
  J(r"""**הוכחת ג:** $NP$ סגורה לאיחוד (מכונה לא-דטרמיניסטית מנחשת לאיזו מהשפות לבדוק), ולכן $L \in NP$. כמו כן $3SAT$ היא $NP$-שלמה ו-$3SAT \le_p L$, ולכן מטרנזיטיביות כל שפה ב-$NP$ מתמפה פולינומית ל-$L$. שני התנאים של $NP$-שלמות מתקיימים.""",
    r"""**הפרכת א:** מראה רק ש-$L \in NP$, לא שהיא $NP$-קשה (למשל $L = \{0\}$).""",
    r"""**הפרכת ב:** מראה רק ש-$L$ היא $NP$-קשה, לא ש-$L \in NP$. למשל $L = A_{TM}$: $SAT \le_p A_{TM}$ (ממפים את $\phi$ לזוג $\langle M_\phi, \varepsilon\rangle$ כאשר $M_\phi$ עוברת על כל ההשמות ומקבלת אם אחת מהן מספקת – כתיבת הקידוד פולינומית), אבל $A_{TM} \notin NP$."""),
  note="Printed 'L1, L2' / 'L = L1 ∪ L2' with plain digits; rendered as subscripts."),

Q(13, "npc",
  "נתונות שתי מחלקות של שפות:\n"
  r"$$A = \{L \mid (*)\}$$"
  r"(*): $CLIQUE \le_p L$ ומתקיים $L \in NP$" "\n"
  r"$$B = \{L \mid (**)\}$$"
  r"(**): $Composite \le_m L$ וגם $|L| > 100$" "\n"
  "איזו מהטענות הבאות היא טענה נכונה:",
  opts(("math", "A = B"), ("math", r"A \supset B"), ("math", r"A \subset B"), NONE),
  "c",
  J(r"""$A = NPC$. $Composite \in R$ ולכן $Composite \le_m L$ לכל $L$ לא טריוויאלית, ולא ל-$\emptyset$ או $\Sigma^*$; לכן $B$ = כל השפות הלא טריוויאליות עם יותר מ-100 מילים.""",
    r"""אם $P \ne NP$: כל שפה $NP$-שלמה אינה ב-$P$ ולכן אינסופית ולא טריוויאלית, כך ש-$A \subseteq B$, וההכלה ממש ($A_{TM} \in B \setminus A$) – תשובה ג.""",
    r"""אם $P = NP$: $\{0\} \in A$ (כל שפה לא טריוויאלית ב-$P$ היא $NP$-שלמה) אבל $\{0\} \notin B$, ו-$A_{TM} \in B \setminus A$ – תשובה ד."""),
  confidence="low",
  hold="Answer depends on the open P vs NP question: if P≠NP then A=NPC ⊂ B (ג); if P=NP a finite language like {0} is NP-complete but not in B, so no relation holds (ד). Intended answer probably ג.",
  note="Printed 'A = { L | CLIQUE ≤p L ומתקיים L ∈ NP }' and 'B = { L | Composite ≤m L וגם |L| > 100 }' — conditions moved to (*)/(**) lines."),

Q(14, "poly_reductions",
  "נתונה שפה הבאה:\n"
  r"$$STAR = \{\langle G, k\rangle \mid (*)\}$$"
  "(*): בגרף הלא מכוון $G$ קיימת קבוצת צמתים $A$ בגודל $k$, ובה צומת $v$ כך ש: $v$ מחובר בקשת לכל צומת אחר ב-$A$, ואין קשתות נוספות בין הצמתים של $A$\n"
  r"ידוע ש-$STAR \in NP$, ורוצים להוכיח ש-$STAR \in NPC$ על ידי הגדרת הרדוקציה $IS \le_p STAR$." "\n"
  "**תזכורת:** השפה Independent_Set / $IS$ ידועה כ-$NP$-שלמה, ולכן לפי הרדוקציה גם $STAR$ חייבת להיות $NP$-שלמה.\n"
  r"מגדירים רדוקציה $IS \le_p STAR$ כדלקמן:" "\n"
  r"$$f(\langle G, k\rangle) = \langle G', k\rangle$$"
  "כאשר:\n"
  "- אם ב-$G$ יש קבוצת צמתים $A$ בלתי תלויה בגודל $k$, אז $G'$ מתקבל על ידי הוספה ל-$G$ צומת $v$ חדש המחובר בקשת לכל אחד מהצמתים ב-$A$\n"
  "- אחרת $G'$ זהה ל-$G$.\n"
  "האם הוכחה הזאת תקפה? סמנו את התשובה הנכונה:",
  opts("לא, כי $f$ לא ניתנת לחישוב",
       "לא, כי לא מובטח שחישוב של $f$ ניתן לבצע בזמן פולינומי",
       r"לא, כי לא מובטח שמתקיים היחס $f(\langle G,k\rangle) \in IS \leftrightarrow \langle G',k\rangle \in STAR$",
       "כן, כי פונקציה $f$ עומדת בכל הדרישות של רדוקציה פולינומית"),
  "b",
  J(r"""**ב נכונה:** חישוב $f$ דורש להכריע אם ב-$G$ יש קבוצה בלתי תלויה בגודל $k$ – בעיה $NP$-שלמה – ולכן לא מובטח זמן פולינומי (אלא אם $P = NP$).""",
    r"""**אבל גם תנאי הנכונות נכשל:** עבור $G$ = שני צמתים המחוברים בקשת ו-$k = 2$: אין ב-$G$ קבוצה בלתי תלויה בגודל 2, ולכן $G' = G$; אבל $\langle G, 2\rangle \in STAR$ (הצמתים עצמם, $v$ אחד מהם). כך ש-$\langle G,k\rangle \notin IS$ ו-$f(\langle G,k\rangle) \in STAR$."""),
  confidence="low",
  hold="Two refutations apply: f is not guaranteed polytime (ב), AND the correctness condition fails (e.g. G = single edge, k=2: G∉IS but G'=G∈STAR), which is what ג tries to say — but ג's printed condition 'f(<G,k>) ∈ IS ↔ <G',k> ∈ STAR' is garbled. Intended answer probably ב.",
  note="Printed STAR definition spans three lines ('- v מחובר קשת לכל צומת אחר ב-A', '- אין קשתות נוספים בין הצמתים של A') — merged into the (*) line."),

Q(15, "mapping_reductions",
  "נתונה שפה $L$:\n"
  r"$$L = \{\langle M\rangle \mid L(M) \subseteq PALINDROMS\}$$"
  "(כאן $PALINDROMS$ היא שפת כל מחרוזות-פלינדרומים).\n"
  r"מנסים להוכיח ש-$L$ לא ניתנת לקבלה בעזרת רדוקציה $\overline{H_{TM}} \le_m L$. לצורך זה מגדירים פונקציה $f$ כדלקמן:" "\n"
  r"$$f(\langle M, w\rangle) = \langle Q\rangle$$"
  "כאשר $Q$ היא מכונת טיורינג הבאה:\n"
  "`Q(x) {`\n"
  r"`    if x ∈ PALINDROMS`" "\n"
  "`    then {ACCEPT}`\n"
  "`    else {M(w); ACCEPT}`\n"
  "`}`\n"
  "איזו מהטענות הבאות נכונה:",
  opts("פונקציה $f$ אכן עומדת בכל הדרישות של רדוקציה",
       "$f$ לא מהווה רדוקציה, כי היא לא ניתנת לחישוב",
       r"$f$ לא מהווה רדוקציה, כי לא מתקיים: $\langle M,w\rangle \notin \overline{H_{TM}} \rightarrow \langle Q\rangle \notin L$",
       r"$f$ לא מהווה רדוקציה, כי לא מתקיים: $\langle M,w\rangle \in \overline{H_{TM}} \rightarrow \langle Q\rangle \in L$"),
  "a",
  J(r"""**הוכחת א:** $f$ ניתנת לחישוב – היא רק כותבת את הקידוד של $Q$ (לא מריצה את $M$).""",
    r"""אם $\langle M,w\rangle \in \overline{H_{TM}}$ ($M$ לא עוצרת על $w$): $Q$ מקבלת בדיוק את הפלינדרומים (על שאר הקלטים היא נתקעת בהרצת $M(w)$), כלומר $L(Q) = PALINDROMS$ ולכן $\langle Q\rangle \in L$.""",
    r"""אם $\langle M,w\rangle \notin \overline{H_{TM}}$ ($M$ עוצרת על $w$): $Q$ מקבלת כל קלט, $L(Q) = \Sigma^* \not\subseteq PALINDROMS$ (למשל $01$), ולכן $\langle Q\rangle \notin L$.""",
    "לכן שני כיווני התנאי מתקיימים, ו-ב, ג, ד לא נכונות."),
  note="Pseudo-code block kept as printed in code spans. Assumes the usual binary alphabet (so Σ* ⊄ PALINDROMS)."),

Q(16, "mapping_reductions",
  "נתון שהשפה $L$ היא $NP$-שלמה.\n"
  "איזו מהטענות הבאות היא טענה נכונה:",
  opts(r"מתקיים $L \le_m \overline{H_{10}}$, אבל לא מתקיים $\overline{L} \le_m \overline{H_{10}}$",
       r"מתקיים $\overline{L} \le_m \overline{H_{10}}$, אבל לא מתקיים $L \le_m \overline{H_{10}}$",
       "כן, מתקיימות שתי הרדוקציות",
       "אף אחת משתי הרדוקציות לא מתקיימת"),
  "c",
  J(r"""**הוכחת ג:** $L \in NP \subseteq R$ ולכן גם $\overline{L} \in R$. $L$ לא טריוויאלית (לא ניתן לבצע רדוקציה מ-$SAT$ ל-$\emptyset$ או ל-$\Sigma^*$). $\overline{H_{10}}$ לא טריוויאלית ($H_{10} \in RE \setminus R$). כל שפה ב-$R$ ניתנת לרדוקציית מיפוי לכל שפה לא טריוויאלית, ולכן גם $L \le_m \overline{H_{10}}$ וגם $\overline{L} \le_m \overline{H_{10}}$.""",
    "**הפרכת א, ב, ד:** כל אחת טוענת שלפחות אחת מהרדוקציות לא מתקיימת.")),

Q(17, "tm",
  "נתונה מכונה $M$ לא-דטרמיניסטית.\n"
  "איזו מהטענות הבאות היא טענה נכונה:",
  opts("אם $M$ מקבלת כל קלט, אז כל מסלולי חישוב של $M$ על כל הקלטים בהכרח עוצרים",
       "אם חלק מהחישובים של $M$ על קלט $w$ עוצרים במצב REJECT ואילו כל שאר החישובים של $M$ על $w$ לא עוצרים, אז $M$ דוחה את $w$",
       "אם קיים קלט $w$ כך שלפחות אחד החישובים של $M$ על $w$ לא עוצר, אז השפה $L(M)$ לא ניתנת להכרעה",
       NONE),
  "d",
  J(r"""**הפרכת א:** מכונה שבכל קלט מנחשת: באחד הענפים מקבלת מיד ובענף אחר נכנסת ללולאה. היא מקבלת כל קלט אבל יש לה מסלולים שלא עוצרים.""",
    r"""**הפרכת ב:** מכונה לא-דטרמיניסטית דוחה את $w$ רק אם **כל** מסלולי החישוב שלה על $w$ עוצרים במצב דוחה. כאן יש מסלולים שלא עוצרים, כך ש-$w \notin L(M)$ אבל $M$ לא דוחה את $w$ (היא לא עוצרת עליו).""",
    r"""**הפרכת ג:** המכונה מהפרכת א מקבלת את $\Sigma^*$, שפה ניתנת להכרעה, למרות שיש לה מסלולים שלא עוצרים.""",
    "לכן אף אחת מהטענות א–ג אינה נכונה."),
  note="Answer relies on the course (Sipser) definition: an NTM rejects w only when every branch halts in reject."),

Q(18, "npc",
  "תהיינה $A, B$ שתי שפות שונות זו מזו.\n"
  "איזו מהטענות הבאות נכונה?",
  opts(r"אם מתקיים $A \le_p B$ וגם $B \le_p A$ אז בהכרח שתי השפות $A, B$ הן $NP$-שלמות",
       r"אם מתקיים $A \le_p B$ וגם $B \le_p A$ אז בהכרח שתי השפות $A, B$ שייכות ל-$P$",
       r"אם מתקיים $A \le_p B$ וגם $B \le_p A$ אז בהכרח מתקיים $P = NP$",
       NONE),
  "d",
  J(r"""**הפרכת א:** $A = \{0\}$, $B = \{1\}$ – שתי שפות שונות ב-$P$ ולא טריוויאליות, ולכן $A \le_p B$ ו-$B \le_p A$. הן לא $NP$-שלמות אלא אם $P = NP$, כך שהמסקנה לא נובעת בהכרח.""",
    r"""**הפרכת ב:** $A = SAT$, $B = 3SAT$ – שתיהן $NP$-שלמות ולכן רדוקציה פולינומית קיימת בשני הכיוונים, אבל לא ידוע שהן ב-$P$ (זה היה גורר $P = NP$).""",
    r"""**הפרכת ג:** הדוגמה של א מקיימת את ההנחה ללא שום השלכה על היחס בין $P$ ל-$NP$.""",
    "לכן אף אחת מהטענות א–ג אינה נכונה בהכרח.")),
]

exam = {
  "examCode": "25A-A",
  "examLabel": "2025 סמסטר א מועד א",
  "year": 2025,
  "examDate": "6.2.2025",
  "sourceFile": "מבחנים/2025/סמ א מועד א 6.2.25.pdf",
  "keyFile": "none — answers solved (stage 1, tools/SOLVE_GUIDE.md), pending blind re-solve",
  "contexts": {},
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 19))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
