/* Decidability course - level 4: closure table (machine-checked by the closure engine) */
CC_LEVEL("dec", {
  id: "D04", order: 4, icon: "🧱", title: "טבלת הסגירות",
  goal: "לדעת אילו פעולות משמרות R, RE ו-coRE, ולהסביר כל כניסה בטבלה ברעיון אחד.",
  lesson: { html: `
<p>אומרים ש"מחלקה סגורה לפעולה" אם התוצאה של הפעולה על שפות מהמחלקה חייבת להישאר בה. הטבלה שצריך לזכור:</p>
<table>
<thead><tr><th>פעולה</th><th>$R$</th><th>$RE$</th><th>$coRE$</th></tr></thead>
<tbody>
<tr><td>איחוד $A \cup B$</td><td>כן</td><td>כן</td><td>כן</td></tr>
<tr><td>חיתוך $A \cap B$</td><td>כן</td><td>כן</td><td>כן</td></tr>
<tr><td>משלים $\overline{A}$</td><td>כן</td><td><b>לא</b></td><td><b>לא</b></td></tr>
<tr><td>שרשור $AB$ וכוכב $A^*$</td><td>כן</td><td>כן</td><td>כן</td></tr>
</tbody></table>
<ul>
<li><b>איחוד ב-$RE$:</b> מריצים את $M_1$ ו-$M_2$ במקביל ומקבלים כשאחת קיבלה. סדרתית זה לא עובד, כי אחת עלולה להיתקע.</li>
<li><b>חיתוך ב-$RE$:</b> אפשר גם בזו אחר זו: אם אחת נתקעת, המילה ממילא לא בחיתוך.</li>
<li><b>משלים ב-$R$:</b> מחליפים $q_{acc}$ ו-$q_{rej}$ במכונה מכריעה. ב-$RE$ אי אפשר (אחרת $RE = R$).</li>
<li><b>שרשור וכוכב:</b> מכונה אי-דטרמיניסטית מנחשת איפה לחתוך את המילה ובודקת כל חלק.</li>
<li><b>$coRE$</b> היא תמונת מראה של $RE$, ואותן סגירויות עוברות לשם בעזרת דה-מורגן.</li>
</ul>
<div class="lesson-rule">🔑 <strong>משלים הופך כיוון:</strong> אם $A \in RE$ אז $\overline{A} \in coRE$ (לא ב-$RE$ בהכרח). אם $A \in coRE$ אז $\overline{A} \in RE$. ובכל מקרה $\overline{A} \in R$ אם ורק אם $A \in R$.</div>
<div class="lesson-trap">⚠️ סגירות מדברת רק על הכיוון "רכיבים ← תוצאה". ב-24A-A-Q4 ו-22A-B-Q6: אם $A, B \in coRE$ אז גם $A\#B = \{x\#y \mid x \in A, y \in B\}$ ב-$coRE$ (וגם בשתי האחרות). אבל מהעובדה ש-$A \cup B \in R$ לא נובע ש-$A, B \in R$.</div>
` },
  questions: [
    { id: "D04-Q1", question: "$A, B \\in RE$. איזו טענה נכונה בהכרח?",
      chk: { kind: "closure", prem: { A: "RE", B: "RE" }, opts: [["A | B", "always:RE"], ["~A", "always:RE"], ["A - B", "always:RE"], ["A | B", "always:R"]] },
      options: ["$A \\cup B \\in RE$", "$\\overline{A} \\in RE$", "$A \\setminus B \\in RE$", "$A \\cup B \\in R$"], answer: 0,
      recap: "RE סגורה לאיחוד, לא למשלים ולא להפרש",
      explanation: "איחוד בהרצה מקבילה נשאר ב-$RE$. משלים והפרש (שהוא חיתוך עם משלים) מוציאים מ-$RE$: $A_{TM} \in RE$ אבל $\overline{A_{TM}} \notin RE$, וההפרש $\Sigma^* \setminus A_{TM}$ הוא בדיוק המשלים הזה. ואיחוד של שפות $RE$ לא חייב להיות כריע (למשל $A_{TM} \cup \emptyset$)." },
    { id: "D04-Q2", question: "$A, B \\in coRE$. איזו טענה נכונה בהכרח?",
      chk: { kind: "closure", prem: { A: "coRE", B: "coRE" }, opts: [["A & B", "always:coRE"], ["~A", "always:coRE"], ["A | B", "always:RE"], ["A - B", "always:coRE"]] },
      options: ["$A \\cap B \\in coRE$", "$\\overline{A} \\in coRE$", "$A \\cup B \\in RE$", "$A \\setminus B \\in coRE$"], answer: 0,
      recap: "coRE סגורה לחיתוך ואיחוד, לא למשלים ולא להפרש",
      explanation: "$coRE$ היא תמונת מראה של $RE$ ולכן סגורה לחיתוך. המשלים של שפה ב-$coRE$ הוא ב-$RE$, לא בהכרח ב-$coRE$. ההפרש $A \\setminus B = A \\cap \\overline{B}$ מערבב $coRE$ עם $RE$: עם $A = \\Sigma^*$ ו-$B = \\overline{A_{TM}}$ התוצאה $A_{TM}$ אינה ב-$coRE$." },
    { id: "D04-Q3", question: "$A \\in RE$. מה בהכרח נכון על המשלים $\\overline{A}$?",
      chk: { kind: "closure", prem: { A: "RE" }, opts: [["~A", "always:coRE"], ["~A", "always:RE"], ["~A", "always:R"], ["~A", "possible:RE\\R"]] },
      options: ["$\\overline{A} \\in coRE$", "$\\overline{A} \\in RE$", "$\\overline{A} \\in R$", "ייתכן ש-$\\overline{A} \\in RE \\setminus R$"], answer: 0,
      recap: "משלים של RE הוא coRE",
      explanation: "זו ההגדרה של $coRE$. ב-$RE$ המשלים לא חייב להיות ($A_{TM}$), וכריע בוודאי לא. ו\"ייתכן ש-$\\overline{A} \\in RE \\setminus R$\": אם $\\overline{A} \\in RE$, אז לפי פוסט $A \\in R$ ולכן גם $\\overline{A} \\in R$, ולכן זה בלתי אפשרי." },
    { id: "D04-Q4", question: "$A, B \\in R$. איזו טענה נכונה?",
      chk: { kind: "closure", prem: { A: "R", B: "R" }, opts: [["A - B", "always:R"], ["A | B", "always:RE\\R"], ["~A", "always:RE\\R"], ["A & B", "always:coRE\\R"]] },
      options: ["$A \\setminus B \\in R$", "$A \\cup B \\in RE \\setminus R$", "$\\overline{A} \\in RE \\setminus R$", "$A \\cap B \\in coRE \\setminus R$"], answer: 0,
      recap: "R סגורה לכל הפעולות",
      explanation: "$R$ סגורה לאיחוד, חיתוך, משלים ולכן גם להפרש. שלוש האחרות טוענות שהתוצאה לא כריעה, וזה בלתי אפשרי כשהיא כריעה בהכרח." },
    { id: "D04-Q5", question: "$A, B \\in RE$. איזו טענה נכונה בהכרח?",
      chk: { kind: "closure", prem: { A: "RE", B: "RE" }, opts: [["A @ B", "always:RE"], ["A - B", "always:RE"], ["~A", "always:RE"], ["A & B", "always:coRE"]] },
      options: ["השרשור $AB$ שייך ל-$RE$", "$A \\setminus B \\in RE$", "$\\overline{A} \\in RE$", "$A \\cap B \\in coRE$"], answer: 0,
      recap: "שרשור נשאר ב-RE: מנחשים נקודת פיצול",
      explanation: "מכונה אי-דטרמיניסטית מנחשת נקודת פיצול $w = uv$ ומריצה את $M_1$ על $u$ ואת $M_2$ על $v$. שלוש האחרות מוציאות מ-$RE$: משלים והפרש כבר ראינו, וחיתוך של שפות $RE$ לא חייב להיות ב-$coRE$ (עם $A = B = A_{TM}$)." },
    { ref: "24A-A-Q4", recap: "A#B: אם A, B ∈ coRE אז A#B ∈ coRE" },
  ],
});
