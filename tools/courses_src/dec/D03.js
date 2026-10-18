/* Decidability course - level 3: the named languages and their classes */
CC_LEVEL("dec", {
  id: "D03", order: 3, icon: "🗂️", title: "השפות המפורסמות והמחלקה של כל אחת",
  goal: "לזכור את הטבלה: לאיזו מחלקה שייכת כל אחת מהשפות A_TM, H_TM, E_TM, EQ_TM ושל המשלימות שלהן, ולנמק למה.",
  lesson: { html: `
<p>ארבע שפות של זוגות ושל מכונות, ושמן קבוע בכל שאלה:</p>
<ul>
<li>$A_{TM} = \{\langle M, w\rangle \mid M \text{ accepts } w\}$: האם המכונה מקבלת את המילה.</li>
<li>$H_{TM} = \{\langle M, w\rangle \mid M \text{ halts on } w\}$: האם המכונה עוצרת על המילה.</li>
<li>$E_{TM} = \{\langle M\rangle \mid L(M) = \emptyset\}$: האם שפת המכונה ריקה.</li>
<li>$EQ_{TM} = \{\langle M_1, M_2\rangle \mid L(M_1) = L(M_2)\}$ ו-$ALL_{TM} = \{\langle M\rangle \mid L(M) = \Sigma^*\}$.</li>
</ul>
<table>
<thead><tr><th>שפה</th><th>המחלקה</th><th>למה</th></tr></thead>
<tbody>
<tr><td>$A_{TM}$, $H_{TM}$</td><td>$RE \setminus R$</td><td>מריצים ומקבלים כשהריצה מצליחה; אבל אי אפשר להכריע</td></tr>
<tr><td>$\overline{A_{TM}}$, $\overline{H_{TM}}$</td><td>$coRE \setminus R$</td><td>המשלים של $RE \setminus R$</td></tr>
<tr><td>$\overline{E_{TM}}$ (שפה לא ריקה)</td><td>$RE \setminus R$</td><td>הרצה משולבת על כל המילים, מקבלים כשמילה אחת התקבלה</td></tr>
<tr><td>$E_{TM}$</td><td>$coRE \setminus R$</td><td>המשלים של הקודמת</td></tr>
<tr><td>$EQ_{TM}$, $ALL_{TM}$</td><td>אף אחת (לא ב-$RE$ ולא ב-$coRE$)</td><td>צריך גם "קיים" וגם "לכל"</td></tr>
<tr><td>$A_{DFA}$, $A_{CFG}$, ...</td><td>$R$</td><td>הקלט הוא אוטומט או דקדוק, ואפשר תמיד להריץ אותו</td></tr>
</tbody></table>
<div class="lesson-rule">🔑 <strong>כלל אצבע:</strong> אם הקלט הוא <b>אוטומט סופי או דקדוק</b>, כמעט תמיד השפה כריעה (23A-B-Q16). אם הקלט הוא מכונת טיורינג והשאלה על כל השפה שלה, לרוב היא לא כריעה.</div>
<div class="lesson-trap">⚠️ $H_{TM}$ ו-$\overline{A_{TM}}$ הן שפות שונות. $H_{TM}$ מכילה כל זוג שהמכונה <b>עוצרת</b> עליו, ואפילו דוחה. המשלים $\overline{H_{TM}}$ מוכל ב-$\overline{A_{TM}}$ (מי שלא עוצרת בוודאי לא מקבלת), ולא להפך (25B-B-Q5).</div>
<div class="lesson-trap">⚠️ $E_{TM}$ היא "המכונה לא מקבלת אף מילה", לא "דוחה כל קלט" ולא "לא עוצרת על אף קלט". שתי האחרונות הן רק חלק ממנה (22A-B-Q5).</div>
` },
  questions: [
    { id: "D03-Q1", question: "לאיזו מחלקה שייכת השפה $E_{TM} = \\{\\langle M \\rangle \\mid L(M) = \\emptyset\\}$?",
      chk: { kind: "fact", lang: "E_TM", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "לא ב-$RE$ ולא ב-$coRE$"], answer: 2,
      recap: "E_TM ∈ coRE∖R: אפשר להפריך (למצוא מילה מתקבלת) אבל לא לאשר",
      explanation: "המשלים הוא \"קיימת מילה ש-$M$ מקבלת\", ובעזרת הרצה משולבת מקבלים אותה ב-$RE$. לכן $E_{TM} \\in coRE$. היא לא כריעה (נראה זאת ברדוקציות). לא ב-$RE$, כי אז לפי פוסט היא הייתה כריעה." },
    { id: "D03-Q2", question: "לאיזו מחלקה שייכת השפה $\\overline{E_{TM}} = \\{\\langle M \\rangle \\mid L(M) \\ne \\emptyset\\}$?",
      chk: { kind: "fact", lang: "notE_TM", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "לא ב-$RE$ ולא ב-$coRE$"], answer: 1,
      recap: "שפה לא ריקה: מקבלים כשמצאנו מילה מתקבלת (הרצה משולבת)",
      explanation: "בשלב $i$ מריצים את $M$ למשך $i$ צעדים על $i$ המילים הראשונות, ומקבלים כשאחת התקבלה. זה מראה שהשפה ב-$RE$. היא לא ב-$coRE$, כי אז $E_{TM}$ הייתה גם ב-$RE$ ו-$\\overline{E_{TM}}$ הייתה כריעה." },
    { id: "D03-Q3", question: "לאיזו מחלקה שייכת $\\overline{H_{TM}}$, המשלים של בעיית העצירה?",
      chk: { kind: "fact", lang: "coH_TM", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "לא ב-$RE$ ולא ב-$coRE$"], answer: 2,
      recap: "H_TM ∈ RE∖R ולכן המשלים שלה ב-coRE∖R",
      explanation: "$H_{TM}$ ב-$RE$ (מריצים ומקבלים כשהמכונה עוצרת, גם אם דחתה) ואינה כריעה. המשלים של שפה ב-$RE \\setminus R$ הוא ב-$coRE \\setminus R$." },
    { id: "D03-Q4", question: "לאיזו מחלקה שייכת $EQ_{TM} = \\{\\langle M_1, M_2 \\rangle \\mid L(M_1) = L(M_2)\\}$?",
      chk: { kind: "fact", lang: "EQ_TM", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "לא ב-$RE$ ולא ב-$coRE$"], answer: 3,
      recap: "שוויון = הכלה בשני כיוונים = גם \"לכל\" וגם \"קיים\"",
      explanation: "כדי לאשר שוויון צריך לבדוק שכל מילה מתקבלת בשתיהן או בשום אחת: זה \"לכל מילה\" ולכן לא ב-$RE$. כדי להפריך צריך מילה שמתקבלת באחת המכונות ולא בשנייה. כדי לדעת שהשנייה לא תקבל אותה צריך לדעת שהיא לא תעצור או תדחה, ולכן גם המשלים לא ב-$RE$. אף אחת מהמחלקות." },
    { id: "D03-Q5", question: "$A_{DFA}$ היא שפת כל הזוגות $\\langle A, w \\rangle$ שבהם האוטומט הדטרמיניסטי $A$ מקבל את המילה $w$. לאיזו מחלקה היא שייכת?",
      chk: { kind: "fact", lang: "A_DFA", opts: ["R", "RE\\R", "coRE\\R", "none"] },
      options: ["$R$", "$RE \\setminus R$", "$coRE \\setminus R$", "לא ב-$RE$ ולא ב-$coRE$"], answer: 0,
      recap: "קלט שהוא אוטומט: מריצים אותו, הוא תמיד עוצר",
      explanation: "אוטומט סופי קורא את המילה ומסיים אחרי $|w|$ צעדים. לכן מסמלצים אותו וענים. זו שפה כריעה, בניגוד ל-$A_{TM}$ שבה המכונה יכולה לא לעצור." },
    { ref: "25B-B-Q5", recap: "המשלים של H_TM מוכל ממש במשלים של A_TM" },
  ],
});
