// Headless DOM test (jsdom, no browser):  node tools/verify_dom.js
// Boots index.html + questions.js + learn.js + app.js, then:
//   - empty bank  -> asserts the app degrades gracefully (start disabled, empty-state shown)
//   - non-empty   -> starts a practice session and answers it; starts a full-exam session,
//                    answers every question BY ID, submits and expects 100%; asserts every
//                    <math> reaching the DOM has dir="ltr", lockOrder questions keep source
//                    order, Hebrew-free options are dir="ltr", and no JS errors occurred.
//   - learn.js    -> every .qref resolves to a bank id (dangling = FAIL), every .xref to a chapter,
//                    learn <math> is dir=ltr; walks all chapters, opens a peek, follows an xref,
//                    starts a drill. A topic chapter with 0 bank questions only WARNs.
const fs = require("fs"), path = require("path");
const { JSDOM, VirtualConsole } = require("jsdom");

const ROOT = process.env.APP_ROOT || path.join(__dirname, "..");   // APP_ROOT: test a copy (e.g. an empty bank)
const errors = [];
const vc = new VirtualConsole();
vc.on("jsdomError", e => errors.push("jsdomError: " + (e.message || e)));
vc.on("error", (...a) => errors.push("console.error: " + a.join(" ")));

const html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
const dom = new JSDOM(html, { pretendToBeVisual: true, runScripts: "outside-only", url: "http://localhost/index.html", virtualConsole: vc });
const { window } = dom;
window.scrollTo = () => {};
window.matchMedia = window.matchMedia || (q => ({ matches: false, media: q, addEventListener() {}, removeEventListener() {}, addListener() {}, removeListener() {} }));
window.HTMLElement.prototype.scrollIntoView = () => {};
window.confirm = () => true;
window.addEventListener("error", e => errors.push("window.onerror: " + e.message));

// load scripts in index.html order (only local ones; analytics is skipped)
const scripts = [...window.document.querySelectorAll("script[src]")]
  .map(s => s.getAttribute("src")).filter(s => !/^(https?:)?\/\//.test(s)).map(s => s.split("?")[0]);
for (const f of scripts) {
  try { window.eval(fs.readFileSync(path.join(ROOT, f), "utf8")); }
  catch (e) { errors.push(`eval ${f}: ${e.message}`); }
}

const doc = window.document, $ = s => doc.querySelector(s), $$ = s => [...doc.querySelectorAll(s)];
let fail = 0;
function assert(cond, msg) { console.log((cond ? "  ok  " : "FAIL  ") + msg); if (!cond) fail++; }
const visible = el => el && !el.classList.contains("hidden");
function mathAllLtr(where) {
  const ms = $$("math");
  const bad = ms.filter(m => m.getAttribute("dir") !== "ltr");
  assert(bad.length === 0, `${where}: all ${ms.length} <math> have dir="ltr"`);
  return ms.length;
}
function setMode(mode) {
  const r = $(`input[name=mode][value="${mode}"]`); r.checked = true;
  r.dispatchEvent(new window.Event("change", { bubbles: true }));
}

assert(scripts.join() === "questions.js,learn.js,app.js", `scripts loaded: ${scripts.join(", ")}`);
const D = window.CC_QUIZ;
assert(D && Array.isArray(D.questions), "window.CC_QUIZ defined");
const QS = D.questions;
const learnCh = Array.isArray(window.LEARN) ? window.LEARN : ((window.LEARN || {}).chapters || []);
assert($$("#topicGrid .topic-btn").length === 12, `topic buttons: ${$$("#topicGrid .topic-btn").length} (11 topics + all)`);
assert(doc.documentElement.getAttribute("dir") === "rtl", "page is dir=rtl");
if (!learnCh.length) assert($("#learnEntry").style.display === "none", "learn entry hidden (no chapters)");
else assert($("#learnEntry").style.display !== "none", "learn entry visible");

if (!QS.length) {
  // ---------------- empty bank ----------------
  assert(visible($("#screen-start")), "start screen shown");
  assert($("#startBtn").disabled, "start disabled on empty bank");
  assert(!!$("#emptyState"), "empty-state message shown");
  assert(/ריק/.test($("#poolInfo").textContent), "pool info says the bank is empty");
  $("#startBtn").click();
  assert(!visible($("#screen-quiz")), "clicking start does nothing");
  setMode("exam");
  assert(visible($("#examOpts")) && $$("#examPick option").length === 1, "exam picker has only 'random'");
} else {
  // ---------------- practice ----------------
  $("#startBtn").click();
  assert(visible($("#screen-quiz")), "practice: quiz screen shown");
  assert($("#questionText").innerHTML.trim().length > 0, "practice: question rendered");
  let opts = $$("#optionsList .opt");
  assert(opts.length >= 2, `practice: options rendered: ${opts.length}`);
  mathAllLtr("practice question");
  // answer with a WRONG option when possible, to see both .wrong and .correct marking
  const cur = () => QS.find(x => x.id === $("#questionText").dataset.qid);
  let q = cur();
  assert(!!q, `practice: rendered question identified (${q && q.id})`);
  const acc = q.acceptedIds || [q.correctId];
  const wrongBtn = opts.find(b => !acc.includes(b.dataset.oid)) || opts[0];
  wrongBtn.click();
  assert(visible($("#feedback")), "practice: feedback shown after answering");
  assert(opts.filter(b => b.classList.contains("correct")).length === acc.length,
    `practice: ${acc.length} accepted option(s) marked correct`);
  assert(opts.filter(b => b.classList.contains("correct")).every(b => acc.includes(b.dataset.oid)),
    "practice: marked-correct options are exactly the accepted ids");
  assert(/לא נכון/.test($("#feedback .verdict").textContent) === !acc.includes(wrongBtn.dataset.oid), "practice: verdict matches id grading");
  mathAllLtr("practice feedback");
  // walk the whole pool once, answering correctly by id
  const seen = new Set([q.id]);
  for (let i = 1; i < QS.length * 2; i++) {
    $("#nextBtn").click();
    opts = $$("#optionsList .opt"); q = cur();
    if (!q) { assert(false, "practice: could not identify question"); break; }
    seen.add(q.id);
    opts.find(b => b.dataset.oid === q.correctId).click();
    if (!/✓/.test($("#feedback .verdict").textContent)) { assert(false, `practice: correct id graded wrong on ${q.id}`); break; }
    mathAllLtr(`practice ${q.id}`);
  }
  $("#quitBtn").click();
  assert(visible($("#screen-start")), "quit returns to start");

  // ---------------- full exam ----------------
  setMode("exam");
  const codes = $$("#examPick option").map(o => o.value).filter(Boolean);
  assert(codes.length >= 1, `exam picker lists ${codes.length} exam(s)`);
  const code = codes[0];
  $("#examPick").value = code; $("#examPick").dispatchEvent(new window.Event("change"));
  const paper = QS.filter(x => x.examCode === code).sort((a, b) => a.num - b.num);
  $("#startBtn").click();
  assert(visible($("#screen-quiz")) && /⏱|שאלה 1\//.test($("#quizMeta").textContent), "exam: session started with timer");
  for (let i = 0; i < paper.length; i++) {
    const pq = paper[i];
    opts = $$("#optionsList .opt");
    const shown = opts.map(b => b.dataset.oid);
    if (pq.lockOrder) assert(shown.join() === pq.options.map(o => o.id).join(), `exam: lockOrder ${pq.id} keeps source order`);
    assert(shown.slice().sort().join() === pq.options.map(o => o.id).sort().join(), `exam: ${pq.id} shows its own options`);
    for (const o of pq.options) {
      const b = opts.find(x => x.dataset.oid === o.id);
      if (o.type === "text" && !/[֐-׿]/.test(o.value))
        assert(!!b.querySelector('.opt-ltr[dir="ltr"]'), `exam: Hebrew-free option ${pq.id}/${o.id} is dir=ltr`);
      if (o.type === "image") assert(!!b.querySelector("img.opt-img"), `exam: image option ${pq.id}/${o.id} rendered`);
    }
    if (pq.contextId) assert(!!$("#qContext .ctx"), `exam: context block shown for ${pq.id}`);
    if (pq.image) assert(!!$("#qExtras img.q-img"), `exam: figure shown for ${pq.id}`);
    mathAllLtr(`exam ${pq.id}`);
    opts.find(b => b.dataset.oid === pq.correctId).click();
    assert(opts.find(b => b.dataset.oid === pq.correctId).classList.contains("chosen-exam"), `exam: choice marked on ${pq.id}`);
    if (i < paper.length - 1) $("#nextBtn").click();
  }
  // back-navigation keeps the same shuffle
  if (paper.length > 1) {
    const before = $$("#optionsList .opt").map(b => b.dataset.oid).join();
    $("#prevBtn").click(); $("#nextBtn").click();
    assert($$("#optionsList .opt").map(b => b.dataset.oid).join() === before, "exam: shuffle stable across back/next");
  }
  // lightbox on a figure, if any
  const img = $(".q-img");
  if (img) { img.click(); assert(visible($("#lightbox")), "lightbox opens on figure click"); $("#lightboxClose").click(); }
  $("#submitExamBtn").click();
  assert(visible($("#screen-results")), "exam: results shown");
  assert($("#resultsSummary").textContent.includes(`${paper.length} / ${paper.length}`), `exam: scored ${paper.length}/${paper.length} answering by id`);
  mathAllLtr("results review");
  $("#backHomeBtn").click();
}

// ---------------- learn mode (learn.js from tools/build_learn.py) ----------------
if (learnCh.length) {
  const TOPIC_KEYS = new Set($$("#topicGrid .topic-btn").map(b => b.dataset.topic).filter(t => t !== "all"));
  const qids = new Set(QS.map(q => q.id));
  const chIds = learnCh.map(c => c.id);
  assert(new Set(chIds).size === chIds.length && chIds.every(Boolean), `learn: ${chIds.length} chapters, unique ids`);
  assert(learnCh.every(c => c.title && c.html), "learn: every chapter has a title and html");
  const badTopic = learnCh.filter(c => c.topic && !TOPIC_KEYS.has(c.topic)).map(c => c.id);
  assert(badTopic.length === 0, `learn: chapter topics are in the closed topic list${badTopic.length ? " BAD: " + badTopic : ""}`);
  const covered = new Set(learnCh.filter(c => c.kind !== "cheat").map(c => c.topic));
  const uncovered = [...TOPIC_KEYS].filter(t => !covered.has(t));
  assert(uncovered.length === 0, `learn: every topic has a brief${uncovered.length ? " MISSING: " + uncovered : ""}`);
  // dangling question refs would open an empty peek -> hard failure
  const dangling = [], deadX = [], mathBad = [];
  let nRefs = 0, nMath = 0;
  for (const c of learnCh) {
    const frag = doc.createElement("div"); frag.innerHTML = c.html;
    for (const b of frag.querySelectorAll(".qref")) { nRefs++; if (!qids.has(b.dataset.q)) dangling.push(`${c.id}:${b.dataset.q}`); }
    for (const a of frag.querySelectorAll(".xref")) if (!chIds.includes(a.dataset.chapter)) deadX.push(`${c.id}->${a.dataset.chapter}`);
    for (const m of frag.querySelectorAll("math")) { nMath++; if (m.getAttribute("dir") !== "ltr" || /[֐-׿]/.test(m.textContent)) mathBad.push(c.id); }
  }
  assert(dangling.length === 0, `learn: all ${nRefs} question refs resolve${dangling.length ? " DANGLING: " + dangling.join(", ") : ""}`);
  assert(deadX.length === 0, `learn: all cross-references resolve${deadX.length ? " DEAD: " + deadX.join(", ") : ""}`);
  assert(mathBad.length === 0, `learn: all ${nMath} <math> are dir=ltr with no Hebrew${mathBad.length ? " BAD in: " + [...new Set(mathBad)] : ""}`);
  // a topic chapter with no questions yet is allowed (the bank grows) -> warning only
  for (const c of learnCh) if (c.kind !== "cheat" && c.topic && !QS.some(q => q.topic === c.topic))
    console.log(`WARN  learn: chapter "${c.id}" (topic ${c.topic}) has 0 questions in the bank`);

  // UI walk
  $("#learnEntry").click();
  assert(visible($("#screen-learn")), "learn: screen opens from the entry button");
  assert($$("#learnToc button").length === learnCh.length, `learn: TOC lists ${learnCh.length} chapters`);
  const seenCh = [];
  for (let i = 0; i < learnCh.length; i++) {
    seenCh.push($("#learnContent").dataset.chapter);
    if (!$("#learnContent .learn-h")) { assert(false, `learn: chapter ${i} has no heading`); break; }
    const t = learnCh[i].topic, n = t ? QS.filter(q => q.topic === t).length : 0;
    if (n && !$("#learnContent .learn-drill")) assert(false, `learn: chapter ${learnCh[i].id} missing drill button`);
    if (i < learnCh.length - 1) $("#learnNext").click();
  }
  assert(seenCh.join() === chIds.join(), "learn: next-button walk visits every chapter in order");
  assert($("#learnNext").disabled, "learn: next disabled on the last chapter");
  // peek: first chapter with a ref
  const withRef = learnCh.findIndex(c => /class="qref"/.test(c.html));
  if (withRef >= 0) {
    $$("#learnToc button")[withRef].click();
    // peek at a ref that resolves (dangling ones already failed above)
    const ref = $$("#learnContent .qref").find(b => qids.has(b.dataset.q)) || $("#learnContent .qref");
    ref.click();
    assert(visible($("#qpeek")), `learn: clicking ${ref.dataset.q} opens the peek`);
    const pq = QS.find(q => q.id === ref.dataset.q) || { options: [], correctId: null };
    const acc = pq.acceptedIds || [pq.correctId];
    const right = $$("#qpeekBody .qpeek-opts li.right").map(li => li.dataset.oid);
    assert(right.length === acc.length && right.every(id => acc.includes(id)), "learn: peek marks exactly the accepted option(s)");
    assert($$("#qpeekBody .qpeek-opts li").map(li => li.dataset.oid).join() === pq.options.map(o => o.id).join(), "learn: peek keeps source option order");
    mathAllLtr("learn peek");
    doc.dispatchEvent(new window.KeyboardEvent("keydown", { key: "Escape", bubbles: true }));
    assert(!visible($("#qpeek")) && visible($("#screen-learn")), "learn: Escape closes the peek, stays in learn");
  }
  // xref jump
  const withX = learnCh.findIndex(c => /class="xref"/.test(c.html));
  if (withX >= 0) {
    $$("#learnToc button")[withX].click();
    const x = $("#learnContent .xref");
    x.click();
    assert($("#learnContent").dataset.chapter === x.dataset.chapter, `learn: xref jumps to ${x.dataset.chapter}`);
  }
  // drill button -> practice session on that topic
  const drillIdx = learnCh.findIndex(c => c.topic && QS.some(q => q.topic === c.topic));
  if (drillIdx >= 0) {
    $$("#learnToc button")[drillIdx].click();
    $("#learnContent .learn-drill").click();
    const shown = QS.find(q => q.id === $("#questionText").dataset.qid);
    assert(visible($("#screen-quiz")) && shown && shown.topic === learnCh[drillIdx].topic, `learn: drill starts a ${learnCh[drillIdx].topic} practice session`);
    $("#quitBtn").click();
  }
  assert(errors.length === 0, `learn: no JS errors so far${errors.length ? ": " + errors.join(" | ") : ""}`);
}

// images referenced anywhere must exist
const refs = [];
for (const q of QS) { if (q.image) refs.push(q.image); for (const o of q.options) if (o.type === "image") refs.push(o.value); }
for (const c of Object.values(D.contexts || {})) if (c.image) refs.push(c.image);
const missing = refs.filter(r => !fs.existsSync(path.join(ROOT, r)));
assert(missing.length === 0, `all ${refs.length} image refs exist${missing.length ? " MISSING: " + missing.join(", ") : ""}`);

assert(errors.length === 0, `no JS errors${errors.length ? ":\n    " + errors.join("\n    ") : ""}`);
console.log(fail === 0 ? "\nDOM VERIFY PASSED" : `\nDOM VERIFY FAILED (${fail})`);
process.exit(fail === 0 ? 0 : 1);
