/* NP course - level 5: the classical reductions (machine-checked by building the graphs) */
CC_LEVEL("np", {
  id: "N05", order: 5, icon: "🧱", title: "הרדוקציות הקלאסיות: 3SAT, CLIQUE, IS ו-VC",
  goal: "לדעת לבנות את הגרף של כל רדוקציה קלאסית, לחשב את הפרמטרים שלה ולהסביר למה היא שומרת על התשובה.",
  lesson: { html: `
<table>
<thead><tr><th>רדוקציה</th><th>הפונקציה</th></tr></thead>
<tbody>
<tr><td>$CLIQUE \le_p IS$ וגם $IS \le_p CLIQUE$</td><td>$\langle G, k \rangle \mapsto \langle \overline{G}, k \rangle$: גרף משלים, אותו $k$</td></tr>
<tr><td>$IS \le_p VC$</td><td>$\langle G, k \rangle \mapsto \langle G, n - k \rangle$: המשלים של קבוצה בלתי תלויה הוא כיסוי</td></tr>
<tr><td>$3SAT \le_p IS$</td><td>קודקוד לכל מופע של ליטרל, $k = $ מספר הפסוקיות</td></tr>
<tr><td>$3SAT \le_p CLIQUE$</td><td>אותם קודקודים, אותו $k$, צלעות משלימות</td></tr>
</tbody></table>
<h3>3SAT אל IS</h3>
<p>בגרף $G_\varphi$ יש קודקוד לכל <b>מופע</b> של ליטרל בכל פסוקית. מחברים בצלע:</p>
<ul>
<li>כל שני קודקודים <b>באותה פסוקית</b> (משולש), כדי לבחור לכל היותר ליטרל אחד מכל פסוקית;</li>
<li>כל זוג ליטרלים <b>סותרים</b> ($x$ ו-$\lnot x$) בפסוקיות שונות, כדי לא לבחור את שניהם.</li>
</ul>
<p>קבוצה בלתי תלויה בגודל $m$ (מספר הפסוקיות) בוחרת ליטרל אחד מכל פסוקית בלי סתירה, כלומר השמה מספקת. ולהפך: השמה מספקת נותנת ליטרל אמת אחד מכל פסוקית. לכן $\varphi \in 3SAT \iff \langle G_\varphi, m \rangle \in IS$. שימו לב ש-$k = m$, לא מספר המשתנים (23S-A-Q20).</p>
<p>ב-$3SAT \le_p CLIQUE$ מחברים בצלע ליטרלים משתי פסוקיות <b>שונות</b> שאינם סותרים; קליקה בגודל $m$ היא בחירה עקבית של ליטרל מכל פסוקית.</p>
<div class="lesson-rule">🔑 <strong>$\overline{G}$ הוא גרף משלים:</strong> אותם קודקודים, וצלע בדיוק היכן שלא הייתה צלע. קליקה ב-$G$ היא קבוצה בלתי תלויה ב-$\overline{G}$ (25B-A-Q15).</div>
<div class="lesson-trap">⚠️ <strong>המרת $k$.</strong> $IS \to VC$ משנה את $k$ ל-$n - k$, אבל $CLIQUE \leftrightarrow IS$ משאירה אותו. טעות בפרמטר שוברת את ה"אם ורק אם". וצריך תמיד לוודא שהבנייה פולינומית, למשל שלא מחשבים את הקליקה עצמה כדי לבנות את הגרף (25S-B-Q15).</div>
` },
  questions: [
    { id: "N05-Q1", question: "איזו פונקציה היא רדוקציה פולינומית $CLIQUE \\le_p IS$? ($n$ = מספר הקודקודים של $G$)",
      chk: { kind: "graph-red", from: "CLIQUE", to: "IS", opts: ["comp(G),k", "G,k", "G,n-k", "comp(G),n-k"] },
      options: ["$\\langle \\overline{G}, k \\rangle$", "$\\langle G, k \\rangle$", "$\\langle G, n-k \\rangle$", "$\\langle \\overline{G}, n-k \\rangle$"], answer: 0,
      recap: "קליקה ב-G = קבוצה בלתי תלויה ב-G המשלים",
      explanation: "קבוצה שכל הזוגות בה מחוברים ב-$G$ הם זוגות שאינם מחוברים ב-$\\overline{G}$, כלומר קבוצה בלתי תלויה, באותו גודל. לכן $k$ לא משתנה. בלי משלים (הפונקציה $\\langle G, k \\rangle$), הקליקה אינה בלתי תלויה; ו-$n-k$ שייך ל-$VC$." },
    { id: "N05-Q2", question: "איזו פונקציה היא רדוקציה פולינומית $IS \\le_p VC$?",
      chk: { kind: "graph-red", from: "IS", to: "VC", opts: ["G,n-k", "G,k", "comp(G),k", "comp(G),n-k"] },
      options: ["$\\langle G, n-k \\rangle$", "$\\langle G, k \\rangle$", "$\\langle \\overline{G}, k \\rangle$", "$\\langle \\overline{G}, n-k \\rangle$"], answer: 0,
      recap: "S בלתי תלויה ⟺ המשלים של S כיסוי קודקודים",
      explanation: "בקבוצה בלתי תלויה $S$ אין צלע בתוך $S$, ולכן כל צלע נוגעת בקודקוד מחוץ ל-$S$: המשלים של $S$ הוא כיסוי בגודל $n-|S|$. ולהפך. אותו גרף, והפרמטר $n - k$." },
    { id: "N05-Q3", question: "בונים את הגרף $G_\\varphi$ של הרדוקציה $3SAT \\le_p IS$ עבור $\\varphi = (x_1 \\lor x_2 \\lor x_3) \\land (\\lnot x_1 \\lor x_2 \\lor \\lnot x_3) \\land (\\lnot x_2 \\lor x_3 \\lor x_1)$. כמה צלעות יש ב-$G_\\varphi$?",
      chk: { kind: "sat-graph", phi: [[1, 2, 3], [-1, 2, -3], [-2, 3, 1]], ask: "IS-edges", opts: ["9", "12", "15", "18"] },
      options: ["9", "12", "15", "18"], answer: 2,
      recap: "משולש לכל פסוקית (3 צלעות) + צלע לכל זוג ליטרלים סותרים בפסוקיות שונות",
      explanation: "בכל פסוקית משולש: 3 צלעות, ובשלוש פסוקיות 9. עוד צלע לכל זוג ליטרלים סותרים בפסוקיות שונות: $x_1$ מופיע בפסוקיות 1 ו-3 ו-$\lnot x_1$ בפסוקית 2 (2 זוגות); $x_2$ בפסוקיות 1 ו-2 ו-$\lnot x_2$ בפסוקית 3 (2 זוגות); $x_3$ בפסוקיות 1 ו-3 ו-$\lnot x_3$ בפסוקית 2 (2 זוגות). סך הכול 6 צלעות סתירה, ובסה\"כ $9 + 6 = 15$." },
    { id: "N05-Q4", question: "עבור אותה $\\varphi$, כמה צלעות יש בגרף של הרדוקציה $3SAT \\le_p CLIQUE$ (מחברים ליטרלים מפסוקיות שונות שאינם סותרים)?",
      chk: { kind: "sat-graph", phi: [[1, 2, 3], [-1, 2, -3], [-2, 3, 1]], ask: "CLIQUE-edges", opts: ["15", "21", "27", "36"] },
      options: ["15", "21", "27", "36"], answer: 1,
      recap: "זוגות בין פסוקיות שונות (27) פחות זוגות סותרים (6)",
      explanation: "בין פסוקיות שונות יש $3 \\cdot 3 \\cdot 3 = 27$ זוגות קודקודים. מהם 6 זוגות סותרים אינם מחוברים. נשארות $27 - 6 = 21$ צלעות. הספירה 36 היא כל הזוגות ($\\binom{9}{2}$), כולל זוגות באותה פסוקית." },
    { id: "N05-Q5", question: "$\\varphi' = (x_1 \\lor x_2) \\land (x_1 \\lor \\lnot x_2) \\land (\\lnot x_1 \\lor x_2) \\land (\\lnot x_1 \\lor \\lnot x_2)$ אינה ספיקה. מהו גודל הקבוצה הבלתי תלויה הגדולה ביותר בגרף של הרדוקציה $\\varphi' \\mapsto G_{\\varphi'}$ (עם ליטרל אחד לכל קודקוד, שני ליטרלים בפסוקית)?",
      chk: { kind: "sat-graph", phi: [[1, 2], [1, -2], [-1, 2], [-1, -2]], ask: "IS-max", opts: ["4", "3", "2", "8"] },
      options: ["4", "3", "2", "8"], answer: 1,
      recap: "נוסחה לא ספיקה: אין קבוצה בלתי תלויה בגודל m",
      explanation: "יש 4 פסוקיות ולכן הקבוצה הגדולה ביותר היא לכל היותר 4 (ליטרל אחד מכל פסוקית). 4 תהיה אפשרית רק אם הנוסחה ספיקה. כיוון שהיא לא ספיקה, המקסימום קטן מ-4, ובפועל הוא 3 (חישוב מלא)." },
    { ref: "23S-A-Q20", recap: "בגרף 3SAT→IS הפרמטר k הוא מספר הפסוקיות" },
  ],
});
