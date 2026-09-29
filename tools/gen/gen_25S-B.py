# -*- coding: utf-8 -*-
"""Generator for tools/raw/25S-B.json (2025 קיץ מועד ב; no date printed).
Transcribed by hand from the rendered pages of `מבחנים/2025/2025 קיץ מועד ב.pdf` (6 pages, p1 blank,
no cover; header "HIT חישוביות 2025 קיץ ב"; metadata author = a private person -> probably a
student retype). Option orders are kept exactly as printed (they differ from the staff's usual
order). NO answer key exists: every answer is SOLVED (stage 1 of tools/SOLVE_GUIDE.md).
Observation: every solved answer is the FIRST printed option (א) — consistent with a retype that
lists the correct answer first; recorded per question in `note` as partial evidence only.
Run: PYTHONUTF8=1 py tools/gen/gen_25S-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25S-B.json"
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

BOTH_T = "שתי הטענות I, II הן נכונות"
BOTH_F = "שתי הטענות I, II הן לא-נכונות"
I_ONLY = "טענה I נכונה וגם טענה II לא-נכונה"
II_ONLY = "טענה II נכונה וגם טענה I לא-נכונה"
D_R = "השפה $L$ ניתנת להכרעה"
D_RE = "השפה $L$ ניתנת לקבלה אבל לא-ניתנת להכרעה"
D_CO = r"השפה $L$ לא-ניתנת לקבלה אבל $\overline{L}$ ניתנת לקבלה"
D_NO = r"השפה $L$ לא-ניתנת לקבלה וגם $\overline{L}$ לא-ניתנת לקבלה"
FIRST = "form evidence: solved answer = first printed option (א), as for every question in this file (retype likely lists the answer first) — agrees."

def J(*paras):
    return "\n".join(paras)

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "solved", "official": False,
         "confidence": "high", "explanation": explanation, "note": FIRST}
    q.update(kw)
    return q

questions = [
Q(1, "mapping_reductions",
  r"תהיינה שתי שפות, $A, B$, המקיימות $A \le_m B$." "\n"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $A \in coRE$ אז $B \in coRE$" "\n"
  r"II. אם $B \in coRE$ אז $A \in coRE$" "\n"
  "איזה מהסעיפים הבאים נכון:",
  opts(II_ONLY, BOTH_F, BOTH_T, I_ONLY), "a",
  J(r"""**טענה II נכונה:** $A \le_m B$ גורר $\overline{A} \le_m \overline{B}$. אם $B \in coRE$ אז $\overline{B} \in RE$, ולפי משפט הרדוקציה $\overline{A} \in RE$, כלומר $A \in coRE$.""",
    r"""**טענה I לא נכונה:** $A = \{0\}$, $B = A_{TM}$. $A \in R$ ו-$B$ לא טריוויאלית, ולכן $A \le_m B$; $A \in coRE$ אבל $A_{TM} \notin coRE$.""")),

Q(2, "decidability",
  r"תהי $L$ שפה כך שמתקיים: $L \in RE$ וגם קיימת שפה $L' \in coRE$ שעבורה $L \le_m L'$." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(D_R, D_NO, D_RE, D_CO), "a",
  J(r"""**הוכחת א:** מ-$L \le_m L'$ נקבל $\overline{L} \le_m \overline{L'}$, ו-$\overline{L'} \in RE$, ולכן לפי משפט הרדוקציה $\overline{L} \in RE$. יחד עם $L \in RE$ נקבל $L \in R$.""",
    r"""**הפרכת השאר:** ב, ד טוענות $L \notin RE$ – סותר את הנתון; ג טוענת $L \notin R$ – סותר את ההוכחה.""")),

Q(3, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M, w\rangle \mid M \text{ stops on } w \text{ or } M \text{ stops on } w^R\}$$"
  r"כלומר, $\langle M, w\rangle \in L$ אםם $M$ עוצרת על $w$ במצב מקבל או $M$ עוצרת על $w^R$ במצב מקבל." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(D_RE, D_R, D_CO, D_NO), "a",
  J(r"""בשתי הקריאות ("עוצרת" או "עוצרת במצב מקבל") $L \in RE \setminus R$: מקבלים ע"י הרצה מקבילית של $M$ על $w$ ועל $w^R$; ורדוקציה מ-$H_{TM}$ (או $A_{TM}$) ע"י $f(\langle M,w\rangle) = \langle M_w, w\rangle$ כאשר $M_w$ מתעלמת מהקלט ומריצה את $M$ על $w$."""),
  confidence="low",
  hold="Stem is internally inconsistent (likely a retype slip): the formula says 'M stops on w or M stops on w^R' but the Hebrew gloss says 'עוצרת … במצב מקבל' (accepts). Both readings give א (RE\\R), but per instructions for this suspected student retype, mistyped stems are held.",
  note="Printed gloss: 'עוצרת על wבמצב מקבל' (missing space) and 'אםם'. " + FIRST),

Q(4, "tm",
  r"תהי $M_1$ מ\"ט דטרמיניסטית, ותהי $M_2$ מ\"ט לא-דטרמיניסטיות, כך שמתקיים $L(M_1) = L(M_2)$." "\n"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. לכל קלט $w$, אם $M_1$ דוחה את $w$, אזי כל מסלול חישוב של $M_2$ על $w$ מסתיים ב-REJECT." "\n"
  r"II. לכל קלט $w$, אם $M_1$ לא עוצרת על $w$, אזי לא קיים מסלול חישוב של $M_2$ על $w$ שמסתיים ב-ACCEPT." "\n"
  "איזה מהסעיפים הבאים נכון:",
  opts(II_ONLY, BOTH_F, BOTH_T, I_ONLY), "a",
  J(r"""**טענה II נכונה:** אם $M_1$ לא עוצרת על $w$ אז $w \notin L(M_1) = L(M_2)$, ולכן אין ל-$M_2$ מסלול מקבל על $w$.""",
    r"""**טענה I לא נכונה:** $M_1 = M_{REJ}$ (דוחה מיד כל קלט), $M_2 = M_{LOOP}$ (לא עוצרת על אף קלט). $L(M_1) = L(M_2) = \emptyset$, $M_1$ דוחה כל $w$, אבל אף מסלול של $M_2$ לא מסתיים ב-REJECT."""),
  note="Printed 'מ\"ט לא-דטרמיניסטיות' (plural, sic) for M2. " + FIRST),

Q(5, "decidability",
  "תהי $M$ מ\"ט.\n"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. ייתכן $L(M) \in R$ וגם $M$ מכונה לא-מכריעה" "\n"
  r"II. ייתכן $L(M) \notin R$ וגם $M$ מכונה מכריעה" "\n"
  "איזה מהסעיפים הבאים נכון:",
  opts(I_ONLY, II_ONLY, BOTH_F, BOTH_T), "a",
  J(r"""**טענה I נכונה:** $M$ שמקבלת את $\varepsilon$ ונכנסת ללולאה על כל קלט אחר: $L(M) = \{\varepsilon\} \in R$ אבל $M$ לא עוצרת על כל קלט.""",
    r"""**טענה II לא נכונה:** אם $M$ מכריעה אז היא עוצרת על כל קלט ומכריעה את $L(M)$, ולכן $L(M) \in R$.""")),

Q(6, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle A_1, A_2\rangle \mid (*)\}$$"
  r"(*): $A_1$ הוא אסל\"ד וגם $A_2$ הוא אסל\"ד כך שמתקיים $L(A_1) \cap L(A_2) = \emptyset$" "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(D_R, D_RE, D_CO, D_NO), "a",
  J(r"""בהינתן שני אסל"דים (אוטומטים סופיים לא-דטרמיניסטיים) ניתן להמיר כל אחד לאס"ד שקול (בניית תת-הקבוצות), לבנות אוטומט מכפלה לחיתוך ולבדוק בזמן סופי אם שפתו ריקה ($E_{DFA}$ כריעה). לכן $L$ ניתנת להכרעה."""),
  note="Empty set printed as ϕ; rendered \\emptyset. 'אסל\"ד' = NFA (the answer is the same for DFAs). " + FIRST),

Q(7, "time_p",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. תהי $f: \Sigma^* \to \Sigma^*$ פונקציה המקיימת שלכל $x$ מתקיים $f(x) \in \{1\}$, אזי $f$ ניתנת לחישוב" "\n"
  r"II. תהי $f: \Sigma^* \to \Sigma^*$ פונקציה המקיימת שלכל $x$ מתקיים $f(x) \in \{1\}$, אזי $f$ ניתנת לחישוב **בזמן פולינומי**" "\n"
  "איזה מהסעיפים הבאים נכון:",
  opts(BOTH_T, BOTH_F, I_ONLY, II_ONLY), "a",
  J(r"""**שתי הטענות נכונות:** הקבוצה $\{1\}$ היא יחידון, ולכן $f$ היא בהכרח הפונקציה הקבועה $f(x) = 1$. מכונה שמוחקת את הקלט (בזמן לינארי) וכותבת $1$ מחשבת אותה, ובפרט בזמן פולינומי."""),
  note="'בזמן פולינומי' underlined in the source; rendered bold. Variant of 25B-A Q3 ({0,1,11,111}, key ב) / 25B-C Q7 ({01,10}); with the singleton {1} f is forced to be constant, so the answer flips to א. "
       "Stage 2 please check the set is really '{1}' (text layer also reads {𝟏}). " + FIRST),

Q(8, "poly_reductions",
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $A \le_m \overline{B}$ וגם $B \le_p C$ אזי מתקיים $A \le_p \overline{C}$." "\n"
  r"II. אם $A \le_m \overline{B}$ וגם $B \le_p C$ אזי מתקיים $A \le_m \overline{C}$." "\n"
  "איזה מהסעיפים הבאים נכון:",
  opts(II_ONLY, I_ONLY, BOTH_T, BOTH_F), "a",
  J(r"""**טענה II נכונה:** $B \le_p C$ גורר $\overline{B} \le_p \overline{C}$ (אותה פונקציה), ובפרט $\overline{B} \le_m \overline{C}$. מטרנזיטיביות $A \le_m \overline{C}$.""",
    r"""**טענה I לא נכונה:** הרדוקציה $A \le_m \overline{B}$ יכולה לא להיות פולינומית. דוגמה: $B = C = \{0\}$ (ולכן $\overline{B} = \overline{C}$) ו-$A$ שפה כריעה שאינה ב-$P$ (קיימת לפי משפט היררכיית הזמן). $A \le_m \overline{B}$ כי $A \in R$ ו-$\overline{B}$ לא טריוויאלית, $B \le_p C$ בזהות, אבל $A \le_p \overline{C}$ היה גורר $A \in P$ (כי $\overline{C} \in P$)."""),
  note="Overlines (on B in the premise and on C in the conclusions only) verified at 4x zoom. " + FIRST),

Q(9, "np",
  r"**נתבונן בטענה הבאה:** אם קיימת שפה $L \in NPC$ כך ש-$L \le_p \overline{L}$ אזי $NP$ סגורה למשלים.",
  opts("הטענה נכונה", "הטענה לא נכונה"), "a",
  J(r"""**הטענה נכונה:** מ-$L \le_p \overline{L}$ נקבל (משלימים את שני הצדדים) $\overline{L} \le_p L$. $L \in NP$ ו-$NP$ סגורה תחת רדוקציה פולינומית, ולכן $\overline{L} \in NP$.""",
    r"""תהי $A \in NP$. $L$ היא $NP$-קשה ולכן $A \le_p L$, כלומר $\overline{A} \le_p \overline{L}$, ו-$\overline{L} \in NP$, ולכן $\overline{A} \in NP$. כלומר $NP$ סגורה למשלים.""")),

Q(10, "npc",
  r"יהיו $L_1, L_2$ שפות לא-טריוויאליות." "\n"
  "נתבונן בשתי הטענות הבאות:\n"
  r"I. אם $L_1 \in NP$ וגם $L_2 \in NP$ וגם $L_2 \le_p L_1$ אז $L_1 \in NPC$" "\n"
  r"II. אם $L_2 \in P$ וגם $L_2 \le_p L_1$ אז $L_1 \in P$" "\n"
  "איזה מהסעיפים הבאים נכון:",
  opts(BOTH_F, II_ONLY, I_ONLY, BOTH_T), "a",
  J(r"""**טענה I לא נכונה (לא נובעת):** רדוקציה משפה **אחת** $L_2$ לא מראה ש-$L_1$ היא $NP$-קשה. למשל $L_1 = L_2 = \{0\}$: מקיימות את ההנחות, אבל $\{0\} \in P$ ולכן היא $NP$-שלמה רק אם $P = NP$ – המסקנה לא נובעת מההנחות.""",
    r"""**טענה II לא נכונה:** $L_2 = \{0\} \in P$ ו-$L_1 = A_{TM}$ (לא טריוויאלית): $L_2 \le_p L_1$ (מכריעים את $L_2$ בזמן פולינומי ומחזירים קידוד קבוע שבתוך $A_{TM}$ או מחוצה לה), אבל $A_{TM} \notin P$."""),
  note="Claim I is 'not provable' (it holds iff P=NP, since under P=NP every nontrivial NP language is NP-complete) — refuted per the course convention (cf. 25B-A Q10 ג, 25B-C Q10 ג). " + FIRST),

Q(11, "decidability",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid M = \langle Q, \Sigma, \Gamma, q_0, q_{acc}, q_{rej}, \delta\rangle,\ |Q| = 3\}$$"
  r"כלומר, $\langle M\rangle \in L$ אםם $M$ מכונת טיורינג עם בדיוק שלושה מצבים." "\n"
  "איזו מהטענות הבאות נכונה:",
  opts(D_R, D_RE, D_CO, D_NO), "a",
  J(r"""מספר המצבים הוא חלק מהקידוד $\langle M\rangle$; מכונה מכריעה מפענחת את הקידוד וסופרת את המצבים בזמן סופי, בלי להריץ את $M$. לכן $L$ ניתנת להכרעה."""),
  note="Tuple printed with < > brackets; rendered as \\langle \\rangle. Same as 25B-C Q11 with |Q| = 3. " + FIRST),

Q(12, "closure",
  r"**נתבונן בטענה הבאה:** תהיינה $A, B$ שפות לא-טריוויאליות כך שמתקיים: $A \cap B \in RE$ וגם $\overline{A \cap B} \in RE$. אזי מתקיים $A \in R$ וגם $B \in R$.",
  opts("הטענה לא נכונה", "הטענה נכונה"), "a",
  J(r"""**הטענה לא נכונה:** $A = A_{TM}$, $B = \overline{A_{TM}}$. שתיהן לא טריוויאליות ו-$A \cap B = \emptyset$, כך ש-$A \cap B \in RE$ וגם $\overline{A \cap B} = \Sigma^* \in RE$, אבל $A_{TM} \notin R$."""),
  note="The overline covers the whole A ∩ B (verified at 5x zoom). " + FIRST),

Q(13, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M\rangle \mid 101 \in L(M)\}$$"
  "איזו מהטענות הבאות נכונה:",
  opts(D_RE, D_NO, D_R, D_CO), "a",
  J(r"""**$L \in RE$:** מריצים את $M$ על $101$ ומקבלים אם היא מקבלת.""",
    r"""**$L \notin R$:** רדוקציה $A_{TM} \le_m L$: $f(\langle M,w\rangle) = \langle M_w\rangle$ כאשר $M_w$ מתעלמת מהקלט, מריצה את $M$ על $w$ ועונה כמוה. $101 \in L(M_w)$ אם"ם $M$ מקבלת את $w$.""")),

Q(14, "classification",
  "נגדיר את השפה הבאה:\n"
  r"$$L = \{\langle M, w\rangle \mid (*)\}$$"
  "(*): $M$ היא מכונת טיורינג שמקבלת את $w^R$\n"
  "איזו מהטענות הבאות נכונה:",
  opts(D_RE, D_R, D_CO, D_NO), "a",
  J(r"""**$L \in RE$:** מחשבים את $w^R$ ומריצים עליו את $M$; מקבלים אם היא מקבלת.""",
    r"""**$L \notin R$:** רדוקציה $A_{TM} \le_m L$: $f(\langle M,w\rangle) = \langle M, w^R\rangle$ (ניתנת לחישוב), ו-$(w^R)^R = w$, כך ש-$\langle M, w^R\rangle \in L$ אם"ם $M$ מקבלת את $w$.""")),
]

contexts = {
  "blk": {"kind": "text", "title": "בלוק של שאלות 15–18",
          "text": r"בהינתן גרף $G$ לא-מכוון עם $n$ קדקודים, ומספר טבעי $k$, נגדיר את הפונקציה הבאה:" "\n"
                  r"$$f(\langle G, k\rangle) = \langle \overline{G}, n-k\rangle$$"
                  r"כאשר $\overline{G}$ הוא הגרף המשלים של הגרף $G$." "\n"
                  "בנוסף, נגדיר את השפה הבאה:\n"
                  r"$$L = \{\langle G, k\rangle \mid (*)\}$$"
                  r"(*): הגרף הלא מכוון $G$ מכיל תת קבוצה $S$ של קודקודים בגודל $n-k$ שהיא כיסוי קדקודים וגם $G$ מכיל תת קבוצה $T$ של קודקודים בגודל $k$ שהיא קליקה" "\n"
                  "**ענו נכון או לא נכון, לכל אחת מהטענות הבאות:**"},
}

BLK = (r"""**עובדה:** $S$ כיסוי קדקודים בגודל $n-k$ אם"ם $V \setminus S$ קבוצה בלתי תלויה בגודל $k$. לכן $\langle G,k\rangle \in L$ אם"ם ב-$G$ יש גם קבוצה בלתי תלויה בגודל $k$ וגם קליקה בגודל $k$. """
       r"""עבור $f(\langle G,k\rangle) = \langle \overline{G}, n-k\rangle$: ב-$\overline{G}$ יש כיסוי בגודל $k$ (כלומר קבוצה בלתי תלויה בגודל $n-k$ ב-$\overline{G}$ = קליקה בגודל $n-k$ ב-$G$) וקליקה בגודל $n-k$ (= קבוצה בלתי תלויה בגודל $n-k$ ב-$G$). לכן $f(\langle G,k\rangle) \in L$ אם"ם ב-$G$ יש גם קליקה וגם קבוצה בלתי תלויה בגודל $n-k$.""")

questions += [
Q(15, "poly_reductions", r"אם $f(\langle G, k\rangle) \in L$ אזי $\langle G, n-k\rangle \in IS$",
  opts("נכון", "לא נכון"), "a",
  J(BLK, r"""**נכון:** אם $f(\langle G,k\rangle) \in L$ אז ב-$\overline{G}$ יש קליקה $T$ בגודל $n-k$, ו-$T$ היא קבוצה בלתי תלויה בגודל $n-k$ ב-$G$. לכן $\langle G, n-k\rangle \in IS$."""),
  contextId="blk"),
Q(16, "poly_reductions", r"אם $\langle G, n-k\rangle \in IS$ אזי $f(\langle G, k\rangle) \in L$",
  opts("לא נכון", "נכון"), "a",
  J(BLK, r"""**לא נכון:** $G$ גרף ללא צלעות על $n = 3$ קודקודים ו-$k = 1$: ב-$G$ יש קבוצה בלתי תלויה בגודל $n-k = 2$, אבל אין בו קליקה בגודל 2, ולכן $f(\langle G,k\rangle) \notin L$."""),
  contextId="blk"),
Q(17, "poly_reductions", r"אם $f(\langle G, k\rangle) \in IS$ אזי $\langle G, k\rangle \in L$",
  opts("לא נכון", "נכון"), "a",
  J(BLK, r"""**לא נכון:** $f(\langle G,k\rangle) = \langle \overline{G}, n-k\rangle \in IS$ שקול לקליקה בגודל $n-k$ ב-$G$. דוגמה: $G = K_3$, $k = 2$: ב-$G$ יש קליקה בגודל $n-k = 1$, אבל אין בו קבוצה בלתי תלויה בגודל 2, ולכן $\langle G,k\rangle \notin L$."""),
  contextId="blk"),
Q(18, "poly_reductions", r"אם $\langle G, k\rangle \in IS$ אזי $f(\langle G, k\rangle) \in L$",
  opts("לא נכון", "נכון"), "a",
  J(BLK, r"""**לא נכון:** $G$ גרף ללא צלעות על $n = 3$ קודקודים ו-$k = 1$: $\langle G,1\rangle \in IS$, אבל ב-$G$ אין קליקה בגודל $n-k = 2$, ולכן $f(\langle G,k\rangle) \notin L$."""),
  contextId="blk"),
]

# --- RESOLUTIONS (ASK_ADIR items resolved by independent math check; Adir authorized 2026-09-29) ---
def _resolve(num, **kw):
    q = next(q for q in questions if q["num"] == num)
    q.pop("hold", None)
    q.update(kw)
# Stage-2 blind verification (tools/raw/_verify_25S-B.json): all agree.
# Q3: the stem mixes 'halts on' (formula) and 'halts in an accepting state' (gloss); both readings give א and both solvers agree -> released.
_resolve(3, confidence="high", note=r"""Released after stage 2: stem is inconsistent ('stops on' vs 'halts in accept'), but both readings give א (RE\R); both solvers agree.""")

exam = {
  "examCode": "25S-B",
  "examLabel": "2025 קיץ מועד ב",
  "year": 2025,
  "sourceFile": "מבחנים/2025/2025 קיץ מועד ב.pdf",
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
