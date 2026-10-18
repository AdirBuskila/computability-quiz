/* Mapping reductions course - level 6: traps with the empty language, Sigma* and complements (brute-forced) */
CC_LEVEL("map", {
  id: "M06", order: 6, icon: "🪤", title: "מלכודות: ∅, Σ* ומשלים",
  goal: "לדעת אילו רדוקציות מותרות כשאחת השפות היא ∅ או Σ*, ומה קורה ברדוקציה של שפה אל המשלים של עצמה.",
  lesson: { html: `
<p>שפה היא <b>לא טריוויאלית</b> אם היא אינה $\emptyset$ ואינה $\Sigma^*$. כדי שתהיה רדוקציה $A \le_m B$ צריך למפות מילים של $A$ אל $B$ ומילים מחוץ ל-$A$ אל מחוץ ל-$B$. מכאן כללים שאינם תלויים בכלל בחישוביות:</p>
<ul>
<li>$A \le_m \emptyset$ רק אם $A = \emptyset$, ו-$A \le_m \Sigma^*$ רק אם $A = \Sigma^*$ (אין לאן למפות את מילות "כן", או את מילות "לא").</li>
<li>$\emptyset \le_m B$ לכל $B \ne \Sigma^*$ (מחזירים תמיד מילה מחוץ ל-$B$), ו-$\Sigma^* \le_m B$ לכל $B \ne \emptyset$.</li>
<li>שפה <b>כריעה</b> לא טריוויאלית מתרדדת לכל שפה לא טריוויאלית: מכריעים את $x$ ומחזירים מילה קבועה בתוך $B$ או מחוצה לה.</li>
<li>כל שפה לא טריוויאלית $A$ מתרדדת ל$\overline{A}$ ולהפך, כשהיא כריעה. ללא כריעות, $L \le_m \overline{L}$ שקול ל-$\overline{L} \le_m L$.</li>
</ul>
<div class="lesson-ex">$A \le_m B$ וגם $A \le_m C$ <b>לא</b> נותן $A \le_m B \cup C$: $H_{TM} \le_m EQ_{TM}$ וגם $H_{TM} \le_m \overline{EQ_{TM}}$, אבל $EQ_{TM} \cup \overline{EQ_{TM}} = \Sigma^*$ ו-$H_{TM} \not\le_m \Sigma^*$ (20A-A-Q1 מעלה זאת).</div>
<div class="lesson-trap">⚠️ <strong>רדוקציה לא מחזירה "בהכרח" כלום.</strong> $A \le_m B$ עם $B$ סופית או רגולרית לא אומר ש-$A$ סופית או רגולרית. ושפה סופית תמיד מתרדדת לשפה אינסופית לא טריוויאלית (23A-A-Q13). וגם: אפשר שאותה פונקציה תהיה רדוקציה גם מ-$A$ ל-$B$ וגם מ-$B$ ל-$A$ (23B-A-Q22).</div>
<div class="lesson-rule">🔑 את הכללים על $\emptyset$ ו-$\Sigma^*$ אפשר לבדוק על עולם קטן של 3 מילים: כל שפה היא תת-קבוצה, וכל פונקציה ממפה מילה למילה.</div>
` },
  questions: [
    { id: "M06-Q1", question: "$A \\le_m \\emptyset$. מה בהכרח נכון על $A$?",
      chk: { kind: "brute-universe", n: 3, opts: ["(not R(A,E)) or A==E", "(not R(A,E)) or A==S", "(not R(A,S)) or A==E", "(not R(A,B)) or B==E"] },
      options: ["$A = \\emptyset$", "$A = \\Sigma^*$", "$A$ לא טריוויאלית", "$A$ יכולה להיות כל שפה"], answer: 0,
      recap: "אין לאן למפות מילה ששייכת ל-A אל השפה הריקה",
      explanation: "אם יש $x \\in A$ אז $f(x) \\in \\emptyset$, שזה בלתי אפשרי. לכן $A$ ריקה. ואם $A$ ריקה, פונקציה קבועה כלשהי עובדת (כל $f(x) \\notin \\emptyset$)." },
    { id: "M06-Q2", question: "איזו טענה נכונה על רדוקציות מהשפה הריקה?",
      chk: { kind: "brute-universe", n: 3, opts: ["(B!=S) <= R(E,B)", "R(E,B)", "(not R(E,B)) or B==E", "(B!=E) <= R(E,B)"] },
      options: ["$\\emptyset \\le_m B$ לכל $B \\ne \\Sigma^*$", "$\\emptyset \\le_m B$ לכל $B$ בלי יוצא מן הכלל", "$\\emptyset \\le_m B$ רק אם $B = \\emptyset$", "$\\emptyset \\le_m B$ לכל $B \\ne \\emptyset$"], answer: 0,
      recap: "∅ מתרדדת לכל שפה שאינה Σ*",
      explanation: "מחזירים תמיד מילה $y \\notin B$ (קיימת כש-$B \\ne \\Sigma^*$). אם $B = \\Sigma^*$ אין מילה כזו, ולכן $\\emptyset \\not\\le_m \\Sigma^*$. לכן האפשרות \"לכל $B$\" שגויה, וגם \"לכל $B \\ne \\emptyset$\" (כי $B = \\Sigma^*$ נכשלת)." },
    { id: "M06-Q3", question: "איזו טענה נכונה לכל שלוש שפות $A, B, C$?",
      chk: { kind: "brute-universe", n: 2, opts: ["(not (R(A,B) and R(A,C))) or R(A,B|C)", "(not (R(A,B) and R(A,C))) or R(A,B&C)", "(not (R(A,B) and R(B,C))) or R(A,C)", "(not (R(A,B) and R(A,C))) or R(B,C)"] },
      options: ["אם $A \\le_m B$ וגם $A \\le_m C$ אז $A \\le_m B \\cup C$", "אם $A \\le_m B$ וגם $A \\le_m C$ אז $A \\le_m B \\cap C$", "אם $A \\le_m B$ וגם $B \\le_m C$ אז $A \\le_m C$", "אם $A \\le_m B$ וגם $A \\le_m C$ אז $B \\le_m C$"], answer: 2,
      recap: "רדוקציה טרנזיטיבית; איחוד וחיתוך של יעדים לא משמרים",
      explanation: "רק הטרנזיטיביות נכונה תמיד. דוגמה נגדית לשתי הראשונות: $A = \\{1\\}$, $B = \\{1\\}$, $C = \\{0\\}$. אז $B \\cup C$ היא כל העולם ($A$ לא מתרדדת אליה), ו-$B \\cap C = \\emptyset$ (גם לא). ולרביעית: $B$ ו-$C$ שונות מבחינת קושי." },
    { id: "M06-Q4", question: "$A$ שפה לא טריוויאלית וכריעה. מה נכון?",
      chk: { kind: "brute-universe", n: 3, opts: ["((A!=E) and (A!=S)) <= R(A,comp(A))", "(not R(A,comp(A))) or A==E", "(not R(A,comp(A))) or A==S", "(not R(A,comp(A))) or A==E or A==S"] },
      options: ["אם $A$ כריעה ולא טריוויאלית אז $A \\le_m \\overline{A}$", "אם $A \\le_m \\overline{A}$ אז $A = \\emptyset$", "אם $A \\le_m \\overline{A}$ אז $A = \\Sigma^*$", "אם $A \\le_m \\overline{A}$ אז $A$ טריוויאלית"], answer: 0,
      recap: "שפה כריעה לא טריוויאלית מתרדדת למשלים שלה",
      explanation: "בוחרים $a \\in A$ ו-$b \\notin A$. ממפים כל איבר של $A$ אל $b$ (שנמצא ב-$\\overline{A}$) וכל איבר שלא ב-$A$ אל $a$. הפונקציה חשיבה כש-$A$ כריעה. בעולם קטן (שפות סופיות) זה בדיוק מה שנבדק. ובנוסף, $\\emptyset$ ו-$\\Sigma^*$ הן הטריוויאליות היחידות שלא מתרדדות למשלים שלהן." },
    { id: "M06-Q5", question: "מה נכון על שפות $A$ ש-$A \\le_m \\Sigma^*$?",
      chk: { kind: "brute-universe", n: 3, opts: ["(not R(A,S)) or A==S", "(not R(A,S)) or A!=S", "R(A,S)", "(A!=S) or R(A,B)"] },
      options: ["$A = \\Sigma^*$", "$A \\ne \\Sigma^*$", "כל שפה $A$ מתרדדת אל $\\Sigma^*$", "$\\Sigma^*$ מתרדדת לכל שפה $B$"], answer: 0,
      recap: "רק Σ* מתרדדת ל-Σ*",
      explanation: "אם יש $x \\notin A$ אז $f(x) \\notin \\Sigma^*$, בלתי אפשרי. לכן $A = \\Sigma^*$. וגם $\\Sigma^*$ אינה מתרדדת ל-$\\emptyset$, כך שהאפשרות האחרונה שגויה." },
    { ref: "23S-A-Q24", recap: "A ≤m ∅ נותן A = ∅; ∅ ≤m B נכון לכל B ≠ Σ*" },
  ],
});
