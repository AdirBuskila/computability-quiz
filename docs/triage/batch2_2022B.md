# Batch 2 — 2022 Semester B (תשפ"ב סמסטר ב)

Source root: `C:\Users\Adir\Desktop\BSC\שנה ג\חישוביות וסיבוכיות`
Renders: `tools/raw/22B-A-SOL`, `22B-A-HEB`, `22B-B-F0`, `22B-C-SOL`, `22B-C-HEB` (200 dpi, all pages).
Lecturer on all covers: ד"ר רדאל בן-אב, course 61306, 2.5 hours, "דף עזר" attached.

Common structure (all three sittings): 20 questions, all MCQ, in 5 sections:
- Q1–5 general (Q1,2,4 and Q5 in 22B-B/C have **3 options א-ג**; Q3/Q5 (L∞) have 4 options)
- Q6–8 classify a language (4 options, the standard R / RE\R / coRE / neither set)
- "יחסים בין שפות" Q9–11 (4 options: =, ⊂, ⊃, "אף תשובה אינה נכונה")
- "רדוקצית מיפוי" Q12–14 (**Q12, Q13 have 2 options א כן / ב לא**; Q14 has 4)
- "רדוקציה פולינומית" Q15–17 (4 options)
- "שאלות שונות" Q18–20 (4 options)

No figures (no TM diagrams). A boxed machine/mapping-function definition precedes Q12 and Q15. No "א ו-ב נכונות" options.
Last 2–4 pages of every file are the scanned helper sheet (דף עזר), image-only.

**Key finding: in 2022B the "גרסא-0" files do NOT follow the "correct answer = first option" rule.** Correct answers sit in natural positions (see 22B-A key).

---

### 22B-A — מועד א, 22-6-22 (3 files, same form)

| file (decoded) | format | pages | notes |
|---|---|---|---|
| `מבחנים/2022/סמסטר ב/2022-06-22-Exam-חישוביות-2022-moedA-גרסא-0 SOLUTION.pdf` | text-PDF (Word 2013) | 10 | **key file**, draft with tracked changes |
| `חומרים אחרים/מבחן 22.6.22.pdf` (mojibake `ÄüçÅ 22.6.22.pdf`) | text-PDF | 10 | **byte-identical to the SOLUTION file except the PDF trailer /ID** (same size 2,024,982 B; 62 differing bytes, all in /ID). Pure duplicate. |
| `מבחנים/2022/סמסטר ב/סמסטר ב מועד א 22-6-22.pdf` | text-PDF (Word 2016) | 10 | clean final exam as handed out: empty answer table, tracked changes applied. Same question order and same option order (checked p.7 Q18–20, text-diff of whole file). |

- Cover: "סמסטר ב' תשפ"ב / מועד א / 22-6-22". No form/version number printed on the cover.
- Version: filename says גרסא-0; the clean sibling has identical order, so there is just one form. Not shuffled.
- **Answer source: letter table on the cover (p.1)** in red, next to question numbers. No highlights/circles. Clear.
- **Key 22B-A:** `1ג 2ג 3א 4א 5ג 6ד 7ג 8א 9ד 10ג 11ד 12א 13א 14ב 15ד 16ג 17א 18ד 19א 20ג`
- **Form-0 check: does NOT hold.** Key = א only for Q3, 4, 8, 12, 13, 17, 19. Exceptions (not first option): 1ג, 2ג, 5ג, 6ד, 7ג, 9ד, 10ג, 11ד, 14ב, 15ד, 16ג, 18ד, 20ג.
- Odd / to watch during extraction:
  - The SOLUTION file is a **draft with visible Word tracked changes** (red underline/strikethrough): the NEQ_TM definition (p.5), the Q8 stem (p.3, an added "כלומר t(<M,w>) הינה פונקציה שמחזירה את מספר צעדי החישוב..." line), the f definition before Q15 (p.6), Q17 stem and options (p.6), Q18 stem "אם P=NP" (p.7).
  - **Q19 was completely rewritten** by tracked changes. The final version (clean sibling p.7) is "תהיינה A ו-B שפות כך ש B∈NPC, B ≤p A, A∈P. האם נובע מנתונים אלה ש NP=P?" with options א כן / ב לא / ג רק אם NP∩coNP≠P / ד רק אם B∉coNP. Key 19א fits the **final** version. Use the stem from the clean sibling.
  - **Q20 option ג has a typo**: "QLIQUE ∈ PM" in SOL and "MQLIQUE ∈ P" in the clean copy. The intended meaning is MCLIQUE ∈ P (key ג).
  - Q12 option ב "לא" is printed bold in all copies (formatting artifact, not a mark).
  - Q4 has 3 options (נכון / לא נכון / אין מספיק מידע). Q1–3 have 3 options.
  - Overlines are all readable in the images (Q1 L̄1∩L̄2, Q2 L̄2∩L1, Q3 complement of L(M2)∩L(M1)). Reductions use ≤m (Q9–14) and ≤p (Q15–18).

### 22B-B — מועד ב, 24-7-22 (2 files, same form, NO KEY)

| file (decoded) | format | pages | notes |
|---|---|---|---|
| `מבחנים/2022/סמסטר ב/2022-07-24-Exam-חישוביות-2022-moedB-גרסא-0 no-sol.pdf` | text-PDF (Word 365) | 11 | clean exam, empty answer table |
| `חומרים אחרים/מחבנים נוספים/מבחן יולי  מועד ב2022.pdf` (mojibake `ÄçüÉëì Éàæöëì/ÄüçÅ ëàîë  ÄàÆâ ü2022.pdf`) | text-PDF | 11 | **byte-identical to the no-sol file except the trailer /ID** (same size 1,239,565 B; 62 differing bytes, all /ID). **0 annotations, no highlights, no marks → contains NO key.** |

- Cover: "סמסטר ב' תשפ"ב / מועד ב / 24-7-22". Answer table on the cover is empty. No version number printed.
- Version: form-0 per filename. It has the same section layout as 22B-A/22B-C.
- Answer source: **none** in either file. So there is no form-0 check.
- Odd:
  - p.2: small stray pen-like scribble left of Q2 (roughly "-ו d"). It is part of the page content (a vector drawing), not an annotation and not an answer mark.
  - Q16 option א refers to "מספר הקודקודיים ב G" although the section is about GSAT/ESAT formulas. This is a copy-paste leftover from 22B-A.
  - Q20 heading says "נגדיר את השפה MCLIQUE" but defines **MIS2** = {⟨φ⟩ | G graph, V(G)=#vertices, ⟨G, V(G)−2⟩ ∈ IS}. The ⟨φ⟩/G mismatch and the wrong heading are in the source.
  - Q8 defines L_h but its options say "L" (cosmetic).
  - Q18: "נניח שקיימות שפות A,B … B ≤p A, A∈NPC, B∉P, מה מהבאים הכרחי" with options NP=coNP / NP∩coNP=P / P≠NP / P=NP.
- Stems partly overlap 22B-C (Q2, Q4, Q12–17, Q19 are near-identical to 22B-C). Where a 22B-C answer exists for a near-identical question, it could be reused **only after a content check**. Q12–14 in B and C differ (INF_TM vs ALL_TM machine definitions), so do not transfer those blindly.

### 22B-C — מועד ג, 21-8-22 (2 files, same form)

| file (decoded) | format | pages | notes |
|---|---|---|---|
| `מבחנים/2022/סמסטר ב/2022-08-21-Exam-חישוביות-2022-moedC-גרסא-0 SOLUTION.pdf` | text-PDF (Word 2016) + **473 PDF annotations** | 11 | "SOLUTION" = someone's handwritten ink markup |
| `מבחנים/2022/סמסטר ב/סמסטר  ב מועד ג 21-8-22.pdf` | text-PDF (Word 2016) | 11 | same exam, clean, 0 annotations. The text layer is identical to the SOLUTION file's base text (only diff = the 2 FreeText boxes). Same order, not shuffled. |

- Cover: "בס"ד / סמסטר ב' תשפ"ב / מועד ג / 21-8-22". Answer table on the cover is **empty** (no letter table). No version number printed.
- **What the ~470 annotations are:** 471 Ink plus 2 FreeText, all created **2024-07-05** (2 years after the exam):
  - red ink, pp.2–4: working notes and circled options
  - blue ink with no author, pp.4–7: working notes, circled options, and big X's crossing out whole sections
  - 2 FreeText boxes on p.2: an explanation for Q3 ("כל שפה L היא סופית ולכן חיתוך… היא ב R") and a stray "L = {M | L(M) empty}" next to Q4
  - This looks like a **tutor/class solving session, not an official key**.
- Answer source: circled letters in handwriting. Clear where present.
- **Key 22B-C (unofficial, handwritten):**
  `1ב 2א 3א 4? 5ב 6ב 7ג 8ג 9ג 10א 11ג 12א 13ב 14ד` and **15–20: no answer**
  - Q4 (p.2): no circle. The stem/options are crossed with a big red X → **unclear**. It may mean the question was treated as dropped or irrelevant.
  - Q2 (p.2): א is circled, and the words "להיות נכון ויכול" in option ג are also underlined → I read the answer as א (the circle is unambiguous).
  - Q6 (p.3): ב circled; ג and ד crossed out.
  - Q9 (p.4): ב crossed out, ג circled. **Note: in 22B-C, Q9 option ג reads "B ⊂ A"** (not "A ⊃ B" as in 22B-A/B), and Q10 ג reads "C ⊂ B", Q11 ג "C ⊂ A". This is the same meaning as ⊃, just phrased differently.
  - Q13 (p.5): ב circled several times. Q14 (p.5): א, ב, ג crossed out, ד circled.
  - **Q15–17 (p.6) and Q18–20 (p.7): the definition box and the questions are crossed out with big blue X's, and no answers are marked.** Most likely they were skipped as outside the material being practised → **no key for 15–20.**
- Form-0 check: the filename says גרסא-0 but the key is **not** all-א: 1ב, 5ב, 6ב, 7ג, 8ג, 9ג, 11ג, 13ב, 14ד are exceptions (א only for 2, 3, 10, 12). This is consistent with 22B-A, where the "first option correct" rule does not apply in 2022B.
- Odd: Q3 stem "|L_i| ≠ ∞ כלומר כל השפות סופיות" is intersection-of-finite-languages. Q20 defines FPhi (CNF, K = #vars − 2, ⟨φ⟩∈KSAT). Q15 f-box: "אם k איזוגי: φ' = φ∧φ'', k' = 2k".

---

## Batch summary

| code | files | #Q | MCQ? | key source | form-0 held? | notes |
|---|---|---|---|---|---|---|
| 22B-A | SOLUTION (key) + `מבחן 22.6.22` (byte-dup) + Hebrew-named clean copy | 20 | yes (Q1–4 3 opts, Q12–13 2 opts, rest 4) | letter table on cover, clear, full 20/20 | **NO** (13 of 20 not א) | SOL is a tracked-changes draft; Q19 rewritten, so take the stem from the clean copy; Q20 ג typo |
| 22B-B | no-sol + `מבחן יולי מועד ב2022` (byte-dup) | 20 | yes (same layout) | **none**: the mojibake file has no marks | n/a | no key anywhere in this batch; Q20 MCLIQUE/MIS2 heading mismatch; Q16 "G" leftover |
| 22B-C | "SOLUTION" (ink notes) + Hebrew-named clean copy | 20 | yes (same layout) | handwritten circles (2024 tutoring ink), 13/20 | **NO** | Q4 crossed out/unclear; Q15–20 crossed out, unanswered; unofficial |
