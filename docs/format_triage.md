# Format triage — Computability & Complexity exams

Consolidated from the per-batch reports in `docs/triage/batch*.md` (full per-file detail, keys,
page numbers). Moodle quizzes are **out of scope** (Adir, 2026-09-29: past exams only).

## Decisions (defaults accepted by Adir 2026-09-29)
- **Year cutoff: 2020+.** 2018 A/B are 5 open proof questions, no solutions → excluded.
- **Form-0 rule does NOT hold in general.** Checked against real keys: fails in 20A-A, 20A-B,
  22A-A/B/C, 22B-A, 23A-A, 23A-B (correct answers spread over א–ד despite "גרסא-0"). Held only
  for 23B-A (Ben-Av) and 23S-A. ⇒ answers come from keys only; form-0-only sittings → ask list.
- **Double answers** confirmed by the key (appeal note / two highlights) → `acceptedIds`.
- **No key** → ask list, not the bank.
- **Topics (11):** tm · decidability · enumerators · undecidability · mapping_reductions ·
  closure · classification · time_p · np (incl. coNP) · poly_reductions · npc.
  Rice / space dropped (Rice only in one student summary; space nowhere).
- Web-shuffler PDFs (`2024-07-08 moedA-no-sol`, `2024 קיץ/מבחן מעורבב`, `2023-02-09 moedA-no-sol`)
  are student-made retypes with lost overlines → **ignored**.

## Per-sitting table
| Code | Date | Q | Opts | Best source file(s) | Key | Status |
|---|---|---|---|---|---|---|
| 18A-A / 18A-B | 5.2.18 / 12.3.18 | 5 open | – | Exam-2018-a moed A/B | none | ❌ excluded (open) |
| 20A-A | 14.2.20 | 25 | T/F + 4 | `…moedA-גרסא-0 SOLUTION` (scan) + `MOED A - SOL` (appeal) | solution scan | ✅ Q23 ג also accepted (MOED A-SOL); Q24 א/ד |
| 20A-B | 11.3.20 | 25 | T/F + 4 | `…moedB-גרסא-0 SOLUTION` | solution | ✅ Q21 no valid option → ask |
| 22A-A | 7.2.22 | 15 | 2–5 | `…moedA-גרסא-0 SOLUTION` | solution | ✅ |
| 22A-B | 9.3.22 | 15 | 2–4 | `…moedB SOLUTION` (= Moed B 2021-22a) | red text | ✅ Q12 hand-drawn graph |
| 22A-C | 2.5.22 | 15 | 4 | `…moedC SOLUTION` (= Moed C 2021-22a ver-0) | solution | ✅ Q8 ב/ד |
| 22B-A | 22.6.22 | 20 | 2–4 | SOLUTION (letter table) + clean `סמסטר ב מועד א 22-6-22` for Q19 | letter table | ✅ |
| 22B-B | 24.7.22 | 20 | 2–4 | no-sol (= `מבחן יולי מועד ב2022`) | none (student scribbles only) | ❓ ask |
| 22B-C | 21.8.22 | 20 | 2–4 | SOLUTION (tutor ink 2024) | handwritten, Q4,15–20 missing | ❓ ask |
| 23A-A | 9.2.23 | 25 | 4 | `חומרים אחרים/מועד א 2023 עם פתרונות` (digital) | highlight + bubble sheet | ✅ Q1 א/ג |
| 23A-B | 5.3.23 | 25 | 4 | `…moedB SOLUTION` | highlight | ✅ |
| 23B-A | 12.6.23 | 25 | 2–4 | `2023/סמסטר א/2023-06-12…SOLUTION` (mis-filed; really סמ ב) | highlight | ✅ Q5 both accepted; Q14 from explanation |
| 23B-B? | 2023 | 25 | ? | collection p70–77 ("מבחן 048", cover missing) | none | ❓ ask |
| 23S-A | 23.8.23 | 25 | mixed | `…2023-08-23 SOLUTION` | explanations highlighted (all א) | ⚠️ medium |
| 24A-A | 21.3.24 | 18 | 4 | `מועד א 21.3 פתרון` | highlight | ✅ Q3 א/ב |
| 24A-B | 5.5.24 | 18 | 4 | `מועד ב פתרון` | highlight | ✅ Q18 ב/ג |
| 24A-C | 30.5.24 | 18 | 4 | `מועד ג פתרון` | highlight | ✅ |
| 24B-A | 8.7.24 | 18 | 2–4 | `מועד א פתרון מתוקן` | corrected key | ✅ Q9 ב/ד |
| 24B-B | 1.8.24 | 18 | 4 | `…moedB-טופס-0` (+ hand-shuffled image copy) | form-0 only | ❓ ask |
| 24S-A | 15.9.24 | 18 | 4 | `…moedA-טופס-0` | form-0 only | ❓ ask |
| 25A-A | 6.2.25 | 18 | 4 | `סמ א מועד א 6.2.25` | none | ❓ ask |
| 25B-A | 2025 | 18 | 4 | `סמ ב מועד א 8` + `פתרון 8` | highlight | ✅ Q17 options swapped in solution → exam letter א |
| 25B-B | 2025 | 18 | 4 | `סמ ב מועד ב 9` + `פתרון 9` | highlight | ✅ |
| 25B-C | 7.9.25 | 18 | 4 | `מס ב מועד ג 7-9` | none | ❓ ask |
| 25S-B | 2025 | 18 | 4 | `2025 קיץ מועד ב` (retype?) | none | ❓ ask |
| 26B-A | 16.6.26 | 25 | 4 | `…מועד א מעורבל עם תשובות` | highlight | ✅ Q2 from proof box |
| 26B-B | 8.7.26 | 25 | 4 | `…מועד ב עם תשובות מתוקן שאלה 17` | highlight | ✅ **FLAGSHIP** |
| SAMP-1 | – | 25 | 4 | `בחינה לדוגמה` (= SAMPLE-FINAL) | 8 Q via SAMP-3 | partial |
| SAMP-2 | תש"פ | 29 | mixed | `בחינה לדוגמה עם הסברים` + review deck 2025 | highlight | ✅ Q24 author doubt |
| SAMP-3 | 2021 | 13+7 | mixed | `פתרון מבחן לדוגמא` | solution | ✅ |

**Keyed & in scope:** 20 sittings (~430 Q before dedupe). Review decks (`מצגות חזרה למבחן/`) →
extra explanations only.

## Duplicates confirmed (don't double count)
- 2018 copies in `חומרים אחרים` = originals. `Moed B/C 2021-22a` = 22A-B / 22A-C.
- `מבחן 22.6.22` = 22B-A SOLUTION; `מבחן יולי מועד ב2022` = 22B-B no-sol.
- `Exam Computability moedB 2022-23a SOLUTION` = `מועד ב 2023 עם תשובות` = 23A-B.
- `MOED A - SOL` = 20A-A (plus Q23 appeal note). `2.5.2022 (לא) מצונזר` = phone notes of 22A-C.
- `מבחנים בסיבוכיות` / `פתרונות למבחנים בסיבוכיות` = self-made packs of existing exams.
- Collection (195p) = per-year files + SAMP-2/3, except the "048" 2023 exam.
