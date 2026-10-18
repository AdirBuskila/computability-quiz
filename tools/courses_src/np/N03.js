/* NP course - level 3: coNP and closure of P and NP */
CC_LEVEL("np", {
  id: "N03", order: 3, icon: "🔄", title: "coNP וסגירויות של P ו-NP",
  goal: "להגדיר coNP, לזכור מה סגור למה, ולהפריד בין מה שהוכח, מה שנובע מ-P=NP ומה שפתוח.",
  lesson: { html: `
<p>$coNP = \{ L \mid \overline{L} \in NP \}$. כאן העד הקצר מוכיח שמילה היא <b>לא</b> בשפה. למשל $\overline{SAT}$ ב-$coNP$, ואין עד קצר ידוע לכך שאף השמה לא מספקת.</p>
<table>
<thead><tr><th>פעולה</th><th>$P$</th><th>$NP$</th></tr></thead>
<tbody>
<tr><td>איחוד, חיתוך</td><td>כן</td><td>כן</td></tr>
<tr><td>שרשור, כוכב</td><td>כן</td><td>כן</td></tr>
<tr><td>משלים</td><td>כן</td><td>לא ידוע (שקול ל-$NP = coNP$)</td></tr>
</tbody></table>
<ul>
<li><b>איחוד ב-$NP$:</b> מריצים את $M_1$, ואם קיבלה, מקבלים; אחרת מריצים את $M_2$. <b>שרשור:</b> מנחשים נקודת פיצול (24B-A-Q7, 22A-B-Q13).</li>
<li>$P \subseteq NP \cap coNP$: אם $L \in P$ אז $\overline{L} \in P \subseteq NP$.</li>
<li>$P = NP \Rightarrow NP = coNP$ (כי $P$ סגורה למשלים). ההפך אינו ידוע.</li>
<li>אם $\overline{SAT} \in NP$ אז $NP$ סגורה למשלים ($SAT \in NPC$, ו-$\overline{SAT} \in NP$ נותן שכל שפה ב-$NP$ מתרדדת למשלימה שב-$NP$).</li>
</ul>
<div class="lesson-trap">⚠️ <strong>מה הוכח ומה פתוח.</strong> לא ידוע אם $P = NP$, לא ידוע אם $NP = coNP$, ולא ידוע אם קיימת $L \in NP \cap coNP$ שאינה ב-$P$ (23S-A-Q23). $PRIME$ שייכת ל-$NP \cap coNP$ אבל גם ל-$P$ (AKS), ולכן אינה דוגמה. בשאלה "מה נכון" טענה שדורשת פתרון בעיה פתוחה היא שגויה.</div>
<div class="lesson-rule">🔑 <strong>$P = coNP$ גורר קריסה:</strong> $L \in NP \Rightarrow \overline{L} \in coNP = P \Rightarrow L \in P$. לכן $NP = P$ ו-$\overline{CLIQUE} \in P \subseteq NP$ (22B-A-Q4). וכן $A \in NP$ ו-$B \in P$ נותנים $A \setminus B = A \cap \overline{B} \in NP$, כי $\overline{B} \in P \subseteq NP$.</div>
` },
  questions: [
    { id: "N03-Q1", question: "איזו טענה נכונה?",
      chk: { kind: "rules", opts: ["np.P_compl", "np.NP_compl_proved", "np.NP_not_compl_proved", "np.NP_union_not_concat"] },
      options: ["$P$ סגורה למשלים", "הוכח ש-$NP$ סגורה למשלים", "הוכח ש-$NP$ אינה סגורה למשלים", "$NP$ סגורה לאיחוד אבל לא לשרשור"], answer: 0,
      recap: "P סגורה למשלים; לגבי NP זו בעיה פתוחה",
      explanation: "מחליפים $q_{acc}$ ו-$q_{rej}$ במכונה דטרמיניסטית פולינומית ומקבלים משלים. עבור $NP$ אף כיוון לא הוכח (זה שקול ל-$NP = coNP$). ו-$NP$ סגורה גם לשרשור, בניחוש נקודת הפיצול." },
    { id: "N03-Q2", question: "נניח $P = NP$. מה בהכרח נובע?",
      chk: { kind: "rules", opts: ["np.P_eq_NP_gives_NP_eq_coNP", "np.P_eq_NP_gives_P_ne_coNP", "np.P_eq_NP_gives_NPcoNP_ne_P", "np.P_eq_NP_gives_CLIQUE_notP"] },
      options: ["$NP = coNP$", "$P \\ne coNP$", "$NP \\cap coNP \\ne P$", "$CLIQUE \\notin P$"], answer: 0,
      recap: "P = NP ⟹ NP = coNP, כי P סגורה למשלים",
      explanation: "אם $L \\in NP = P$ אז $\\overline{L} \\in P = NP$, ולכן $\\overline{L} \\in NP$ ו-$L \\in coNP$. מכאן $NP \\subseteq coNP$ ובסימטריה השוויון. שאר התשובות נוגדות את ההנחה: תחת $P = NP$ גם $CLIQUE \\in P$ ו-$NP \\cap coNP = P$." },
    { id: "N03-Q3", question: "איזו טענה נכונה?",
      chk: { kind: "rules", opts: ["np.P_sub_NPcoNP", "np.proved_NPcoNP_sub_P", "np.proved_NP_sub_coNP", "np.proved_P_eq_NP"] },
      options: ["$P \\subseteq NP \\cap coNP$", "הוכח ש-$NP \\cap coNP \\subseteq P$", "הוכח ש-$NP \\subseteq coNP$", "הוכח ש-$P = NP$"], answer: 0,
      recap: "P ⊆ NP ∩ coNP; ההפך פתוח",
      explanation: "שפה ב-$P$ ב-$NP$, והמשלים שלה גם ב-$P \\subseteq NP$, כלומר היא ב-$coNP$. שלוש האחרות פתוחות. לא הוכחו ולא הופרכו." },
    { id: "N03-Q4", question: "מה נכון לגבי שפות ב-$NP \\cap coNP$ שאינן ב-$P$?",
      chk: { kind: "rules", opts: ["np.open_NPcoNP_notP", "np.SAT_in_NPcoNP_notP", "np.PRIME_example", "np.proved_no_NPcoNP_notP"] },
      options: ["לא ידוע אם קיימת שפה כזו", "$SAT$ היא דוגמה כזו", "$PRIME$ היא דוגמה כזו", "הוכח שאין שפה כזו"], answer: 0,
      recap: "NP∩coNP∖P: שאלה פתוחה; PRIME ב-P",
      explanation: "$PRIME$ ב-$NP \\cap coNP$ אבל גם ב-$P$ (AKS), ולכן אינה דוגמה. $SAT$ ב-$coNP$ רק אם $NP = coNP$, שלא ידוע. ואין הוכחה שאין שפה כזו." },
    { id: "N03-Q5", question: "נתון ש-$\\overline{SAT} \\in NP$. מה בהכרח נובע?",
      chk: { kind: "rules", opts: ["np.coSAT_in_NP_gives_NP_eq_coNP", "np.coSAT_in_NP_gives_SAT_in_P", "np.coSAT_in_NP_gives_P_eq_NP", "np.coSAT_in_NP_gives_SAT_notNP"] },
      options: ["$NP$ סגורה למשלים", "$SAT \\in P$", "$P = NP$", "$SAT \\notin NP$"], answer: 0,
      recap: "SAT̄ ∈ NP ⟹ NP = coNP",
      explanation: "כל $L \\in NP$ מתרדדת ל-$SAT$, ולכן $\\overline{L} \\le_p \\overline{SAT} \\in NP$, כלומר $\\overline{L} \\in NP$. אין מכאן $P = NP$, ו-$SAT \\in NP$ מתקיים תמיד." },
    { ref: "20A-A-Q22", recap: "A ∈ NP ו-B ∈ P ⟹ A∖B ∈ NP" },
  ],
});
