/* Decidability course - level 5: mixed difference and the substitution trick */
CC_LEVEL("dec", {
  id: "D05", order: 5, icon: "🧪", title: "הפרש מעורב והצבת ∅ ו-Σ*",
  goal: "לפתור שאלת \"מה בהכרח נכון על A∖B\" בשני כלים: המרת הפרש לחיתוך עם משלים, והצבת שפות פשוטות כדי להפריך.",
  lesson: { html: `
<p>רוב שאלות הסגירות במבחן הן על שפות ממחלקות <b>שונות</b>. הכלי הראשון: <b>הפרש הוא חיתוך עם משלים</b>.</p>
<div class="lesson-formula">$A \setminus B = A \cap \overline{B}$</div>
<p>המשלים הופך כיוון ($RE \leftrightarrow coRE$, ו-$R$ נשאר $R$), ואז בודקים סגירות של חיתוך.</p>
<table>
<thead><tr><th>$A$</th><th>$B$</th><th>$A \setminus B$ בהכרח ב-</th></tr></thead>
<tbody>
<tr><td>$RE$</td><td>$R$</td><td>$RE$ ($\overline{B} \in R \subseteq RE$)</td></tr>
<tr><td>$RE$</td><td>$coRE$</td><td>$RE$ ($\overline{B} \in RE$)</td></tr>
<tr><td>$R$</td><td>$RE$</td><td>$coRE$ ($\overline{B} \in coRE$, וגם $A \in coRE$)</td></tr>
<tr><td>$RE$</td><td>$RE$</td><td>אין הבטחה כלל</td></tr>
</tbody></table>
<h3>הכלי השני: הצבה</h3>
<p>שתי השפות $\emptyset$ ו-$\Sigma^*$ כריעות, ולכן מותר להציב אותן בכל מקום, וגם את $A_{TM}$ ואת $\overline{A_{TM}}$ כשצריך שפה לא כריעה.</p>
<ul>
<li>להפריך "<b>בהכרח</b> לא כריעה" או "בהכרח $RE \setminus R$": מציבים כך שהתוצאה מתרוקנת, $\emptyset$ או $\Sigma^*$.</li>
<li>להפריך "בהכרח כריעה": מציבים $A = A_{TM}$ ו-$B = \emptyset$, כך שהתוצאה היא $A_{TM}$ עצמה.</li>
</ul>
<div class="lesson-trap">⚠️ "<b>בהכרח</b> ב-$RE \setminus R$" כמעט תמיד שגוי: מספיק $B = \Sigma^*$ כדי לקבל $A \setminus B = \emptyset \in R$ (23B-A-Q3, 20A-B-Q3). וקריאה חד-צדדית: "יתכן" פירושו שקיימת דוגמה אחת, "בהכרח" פירושו שכל דוגמה עובדת.</div>
<div class="lesson-rule">🔑 22A-C-Q3: אם $A \in R$ ו-$B \in RE \setminus R$, אז $B \setminus A = B \cap \overline{A}$ ב-$RE$, אבל לא בהכרח כריעה.</div>
` },
  questions: [
    { id: "D05-Q1", question: "$A \\in RE$ ו-$B \\in R$. איזו טענה נכונה בהכרח על $A \\setminus B$?",
      chk: { kind: "closure", prem: { A: "RE", B: "R" }, opts: [["A - B", "always:RE"], ["A - B", "always:RE\\R"], ["A - B", "always:R"], ["A - B", "always:coRE"]] },
      options: ["$A \\setminus B \\in RE$", "$A \\setminus B \\in RE \\setminus R$", "$A \\setminus B \\in R$", "$A \\setminus B \\in coRE$"], answer: 0,
      recap: "RE ∖ R = RE ∩ (משלים של R) ∈ RE",
      explanation: "$A \\setminus B = A \\cap \\overline{B}$ ו-$\\overline{B} \\in R \\subseteq RE$, והחיתוך של שתי שפות $RE$ ב-$RE$. \"ב-$RE \\setminus R$\" נכשל עם $B = \\Sigma^*$ (תוצאה $\\emptyset$), \"כריעה\" נכשל עם $A = A_{TM}$, $B = \\emptyset$, ו-\"$coRE$\" נכשל באותה דוגמה." },
    { id: "D05-Q2", question: "$A \\in R$ ו-$B \\in RE$. איזו טענה נכונה בהכרח על $A \\setminus B$?",
      chk: { kind: "closure", prem: { A: "R", B: "RE" }, opts: [["A - B", "always:coRE"], ["A - B", "always:RE"], ["A - B", "always:R"], ["A - B", "always:coRE\\R"]] },
      options: ["$A \\setminus B \\in coRE$", "$A \\setminus B \\in RE$", "$A \\setminus B \\in R$", "$A \\setminus B \\in coRE \\setminus R$"], answer: 0,
      recap: "R ∖ RE = R ∩ coRE ∈ coRE (לא בהכרח RE)",
      explanation: "$A \\setminus B = A \\cap \\overline{B}$, כש-$A \\in R \\subseteq coRE$ ו-$\\overline{B} \\in coRE$. החיתוך ב-$coRE$. עם $A = \\Sigma^*$ ו-$B = A_{TM}$ מקבלים $\\overline{A_{TM}}$, שאינה ב-$RE$ ואינה כריעה. לכן \"$RE$\" ו-\"כריעה\" נפסלות. ו-\"$coRE \\setminus R$ בהכרח\" נפסלת עם $A = \\emptyset$." },
    { id: "D05-Q3", question: "$A \\in RE \\setminus R$ ו-$B \\in R$. איזו טענה נכונה בהכרח על $A \\cup B$?",
      chk: { kind: "closure", prem: { A: "RE\\R", B: "R" }, opts: [["A | B", "always:RE"], ["A | B", "always:RE\\R"], ["A | B", "always:R"], ["A | B", "always:coRE"]] },
      options: ["$A \\cup B \\in RE$", "$A \\cup B \\in RE \\setminus R$", "$A \\cup B \\in R$", "$A \\cup B \\in coRE$"], answer: 0,
      recap: "איחוד עם R נשאר ב-RE, אבל עם B = Σ* הוא כריע",
      explanation: "איחוד בין $RE$ ל-$R$ ב-$RE$. אבל אם $B = \\Sigma^*$ האיחוד הוא $\\Sigma^*$, כריעה, ולכן \"בהכרח $RE \\setminus R$\" שגוי. ואם $B = \\emptyset$ האיחוד הוא $A \\notin R$, ולכן \"כריעה\" שגוי, וגם $A \\notin coRE$." },
    { id: "D05-Q4", question: "$A \\in RE$ ו-$B \\in coRE$. איזו טענה נכונה בהכרח על $B \\setminus A$?",
      chk: { kind: "closure", prem: { A: "RE", B: "coRE" }, opts: [["B - A", "always:coRE"], ["B - A", "always:RE"], ["B - A", "always:R"], ["A | B", "always:R"]] },
      options: ["$B \\setminus A \\in coRE$", "$B \\setminus A \\in RE$", "$B \\setminus A \\in R$", "$A \\cup B \\in R$"], answer: 0,
      recap: "coRE ∖ RE = coRE ∩ coRE ∈ coRE",
      explanation: "$B \\setminus A = B \\cap \\overline{A}$, ו-$\\overline{A} \\in coRE$. חיתוך של שתי שפות $coRE$ הוא ב-$coRE$. עם $B = \\overline{A_{TM}}$ ו-$A = \\emptyset$ התוצאה אינה ב-$RE$; עם $A = A_{TM}$ ו-$B = \\emptyset$ האיחוד $A \\cup B$ אינו כריע." },
    { id: "D05-Q5", question: "$A \\in R$ ו-$B \\in RE$. מה **לא ייתכן** על $A \\setminus B$?",
      chk: { kind: "closure", neg: true, prem: { A: "R", B: "RE" }, opts: [["A - B", "possible:RE\\R"], ["A - B", "possible:coRE\\R"], ["A - B", "possible:R"], ["A - B", "possible:coRE"]] },
      options: ["שהיא ב-$RE \\setminus R$", "שהיא ב-$coRE \\setminus R$", "שהיא כריעה", "שהיא ב-$coRE$"], answer: 0,
      recap: "R∖RE ∈ coRE, ולכן לא ייתכן שהיא RE∖R",
      explanation: "ההפרש תמיד ב-$coRE$. אם הוא היה גם ב-$RE \\setminus R$, הוא היה ב-$RE \\cap coRE = R$, סתירה. שלוש האחרות אפשריות: $\\Sigma^* \\setminus A_{TM}$ ב-$coRE \\setminus R$, ו-$\\Sigma^* \\setminus \\Sigma^* = \\emptyset$ כריע (וגם ב-$coRE$)." },
    { ref: "26B-B-Q9", recap: "A, B ∈ RE: ההפרש יכול להיות כריע, ואין הבטחה אחרת" },
  ],
});
