# -*- coding: utf-8 -*-
"""Pronunciation lexicon for the computability videos: the shared machinery (tools/video/lexicon_base.py) plus the
course's own terms. Add a term here (never ad hoc in a script); check new entries by synthesizing them and
transcribing them back (vid.py --check runs that on whole scripts).

TeX is spoken token by token (TEX_TOKENS, longest first): a span with any token outside the table is refused, and
the script must give P(..., say=...). Variable letters are spoken by their English names in Hebrew letters (Latin letters are misread: R -> "מדר").

STT-checked 2026-10-30: M -> "אֵם" (with "אֶם", "של אֶם" merged into "שלהם"); coRE -> "קוֹאוּ אָר אִי" (heard CORE;
"קוֹ" alone was heard "קבוע"); coNP -> "קוֹ-אֶן-פִּי"; A_TM / H_TM in Hebrew letters (Latin "H T M" was heard "ATM").
כריעה / קריאה sound the same in spoken Hebrew: the recognizer writes קריאה, a listener hears the right word in context.
"""
import re
from lexicon_base import *          # noqa: F401,F403
from lexicon_base import WORDS, SYMBOL, base_tex_say

WORDS.update({
    "מ״ט": "מכונת טיורינג",
    "מ״ט אי-דטרמיניסטית": "מכונת טיורינג אי דטרמיניסטית",
})

# meaning-flipping mishearings to flag in the STT report: {what the recognizer wrote: what was said}
HOMOPHONES = {"שלא": "שלו", "הקלה": "הכלה", "לו": "לא"}

# TeX token -> spoken Hebrew. Order matters only through length (longest match first).
TEX_TOKENS = {
    r"A_{TM}": "אֵיי טִי אֶם", r"H_{TM}": "אֵייץ' טִי אֶם", r"E_{TM}": "אִי טִי אֶם", r"EQ_{TM}": "אִי קְיוּ טִי אֶם",
    r"ALL_{TM}": "אוֹל טִי אֶם", r"HALT_{TM}": "הוֹלְט טִי אֶם",
    r"q_{acc}": "קְיוּ אַקְסֶפְּט", r"q_{rej}": "קְיוּ רִיגֶ'קְט", r"q_{accept}": "קְיוּ אַקְסֶפְּט", r"q_{reject}": "קְיוּ רִיגֶ'קְט",
    r"coRE": "קוֹאוּ אָר אִי", r"coNP": "קוֹ-אֶן-פִּי", r"RE": "אָר אִי", r"NP": "אֶן פִּי", r"3SAT": "שָׁלוֹשׁ סַאט",
    r"SAT": "סַאט", r"CLIQUE": "קְלִיק", r"PATH": "פַּאת'",
    r"\le_m": "ניתנת לרדוקציה אל", r"\leq_m": "ניתנת לרדוקציה אל",
    r"\le_p": "ניתנת לרדוקציה פולינומית אל", r"\leq_p": "ניתנת לרדוקציה פולינומית אל",
    r"\notin": "לא שייכת ל", r"\in": "שייכת ל", r"\setminus": "פחות", r"\ne": "שונה מ", r"\neq": "שונה מ",
    r"\cup": "איחוד", r"\cap": "חיתוך", r"\subseteq": "מוכלת ב", r"\subsetneq": "מוכלת ממש ב",
    r"\sqcup": "רווח", r"\Sigma^*": "סיגמא כוכבית", r"\Sigma": "סיגמא", r"\Gamma": "גמא", r"\delta": "דלתא",
    r"\emptyset": "הקבוצה הריקה", r"\varnothing": "הקבוצה הריקה", r"\varepsilon": "אפסילון", r"\epsilon": "אפסילון",
    r"\to": "עובר ל", r"\rightarrow": "עובר ל", r"\Rightarrow": "גורר", r"\iff": "אם ורק אם",
    r"=": "שווה", r"<": "קטן מ", r">": "גדול מ", r"\le": "קטן או שווה ל", r"\ge": "גדול או שווה ל",
    r"\cdot": "כפול", r"+": "ועוד", r",": ",",
    "M": "אֵם", "L": "אֵל", "A": "אֵיי", "B": "בִּי", "C": "סִי", "D": "דִּי", "G": "גִ'י", "N": "אֶן", "P": "פִּי",
    "Q": "קְיוּ", "K": "קֵיי", "H": "אֵייץ'", "R": "אָר", "S": "אֶס", "T": "טִי", "U": "יוּ", "V": "וִי", "X": "אֶקְס", "Y": "וַואי", "Z": "זֶד", "W": "דַּאבְּלְיוּ",
    "f": "אֶף", "g": "גִ'י", "w": "דַּאבְּלְיוּ", "x": "אִקְס", "y": "וַואי", "z": "זֶד", "k": "קֵיי", "n": "אֶן",
    "m": "אֶם", "t": "טִי", "u": "יוּ", "v": "וִי", "s": "אֶס", "i": "אַיי", "j": "גֵ'יי",
}
for d, s in DIGIT.items():                       # noqa: F405
    TEX_TOKENS[d] = s
_TOK = sorted(TEX_TOKENS, key=len, reverse=True)


def _spell(t):
    """speak a TeX span token by token; None if a token is unknown"""
    t = t.replace(r"\,", " ").replace(r"\ ", " ").replace(r"\mathrm", "").replace(r"\text", "")
    out, i = [], 0
    t = re.sub(r"\\overline\{([^{}]+)\}", r"⟨overline⟩{\1}", t)
    while i < len(t):
        c = t[i]
        if c in " {}":
            i += 1
            continue
        if t.startswith("⟨overline⟩", i):
            out.append("המשלים של")
            i += len("⟨overline⟩")
            continue
        m = re.match(r"_\{?(\d+)\}?", t[i:])
        if m:                                    # M_1, q_0: the index as a number word
            out.append(" ".join(DIGIT[d] for d in m.group(1)))   # noqa: F405
            i += m.end()
            continue
        if c == "(" and out:                     # f(x), L(M): "של"
            out.append("של")
            i += 1
            continue
        if c == ")":
            i += 1
            continue
        hit = next((k for k in _TOK if t.startswith(k, i)), None)
        if hit is None:
            return None
        out.append(TEX_TOKENS[hit])
        i += len(hit)
    s = " ".join(out).replace(" ,", ",")
    s = re.sub(r"(^|\s)([לבמ])\s+", r"\1\2", s)      # "שייכת ל" + "אָר": one word, not the letter's name
    return re.sub(r"\s+", " ", s).strip() or None


def tex_say(tex):
    t = tex.strip()
    if re.fullmatch(r"q_\{?\d+\}?", t.replace(" ", "")):
        return base_tex_say(t)
    if re.fullmatch(r"[01]+", t):
        return word_say(t)                       # noqa: F405 — a word over {0,1}: digit by digit
    return _spell(t)
