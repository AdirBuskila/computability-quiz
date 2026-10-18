/* NP course - level 7: what P = NP and NP-completeness imply */
CC_LEVEL("np", {
  id: "N07", order: 7, icon: "🎯", title: "מה גורר P = NP ומה גוררת NP-שלמות",
  goal: "להסיק נכון מהנחות כמו \"L ב-NPC ב-P\", \"SAT ≤p PATH\" או \"אם P = NP\", ולזהות מה אינו נובע.",
  lesson: { html: `
<p>שאלות "מה נובע" נפתרות בכמה משפטים קבועים:</p>
<ul>
<li>$P \cap NPC \ne \emptyset \iff P = NP$. שפה $NP$-שלמה אחת ב-$P$ מספיקה. ולהפך, $P \ne NP$ אם ורק אם $P$ ו-$NPC$ זרות.</li>
<li>$P \ne NP \iff CLIQUE \notin P$, כי $CLIQUE \in NPC$.</li>
<li>אם $B \in NPC$, $B \le_p A$ ו-$A \in P$ אז $P = NP$ (22B-A-Q19). אם $L \in NPC$ ו-$\overline{L} \notin P$ אז $P \ne NP$ (26B-B-Q10).</li>
<li>$NPC \cap coNP \ne \emptyset \iff NP = coNP$.</li>
<li>אם $P = NP$ אז <b>כל שפה לא טריוויאלית ב-$P$ היא $NP$-שלמה</b>, גם שפה סופית וגם $PATH$ (25B-A-Q10). כי כל שתי שפות לא טריוויאליות ב-$NP$ מתרדדות זו לזו.</li>
</ul>
<div class="lesson-trap">⚠️ <strong>$\emptyset$ ו-$\Sigma^*$ לעולם אינן $NP$-שלמות.</strong> אין רדוקציה משפה לא טריוויאלית אליהן. לכן תמיד כותבים "לא טריוויאלית".</div>
<div class="lesson-rule">🔑 <strong>רדוקציה אל שפה קלה מכריעה את $SAT$:</strong> $SAT \le_p A$ ו-$A \in P$ נותן $SAT \in P$, ולכן $P = NP$. אפילו אם רק מצליחים להראות $SAT \le_p PATH$, נקבל $P = NP$ וגם $NP = coNP$ (25B-A-Q9).</div>
<div class="lesson-trap">⚠️ <strong>"מציאת אלגוריתם פולינומי לשפה ב-$NP$" אינה $P = NP$</strong> אלא אם השפה $NP$-שלמה. ($PATH \in NP$ ויש לה אלגוריתם פולינומי.) ו"$NPC$ היא הכי קשה בעולם" שגוי: כל שפה $NP$-שלמה כריעה, והיא קלה בהרבה מ-$ALL_{TM}$.</div>
` },
  questions: [
    { id: "N07-Q1", question: "נתון שקיימת שפה $L \\in NPC$ שגם $L \\in P$. מה נובע?",
      chk: { kind: "rules", opts: ["np2.P_eq_NP", "np2.P_ne_NP", "np2.NP_ne_coNP", "np2.SAT_notP"] },
      options: ["$P = NP$", "$P \\ne NP$", "$NP \\ne coNP$", "$SAT \\notin P$"], answer: 0,
      recap: "שפה NP-שלמה אחת ב-P גוררת P = NP",
      explanation: "לכל $A \\in NP$ מתקיים $A \\le_p L \\in P$, ולכן $A \\in P$. כלומר $NP \\subseteq P$. הטענה $SAT \\notin P$ נוגדת, כי $SAT \\le_p L$. ו-$NP \\ne coNP$ נוגד, כי $P = NP$ גורר $NP = coNP$." },
    { id: "N07-Q2", question: "נתון $P = NP$. איזו טענה נכונה על $PATH$ (שפה שנמצאת ב-$P$)?",
      chk: { kind: "rules", opts: ["np2.PATH_NPC_if_PNP", "np2.PATH_notNPC", "np2.PATH_NPC_always", "np2.PATH_notNP"] },
      options: ["$PATH$ היא $NP$-שלמה", "$PATH$ אינה $NP$-שלמה", "$PATH$ אינה ב-$NP$", "$PATH$ היא $NP$-שלמה גם אם $P \\ne NP$"], answer: 0,
      recap: "אם P = NP, כל שפה לא טריוויאלית ב-P היא NP-שלמה",
      explanation: "תחת $P = NP$ כל שפה ב-$NP$ מתרדדת ל-$PATH$ (מכריעים אותה בזמן פולינומי ומחזירים מילה קבועה בתוך $PATH$ או מחוץ לה), ו-$PATH \\in NP$. אם $P \\ne NP$ ההפך: $PATH \\in P$, ולכן לא $NP$-שלמה." },
    { id: "N07-Q3", question: "איזו טענה נכונה?",
      chk: { kind: "rules", opts: ["np2.empty_never_NPC", "np2.empty_NPC_if_PNP", "np2.Sigma_NPC_if_PNP", "np2.finite_NPC_always"] },
      options: ["$\\emptyset$ אינה $NP$-שלמה לעולם", "$\\emptyset$ היא $NP$-שלמה אם $P = NP$", "$\\Sigma^*$ היא $NP$-שלמה אם $P = NP$", "כל שפה סופית היא $NP$-שלמה"], answer: 0,
      recap: "∅ ו-Σ* אינן NP-שלמות לעולם",
      explanation: "$SAT \\le_p \\emptyset$ אינה אפשרית: אין לאן למפות את הנוסחאות הספיקות. אותו דבר ל-$\\Sigma^*$ (אין לאן למפות את הלא ספיקות). שפה סופית לא טריוויאלית יכולה להיות $NP$-שלמה רק תחת $P = NP$." },
    { id: "N07-Q4", question: "מראים רדוקציה פולינומית $SAT \\le_p PATH$. מה נובע?",
      chk: { kind: "rules", opts: ["np2.SATtoPATH_PNP", "np2.SATtoPATH_PneNP", "np2.SATtoPATH_PATHnotP", "np2.SATtoPATH_NPnotclosed"] },
      options: ["$P = NP$ (ולכן גם $NP$ סגורה למשלים)", "$P \\ne NP$", "$PATH \\notin P$", "$NP$ אינה סגורה למשלים"], answer: 0,
      recap: "רדוקציה מ-SAT לשפה ב-P מכריעה את SAT",
      explanation: "$PATH \\in P$ ולכן $SAT \\in P$, כלומר $NP = P$. מכיוון ש-$P$ סגורה למשלים, גם $NP = coNP$. השאר נוגדים זאת." },
    { id: "N07-Q5", question: "נתון $L \\in NPC$ וגם $\\overline{L} \\in NP$. מה נובע?",
      chk: { kind: "rules", opts: ["np2.coNP_eq_NP", "np2.L_in_P", "np2.P_eq_NP2", "np2.L_notNP"] },
      options: ["$NP = coNP$", "$L \\in P$", "$P = NP$", "$L \\notin NP$"], answer: 0,
      recap: "NPC ∩ coNP ≠ ∅ ⟹ NP = coNP",
      explanation: "כל $A \\in NP$ מתרדדת ל-$L$, ולכן $\\overline{A} \\le_p \\overline{L} \\in NP$, כלומר $\\overline{A} \\in NP$. מכאן $NP$ סגורה למשלים. אין מכאן $L \\in P$ או $P = NP$ (לא ידוע), ו-$L \\in NP$ מההגדרה." },
    { ref: "26B-B-Q10", recap: "L ∈ NPC ו-L̄ ∉ P ⟹ P ≠ NP" },
  ],
});
