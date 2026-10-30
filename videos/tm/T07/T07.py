# -*- coding: utf-8 -*-
"""T07 · מבחן גמר: מכונות טיורינג — video script (build: tools/video/vid.py T07). Boss level: exam walkthroughs.

Source: tools/courses_src/tm/T07.js (boss; its quiz is 24B-B-Q4, 24B-A-Q3, 22A-B-Q11, 24A-B-Q4, 25B-B-Q14, 24A-C-Q14,
none of them solved here). Exam anchors, all tm-topic questions no guided quiz uses:
  22A-A-Q7   two non-deterministic machines for A and its complement both accept w: impossible
  26B-A-Q23  "sympathetic" 3-tape machine (heads move together): the class it decides is exactly R
  24S-A-Q13  K_{M,w}(x) = {run M on w; accept}: K deciding does not make M deciding, the converse holds
  25B-C-Q4   two non-deterministic machines with the same language: both claims about their paths are false
Checked below: the complement argument on a sample language; a sympathetic machine and its one-tape encoding
(tape alphabet Γ³) give the same result and the same number of steps; a basic machine runs unchanged on tape 1 of a
sympathetic one; the K counterexample uses a machine that halts on w and loops on another word (run_tm); the two
counterexample pairs of 25B-C-Q4 have the same verdict on w (w_tm.ntm_verdict) and break the claims.
"""
from vid import P, Scene, Video, show, hide, BANK
from common import ACC, REJ, BLANK, run_tm, words
import stage as st
import w_tm

# ---------------------------------------------------------------- 22A-A-Q7
A = {w for w in words(6) if w.count("1") % 2 == 0}
assert all(not (w in A and w not in A) for w in words(6))         # w ∈ L(M_A) = A and w ∈ L(N_A) = Ā: never both


# ---------------------------------------------------------------- 26B-A-Q23
def run_sym(delta, start, word, cap=500):
    """three tapes, one head position shared by all three (heads move together); -> (result, steps)"""
    tapes = [list(word) or [BLANK], [BLANK], [BLANK]]
    pos, q, steps = 0, start, 0
    while steps < cap:
        if q in (ACC, REJ):
            return ("accept" if q == ACC else "reject"), steps
        for t in tapes:
            while len(t) <= pos:
                t.append(BLANK)
        nxt = delta.get((q, tuple(t[pos] for t in tapes)))
        if nxt is None:
            return "reject", steps
        q, out, d = nxt
        for t, c in zip(tapes, out):
            t[pos] = c
        pos = max(0, pos - 1) if d == "L" else pos + 1
        steps += 1
    return "loop", steps


B3 = (BLANK, BLANK, BLANK)
# S copies tape 1 onto tape 2 and accepts if the input has an even number of 1s (the parity is in the state);
# E is the basic machine whose tape symbols are the triples of S (the all-blank triple is its blank)
S = {}
for par in ("q_0", "q_1"):
    for c in "01":
        nxt = par if c == "0" else ("q_1" if par == "q_0" else "q_0")
        S[(par, (c, BLANK, BLANK))] = (nxt, (c, c, BLANK), "R")
S[("q_0", B3)] = (ACC, B3, "R")
TRIPLES = sorted({a for _, a in S} | {b for _, b, _ in S.values()})
enc = {t: (BLANK if t == B3 else chr(0x2460 + i)) for i, t in enumerate(TRIPLES)}   # one tape symbol per triple
E = {(q, enc[a]): (p, enc[b], d) for (q, a), (p, b, d) in S.items()}
for w in words(6):
    one = run_tm(E, "q_0", "".join(enc[(c, BLANK, BLANK)] for c in w))
    sym = run_sym(S, "q_0", w)
    assert (one[0], one[1]) == sym and sym[0] == ("accept" if w.count("1") % 2 == 0 else "reject"), (w, one, sym)
# R ⊆ C: a basic machine runs on tape 1 and ignores the others
DB = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): (REJ, BLANK, "R")}
SB = {(q, (a, x, y)): (p, (b, x, y), d) for (q, a), (p, b, d) in DB.items() for x in (BLANK,) for y in (BLANK,)}
for w in words(6):
    assert run_sym(SB, "q_0", w) == run_tm(DB, "q_0", w)[:2], w

# ---------------------------------------------------------------- 24S-A-Q13
DM = {("q_0", "0"): ("q_0", "0", "R"), ("q_0", "1"): (ACC, "1", "R"), ("q_0", BLANK): ("q_1", BLANK, "L"),
      ("q_1", "0"): ("q_1", "0", "L")}                               # T02's machine: halts on 01, loops on 00
assert run_tm(DM, "q_0", "01")[0] == "accept" and run_tm(DM, "q_0", "00")[0] == "loop"

# ---------------------------------------------------------------- 25B-C-Q4
V = w_tm.ntm_verdict
I1, I2 = [("rej", 2)], [("loop", 1)]                      # M_1 rejects at once, M_2 never halts: both L = ∅
II1, II2 = [("acc", 2), ("acc", 2)], [("acc", 2), ("loop", 1)]   # every path of M_1 accepts; M_2 also has an infinite one
assert V([k for k, _ in I1]) == "reject" and V([k for k, _ in I2]) == "none"         # w ∉ both languages
assert not any(k in ("acc", "rej") for k, _ in I2)                                  # claim I broken
assert V([k for k, _ in II1]) == V([k for k, _ in II2]) == "accept"                 # w ∈ both languages
assert all(k == "acc" for k, _ in II1) and any(k == "loop" for k, _ in II2)        # claim II broken

Q1, Q2, Q3, Q4 = BANK["22A-A-Q7"], BANK["26B-A-Q23"], BANK["24S-A-Q13"], BANK["25B-C-Q4"]
assert (Q1["correctId"], Q2["correctId"], Q3["correctId"], Q4["correctId"]) == ("d", "c", "a", "b")


def opts(Q):
    return [(o["id"], f'${o["value"]}$' if o["type"] == "math" else o["value"]) for o in Q["options"]]


# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("זה מבחן הגמר של הפרק על מכונות טיורינג."),
    P("נפתור יחד ארבע שאלות ממבחנים אמיתיים, ובכל אחת נחפש את המלכודת.", hold=0.4),
], stage='<div class="kicker">T07 · מכונות טיורינג</div><h1>מבחן גמר: מכונות טיורינג</h1>'
         '<p>ארבע שאלות ממבחנים: מכונות אי-דטרמיניסטיות, וריאנט חדש, ומכונה שמריצה מכונה.</p>', layout="title")

s1 = Scene("q1", "שאלה 1", [
    P("שאלה ראשונה. $M_A$ ו-$N_A$ הן מכונות אי-דטרמיניסטיות. הראשונה מקבלת את $A$, והשנייה את המשלים שלה."),
    P("והשאלה: האם ייתכן שבשני עצי החישוב, על אותה מילה $w$, יש קונפיגורציה מקבלת?"),
    P("נתרגם את זה לשפות. אם בעץ של $M_A$ יש קונפיגורציה מקבלת, אז $w$ שייכת ל-$A$.", do=show("a-1")),
    P("ואם גם בעץ של $N_A$ יש כזו, אז $w$ שייכת גם למשלים של $A$.", do=show("a-2")),
    P("אבל מילה לא יכולה להיות גם ב-$A$ וגם במשלים שלה. החיתוך שלהן ריק.", do=show("a-3")),
    P("המלכודת: לחשוב שבמכונה אי-דטרמיניסטית ״הכול אפשרי״, כי יש מסלולים רבים.", do=show("a-t")),
    P("אבל מסלול מקבל אחד כבר אומר שהמילה בשפה. לכן השילוב **אינו אפשרי**.",
      do=show("q1-ok-d", "q1-x-a", "q1-x-b", "q1-x-c"), hold=0.6),
], stage='<div class="stack">'
         + st.card("a-1", "ex", "מסלול מקבל של $M_A$ ⇐ $w \\in A$")
         + st.card("a-2", "ex", "מסלול מקבל של $N_A$ ⇐ $w \\in \\overline{A}$")
         + st.card("a-3", "rule", "🔑 $A \\cap \\overline{A} = \\emptyset$")
         + st.card("a-t", "trap", "⚠️ מסלול מקבל אחד מספיק: המילה בשפה")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q1["id"]}</span>בשני עצי החישוב, של $M_A$ ושל $N_A$ על $w$, '
         'יש קונפיגורציה מקבלת. מה נכון?</div>' + st.options("q1", opts(Q1)))

s2 = Scene("q2", "שאלה 2", [
    P("שאלה שנייה: מכונה **סימפטית** היא מכונה עם שלושה סרטים, ששלושת הראשים שלה זזים תמיד יחד."),
    P("$C$ היא מחלקת השפות שמכונה סימפטית מכריעה. מה היחס בין $C$ לבין $R$?",
      say="סִי היא מחלקת השפות שמכונה סימפטית מכריעה. מה היחס בין סִי לבין אָר?"),
    P("כיוון ראשון: כל שפה ב-$R$ נמצאת ב-$C$. מכונה סימפטית יכולה פשוט להתעלם משני הסרטים האחרים.",
      do=show("b-1")),
    P("כיוון שני: מכונה בסיסית מסמלצת מכונה סימפטית. הראשים תמיד באותו מקום, אז כל תא מחזיק שלישייה.",
      do=show("b-2")),
    P("א״ב הסרט הוא שלישיות של תווים, וזה עדיין א״ב סופי. כל צעד סימפטי הוא צעד אחד של המכונה הבסיסית.",
      do=show("b-3")),
    P("המלכודת: לחשוב ששלושה סרטים מוסיפים כוח. וריאנטים משנים זמן, לא את מה שאפשר להכריע.", do=show("b-t")),
    P("לכן $R$ שווה ל-$C$. שתי האפשרויות של הכלה ממש נופלות.",
      do=show("q2-ok-c", "q2-x-a", "q2-x-b", "q2-x-d"), hold=0.6, say="לכן אָר שווה לסִי. שתי האפשרויות של הכלה ממש נופלות."),
], stage='<div class="stack">'
         + st.card("b-1", "ex", "$R \\subseteq C$: מתעלמים מסרטים 2 ו-3")
         + st.card("b-2", "ex", "$C \\subseteq R$: תא אחד מחזיק שלישייה")
         + st.card("b-3", "rule", "🔑 $\\Gamma' = \\Gamma^3$: עדיין סופי, צעד מול צעד")
         + st.card("b-t", "trap", "⚠️ וריאנט משנה זמן, לא כוח")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q2["id"]}</span>3 סרטים, הראשים זזים יחד. '
         '$C$ = השפות שמכונה סימפטית מכריעה. מה נכון?</div>' + st.options("q2", opts(Q2)))

s3 = Scene("q3", "שאלה 3", [
    P("שאלה שלישית: המכונה $K_{M,w}$ מתעלמת מהקלט שלה. היא מריצה את $M$ על $w$, ואם הריצה נגמרה, מקבלת.",
      say="שאלה שלישית: המכונה קֵיי אֵם דַּאבְּלְיוּ מתעלמת מהקלט שלה. היא מריצה את אֵם על דַּאבְּלְיוּ, ואם הריצה נגמרה, מקבלת."),
    P("טענה ראשונה: אם $K$ מכריעה, אז גם $M$ מכריעה.", do=show("c-1"),
      say="טענה ראשונה: אם המכונה קֵיי מכריעה, אז גם המכונה אֵם מכריעה."),
    P("$K$ עוצרת על כל קלט בדיוק כש-$M$ עוצרת על $w$. על **מילה אחת** בלבד.", do=show("c-2"),
      say="המכונה קֵיי עוצרת על כל קלט בדיוק כשהמכונה אֵם עוצרת על דַּאבְּלְיוּ. על מילה אחת בלבד."),
    P("למשל המכונה מהרמה השנייה: על $01$ היא מקבלת, ועל $00$ היא בלולאה.", do=show("c-3")),
    P("עם $w$ שהיא $01$, $K$ מכריעה, אבל $M$ לא מכריעה. הטענה הראשונה לא נכונה.", do=show("c-4"),
      say="עם דַּאבְּלְיוּ שהיא אפס אחת, המכונה קֵיי מכריעה, אבל המכונה אֵם לא מכריעה. הטענה הראשונה לא נכונה."),
    P("טענה שנייה: אם $M$ מכריעה, היא עוצרת על כל מילה, ובפרט על $w$. אז $K$ עוצרת תמיד, ומכריעה.",
      do=show("c-5"), say="טענה שנייה: אם המכונה אֵם מכריעה, היא עוצרת על כל מילה, ובפרט על דַּאבְּלְיוּ. "
      "אז המכונה קֵיי עוצרת תמיד, ומכריעה."),
    P("המלכודת: לבלבל בין ״עוצרת על $w$״ לבין ״עוצרת על הכול״. התשובה: הראשונה לא נכונה, והשנייה נכונה.",
      do=show("q3-ok-a", "q3-x-b", "q3-x-c", "q3-x-d"), hold=0.6),
], stage='<div class="stack"><div class="bigmath" style="font-size:42px">$K_{M,w}(x) : \\{ M(w) ; \\ \\text{accept} \\}$</div>'
         + st.card("c-1", "plain", "I: $K$ מכריעה ⇐ $M$ מכריעה?")
         + st.card("c-2", "ex", "$K$ עוצרת תמיד ⟺ $M$ עוצרת על $w$")
         + st.card("c-3", "ex", "$M$: על $01$ מקבלת, על $00$ לולאה")
         + st.card("c-4", "trap", "⚠️ I לא נכונה: עוצרת על $w$ ≠ עוצרת על הכול")
         + st.card("c-5", "rule", "🔑 II נכונה: $M$ מכריעה ⇐ עוצרת על $w$")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q3["id"]}</span>I: $K_{{M,w}}$ מכריעה ⇐ $M$ מכריעה. '
         'II: $M$ מכריעה ⇐ $K_{{M,w}}$ מכריעה. מה נכון?</div>' + st.options("q3", opts(Q3)))



def tree(pfx, t, cap):
    return (f'<div class="stack" style="gap:4px;width:auto">{w_tm.ntm_tree(pfx, t, 220, 250)}'
            f'<div class="hint">{cap}</div></div>')


def show_tree(pfx, t):
    return show(*[f"{pfx}-b{i}" for i in range(len(t))], *[f"{pfx}-l{i}-{k}" for i, (k, _) in enumerate(t)])


s4 = Scene("q4", "שאלה 4", [
    P("שאלה רביעית: $M_1$ ו-$M_2$ אי-דטרמיניסטיות, עם אותה שפה. שתי טענות על מסלולי החישוב שלהן."),
    P("טענה ראשונה: אם ל-$M_1$ יש מסלול שנגמר בדחייה, אז ל-$M_2$ יש מסלול שעוצר.", do=show("d-1")),
    P("דוגמה נגדית: $M_1$ דוחה מיד כל קלט, ו-$M_2$ לא עוצרת על אף קלט.", do=show_tree("i1", I1) + show_tree("i2", I2)),
    P("לשתיהן השפה הריקה. אבל ל-$M_2$ אין אף מסלול שעוצר. הטענה הראשונה לא נכונה.", do=show("d-2")),
    P("טענה שנייה: אם **כל** המסלולים של $M_1$ מקבלים, אז כל המסלולים של $M_2$ עוצרים.", do=show("d-3")),
    P("דוגמה נגדית: $M_1$ מקבלת מיד. $M_2$ מנחשת: בענף אחד מקבלת, ובענף אחר נכנסת ללולאה.",
      do=show_tree("j1", II1) + show_tree("j2", II2)),
    P("שתיהן מקבלות כל מילה, אבל ל-$M_2$ יש מסלול אינסופי. גם הטענה השנייה לא נכונה.", do=show("d-4")),
    P("המלכודת: אותה שפה אומרת רק **מי מתקבל**. היא לא אומרת כלום על הדחיות ועל העצירה. שתי הטענות לא נכונות.",
      do=show("q4-ok-b", "q4-x-a", "q4-x-c", "q4-x-d"), hold=0.6),
], stage='<div class="stack" style="gap:10px">'
         '<div style="display:flex;gap:30px;direction:ltr;justify-content:center">'
         + tree("i1", I1, "I: $M_1$") + tree("i2", I2, "I: $M_2$")
         + tree("j1", II1, "II: $M_1$") + tree("j2", II2, "II: $M_2$") + "</div>"
         + st.card("d-1", "plain", "I: מסלול דוחה ב-$M_1$ ⇐ מסלול עוצר ב-$M_2$?")
         + st.card("d-2", "trap", "⚠️ I לא נכונה: $\\emptyset$ עם דחייה, $\\emptyset$ עם לולאה")
         + st.card("d-3", "plain", "II: כל מסלולי $M_1$ מקבלים ⇐ כל מסלולי $M_2$ עוצרים?")
         + st.card("d-4", "trap", "⚠️ II לא נכונה: מסלול אינסופי לא מונע קבלה")
         + "</div>",
   panel=f'<div class="qstem"><span class="qid">{Q4["id"]}</span>$L(M_1) = L(M_2)$, שתיהן אי-דטרמיניסטיות. '
         'מה נכון על טענות I ו-II?</div>' + st.options("q4", opts(Q4)))

recap = Scene("recap", "סיכום", [
    P("ארבע מלכודות לזכור.", do=show("r-0")),
    P("מסלול מקבל אחד במכונה אי-דטרמיניסטית אומר שהמילה בשפה, ולכן אין מילה ששתי המכונות מקבלות.",
      do=show("r-1")),
    P("וריאנטים של מכונת טיורינג משנים את הזמן, לא את מה שאפשר להכריע.", do=show("r-2")),
    P("עצירה על מילה אחת אינה עצירה על כל הקלטים.", do=show("r-3")),
    P("ושתי מכונות עם אותה שפה יכולות להתנהג אחרת גם על מילים שבשפה, עם ענף אינסופי, וגם על מילים שלא בשפה. בהצלחה במבחן!", do=show("r-4"), hold=0.8),
], stage='<div class="stack"><div id="r-0" class="bigmath h">🏆</div></div>',
   panel=st.card("r-1", "rule", "🔑 $w \\in L(M_A) \\cap L(N_A)$: בלתי אפשרי")
         + st.card("r-2", "rule", "🔑 וריאנט: זמן אחר, אותו כוח")
         + st.card("r-3", "trap", "⚠️ עוצרת על $w$ ≠ מכריעה")
         + st.card("r-4", "trap", "⚠️ אותה שפה ≠ אותה התנהגות"))

VIDEO = Video("T07", "tm", "מבחן גמר: מכונות טיורינג", [title, s1, s2, s3, s4, recap],
              bank={"22A-A-Q7": "d", "26B-A-Q23": "c", "24S-A-Q13": "a", "25B-C-Q4": "b"})
