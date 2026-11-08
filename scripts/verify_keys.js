const fs = require('fs');

const content = fs.readFileSync('i18n.js', 'utf8');

// evaluate TRANSLATIONS
let translations;
try {
  const match = content.match(/const TRANSLATIONS\s*=\s*(\{[\s\S]*?\n\s*\});\s*\n/);
  if (!match) throw new Error('TRANSLATIONS not matched');
  translations = new Function(`return ${match[1]};`)();
} catch (e) {
  console.error('Failed to parse TRANSLATIONS:', e.message);
  process.exit(1);
}

const langs = ['en', 'vi', 'zh', 'fr', 'ko', 'es', 'ru', 'hi', 'he', 'kk'];
const keysToCheck = [
  'nav.devHub',
  'nav.devHubShort',
  'dev.badge',
  'dev.title',
  'dev.subtitle',
  'dev.card1Title',
  'dev.card1Desc',
  'dev.card1Badge',
  'dev.card2Title',
  'dev.card2Desc',
  'dev.card2Badge',
  'dev.card3Title',
  'dev.card3Desc',
  'dev.card3Badge',
  'dev.sec1Title',
  'dev.sec1Desc',
  'dev.step1Label',
  'dev.step2Label',
  'dev.step3Title',
  'dev.step3Desc',
  'dev.sec2Title',
  'dev.sec2Desc',
  'dev.sec2PromptsTitle',
  'dev.sec2Prompt1',
  'dev.sec2Prompt2',
  'dev.sec2Prompt3',
  'dev.sec3Title',
  'dev.sec3Desc',
  'mcp.sdkTitle',
  'mcp.sdkDesc',
  'btn.copy',
  'btn.copyCode',
  'btn.copyJson',
  'btn.copyCurl'
];

let missing = 0;
for (const lang of langs) {
  if (!translations[lang]) {
    console.error(`Missing language: ${lang}`);
    missing++;
    continue;
  }
  for (const k of keysToCheck) {
    if (!translations[lang][k]) {
      console.warn(`[${lang}] missing key: ${k}`);
      missing++;
    }
  }
}

if (missing === 0) {
  console.log('SUCCESS: All 34 keys present across all 10 languages with 0 missing!');
} else {
  console.log(`TOTAL MISSING: ${missing}`);
}
