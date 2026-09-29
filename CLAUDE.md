# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

A Hebrew/RTL **Computability & Complexity (חישוביות וסיבוכיות, HIT 61306)** exam trainer — the
6th app in the quiz family (`data-science-quiz`, `software-engineering-quiz`,
`machine-learning-quiz`, `databases-quiz`, …). The shipped site is **100% static**: `index.html`
+ `styles.css` + `app.js` + `questions.js` + `learn.js` + `images/` + `favicon.svg`. No bundler, no
framework, no runtime deps, no CDN; runs from `file://` and GitHub Pages (`.nojekyll`).
Everything under `tools/` is an offline pipeline that *produces* `questions.js` / `learn.js`.

Source material lives outside the repo (read-only):
`C:\Users\Adir\Desktop\BSC\שנה ג\חישוביות וסיבוכיות`.

## Commands

```bash
cd tools && npm install katex jsdom puppeteer-core   # deps are gitignored
PYTHONUTF8=1 py tools/validate.py [CODE]              # lint raw files
PYTHONUTF8=1 py tools/build_questions.py             # raw -> questions.js/json + build_report.md
PYTHONUTF8=1 py tools/build_learn.py                 # docs/briefs/*.md -> learn.js
node tools/smoke.js                                  # integrity + 5000-shuffle id grading + js≡json
node tools/verify_dom.js                             # jsdom boot, practice + exam session, learn refs
node tools/verify_learn.js                           # puppeteer: every chapter at 390px, no overflow
node tools/shoot.js                                  # screenshots 390/1000px, both themes
```

**Use `py` (Python 3.13), not `python`** — only 3.13 has PyMuPDF / pdfplumber / python-docx.
Always `PYTHONUTF8=1` (console is cp1255; scripts print ASCII, Hebrew goes to UTF-8 files).

## Data flow

```
exam PDF --render_pdf.py--> tools/raw/<CODE>/page-NN.png  (look at the pages!)
         (transcribed by hand/agent) --> tools/gen/gen_<CODE>.py --> tools/raw/<CODE>.json  <- SOURCE OF TRUTH
         --build_questions.py--> questions.js + questions.json + tools/build_report.md
docs/briefs/*.md --build_learn.py--> learn.js
```

- **Edit the generator `tools/gen/gen_<CODE>.py`, re-run it** — never hand-edit
  `tools/raw/*.json`, `questions.*` or `learn.js`. Generators use Python raw strings so TeX
  backslashes stay sane.
- Contract: `tools/RAW_SCHEMA.md`. Extraction rules: `tools/EXTRACTION_GUIDE.md`.
- Exam codes `YY[A|B|S]-[A|B|C]` (year of the sitting, semester א/ב/קיץ, מועד) + `SAMP-N`.
- Topics: closed list of 11 keys (tm, decidability, enumerators, undecidability,
  mapping_reductions, closure, classification, time_p, np, poly_reductions, npc) — in sync in
  `build_questions.py` (`TOPIC_LABEL`), `validate.py`, `app.js`, `build_learn.py`.

## Invariants (tests enforce them)

- **Answer by option id, never by position.** Options are Fisher–Yates shuffled at render;
  `lockOrder` (auto-detected when an option cites sibling letters) keeps source order.
- `acceptedIds` = officially accepted double answers (appeals / two highlights); correctId first.
- `official:true` only when a real key file keyed it. `hold:"reason"` keeps a question in raw
  but OUT of the bank (listed in build_report + `docs/ASK_ADIR.md`).
- Unique ids; `questions.js` ≡ `questions.json`; every image path exists.
- Duplicates kept + `dedupKey`; `dedupePool()` de-dups only topic/random pools.
- **Math → MathML at build time** (KaTeX via `tools/render_math.js`), `dir="ltr"` on every
  `<math>`. **No Hebrew inside `$…$`** (build aborts). Hebrew set-builder conditions go on a
  separate `(*): …` line.
- `\overline` is post-processed into `<mrow class="ovl">` (Chrome draws KaTeX's `<mover>` bar as
  a stub on the corner — a complement that renders wrong flips the answer).

## Lessons learned (read before extracting more exams)

- **"גרסא-0 / טופס-0" does NOT mean "first option is correct" in this course.** Checked against
  real keys: failed for 2020, 2022, 23A-A, 23A-B; held only for 23B-A and 23S-A. Keys come from
  highlights / letter tables / worked solutions only. Form-0-only sittings (24B-B, 24S-A) stay out.
- Solution files mark answers with **yellow highlight** + blue proof boxes (→ `explanation`).
  Some solution files reorder options vs. the exam (25B-A Q17) — match the key **by content**.
- Text layers drop overlines (sometimes they appear as combining ̅ after the token) and scramble
  bidi order. Trust the rendered image; zoom doubtful tokens at 5× (PyMuPDF `clip`).
- `חומרים אחרים/` filenames are mojibake: `name.encode('cp437').decode('cp862')`.
- Student "web-shuffler" retypes (`2024-07-08…no-sol`, `2024 קיץ/מבחן מעורבב`,
  `2023-02-09…no-sol`) lost overlines and carry fake keys — ignore them.
- Official keys are sometimes mathematically wrong (23A-B Q9, 22B-A Q13): flag with
  `hold` / `confidence:"med"` + ASK_ADIR, never silently "fix" the answer.
- Parallel extraction agents must use unique temp-file names (one overwrote another's script).
- Rice's theorem and space complexity are not taught in this course — no topics for them.

## Docs
`docs/build_plan.md` (plan/milestones) · `docs/format_triage.md` (every source file → sitting,
key, status) · `docs/triage/batch*.md` (per-file detail) · `docs/ASK_ADIR.md` (open questions) ·
`docs/pipeline.md` · `tools/build_report.md` (generated counts).
