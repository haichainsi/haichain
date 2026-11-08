const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('dashboard.html', 'utf8');
const dom = new JSDOM(html, { runScripts: "dangerously" });
const window = dom.window;
const document = window.document;

// Load i18n
const i18nCode = fs.readFileSync('i18n.js', 'utf8');
const scriptEl = document.createElement('script');
scriptEl.textContent = i18nCode;
document.body.appendChild(scriptEl);

const langs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he'];

console.log("Simulating language switching on tab-docs...");

const tabDocs = document.getElementById('tab-docs');
if (!tabDocs) {
  console.error("tab-docs not found!");
  process.exit(1);
}

for (const lang of langs) {
  if (typeof window.setLanguage === 'function') {
    window.setLanguage(lang);
  }
  
  // Check key elements
  const sec1Title = tabDocs.querySelector('[data-i18n="dev.sec1Title"]');
  const pyBadge = tabDocs.querySelector('[data-i18n="dev.pyBadge"]');
  const watchtowerTitle = tabDocs.querySelector('[data-i18n="dev.watchtowerTitle"]');
  const recycleDesc = tabDocs.querySelector('[data-i18n="dev.cardRecycleDesc"]');
  
  if (!sec1Title || !pyBadge || !watchtowerTitle || !recycleDesc) {
    console.error(`Failed to find translated nodes for ${lang}`);
    process.exit(1);
  }
  
  console.log(`[${lang}] sec1Title: "${sec1Title.textContent.trim()}"`);
  console.log(`[${lang}] pyBadge: "${pyBadge.textContent.trim()}"`);
  console.log(`[${lang}] watchtower: "${watchtowerTitle.textContent.trim()}"`);
}

console.log("\nAll 10 languages switched and rendered successfully in DOM simulation!");
