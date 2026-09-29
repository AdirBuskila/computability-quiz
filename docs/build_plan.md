# Build plan — Computability & Complexity MCQ Quiz (חישוביות וסיבוכיות)

Phase-0 deliverable. Source of truth + resume point. 6th app in the quiz family.

## Reference apps studied
- **Template = `databases-quiz`** (no `automata-quiz` exists). Data model `{meta, contexts,
  questions}`, shared context blocks via `contextId`, typed options `{id,type,value}`,
  `correctId` + `acceptedIds[]`, `confidence`, `answerSource`, `official`. Per-exam raw JSON →
  `build_questions.py` → `questions.json` + `questions.js`.
- **Rules adopted from `machine-learning-quiz/CLAUDE.md`:**
  - `tools/raw/<CODE>.json` is the source of truth; never hand-edit `questions.js/json`, `learn.js`.
  - Closed topic list, declared in sync in `build_questions.py`, `validate.py`, `app.js`, learn manifest.
  - Answer stored by **option id**, never position; options Fisher–Yates shuffled at render;
    `smoke.js` checks 5000 shuffles never drift the click→id mapping.
  - `lockOrder` when an option cites siblings by letter ("תשובות א ו-ב נכונות").
  - Unique `id`; `questions.js` ≡ `questions.json` (smoke asserts).
  - Duplicates **kept + stamped with `dedupKey`** (full-exam replay intact); `dedupePool()`
    de-dups topic/random pools at runtime.
  - `official: true` only when a real key file (solution / highlighted / מתוקן) keyed it.
    Form-0 inference alone ⇒ `official:false` + "תשובה לא רשמית" badge.
  - `PYTHONUTF8=1`; scripts print ASCII, Hebrew goes to UTF-8 files. Use **`py`** (3.13 has
    PyMuPDF/pdfplumber/python-docx); the default `python` 3.11 lacks them.
  - `?v=N` cache-buster in `index.html`; `dir="ltr"` on any non-Hebrew option text.
- **Math:** KaTeX → **MathML at build time** (`tools/render_math.js`, copied from ML app),
  `dir="ltr"` on every `<math>`, no runtime math lib / fonts / CDN. **Hebrew never inside a
  math span** — split the sentence: Hebrew text, then `$…$` for the notation.

## Architecture
Static, `file://` + GitHub Pages (`.nojekyll`). Runtime: `index.html`, `styles.css`, `app.js`,
`learn.js`, `questions.js`, `images/`, `favicon.svg`. Offline pipeline in `tools/`
(`render_pdf.py`, `crop.py`, `validate.py`, `build_questions.py`, `render_math.js`,
`build_learn.py`, `smoke.js`, `verify_dom.js`, `shoot.js`).

## Data model
`window.CC_QUIZ = { meta, contexts, questions }`
- **questions[]**: `{ id, examCode, examLabel, year, num, topic, topicLabel, question,
  contextId?, options:[{id,type,value}], correctId, acceptedIds?, official, answerSource,
  confidence, explanation, source, dedupKey, lockOrder? }`
  - option `type` ∈ `text | math | image` (text may contain inline `$…$`).
  - Stem / explanation: richText with inline `$…$`, display `$$…$$`, `**bold**`, `` `code` ``;
    all `$…$` pre-rendered to MathML at build.
  - `source` ∈ `exam | sample | moodle | review`.
  - `answerSource` ∈ `solution-pdf | highlighted-pdf | corrected-key | shuffled-key |
    moodle-100 | moodle-summary | form0-inferred`.
- **contexts[id]**: `{kind: image|text, title, image?, caption?, text?}` — TM diagrams,
  reduction figures, shared definitions of languages used by several questions.

## Notation conventions (character-exact)
`\le_m`, `\le_p`, `\not\le_m`, `\mathrm{R}`, `\mathrm{RE}`, `\mathrm{coRE}`, `\mathrm{P}`,
`\mathrm{NP}`, `\mathrm{coNP}`, `\mathrm{NPC}`, `A_{TM}`, `HALT_{TM}`/`H_{TM}` (keep the exam's
own glyph), `E_{TM}`, `EQ_{TM}`, `\overline{L}`, `\langle M\rangle`, `\langle M,w\rangle`,
`\Sigma^*`, `O(n^2)`. A dropped overline or `≤m`↔`≤p` flips the answer → crop as image or ask.

## Answer rules
- Form 0 (`גרסא-0`/`טופס-0`) ⇒ first option correct — **verify per exam against its key
  before relying on it**; report whether it held. (Already observed: 2025 סמ ב מועד א key has
  Q2 = ד, so non-"גרסא-0" papers are NOT form-0.)
- Shuffled (`מעורבב/מעורבל`) ⇒ never positional; answer from its marks or its form-0 sibling
  by content. `מתוקן` keys win. Disagreement ⇒ flag, don't pick. No key ⇒ ASK list.

## Exam codes
`YY[A|B|S]-[A|B|C]` (year, semester א/ב/קיץ, מועד); `SAMP-N` sample exams; `MQ1..MQ4` Moodle
quizzes. Sitting = one code even if several files (form-0, shuffled, solution) exist.

## Milestones
- **M0 — Study + plan.** ✅ this doc.
- **M1 — Inventory + triage** → `docs/format_triage.md`, then STOP for Adir (year cutoff).
- **M2 — Flagship vertical slice** (a 2026/2025 sitting with key) end to end: raw JSON →
  build → app renders → verify. Sign-off.
- **M3 — Scale** with parallel subagents per year batch; dedupe; ask list in `docs/ASK_ADIR.md`.
- **M4 — Learn mode** from `סיכומים/` (per-topic briefs, reduction cheat-sheet, closure table).
- **M5 — Ship + verify**: validate, smoke (5000 shuffles), jsdom verify_dom, mobile screenshots,
  README + CLAUDE.md, counts report.
