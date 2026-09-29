# Raw exam JSON — `tools/raw/<CODE>.json` (THE source of truth)

```jsonc
{
  "examCode": "26B-B",                 // YY[A|B|S]-[A|B|C] or SAMP-N
  "examLabel": "2026 סמסטר ב מועד ב",
  "year": 2026,
  "examDate": "8.7.2026",
  "sourceFile": "מבחנים/2026/…pdf",    // relative to the course folder
  "keyFile": "…",                      // where the answers came from
  "contexts": {                        // optional shared blocks; ids are local, build namespaces them <CODE>-<id>
    "tm1": { "kind": "image", "title": "…", "image": "images/exams/26B-B-tm1.png", "caption": "…" },
    "defs": { "kind": "text", "title": "…", "text": "rich text" }
  },
  "questions": [
    {
      "num": 1,
      "topic": "mapping_reductions",   // closed list, see below
      "question": "rich text",
      "contextId": "tm1",              // optional
      "image": "images/exams/26B-B-Q5.png", // optional per-question figure
      "options": [
        { "id": "a", "type": "text",  "value": "rich text" },   // ids a,b,c,d,e = printed א,ב,ג,ד,ה
        { "id": "b", "type": "math",  "value": "TeX without $" }, // whole option is one formula
        { "id": "c", "type": "image", "value": "images/exams/26B-B-Q7c.png" }
      ],
      "correctId": "c",
      "acceptedIds": ["c", "a"],       // only when >1 accepted (correctId first)
      "lockOrder": true,               // optional; build also auto-detects "א ו-ב" style refs
      "answerSource": "solution-pdf",  // solution-pdf | highlighted-pdf | corrected-key | letter-table | explanation-inferred | solved (derived + independently verified; official:false)
      "official": true,
      "confidence": "high",            // high | med | low
      "explanation": "rich text (Hebrew, from the key's proof box; may be empty)"
    }
  ]
}
```

## Rich text
- Inline math `$…$`, display math `$$…$$` — **TeX for KaTeX**, rendered to MathML at build time.
  **No Hebrew inside `$…$`** (split: `השפה $L$ ניתנת להכרעה`).
- `**bold**`, `` `code` `` (LTR), `\n` = line break. Literal `$` → `\$`.
- Roman-numeral claims (I / II) stay as plain text lines.

## Notation (character-exact, use these macros)
`\le_m`, `\le_p`, `\not\le_m`, `\not\le_p`, `\mathrm{R}`, `\mathrm{RE}`, `\mathrm{coRE}`,
`\mathrm{P}`, `\mathrm{NP}`, `\mathrm{coNP}`, `\mathrm{NPC}`, `A_{TM}`, `H_{TM}` / `HALT_{TM}`
(as printed), `E_{TM}`, `EQ_{TM}`, `\overline{L}`, `\langle M\rangle`, `\langle M,w\rangle`,
`\Sigma^*`, `O(n^2)`, `\in`, `\notin`, `\cap`, `\cup`, `\emptyset`.

## Topics (closed list — keep in sync: build_questions.py, validate.py, app.js, build_learn.py)
| key | label |
|---|---|
| tm | מכונות טיורינג, וריאנטים ומ"ט א"ד |
| decidability | כריעות וקבלה: R, RE, coRE |
| enumerators | אנומרטורים |
| undecidability | אי-כריעות: לכסון ובעיית העצירה |
| mapping_reductions | רדוקציות מיפוי (≤m) |
| closure | תכונות סגור |
| classification | סיווג שפות |
| time_p | סיבוכיות זמן והמחלקה P |
| np | המחלקה NP ו-coNP |
| poly_reductions | רדוקציות פולינומיות (≤p) |
| npc | NP-שלמות |

## Derived at build (do NOT put in raw)
`id` (`<CODE>-Q<num>`), `examCode`, `examLabel`, `year`, `source` (exam|sample), `topicLabel`,
`dedupKey`, auto-`lockOrder`, namespaced `contextId`, and the `*Html` fields
(`questionHtml`, option `html`, `explanationHtml`, context `textHtml`) with MathML.
