/* Mapping reductions course - level 7: boss */
CC_LEVEL("map", {
  id: "M07", order: 7, icon: "🏆", title: "מבחן גמר: רדוקציות מיפוי", boss: true,
  goal: "שש שאלות אמיתיות מהמבחנים על כיוון הרדוקציה, מה היא מוכיחה ובניית הפונקציה.",
  lesson: { html: `
<p>סיכום לפני שאלות האמת:</p>
<ul>
<li><b>הגדרה:</b> $f$ חשיבה על כל קלט, ו-$x \in A \iff f(x) \in B$. בודקים שני כיוונים בנפרד.</li>
<li><b>זרימה:</b> קלות זורמת מ-$B$ אל $A$ ($B \in R/RE/coRE \Rightarrow$ אותו דבר ל-$A$), קושי זורם מ-$A$ אל $B$. ההפך אינו נכון.</li>
<li><b>משלימים:</b> $A \le_m B \iff \overline{A} \le_m \overline{B}$ באותה $f$. $x \in A \iff f(x) \notin B$ הוא $A \le_m \overline{B}$.</li>
<li><b>הוכחת קושי:</b> מרדדים משפה קשה אל השפה החדשה: $A_{TM} \le_m L$ נותן $L \notin R$ ו-$L \notin coRE$; $\overline{A_{TM}} \le_m L$ נותן $L \notin RE$.</li>
<li><b>רדוקציה שלא קיימת:</b> לא מרדדים שפה שאינה ב-$RE$ אל שפה ב-$RE$; אין רדוקציה בין $RE \setminus R$ ל-$coRE \setminus R$.</li>
<li><b>בנייה:</b> $K_{M,w}$ (התעלם מהקלט, הרץ, קבל) נותנת $\Sigma^*$ או $\emptyset$; מילים בטוחות קודם לשפות מסוימות.</li>
<li><b>טריוויאליות:</b> $A \le_m \emptyset$ רק אם $A = \emptyset$; כל שפה כריעה לא טריוויאלית מתרדדת לכל שפה לא טריוויאלית; $\le_m$ טרנזיטיבי, לא סימטרי.</li>
</ul>
<div class="lesson-rule">🔑 לפני שמוכיחים כלום, שאלו: מי המקור ומי היעד? ומה אני יודע על כל אחד מהם?</div>
` },
  questions: [
    { ref: "22A-A-Q9", recap: "שפה כריעה מתרדדת ל-A_TM; שפה לא כריעה לא חייבת להתרדד בשני הכיוונים" },
    { ref: "23A-B-Q12", recap: "בין שפות לא טריוויאליות: B ∈ RE∩coRE נותן A ∈ RE∩coRE" },
    { ref: "24B-A-Q1", recap: "שתי שפות שמתרדדות זו לזו אינן בהכרח כריעות" },
    { ref: "24B-A-Q8", recap: "x ∈ L₁ ⟺ f(x) ∉ L₂ הוא רדוקציה למשלים" },
    { ref: "25B-B-Q8", recap: "ALL_TM ≤m EQ_TM: משווים למכונה שמקבלת הכול" },
    { ref: "26B-A-Q13", recap: "A ≤m B ⟺ משלים A ≤m משלים B" },
  ],
});
