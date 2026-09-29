# Pipeline & tests

```
tools/raw/<CODE>.json  (contract: tools/RAW_SCHEMA.md; files starting "_" are skipped)
   --validate.py-------->  lint (exit 1 on any problem)
   --build_questions.py->  questions.json + questions.js (window.CC_QUIZ) + tools/build_report.md
                           math: every $…$ / $$…$$ / type:"math" option -> ONE node call to
                           tools/render_math.js (KaTeX -> MathML, dir="ltr"); any KaTeX error or
                           Hebrew inside math aborts the build and writes nothing.
```

```bash
cd tools && npm install katex jsdom puppeteer-core     # once (deps are gitignored)
PYTHONUTF8=1 py tools/validate.py [CODE]
PYTHONUTF8=1 py tools/build_questions.py
node tools/smoke.js        # ids, correctId/acceptedIds, images, js==json, 5000-shuffle id grading
node tools/verify_dom.js   # jsdom: practice + full-exam session, <math dir=ltr>, no JS errors
                           # APP_ROOT=<dir> runs it against a copy (e.g. an empty bank)
node tools/shoot.js        # Chrome screenshots 390px + 1000px, dark + light -> tools/raw/shots/
                           # EXAM=<code> MAX_Q=<n>; fails on horizontal overflow or page errors
```

Build-time details worth knowing:
- `\overline{…}`: KaTeX emits `<mover>` + stretchy U+203E, which Chrome draws as a stub on the
  base's corner. `build_questions.py` rewrites it to `<mrow class="ovl">`; `styles.css` draws
  the bar as a border-top across the whole base.
- `lockOrder` is auto-set when a text option cites sibling letters ("תשובות א ו-ב", "א' ו-ג'",
  "רק ב,ג", "תשובה ג"). "כל התשובות האחרות" does not lock. Raw `lockOrder:false` overrides.
- `dedupKey` = sha1(normalized stem + sorted normalized option values)[:16]. Duplicates are kept;
  `app.js dedupePool()` de-dups topic/random pools only; full-exam mode replays every copy.
- Extra derived fields beyond RAW_SCHEMA: context `captionHtml` / `titleHtml`, `meta.exams`,
  `meta.topics`.

## Learn mode

```
docs/briefs/NN - <title>.md  --build_learn.py-->  learn.js  (window.LEARN = {chapters:[{id,title,topic,kind,html}], meta})
```

```bash
PYTHONUTF8=1 py tools/build_learn.py   # after build_questions.py whenever the bank changes
node tools/verify_dom.js               # also checks learn: dangling qrefs FAIL, 0-question topic WARNs
node tools/verify_learn.js             # Chrome: every chapter at 390px (dark+light) + 1000px;
                                       # fails on horizontal overflow / content sticking out of the card
                                       # shots -> tools/raw/shots/learn-*.png  (SHOTS=0 to skip, FULL=1 full page)
```

- `MANIFEST` in `build_learn.py` maps file -> chapter id -> topic key -> kind (`topic` | `cheat`).
  Every topic in the closed list needs one `topic` brief; `cheat` chapters (דף עזר) only use the
  topic for the drill button.
- Math: same KaTeX->MathML path as the questions (one `render_math.js` call), same `fix_overlines`.
  Hebrew inside `$…$` or a KaTeX error fails the build and writes nothing.
- `` `26B-B-Q3` `` (a question id in backticks) -> `.qref` button that opens the question peek
  (source option order, accepted answer marked, explanation). An id not in `questions.json`
  fails the build. `[[chapter_id]]` / `[[chapter_id|label]]` -> `.xref` in-app link.
- Each `topic` chapter gets an auto-appended "שאלות מבחן בנושא" list built from `questions.json`
  (grouped by exam, newest first) — it stays current on every rebuild.
- Callouts: a blockquote whose first line starts with 🔑 💡 🪤 ⚠️ 🚨 ✅ ❌ gets a `cal-*` colour.
- `app.js initLearn`: TOC (drawer on mobile), chapter view with "תרגל נושא זה" (`startTopicPractice`),
  `.qref` peek (`#qpeek`), `.xref` jumps, `markScrollable()` edge shadows on overflowing
  tables/formulas. Deep links: `index.html?learn=<chapterId>`, `index.html?practice=<topic>`.
- The course does not teach Rice's theorem or space complexity — keep them out of the briefs.
