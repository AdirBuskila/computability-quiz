# Batch 8: review decks and topic taxonomy

Source root: `C:\Users\Adir\Desktop\BSC\שנה ג\חישוביות וסיבוכיות` (read-only, nothing modified).
Renders are under `tools/raw/REV-SAMPLE-TASHPAP/` (80 dpi), `tools/raw/REV-2024-STUDENTS/` (110 dpi) and `tools/raw/REV-2025-L13/` (80 dpi). All are slide or page images, and the file names are `page-NN.png` (two digits, `page-100.png` and up for three).

Method: I dumped the text layer of every exam, sample exam, deck, lecture and tutorial. I then matched question stems against the exam corpus after NFKC and whitespace normalisation. I viewed about 10 slides per deck to check the format and the answer marking.

Sitting codes follow the brief: 20A-A = 2020-02-14, 20A-B = 2020-03-11, 22A-A = 2022-02-07, 22A-B = 2022-03-09, 22A-C = 2022-05-02, 22B-A = 2022-06-22, 23A-B = 2023-03-05, 23B-A = the "2023-06-12 moedA" file (matching the existing `23B-A-SOL` render), 23S-A = 2023-08-23, 24A-A/B/C = 2024 semester A, 24B-A = 2024-07-08, 25A-A = 6.2.25.

Sample exams:
- **SMP-29** = `מבחנים לדוגמה/בחינה לדוגמה עם הסברים.pdf`: the "מבחן לדוגמא תש"פ", 29 questions in parts א–ו, with explanations.
- **SMP-25** = `מבחנים לדוגמה/ בחינה לדוגמה.pdf`: a different sample, 25 questions.

---

## Part 1: review decks

### 1. ` פתרון מבחן לדוגמא תשפ אלישבע סמסטר ב 2025.pdf` (113 slides, text-PDF slides, Elisheva, 2025B)

**Main part (slides 1–82): the full sample exam SMP-29, all 29 questions.**
- **Parts:**
  - א (Q1–6): true/false.
  - ב (Q7–9): 4-option classification.
  - ג (Q10–12): relations between the classes G1, G2, G3.
  - ד (Q13–20): true/false on R_M and T_M.
  - ה (Q21–24): VCM ≤p proof.
  - ו (Q25–29): MCQ with א–ד options, including "תשובות א ו-ב נכונות".
- **Match:** the stems match `בחינה לדוגמה עם הסברים.pdf` question by question. I checked Q1, 2, 7, 8, 9, 21–29 by text. The same sample is also inside `אוסף מבחנים…pdf` pp.171–186.
- **Answers:** every question has a question slide followed by a "תשובה" slide. The correct option is **highlighted in yellow** (I saw this on p7, where A1 = נכון) and followed by a "הסבר". Many questions add extra "הרחבות" slides that the PDF explanations do not have, for example p8, p13–16, p52, p57, p60.
- **New questions:** none. This part is useful as a second, richer explanation source for SMP-29.

**Extra part (slides 83–113): "שאלות נוספות, ממבחנים אחרים…" (9 items).**

| # | slides | stem | source sitting | answer shown? |
|---|---|---|---|---|
| 1 | 84–86 | L = {⟨M⟩ \| M halts on all input} | 23S-A (p4) | yes, highlighted, with expansion |
| 2 | 87–88 | {⟨M,k⟩ \| ∃w: M(w) does not halt within k steps} | 23A-B (p7) | yes (א, decidable) |
| 3 | 89–91 | f = 0/00/1 by halting parity; which L works | 23A-B Q11 (p9); variant in 23A-A | yes |
| 4 | 92–95 | L = {⟨M⟩ \| M accepts all even palindromes}, Q(x), H_TM NP-hard | 22A-C Q7 and 23A-B Q13 (same question) | yes (ג, cyan highlight) |
| 5 | 96–97 | L = {⟨A,w⟩ \| DFA A accepts w and ∃ TM M accepting w} | 23A-B Q16 (p13) | yes |
| 6 | 98–103 | A = {L \| CLIQUE ≤p L, L∈NP}, B = {L \| PATH ≤p L} | 23A-B Q18 (p15); 22A-A Q15 is a 3SAT/PRIME variant | yes, and slide 100 says "נושא זה אינו בחומר" for the P=NP condition |
| 7 | 104–108 | ALL_DFA / ALL_NFA / RG … | 23S-A (labelled "תשפ"ג קיץ א" on the slide) | yes |
| 8 | 109–111 | ECLQ: CLIQUE ≤p ECLQ, Q20–21 | **20A-A Q20–22** (scan, p7; I viewed it) | **no answer slide** |
| 9 | 111–113 | F2SAT ≤p 3SAT, Q17–19 plus a worked φ example | 23B-A (p11–12) | **no answer slide** (only a worked example on p112) |

**Verdict:** this deck solves **SMP-29 fully** plus 9 known exam questions from 20A-A, 22A-C, 23A-B, 23S-A and 23B-A. It adds **no new questions**. Its value is the extended explanations. For items 8 and 9 the key must come from the exam solutions.

### 2. `2024-חישוביות-שיעור-חזרה-לבחינה-מבוסס על שאלות שבחרו הסטודנטים-1.pdf` (15 pages, one question per page)

- **Format:** each page has "שאלה N" with the stem, then "פתרון – התשובה הנכונה היא X" with the letter highlighted in yellow, then a full proof (reductions, NTM constructions, tables showing that the reduction preserves membership).
- **Stems:** they are pictures or pasted images, and some are phone photos of exam pages (Q10, Q11, Q12, Q14). The text layer contains **only the solutions**, not the stems.
- **Count:** 14 questions (Q2 spans pp.2–3).

| # | page | stem (short) | answer | source |
|---|---|---|---|---|
| 1 | 1 | {⟨M,w⟩ \| NTM M rejects w} | ב | not located (possibly new, or in a scan) |
| 2 | 2–3 | {⟨M⟩ \| L(M)≠∅ and L(M)≠Σ*} | ד | not located |
| 3 | 4 | ∀w M halts within \|w\|² steps | ג | 22B-A (p3); also 20A-B, SMP-25 |
| 4 | 5 | infinite union of always-halting TMs M1, M2, … | ב | 20A-B (p10); SMP-25 (p9) |
| 5 | 6 | L1∈R, L2∈RE: L1∖L2 … | ג | 22A-A (p3); 24B-A (p2) |
| 6 | 7 | {⟨M⟩ \| M accepts no palindrome} | ג | not located |
| 7 | 8 | A#B closure | ג | 22A-B (p6); 24A-A (p3) |
| 8 | 9 | M accepts no even-length word (by the solution) | ד | not located |
| 9 | 10 | f(⟨M,x,1^k⟩) computable in poly time (question "25.") | א | **SMP-25 Q25** (p9); also 20A-B p11 |
| 10 | 11 | ∃L∈NP with L ≤p L̄ ⇒ P=NP (photo) | א (לא נכון) | SMP-29 Q5 |
| 11 | 12 | L∈RE∖R and NTM paths infinite/finite (photo) | discussed per option | 23A-B (p2); similar in 24A-B p2 |
| 12 | 13 | ⟨A,w⟩ DFA and ∃TM (photo, "שאלה 16") | א | 23A-B Q16 |
| 13 | 14 | R_M, ALL_TM / INF_TM counterexamples | open-form | 20A-B (p4–7); SMP-25 (p5–6) |
| 14 | 15 | CLIQUE_2024 with P≠NP (photo) | א | 24A-A Q8 |

**Verdict:** everything located comes from past sittings: 20A-B, 22A-A, 22A-B, 22B-A, 23A-B, 24A-A, SMP-25 and SMP-29. The deck gives the **answer plus a full explanation** for all 14. Q1, Q2, Q6 and Q8 were not found in any exam text layer. They could be in the scan-only files (20A-A, 23A-A-SOL) or they could be **new questions**. They need a visual check against those scans before they are treated as new.

### 3. `2025-Lecture 13 - שיעור חזרה למבחן.pdf` (79 slides, "הרצאה 13", Elisheva 2025B)

- **Structure:** 26 numbered questions. Each has a question slide, then one or two answer slides with the correct option **highlighted in yellow** and a blue "פתרון / הוכחה / הפרכה" box that refutes each option. I viewed pp.8, 22–23, 37, 44, 55, 76–77.
- **Text layer:** most question slides are images, so the text layer covers only about 12 of the 26.
- **Question types:** 4–5-option MCQ (Q3 has options א–ה), true/false (Q14/15 and Q17), and "find the error in the proof" (Q19).

Sources identified (by text match or by stem viewed):
- **Q1** universal TM / SAT ≤m SAT / P closed under ∩: **22A-C** (p2); also 24A-C p2.
- **Q2** {M \| ∃ palindrome u such that M halts on u}: **22A-C** (p2).
- **Q5** PATH NP-complete if P=NP: 22A-A (p9) or 22A-C (p4).
- **Q8** NTM computation trees: 22A-A (p3–4), 22A-C (p9–10) and 24A-B (p2) have the same theme. Answer ד.
- **Q11** H_TM ≤m L; possible reductions with E_TM: **22A-C** (p3).
- **Q13** ∃w on which M rejects in exactly \|Q\| steps: 24B-A-SOL (p11); also 23S-A, 25S-B, 25B-C.
- **Q17** "תחת ההנחה P=NP: A,B∈NPC ⇒ A∪B∈NPC": **SMP-25 Q2**.
- **Q19** "prime and divisible by 3", R(x) with x==17∨18, find the error: **22A-A** (p8).
- **Q21** A,B non-trivial distinct, A≤mB and B≤mA: 24B-A (p1–2) or 25A-A (p9).
- **Q26** L1∈R, L2∈RE, which is not necessarily in RE: 22A-A (p3) or 24B-A (p2). Answer ב.
- **Not located:** Q3 (L∉R ⇒ A_TM ≤m L…, 5 options), Q4, Q6, Q7 (function T computed via HALT), Q9, Q10, Q12, Q14–16, Q18, Q20, Q22–25. Their slides are image-only and I did not open them all.

**Verdict:** this is a compilation of past-exam questions with the **answer plus a per-option explanation**. It leans heavily on 22A-A, 22A-C, 24B-A and the samples. It may contain a few new or reworded items among the roughly 14 I did not locate. For extraction, dedupe by content against the exams first, and treat only the leftovers as new.

---

## Part 2: topic taxonomy

### What is taught, and where (Elisheva, 2025 semester B)

`הרצאות אלישבע סמסטר ב 2025.pdf` is **only a one-page list of dates and links** (lessons 1–12 plus a תגבור, 2.3–27.5). It has no titles. Slides exist only for lectures 1–7. I inferred lectures 8–12 from tutorials 8–12, the handwritten summaries in `סיכומים/אלישבע סמ' ב 2025 אברהם דבורה/` (mirrored scans that are hard to read) and the lecture 13 review, so that part is lower confidence.

| Lecture / tutorial | Content | Topic keys |
|---|---|---|
| L1 | decision problems and languages; DFA/PDA recap; TM informal and formal definition, δ, non-halting | tm |
| L2 | configurations, computations, accept vs decide, classes **R, RE**; variants: stay-put, multi-tape, two-way-infinite tape; Hilbert's hotel | tm, decidability |
| L3 | non-deterministic TM, computation trees, NTM ≡ DTM (BFS simulation) | tm |
| L4 | **Church–Turing thesis (2 slides)**; Hilbert's 10th problem, H10 ∈ RE; R closed under complement; L∈R ⇔ L, L̄ ∈ RE; **coRE**; **enumerators** (the lexicographic enumerator ⇔ R part is "חומר רשות") | church_turing, decidability, closure, enumerators |
| L5 | encodings (graphs, TMs, DFAs); A_DFA, A_NFA ∈ R; universal TM; A_TM | decidability |
| L6 | countability and diagonalization (a non-RE language exists); **A_TM ∉ R**, **HALT ∉ R**, K_{M,w}, **E_TM ∉ R, E_TM ∈ coRE** | undecidability |
| L7 | reduction intuition; **computable functions**; **≤m definition**; A_NFA ≤m A_DFA; A_TM ≤m HALT; the reduction theorem; using it for E_TM | mapping_reductions |
| L8–9 (inferred) | more ≤m reductions; complement or transitivity properties (≤m ⇔ complements) | mapping_reductions |
| L10 (inferred) | map of RE∖R, coRE∖R and neither | classification |
| L11 (inferred) | P and NP (NTM in poly time), PATH, CLIQUE, P=NP? | time_p, np |
| L12 (inferred) | NP-completeness, ≤p properties, SAT/CNF, Cook–Levin | poly_reductions, npc |
| T1–T2 | build TMs (Σ*1, palindromes, shiftRight); can L(M) be in R if M does not halt on some w? | tm |
| T3 | R and RE closed under ∩ and ∪ | closure |
| T4 | NTM for composite numbers; accepting paths | tm |
| T5 | NTM halting on every input ⇒ decides?; L1∖L2 with R/RE; concatenation closure | tm, closure |
| T6 | classify ⟨M,k⟩ and H10Even; class relations A vs B; G1–G4 relations; EQ_TM ∉ R | classification, undecidability |
| T7 | INTERSECT_TM ∈ RE∖R and similar | classification, undecidability |
| T8–T9 | ≤m definition and theorem; graph-language reductions; L ≤m L̄ with L∈RE ⇒ L∈R; HALT ≤m A_TM? | mapping_reductions |
| T10 | P and NP (NP **defined via a poly-time NTM**); P/NP closed under ∪ and ∩, P under complement ("unknown whether NP is closed under complement"); PATH ∈ P; SUBSETSUM | time_p, np, closure |
| T11 | ≤p transitivity; HAMPATH/HAMCYC variants; IS ≤p Almost-IS | poly_reductions |
| T12 | NPC definition; Cook–Levin; NPC∩P≠∅ ⇔ P=NP; PALI and NPC; 4SAT ≤p 3SAT; the flawed "P≠NP proof" | npc |

Evidence of how often each topic appears in exams (text-layer hits over all exam files):

| Topic | Exam files | Details |
|---|---|---|
| **Rice** | **0** | Also 0 in lectures, tutorials and all three review decks. Only one student summary mentions it (תומר כהן 2026). |
| **coNP** | about 9 | 22B-A/B/C, 23B-A, 23S-A, 24A-C, 22A-C. None in 2025 or 2026, and not in the 2025B tutorials. |
| **Enumerators** | 9 sittings | 18A-A, 20A-B, 22A-C, 23A-A, 23A-B, 25A-A, SMP-25, SMP-SOL, … |
| **Verifiers / certificates** | 0 | NP is taught via NTMs. |
| **Space / PSPACE / Savitch** | 0 | Nothing anywhere. |
| **Recursion theorem** | 0 | |
| **Computable functions** | many | Always inside ≤m reductions ("f ניתנת לחישוב", or poly-time computable). |

### Proposed closed list (amended)

| key | תווית | status |
|---|---|---|
| `tm` | מכונות טיורינג, וריאנטים ומ"ט א"ד (כולל קונפיגורציות ותזת צ'רץ'-טיורינג) | keep; **absorbs church_turing** |
| `decidability` | כריעות וקבלה: R, RE, coRE (כולל בעיות כריעות על אוטומטים, H10) | keep |
| `enumerators` | אנומרטורים | **add** (L4; about 9 exam sittings) |
| `undecidability` | אי-כריעות: לכסון ובעיית העצירה, E_TM | keep |
| `mapping_reductions` | רדוקציות מיפוי (≤m) ופונקציות ניתנות לחישוב | keep; **absorbs computable functions** |
| `closure` | תכונות סגור (R/RE/coRE, וגם P/NP) | keep |
| `classification` | סיווג שפות (R / RE∖R / coRE∖R / אף אחת) | keep, the most frequent question type; allow a co-tag with mapping_reductions |
| `time_p` | סיבוכיות זמן והמחלקה P | keep |
| `np` | המחלקה NP (מ"ט א"ד פולינומית), כולל coNP | keep, but **change the label**: not "verifiers" (not taught). **Absorbs conp** |
| `poly_reductions` | רדוקציות פולינומיות (≤p) | keep |
| `npc` | NP-שלמות: Cook–Levin, SAT/3SAT/CLIQUE/IS/VC/HAMPATH | keep |

- **Drop:** `church_turing` (merge into tm: two slides and no standalone exam questions), `rice` (not taught and never asked; the "property of L(M)" questions are solved by reductions, so they go to classification or mapping_reductions), `space` (not taught), `conp` (merge into np; its few questions are all from 2022–2024).
- **Do not add:** recursion theorem, PSPACE or space complexity (not covered). Universal TM and encodings stay inside decidability/undecidability.
- **Optional:** if you want coNP to stay filterable, keep `conp` as a separate key. It would hold roughly 5–10 questions.

---

## Batch summary

| code | file | #Q | MCQ? | key source | form-0? | notes |
|---|---|---|---|---|---|---|
| REV-SAMPLE-TASHPAP | ` פתרון מבחן לדוגמא תשפ…2025.pdf` | 29 + 9 extras | T/F and 4-option | yellow highlight + הסבר + הרחבות | n/a | = SMP-29 plus extras from 20A-A, 22A-C, 23A-B, 23S-A, 23B-A; no answer for extras 8 and 9; no new questions |
| REV-2024-STUDENTS | `2024-…שאלות שבחרו הסטודנטים-1.pdf` | 14 | 4-option (mostly) | "התשובה הנכונה היא X" + proof | n/a | stems are images or photos; 10 of 14 located in past exams; Q1, 2, 6, 8 unlocated (possibly new) |
| REV-2025-L13 | `2025-Lecture 13 - שיעור חזרה למבחן.pdf` | 26 | 4/5-option, T/F, find-the-error | yellow highlight + per-option refutation | n/a | about 10 located (22A-A, 22A-C, 24B-A, 25A-A, SMP-25); about 14 image-only slides not checked |
