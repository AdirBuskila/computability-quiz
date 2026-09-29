# Triage agent brief (Phase 1 — LOOK, don't extract)

App dir: C:\Users\Adir\Desktop\Coding\Dev\computability-quiz
Source:  C:\Users\Adir\Desktop\BSC\שנה ג\חישוביות וסיבוכיות   (READ-ONLY — never rename/move/modify anything there)

Course: Computability & Complexity (Hebrew, HIT). Exams are mostly multiple-choice (א-ד / א-ה).
Solution files typically show the correct option **highlighted in yellow** plus blue proof boxes.

## Tools
- Use `py` (Python 3.13 with PyMuPDF/pdfplumber/python-docx/Pillow), always with `PYTHONUTF8=1`.
  The default `python` lacks these libs.
- Render: `PYTHONUTF8=1 py tools/render_pdf.py "<pdf>" <OUTNAME> --dpi 200 [--pages 1-4]`
  (run from the app dir) → tools/raw/<OUTNAME>/page-NN.png. Then VIEW pages with the Read tool.
  Use OUTNAME = sitting code + suffix, e.g. `25B-A` (exam), `25B-A-SOL` (solution), `24B-B-SHUF`,
  `24B-B-F0`, `MQ2-100b`… so renders are reusable for extraction later.
- Text layer: `PYTHONUTF8=1 py -c "import fitz;d=fitz.open(r'<pdf>');print(d[1].get_text())"` —
  helpful for speed, but math glyphs/overlines are often lost: trust the IMAGE.
- `חומרים אחרים/` filenames are mojibake (CP862 bytes shown as CP437). Get real paths with
  `os.listdir` and decode with `name.encode('cp437').decode('cp862')` to know what each is.
  In your report, cite decoded names.
- docx: `py -c "import docx; ..."` (text + inline images via doc.inline_shapes / zip `word/media`).
- Images (jpg/png): view directly with Read.

## For EVERY file in your batch, record
1. path (decoded) · sitting code `YY[A|B|S]-[A|B|C]` (year of exam date; semester א=A ב=B קיץ=S;
   מועד א/ב/ג=A/B/C) · exam date printed on the cover.
2. format: text-PDF / scan / image / docx; page count.
3. question style: MCQ / open-ended / mixed; # questions; # options per question (א-ד? א-ה?);
   any questions with figures (TM diagrams etc.), any "תשובות א ו-ב נכונות"-style options.
4. version: form-0 (גרסא-0/טופס-0) / shuffled (מעורבב/מעורבל) / unknown. Is there a form/version
   number printed on the cover?
5. answer source: highlighted / circled / worked solution / letter table / none. Is it clear?
6. **Answer key**: for every question whose correct answer is visibly marked, the letter
   (e.g. `1א 2ד 3א …`). Say which are unclear.
7. **Form-0 check** (only for form-0 files that have a key, or form-0 + separate solution):
   does the correct answer = the FIRST option for every question? List exceptions exactly.
8. duplicates / siblings: which other files are the same sitting (same questions)? For
   shuffled copies, spot-check 3 questions: same stems? options permuted? do the keys agree
   by CONTENT?
9. anything odd: missing pages, cut-off text, unreadable scans, notation you couldn't read
   (overlines, ≤m vs ≤p), corrections ("מתוקן", appeal notes), handwriting.

## Rules
- Look at the rendered pages yourself — at least the cover, 2 question pages, and every
  answer-marked page needed for the key. For solution files, read ALL question pages (needed
  for the key).
- Never guess. Unclear ⇒ say "unclear" with page number.
- Don't write JSON; don't build anything. Only write your report file (path given in your task)
  and renders under tools/raw/.
- Report file: Markdown, one `###` section per file (or per sitting grouping its files), then a
  short "Batch summary" table: code | files | #Q | MCQ? | key source | form-0 held? | notes.
- Your final message: a concise summary (≤25 lines) of the batch + open questions for Adir.
