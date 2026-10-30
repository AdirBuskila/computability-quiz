# -*- coding: utf-8 -*-
"""N08 · מבחן גמר: P, NP ו-NP-שלמות — video script (build: tools/video/vid.py N08).

Boss level: a walkthrough of three exam questions that no guided quiz uses (vid.py refuses quiz ids):
  23A-A-Q17 (L NP-complete: what may its union with a regular language be?),
  22A-B-Q15 (MEDIUM-SIMPLE-CYCLE: the smallest class, assuming P != NP),
  23B-A-Q20 (VC <=p A and the complement of A <=p IS: what follows?).
Not used on purpose: the six boss-quiz questions (23A-A-Q21, 24A-A-Q8, 25B-A-Q8, 23S-A-Q6, 25B-B-Q9, 24A-A-Q14) and
their near twins (24A-B-Q14 / 23A-A-Q24 on A ∩ B, 26B-A-Q14 on mutual reductions, 24A-B-Q10 on 4SAT <=p L).
"""
import itertools
from vid import P, Scene, Video, show, hide, BANK
import stage as st
import w_np as g


# ---------------------------------------------------------------- facts (verified)
def has_cycle(V, E, L):
    """a simple cycle with exactly L >= 3 vertices"""
    if L < 3:
        return False
    for S in itertools.permutations(V, L):
        if S[0] != min(S) or S[1] > S[-1]:
            continue
        if all(frozenset((S[i], S[(i + 1) % L])) in E for i in range(L)):
            return True
    return False


def two_copies(V, E):
    V2 = [v + "a" for v in V] + [v + "b" for v in V]
    E2 = frozenset(frozenset(x + s for x in e) for e in E for s in "ab")
    return V2, E2


for n in range(1, 6):                              # HAM-CYCLE <=p MEDIUM-SIMPLE-CYCLE by two copies of G
    Vn = [str(i) for i in range(n)]
    pairs = list(itertools.combinations(Vn, 2))
    for bits in range(1 << len(pairs)):
        En = frozenset(frozenset(p) for i, p in enumerate(pairs) if bits >> i & 1)
        V2, E2 = two_copies(Vn, En)
        assert has_cycle(Vn, En, n) == has_cycle(V2, E2, len(V2) // 2)

V = ["1", "2", "3", "4"]
E = g.E_(("1", "2"), ("2", "3"), ("3", "4"), ("4", "1"), ("1", "3"))
V2, E2 = two_copies(V, E)
HAM = ["1a", "2a", "3a", "4a"]
assert has_cycle(V, E, 4) and len(V2) // 2 == 4 and all(frozenset((HAM[i], HAM[(i + 1) % 4])) in E2 for i in range(4))

Q1, Q2, Q3 = BANK["23A-A-Q17"], BANK["22A-B-Q15"], BANK["23B-A-Q20"]
assert (Q1["correctId"], Q2["correctId"], Q3["correctId"]) == ("b", "b", "a")


def opts(Q):
    return [(o["id"], f'${o["value"]}$' if o["type"] == "math" else o["value"]) for o in Q["options"]]


POS = {}
for s, dx in (("a", 0), ("b", 470)):
    for v, (x, y) in {"1": (90, 100), "2": (330, 100), "3": (330, 340), "4": (90, 340)}.items():
        POS[v + s] = (x + dx, y)
NAMES = {v: v[0] for v in V2}
G2 = g.graph_svg("g2", V2, E2, POS, names=NAMES, w=900, h=440, scale=0.72)

# ---------------------------------------------------------------- scenes
title = Scene("title", "", [
    P("מבחן גמר על $P$, $NP$ ו-$NP$-שלמות: שלוש שאלות אמת ממבחנים, צעד אחר צעד.",
      say="מבחן גמר על פִּי, אֶן פִּי ואֶן פִּי שלמות: שלוש שאלות אמת ממבחנים, צעד אחר צעד."),
    P("בכל שאלה נשאל: מה הוכח, מה נובע מההנחה, ומה עדיין פתוח.", hold=0.4),
], stage='<div class="kicker">N08 · P, NP ו-NP-שלמות</div><h1>מבחן גמר: P, NP ו-NP-שלמות</h1>'
         '<p>שלוש שאלות ממבחנים: שפה $NP$-שלמה ושפה רגולרית, מעגל באורך חצי, ושרשרת רדוקציות שמזיזה את $coNP$.</p>',
   layout="title")

q1 = Scene("q1", "שאלה 1", [
    P("שאלה ראשונה: $L$ היא $NP$-שלמה. איזו טענה נכונה?", say="שאלה ראשונה: אֵל היא אֶן פִּי שלמה. איזו טענה נכונה?"),
    P("האם ייתכן שהמשלים של $L$ אינו ניתן לקבלה? לא. $L$ ב-$NP$, ולכן כריעה, וגם המשלים שלה כריע.",
      do=show("a-x-a", "a-n-a", "a1"),
      say="האם ייתכן שהמשלים של אֵל אינו ניתן לקבלה? לא. אֵל באֶן פִּי, ולכן כריעה, וגם המשלים שלה כריע."),
    P("עכשיו איחוד עם שפה רגולרית. הטריק: לבחור את השפה הרגולרית בחוכמה.", do=show("a2")),
    P("איחוד עם הקבוצה הריקה, שהיא רגולרית, משאיר את $L$ כמו שהיא. אז האיחוד $NP$-שלם. ייתכן.",
      do=show("a-ok-b", "a3"),
      say="איחוד עם הקבוצה הריקה, שהיא רגולרית, משאיר את אֵל כמו שהיא. אז האיחוד אֶן פִּי שלם. ייתכן."),
    P("ואיחוד עם סיגמא כוכבית, גם היא רגולרית, נותן סיגמא כוכבית, שהיא ב-$P$.", do=show("a4"),
      say="ואיחוד עם סיגמא כוכבית, גם היא רגולרית, נותן סיגמא כוכבית, שהיא בפִּי."),
    P("אז הטענה ״לא ייתכן שהאיחוד ב-$P$״ שגויה, והתשובה היא שהאיחוד יכול להיות $NP$-שלם.", do=show("a-x-c", "a-x-d"), hold=0.5,
      say="אז הטענה לא ייתכן שהאיחוד בפִּי שגויה, והתשובה היא שהאיחוד יכול להיות אֶן פִּי שלם."),
], stage='<div class="stack" style="gap:26px">'
         '<div id="a1" class="card plain h" style="font-size:34px">$NPC \\subseteq NP \\subseteq R$ ← $\\overline{L} \\in R$</div>'
         '<div id="a2" class="card ex h" style="font-size:34px">״ייתכן״ ← מספיקה דוגמה אחת</div>'
         '<div id="a3" class="bigmath h" style="font-size:42px">$L \\cup \\emptyset = L \\in NPC$</div>'
         '<div id="a4" class="bigmath h" style="font-size:42px">$L \\cup \\Sigma^* = \\Sigma^* \\in P$</div></div>',
   panel=f'<div class="qstem"><span class="qid">{Q1["id"]}</span>$L$ היא $NP$-שלמה. איזו טענה נכונה?</div>'
         + '<div class="optsm">' + st.options("a", opts(Q1), notes={"a": "L כריעה"}) + '</div>')

q2 = Scene("q2", "שאלה 2", [
    P("שאלה שנייה: גרפים שיש בהם מעגל פשוט באורך **בדיוק** חצי ממספר הקודקודים. בהנחה ש-$P \\ne NP$, מהי המחלקה הקטנה ביותר?",
      say="שאלה שנייה: גרפים שיש בהם מעגל פשוט באורך בדיוק חצי ממספר הקודקודים. בהנחה שפִּי שונה מאֶן פִּי, מהי המחלקה הקטנה ביותר?"),
    P("קודם, השפה ב-$NP$: העד הוא המעגל עצמו, ובודקים אותו מהר.", do=show("m-1"),
      say="קודם, השפה באֶן פִּי: העד הוא המעגל עצמו, ובודקים אותו מהר."),
    P("האורך כאן **גדל** עם הקלט, אז אין חיפוש ממצה קצר. נחשוד שהיא שלמה, ונבנה רדוקציה ממעגל המילטון.", do=show("m-2")),
    P("הגאדג'ט: שני עותקים של הגרף, בלי חיבורים ביניהם. מספר הקודקודים מוכפל, אז חצי ממנו הוא בדיוק $n$.",
      do=show("m-g", "m-3"),
      say="הגאדג'ט: שני עותקים של הגרף, בלי חיבורים ביניהם. מספר הקודקודים מוכפל, אז חצי ממנו הוא בדיוק אֶן."),
    P("מעגל המילטון בגרף המקורי הוא מעגל באורך $n$ בעותק אחד.", do=show(*g.hv("g2", *HAM)) + show(*[g.heid("g2", HAM[i], HAM[(i + 1) % 4], V2) for i in range(4)]),
      say="מעגל המילטון בגרף המקורי הוא מעגל באורך אֶן בעותק אחד."),
    P("ולהפך: מעגל באורך $n$ חייב להיות בתוך עותק אחד, ושם הוא עובר בכל הקודקודים. כלומר מעגל המילטון.", do=show("m-4"),
      say="ולהפך: מעגל באורך אֶן חייב להיות בתוך עותק אחד, ושם הוא עובר בכל הקודקודים. כלומר מעגל המילטון."),
    P("אז השפה $NP$-שלמה. וכש-$P \\ne NP$, היא לא ב-$P$. המחלקה הקטנה ביותר: $NP$.", do=show("b-ok-b", "b-x-a"), hold=0.5,
      say="אז השפה אֶן פִּי שלמה. וכשפִּי שונה מאֶן פִּי, היא לא בפִּי. המחלקה הקטנה ביותר: אֶן פִּי."),
    P("ו-$R$ ו-$RE$? גם הן מכילות את השפה, אבל הן גדולות יותר. השאלה מבקשת את הקטנה ביותר.", do=show("b-x-c", "b-x-d"), hold=0.5,
      say="ואָר ואָר אִי? גם הן מכילות את השפה, אבל הן גדולות יותר. השאלה מבקשת את הקטנה ביותר."),
], stage=f'<div class="stack" style="gap:14px"><div id="m-g" class="h">{G2}</div>'
         + st.card("m-1", "plain", "ב-$NP$: העד הוא המעגל")
         + st.card("m-2", "trap", "⚠️ האורך גדל עם הקלט, לא קבוע")
         + '<div id="m-3" class="card ex h">$|V\'| = 2n$ ← מעגל באורך $n$</div>'
         + st.card("m-4", "rule", "🔑 $HAMCYCLE \\le_p$ השפה") + '</div>',
   panel=f'<div class="qstem" style="font-size:30px"><span class="qid">{Q2["id"]}</span>מעגל פשוט באורך '
         '$\\lfloor |V|/2 \\rfloor$ בדיוק. בהנחה ש-$P \\ne NP$, המחלקה הקטנה ביותר?</div>'
         + '<div class="optsm">' + st.options("b", opts(Q2)) + '</div>')

q3 = Scene("q3", "שאלה 3", [
    P("שאלה שלישית: $VC$ מתרדדת ל-$A$, והמשלים של $A$ מתרדד ל-$IS$. מה נובע?",
      say="שאלה שלישית: וִי סִי מתרדדת לאֵיי, והמשלים של אֵיי מתרדד לאַיי אֶס. מה נובע?"),
    P("צעד ראשון: רדוקציה מהמשלים של $A$ ל-$IS$ היא, באותה פונקציה, רדוקציה מ-$A$ למשלים של $IS$.", do=show("c-1"),
      say="צעד ראשון: רדוקציה מהמשלים של אֵיי לאַיי אֶס היא, באותה פונקציה, רדוקציה מאֵיי למשלים של אַיי אֶס."),
    P("צעד שני: משרשרים. $VC$ מתרדדת ל-$A$, ו-$A$ למשלים של $IS$.", do=show("c-2"),
      say="צעד שני: משרשרים. וִי סִי מתרדדת לאֵיי, ואֵיי למשלים של אַיי אֶס."),
    P("המשלים של $IS$ ב-$coNP$. ושפה שניתנת לרדוקציה פולינומית לשפה ב-$coNP$ היא גם ב-$coNP$.", do=show("c-3"),
      say="המשלים של אַיי אֶס בקוֹ-אֶן-פִּי. ושפה שניתנת לרדוקציה פולינומית לשפה בקוֹ-אֶן-פִּי היא גם בקוֹ-אֶן-פִּי."),
    P("אז $VC$ ב-$coNP$.", say="אז וִי סִי בקוֹ-אֶן-פִּי."),
    P("אבל $VC$ שלמה. שפה שלמה ב-$coNP$ גוררת ש-$NP$ שווה ל-$coNP$, כלומר $NP$ סגורה למשלים.", do=show("c-4", "c-ok-a", "c-x-c"),
      say="אבל וִי סִי שלמה. שפה שלמה בקוֹ-אֶן-פִּי גוררת שאֶן פִּי שווה לקוֹ-אֶן-פִּי, כלומר אֶן פִּי סגורה למשלים."),
    P("המלכודת: $P = NP$ לא נובע. ראינו ש-$P = NP$ גורר $NP = coNP$, אבל לא להפך.", do=show("c-x-d", "c-n-d"),
      say="המלכודת: פִּי שווה אֶן פִּי לא נובע. ראינו שפִּי שווה אֶן פִּי גורר אֶן פִּי שווה קוֹ-אֶן-פִּי, אבל לא להפך."),
    P("ו-$A$ לא יכולה להיות לא כריעה: היא מתרדדת לשפה כריעה.", do=show("c-x-b"), hold=0.5,
      say="ואֵיי לא יכולה להיות לא כריעה: היא מתרדדת לשפה כריעה."),
], stage='<div class="stack" style="gap:24px">'
         '<div id="c-1" class="bigmath h" style="font-size:40px">$\\overline{A} \\le_p IS \\Rightarrow A \\le_p \\overline{IS}$</div>'
         '<div id="c-2" class="bigmath h" style="font-size:40px">$VC \\le_p A \\le_p \\overline{IS}$</div>'
         '<div id="c-3" class="bigmath h" style="font-size:40px">$\\overline{IS} \\in coNP \\Rightarrow VC \\in coNP$</div>'
         '<div id="c-4" class="bigmath h" style="font-size:40px">$VC \\in NPC \\cap coNP \\Rightarrow NP = coNP$</div></div>',
   panel=f'<div class="qstem"><span class="qid">{Q3["id"]}</span>$VC \\le_p A$ וגם $\\overline{{A}} \\le_p IS$. '
         'איזו טענה נכונה?</div>' + st.options("c", opts(Q3), notes={"d": "לא נובע"}))

recap = Scene("recap", "סיכום", [
    P("מה לקחנו: ״ייתכן״ דורש דוגמה אחת, ושפות טריוויאליות הן דוגמאות טובות.", do=show("r-1")),
    P("פרמטר שגדל עם הקלט, ושני עותקים של גרף, נותנים רדוקציה ממעגל המילטון.", do=show("r-2")),
    P("ורדוקציה אל משלים מעבירה שפה שלמה ל-$coNP$, ואז $NP = coNP$. בהצלחה במבחן!", do=show("r-3"), hold=0.8,
      say="ורדוקציה אל משלים מעבירה שפה שלמה לקוֹ-אֶן-פִּי, ואז אֶן פִּי שווה קוֹ-אֶן-פִּי. בהצלחה במבחן!"),
], stage='<div class="stack"><div class="bigmath">$P \\subseteq NP \\subseteq R$</div>'
         '<div class="bigmath" style="font-size:40px">$NPC \\cap coNP \\ne \\emptyset \\iff NP = coNP$</div></div>',
   panel=st.card("r-1", "rule", "🔑 ״ייתכן״ ← דוגמה: $\\emptyset$, $\\Sigma^*$")
         + st.card("r-2", "rule", "🔑 שני עותקים: $|V'| = 2n$")
         + st.card("r-3", "rule", "🔑 שלמה ב-$coNP$ ← $NP = coNP$"))

VIDEO = Video("N08", "np", "מבחן גמר: P, NP ו-NP-שלמות", [title, q1, q2, q3, recap],
              bank={"23A-A-Q17": "b", "22A-B-Q15": "b", "23B-A-Q20": "a"})
