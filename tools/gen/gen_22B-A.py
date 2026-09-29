# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-A.json (2022 סמסטר ב מועד א, 22.6.2022, ד"ר רדאל בן-אב).
Key = red letter table on the cover of
`מבחנים/2022/סמסטר ב/2022-06-22-Exam-חישוביות-2022-moedA-גרסא-0 SOLUTION.pdf` (a Word draft with
tracked changes). Question/option text transcribed from the clean final copy
`מבחנים/2022/סמסטר ב/סמסטר ב מועד א 22-6-22.pdf` (same question and option order; Q19 was
rewritten by tracked changes and the key fits the final version). No explanations in the key.
Run: PYTHONUTF8=1 py tools/gen/gen_22B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-A.json"
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

TRI = opts("אף פעם לא נכון", "תמיד נכון", "יכול להיות נכון ויכול להיות לא נכון.")
DEC4 = opts(
    "$L$ ניתנת להכרעה.",
    "$L$ ניתנת לקבלה אבל לא ניתנת להכרעה.",
    r"$L$ לא ניתנת לקבלה אבל $\overline{L}$ כן ניתנת לקבלה.",
    r"$L$ לא ניתנת לקבלה וגם $\overline{L}$ לא ניתנת לקבלה.",
)
YESNO = opts("כן", "לא")
NONE = "אף תשובה אינה נכונה"

def rel(x, y):
    return opts(("math", rf"{x} = {y}"), ("math", rf"{x} \subset {y}"), ("math", rf"{x} \supset {y}"), NONE)

def Q(num, topic, question, options, correct, explanation="", **kw):
    q = {"num": num, "topic": topic, "question": question, "options": options,
         "correctId": correct, "answerSource": "letter-table", "official": True,
         "confidence": "high", "explanation": explanation}
    q.update(kw)
    return q

contexts = {
  "rel": {"kind": "text", "title": "יחסים בין שפות – הגדרות לשאלות 9–11",
          "text": r"ידוע כי $H_{TM} \le_m A_{TM}$ וכמו כן $A_{TM} \le_m H_{TM}$. השאלות בחלק זה מתייחסות להגדרות הבאות:" "\n"
                  r"$$A = \{L \mid A_{TM} \le_m L\}$$"
                  r"$$B = \{L \mid \overline{H_{TM}} \le_m L\}$$"
                  r"$$C = \{L \mid A_{TM} \le_m \overline{L} \ \wedge\ \overline{L} \le_m A_{TM}\}$$"
                  "(בהגדרת $C$ מודפס \"וגם\" בין שני התנאים.)"},
  "map": {"kind": "text", "title": "רדוקציית מיפוי – הגדרות לשאלות 12–14",
          "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\n**שפות:**\n"
                  r"$$NEQ_{TM} = \{\langle M_1, M_2\rangle \mid \overline{L(M_1)} \ne \overline{L(M_2)}\}$$"
                  r"$$CE_{TM} = \{\langle M\rangle \mid \overline{L(M)} = \emptyset\}$$"
                  "**פונקציות מיפוי:**\n"
                  r"$$f(\langle M_1, M_2\rangle) = \langle T_{M_1,M_2}\rangle$$"
                  "כאשר המכונה $T_{M_1,M_2}$ מוגדרת באופן הבא:\n"
                  "$T_{M_1,M_2}$ על קלט $w$:\n"
                  "1. הרץ את $M_2$ על הקלט $w$.\n"
                  "2. הרץ את $M_1$ על הקלט $w$.\n"
                  "3. אם $M_1$ סיים במצב \"מקבל\" ו-$M_2$ סיים במצב \"דוחה\" – אזי סיים במצב \"מקבל\"\n"
                  "4. אם $M_1$ סיים במצב \"דוחה\" ו-$M_2$ סיים במצב \"מקבל\" – אזי סיים במצב \"מקבל\"\n"
                  "5. סיים במצב \"דוחה\""},
  "poly": {"kind": "text", "title": "רדוקציה פולינומית – הגדרות לשאלות 15–17",
           "text": "השאלות בחלק זה מתייחסות להגדרות הבאות:\nבעיית הקבוצה הבלתי תלויה מוגדרת באופן הבא:\n"
                   r"$$PClique = \{\langle G, k\rangle \mid (*)\}$$"
                   "(*): $G$ גרף לא מכוון, $k$ מספר שלם, $k$ מספר ראשוני, יש ב-$G$ קליקה בגודל $k$\n"
                   "נגדיר בעיה נוספת:\n"
                   r"$$OClique = \{\langle G, k\rangle \mid (**)\}$$"
                   "(**): $G$ גרף לא מכוון, $k$ מספר שלם, $(k-1)$ הינו מספר ראשוני, יש ב-$G$ קליקה בגודל $k$\n"
                   r"רוצים להוכיח כי $PClique \le_p OClique$. נגדיר את $f$ פונקציית המיפוי הבאה:" "\n"
                   "$G'$ הוא הגרף $G$ בתוספת של צומת אחת חדשה ובתוספת של קשתות מהנקודה החדשה אל כל הצמתים בקליקה המקסימלית בגרף $G$.\n"
                   r"$$f(\langle G, k\rangle) = \langle G', k+1\rangle$$"
                   "לפניך מספר טענות. לכל טענה עליך לקבוע האם היא נכונה או לא."},
}

questions = [
Q(1, "closure",
  r"אם $L_1 \notin RE$ וגם $L_2 \notin RE$, אזי $\overline{L_1} \cap \overline{L_2} \notin RE$.",
  TRI, "c"),
Q(2, "closure",
  r"אם $L_1 \notin RE$ ו-$L_2 \in R$, אזי $\overline{L_2} \cap L_1 \in R$",
  TRI, "c"),
Q(3, "closure",
  "תהי $M_1$ מכונת טיורינג בסיסית שמקבלת שפה שלא ניתנת להכרעה. ותהי $M_2$ מכונת טיורינג שבנויה מהמכונה $M_1$ "
  "על ידי החלפת המצב המקבל במצב דוחה והשארת המצב הדוחה ללא שינוי. אזי "
  r"$\overline{L(M_2)} \cap \overline{L(M_1)}$ ניתנת לקבלה",
  TRI, "a"),
Q(4, "np",
  r"אם $P = coNP$ אז $\overline{CLIQUE} \in NP$.",
  opts("נכון", "לא נכון", "אין מספיק מידע"), "a"),
Q(5, "closure",
  r"נניח שקיימת קבוצה אין סופית של שפות $\{L_i \mid 1 \le i \le \infty\}$ כך ש-$\forall i: L_i \subseteq L_{i+1}$ "
  r"וכן $L_1 \in RE \setminus R$." "\n"
  r"נגדיר $L_\infty = \bigcap_{i=1}^{i=\infty} L_i$. איזה משפט מהבאים נכון?",
  opts(("math", r"L_\infty \in R"), ("math", r"L_\infty \notin RE"), ("math", r"L_\infty \in RE"), ("math", r"L_\infty \in P")),
  "c",
  note="Set printed as '{L_i  1 ≤ i ≤ ∞}' (no separator bar); a \\mid was added."),

Q(6, "classification",
  "לפניך הגדרות של שפות. לכל שפה, עליך לשייך אותה לאחת מהמחלקות המפורטות.\n"
  r"$$L = \{\langle M_1, M_2, M_3\rangle \mid |L(M_1)| + |L(M_2)| + |L(M_3)| = 1\}$$",
  DEC4, "d"),
Q(7, "classification",
  r"$$L = \{\langle M, w\rangle \mid (*)\}$$"
  "(*): $w \\in \\Sigma^*$, $v \\in \\Sigma^*$, $M$ מכונת טיורינג בסיסית כך ש-$L(M)$ היא רק המילים מהצורה $wv$",
  DEC4, "c",
  note="Printed as a two-line set-builder; the Hebrew condition moved to a (*) line."),
Q(8, "classification",
  r"נגדיר $t(\langle M,w\rangle)$ לפי:" "\n"
  r"• $t(\langle M,w\rangle) = k$ אם $M$ מקבלת את $w$ אחרי בדיוק $k$ צעדים" "\n"
  r"• $t(\langle M,w\rangle) = \infty$ אם $M$ לא מקבלת את $w$" "\n"
  r"כלומר $t(\langle M,w\rangle)$ הינה פונקציה שמחזירה את מספר צעדי החישוב עד ש-$M$ מקבלת את $w$." "\n"
  r"$$L = \{\langle M, w\rangle \mid t(\langle M, w\rangle) \le |w|^2\}$$",
  DEC4, "a",
  note="t is printed as a two-case brace with Hebrew conditions; rewritten as two bullet lines."),

Q(9, "mapping_reductions", "קבע מהו היחס בין $A$ ל-$B$:", rel("A", "B"), "d", contextId="rel"),
Q(10, "mapping_reductions", "קבע מהו היחס בין $B$ ל-$C$:", rel("B", "C"), "c", contextId="rel"),
Q(11, "mapping_reductions", "מה מהמשפטים הבאים נכון", rel("A", "C"), "d", contextId="rel"),

Q(12, "mapping_reductions",
  r"האם $f(\langle M_1, M_2\rangle) = \langle T_{M_1,M_2}\rangle$ היא פונקציה ניתנת לחישוב?",
  YESNO, "a", contextId="map",
  note="Option ב 'לא' is printed bold in all copies (formatting artifact, not a mark)."),
Q(13, "mapping_reductions",
  "אם $M_1$ וגם $M_2$ הן מכונות שמכריעות שפה. אזי האם מתקיים\n"
  r"$f(\langle M_1, M_2\rangle) \in CE_{TM} \Leftrightarrow \langle M_1, M_2\rangle \in NEQ_{TM}$?",
  YESNO, "a", contextId="map", confidence="med",
  note="Key table says א (כן). Doubt: L(T)=L(M1)ΔL(M2), so f(x)∈CE_TM iff L(M1)=complement of L(M2), "
       "which is not the same as L(M1)≠L(M2) (e.g. L(M1)={0}, L(M2)={1}). Kept the official key; ASK_ADIR."),
Q(14, "mapping_reductions",
  r"האם $f$ היא מקיימת את תנאי המיפוי ברדוקציה עבור $CE_{TM} \le_m NEQ_{TM}$?",
  opts("כן",
       "לא כי הכיוון של הרדוקציה הוא הפוך.",
       r"לא כי קיימת מילה $w = \langle M_1, M_2\rangle$ שמקיימת $w \in NEQ_{TM}$ אבל $f(w) \notin CE_{TM}$",
       r"לא כי קיימת מילה $w = \langle M_1, M_2\rangle$ שמקיימת $w \notin NEQ_{TM}$ אבל $f(w) \in CE_{TM}$"),
  "b", contextId="map",
  note="Stem prints 'האם f היא מקיימת' (sic)."),

Q(15, "poly_reductions",
  r"אם $\langle G, k\rangle \in PClique$ אז $f(\langle G, k\rangle) \in OClique$.",
  opts("נכון רק אם מספר הקודקודים ב-$G$ הינו מספר ראשוני",
       "נכון רק עבור $k$ זוגי.",
       "לא בהכרח נכון. כלומר לכל $k$ - יכול להיות נכון ויכול להיות לא נכון.",
       "נכון תמיד"),
  "d", contextId="poly"),
Q(16, "poly_reductions",
  r"אם $\langle G, k\rangle \notin PClique$ אז $f(\langle G, k\rangle) \notin OClique$.",
  opts("נכון רק אם מספר הקודקודים ב-$G$ זוגי",
       "נכון רק אם $k$ זוגי",
       "נכון תמיד",
       "המשפט לא מתקיים. כלומר יש מקרים שבהם נכון ויש מקרים בהם איננו נכון."),
  "c", contextId="poly"),
Q(17, "poly_reductions",
  r"האם ההוכחה הנ\"ל מוכיחה כי $PClique \le_p OClique$?",
  opts("לא נכון כי הפונקציה $f$ שהוגדרה לא מקיימת את תנאי הרדוקציה הפולינומיאלית",
       "נכון כי הפונקציה $f$ שהוגדרה מקיימת את כל תנאי הרדוקציה הפולינומיאלית",
       "למרות שהפונקציה $f$ שהוגדרה לא מקיימת את תנאי הרדוקציה הפולינומיאלית – ההוכחה נכונה",
       "הפונקציה $f$ שהוגדרה מקיימת את תנאי הרדוקציה ובכל זאת המשפט לא נכון."),
  "a", contextId="poly",
  note="Section intro says 'בעיית הקבוצה הבלתי תלויה' but defines PClique (clique) — kept as printed."),

Q(18, "npc",
  r"תהינה $A$ ו-$B$ שפות כך שמתקיים $\overline{A} \le_p \overline{B}$ וגם $\overline{B} \le_p \overline{A}$. "
  "מה מהבאים אפשרי אם $P=NP$?",
  opts(r"$A \in P$ ו-$B \notin NPC$",
       r"$A \notin NP$ ו-$B \in P$",
       r"$A \notin P$ ו-$B \in NPC$",
       "$A$ סופית ו-$B$ אינסופית"),
  "d"),
Q(19, "npc",
  r"תהיינה $A$ ו-$B$ שפות כך ש: $B \in NPC$, $B \le_p A$, $A \in P$." "\n"
  "האם נובע מנתונים אלה ש-$NP=P$?",
  opts("כן", "לא", r"רק אם $NP \cap coNP \ne P$.", r"רק אם $B \notin coNP$"),
  "a",
  note="The key file (draft) shows Q19 fully rewritten via tracked changes; stem/options taken from the clean final copy, which the key fits."),
Q(20, "npc",
  "נגדיר את השפה $MCLIQUE$:\n"
  r"$$MCLIQUE = \{\langle G\rangle \mid (*)\}$$"
  r"(*): $G$ גרף לא מכוון, $V(G)$ = מספר הקודקודים ב-$G$, $\langle G, (V(G)-1)\rangle \in CLIQUE$" "\n"
  r"איזו מהטענות הבאות נכונה? (בהנחה ש-$P \ne NP$)",
  opts(("math", r"MCLIQUE \in NPC"),
       ("math", r"MCLIQUE \notin NP - NPC"),
       ("math", r"MQLIQUE \in P"),
       NONE),
  "c",
  note="Option ג is printed 'MQLIQUE ∈ P' in the clean copy ('QLIQUE ∈ PM' in the draft, a bidi artifact) — "
       "a typo for MCLIQUE ∈ P; kept as printed."),
]

# --- RESOLUTIONS (ASK_ADIR items resolved by independent math check; Adir authorized 2026-09-29) ---
def _resolve(num, **kw):
    q = next(q for q in questions if q["num"] == num)
    q.pop("hold", None)
    q.update(kw)
_resolve(13, correctId="b", answerSource="solved", official=False, confidence="high",
  explanation="\n".join([
    r"""**התשובה הנכונה: ב (לא)** (בטבלת התשובות הרשמית סומנה א). כש-$M_1, M_2$ מכריעות, $T_{M_1,M_2}$ מקבלת את $w$ בדיוק כשאחת מהן מקבלת והשנייה דוחה, כלומר $L(T_{M_1,M_2}) = L(M_1) \triangle L(M_2)$. לפי ההגדרה $\langle T\rangle \in CE_{TM}$ אם"ם $\overline{L(T)} = \emptyset$, כלומר $L(M_1) \triangle L(M_2) = \Sigma^*$, כלומר $L(M_2) = \overline{L(M_1)}$ – וזה לא שקול ל-$L(M_1) \ne L(M_2)$.""",
    r"""**דוגמה נגדית:** $L(M_1) = \{0\}$, $L(M_2) = \{1\}$. השפות שונות ולכן $\langle M_1,M_2\rangle \in NEQ_{TM}$, אבל $L(T) = \{0,1\} \ne \Sigma^*$ ולכן $f(\langle M_1,M_2\rangle) \notin CE_{TM}$.""",
    r"""**הערה:** אילו $CE_{TM}$ הייתה שפת המכונות ששפתן **לא ריקה**, התשובה הייתה א (כנראה כוונת הבוחנים); לפי ההגדרה המודפסת התשובה היא ב.""",
  ]),
  note=r"""Official letter table = א. Printed CE_TM = {<M> | complement(L(M)) = ∅} (verified at zoom on the clean copy p5); under it the equivalence fails -> ב.""")

exam = {
  "examCode": "22B-A",
  "examLabel": "2022 סמסטר ב מועד א",
  "year": 2022,
  "examDate": "22.6.2022",
  "sourceFile": "מבחנים/2022/סמסטר ב/סמסטר ב מועד א 22-6-22.pdf",
  "keyFile": "מבחנים/2022/סמסטר ב/2022-06-22-Exam-חישוביות-2022-moedA-גרסא-0 SOLUTION.pdf (red letter table on the cover)",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
assert [q["num"] for q in exam["questions"]] == list(range(1, 21))
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions")
