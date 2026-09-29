# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-C.json (2025 סמסטר ב מועד ג, 7.9.2025; staff of 25B-A/25B-B).
Transcribed by hand from the rendered pages of `מבחנים/2025/מס ב מועד ג 7-9.pdf` (7 pages).
NO answer key exists: every answer below is SOLVED (stage 1 of tools/SOLVE_GUIDE.md) —
answerSource "solved", official False. Q5 diagram cropped to images/exams/25B-C-Q5.png.
Run: PYTHONUTF8=1 py tools/gen/gen_25B-C.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-C.json"
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

def J(*paras):
    return "\n".join(paras)

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "solved", "official": False,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

questions = [
Q(1, "decidability",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $L \in RE \cup coRE$ אזי מתקיים $L \in R$." "\n"
  r"II. אם $\overline{L} \in NP$ אזי מתקיים $L \in RE$." "\n"
  "איזה מהסעיפים הבאים נכון:",
  TWO_CLAIMS, "d",
  J(r"""**טענה I לא נכונה:** $A_{TM} \in RE \subseteq RE \cup coRE$ אבל $A_{TM} \notin R$.""",
    r"""**טענה II נכונה:** $NP \subseteq R$, ולכן $\overline{L} \in R$. $R$ סגורה למשלים ולכן $L \in R \subseteq RE$.""")),

Q(2, "classification",
  r"תהי $L$ שפה כך שמתקיים: $\overline{ALL_{TM}} \le_m L$." "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "d",
  J(r"""**הוכחת ד:** ידוע ש-$ALL_{TM} \notin RE \cup coRE$, כלומר גם $ALL_{TM}$ וגם $\overline{ALL_{TM}}$ לא ניתנות לקבלה.""",
    r"""מ-$\overline{ALL_{TM}} \le_m L$ ומשפט הרדוקציה: אילו $L \in RE$ אז $\overline{ALL_{TM}} \in RE$ – סתירה. לכן $L \notin RE$.""",
    r"""כמו כן $ALL_{TM} \le_m \overline{L}$ (משלימים את שני הצדדים), ולכן באותו אופן $\overline{L} \notin RE$."""),
  note="Same format as 25B-A Q2 (EQ_TM ≤m L, key ד); here with the complement of ALL_TM (overline over the whole ALL_TM)."),

Q(3, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M, w\rangle \mid M \text{ accepts } w \text{ and } M \text{ accepts } w^R\}$$"
  r"כלומר, $\langle M, w\rangle \in L$ אם $M$ עוצרת על $w$ במצב מקבל וגם $M$ עוצרת על $w^R$ במצב מקבל." "\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "b",
  J(r"""**$L \in RE$:** בהינתן $\langle M,w\rangle$ נריץ את $M$ על $w$; אם קיבלה – נריץ את $M$ על $w^R$; אם גם זו קיבלה – נקבל. אם $\langle M,w\rangle \in L$ שתי הריצות מסתיימות בקבלה.""",
    r"""**$L \notin R$:** רדוקציה $A_{TM} \le_m L$: $f(\langle M,w\rangle) = \langle M_w, w\rangle$ כאשר $M_w$ על קלט $x$ מתעלמת מ-$x$, מריצה את $M$ על $w$ ועונה כמוה. אם $M$ מקבלת את $w$ אז $M_w$ מקבלת גם את $w$ וגם את $w^R$; אחרת $M_w$ לא מקבלת אף מילה.""",
    r"""לכן $L \in RE \setminus R$ – תשובה ב (ובפרט לא א, ג, ד)."""),
  note="Set-builder condition printed in English; kept via \\text{}."),

Q(4, "tm",
  r"יהיו $M_1, M_2$ מ\"ט לא-דטרמיניסטיות כך שמתקיים $L(M_1) = L(M_2)$." "\n"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. לכל קלט $w$, אם קיים מסלול חישוב של $M_1$ על $w$ שמסתיים ב-REJECT אזי קיים מסלול חישוב של $M_2$ על $w$ שמסתיים ב-ACCEPT או ב-REJECT." "\n"
  r"II. לכל קלט $w$, אם כל מסלול חישוב של $M_1$ על $w$ מסתיים ב-ACCEPT אזי כל מסלול חישוב של $M_2$ על $w$ מסתיים ב-ACCEPT או ב-REJECT." "\n"
  "איזה מהסעיפים הבאים נכון:",
  TWO_CLAIMS, "b",
  J(r"""**טענה I לא נכונה:** $M_1 = M_{REJ}$ (דוחה מיד כל קלט), $M_2 = M_{LOOP}$ (לא עוצרת על אף קלט). $L(M_1) = L(M_2) = \emptyset$, ל-$M_1$ יש מסלול שמסתיים ב-REJECT, אבל ל-$M_2$ אין אף מסלול שעוצר.""",
    r"""**טענה II לא נכונה:** $M_1$ מקבלת מיד כל קלט; $M_2$ מנחשת בכל קלט: באחד הענפים מקבלת ובענף אחר נכנסת ללולאה אינסופית. $L(M_1) = L(M_2) = \Sigma^*$, כל מסלולי $M_1$ מסתיימים ב-ACCEPT, אבל ל-$M_2$ יש מסלול שלא עוצר."""),
  note="Option ג printed with a typo 'ענה I נכונה…' (for 'טענה'); standard TWO_CLAIMS wording used. "
       "Variant of 25B-B Q4 (different claims). 'כל' in claim II ('אזי כל מסלול חישוב של M2') verified in the text layer."),

Q(5, "tm",
  "תהי $M$ מכונת הטיורינג הבסיסית הבאה:\n"
  "איזו מהטענות הבאות היא נכונה?",
  opts(r"מתקיים $L(M) \in R$ וגם $M$ מכונה מכריעה",
       r"מתקיים $L(M) \notin R$ וגם $M$ מכונה מכריעה",
       r"מתקיים $L(M) \in R$ וגם $M$ מכונה לא-מכריעה",
       "כל הטענות האחרות לא נכונות"),
  "c",
  J(r"""**מעקב אחרי המכונה** (קלט $x = x_1x_2\cdots$ מעל $\{0,1\}$, הראש בתא 1):""",
    r"""• $q_0$ קוראת את $x_1$ (או רווח), משאירה אותו, זזה ימינה ועוברת ל-$q_1$.""",
    r"""• $q_1$ קוראת את התו בתא 2: רווח (כלומר $|x| \le 1$) – עוברת ל-rej; $1$ – עוברת ל-acc; $0$ – זזה שמאלה לתא 1 וחוזרת ל-$q_0$.""",
    r"""• במקרה האחרון $q_0$ שוב זזה ימינה, $q_1$ שוב קוראת $0$ וחוזר חלילה – לולאה אינסופית.""",
    r"""לכן $L(M) = \{x \mid |x| \ge 2,\ x_2 = 1\} = (0+1)1(0+1)^*$ – שפה רגולרית ובפרט ב-$R$. אבל $M$ לא עוצרת למשל על $00$, ולכן אינה מכריעה. תשובה ג; א, ב, ד לא נכונות."""),
  image="images/exams/25B-C-Q5.png",
  note="Diagram: q0 --(⊔→⊔,R | 0→0,R | 1→1,R)--> q1; q1 --(0→0,L)--> q0; q1 --(⊔→0,L)--> rej; q1 --(1→0,L)--> acc. Same option set as 25B-B Q10."),

Q(6, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle A_1, A_2\rangle \mid (*)\}$$"
  r"(*): $A_1$ הוא אס\"ד וגם $A_2$ הוא אס\"ד כך שמתקיים $L(A_1) \subseteq L(A_2)$",
  DEC4, "a",
  J(r"""$L(A_1) \subseteq L(A_2)$ אם"ם $L(A_1) \cap \overline{L(A_2)} = \emptyset$. בהינתן שני אס"דים ניתן לבנות אס"ד ל-$\overline{L(A_2)}$ (החלפת מצבים מקבלים), אוטומט מכפלה לחיתוך, ולבדוק בזמן סופי אם שפתו ריקה (האם מצב מקבל ישיג מההתחלתי – $E_{DFA}$ כריעה). לכן $L$ ניתנת להכרעה."""),
  note="PRINT ERROR: the options are lettered ה/ו/ז/ח instead of א/ב/ג/ד (content = the standard four decidability options, same order); answer = first option (printed ה). No question line printed after the definition."),

Q(7, "time_p",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. תהי $f: \Sigma^* \to \Sigma^*$ פונקציה המקיימת שלכל $x$ מתקיים $f(x) \in \{01, 10\}$, אזי $f$ ניתנת לחישוב" "\n"
  r"II. תהי $f: \Sigma^* \to \Sigma^*$ פונקציה המקיימת שלכל $x$ מתקיים $f(x) \in \{01, 10\}$, אזי $f$ ניתנת לחישוב **בזמן פולינומי**" "\n"
  "איזה מהסעיפים הבאים נכון:",
  TWO_CLAIMS, "b",
  J(r"""**שתי הטענות לא נכונות:** נגדיר $f(x) = 01$ אם $x \in A_{TM}$ ו-$f(x) = 10$ אחרת. $f$ מקיימת את הנתון, אבל אילו הייתה ניתנת לחישוב היינו מכריעים את $A_{TM}$ (מחשבים $f(x)$ ובודקים את התו הראשון). לכן $f$ לא ניתנת לחישוב, ובפרט לא בזמן פולינומי."""),
  note="'בזמן פולינומי' underlined in the source; rendered bold. Same stem as 25B-A Q3 with {01,10} instead of {0,1,11,111} (25B-A key ב — agrees)."),

Q(8, "poly_reductions",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $A \le_m \overline{B}$ וגם $\overline{B} \le_p C$ אזי מתקיים $A \le_m C$." "\n"
  r"II. אם $A \le_m \overline{B}$ וגם $\overline{B} \le_p C$ אזי מתקיים $A \le_p C$." "\n"
  "איזה מהסעיפים הבאים נכון:",
  TWO_CLAIMS, "c",
  J(r"""**טענה I נכונה:** כל רדוקציה פולינומית היא רדוקציית מיפוי, ולכן $\overline{B} \le_m C$, ומטרנזיטיביות $A \le_m C$.""",
    r"""**טענה II לא נכונה:** הרדוקציה $A \le_m \overline{B}$ יכולה לרוץ בזמן לא פולינומי. דוגמה: $\overline{B} = C = \{1\}$ ו-$A$ שפה כריעה שאינה ב-$P$ (קיימת כזו לפי משפט היררכיית הזמן). $A \le_m \{1\}$ (מכריעים את $A$ ומחזירים $1$ או $0$), $\overline{B} \le_p C$ בזהות, אבל $A \le_p \{1\}$ היה גורר $A \in P$."""),
  note="Claim I is identical to 26B-A Q8 claim I (key: true — agrees). Options continue on p5."),

Q(9, "npc",
  r"**נתבונן בטענה הבאה:** אם $A \in NPC$ וגם $B \in NPC$ אזי מתקיים $A \le_m B$ וגם $B \le_m A$.",
  CLAIM2, "a",
  J(r"""**הטענה נכונה:** לפי הגדרת $NP$-שלמות, $A \in NP$ ו-$B$ היא $NP$-קשה ולכן $A \le_p B$; באופן סימטרי $B \le_p A$. כל רדוקציה פולינומית היא בפרט רדוקציית מיפוי, ולכן $A \le_m B$ וגם $B \le_m A$.""")),

Q(10, "npc",
  "תהי $L$ שפה לא-טריוויאלית. איזו מהטענות הבאות היא נכונה?",
  opts(r"אם $P \ne NP$ וגם $L \in NPC$ אזי $L \in P$",
       r"אם $P \ne NP$ וגם $L \in P$ אזי $L \in NPC$",
       r"אם $L \in NPC$ וגם $\overline{L} \in P$ אזי $P \ne NP$",
       r"אם $P = NP$ וגם $L \in NPC$ אזי $L \in P$"),
  "d",
  J(r"""**הוכחת ד:** $L \in NPC \subseteq NP = P$.""",
    r"""**הפרכת א, ב:** אם $P \ne NP$ אז $P \cap NPC = \emptyset$, ולכן שפה $NP$-שלמה אינה ב-$P$ ושפה ב-$P$ אינה $NP$-שלמה.""",
    r"""**הפרכת ג:** $P$ סגורה למשלים, ולכן $\overline{L} \in P$ גורר $L \in P$; יחד עם $L \in NPC$ נקבל $P \cap NPC \ne \emptyset$, כלומר $P = NP$ – ההפך מהמסקנה."""),
  note="Option ג is the same as 25B-A Q10 ג (refuted there by the key)."),

Q(11, "decidability",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid M = \langle Q, \Sigma, \Gamma, q_0, q_{acc}, q_{rej}, \delta\rangle,\ |Q| = 2\}$$"
  r"כלומר, $\langle M\rangle \in L$ אם יש בה בדיוק שני מצבים. איזו מהטענות הבאות נכונה?",
  DEC4, "a",
  J(r"""מספר המצבים הוא חלק מהקידוד $\langle M\rangle$. מכונה מכריעה פשוט מפענחת את הקידוד וסופרת את המצבים (ודוחה קלט שאינו קידוד חוקי) – בזמן סופי, בלי להריץ את $M$. לכן $L$ ניתנת להכרעה."""),
  note="Tuple printed with < > brackets; rendered as \\langle \\rangle."),

Q(12, "closure",
  r"**נתבונן בטענה הבאה:** תהיינה $A, B$ שפות לא-טריוויאליות כך שמתקיים: $A \cap B \in R$ וגם $A \cup B \in R$. אזי מתקיים $A \in RE$ וגם $B \in RE$.",
  CLAIM2, "b",
  J(r"""**הטענה לא נכונה:** $A = \overline{A_{TM}}$, $B = A_{TM}$. שתיהן לא טריוויאליות, $A \cap B = \emptyset \in R$ ו-$A \cup B = \Sigma^* \in R$, אבל $A = \overline{A_{TM}} \notin RE$.""")),

Q(13, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid L(M) = (\Sigma\Sigma)^*\}$$"
  r"כלומר, $\langle M\rangle \in L$ אם השפה של $M$ מכילה את כל המילים באורך זוגי וגם לא מכילה אף מילה באורך אי-זוגי. איזו מהטענות הבאות נכונה?",
  DEC4, "d",
  J(r"""**$L \notin RE$:** רדוקציה $\overline{H_{TM}} \le_m L$: $f(\langle M,w\rangle) = \langle M'\rangle$, כאשר $M'$ על קלט $x$: אם $|x|$ זוגי – קבל; אחרת הרץ את $M$ על $w$ וקבל. אם $M$ לא עוצרת על $w$ אז $L(M') = (\Sigma\Sigma)^*$; אחרת $L(M') = \Sigma^*$.""",
    r"""**$\overline{L} \notin RE$:** רדוקציה $H_{TM} \le_m L$ (ולכן $\overline{H_{TM}} \le_m \overline{L}$): $f(\langle M,w\rangle) = \langle M''\rangle$, כאשר $M''$ על קלט $x$: הרץ את $M$ על $w$; אם $|x|$ זוגי קבל, אחרת דחה. אם $M$ עוצרת על $w$ אז $L(M'') = (\Sigma\Sigma)^*$; אחרת $L(M'') = \emptyset$.""")),

Q(14, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M, w\rangle \mid (*)\}$$"
  "(*): $M$ היא מכונת טיורינג שמקבלת מילה $w$ לאחר ביצוע של בדיוק מספר זוגי של צעדי חישוב\n"
  "איזו מהטענות הבאות נכונה?",
  DEC4, "b",
  J(r"""**$L \in RE$:** נריץ את $M$ על $w$ תוך ספירת צעדים; אם $M$ מקבלת – נקבל אם מספר הצעדים זוגי ונדחה אחרת.""",
    r"""**$L \notin R$:** רדוקציה $A_{TM} \le_m L$: $f(\langle M,w\rangle) = \langle M', w\rangle$, כאשר $M'$ מסמלצת את $M$ וסופרת צעדים, ולפני שהיא נכנסת למצב המקבל היא מוסיפה צעד "ריק" אחד אם הזוגיות אינה מתאימה. כך $M'$ מקבלת את $w$ אחרי מספר זוגי של צעדים אם"ם $M$ מקבלת את $w$.""",
    r"""לכן $L \in RE \setminus R$ – תשובה ב."""),
  note="Set-builder condition printed over three lines inside the braces; merged into a (*) line."),
]

contexts = {
  "blk": {"kind": "text", "title": "בלוק של שאלות 15–18",
          "text": r"בהינתן גרף $G$ לא-מכוון ומספר טבעי $k$, נגדיר את הפונקציה הבאה: $f(\langle G, k\rangle) = \langle \overline{G}, k\rangle$" "\n"
                  r"כאשר $\overline{G}$ הוא הגרף המשלים של הגרף $G$." "\n"
                  "בנוסף, נגדיר את השפה הבאה:\n"
                  r"$$L = \{\langle G, k\rangle \mid (*)\}$$"
                  r"(*): הגרף הלא מכוון $G$ מכיל תת קבוצה $S$ של קודקודים בגודל $k$ שהיא קליקה וגם $G$ מכיל תת קבוצה $T$ של קודקודים בגודל $k+1$ שהיא בלתי תלויה" "\n"
                  "**ענו נכון או לא נכון, לכל אחת מהטענות הבאות:**"},
}

questions += [
Q(15, "poly_reductions", r"אם $f(\langle G, k\rangle) \in L$ אזי $\langle G, k\rangle \in CLIQUE$", TF, "a",
  J(r"""**נכון:** $f(\langle G,k\rangle) = \langle \overline{G}, k\rangle \in L$, ולכן בפרט ב-$\overline{G}$ יש קבוצה בלתי תלויה $T$ בגודל $k+1$. $T$ היא קליקה בגודל $k+1$ ב-$G$, וכל $k$ מקודקודיה הם קליקה בגודל $k$ ב-$G$. לכן $\langle G,k\rangle \in CLIQUE$."""),
  contextId="blk"),
Q(16, "poly_reductions", r"אם $\langle G, k\rangle \in CLIQUE$ אזי $f(\langle G, k\rangle) \in L$", TF, "b",
  J(r"""**לא נכון:** $G = K_k$ (קליקה מלאה על $k \ge 2$ קודקודים). $\langle G,k\rangle \in CLIQUE$, אבל $\overline{G}$ הוא גרף ללא צלעות על $k$ קודקודים, ואין בו קליקה בגודל $k$ (וגם אין בו $k+1$ קודקודים בכלל). לכן $f(\langle G,k\rangle) \notin L$."""),
  contextId="blk"),
Q(17, "poly_reductions", r"אם $f(\langle G, k\rangle) \in IS$ אזי $\langle G, k\rangle \in L$", TF, "b",
  J(r"""**לא נכון:** $f(\langle G,k\rangle) = \langle \overline{G}, k\rangle \in IS$ שקול לכך שב-$G$ יש קליקה בגודל $k$. אבל $L$ דורשת גם קבוצה בלתי תלויה בגודל $k+1$. דוגמה: $G = K_k$ עם $k \ge 1$ – יש קליקה בגודל $k$, אבל אין אפילו $k+1$ קודקודים. לכן $\langle G,k\rangle \notin L$."""),
  contextId="blk"),
Q(18, "poly_reductions", r"אם $\langle G, k\rangle \in IS$ אזי $f(\langle G, k\rangle) \in L$", TF, "b",
  J(r"""**לא נכון:** $f(\langle G,k\rangle) \in L$ דורש שב-$\overline{G}$ תהיה קבוצה בלתי תלויה בגודל $k+1$, כלומר קליקה בגודל $k+1$ ב-$G$. דוגמה: $G$ גרף ללא צלעות על $k \ge 1$ קודקודים – $\langle G,k\rangle \in IS$, אבל ב-$G$ אין קליקה בגודל $k+1$. לכן $f(\langle G,k\rangle) \notin L$."""),
  contextId="blk"),
]

exam = {
  "examCode": "25B-C",
  "examLabel": "2025 סמסטר ב מועד ג",
  "year": 2025,
  "examDate": "7.9.2025",
  "sourceFile": "מבחנים/2025/מס ב מועד ג 7-9.pdf",
  "keyFile": "none — answers solved (stage 1, tools/SOLVE_GUIDE.md), pending blind re-solve",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 19))
def _fix(x):
    """raw strings keep the backslash of \\" (e.g. in מ\\"ט) -> strip it."""
    if isinstance(x, str): return x.replace('\\"', '"')
    if isinstance(x, list): return [_fix(v) for v in x]
    if isinstance(x, dict): return {k: _fix(v) for k, v in x.items()}
    return x
exam = _fix(exam)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
