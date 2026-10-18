/* Mapping reductions course - level 3: what a reduction proves, and which reductions cannot exist */
CC_LEVEL("map", {
  id: "M03", order: 3, icon: "🧭", title: "מה מוכיחים ברדוקציה, ואילו רדוקציות לא קיימות",
  goal: "לבחור את הכיוון הנכון כדי להוכיח ש-L לא כריעה או לא ניתנת לקבלה, ולזהות רדוקציה שאי אפשר שתתקיים.",
  lesson: { html: `
<p>כדי להוכיח שמשהו <b>קשה</b>, מרדדים <b>מ</b>שפה קשה ידועה <b>אל</b> השפה החדשה (קושי זורם ימינה):</p>
<table>
<thead><tr><th>רוצים להוכיח</th><th>מרדדים</th></tr></thead>
<tbody>
<tr><td>$L \notin R$</td><td>$A_{TM} \le_m L$ (או כל שפה לא כריעה)</td></tr>
<tr><td>$L \notin RE$</td><td>$\overline{A_{TM}} \le_m L$ או $\overline{H_{TM}} \le_m L$</td></tr>
<tr><td>$L \notin coRE$</td><td>$A_{TM} \le_m L$ או $H_{TM} \le_m L$ (כי אז $\overline{A_{TM}} \le_m \overline{L}$ ו-$\overline{L} \notin RE$)</td></tr>
</tbody></table>
<div class="lesson-trap">⚠️ <strong>הכיוון.</strong> $L \le_m A_{TM}$ מוכיח רק ש-$L \in RE$. כדי להוכיח קושי הכיוון הוא <b>אל</b> $L$. ו-$A \le_m B$ לבדו אינו אומר כלום עד שיודעים משהו על אחת השפות.</div>
<h3>רדוקציה שלא יכולה להתקיים</h3>
<p>אם $B \in RE$ אז כל $A \le_m B$ חייבת להיות ב-$RE$. לכן <b>אי אפשר</b> לרדד שפה שאינה ב-$RE$ אל שפה ב-$RE$; ובדומה לגבי $coRE$ ו-$R$. בפרט <b>אין רדוקציה בין שפה ב-$RE \setminus R$ לשפה ב-$coRE \setminus R$</b> באף כיוון.</p>
<div class="lesson-ex">$H_{TM} \le_m E_{TM}$? $E_{TM} \in coRE$, אבל $H_{TM} \notin coRE$. בלתי אפשרי. לעומת זאת $\overline{H_{TM}} \le_m E_{TM}$ אפשרית, וגם $H_{TM} \le_m \overline{E_{TM}}$ (23A-A-Q20 מדגים זאת). וגם $EQ_{TM} \le_m L$ נותנת ש-$L$ ו-$\overline{L}$ שתיהן לא ב-$RE$ (25B-A-Q2); ובין שפה ב-$RE \setminus R$ לשפה ב-$coRE \setminus R$ אין רדוקציה כלל (26B-B-Q1 מתבסס על כך).</div>
<div class="lesson-rule">🔑 <strong>$L \le_m \overline{L}$</strong> שקול ל-$\overline{L} \le_m L$. אם בנוסף $L \in RE$ אז $\overline{L} \in RE$ ולכן $L \in R$. ואם $L \notin R$ אז $L \notin RE$ וגם $L \notin coRE$.</div>
` },
  questions: [
    { id: "M03-Q1", question: "איזו מהרדוקציות הבאות **לא יכולה** להתקיים?",
      chk: { kind: "red-impossible", opts: [["H_TM", "E_TM"], ["H_TM", "notE_TM"], ["coH_TM", "E_TM"], ["E_TM", "EQ_TM"]] },
      options: ["$H_{TM} \\le_m E_{TM}$", "$H_{TM} \\le_m \\overline{E_{TM}}$", "$\\overline{H_{TM}} \\le_m E_{TM}$", "$E_{TM} \\le_m EQ_{TM}$"], answer: 0,
      recap: "אין רדוקציה בין RE∖R ל-coRE∖R",
      explanation: "$E_{TM} \\in coRE$ אבל $H_{TM} \\notin coRE$, ולכן $H_{TM} \\le_m E_{TM}$ בלתי אפשרית. שלוש האחרות קיימות: $H_{TM} \\le_m \\overline{E_{TM}}$ ו-$\\overline{H_{TM}} \\le_m E_{TM}$ בעזרת המכונה $K_{M,w}$ (נראה בהמשך), ו-$E_{TM} \\le_m EQ_{TM}$ כי לבדוק $L(M) = \\emptyset$ זה בדיוק לבדוק שוויון עם מכונה שדוחה הכול." },
    { id: "M03-Q2", question: "איזו מהרדוקציות הבאות **לא יכולה** להתקיים?",
      chk: { kind: "red-impossible", opts: [["EQ_TM", "A_TM"], ["A_TM", "H_TM"], ["H_TM", "ALL_TM"], ["A_TM", "ALL_TM"]] },
      options: ["$EQ_{TM} \\le_m A_{TM}$", "$A_{TM} \\le_m H_{TM}$", "$H_{TM} \\le_m ALL_{TM}$", "$A_{TM} \\le_m ALL_{TM}$"], answer: 0,
      recap: "שפה שלא ב-RE לא מתרדדת לשפה ב-RE",
      explanation: "$A_{TM} \\in RE$ אבל $EQ_{TM} \\notin RE$, ולכן אין רדוקציה $EQ_{TM} \\le_m A_{TM}$. ההפכים קיימים: $A_{TM}$ ו-$H_{TM}$ מתרדדות זו לזו, ושתיהן מתרדדות ל-$ALL_{TM}$." },
    { id: "M03-Q3", question: "רוצים להוכיח ש-$L$ **אינה ניתנת לקבלה**. איזו רדוקציה מספיקה?",
      chk: { kind: "rules", opts: ["proof.notRE_from_coATM", "proof.ATM_gives_notRE", "proof.L_to_coATM", "proof.L_to_ATM"] },
      options: ["$\\overline{A_{TM}} \\le_m L$", "$A_{TM} \\le_m L$", "$L \\le_m \\overline{A_{TM}}$", "$L \\le_m A_{TM}$"], answer: 0,
      recap: "∉ RE: מרדדים משפה שאינה ב-RE אל L",
      explanation: "$\\overline{A_{TM}} \\notin RE$ והקושי זורם אל $L$. הרדוקציה $A_{TM} \\le_m L$ נותנת רק ש-$L$ לא כריעה ולא ב-$coRE$ ($L$ יכולה להיות ב-$RE$). שתי האחרונות בכיוון ההפוך ומראות הכלה במחלקות." },
    { id: "M03-Q4", question: "נתון $A_{TM} \\le_m L$. מה בהכרח נכון על $L$?",
      chk: { kind: "rules", opts: ["proof.ATM_gives_notR_notcoRE", "proof.ATM_gives_notRE", "proof.ATM_gives_in_RE", "proof.ATM_gives_in_coRE"] },
      options: ["$L \\notin R$ וגם $L \\notin coRE$", "$L \\notin RE$", "$L \\in RE$", "$L \\in coRE$"], answer: 0,
      recap: "A_TM ≤m L: L לא כריעה, ולא ב-coRE (אבל יכולה להיות ב-RE)",
      explanation: "$A_{TM} \\notin R$ ולכן $L \\notin R$. ובנוסף $\\overline{A_{TM}} \\le_m \\overline{L}$ ו-$\\overline{A_{TM}} \\notin RE$, ולכן $\\overline{L} \\notin RE$, כלומר $L \\notin coRE$. על $RE$ אין מסקנה: $L = H_{TM}$ ב-$RE$ ואילו $L = EQ_{TM}$ (ש-$A_{TM}$ מתרדדת אליה) אינה ב-$RE$." },
    { id: "M03-Q5", question: "נתון $L \\in RE$ וגם $L \\le_m \\overline{L}$. מה בהכרח נכון?",
      chk: { kind: "rules", opts: ["x.L_le_coL_RE_in_R", "x.L_le_coL_RE_in_RE_notR", "x.L_le_coL_RE_coRE_notR", "x.L_le_coL_RE_none"] },
      options: ["$L \\in R$", "$L \\in RE \\setminus R$", "$L \\in coRE \\setminus R$", "$L$ לא ב-$RE$ ולא ב-$coRE$"], answer: 0,
      recap: "L ≤m המשלים שלה ו-L ∈ RE ⟹ L כריעה",
      explanation: "אותה פונקציה שמרדדת את $L$ אל $\\overline{L}$ מרדדת גם את $\\overline{L}$ אל $L$ (משלימים). כיוון ש-$L \\in RE$, קלות זורמת שמאלה ונקבל $\\overline{L} \\in RE$. אז גם $L$ וגם המשלים שלה ב-$RE$, ולפי פוסט $L \\in R$." },
    { ref: "22A-A-Q10", recap: "L̄ ≤m L ו-L ∉ R ⟹ L לא ב-RE ולא ב-coRE" },
  ],
});
