/* Decidability course - level 6: classifying a language of machines by the shape of its condition */
CC_LEVEL("dec", {
  id: "D06", order: 6, icon: "🧭", title: "מתכון הסיווג: קיים, לכל או חסם",
  goal: "לסווג שפה של מכונות ל-R, RE∖R, coRE∖R או אף אחת, לפי צורת התנאי: חסם סופי, \"קיים\", \"לכל\" או שוויון.",
  lesson: { html: `
<p>שואלים שתי שאלות: מה צריך לראות כדי לענות <b>כן</b>, ומה כדי לענות <b>לא</b>?</p>
<table>
<thead><tr><th>צורת התנאי</th><th>המחלקה</th><th>למה</th></tr></thead>
<tbody>
<tr><td><b>חסם סופי</b> על צעדים או תאים</td><td>$R$</td><td>מסמלצים עד החסם ועונים</td></tr>
<tr><td>"קיימת מילה ש-$M$ מקבלת / עוצרת עליה"</td><td>$RE \setminus R$</td><td>הרצה משולבת, מקבלים כשמצאנו</td></tr>
<tr><td>$|L(M)| \ge k$</td><td>$RE \setminus R$</td><td>מחכים ל-$k$ מילים מתקבלות</td></tr>
<tr><td>"לכל מילה" / "$M$ לא מקבלת אף מילה"</td><td>$coRE \setminus R$</td><td>המשלים הוא "קיימת מילה שמפרה"</td></tr>
<tr><td>$|L(M)| \le k$</td><td>$coRE \setminus R$</td><td>המשלים הוא $|L(M)| > k$</td></tr>
<tr><td>$L(M)$ = שפה מסוימת, הכלה, שוויון, $|L(M)| = k$</td><td>אף אחת</td><td>צריך גם "קיים" וגם "לכל"</td></tr>
</tbody></table>
<p>אחרי הסיווג בודקים שהשפה <b>אינה כריעה</b> בדרך כלל על ידי רדוקציה מ-$A_{TM}$ (נתרגל בקורס רדוקציות המיפוי). כאן מתרגלים את הצד השני: מה השפה בכלל.</p>
<div class="lesson-ex">"$M$ מקבלת מילה כלשהי שהיא פלינדרום" (22A-C-Q2) היא "קיים": $RE \setminus R$. "$M$ מקבלת מילה מהצורה $ww$" (24A-C-Q2): גם כן. "$M$ מקבלת את 00 ואת 11" (26B-A-Q6): שתי הרצות, ו-$RE \setminus R$.</div>
<div class="lesson-trap">⚠️ <strong>חסם שתלוי בקלט עם "לכל" משנה מחלקה.</strong> "$M$ עוצרת על $w$ בתוך $|w|^2$ צעדים" כשהמילה $w$ נתונה בקלט: חסם סופי, כריע. אבל "<b>לכל</b> מילה $w$, $M$ עוצרת תוך $|w|^2$ צעדים" היא $coRE \setminus R$: מילה מפרה נמצאת בזמן סופי, אבל אי אפשר לבדוק אינסוף מילים. ו"קיימת מילה" עם חסם שלא תלוי ב-$w$, כמו "תוך $|\langle M\rangle|$ צעדים", חוזרת ל-$R$: בתוך $k$ צעדים נקראים לכל היותר $k$ תאים, ויש מספר סופי של מילים לבדוק.</div>
<div class="lesson-trap">⚠️ <strong>"דוחה" אינו "לא מקבלת".</strong> "$M$ דוחה את $w$" אפשר לראות בזמן סופי: $RE \setminus R$. "$w \notin L(M)$" כולל גם לולאה: $coRE \setminus R$. ו"$M$ לא עוצרת על אף מילה" היא $coRE \setminus R$.</div>
` },
  questions: [
    { id: "D06-Q1", question: "$L = \\{\\langle M\\rangle \\mid (*)\\}$ כאשר (*): $M$ עוצרת על מילה כלשהי שמתחילה ב-0. לאיזו מחלקה היא שייכת?",
      chk: { kind: "shape", shape: "exists", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "אף אחת מהשלוש"], answer: 1,
      recap: "\"קיימת מילה ש...\" בלי חסם: RE∖R",
      explanation: "\"קיימת מילה\" מתקבלת בהרצה משולבת: אין חסם על הצעדים, ולכן לא כריעה, אבל אפשר לקבל ברגע שמצאנו מילה כזו. היא לא ב-$coRE$ כי אז היה לה גם מכריע." },
    { id: "D06-Q2", question: "$L = \\{\\langle M, w\\rangle \\mid (*)\\}$ כאשר (*): $M$ עוצרת על $w$ בתוך 100 צעדים לכל היותר. לאיזו מחלקה היא שייכת?",
      chk: { kind: "shape", shape: "bounded", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "אף אחת מהשלוש"], answer: 0,
      recap: "חסם צעדים קבוע: מסמלצים 100 צעדים ועונים",
      explanation: "מריצים את $M$ על $w$ למשך 100 צעדים: אם עצרה עד אז, מקבלים, ואחרת דוחים. הריצה סופית, והשפה כריעה. בעיית העצירה הכללית אינה כריעה בגלל שאין חסם." },
    { id: "D06-Q3", question: "$L = \\{\\langle M\\rangle \\mid (*)\\}$ כאשר (*): $M$ לא מקבלת אף מילה שמתחילה ב-0. לאיזו מחלקה היא שייכת?",
      chk: { kind: "shape", shape: "forall", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "אף אחת מהשלוש"], answer: 2,
      recap: "\"אף מילה\" = \"לכל\": המשלים הוא \"קיימת מילה\" ולכן coRE∖R",
      explanation: "המשלים הוא \"$M$ מקבלת מילה שמתחילה ב-0\", שהיא \"קיים\" ולכן ב-$RE \\setminus R$. לכן $L \\in coRE \\setminus R$." },
    { id: "D06-Q4", question: "$L = \\{\\langle M \\rangle \\mid |L(M)| \\le 2\\}$. לאיזו מחלקה היא שייכת?",
      chk: { kind: "shape", shape: "count_le", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "אף אחת מהשלוש"], answer: 2,
      recap: "|L(M)| ≤ k : המשלים |L(M)| ≥ k+1 הוא RE, ולכן coRE∖R",
      explanation: "המשלים הוא $|L(M)| \\ge 3$: מחכים לשלוש מילים מתקבלות. לכן המשלים ב-$RE \\setminus R$ ו-$L \\in coRE \\setminus R$. החסם התחתון (\"לפחות\") נותן $RE$ והעליון (\"לכל היותר\") נותן $coRE$." },
    { id: "D06-Q5", question: "$L = \\{\\langle M \\rangle \\mid L(M) = \\{0, 1\\}\\}$. לאיזו מחלקה היא שייכת?",
      chk: { kind: "shape", shape: "specific", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "אף אחת מהשלוש"], answer: 3,
      recap: "שפה מסוימת בדיוק: צריך גם \"קיים\" (0 ו-1 ב-L) וגם \"לכל\" (שום דבר אחר)",
      explanation: "לאשר צריך לראות ש-0 ו-1 מתקבלות ($RE$) וגם שאף מילה אחרת לא מתקבלת (\"לכל\", $coRE$). שני התנאים יחד אינם ב-$RE$ ואינם ב-$coRE$." },
    { ref: "23S-A-Q9", recap: "|L(M)| ≥ 3: מחכים לשלוש מילים, ולכן RE∖R" },
  ],
});
