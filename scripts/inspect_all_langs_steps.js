const fs = require('fs');
const content = fs.readFileSync('i18n.js', 'utf8');

const start = content.indexOf('const TRANSLATIONS = {');
const end = content.indexOf('function getInitialLanguage()');
let code = content.slice(start, end).trim();
if (code.endsWith(';')) code = code.slice(0, -1);
code = code.replace('const TRANSLATIONS =', 'global.TRANSLATIONS =');
eval(code);

const TRANSLATIONS = global.TRANSLATIONS;
const langs = Object.keys(TRANSLATIONS);

// Inspect dev and mcp keys
const enKeys = Object.keys(TRANSLATIONS.en).filter(k => k.startsWith('dev.') || k.startsWith('mcp.'));
console.log('Total dev and mcp keys:', enKeys.length);

const programmingStepKeys = [
  'dev.pyStep1',
  'dev.pyStep2',
  'dev.pyStep3',
  'dev.step1Label',
  'dev.step2Label',
  'dev.step3Title',
  'mcp.sdkTitle',
  'mcp.sdkDesc',
  'btn.copyCode',
  'mcp.copyJson'
];

langs.forEach(lang => {
  console.log(`\n--- LANG: ${lang} ---`);
  programmingStepKeys.forEach(k => {
    if (TRANSLATIONS[lang] && TRANSLATIONS[lang][k]) {
      console.log(`  ${k}: "${TRANSLATIONS[lang][k]}"`);
    }
  });
});
