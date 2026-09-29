# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-B.json. Source: the scanned Holon exam "מבחן מס' 048"
(code ~JC1-6|7-9|10-12|13-16|17-19N|20-25M/1-6Z/13-18Z) on pages 70-77 of
`מבחנים/אוסף מבחנים בחישוביות וסיבוכיות.pdf` (pages 1-2 of 10 = cover missing; Q17 mentions
|L|=2023). NO answer key anywhere -> every question is SOLVED per tools/SOLVE_GUIDE.md
(answerSource "solved", official False). Rendered at 200 dpi into tools/raw/23B-B-SRC.
Option letters: printed on Q1, Q2 and Q23-25; on the other questions the printed letters are missing
and were hand-written in (א, ב, ג, ד top to bottom) - the order used here is the printed top-to-bottom order.
Run: PYTHONUTF8=1 py tools/gen/gen_23B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-B.json"
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

NO_YES = opts("לא נכון", "נכון")      # Q4-7, Q11: printed order
YES_NO = opts("נכון", "לא נכון")      # Q12, Q20-25
L_RE = r"$\overline{L}$"

contexts = {
  "map": {"kind": "text", "title": "רדוקציית מיפוי (שאלות 4–7)",
    "text": "תהי\n"
            r"$$L = \{\langle M_1, M_2\rangle \mid \exists x_1 \exists x_2 : x_1 \in L(M_1) \setminus L(M_2) \text{ and } x_2 \in L(M_2) \setminus L(M_1)\}$$"
            "ותהי\n"
            r"$$L_d = \{\langle M\rangle \mid \langle M\rangle \notin L(M)\}$$"
            "להלן פונקציות מיפוי:\n"
            r"$$f(\langle M\rangle) = \langle M_{1M}, M_{2M}\rangle$$"
            r"$\langle M_{1M}\rangle$ קידוד של מ\"ט אשר בהינתן קלט $x$: בודקת האם $x = 1$ אם כן מקבלת, אחרת מריצה את $M$ על $M$ ועונה הפוך ממנה" "\n"
            r"$\langle M_{2M}\rangle$ קידוד של מ\"ט אשר בהינתן קלט $x$: בודקת האם $x = 2$ אם כן מקבלת, אחרת מריצה את $M$ על $M$ ועונה הפוך ממנה" "\n"
            r"$$g(\langle M\rangle) = \langle M_{3M}, M_{4M}\rangle$$"
            r"$\langle M_{3M}\rangle$ קידוד של מ\"ט אשר בהינתן קלט $x$: בודקת האם $x = 1$ אם כן מקבלת, אחרת מריצה את $M$ על $M$ ועונה כמותה" "\n"
            r"$\langle M_{4M}\rangle$ קידוד של מ\"ט אשר בהינתן קלט $x$: בודקת האם $x = 2$ אם כן מקבלת, אחרת מריצה את $M$ על $M$ ועונה כמותה" "\n"
            r"$$w(\langle M\rangle) = \langle M_{even}, M'\rangle$$"
            r"$\langle M_{even}\rangle$ קידוד של מ\"ט שמקבלת רק את כל המילים באורך זוגי" "\n"
            r"$\langle M'\rangle$ קידוד של מ\"ט אשר בהינתן קלט $x$: בודקת האם $x$ באורך אי זוגי, אם כן, מקבלת, אחרת מריצה את $M$ על כל הקלטים שקטנים מ-$x$ ועונה כן רק אם כולם התקבלו"},
  "rel": {"kind": "text", "title": "יחסים בין שפות (שאלות 8–10)",
    "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n"
            r"$$A = \{\langle M\rangle \mid L(M) = \overline{HTM}\}$$"
            r"$$B = \{\langle M\rangle \mid L(M) = HTM\}$$"
            r"$$C = \{\langle M\rangle \mid L(M) \in RE\}$$"},
  "isc": {"kind": "text", "title": "רדוקציה פולינומית (שאלות 11–13)",
    "text": r"נגדיר את השפה $IS \cap CLIQUE$. קל להוכיח כי השפה שייכת ל-$NP$." "\n"
            r"בהינתן גרף $G = (V = \{v_1, \ldots v_n\}, E)$." "\n"
            "נגדיר את הפונקציה הבאה:\n"
            r"$$f(\langle G, k\rangle) = \langle G' = G \cup G^*, k\rangle$$"
            r"כאשר: $G^* = (V^*, E^*)$ כך ש-$V^* = \{v_1^*, \ldots, v_n^*\}$ ו-$E^* = \{\{u^*, v^*\} \mid u, v \in V, \{u, v\} \notin E\}$" "\n"
            r"כלומר הגרף משלים זר בצמתים של $G$." "\n"
            r"כלומר, הפונקציה מחזירה איחוד זר בצמתים של הגרף $G$ והעתק של הגרף המשלים של $G$."},
}

questions = [
S(1, "classification",
  r"$$L = \{\langle M\rangle \mid M \text{ is a TM and } \forall x : M \text{ accepts at least one of } \{0 \cdot x, 1 \cdot x\}\}$$"
  "(הסימון $\\cdot$ משמעו שרשור)",
  opts("$L$ ניתנת להכרעה", r"גם $L$ וגם $\overline{L}$ לא ניתנות לקבלה",
       "$L$ לא ניתנת להכרעה אך ניתנת לקבלה", r"$L$ לא ניתנת לקבלה אך $\overline{L}$ ניתנת לקבלה"),
  "b",
  J(r"""**$L \notin RE$:** רדוקציה $\overline{H_{TM}} \le_m L$. $f(\langle M,w\rangle) = \langle M'\rangle$ כאשר $M'$ על קלט $y$: מריצה את $M$ על $w$ למשך $|y|$ צעדים; אם $M$ עצרה – דוחה, אחרת מקבלת. אם $M$ לא עוצרת על $w$ אז $L(M') = \Sigma^*$ ולכן $\langle M'\rangle \in L$. אם $M$ עוצרת אחרי $t$ צעדים, אז לכל $x$ עם $|x| \ge t$ גם $0x$ וגם $1x$ נדחות, ולכן $\langle M'\rangle \notin L$.""",
    r"""**$L \notin coRE$:** רדוקציה $H_{TM} \le_m L$. $g(\langle M,w\rangle) = \langle M''\rangle$ כאשר $M''$ על קלט $y$: מריצה את $M$ על $w$ ומקבלת. אם $M$ עוצרת על $w$ אז $L(M'') = \Sigma^*$ ו-$\langle M''\rangle \in L$; אחרת $L(M'') = \emptyset$ ו-$\langle M''\rangle \notin L$.""",
    r"""שתי הפונקציות ניתנות לחישוב, ולפי משפט הרדוקציה $L \notin RE \cup coRE$ – תשובה ב.""")),

S(2, "classification",
  r"מ\"ט תיקרא נחמדה (nice) אם היא מכריעה את שפתה, בעלת 100 מצבים לכל היותר, וא\"ב הסרט שלה הוא $\{0, 1, \sqcup\}$. לאיזו מחלקה שייכת השפה הבאה:" "\n"
  r"$$L = \{\langle x, y\rangle \mid \text{There exists a nice TM that accepts } x \text{ and rejects } y\}$$",
  opts(r"$L$ לא ניתנת לקבלה אך $\overline{L}$ ניתנת לקבלה", "$L$ ניתנת להכרעה",
       r"גם $L$ וגם $\overline{L}$ לא ניתנות לקבלה", "$L$ לא ניתנת להכרעה אך ניתנת לקבלה"),
  "b",
  J(r"""**$L$ ניתנת להכרעה.** יש מספר **סופי** של מכונות טיורינג עם לכל היותר 100 מצבים מעל א\"ב הסרט $\{0,1,\sqcup\}$ (עד כדי שינוי שמות מצבים), ולכן גם מספר סופי של מכונות נחמדות $N_1, \ldots, N_m$. כל אחת מהן מכריעה את שפתה, כלומר עוצרת על כל קלט.""",
    r"""נבנה מכריע ל-$L$ שבו רשימת המכונות הנחמדות "מקודדת" מראש (רשימה כזו קיימת, גם אם איננו יודעים לחשב אותה): על קלט $\langle x, y\rangle$ – לכל $i$ הרץ את $N_i$ על $x$ ועל $y$ (הריצות עוצרות); אם קיים $i$ ש-$N_i$ מקבלת את $x$ ודוחה את $y$ – קבל, אחרת דחה. המכונה עוצרת תמיד ועונה נכון, ולכן $L \in R$ (ובפרט התשובות א, ג, ד שגויות).""")),

S(3, "classification",
  r"תהי:" "\n"
  r"$$L = \{\langle M, w\rangle : M \text{ does not repeat a configuration during its run on } w\}$$"
  "לאיזו מחלקה היא שייכת?",
  opts(r"$L$ לא ניתנת לקבלה אך $\overline{L}$ ניתנת לקבלה", r"גם $L$ וגם $\overline{L}$ לא ניתנות לקבלה",
       "$L$ ניתנת להכרעה", "$L$ לא ניתנת להכרעה אך ניתנת לקבלה"),
  "a",
  J(r"""**$\overline{L} \in RE$:** $\overline{L}$ היא קבוצת הזוגות שבהם $M$ חוזרת על קונפיגורציה בריצתה על $w$. מכונה מקבלת: מסמלצת את $M$ על $w$ ושומרת את כל הקונפיגורציות שראתה (בכל רגע רשימה סופית); אם קונפיגורציה חוזרת – מקבלת; אם $M$ עוצרת – דוחה.""",
    r"""**$\overline{L} \notin R$:** רדוקציה $H_{TM} \le_m \overline{L}$. $f(\langle M,w\rangle) = \langle M', \varepsilon\rangle$ כאשר $M'$ מסמלצת את $M$ על $w$, ואחרי כל צעד מסומלץ מגדילה מונה בקצה הסרט (כך שתוכן הסרט גדל ואף קונפיגורציה לא חוזרת במהלך הסימולציה). אם הסימולציה עוצרת, $M'$ נכנסת ללולאה שבה הראש זז ימינה ושמאלה על אותם תאים – וחוזרת על קונפיגורציה. לכן $M$ עוצרת על $w$ אם"ם $M'$ חוזרת על קונפיגורציה.""",
    r"""מכאן $\overline{L} \in RE \setminus R$, ולכן $L \notin RE$ (אחרת גם $L$ וגם $\overline{L}$ ב-$RE$ ו-$L \in R$) ו-$L \in coRE$ – תשובה א."""),
  note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(4, "mapping_reductions",
  r"האם $g$ רדוקציה $\overline{L_d} \le_m L$?",
  NO_YES, "a",
  J(r"""**לא נכון.** נחשב את $g$: אם $M$ מקבלת את $\langle M\rangle$ אז $M_{3M}$ ו-$M_{4M}$ מקבלות כל קלט, $L(M_{3M}) = L(M_{4M}) = \Sigma^*$, ולכן $g(\langle M\rangle) \notin L$. אם $M$ לא מקבלת את $\langle M\rangle$ (דוחה או לא עוצרת) אז $L(M_{3M}) = \{1\}$, $L(M_{4M}) = \{2\}$ – שתי שפות שאף אחת לא מוכלת בשנייה, ולכן $g(\langle M\rangle) \in L$.""",
    r"""כלומר $g(\langle M\rangle) \in L \Leftrightarrow \langle M\rangle \notin L(M) \Leftrightarrow \langle M\rangle \in L_d$. עבור מכונה $M$ שמקבלת כל קלט: $\langle M\rangle \in \overline{L_d}$ אבל $g(\langle M\rangle) \notin L$, ולכן $g$ אינה רדוקציה מ-$\overline{L_d}$ ל-$L$."""),
  contextId="map"),

S(5, "mapping_reductions",
  r"האם $g$ רדוקציה $L_d \le_m L$?",
  NO_YES, "b",
  J(r"""**נכון.** כפי שחושב בשאלה הקודמת: אם $M$ מקבלת את $\langle M\rangle$ אז $L(M_{3M}) = L(M_{4M}) = \Sigma^*$ ו-$g(\langle M\rangle) \notin L$; אחרת $L(M_{3M}) = \{1\}$, $L(M_{4M}) = \{2\}$, ויש $x_1 = 1 \in L(M_{3M}) \setminus L(M_{4M})$ ו-$x_2 = 2 \in L(M_{4M}) \setminus L(M_{3M})$, ולכן $g(\langle M\rangle) \in L$.""",
    r"""לכן $\langle M\rangle \in L_d \Leftrightarrow g(\langle M\rangle) \in L$, ו-$g$ ניתנת לחישוב (רק בונים קידודים) – זו רדוקציה $L_d \le_m L$."""),
  contextId="map"),

S(6, "mapping_reductions",
  r"האם $w$ רדוקציה $\overline{ALL_{TM}} \le_m L$?",
  NO_YES, "b",
  J(r"""**נכון.** $L(M_{even})$ = המילים באורך זוגי. $L(M')$ מכילה את כל המילים באורך אי-זוגי, ומילה $x$ באורך זוגי שייכת ל-$L(M')$ אם"ם $M$ מקבלת את כל המילים הקטנות מ-$x$.""",
    r"""אם $\langle M\rangle \in ALL_{TM}$: $L(M') = \Sigma^*$, ולכן $L(M_{even}) \setminus L(M') = \emptyset$ ו-$w(\langle M\rangle) \notin L$.""",
    r"""אם $\langle M\rangle \in \overline{ALL_{TM}}$: קיימת $y_0$ ש-$M$ לא מקבלת. אז כל מילה זוגית הגדולה מ-$y_0$ לא ב-$L(M')$, כלומר $L(M')$ מכילה רק מספר סופי של מילים זוגיות. לכן $L(M_{even}) \setminus L(M') \ne \emptyset$ (אינסוף מילים זוגיות), וגם $L(M') \setminus L(M_{even}) \ne \emptyset$ (כל המילים האי-זוגיות) – ולכן $w(\langle M\rangle) \in L$.""",
    r"""$w$ ניתנת לחישוב, ולכן זו רדוקציה $\overline{ALL_{TM}} \le_m L$."""),
  contextId="map"),

S(7, "mapping_reductions",
  r"האם $f$ רדוקציה $\overline{L_d} \le_m L$?",
  NO_YES, "a",
  J(r"""**לא נכון.** $M_{1M}, M_{2M}$ "עונות הפוך" מ-$M$ על $\langle M\rangle$ – אבל אם $M$ לא עוצרת על $\langle M\rangle$ גם הן לא עוצרות. לכן: אם $M$ דוחה את $\langle M\rangle$: $L(M_{1M}) = L(M_{2M}) = \Sigma^*$ ו-$f(\langle M\rangle) \notin L$. אם $M$ מקבלת את $\langle M\rangle$ **או לא עוצרת עליו**: $L(M_{1M}) = \{1\}$, $L(M_{2M}) = \{2\}$ ו-$f(\langle M\rangle) \in L$.""",
    r"""דוגמה נגדית: $M$ שלא עוצרת על אף קלט. $\langle M\rangle \notin L(M)$ ולכן $\langle M\rangle \notin \overline{L_d}$, אבל $f(\langle M\rangle) \in L$. לכן $f$ אינה רדוקציה $\overline{L_d} \le_m L$."""),
  contextId="map"),

S(8, "decidability", "קבע מהו היחס בין A ל-B:",
  opts(("math", r"B \subset A"), ("math", "A = B"), "אף אחד מהנ\"ל", ("math", r"A \subset B")), "d",
  J(r"""**ד: $A \subset B$.** $\overline{HTM} \notin RE$, ולכן אין מכונת טיורינג $M$ עם $L(M) = \overline{HTM}$ (שפה של מכונה היא תמיד ב-$RE$). לכן $A = \emptyset$.""",
    r"""לעומת זאת $HTM \in RE$, כלומר קיימת מכונה $M$ עם $L(M) = HTM$, ולכן $B \ne \emptyset$. מכאן $A = \emptyset \subset B$ (הכלה ממש), והתשובות א, ב, ג שגויות."""),
  contextId="rel", note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(9, "decidability", "קבע מהו היחס בין B ל-C:",
  opts("אף אחד מהנ\"ל", ("math", r"B \subset C"), ("math", r"C \subset B"), ("math", "B = C")), "b",
  J(r"""**ב: $B \subset C$.** לכל מכונה $M$ מתקיים $L(M) \in RE$ (בהגדרה), ולכן $C$ היא קבוצת כל קידודי המכונות, ובפרט $B \subseteq C$. ההכלה ממש: מכונה שדוחה כל קלט – $L(M) = \emptyset \ne HTM$, כלומר $\langle M\rangle \in C \setminus B$."""),
  contextId="rel", note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(10, "decidability", "קבע מהו היחס בין C ל-A:",
  opts(("math", r"A \subset C"), ("math", "A = C"), ("math", r"C \subset A"), "אף אחד מהנ\"ל"), "a",
  J(r"""**א: $A \subset C$.** כפי שראינו $A = \emptyset$ (אין מכונה שמקבלת את $\overline{HTM} \notin RE$), ו-$C$ היא קבוצת כל קידודי המכונות – קבוצה לא ריקה. לכן $A = \emptyset \subset C$."""),
  contextId="rel", note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(11, "poly_reductions",
  r"אם $\langle G, k\rangle \in CLIQUE$ אזי $f(\langle G, k\rangle) \in IS \cap CLIQUE$",
  NO_YES, "b",
  J(r"""**נכון.** אם ב-$G$ יש קליקה $K$ בגודל $k$, אז $K$ היא גם קליקה בגודל $k$ ב-$G' = G \cup G^*$. בנוסף, העותקים $\{v^* \mid v \in K\}$ ב-$G^*$ (המשלים) הם קבוצה בלתי תלויה בגודל $k$, ומכיוון שאין צלעות בין $G$ ל-$G^*$ זו קבוצה בלתי תלויה גם ב-$G'$. לכן $f(\langle G,k\rangle) \in IS \cap CLIQUE$."""),
  contextId="isc", note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(12, "poly_reductions",
  r"אם $f(\langle G, k\rangle) \in IS \cap CLIQUE$ אזי $\langle G, k\rangle \in CLIQUE$",
  YES_NO, "b",
  J(r"""**לא נכון.** קליקה ב-$G'$ נמצאת כולה ב-$G$ או כולה ב-$G^*$. אם היא ב-$G^*$ היא מתאימה לקבוצה בלתי תלויה ב-$G$, ולא לקליקה ב-$G$.""",
    r"""דוגמה נגדית: $G$ = שני קדקודים ללא צלע, $k = 2$. ב-$G$ אין קליקה בגודל 2, אבל ב-$G^*$ יש צלע (קליקה בגודל 2), וב-$G'$ שני הקדקודים של $G$ הם קבוצה בלתי תלויה בגודל 2. לכן $f(\langle G,2\rangle) \in IS \cap CLIQUE$ אבל $\langle G,2\rangle \notin CLIQUE$."""),
  contextId="isc", note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(13, "npc",
  r"האם המסקנה היא כי $IS \cap CLIQUE \in NPC$?",
  opts("ההוכחה שנתנה פה שגויה והמסקנה שגויה", "המסקנה נכונה והיא נובעת מההוכחה שבשאלה",
       "ההוכחה שגויה אבל המסקנה נכונה וניתן להוכיח אותה ע\"י רדוקציה אחרת", "ההוכחה שניתנה פה נכונה אבל המסקנה שגויה"),
  "c",
  J(r"""**ההוכחה שגויה:** לפי השאלה הקודמת $f$ אינה מקיימת את כיוון "$f(x) \in IS \cap CLIQUE \Rightarrow x \in CLIQUE$", ולכן אינה רדוקציה $CLIQUE \le_p IS \cap CLIQUE$ (הפרכת ב, ד).""",
    r"""**המסקנה נכונה:** נתון $IS \cap CLIQUE \in NP$. רדוקציה אחרת $CLIQUE \le_p IS \cap CLIQUE$: עבור $k \ge 2$, $h(\langle G,k\rangle) = \langle G'', k\rangle$ כאשר $G''$ הוא $G$ בתוספת $k$ קדקודים חדשים מבודדים. ב-$G''$ תמיד יש קבוצה בלתי תלויה בגודל $k$ (הקדקודים החדשים), וקדקוד מבודד לא משתתף בקליקה בגודל $\ge 2$, לכן ב-$G''$ יש קליקה בגודל $k$ אם"ם ב-$G$ יש. (עבור $k \le 1$ הבעיה טריוויאלית וממפים למופע קבוע מתאים.) $h$ פולינומית, ולכן $IS \cap CLIQUE \in NPC$ – הפרכת א, ותשובה ג."""),
  contextId="isc", note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(14, "mapping_reductions",
  r"תהיינה $A, B \subseteq \Sigma^*$ שפות, ונניח כי $A \le_m \Sigma^*$ וגם $\Sigma^* \le_m B$. להלן שתי טענות:" "\n"
  r"1. בהכרח מתקיים כי $A = \Sigma^*$" "\n"
  r"2. בהכרח מתקיים כי $B = \Sigma^*$" "\n"
  "בחרו בתשובה הנכונה:",
  opts("טענה 2 נכונה וטענה 1 אינה נכונה", "טענה 1 נכונה וטענה 2 אינה נכונה",
       "שתי הטענות שגויות", "שתי הטענות נכונות"),
  "b",
  J(r"""**טענה 1 נכונה:** אם $f$ רדוקציה $A \le_m \Sigma^*$ אז לכל $x$: $x \in A \Leftrightarrow f(x) \in \Sigma^*$. אבל תמיד $f(x) \in \Sigma^*$, ולכן כל $x$ שייך ל-$A$, כלומר $A = \Sigma^*$.""",
    r"""**טענה 2 לא נכונה:** $\Sigma^* \le_m B$ מחייב רק ש-$B \ne \emptyset$ (כל המילים ממופות לתוך $B$). דוגמה: $B = \{0\}$ והפונקציה הקבועה $f(x) = 0$ – רדוקציה $\Sigma^* \le_m B$, אבל $B \ne \Sigma^*$."""),
  note="Options have no printed letters; hand-written letters (top to bottom) used. Order of the two reductions "
       "(A ≤m Σ*, Σ* ≤m B) checked at zoom on the scan."),

S(15, "mapping_reductions",
  "להלן שתי טענות:\n"
  "1. רדוקציית המיפוי היא בהכרח פונקציה חח\"ע (חד חד ערכית)\n"
  "2. רדוקציית המיפוי היא בהכרח פונקציה על\n"
  "בחרו בטענה הנכונה:",
  opts("שתי הטענות נכונות", "שתי הטענות שגויות", "טענה 1 נכונה ו-2 שגויה", "טענה 2 נכונה וטענה 1 שגויה"),
  "b",
  J(r"""**שתי הטענות שגויות.** דוגמה: $A$ = המילים שמתחילות ב-0, $B = \{0\}$, ו-$f(x) = 0$ אם $x$ מתחיל ב-0 ו-$f(x) = 1$ אחרת. $f$ ניתנת לחישוב ומקיימת $x \in A \Leftrightarrow f(x) \in B$, כלומר היא רדוקציה $A \le_m B$. אבל $f$ אינה חח\"ע (אינסוף מילים ממופות ל-0) ואינה על (התמונה היא $\{0,1\}$ בלבד)."""),
  note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(16, "time_p",
  r"מ\"ט עם 3 סרטים וראשים בו זמניים, הינה מכונת טיורינג עם שלושה סרטים בה שלושת הראשונים זזים יחד ימינה או שמאלה, פורמלית, פונקצית המעברים היא מהצורה $\delta: Q \times \Gamma^3 \to Q \times \Gamma^3 \times \{L, R\}$, "
  r"תהי $M$ מכונת טיורינג עם שלושה סרטים וראשים בו זמניים המכריעה את $L$ בזמן $t(n)$ כאשר $t(n) \ge n$ אזי קיימת מ\"ט בעלת סרט אחד המכריעה את $L$ בזמן:",
  opts("אף אחת מהנ\"ל",
       r"$O((t(n))^3)$ אבל לא בהכרח קיימת מ\"ט המכריעה בזמן $O((t(n))^2)$",
       ("math", r"O(t(n))"),
       r"$O((t(n))^2)$ אבל לא בהכרח קיימת מ\"ט המכריעה בזמן $O(t(n))$"),
  "c",
  J(r"""**ג.** מכיוון שהראשים תמיד באותו מיקום, מכונה בעלת סרט אחד עם א\"ב סרט $\Gamma^3$ (כל תא מחזיק שלישייה – "שלושה מסלולים") מסמלצת את $M$ צעד אחר צעד: תו קלט $a$ מתפרש כשלישייה $(a, \sqcup, \sqcup)$, והמעבר $\delta'(q, (a,b,c)) = (q', (a',b',c'), D)$ מועתק ישירות מ-$\delta$. כל צעד של $M$ הוא צעד אחד של המכונה החדשה, ולכן זמן הריצה הוא $t(n) = O(t(n))$.""",
    r"""**הפרכת ב, ד:** טוענות ש"לא בהכרח" קיימת מכונה בזמן נמוך יותר, אבל הראינו שתמיד קיימת מכונה בזמן $O(t(n))$. **הפרכת א:** ג נכונה."""),
  note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(17, "npc",
  "תהי $L$ שפה לא טריביאלית. איזה מבין הטענות הבאות **אינה** בהכרח נכונה?",
  opts(r"אם $P = NP$ ו-$L \in NPC$ אזי $L$ אינסופית",
       r"אם $P \ne NP$ ו-$|L| = 2023$ אזי $L \notin NPC$",
       r"אם $P = NP$ ו-$L$ סופית אזי $L \in NPC$",
       r"אם $L \in NPC$ ו-$L$ סופית, אזי $P = NP$"),
  "a",
  J(r"""**א אינה בהכרח נכונה:** אם $P = NP$, כל שפה לא טריוויאלית $L \in P$ היא $NP$-שלמה: לכל $L' \in NP = P$, הרדוקציה מכריעה את $L'$ בזמן פולינומי ומחזירה מילה קבועה ב-$L$ או מילה קבועה מחוץ ל-$L$. בפרט שפה סופית לא ריקה (למשל $L = \{0\}$) שייכת ל-$NPC$ והיא לא אינסופית.""",
    r"""**ב נכונה:** שפה סופית שייכת ל-$P$; אילו $L \in NPC$ היינו מקבלים $P \cap NPC \ne \emptyset$ ולכן $P = NP$, בסתירה להנחה.""",
    r"""**ג נכונה:** $L$ סופית ולא טריוויאלית, ולכן $L \in P$ ולפי הטיעון בא' $L \in NPC$ כש-$P = NP$.""",
    r"""**ד נכונה:** $L$ סופית ולכן $L \in P$; יחד עם $L \in NPC$ נקבל $P = NP$."""),
  note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(18, "undecidability",
  r"יהי $\langle P(x1, x2 \ldots xn)\rangle$ קידוד של פולינום עם $n$ משתנים." "\n"
  r"נגדיר $f(k, \langle P(x1, x2, \ldots, xn)\rangle) \to \{0, 1\}$ בצורה הבאה:" "\n"
  r"• $f(k, \langle P(x1, x2, \ldots, xn)\rangle) = 1$ אם\"ם לפולינום יש יותר מ-$k$ שורשים בשלמים." "\n"
  r"• אחרת $f(k, \langle P(x1, x2, \ldots, xn)\rangle) = 0$",
  opts("לכל מספר $k$ הפונקציה $f$ ניתנת לחישוב אך לאו דווקא בזמן פולינומיאלי",
       "לכל מספר $k > 0$ הפונקציה $f$ לא ניתנת לחישוב.",
       "קיים $k$ עבורו הפונקציה לא ניתנת לחישוב, אך קיים $k > 0$ עבורו הפונקציה כן ניתנת לחישוב",
       "הפונקציה ניתנת לחישוב בזמן פולינומיאלי אם $P = NP$."),
  "b",
  J(r"""**ב.** נקבע $k \ge 0$ כלשהו, ונראה שחישוב $f(k, \cdot)$ מאפשר להכריע את $H_{10}$ (פולינומים עם שורש בשלמים), שאינה ב-$R$. בהינתן פולינום $P(x_1,\ldots,x_n)$ נבנה $Q(x_1,\ldots,x_n,y) = P(x_1,\ldots,x_n)$ עם משתנה נוסף $y$ שאינו מופיע. אם ל-$P$ יש שורש $(a_1,\ldots,a_n)$ אז לכל שלם $b$ הנקודה $(a_1,\ldots,a_n,b)$ שורש של $Q$ – אינסוף שורשים, יותר מ-$k$. אם ל-$P$ אין שורש, גם ל-$Q$ אין. לכן $\langle P\rangle \in H_{10} \Leftrightarrow f(k, \langle Q\rangle) = 1$, ואילו $f(k,\cdot)$ הייתה ניתנת לחישוב היינו מכריעים את $H_{10}$. מכאן שלכל $k$ (בפרט לכל $k > 0$) $f$ לא ניתנת לחישוב.""",
    r"""**הפרכת א, ג:** אין $k$ שעבורו $f$ ניתנת לחישוב. **הפרכת ד:** $f$ לא ניתנת לחישוב כלל, בלי קשר ל-$P = NP$."""),
  note="Printed with variable names 'x1, x2 ... xn' (no subscripts) and ',,' typos in the argument list — cleaned to '\\ldots'. "
       "Options have no printed letters; hand-written letters (top to bottom) used."),

S(19, "closure",
  r"תהיינה $L_1, L_2$ שפות שאינן שייכות ל-$NP$" "\n"
  "להלן שתי טענות:\n"
  r"1. $L_1 \cap L_2 \notin NP$" "\n"
  r"2. $L_1 \cup L_2 \notin NP$" "\n"
  "בחרו בתשובה הנכונה:",
  opts("שתי הטענות שגויות", "טענה 2 נכונה וטענה 1 שגוייה", "טענה 1 נכונה וטענה 2 שגוייה", "שתי הטענות נכונות"),
  "a",
  J(r"""**שתי הטענות שגויות.** $L_1 = A_{TM}$, $L_2 = \overline{A_{TM}}$. שתיהן לא ב-$R$, ולכן לא ב-$NP \subseteq R$. אבל $L_1 \cap L_2 = \emptyset \in NP$ ו-$L_1 \cup L_2 = \Sigma^* \in NP$."""),
  note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(20, "closure",
  "לכל שפה $A$ שאינה ניתנת לקבלה קיימת שפה $B$ שאינה ניתנת לקבלה כך ש-$B$ מכילה ממש את $A$",
  YES_NO, "a",
  J(r"""**נכון.** $A \notin RE$, ולכן $\overline{A}$ אינסופית (אילו $\overline{A}$ הייתה סופית, $A$ הייתה משלימה של שפה סופית ולכן ב-$R$). ניקח $x \notin A$ ונגדיר $B = A \cup \{x\}$, שמכילה ממש את $A$. אילו $B \in RE$, אז $A = B \cap \overline{\{x\}}$ – חיתוך של שפה ב-$RE$ עם שפה ב-$R$ – הייתה ב-$RE$, סתירה. לכן $B \notin RE$."""),
  note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(21, "tm",
  r"אוסף השפות הניתנות להכרעה על-ידי מ\"ט דטרמיניסטית עם חמישה סרטים זהה למחלקה $R$.",
  YES_NO, "a",
  J(r"""**נכון.** כל מכונה עם סרט אחד היא בפרט מכונה עם חמישה סרטים (שמשתמשת רק בסרט אחד), וכל מכונה רב-סרטית ניתנת לסימולציה על ידי מכונה עם סרט אחד שעוצרת בדיוק כשהמקורית עוצרת ועונה כמוה. לכן מכונות עם חמישה סרטים מכריעות בדיוק את השפות ב-$R$."""),
  note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(22, "tm",
  r"לכל מספר טבעי $k$ קיימת שפה הניתנת לקבלה ע\"י מ\"ט עם $2k$ סרטים אבל אינה ניתנת לקבלה ע\"י מ\"ט עם $k$ סרטים",
  YES_NO, "b",
  J(r"""**לא נכון.** כל מכונה רב-סרטית שקולה למכונה עם סרט אחד (ובפרט למכונה עם $k \ge 1$ סרטים) המקבלת את אותה שפה. לכן כל שפה שניתנת לקבלה ע\"י מכונה עם $2k$ סרטים ניתנת לקבלה גם ע\"י מכונה עם $k$ סרטים."""),
  note="Options have no printed letters; hand-written letters (top to bottom) used."),

S(23, "np",
  r"אם $Q$ שייכת ל-$NPC \cap coNP$ אזי $\overline{Q}$ שפה $NP$ קשה",
  YES_NO, "a",
  J(r"""**נכון.** $Q \in coNP$, וכל $L \in NP$ מקיימת $L \le_p Q$ (כי $Q \in NPC$); לכן $L \in coNP$ (כי $coNP$ סגורה לרדוקציה פולינומית: $\overline{L} \le_p \overline{Q} \in NP$). כלומר $NP \subseteq coNP$ ולכן $NP = coNP$.""",
    r"""כעת תהי $L \in NP$. אז $\overline{L} \in coNP = NP$, ולכן $\overline{L} \le_p Q$, כלומר $L \le_p \overline{Q}$. לכן כל שפה ב-$NP$ ניתנת לרדוקציה פולינומית ל-$\overline{Q}$ – $\overline{Q}$ היא $NP$-קשה."""),
  hold="Math is certain (א, נכון), but the scan has an unidentified hand mark: the letter ב is boxed "
       "(possibly someone's selection) - DISAGREES. Adir: release if the p77 marks are not a key.",
  note="Scan p77: hand-drawn box around ב (unknown author/meaning; triage called the p77 marks relabelling/artifacts)."),

S(24, "mapping_reductions",
  r"מתקיים $SAT \le_m \overline{SAT}$",
  YES_NO, "a",
  J(r"""**נכון.** $SAT \in NP \subseteq R$, ו-$\overline{SAT}$ לא טריוויאלית. נקבע $y_1 \in \overline{SAT}$ ו-$y_0 \notin \overline{SAT}$ ונגדיר $f(x) = y_1$ אם $x \in SAT$ ו-$f(x) = y_0$ אחרת. $f$ ניתנת לחישוב (כי $SAT$ כריעה) ומקיימת $x \in SAT \Leftrightarrow f(x) \in \overline{SAT}$. (מדובר ברדוקציית מיפוי, לא ברדוקציה פולינומית.)"""),
  note="Scan p77: hand scribble over the letter א (unknown meaning; if a selection it agrees, if a cross-out it disagrees)."),

S(25, "time_p",
  r"תהי $M$ מ\"ט דטרמיניסטית שמכריעה שפה. אם לכל $n$ טבעי קיימת מילה באורך $n$ עליה $M$ עוצרת אחרי $2^n$ צעדים אזי $L(M)$ אינה ב-$P$",
  YES_NO, "b",
  J(r"""**לא נכון.** זמן הריצה של מכונה **מסוימת** לא קובע את המחלקה של **השפה**. דוגמה: $M$ שעל קלט $x$ באורך $n$ מבצעת $2^n$ צעדי סרק ואז דוחה. $M$ מכריעה את $L(M) = \emptyset$ ועוצרת על כל מילה באורך $n$ אחרי $2^n$ צעדים (בערך), אבל $\emptyset \in P$ (מכונה שדוחה מיד)."""),
  hold="Math is certain (ב, לא נכון), but the scan has an unidentified hand scribble over the letter א "
       "(if it is someone's selection it DISAGREES). Adir: release if the p77 marks are not a key.",
  note="Scan p77: hand scribble over the letter א (unknown author/meaning)."),
]

# --- RESOLUTIONS (ASK_ADIR items resolved by independent math check; Adir authorized 2026-09-29) ---
def _resolve(num, **kw):
    q = next(q for q in questions if q["num"] == num)
    q.pop("hold", None)
    q.update(kw)
# Stage-2 blind verification (tools/raw/_verify_23B-B.json): all 25 agree.
# Q23/Q25 were held only over hand marks of unknown origin on the scan (a student's, not a key); both solvers prove the answers -> released.
_resolve(23, confidence="high", note=r"""Released after stage 2: both solvers get א. The scan's hand box on ב is a student's mark, not a key.""")
_resolve(25, confidence="high", note=r"""Released after stage 2: both solvers get ב. The scan's scribble on א is a student's mark, not a key.""")

exam = {
  "examCode": "23B-B",
  "examLabel": "2023 סמסטר ב מועד ב (משוער)",
  "year": 2023,
  "sourceFile": "מבחנים/אוסף מבחנים בחישוביות וסיבוכיות.pdf",
  "keyFile": "no key - all answers solved (tools/SOLVE_GUIDE.md, unofficial); "
             "sitting inferred: Holon exam 048 from the collection p70–77, cover missing",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 26))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
