# חישוביות וסיבוכיות — תרגול מבחנים (Computability & Complexity Quiz)

משחק תרגול (עברית, RTL) לקורס *חישוביות וסיבוכיות* (61306, HIT). שאלות אמריקאיות ממבחני עבר,
משוב מיידי עם הסבר מתוך הפתרון הרשמי, מצב מבחן בזמן קצוב ומצב לימוד. אתר **סטטי לחלוטין**
(HTML+CSS+JS) — נפתח מקומית מ-`file://` או ב-GitHub Pages, ללא שלב בנייה וללא CDN.

**אתר:** https://adirbuskila.github.io/computability-quiz/

## מאפיינים
- **427 שאלות מ-21 מבחנים** (2020–2026 + 3 מבחנים לדוגמה), 400 ייחודיות. **כל התשובות ממחוון
  אמיתי** (סימון צהוב / טבלת תשובות / פתרון מתוקן), לא מ"התשובה הראשונה".
- **הסברים** מתוך תיבות ההוכחה של הפתרון הרשמי (ומשיעור החזרה 2025 למבחן לדוגמה).
- **סימון מתמטי מדויק** — `≤m`/`≤p`, משלים (קו עליון), `⟨M,w⟩`, `A_TM`… מרונדרים מראש ל-MathML
  (KaTeX בזמן בנייה), כך שהאתר לא טוען ספריית מתמטיקה.
- **מצב לימוד 📖:** 13 פרקים — 11 תדריכים לפי נושא + דף עזר "כיוון הרדוקציה" + טבלת סגירות
  R/RE/coRE ומתכון סיווג שפות. כל מזהה שאלה (למשל `26B-B-Q3`) לחיץ ופותח את השאלה, ומכל פרק
  אפשר לקפוץ לתרגול הנושא.
- **תרגול חופשי** או **מבחן מלא** (אקראי או מבחן עבר ספציפי, זמן קצוב, ציון ופירוט לפי נושא).
- 11 נושאים: מ"ט, כריעות וקבלה, אנומרטורים, אי-כריעות, רדוקציות מיפוי, תכונות סגור, סיווג שפות,
  סיבוכיות זמן ו-P, NP ו-coNP, רדוקציות פולינומיות, NP-שלמות.
- **ערבוב התשובות** בכל הצגה, הבדיקה לפי מזהה — "תמיד א" לא עובד.
- תשובות כפולות שהתקבלו בערעור נספרות כנכונות (9 שאלות). מצב בהיר/כהה, מותאם לנייד.

## בנייה מחדש (רק אחרי עריכת `tools/gen/*` או `docs/briefs/*`)
```bash
cd tools && npm install katex jsdom puppeteer-core && cd ..
PYTHONUTF8=1 py tools/gen/gen_<CODE>.py          # generator -> tools/raw/<CODE>.json
PYTHONUTF8=1 py tools/validate.py
PYTHONUTF8=1 py tools/build_questions.py         # -> questions.js/json + tools/build_report.md
PYTHONUTF8=1 py tools/build_learn.py             # docs/briefs -> learn.js
node tools/smoke.js && node tools/verify_dom.js && node tools/verify_learn.js
```

## מבנה
```
index.html · styles.css · app.js · questions.js · learn.js · images/   ← האתר
tools/gen/      ← מחולל לכל מבחן (תמלול ידני מהדפים)   tools/raw/*.json ← מקור האמת
tools/          ← צינור בנייה ובדיקות                   docs/briefs/     ← פרקי מצב הלימוד
docs/           ← build_plan · format_triage · ASK_ADIR (שאלות פתוחות)
```
פירוט: `CLAUDE.md`, `docs/pipeline.md`, `tools/build_report.md`.
