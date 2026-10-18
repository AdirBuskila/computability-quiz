# "צריך עזרה?" - plan

Every study app gets four guided courses (Adir's rule). Shell ported from `machine-learning-quiz`
(`course-ui.js`, `courses.js`, the level map / lesson / quiz / summary flow, progress per course in
`localStorage` with try/catch). Design: `course-factory/docs/superpowers/specs/2026-10-17-course-factory-design.md` section 3.4.

## Which four areas (from the bank, 592 questions, 11 topics)

| topic | questions |
|---|---|
| mapping_reductions | 142 |
| classification | 89 |
| poly_reductions | 84 |
| npc | 67 |
| decidability | 54 |
| tm | 46 |
| closure | 46 |
| time_p / np | 27 / 25 |
| undecidability / enumerators | 8 / 4 |

The guess (Turing machines, decidability/closure, mapping reductions, P/NP) matches the bank, grouped like this:

| course | id | topics | questions in bank | levels |
|---|---|---|---|---|
| 🔧 מכונות טיורינג | `tm` | tm, enumerators | 50 | T01-T07 |
| 🧮 כריעות, סגירות וסיווג | `dec` | decidability, undecidability, closure, classification | 197 | D01-D07 |
| 🔁 רדוקציות מיפוי | `map` | mapping_reductions | 142 | M01-M07 |
| 🧩 P, NP ו-NP-שלמות | `np` | time_p, np, poly_reductions, npc | 203 | N01-N08 |

Each course: lesson + 4-6 questions per level, last level is a 🏆 boss of six real bank questions pulled by id.
"Teach before you ask": a boss question is only used if an earlier lesson of the course teaches its idea; lessons cite
exam ids (they become peek buttons). Original questions use the main engine (`S.mode = "course"`), bank questions are
cloned from the bank by `ref`.

## Authoring and build

- Sources: `tools/courses_src/<course>/<ID>.js` (`CC_LEVEL(...)`); math as `$TeX$`, no Hebrew inside math.
- `node tools/build_courses.js` renders TeX to MathML (KaTeX, like the bank) and writes `courses/<course>/<ID>.js`
  (generated, do not edit). `node tools/course_check.js --sync` lints them and writes the script tags into `index.html`.
- All text goes through `rich()` in `course-ui.js` -> `bidi.js` (formulas keep their LTR order), exam ids become peek
  buttons, and the per-question report link (`feedback.js`) is shown on course questions too.

## Machine checks (`tools/verify/needhelp/<course>/check.py`, run with `PYTHONUTF8=1 py ...`)

| course | what is machine-checked |
|---|---|
| `tm` | every printed transition table is parsed and SIMULATED: final tape, step count, accept/reject/loop, language of the machine (all words up to length 8), "does it halt on everything"; configuration counts and exponents recomputed |
| `dec` | every closure option goes through a closure engine (sound propagation of R/RE/coRE flags + a 4-language Boolean model as counterexample finder); named-language classes and "shape of the condition" classes against a rule table; definitional facts against `rules.py` |
| `map` | toy reductions brute-forced on all binary words up to length 10 (both directions separately); trivial-language facts (empty, Sigma*, complement, composition) brute-forced over all subsets of a 2-3 word universe; impossible reductions by class monotonicity; `K_{M,w}` and `R_{M,w}` by simulating the printed machine |
| `np` | CLIQUE<->IS, IS->VC, 3SAT->IS, 3SAT->CLIQUE verified on hundreds of random instances; broken or valid gadgets (`G,k,1`, doubled graph, parity fix) found by brute force; edge counts and max independent set of the printed formulas computed; open-problem statements against `rules.py` |

Each check demands that the keyed option is true and that no other option is (one defensible answer).

## Blind review and tests

After authoring, every course question was re-solved cold from its text and options (answers written down before opening
the keys) and compared to the keys; disagreements fixed. Then: `node tools/smoke.js`, `node tools/verify_dom.js`,
`node tools/course_check.js`, `node tools/course_flow.js all light mobile`, and `course-factory/scripts/render_audit.js`
on the app (0 findings), screenshots at 390px.
