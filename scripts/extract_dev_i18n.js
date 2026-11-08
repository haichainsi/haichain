const fs = require('fs');

const content = fs.readFileSync('i18n.js', 'utf8');

const sandbox = {
  window: {
    addEventListener: () => {},
  },
  document: {
    addEventListener: () => {},
    documentElement: { setAttribute: () => {} },
    querySelectorAll: () => [],
    querySelector: () => null,
    getElementById: () => null,
  },
  navigator: { language: 'en' },
  localStorage: { getItem: () => null, setItem: () => {} }
};
sandbox.window.document = sandbox.document;
sandbox.window.localStorage = sandbox.localStorage;

const fn = new Function('window', 'document', 'navigator', 'localStorage', content);
fn(sandbox.window, sandbox.document, sandbox.navigator, sandbox.localStorage);

const translations = sandbox.window.haichainTranslations;
if (!translations) {
  console.log("Could not find haichainTranslations");
  process.exit(1);
}

const langs = Object.keys(translations);
console.log("Found languages:", langs);

const devKeys = new Set();
for (const lang of langs) {
  for (const k of Object.keys(translations[lang])) {
    if (k.startsWith('dev.') || k.startsWith('mcp.') || k.startsWith('nav.devHub')) {
      devKeys.add(k);
    }
  }
}

console.log("\nUnique dev.*, mcp.*, nav.devHub keys count:", devKeys.size);

const report = {};
for (const k of Array.from(devKeys).sort()) {
  report[k] = {};
  for (const lang of langs) {
    report[k][lang] = translations[lang][k] || null;
  }
}

fs.writeFileSync('scripts/dev_i18n_report.json', JSON.stringify(report, null, 2), 'utf8');
console.log("Wrote dev_i18n_report.json");
