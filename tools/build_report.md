# Build report — Computability & Complexity questions

- Raw exam files: **29**
- **Final questions: 592** (unique by dedupKey: 551, duplicates kept: 41)
- Excluded: **0** 
- Shared context blocks: **42**
- Math spans rendered (distinct): **2493**
- lockOrder: 6 · multiple accepted answers: 9

- **On hold (not in bank, see docs/ASK_ADIR.md): 9**

  - 22B-B Q3: No option is always true: without the chain condition L_i ⊆ L_{i+1} (present in 22B-A Q5), the union of RE\R languages can be Σ* (∈P, ∈R), RE\R, or not RE (examples in the explanation). Likely intended ג (RE closed under union) but that is false for infinite unions -> hold.
  - 22B-B Q5: Stage-2 verifier not confident: c holds if M1 may be nondeterministic (an immediate-reject branch), but the intended deterministic reading gives a.
  - 22B-C Q4: Two readings give different answers: as 'assume P=coNP; is CLIQUE̅∉NP?' the conclusion is refuted -> ב; as a material implication the statement is equivalent to P≠coNP (i.e. P≠NP), an open problem -> ג (אין מספיק מידע). The tutor's ink crosses Q4 out with no circle.
  - 22B-C Q13: Tutor circled ב (several times) — DISAGREES with the solved א. Also the T box has a print error (step 2 tests 'M2 accepted' before M2 runs, step 4 tests M1): with the intended M1/M2 order the answer is א; read literally (accept only in step 4 when M1 accepted, after M2 halted) L(T)=L(M1)∩halt(M2) and the answer is ב.
  - 22B-C Q17: Print omission changes the answer: the f box defines f only for odd k. With the natural completion (identity for even k, as printed in 22B-B) f is a valid poly-time reduction -> ב; read literally f is not defined on inputs with even k, so it is not a (total) reduction -> א.
  - 22B-C Q20: KSAT is never defined in the exam. Read as 'satisfiable with ≤K true variables' (like GSAT) FPhi is NP-complete -> ב; read as K-CNF-SAT (every clause has K = n-2 literals) it is in P (each clause kills only 4 of 2^n assignments, so an unsatisfiable input must have ≥2^(n-2) clauses and brute force is polynomial in the input) -> ג, which is also what the parallel questions 22B-A Q20 / 22B-B Q20 (…∈P) suggest. Ambiguous -> hold.
  - 25A-A Q13: Answer depends on the open P vs NP question: if P≠NP then A=NPC ⊂ B (ג); if P=NP a finite language like {0} is NP-complete but not in B, so no relation holds (ד). Intended answer probably ג.
  - 25A-A Q14: Two refutations apply: f is not guaranteed polytime (ב), AND the correctness condition fails (e.g. G = single edge, k=2: G∉IS but G'=G∈STAR), which is what ג tries to say — but ג's printed condition 'f(<G,k>) ∈ IS ↔ <G',k> ∈ STAR' is garbled. Intended answer probably ב.
  - SAMP-1 Q7: Print-level ambiguity: read literally, w=ε forces M to halt within 0 steps, i.e. its start state is a halting state, so M halts at once on every input and L = {<M> | q0 ∈ {q_acc,q_rej}} is DECIDABLE (א). The intended answer is surely ג (coRE\R, via an H̄_TM ≤m L reduction). The two readings give different answers -> hold.

## By topic

| topic | label | n |
|---|---|---|
| `tm` | מכונות טיורינג, וריאנטים ומ"ט א"ד | 46 |
| `decidability` | כריעות וקבלה: R, RE, coRE | 54 |
| `enumerators` | אנומרטורים | 4 |
| `undecidability` | אי-כריעות: לכסון ובעיית העצירה | 8 |
| `mapping_reductions` | רדוקציות מיפוי (≤m) | 142 |
| `closure` | תכונות סגור | 46 |
| `classification` | סיווג שפות | 89 |
| `time_p` | סיבוכיות זמן והמחלקה P | 27 |
| `np` | המחלקה NP ו-coNP | 25 |
| `poly_reductions` | רדוקציות פולינומיות (≤p) | 84 |
| `npc` | NP-שלמות | 67 |

## By exam

- SAMP-1: 24
- SAMP-2: 29
- SAMP-3: 20
- 20A-A: 25
- 20A-B: 24
- 22A-A: 15
- 22A-B: 15
- 22A-C: 15
- 22B-A: 20
- 22B-B: 18
- 22B-C: 16
- 23A-A: 25
- 23A-B: 25
- 23B-A: 25
- 23B-B: 25
- 23S-A: 25
- 24A-A: 18
- 24A-B: 18
- 24A-C: 18
- 24B-A: 18
- 24B-B: 18
- 24S-A: 18
- 25A-A: 16
- 25B-A: 18
- 25B-B: 18
- 25B-C: 18
- 25S-B: 18
- 26B-A: 25
- 26B-B: 25

## By source

- exam: 519
- sample: 73

## By confidence

- high: 591
- med: 1
- low: 0

## Official vs unofficial

- official: 425
- unofficial: 167

## By answerSource

- corrected-key: 18
- explanation-inferred: 27
- highlighted-pdf: 319
- letter-table: 19
- solution-pdf: 42
- solved: 167
