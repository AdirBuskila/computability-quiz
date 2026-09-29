# -*- coding: utf-8 -*-
"""Generator for tools/raw/SAMP-1.json. Source: `מבחנים/מבחנים לדוגמה/ בחינה לדוגמה.pdf`
(25 Q, NO key). Only the questions that appear VERBATIM (same stem AND same options, same
order) in SAMP-3 (`פתרון מבחן לדוגמא.pdf`, which has a key) are included; their key and
explanation are taken from SAMP-3 by content. Everything else is skipped (see SKIPPED).
Depends on tools/raw/SAMP-3.json -> run gen_SAMP-3.py first.
Run: PYTHONUTF8=1 py tools/gen/gen_SAMP-1.py"""
import json, pathlib, copy

RAW = pathlib.Path(__file__).resolve().parents[1] / "raw"
OUT = RAW / "SAMP-1.json"
s3 = json.loads((RAW / "SAMP-3.json").read_text(encoding="utf-8"))
S3 = {q["num"]: q for q in s3["questions"]}

# SAMP-1 num -> SAMP-3 num (checked on the rendered pages: stem, options and option order identical)
MAP = {13: 6, 14: 7, 15: 8, 16: 9, 23: 1, 24: 13, 25: 12}
SKIPPED = {
    "1-6": "true/false block, not in SAMP-3 (no key)",
    "7-9": "classification, not in SAMP-3 (no key)",
    "10-12": "relations with different definitions than SAMP-3 (A = L(M) finite, ...) - no key",
    "17-19": "ZSAT reduction block, not in SAMP-3 (no key)",
    "20": "not in SAMP-3 (no key)",
    "21": "variant of SAMP-3 Q2 but options differ (4 options, no 'בהכרח מתקיים', no 'כל התשובות נכונות') - not verbatim",
    "22": "not in SAMP-3 (no key)",
}

questions = []
for n1, n3 in MAP.items():
    q = copy.deepcopy(S3[n3])
    q["num"] = n1
    q["answerSource"] = "solution-pdf"
    q["official"] = True
    q["confidence"] = "high"
    q["note"] = f"key from SAMP-3 Q{n3} (identical stem and options in `פתרון מבחן לדוגמא.pdf`)."
    questions.append(q)

contexts = {}
ctx = copy.deepcopy(s3["contexts"]["map"])
ctx["title"] = "רדוקציית מיפוי (שאלות 13–16)"
ctx["text"] = ctx["text"].replace("**ענה על השאלות הבאות**", "**יש לענות על השאלות הבאות**")
contexts["map"] = ctx

exam = {
  "examCode": "SAMP-1",
  "examLabel": "מבחן לדוגמה 1",
  "year": 2022,
  "sourceFile": "מבחנים/מבחנים לדוגמה/ בחינה לדוגמה.pdf",
  "keyFile": "no own key; keys/explanations from מבחנים/מבחנים לדוגמה/פתרון מבחן לדוגמא.pdf (SAMP-3) by identical content",
  "contexts": contexts,
  "questions": sorted(questions, key=lambda q: q["num"]),
}
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(exam["questions"]), "questions; skipped:", ", ".join(SKIPPED))
