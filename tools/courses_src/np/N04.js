/* NP course - level 4: polynomial reductions, NP-hard and NP-complete */
CC_LEVEL("np", {
  id: "N04", order: 4, icon: "🪜", title: "רדוקציה פולינומית, NP-קשה ו-NP-שלמה",
  goal: "להגדיר A ≤p B, לדעת מה היא מעבירה בין P, NP ו-NP-קשה, ולהבדיל בין NP-קשה ל-NP-שלמה.",
  lesson: { html: `
<p>$A \le_p B$ היא רדוקציית מיפוי שבנוסף <b>רצה בזמן פולינומי</b>. בודקים שלושה דברים: (א) $f$ פולינומית (על מכונה דטרמיניסטית שעוצרת תוך $|x|^c$ צעדים); (ב) $x \in A \Rightarrow f(x) \in B$; (ג) $x \notin A \Rightarrow f(x) \notin B$.</p>
<table>
<thead><tr><th>אם $A \le_p B$ ו...</th><th>אז</th></tr></thead>
<tbody>
<tr><td>$B \in P$</td><td>$A \in P$</td></tr>
<tr><td>$B \in NP$</td><td>$A \in NP$</td></tr>
<tr><td>$A \notin P$</td><td>$B \notin P$</td></tr>
<tr><td>$A$ היא $NP$-קשה</td><td>$B$ היא $NP$-קשה</td></tr>
</tbody></table>
<p>כמו ברדוקציות מיפוי: קלות זורמת שמאלה וקושי ימינה. וגם $A \le_p B \iff \overline{A} \le_p \overline{B}$ באותה $f$ (25B-A-Q7), ו-$A \le_p B \Rightarrow A \le_m B$ אבל לא להפך.</p>
<h3>NP-קשה מול NP-שלמה</h3>
<ul>
<li><b>$NP$-קשה:</b> לכל $A \in NP$ מתקיים $A \le_p L$. השפה יכולה להיות בכל מקום, אפילו מחוץ ל-$R$.</li>
<li><b>$NP$-שלמה:</b> $NP$-קשה <b>וגם</b> $L \in NP$.</li>
</ul>
<div class="lesson-ex">$H_{TM}$ היא $NP$-קשה, כי כל שפה כריעה מתרדדת אליה (אפילו בזמן פולינומי: רק כותבים קוד, 23A-B-Q13). אבל היא לא $NP$-שלמה, כי היא לא כריעה ולכן לא ב-$NP$ (22A-C-Q10). זה נכון בלי קשר ל-$P = NP$.</div>
<div class="lesson-rule">🔑 <strong>איך מוכיחים $L \in NPC$:</strong> (1) $L \in NP$ (עד ומוודא); (2) רדוקציה פולינומית <b>מ</b>שפה $NP$-שלמה ידועה <b>אל</b> $L$.</div>
<div class="lesson-trap">⚠️ <strong>רדוקציה בחינם.</strong> אם $C \in NPC$ ו-$A \in NP$ אז $A \le_p C$ <b>תמיד</b> (זו ההגדרה). כך $5SAT \le_p 3SAT$ מתקיימת בהכרח. וגם: אם $A \in P$ ו-$B$ לא טריוויאלית אז $A \le_p B$, ולכן רדוקציה <b>מ</b>שפה ב-$P$ לא מלמדת כלום על $B$.</div>
` },
  questions: [
    { id: "N04-Q1", question: "מה צריך לבדוק כדי להראות ש-$f$ היא רדוקציה פולינומית $A \\le_p B$?",
      options: ["$f$ חשיבה בזמן פולינומי, $x \\in A \\Rightarrow f(x) \\in B$ וגם $x \\notin A \\Rightarrow f(x) \\notin B$", "רק ש-$f$ חשיבה בזמן פולינומי", "רק ש-$x \\in A \\Rightarrow f(x) \\in B$", "ש-$f$ פותרת את $A$ בזמן פולינומי ומחזירה קלט ל-$B$"], answer: 0,
      recap: "שלושה תנאים: פולינומית, כיוון חיובי, כיוון שלילי",
      explanation: "חסר אחד מהם והרדוקציה שבורה. אם $f$ פותרת את $A$ בעצמה (האפשרות שפותרת את $A$ בזמן פולינומי), היא לא צריכה להיות רדוקציה: מציאת קליקה כדי למחוק את צלעותיה דורשת זמן אקספוננציאלי, אלא אם $P = NP$." },
    { id: "N04-Q2", question: "נתון $A \\le_p B$. איזו טענה נכונה?",
      chk: { kind: "rules", opts: ["pr.NP_down", "pr.NP_up", "pr.hard_down", "pr.P_up"] },
      options: ["אם $B \\in NP$ אז $A \\in NP$", "אם $A \\in NP$ אז $B \\in NP$", "אם $B$ היא $NP$-קשה אז $A$ היא $NP$-קשה", "אם $A \\in P$ אז $B \\in P$"], answer: 0,
      recap: "קלות זורמת מ-B אל A; קושי מ-A אל B",
      explanation: "הפוך בכל השאר: אם $A$ קלה (למשל $A \\in P$) ו-$B$ קשה, מתקיימת $A \\le_p B$ בלי ש-$B$ ב-$NP$ או ב-$P$, ובלי ש-$A$ קשה." },
    { id: "N04-Q3", question: "מה נכון לגבי $H_{TM}$?",
      chk: { kind: "rules", opts: ["pr.HTM_hard_notC", "pr.HTM_C_if_PNP", "pr.HTM_C", "pr.HTM_not_hard"] },
      options: ["היא $NP$-קשה אבל לא $NP$-שלמה", "היא $NP$-שלמה אם $P = NP$", "היא $NP$-שלמה", "היא לא $NP$-קשה"], answer: 0,
      recap: "H_TM קשה (מכל שפה כריעה) אבל לא ב-NP",
      explanation: "כל שפה ב-$NP$ כריעה, ומשפה כריעה לא טריוויאלית יש רדוקציה (פולינומית, שרק כותבת קוד) אל $H_{TM}$. אבל $H_{TM} \\notin R$, ולכן $H_{TM} \\notin NP$ בכל מקרה, ולא תחת $P = NP$ ולא תחת $P \\ne NP$." },
    { id: "N04-Q4", question: "רוצים להוכיח ש-$L$ היא $NP$-קשה. איזו רדוקציה מספיקה?",
      chk: { kind: "rules", opts: ["pr.SAT_to_L", "pr.L_to_SAT", "pr.L_to_PATH", "pr.PATH_to_L"] },
      options: ["$SAT \\le_p L$", "$L \\le_p SAT$", "$L \\le_p PATH$", "$PATH \\le_p L$"], answer: 0,
      recap: "מרדדים משפה NP-קשה אל L",
      explanation: "הקושי זורם ימינה, ולכן מרדדים מ-$SAT$ אל $L$. $L \\le_p SAT$ מוכיחה רק ש-$L \\in NP$ (אל תחליפו כיוון). $PATH \\in P$ ולכן רדוקציה ממנה לא מלמדת על $L$, ו-$L \\le_p PATH$ נותנת $L \\in P$." },
    { id: "N04-Q5", question: "$A \\in NPC$ ו-$B$ היא $NP$-קשה. מה בהכרח נכון?",
      chk: { kind: "rules", opts: ["pr.NPC_to_hard", "pr.hard_to_NPC", "pr.NPC_to_NP", "pr.NPC_to_P"] },
      options: ["$A \\le_p B$", "$B \\le_p A$", "$A \\le_p B$ רק אם $B \\in NP$", "$A \\le_p B$ רק אם $B \\in P$"], answer: 0,
      recap: "A ∈ NP, ולכן A מתרדדת לכל שפה NP-קשה",
      explanation: "$B$ קשה, כלומר כל שפה ב-$NP$ מתרדדת אליה, ו-$A \\in NP$. לכן $A \\le_p B$. ההפך ($B \\le_p A$) לא בהכרח, אחרת $B$ הייתה כריעה. שתי האחרונות מוסיפות תנאים מיותרים." },
    { ref: "22A-C-Q15", recap: "SAT ≤p A ו-A ≤p B ⟹ B NP-קשה" },
  ],
});
