// Guided courses ("צריך עזרה?"): tools/courses_src/<course>/<ID>.js  ->  courses/<course>/<ID>.js
//
//   node tools/build_courses.js                 build every level file (needs tools/node_modules/katex)
//   node tools/build_courses.js --export FILE   also write the RAW levels (TeX kept as $..$, chk kept) as JSON,
//                                               for the checkers in tools/verify/needhelp/<course>/check.py
//
// The sources are plain JS calling CC_LEVEL("<course>", {...}). Inside any string, $...$ is inline TeX and
// $$...$$ display TeX; they are rendered to MathML here (KaTeX, output:"mathml") exactly like the bank's
// questions, so the site ships no math code. No Hebrew inside $...$. The optional `chk` field on a question is
// machine-check metadata for the Python checkers; it is stripped from the shipped files.
const fs = require("fs"), path = require("path"), vm = require("vm");
const ROOT = path.join(__dirname, "..");
const SRC = path.join(__dirname, "courses_src");
const OUT = path.join(ROOT, "courses");
const katex = require(path.join(__dirname, "node_modules", "katex"));
const HEB = /[֐-׿]/;
const COURSES = ["tm", "dec", "map", "np"];

let bad = 0; const err = (...a) => { console.log("ERROR", ...a); bad++; };

// Chrome's MathML Core draws KaTeX's \overline (<mover>+U+203E) as a stub; rewrite to <mrow class="ovl">
function fixOverlines(m){
  const OPEN = '<mover accent="true">', TAIL = '<mo stretchy="true">‾</mo></mover>';
  const starts = []; let i = m.indexOf(OPEN);
  while (i !== -1) { starts.push(i); i = m.indexOf(OPEN, i + 1); }
  for (const st of starts.reverse()) {
    let depth = 0, j = st;
    for (;;) {
      const o = m.indexOf("<mover", j), c = m.indexOf("</mover>", j);
      if (c === -1) return m;
      if (o !== -1 && o < c) { depth++; j = o + 6; } else { depth--; j = c + 8; if (!depth) break; }
    }
    const seg = m.slice(st, j);
    if (seg.endsWith(TAIL)) m = m.slice(0, st) + '<mrow class="ovl">' + seg.slice(OPEN.length, seg.length - TAIL.length) + "</mrow>" + m.slice(j);
  }
  return m;
}
const cache = new Map();
function render(tex, display, where){
  const key = (display ? "D" : "I") + tex;
  if (cache.has(key)) return cache.get(key);
  if (HEB.test(tex)) err(where, "Hebrew inside math:", tex);
  let h = "";
  try {
    let s = katex.renderToString(tex, { output: "mathml", displayMode: !!display, throwOnError: true, strict: false });
    const m = s.match(/<math[\s\S]*<\/math>/); if (!m) throw new Error("no <math> in KaTeX output");
    s = fixOverlines(m[0].replace(/^<math /, '<math dir="ltr" '));
    h = `<span class="math-${display ? "block" : "inline"}">${s}</span>`;
  } catch (e) { err(where, "TeX error in", JSON.stringify(tex), String(e.message).slice(0, 120)); h = "[TeX error]"; }
  cache.set(key, h);
  return h;
}

const PH = /(\d+)/g;
function loadSource(file){
  const maths = [];
  let text = fs.readFileSync(file, "utf8").replace(/\r\n/g, "\n");
  // display first, then inline; TeX never contains a newline (inline) so a stray $ is caught below
  text = text.replace(/\$\$([\s\S]+?)\$\$/g, (m, t) => { maths.push({ tex: t.trim().replace(/\\\\/g, "\\"), display: true }); return `${maths.length - 1}`; });
  text = text.replace(/\$([^$\n]+?)\$/g, (m, t) => { maths.push({ tex: t.trim().replace(/\\\\/g, "\\"), display: false }); return `${maths.length - 1}`; });
  const levels = [];
  const ctx = { CC_LEVEL: (cid, level) => levels.push([cid, level]) };
  vm.createContext(ctx);
  vm.runInContext(text, ctx, { filename: file });
  return { levels, maths };
}
const walk = (v, f) => Array.isArray(v) ? v.map(x => walk(x, f)) : (v && typeof v === "object") ? Object.fromEntries(Object.entries(v).map(([k, x]) => [k, walk(x, f)])) : typeof v === "string" ? f(v) : v;

const args = process.argv.slice(2);
const exportTo = args.includes("--export") ? args[args.indexOf("--export") + 1] : null;
const rawAll = [];
let nFiles = 0, nMath = 0;
for (const cid of COURSES) {
  const dir = path.join(SRC, cid);
  if (!fs.existsSync(dir)) continue;
  fs.mkdirSync(path.join(OUT, cid), { recursive: true });
  const made = new Set();
  for (const f of fs.readdirSync(dir).filter(f => /\.js$/.test(f)).sort()) {
    const where = `${cid}/${f}`;
    let src;
    try { src = loadSource(path.join(dir, f)); } catch (e) { err(where, "cannot load:", e.message); continue; }
    if (src.levels.length !== 1) { err(where, "must call CC_LEVEL exactly once"); continue; }
    const [lcid, level] = src.levels[0];
    if (lcid !== cid) err(where, `CC_LEVEL course "${lcid}" != folder "${cid}"`);
    if (level.id + ".js" !== f) err(where, `level id ${level.id} != file name`);
    const raw = walk(level, s => s.replace(PH, (m, i) => (src.maths[+i].display ? "$$" : "$") + src.maths[+i].tex + (src.maths[+i].display ? "$$" : "$")));
    rawAll.push({ course: cid, level: raw });
    const built = walk(level, s => {
      const out = s.replace(PH, (m, i) => { nMath++; return render(src.maths[+i].tex, src.maths[+i].display, where + " " + level.id); });
      const rest = out.replace(/<math[\s\S]*?<\/math>/g, "[M]");
      if (/\$/.test(rest)) err(where, "stray $ in:", rest.slice(0, 100));
      return out;
    });
    (built.questions || []).forEach(q => { delete q.chk; });
    const text = `/* GENERATED by tools/build_courses.js from tools/courses_src/${cid}/${f} - edit the source, not this file. */\n` +
      `CC_LEVEL(${JSON.stringify(cid)}, ${JSON.stringify(built, null, 1)});\n`;
    fs.writeFileSync(path.join(OUT, cid, f), text);
    made.add(f); nFiles++;
  }
  // drop stale built files whose source is gone
  for (const f of fs.readdirSync(path.join(OUT, cid))) if (/\.js$/.test(f) && !made.has(f)) { fs.unlinkSync(path.join(OUT, cid, f)); console.log("removed stale", `${cid}/${f}`); }
}
if (exportTo) { fs.mkdirSync(path.dirname(path.resolve(exportTo)), { recursive: true }); fs.writeFileSync(exportTo, JSON.stringify(rawAll, null, 1)); }
console.log(`built ${nFiles} level files, ${nMath} math spans${exportTo ? ", exported raw to " + exportTo : ""}`);
if (bad) { console.log(`BUILD FAILED: ${bad} error(s)`); process.exit(1); }
