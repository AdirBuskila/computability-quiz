# Batch 6: collections, sample exams, "מבחנים בסיבוכיות" pack

Source root: `C:\Users\Adir\Desktop\BSC\שנה ג\חישוביות וסיבוכיות` (read-only). All names below are decoded.
Renders: `tools/raw/SAMP-1`, `SAMP-2` (collection p170-178), `SAMP-2-SOL`, `SAMP-3-SOL`. The collection was surveyed with low-res contact sheets, not full renders.
Method: I matched every collection page to the other PDFs by text fingerprint, and scanned pages by a visual pixel diff. The "= file X" claims below are exact page matches, not guesses.

---

### 1. `מבחנים/אוסף מבחנים בחישוביות וסיבוכיות.pdf`: table of contents

- 195 pages, text-PDF mixed with image-only pages. It was merged with iLovePDF, modDate 2024-06-28, so it contains nothing later than 24A.
- **The 1254 annotations are all `Ink` strokes in blue pen (0,0.3,0.9) on pages 90-95.** They are a student's handwritten scribbles and circled answers on a copy of 22B-B (24.7.22). They are not official marks.
- There is no PDF outline or bookmarks.

| Pages | Sitting | Content | Exact match elsewhere |
|---|---|---|---|
| 1-9 | **24A-A** 21.3.2024 (Trachtenbrot) | exam, no answers | = `2024/סמסטר א/מועד א.pdf` (9p) |
| 10-21 | 24A-A | solution, yellow highlight + explanations | = `2024/סמסטר א/מועד א 21.3 פתרון.pdf` (12p) |
| 22-30 | **23S-A** 23-8-23 | exam, no answers | = `2023/סמסטר קיץ/23-8-23.pdf` (9p) |
| 31-41 | 23S-A | solution, highlighted | = `2023-08-23-...-גרסא-0 SOLUTION.pdf` (11p) |
| 42-49 | **23B-A** 12/06/2023, Holon "זום" print, **מבחן מס' 000**, code `~RG1-6\|7-9\|...` | exam, form 000, no answers, 8p | **not in per-year files** (see note A) |
| 50-69 | **23A-B** 5.3.2023 (Trachtenbrot) | header says "פתרון" but the **answers and explanations are stripped** (Wondershare watermark): a clean question paper, 20p | same questions as `2023-03-05-...SOLUTION.pdf`, but that file keeps its highlights; no clean paper exists elsewhere |
| 70-77 | **UNIDENTIFIED 2023 Holon sitting**, scan, "מבחן מס' 048", code `~JC1-6\|7-9\|10-12\|13-16\|17-19N\|20-25M/1-6Z/13-18Z` | exam, **pages 1-2 of 10 missing** (cover); Q1-Q25 all present, no key | **NOT found anywhere else**: possible gap-filler (note B) |
| 78-88 | **22B-B** 24-7-22 (Radal Ben-Av) | exam 78-84 + formula sheet 85-88, no answers | = `2022/סמסטר ב/2022-07-24-...no-sol.pdf` (11p) = `חומרים אחרים/מחבנים נוספים/מבחן יולי מועד ב2022.pdf` |
| 89-99 | 22B-B | same pages + **student's blue ink on 90-95** (circled answers, scratch work) | see note C |
| 100 | **22A-A** 7.2.2022 solution, **censored** (answers blacked out, red handwritten option copies, note "לא למחוק את הצנזורה!") | one tall page (2662×11727 pt) | censored copy of `2022-02-07-...SOLUTION.pdf`; also `חומרים אחרים/מבחנים בסיבוכיות.pdf` p2 |
| 101-109 | 23B-A, HIT format, cover says **"סמסטר א' תשפ"ג מועד א'" with no date** (Radal Ben-Av, 25 Q) | exam, no answers | questions identical to p42-49; per-year only has the solution |
| 110-123 | 23B-A | solution, highlighted | = `2023/סמסטר א/2023-06-12-...-גרסא-0 SOLUTION.pdf` (14p) |
| 124-138 | **20A-A** 14.02.2020 | exam + formula sheet + draft pages (image-only) | = `2020-02-14-...moedA.pdf` (15p, pixel-identical) |
| 139-149 | 20A-A | solution, image-only | = `2020-02-14-...גרסא-0 SOLUTION.pdf` (11p, pixel-identical) |
| 150-158 | **20A-B** 11.03.2020 | exam | = `2020-03-11-...moedB.pdf` (9p) |
| 159-169 | 20A-B | solution | = `2020-03-11-...SOLUTION.pdf` (11p) |
| 170-178 | **SAMP-2** question paper (p170 = sample answer-sheet page, 171-178 = Q1-29) | no answers | **not a separate file** anywhere; only the explanations version exists |
| 179-188 | SAMP-2 | "הסברים לפתרון הבחינה לדוגמא" | = `מבחנים לדוגמה/בחינה לדוגמה עם הסברים.pdf` (10p) |
| 189-195 | **SAMP-3** solution ("חלק א משך הזמן שעה פתרון") | worked solution | = `מבחנים לדוגמה/פתרון מבחן לדוגמא.pdf` (7p) |

**Notes**
- **A. 23B-A cover mislabel.** The HIT cover (p101, and per-year solution p1) says "סמסטר א' תשפ"ג מועד א'" with no date. The Holon form-000 print (p42) of the same questions says "תשפ"ג, סמסטר ב, מועד א, 12/06/2023".
  - So the per-year filename `2023-06-12...` is correct, and it is really **23B-A**, even though it sits in the `2023/סמסטר א` folder.
  - Spot-checks of Q1 (A⊆B⊆C, A,C∉RE; options "א. לא נכון / ב. נכון"), Q7 and Q10-12 show that form 000 has the same order as the HIT paper. So the solution's key applies to form 000 directly.
  - The key is not always the first option: in the solution, Q1 = א, Q2 = א, **Q3 = ב**. The full form-0 check is left to the 23B-A batch.
- **B. Exam 048 (p70-77).**
  - It is a scanned, shuffled Holon form with 25 Q. Q17 mentions "|L|=2023", so it is a 2023 sitting. The code prefix `~JC` differs from 23B-A's `~RG`.
  - Most likely it is **23B-B (Holon, summer 2023)** or another 2023 moed that has no per-year file. Adir should confirm.
  - Printed option letters are missing and were hand-written in. The scribbles at Q23-25 on p77 are relabelling or artifacts, not answers. **No key.**
  - Topics: classification ("nice" TM, does not repeat a configuration), mapping reductions (L_d, ALL_TM), relations (HTM), IS∩CLIQUE, misc MCQ, T/F. Q9-Q25 were legible at 80 dpi.
- **C. 22B-B student marks (UNOFFICIAL, pages 90-95).** Circled answers:
  - 1ג 2ב 3? 4ג 5א 6א 7ג 8ב 9א 10ב 11ב 12א 13א 14א 15ד 16ג 17(none) 18ג 19א 20ב
  - Q3: the student crossed out א/ב/ד and wrote "ה. אף תשובה לא נכונה" with a "?". Unclear.
  - These are one student's answers, not a solution. **22B-B still has no official key.**
- **Keys for sittings that lack keys elsewhere:** none. The collection predates 2024B and does not contain 23A-A (9.2.23), 24B-B, 24S, or any 2025/2026 sitting. The 22B-B marks are student marks only.
- **Not in the collection:** 2018, 22A-B, 22A-C, 22B-A, 22B-C, 23A-A, 24A-B/C, and everything from 2024B on.

---

### 2. Sample exams (מבחנים לדוגמה + copies)

There are **three different sample exams**, not one. SAMP-1 and SAMP-3 share several questions.

#### SAMP-1: `מבחנים/מבחנים לדוגמה/ בחינה לדוגמה.pdf` = `חומרים אחרים/מחבנים נוספים/SAMPLE-FINAL.pdf`
- Text-PDF, 9p, Word 365, modDate 2022-01-02. The two files are pixel-identical (md5 differs only in metadata). Also reproduced in `חומרים אחרים/מבחנים בסיבוכיות.pdf` p14-22.
- Cover: "בחינה לדוגמא", 3 h, 25 Q × 4 pts.
- Parts:
  - T/F Q1-6 (Q6 has a third option "ג. תלוי ב-P=NP?")
  - classification Q7-9 (א-ד)
  - relations Q10-12 (א-ד)
  - mapping reduction Q13-16 (כן/לא)
  - ZSAT polynomial reduction Q17-19
  - misc MCQ Q20-23
  - Q24-25
- **No answer marks.**
- Several questions are identical to SAMP-3 questions that have a key:
  - Q13-16 = SAMP-3 part A Q6-9 → **13א 14א 15א 16ב**
  - Q21 = SAMP-3 A-Q2 (SAMP-3 has an extra option "כל התשובות נכונות"; correct by content is "אף תשובה" = SAMP-1 **ד**)
  - Q23 = SAMP-3 A-Q1 → **א**
  - Q24 = SAMP-3 B-Q4 → **א**
  - Q25 = SAMP-3 B-Q3 → **א**
- Q10-12 (A = complement finite, B = L(M) infinite, C = L(M)∈R) are the same sets as SAMP-2 Q10-12 (G3, G2, G1). By content: **10ב (A⊂B), 11ד, 12ג (C⊃A)**. These are derived by content, so verify.
- Q1-9, 17-20 and 22 have no key.

#### SAMP-2: `מבחנים/מבחנים לדוגמה/בחינה לדוגמה עם הסברים.pdf` (10p) + question paper = collection p170-178
- Text-PDF. 29 Q in parts:
  - א: T/F 1-6
  - ב: classification 7-9
  - ג: relations 10-12
  - ד: T/F 13-20 about E_TM/L1/L2 with R_M, T_M
  - ה: VCM reduction 21-24
  - ו: MCQ 25-29
- Option counts vary: Q26 has **6 options (א-ו)**, Q29 has 5 (א-ה); the rest have 2 or 4.
- Answer source: yellow highlight + red explanations. Clear.
- **Key:**
  - 1א 2א 3ב 4א 5ב 6א
  - 7א 8ד 9א
  - 10ד 11ג 12ג
  - 13א 14ב 15א 16ב 17א 18ב 19ב 20ב (א=נכון, ב=לא נכון, checked on p175)
  - 21ב 22ב 23ב 24א (answers written as "לא נכון"/"נכון"; assumes the same א=נכון order)
  - 25ד 26ד 27ב 28ב 29ד
- **Odd:** Q24 has a green note: "הערה: אם ב-G יש רק k−1 קדקודים אז זה לא נכון... האם לשנות את התשובה ???". The author doubts the answer, so flag Q24.
- The question-paper pages 174 and 176 are text-identical to the explanation pages. The other pages differ only by the added explanations.

#### SAMP-3: `מבחנים/מבחנים לדוגמה/פתרון מבחן לדוגמא.pdf`
- Copies: `חומרים אחרים/בחינה לדוגמא פתרון.pdf`, `חומרים אחרים/מחבנים נוספים/בחינה לדוגמא פתרון.pdf`, `מבחנים בסיבוכיות.pdf` p23-29, collection p189-195.
- All copies are pixel-identical. Word 2016, modDate 2021-01-27.
- Solution only (the question paper is embedded), 7p. The format is two one-hour parts (the 2021-era format), and **numbering restarts in part B**.
- Part A, 9 Q: misc 1-2 (א-ד / א-ה), relations 3-5 (א-ה / א-ד), mapping 6-9 (כן/לא).
- Part B: misc 1-4, then Q5 = DOUBLE-CLIQUE with **7 true/false sub-claims א-ז**.
- Answer source: cyan highlight + blue explanations. Clear.
- **Key:**
  - A: 1א 2ה 3ה 4ד 5ג 6א 7א 8א 9ב
  - B: 1א 2א 3א 4א
  - B5 sub-claims: א-לא ב-לא ג-לא **ד-כן** ה-לא ו-לא ז-לא
- Outside this batch: `מצגות חזרה למבחן/ פתרון מבחן לדוגמא תשפ אלישבע סמסטר ב 2025.pdf` looks like a fourth sample. I did not check it.

**Do the keys agree?** The only content overlap is SAMP-1 ↔ SAMP-3, and SAMP-1 has no key of its own, so there is nothing to conflict. The SAMP-2 relations answers are consistent with the SAMP-1 content derivation above.

---

### 3. `חומרים אחרים/מבחנים בסיבוכיות.pdf` (29p) and `פתרונות למבחנים בסיבוכיות.pdf` (25p, + "(1)" copy)

- The name is misleading: this is **not complexity-only**. "סיבוכיות" is just the course name. These are two self-made study packs (PassportPDF, 2023-02-08). One is an "exams" pack with answers censored; the other is the matching "solutions" pack.
- The "(1)" copy has a different md5 (and 1 annotation) but the same producer and timestamp. It is treated as a duplicate; I did not diff it page by page.

**מבחנים בסיבוכיות.pdf**

| Pages | Content |
|---|---|
| 1 | 22A-C 2.5.2022 solution, **censored**, one tall Google-Docs-style page ("פאשלה עם קביעת תבנית... דפדף הרבה למטה") |
| 2-3 | 22A-A 7.2.2022 solution, censored (same page twice; = collection p100) |
| 4 | **22A-B 9/3/2022** solution, censored (tall page; answer and explanation boxes greyed out) |
| 5-8 | 18A-A 05.02.18 exam + formula sheet (open-ended, "הוכח או הפרך") |
| 9-13 | 18A-B 12/03/2018 exam + formula sheet (open-ended) |
| 14-22 | SAMP-1 |
| 23-29 | SAMP-3 (with solution, so it is not censored here) |

**פתרונות למבחנים בסיבוכיות.pdf**

| Pages | Content |
|---|---|
| 1 | 22A-C 2.5.2022 solution, **uncensored** |
| 2-3 | 22A-A 7.2.2022 solution, uncensored (twice) |
| 4 | 22A-B 9.3.2022 solution, uncensored (red answers + blue explanations) |
| 5-14 | 22B-A 22-6-22 exam + formula sheet. The cover p5 has an **answer letter table 1-20**, identical to the cover of per-year `2022-06-22-...SOLUTION.pdf` p1 |
| 15-25 | 20A-A 14.02.2020 solution (image-only; = per-year SOLUTION = collection p139-149) |

- 22B-A table: 1ג 2ג 3א 4א 5ג 6ד 7ג 8א 9ד 10ג 11ד 12א 13א 14ב 15ד 16ג 17א 18ד 19א 20ג (same as the per-year solution, so not new).
- **New questions?** None. Every sitting here also exists in per-year files, including 2018, which has no solutions anywhere.
- **Are the solutions keyed per question?** Yes, wherever solutions exist: highlighted or red letters per question, plus the 22B-A table. The solutions pack is just the uncensored twin of the exams pack.

### 4. `חומרים אחרים/מבחנים.docx`
- A student's own practice notes: author "חשבון Microsoft", created 2022-02-03, modified 2022-02-07 (the 22A-A exam day).
- **8 screenshot questions**, each followed by the student's worked reasoning. The screenshots are in Holon "שאלה מספר N:" format:
  - Q1 |L(M1)∩L(M2)|=1 (classification, א-ד)
  - Q2 {⟨M,w⟩ | M a non-deterministic TM that rejects w}
  - Q3 L(M)≠∅ and L(M)≠Σ*
  - Q4 A≤mB and A≤mC ⇒ A≤m(B∪C) (T/F)
  - Q5 A∈RE, B∉RE ⇒ A≤mB (T/F)
  - Q6 ∃A,B: A≤pB ⇔ P=NP (T/F)
  - Q7 P=NP ⇒ co-CLIQUE∈P (T/F)
  - an open 3-part PALI question (PALI NP-complete? SAT≤p PALI? PALI≤p SAT?)
- Student answers (**unofficial**): Q1 no letter given (reasoning cut off), Q2 ב, Q3 ד, Q4 ב (לא נכון), Q5 ב (לא נכון), Q6 א (נכון), Q7 א (נכון). PALI: 1 "possible only if P=NP", 3 "yes".
- **Source sitting unidentified**, probably a 2021 exam or a practice sheet. These questions may be new. The text search could not locate them in other PDFs because the stems are images.

---

## Batch summary

| code | files | #Q | MCQ? | key source | form-0 held? | notes |
|---|---|---|---|---|---|---|
| (collection) | אוסף מבחנים...pdf | n/a | n/a | n/a | n/a | 195p merge. Everything is a duplicate except exam 048, the SAMP-2 question paper, the 23B-A form-000 print and the stripped 23A-B paper. The 1254 annots are student ink on 22B-B |
| ??-? (2023, "048") | collection p70-77 | 25 | MCQ + T/F | none | shuffled | **possible gap-filler**, cover pages missing, sitting unknown |
| 23B-A | collection p42-49 (form 000), p101-109, p110-123 | 25 | MCQ | highlight (per-year sol) | no (Q3=ב) | cover mislabelled "סמסטר א" |
| 22B-B | collection p78-99 | 20 | MCQ | **student ink only** | n/a | still no official key |
| SAMP-1 | בחינה לדוגמה.pdf = SAMPLE-FINAL.pdf (+מבחנים בסיבוכיות p14-22) | 25 | MCQ + T/F | none (8 Q keyed via SAMP-3, 3 derived) | n/a | 2022-01 |
| SAMP-2 | בחינה לדוגמה עם הסברים.pdf + collection p170-178 | 29 | MCQ + T/F | highlight + explanations | n/a | Q24 author doubt; Q26 has 6 options |
| SAMP-3 | פתרון מבחן לדוגמא.pdf (+4 copies) | 9+4+7 sub | MCQ + T/F | highlight + explanations | n/a | 2021, 2 parts, numbering restarts |
| pack | מבחנים בסיבוכיות.pdf / פתרונות...pdf (+(1)) | n/a | n/a | n/a | n/a | censored/uncensored 22A-A/B/C sols, 18A-A/B, 22B-A, 20A-A-sol, SAMP-1/3; nothing new |
| DOCX | מבחנים.docx | 7+1 | MCQ/T/F + open | student reasoning | n/a | unidentified source, possibly new questions |
