# -*- coding: utf-8 -*-
"""Generator for tools/raw/SAMP-1.json. Source: `מבחנים/מבחנים לדוגמה/ בחינה לדוגמה.pdf`
(25 Q, NO key). Only the questions that appear VERBATIM (same stem AND same options, same
order) in SAMP-3 (`פתרון מבחן לדוגמא.pdf`, which has a key) are included; their key and
explanation are taken from SAMP-3 by content. The other 18 (Q1-12, Q17-22) are SOLVED per
tools/SOLVE_GUIDE.md (answerSource "solved", official False; Q7 on hold).
Depends on tools/raw/SAMP-3.json -> run gen_SAMP-3.py first.
Run: PYTHONUTF8=1 py tools/gen/gen_SAMP-1.py"""
import json, pathlib, copy

RAW = pathlib.Path(__file__).resolve().parents[1] / "raw"
OUT = RAW / "SAMP-1.json"
s3 = json.loads((RAW / "SAMP-3.json").read_text(encoding="utf-8"))
S3 = {q["num"]: q for q in s3["questions"]}

# SAMP-1 num -> SAMP-3 num (checked on the rendered pages: stem, options and option order identical)
MAP = {13: 6, 14: 7, 15: 8, 16: 9, 23: 1, 24: 13, 25: 12}
SKIPPED = {}  # Q1-12, Q17-22 are SOLVED below (tools/SOLVE_GUIDE.md stage 1; official: False)

questions = []
for n1, n3 in MAP.items():
    q = copy.deepcopy(S3[n3])
    q["num"] = n1
    q["answerSource"] = "solution-pdf"
    q["official"] = True
    q["confidence"] = "high"
    q["note"] = f"key from SAMP-3 Q{n3} (identical stem and options in `פתרון מבחן לדוגמא.pdf`)."
    questions.append(q)

# ---------------------------------------------------------------------------------------------
# SOLVED questions (no key anywhere). Transcribed from the text PDF (overlines checked at zoom:
# A's definition has an overline over L(M); Q20 has \overline{SAT} in the second reduction).
IDS = "abcde"
def opts(*vals):
    out = []
    for i, v in enumerate(vals):
        if isinstance(v, tuple):
            out.append({"id": IDS[i], "type": v[0], "value": v[1]})
        else:
            out.append({"id": IDS[i], "type": "text", "value": v})
    return out

def S(num, topic, question, options, correct, explanation, **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "solved", "official": False,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

def J(*paras):
    return "\n".join(paras)

TF = opts("נכון", "לא נכון")
YN = opts("כן", "לא")
DEC4 = opts(
    "$L$ ניתנת להכרעה.",
    "$L$ ניתנת לקבלה אבל לא ניתנת להכרעה.",
    r"$L$ לא ניתנת לקבלה אבל $\overline{L}$ כן ניתנת לקבלה.",
    r"$L$ לא ניתנת לקבלה וגם $\overline{L}$ לא ניתנת לקבלה.",
)
NONE_REL = "אף תשובה אינה נכונה"
def rel(x, y):
    return opts(("math", f"{x} = {y}"), ("math", rf"{x} \subset {y}"), ("math", rf"{x} \supset {y}"), NONE_REL)

questions += [
S(1, "decidability",
  r"אם $A \subseteq B \subseteq C$ וגם $A, C \in R$, אז $B \in R$",
  TF, "b",
  J(r"""**לא נכון.** דוגמה נגדית: $A = \emptyset$, $C = \Sigma^*$ (שתיהן ב-$R$) ו-$B = A_{TM}$. מתקיים $\emptyset \subseteq A_{TM} \subseteq \Sigma^*$ אבל $A_{TM} \notin R$. הכלה בין שפות לא אומרת דבר על כריעות.""")),

S(2, "npc",
  r"תחת ההנחה $P = NP$: אם $A, B \in NPC$ אז $A \cup B \in NPC$",
  TF, "b",
  J(r"""**לא נכון.** תחת $P = NP$ מתקיים $SAT \in P$ ולכן גם $\overline{SAT} \in P = NP$. כל שפה $L \in NP = P$ ניתנת לרדוקציה פולינומית ל-$\overline{SAT}$ (מכריעים את $L$ בזמן פולינומי ומחזירים מילה קבועה ב-$\overline{SAT}$ או מילה קבועה מחוץ לה), ולכן $SAT, \overline{SAT} \in NPC$.""",
    r"""אבל $SAT \cup \overline{SAT} = \Sigma^*$, ו-$\Sigma^* \notin NPC$: שפה לא טריוויאלית (למשל $SAT$) לא ניתנת לרדוקציה ל-$\Sigma^*$, כי אין מילה מחוץ ל-$\Sigma^*$ שאליה ימופו המילים שאינן בשפה.""")),

S(3, "closure",
  r"אם $A \in RE$ וגם $B \in R$, אז $A - B \in RE - R$",
  TF, "b",
  J(r"""**לא נכון.** דוגמה נגדית: $A = B = \emptyset$ (או $A = B = \Sigma^*$). אז $A - B = \emptyset \in R$, ולכן $A - B \notin RE - R$. (מה שכן נכון הוא $A - B = A \cap \overline{B} \in RE$, אבל לא בהכרח מחוץ ל-$R$.)""")),

S(4, "decidability",
  r"נתון $L(M) \in R$. אזי בהכרח לכל $w \in \Sigma^*$ סדרת הקונפיגורציות של החישוב של $M$ על $w$ היא סופית.",
  TF, "b",
  J(r"""**לא נכון.** העובדה ש**השפה** $L(M)$ כריעה לא אומרת ש**המכונה** $M$ עוצרת על כל קלט. דוגמה נגדית: $M$ שנכנסת ללולאה אינסופית על כל קלט. אז $L(M) = \emptyset \in R$, אבל סדרת הקונפיגורציות של $M$ על כל $w$ אינסופית.""")),

S(5, "decidability",
  r"נתון $L \notin R$. אזי לכל מכונת טיורינג $M$ מתקיים: אם $L(M) = L$ אז קיימת $w \in \Sigma^*$ כך שסדרת הקונפיגורציות של החישוב של $M$ על $w$ היא אינסופית.",
  TF, "a",
  J(r"""**נכון.** נניח בשלילה ש-$L(M) = L$ ו-$M$ עוצרת על כל קלט (לכל $w$ סדרת הקונפיגורציות סופית). אז $M$ מכריעה את $L$, כלומר $L \in R$ – בסתירה לנתון $L \notin R$. לכן יש $w$ שעליה $M$ לא עוצרת.""")),

S(6, "enumerators",
  r"תהינה $A, B$ שפות כך ש-$A \in NPC$ וגם $B \in RE - NPC$. אזי קיים אנומרטור חד-ערכי (כלומר, כל מילה מודפסת פעם אחת בלבד) עבור השפה $A \cup B$.",
  opts("נכון", "לא נכון", "תלוי בתשובה לשאלה $P = NP$?"), "a",
  J(r"""**נכון (ללא תלות ב-$P = NP$).** $A \in NPC \subseteq NP \subseteq R \subseteq RE$ וגם $B \in RE$, ו-$RE$ סגורה לאיחוד, לכן $A \cup B \in RE$ ויש לה אנומרטור $E$.""",
    r"""מכל אנומרטור $E$ ניתן לבנות אנומרטור חד-ערכי $E'$: $E'$ מריץ את $E$, ושומר על הסרט את רשימת המילים שכבר הדפיס (בכל רגע זו רשימה סופית). כש-$E$ מדפיס מילה $x$, $E'$ בודק אם $x$ כבר ברשימה; אם לא – מדפיס אותה ומוסיף לרשימה, אחרת מדלג. $E'$ מדפיס בדיוק את המילים ש-$E$ מדפיס, כל אחת פעם אחת.""",
    r"""**הפרכת ב:** ראו לעיל. **הפרכת ג:** הטיעון לא משתמש בשום הנחה על היחס בין $P$ ל-$NP$.""")),

S(7, "classification",
  r"$$L = \{\langle M\rangle \mid (*)\}$$" "\n"
  r"(*): לכל מילה $w$, המכונה $M$ עוצרת על $w$ בתוך לכל היותר $|w|^2$ צעדים",
  DEC4, "c",
  J(r"""**$\overline{L} \in RE$:** מכונה שעוברת על המילים $w$ לפי הסדר ומריצה את $M$ על $w$ למשך $|w|^2$ צעדים; אם עבור איזו $w$ $M$ לא עצרה – קבל."""),
  hold="Print-level ambiguity: read literally, w=ε forces M to halt within 0 steps, i.e. its start state is "
       "a halting state, so M halts at once on every input and L = {<M> | q0 ∈ {q_acc,q_rej}} is DECIDABLE (א). "
       "The intended answer is surely ג (coRE\\R, via an H̄_TM ≤m L reduction). The two readings give different answers -> hold.",
  note="Printed: 'L = { <M> | לכל מילה w, המכונה M עוצרת על w בתוך לכל היותר |w|^2 צעדים }' — condition moved to a (*) line."),

S(8, "classification",
  r"$$L = \{\langle M\rangle \mid L(M) = A_{TM}\}$$",
  DEC4, "d",
  J(r"""**$L \notin RE$:** רדוקציה $\overline{H_{TM}} \le_m L$. $f(\langle M,w\rangle) = \langle M_1\rangle$, כאשר $M_1$ על קלט $x$: מריצה במקביל (צעד-צעד לסירוגין) את המכונה האוניברסלית $U$ על $x$ ואת $M$ על $w$; אם $U$ מקבלת את $x$ או ש-$M$ עוצרת על $w$ – מקבלת. אם $M$ לא עוצרת על $w$ אז $L(M_1) = A_{TM}$ ולכן $\langle M_1\rangle \in L$; אם $M$ עוצרת על $w$ אז $L(M_1) = \Sigma^* \ne A_{TM}$.""",
    r"""**$L \notin coRE$:** רדוקציה $H_{TM} \le_m L$. $g(\langle M,w\rangle) = \langle M_2\rangle$, כאשר $M_2$ על קלט $x$: מריצה את $M$ על $w$; אם עצרה – מריצה את $U$ על $x$ ועונה כמוה. אם $M$ עוצרת על $w$ אז $L(M_2) = A_{TM}$; אחרת $L(M_2) = \emptyset \ne A_{TM}$.""",
    r"""שתי הפונקציות ניתנות לחישוב (רק בונים קידוד). לפי משפט הרדוקציה, מכיוון ש-$\overline{H_{TM}} \notin RE$ ו-$H_{TM} \notin coRE$, מתקבל $L \notin RE \cup coRE$ – תשובה ד.""")),

S(9, "classification",
  r"$$L = \{\langle M_1, M_2\rangle \mid L(M_1) \subset L(M_2)\}$$",
  DEC4, "d",
  J(r"""(כאן $\subset$ היא הכלה ממש; הטיעון עובד גם עבור $\subseteq$ עם שינוי קל.)""",
    r"""**$L \notin RE$:** רדוקציה $\overline{H_{TM}} \le_m L$. $f(\langle M,w\rangle) = \langle M_1, M_{all}\rangle$ כאשר $M_{all}$ מקבלת כל קלט, ו-$M_1$ על קלט $x$: אם $x = \varepsilon$ – קבל; אחרת הרץ את $M$ על $w$ וקבל. אם $M$ לא עוצרת על $w$: $L(M_1) = \{\varepsilon\} \subset \Sigma^*$; אם עוצרת: $L(M_1) = \Sigma^*$, שאינה מוכלת ממש ב-$\Sigma^*$.""",
    r"""**$L \notin coRE$:** רדוקציה $H_{TM} \le_m L$. $g(\langle M,w\rangle) = \langle M_\emptyset, M_2\rangle$ כאשר $M_\emptyset$ דוחה כל קלט, ו-$M_2$ על קלט $x$: הרץ את $M$ על $w$ וקבל. אם $M$ עוצרת על $w$: $\emptyset \subset \Sigma^* = L(M_2)$; אחרת $L(M_2) = \emptyset$ ו-$\emptyset \not\subset \emptyset$.""",
    r"""לפי משפט הרדוקציה $L \notin RE$ וגם $L \notin coRE$ – תשובה ד.""",
  ),
  note="Printed with a stray extra closing brace: 'L = { <M1,M2> | L(M1) ⊂ L(M2)}   }' — dropped."),

S(10, "decidability", "מהו היחס בין $A$ ל-$B$:", rel("A", "B"), "b",
  J(r"""**ב: $A \subset B$.** אם $\overline{L(M)}$ סופית אז $L(M) = \Sigma^* \setminus \overline{L(M)}$ אינסופית (כי $\Sigma^*$ אינסופית), לכן $A \subseteq B$. ההכלה ממש: מכונה שמקבלת בדיוק את המילים באורך זוגי – שפתה אינסופית וגם המשלימה שלה אינסופית, כלומר $\langle M\rangle \in B \setminus A$.""",
    r"""**הפרכת א, ג:** הדוגמה האחרונה מראה $B \not\subseteq A$. **הפרכת ד:** ב נכונה."""),
  contextId="rel", note="Triage derived 10ב from SAMP-2's relation answers — agrees."),

S(11, "decidability", "מהו היחס בין $B$ ל-$C$:", rel("B", "C"), "d",
  J(r"""**ד.** $B \not\subseteq C$: מכונה $M$ עם $L(M) = A_{TM}$ (המכונה האוניברסלית) – $A_{TM}$ אינסופית אבל $A_{TM} \notin R$, לכן $\langle M\rangle \in B \setminus C$.""",
    r"""$C \not\subseteq B$: מכונה שדוחה כל קלט – $L(M) = \emptyset \in R$ והיא סופית, לכן $\langle M\rangle \in C \setminus B$.""",
    r"""לכן אף אחד מהיחסים $=, \subset, \supset$ לא מתקיים."""),
  contextId="rel", note="Triage derived 11ד from SAMP-2's relation answers — agrees."),

S(12, "decidability", "מהו היחס בין $C$ ל-$A$:", rel("A", "C"), "b",
  J(r"""**ב: $A \subset C$.** אם $\overline{L(M)}$ סופית, אז $L(M)$ היא משלימה של שפה סופית; שפה סופית ניתנת להכרעה ו-$R$ סגורה למשלים, לכן $L(M) \in R$, כלומר $A \subseteq C$. ההכלה ממש: מכונה שדוחה כל קלט – $L(M) = \emptyset \in R$ אבל $\overline{\emptyset} = \Sigma^*$ אינסופית, לכן $\langle M\rangle \in C \setminus A$.""",
    r"""**הפרכת א, ג:** הדוגמה האחרונה. **הפרכת ד:** ב נכונה."""),
  contextId="rel",
  note="Options printed as A=C / A⊂C / A⊃C (A first although the stem says 'between C and A'). "
       "Triage wrote '12ג (C⊃A)' — same relation by content, but in SAMP-1's option wording it is ב (A⊂C)."),

S(17, "poly_reductions",
  r"אם $\langle \phi\rangle \in 3SAT$ אז $f(\langle \phi\rangle) \in ZSAT$",
  TF, "a",
  J(r"""**נכון.** נסמן ב-$n$ את מספר המשתנים ב-$\phi$; ב-$f(\phi)$ יש $n + N$ משתנים, ו-$N \ge n$. ניקח השמה מספקת של $\phi$ ונשים $False$ בכל $z_i$. אז $\phi$ מסופקת, וכל פסוקית $(\neg z_{3j-2} \vee \neg z_{3j-1} \vee \neg z_{3j})$ מסופקת. מספר המשתנים שקיבלו $False$ הוא לפחות $N \ge \frac{n+N}{2}$, כלומר לפחות מחצית מהמשתנים. $f(\phi)$ היא נוסחת $3CNF$, ולכן $f(\phi) \in ZSAT$."""),
  contextId="zsat"),

S(18, "poly_reductions",
  r"אם $\langle \phi\rangle \notin 3SAT$ אז $f(\langle \phi\rangle) \notin ZSAT$",
  TF, "a",
  J(r"""**נכון.** $f(\phi) = \phi \wedge d(\phi)$. כל השמה שמספקת את $f(\phi)$ מספקת בפרט את $\phi$ (המשתנים $z_i$ לא מופיעים ב-$\phi$). אם $\phi$ לא ספיקה אז גם $f(\phi)$ לא ספיקה בכלל, ובפרט לא ספיקה בהשמה שבה לפחות מחצית מהמשתנים $False$, לכן $f(\phi) \notin ZSAT$."""),
  contextId="zsat"),

S(19, "npc",
  r"האם המסקנה היא: $ZSAT \in NPC$?",
  YN, "a",
  J(r"""**כן.** לפי שאלות 17–18, $\phi \in 3SAT \Leftrightarrow f(\phi) \in ZSAT$, ו-$f$ ניתנת לחישוב בזמן פולינומי (מוסיפים $N \le n+2$ משתנים חדשים ו-$N/3$ פסוקיות). לכן $3SAT \le_p ZSAT$, ומכיוון ש-$3SAT \in NPC$ נקבל ש-$ZSAT$ היא $NP$-קשה. יחד עם הנתון $ZSAT \in NP$ מתקבל $ZSAT \in NPC$."""),
  contextId="zsat"),

S(20, "npc",
  r"תהא $A$ שפה כך שמתקיים $SAT \le_P A$ וגם $\overline{SAT} \le_P A$. איזו מהטענות הבאות נכונה?",
  opts("$NP$ סגורה למשלים.", "$NP$ אינה סגורה למשלים.", r"$A \in R$.", "אף תשובה אינה נכונה."), "d",
  J(r"""**ד.** הנתונים לא מגבילים את $A$ מלמעלה, ולכן לא נובע מהם דבר על $NP$ ולא על כריעות $A$.""",
    r"""**הפרכת ג:** $A = A_{TM}$. תהי $M_{SAT}$ מכונה המכריעה את $SAT$; הפונקציה $\phi \mapsto \langle M_{SAT}, \phi\rangle$ ניתנת לחישוב בזמן פולינומי ומקיימת $\phi \in SAT \Leftrightarrow \langle M_{SAT}, \phi\rangle \in A_{TM}$; באותו אופן עם מכונה המכריעה את $\overline{SAT}$. כלומר שתי הרדוקציות קיימות, אבל $A_{TM} \notin R$.""",
    r"""**הפרכת א, ב:** אילו $A \in NP$ היה נתון, היה נובע $\overline{SAT} \in NP$ ולכן $NP = coNP$. אבל $A$ יכולה להיות מחוץ ל-$NP$ (כמו בדוגמה $A_{TM}$), ולכן הנתונים מתקיימים בלי קשר לשאלה (הפתוחה) אם $NP$ סגורה למשלים – אף אחת מהטענות לא נובעת.""")),

S(21, "decidability",
  r"תהא $M$ מ\"ט דטרמיניסטית ותהא $M'$ המכונה שמתקבלת מ-$M$ ע\"י כך שמחליפים בין המצבים $q_{acc}$ ו-$q_{rej}$. איזו מהטענות הבאות נכונה?",
  opts(r"אם $L(M) \in R$ אז $L(M') \in R$.", r"$L(M) \ne L(M')$.",
       r"ייתכן ש-$L(M) \in RE$ אבל $L(M') \notin RE$.", "אף תשובה איננה נכונה."), "d",
  J(r"""**ד.** $L(M')$ היא קבוצת המילים ש-$M$ **דוחה** (עוצרת ב-$q_{rej}$).""",
    r"""**הפרכת א:** $M$ על קלט $\langle N, w\rangle$ מריצה את $N$ על $w$, ואם $N$ עוצרת – $M$ דוחה (על קלט שאינו קידוד כזה $M$ נכנסת ללולאה). $M$ לא מקבלת אף מילה, לכן $L(M) = \emptyset \in R$; אבל $M$ דוחה בדיוק את $H_{TM}$, לכן $L(M') = H_{TM} \notin R$.""",
    r"""**הפרכת ב:** $M$ שנכנסת ללולאה על כל קלט: $L(M) = L(M') = \emptyset$.""",
    r"""**הפרכת ג:** $M'$ היא מכונת טיורינג, ולכן תמיד $L(M') \in RE$."""),
  note="Variant of SAMP-3 part A Q2 (4 options instead of 5, no 'בהכרח מתקיים', no 'כל התשובות נכונות'); "
       "SAMP-3's key there is 'אף תשובה אינה נכונה' — agrees with ד."),

S(22, "mapping_reductions",
  r"תהינה $A$ ו-$B$ שפות ו-$f$ פונקצית רדוקציה מ-$A$ ל-$B$. האם קיימת דוגמה שבה $f$ פונקציה הפיכה?",
  opts(r"קיימת דוגמה כזו, שבה $A$ ו-$B$ שייכות ל-$R$.",
       r"קיימת דוגמה כזו, שבה $A$ ו-$B$ אינן שייכות ל-$R$.",
       "תשובות א' ו-ב' נכונות.",
       "לא קיימת דוגמה כזו, פונקצית רדוקציה בהכרח לא הפיכה."), "c",
  J(r"""**ג.** פונקציית הזהות $f(x) = x$ ניתנת לחישוב והפיכה, והיא רדוקציה $A \le_m A$ לכל שפה $A$.""",
    r"""**א נכונה:** $A = B = \emptyset$ (או כל שפה ב-$R$) עם $f$ = זהות. **ב נכונה:** $A = B = A_{TM}$ עם $f$ = זהות.""",
    r"""**הפרכת ד:** הדוגמאות לעיל. מכיוון שגם א וגם ב נכונות, התשובה המלאה היא ג."""),
  lockOrder=True),
]

contexts = {}
contexts["rel"] = {"kind": "text", "title": "יחסים בין שפות (שאלות 10–12)",
  "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
          r"$$A = \{\langle M\rangle \mid (*)\}$$"
          "(*): $\\overline{L(M)}$ סופית\n"
          r"$$B = \{\langle M\rangle \mid (**)\}$$"
          "(**): $L(M)$ אינסופית\n"
          r"$$C = \{\langle M\rangle \mid L(M) \in R\}$$"}
contexts["zsat"] = {"kind": "text", "title": "רדוקציה פולינומית (שאלות 17–19)",
  "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
          r"$$ZSAT = \{\langle \phi\rangle \mid (*)\}$$"
          "(*): $\\phi$ היא נוסחת $3CNF$ שניתנת לסיפוק באמצעות השמה שבה לפחות מחצית מהמשתנים מקבלים ערך $False$\n"
          "ניתן להראות כי $ZSAT \\in NP$ – נדלג כאן על ההוכחה.\n"
          r"**טענה:** $3SAT \le_p ZSAT$" "\n"
          "נגדיר את הפונקציה הבאה:\n"
          r"$$f(\langle \phi\rangle) = \phi \wedge (\neg z_1 \vee \neg z_2 \vee \neg z_3) \wedge (\neg z_4 \vee \neg z_5 \vee \neg z_6) \wedge \cdots (\neg z_{N-2} \vee \neg z_{N-1} \vee \neg z_N)$$"
          "כאשר: $z_i$ הינם משתנים חדשים שלא מופיעים ב-$\\phi$. ערכו של $N$ מתחלק ב-3 והוא הנמוך ביותר שעדיין גדול או שווה למספר המשתנים השונים המופיעים ב-$\\phi$.\n"
          "נסמן את התוספת\n"
          r"$$d(\phi) = (\neg z_1 \vee \neg z_2 \vee \neg z_3) \wedge (\neg z_4 \vee \neg z_5 \vee \neg z_6) \wedge \cdots (\neg z_{N-2} \vee \neg z_{N-1} \vee \neg z_N)$$"
          r"$$f(\phi) = \phi \wedge d(\phi)$$"}
ctx = copy.deepcopy(s3["contexts"]["map"])
ctx["title"] = "רדוקציית מיפוי (שאלות 13–16)"
ctx["text"] = ctx["text"].replace("**ענה על השאלות הבאות**", "**יש לענות על השאלות הבאות**")
contexts["map"] = ctx

exam = {
  "examCode": "SAMP-1",
  "examLabel": "מבחן לדוגמה 1",
  "year": 2022,
  "sourceFile": "מבחנים/מבחנים לדוגמה/ בחינה לדוגמה.pdf",
  "keyFile": "no own key; Q13-16, Q23-25: keys/explanations from מבחנים/מבחנים לדוגמה/פתרון מבחן לדוגמא.pdf (SAMP-3) "
             "by identical content; Q1-12, Q17-22: solved (tools/SOLVE_GUIDE.md, unofficial)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 26))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions; skipped:", ", ".join(SKIPPED))
