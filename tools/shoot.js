// Screenshot driver (puppeteer-core + local Chrome):  node tools/shoot.js
// Opens index.html over file:// (no server needed) at 390px (mobile) and 1000px (desktop)
// in both themes, and captures: start screen, every question of the first exam in
// full-exam mode, a practice question after answering, and the exam results.
// Also fails if any screen overflows horizontally (the mobile guard).
// Env: EXAM=<code> picks the paper (default: first in the picker), MAX_Q caps shots per paper.
// Output: tools/raw/shots/<viewport>-<theme>-NN-<name>.png
const puppeteer = require("puppeteer-core");
const path = require("path"), fs = require("fs"), url = require("url");

const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe";
const APP = process.env.APP_URL || url.pathToFileURL(path.join(__dirname, "..", "index.html")).href;
const OUT = path.join(__dirname, "raw", "shots");
const MAX_Q = +(process.env.MAX_Q || 6);
fs.mkdirSync(OUT, { recursive: true });
const sleep = ms => new Promise(r => setTimeout(r, ms));

const VIEWPORTS = [
  ["m390", { width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true }],
  ["d1000", { width: 1000, height: 900, deviceScaleFactor: 1 }],
];
const THEMES = ["dark", "light"];

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new",
    args: ["--no-sandbox", "--force-color-profile=srgb", "--hide-scrollbars", "--allow-file-access-from-files"] });
  const errors = [], overflow = [];
  for (const [vpName, vp] of VIEWPORTS) for (const theme of THEMES) {
    const page = await browser.newPage();
    page.on("pageerror", e => errors.push(`${vpName}/${theme} PAGEERROR: ${e.message}`));
    page.on("console", m => { if (m.type() === "error" && !/goatcounter|gc\.zgo\.at|ERR_/.test(m.text())) errors.push(`${vpName}/${theme} CONSOLE: ${m.text()}`); });
    page.on("dialog", d => d.accept());
    await page.setViewport(vp);
    await page.evaluateOnNewDocument(t => { try { localStorage.setItem("ccq_theme", t); } catch (e) {} }, theme);
    await page.goto(APP, { waitUntil: "load" });
    let n = 0;
    const shot = async name => {
      await sleep(250);
      const ov = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      if (ov > 1) overflow.push(`${vpName}/${theme}/${name}: +${ov}px`);
      const f = `${vpName}-${theme}-${String(++n).padStart(2, "0")}-${name}.png`;
      await page.screenshot({ path: path.join(OUT, f), fullPage: true });
      console.log("shot:", f);
    };
    await shot("start");
    const nq = await page.evaluate(() => (window.CC_QUIZ.questions || []).length);
    if (nq) {
      // full exam of the first paper: every question in printed order
      await page.click('input[name=mode][value="exam"]');
      const code = process.env.EXAM || await page.evaluate(() => { const o = [...document.querySelectorAll("#examPick option")].find(x => x.value); return o && o.value; });
      await page.select("#examPick", code);
      await page.click("#startBtn");
      const total = await page.evaluate(c => window.CC_QUIZ.questions.filter(q => q.examCode === c).length, code);
      for (let i = 0; i < total; i++) {
        if (i < MAX_Q) await shot(`exam-q${i + 1}`);
        await page.click('#optionsList .opt[data-disp="0"]');
        if (i < total - 1) await page.click("#nextBtn");
      }
      await page.click("#submitExamBtn");
      await shot("results");
      await page.click("#backHomeBtn");
      // practice: answer the first question shown with display slot 0
      await page.click('input[name=mode][value="practice"]');
      await page.click("#startBtn");
      await page.click('#optionsList .opt[data-disp="0"]');
      await shot("practice-answered");
    }
    await page.close();
  }
  await browser.close();
  console.log("\noverflow:", overflow.length ? overflow : "none");
  console.log("errors:", errors.length ? errors : "none");
  process.exit(errors.length || overflow.length ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
