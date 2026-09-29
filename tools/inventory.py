# -*- coding: utf-8 -*-
"""Phase-1 inventory: page count, text-layer size, yellow-highlight annots per file.
Usage: PYTHONUTF8=1 py tools/inventory.py > tools/raw/inventory.tsv"""
import os, sys, fitz
SRC = r"C:\Users\Adir\Desktop\BSC\שנה ג\חישוביות וסיבוכיות"
DIRS = ["מבחנים", "חומרים אחרים", "בחנים במודל", "מצגות חזרה למבחן"]
def dec(p):
    try: return p.encode("cp437").decode("cp862") if "חומרים אחרים" in p else p
    except Exception: return p
print("path\tdecoded\tpages\ttextchars\tchars_p1\thighlights\timages_p1")
for d in DIRS:
    for r, _, fs in os.walk(os.path.join(SRC, d)):
        for f in sorted(fs):
            fp = os.path.join(r, f); rel = os.path.relpath(fp, SRC)
            if not f.lower().endswith(".pdf"):
                print(f"{rel}\t{dec(rel)}\t-\t-\t-\t-\t-"); continue
            try:
                doc = fitz.open(fp)
                txt = [p.get_text() for p in doc]
                hl = sum(1 for p in doc for a in (p.annots() or []) if a.type[1] in ("Highlight",))
                print(f"{rel}\t{dec(rel)}\t{doc.page_count}\t{sum(len(t.strip()) for t in txt)}\t{len(txt[0].strip())}\t{hl}\t{len(doc[0].get_images())}")
            except Exception as e:
                print(f"{rel}\t{dec(rel)}\tERR {e}")
