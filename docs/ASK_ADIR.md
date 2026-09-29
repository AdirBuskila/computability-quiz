# Ask Adir — open items

Running list. Items stay out of the bank until answered.

## Sittings without a key (excluded until you provide one)
1. **22B-B** (24.7.2022) — `מבחנים/2022/סמסטר ב/2022-07-24-…moedB-גרסא-0 no-sol.pdf`. Only a student's scribbles (collection p90–95). Key?
2. **23B-B?** — collection `אוסף מבחנים…pdf` p70–77, Holon "מבחן מס' 048", cover missing. Which sitting? Key?
3. **25A-A** (6.2.2025), **25B-C** (7.9.2025), **25S-B** (`2025 קיץ מועד ב.pdf`, no cover — official copy?). Keys?
4. **24B-B** (1.8.2024) and **24S-A** (15.9.2024) — only form-0 files; form-0 rule proved unreliable elsewhere. Include as "unofficial"?
5. **22B-C** (21.8.2022) — only a tutor's handwritten 2024 answers, Q4 and Q15–20 unanswered. Use as low-confidence?
6. **SAMP-1** (`בחינה לדוגמה.pdf`) — 17 of 25 questions have no key.

## Per-question
7. **20A-B Q21** — solution says "none correct" but no such option exists. Drop?
8. **SAMP-2 Q24** — author's own note questions the key ("נכון"). Keep?
9. **26B-B Q17** — file says "מתוקן שאלה 17", no note inside; keyed ג (L ∉ RE, L̄ ∈ RE). Do you know what changed?
10. **23S-A** — options not highlighted; key (all א) inferred from highlighted explanations. OK?

## From extraction (in bank unless marked HOLD)
11. **HOLD — 23A-B Q9** (`2023-03-05…moedB…SOLUTION.pdf` p7): L = {⟨M,k⟩ | ∃w: M doesn't halt on w within k steps}. Key = ב (RE\R), but within k steps M reads only its first ~k cells, so testing all words of length ≤ k+1 decides L → א. The key's own proof is "intuitive, no reduction given". Which answer?
12. **23B-A Q14** (`2023-06-12…SOLUTION.pdf` p9): no highlight; answer א (כן) inferred from the explanation (confidence med). Confirm.
13. **23B-A cover** says "סמסטר א' תשפ"ג", no date, lecturer Ben-Av; the Holon print of the same exam says סמסטר ב 12/06/2023 → coded 23B-A. Confirm.
14. **23S-A Q20** (`2023-08-23…SOLUTION.pdf` p9): answer inferred from a thin explanation (n = number of clauses, א). Confirm.
15. **22B-A Q13** (clean copy `סמסטר ב מועד א 22-6-22.pdf` p5): key = כן, but T accepts L(M1) Δ L(M2), so f(x) ∈ CE_TM ⇔ L(M1) = complement of L(M2), not ⇔ L(M1) ≠ L(M2). Kept the key at med confidence. Is the key right?
16. **20A-B Q21**: omitted (key says "none correct"; no such option).
17. **24B-A Q9** (`מבחנים/2024/סמסטר ב/מועד א פתרון מתוקן.pdf` ~p7): both ב and ד accepted (corrected key). Wording suggests ב was the original answer and ד was added. Both are accepted in the app.
18. **26B-A Q2** (`מבחנים/2026/…מועד א מעורבל עם תשובות.pdf` p2–3): nothing highlighted. א comes from the "הוכחת א" box, and a hand-trace of the diagram agrees. Confirm.
19. **26B-A Q23** (same file p14): the proof is headed "הוכחת א", but the highlight and the content are ג. Keyed ג. Options א (R⊂C) and ב (C⊃R) are equivalent as printed.
20. **SAMP-2 Q25** (`מבחנים לדוגמה/בחינה לדוגמה עם הסברים.pdf` p9 vs review deck slide 75): the PDF highlights only ד. The 2025 review deck highlights ג and ד ("כנראה שיש טעות, ושתי התשובות נכונות"). The app accepts both (confidence med). OK?
21. **SAMP-2 Q24**: the author's green note asks "האם לשנות את התשובה ???", and deck slide 71 says "יש מקום לענות 'לא נכון'". Kept נכון with confidence low.
22. **24A-A Q9** (`מבחנים/2024/סמסטר א/מועד א 21.3 פתרון.pdf` p6): the key is ב (A ⊂ B). But A = R includes ∅ and Σ*, which are not in B, so the containment looks doubtful. Kept the key at med confidence. Confirm?

## RESOLVED 2026-09-29 (Adir: "whatever you think is correct, mark as correct — make sure it's correct")
Each was re-derived mathematically; where the official key is wrong the question is marked
`answerSource: "solved"`, `official: false` (the app shows "תשובה לא רשמית") and the explanation
says what the official key was and why it's wrong.
- #11 **23A-B Q9 → א** (official ב). Within k steps M reads only the first k cells, so a finite check of all words of length ≤ k decides L. Back in the bank.
- #15 **22B-A Q13 → ב/לא** (official א). Under the printed CE_TM = {⟨M⟩ | complement(L(M)) = ∅}: L(T) = L1 Δ L2, and L1 Δ L2 = Σ* ⇔ L2 = complement(L1), not ⇔ L1 ≠ L2. Counterexample: {0} vs {1}.
- #22 **24A-A Q9 → ד** (official ב). A = R ∋ ∅, Σ*; B = the non-trivial languages ∌ ∅, Σ*; and H_TM ∈ B \ A. Neither inclusion holds.
- #12 23B-A Q14 (א), #14 23S-A Q20 (א), #18 26B-A Q2 (א, TM traced: all moves go right, so L = 0*11*01(0+1)*): verified, now high confidence.
- #20 SAMP-2 Q25: ג and ד are both true (only ∅ and Σ* in R are not R-complete) → both accepted, high.
- #21 SAMP-2 Q24: נכון kept (a k-1 cover pads to k; the doubt is only the degenerate |V| = k-1 case) → med.
- #10 23S-A (all 25 inferred from the highlighted explanations): consistent with that lecturer's form-0 = first option; kept.
- #7 20A-B Q21: stays omitted (no option is correct as printed).
- #17 24B-A Q9 and #19 26B-A Q23: already handled correctly.
- **Keyless sittings (#1–#6):** being solved with a two-stage blind cross-check; only agreements enter the bank, marked unofficial.

## RESOLVED — keyless sittings (2026-09-29)
Solved with the two-stage blind protocol (`tools/SOLVE_GUIDE.md`, audit trail `tools/raw/_verify_*.json`):
22B-B 18/20, 22B-C 16/20, 23B-B 25/25, 24B-B 18/18, 24S-A 18/18, 25A-A 16/18, 25B-C 18/18,
25S-B 18/18, SAMP-1 24/25 → 171 questions, all `official:false` (4 of them from other keys).
24B-B and 24S-A: stage 1, stage 2 and the form-0 first option all agree (36/36).
**Still out of the bank (9, ambiguous as printed — only a corrected official text could settle them):**
22B-B Q3 (no option always true without the chain condition), 22B-B Q5 (deterministic vs NTM reading),
22B-C Q4 (implication reading), Q13 (M1/M2 swapped in the box), Q17 (f undefined for even k),
Q20 (KSAT undefined), 25A-A Q13 (depends on P vs NP), Q14 (misprinted option ג),
SAMP-1 Q7 (empty-word edge case).
