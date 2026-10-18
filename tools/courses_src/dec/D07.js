/* Decidability course - level 7: boss */
CC_LEVEL("dec", {
  id: "D07", order: 7, icon: "🏆", title: "מבחן גמר: כריעות, סגירות וסיווג", boss: true,
  goal: "שש שאלות אמיתיות מהמבחנים על הפרש מעורב, סגירויות וסיווג שפות של מכונות.",
  lesson: { html: `
<p>סיכום קצר לפני שאלות האמת:</p>
<ul>
<li><b>הגדרות:</b> $R$ מכריעות, $RE$ מקבלות, $coRE$ משלימים של $RE$. $R = RE \cap coRE$ (פוסט), ולכן אם $L \in RE \setminus R$ אז המשלים שלה אינו ב-$RE$.</li>
<li><b>שפות מוכרות:</b> $A_{TM}, H_{TM}, \overline{E_{TM}}$ ב-$RE \setminus R$; משלימותיהן ו-$E_{TM}$ ב-$coRE \setminus R$; $EQ_{TM}, ALL_{TM}$ באף אחת; קלט שהוא אוטומט ← $R$.</li>
<li><b>סגירות:</b> $R$ לכל הפעולות; $RE$ ו-$coRE$ לאיחוד, חיתוך, שרשור וכוכב; משלים הופך $RE$ ל-$coRE$.</li>
<li><b>הפרש:</b> $A \setminus B = A \cap \overline{B}$. $RE \setminus R \to RE$, $RE \setminus coRE \to RE$, $R \setminus RE \to coRE$, $RE \setminus RE \to$ כלום.</li>
<li><b>סיווג:</b> חסם סופי ← $R$. "קיימת" ו-$|L(M)| \ge k$ ← $RE \setminus R$. "לכל" ו-$|L(M)| \le k$ ← $coRE \setminus R$. שוויון והכלה ← אף אחת.</li>
<li><b>מלכודות:</b> "דוחה" מול "לא מקבלת"; חסם שתלוי ב-$|w|$ עם "לכל"; "בהכרח" מול "יתכן"; הצבת $\emptyset$ ו-$\Sigma^*$.</li>
</ul>
<div class="lesson-rule">🔑 בשאלת "מה בהכרח" נסו קודם להפריך: הציבו $\emptyset$, $\Sigma^*$, $A_{TM}$ ו-$\overline{A_{TM}}$.</div>
` },
  questions: [
    { ref: "24B-A-Q2", recap: "R∖RE ∈ coRE: ההפרש L₁∖L₂ לא בהכרח ב-RE" },
    { ref: "26B-A-Q9", recap: "RE ∖ coRE = RE ∩ RE ∈ RE" },
    { ref: "22A-B-Q2", recap: "\"קיימת מילה\" עם חסם צעדים: מספר מילים סופי, ולכן R" },
    { ref: "23A-A-Q8", recap: "\"M דוחה את w\": אפשר לראות בזמן סופי, RE∖R" },
    { ref: "20A-B-Q7", recap: "\"לכל מילה\" עם חסם שתלוי ב-|w|: coRE∖R" },
    { ref: "26B-B-Q17", recap: "\"M לא עוצרת על אף מילה\": coRE∖R" },
  ],
});
