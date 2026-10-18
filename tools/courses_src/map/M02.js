/* Mapping reductions course - level 2: where easiness and hardness flow */
CC_LEVEL("map", {
  id: "M02", order: 2, icon: "➡️", title: "לאן זורמות קלות וקושי",
  goal: "לדעת מה מותר להסיק מ-A ≤m B על המחלקות של A ושל B, ומה אסור.",
  lesson: { html: `
<p>$A \le_m B$ אומר ש-$A$ <b>לא קשה יותר</b> מ-$B$: פתרון ל-$B$ נותן פתרון ל-$A$ (מתרגמים בעזרת $f$ ושואלים את $B$). לכן $B$ היא "חסם עליון" על הקושי של $A$.</p>
<div class="lesson-rule">🔑 <strong>קלות זורמת שמאלה (מ-$B$ אל $A$), קושי זורם ימינה (מ-$A$ אל $B$).</strong></div>
<table>
<thead><tr><th>ידוע (ו-$A \le_m B$)</th><th>מסקנה</th></tr></thead>
<tbody>
<tr><td>$B \in R$</td><td>$A \in R$</td></tr>
<tr><td>$B \in RE$</td><td>$A \in RE$</td></tr>
<tr><td>$B \in coRE$</td><td>$A \in coRE$</td></tr>
<tr><td>$A \notin R$</td><td>$B \notin R$</td></tr>
<tr><td>$A \notin RE$</td><td>$B \notin RE$</td></tr>
<tr><td>$A \notin coRE$</td><td>$B \notin coRE$</td></tr>
</tbody></table>
<p>כל השורות עוברות <b>רק</b> מהצד שהוצג. ההפך אינו נכון: $A \in R$ לא אומר כלום על $B$, כי כל שפה כריעה מתרדדת לכל שפה לא טריוויאלית (מכריעים את $x$ ומחזירים מילה קבועה בתוך $B$ או מחוץ לה).</p>
<h3>עוד תכונות</h3>
<ul>
<li><b>משלים:</b> $A \le_m B \iff \overline{A} \le_m \overline{B}$, באותה פונקציה בדיוק. לכן שורות ה-$coRE$ נובעות משורות ה-$RE$.</li>
<li><b>טרנזיטיביות:</b> $A \le_m B$ ו-$B \le_m C$ נותנים $A \le_m C$ (מרכיבים את הפונקציות).</li>
<li><b>אין סימטריה:</b> $A_{TM} \le_m ALL_{TM}$ אבל $ALL_{TM} \not\le_m A_{TM}$, ולכן $\le_m$ אינו יחס שקילות (23S-A-Q22).</li>
</ul>
<div class="lesson-trap">⚠️ <strong>"לא קיימת רדוקציה" גם מעביר.</strong> אם $A \le_m B$ ו-$A \not\le_m C$ אז $B \not\le_m C$ (אחרת הרכבה הייתה נותנת $A \le_m C$). ראו 25B-A-Q1. ההפך אינו נכון: $A \not\le_m B$ ו-$B \le_m C$ לא אומר ש-$A \not\le_m C$.</div>
` },
  questions: [
    { id: "M02-Q1", question: "נתון $A \\le_m B$. איזו טענה נכונה?",
      chk: { kind: "rules", opts: ["red.R_down", "red.R_up", "red.B_notR_gives_A_notR", "red.symmetric"] },
      options: ["אם $B \\in R$ אז $A \\in R$", "אם $A \\in R$ אז $B \\in R$", "אם $B \\notin R$ אז $A \\notin R$", "בהכרח גם $B \\le_m A$"], answer: 0,
      recap: "קלות זורמת מ-B אל A",
      explanation: "פתרון ל-$B$ נותן פתרון ל-$A$. את השאר אפשר להפריך כש-$A = \\emptyset$ (כריעה) ו-$B = A_{TM}$ (לא כריעה): $A \\le_m B$ מתקיימת, אבל $A \\in R$ לא נותן $B \\in R$, $B \\notin R$ לא נותן $A \\notin R$, ו-$B \\le_m A$ לא מתקיימת." },
    { id: "M02-Q2", question: "נתון $A \\le_m B$. איזו טענה נכונה?",
      chk: { kind: "rules", opts: ["red.notRE_flows", "red.RE_up", "red.B_notRE_gives_A_notRE", "red.coRE_down_to_RE"] },
      options: ["אם $A \\notin RE$ אז $B \\notin RE$", "אם $A \\in RE$ אז $B \\in RE$", "אם $B \\notin RE$ אז $A \\notin RE$", "אם $B \\in coRE$ אז $A \\in RE$"], answer: 0,
      recap: "קושי זורם מ-A אל B: A ∉ RE ⟹ B ∉ RE",
      explanation: "אילו $B \\in RE$ היינו מקבלים $A \\in RE$ (שורת ה-$RE$), וזו שקולה לטענה הנכונה. שאר האפשרויות הפוכות: עם $A = \\emptyset$ ו-$B \\notin RE$ מתקיים $A \\le_m B$ בלי שאף אחת מהן נכונה." },
    { id: "M02-Q3", question: "איזו טענה על משלימים נכונה תמיד?",
      chk: { kind: "rules", opts: ["red.complement_same_f", "red.complement_one_side", "red.complement_target_only", "red.complement_swapped"] },
      options: ["$A \\le_m B$ אם ורק אם $\\overline{A} \\le_m \\overline{B}$", "$A \\le_m B$ אם ורק אם $\\overline{A} \\le_m B$", "$A \\le_m B$ אם ורק אם $A \\le_m \\overline{B}$", "$A \\le_m B$ אם ורק אם $\\overline{B} \\le_m \\overline{A}$"], answer: 0,
      recap: "אותה f מרדדת את A ל-B ואת המשלים של A למשלים של B",
      explanation: "$x \\in A \\iff f(x) \\in B$ שקול ל-$x \\notin A \\iff f(x) \\notin B$. זה מראה שהפונקציה $f$ עצמה מרדדת גם את המשלימים. שלושת האחרות מערבבות משלים בצד אחד בלבד או הופכות את כיוון הרדוקציה." },
    { id: "M02-Q4", question: "איזו טענה נכונה לכל שלוש שפות $A, B, C$?",
      chk: { kind: "rules", opts: ["red.transitive", "red.common_source", "red.common_target", "red.equiv_means_equal"] },
      options: ["אם $A \\le_m B$ וגם $B \\le_m C$ אז $A \\le_m C$", "אם $A \\le_m B$ וגם $A \\le_m C$ אז $B \\le_m C$", "אם $A \\le_m B$ וגם $C \\le_m B$ אז $A \\le_m C$", "אם $A \\le_m B$ וגם $B \\le_m A$ אז $A = B$"], answer: 0,
      recap: "רדוקציה היא טרנזיטיבית",
      explanation: "מרכיבים את שתי הפונקציות: $x \\in A \\iff f(x) \\in B \\iff g(f(x)) \\in C$. הטענות האחרות מניחות סימטריה שאין: למשל $A_{TM}$ ו-$H_{TM}$ מתרדדות זו לזו ובכל זאת שונות." },
    { id: "M02-Q5", question: "נתון $A \\le_m B$ וגם $B \\in coRE$. מה בהכרח נכון?",
      chk: { kind: "rules", opts: ["red.coRE_down", "red.coRE_up", "red.coRE_down_to_RE", "red.RE_down_wrong_class"] },
      options: ["$A \\in coRE$", "אם $A \\in coRE$ אז $B \\in coRE$", "$A \\in RE$", "$A \\in R$"], answer: 0,
      recap: "coRE ירדה שמאלה כמו RE",
      explanation: "אותה הוכחה כמו ב-$RE$: ממפים את $x$ ל-$f(x)$ ומשתמשים במכונה של $\\overline{B}$ (באותה פונקציה, $A \\le_m B$ נותן $\\overline{A} \\le_m \\overline{B}$). הטענה ש-$A \\in coRE$ גוררת $B \\in coRE$ היא הכיוון ההפוך, והטענות על $A \\in RE$ ועל $A \\in R$ מניחות יותר ממה שנתון." },
    { ref: "25S-B-Q1", recap: "A ≤m B ו-B ∈ coRE ⟹ A ∈ coRE, אבל לא להפך" },
  ],
});
