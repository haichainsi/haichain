const fs = require('fs');

function loadI18n() {
  const content = fs.readFileSync('i18n.js', 'utf8');
  const start = content.indexOf('const TRANSLATIONS = {');
  const end = content.indexOf('function getInitialLanguage()');
  let code = content.slice(start, end).trim();
  if (code.endsWith(';')) code = code.slice(0, -1);
  code = code.replace('const TRANSLATIONS =', 'global.TRANSLATIONS =');
  eval(code);
  return global.TRANSLATIONS;
}

function extractDataI18nKeys(htmlFile) {
  const content = fs.readFileSync(htmlFile, 'utf8');
  const regex = /data-i18n="([^"]+)"/g;
  const keys = new Set();
  let m;
  while ((m = regex.exec(content)) !== null) {
    keys.add(m[1]);
  }
  return Array.from(keys);
}

function runDeepAudit() {
  console.log('====================================================');
  console.log('       HAICHAIN i18n DEEP PARITY AUDIT              ');
  console.log('====================================================\n');

  const translations = loadI18n();
  const languages = Object.keys(translations);

  // 1. Collect all active keys used in index.html & dashboard.html
  const indexKeys = extractDataI18nKeys('index.html');
  const dashKeys = extractDataI18nKeys('dashboard.html');
  const activeHtmlKeys = new Set([...indexKeys, ...dashKeys]);

  console.log(`[1] Total HTML Keys Referenced: ${activeHtmlKeys.size}`);
  console.log(`    - index.html: ${indexKeys.length}`);
  console.log(`    - dashboard.html: ${dashKeys.length}\n`);

  // 2. Check each language against activeHtmlKeys
  console.log('[2] Active HTML Keys Coverage per Language:');
  for (const lang of languages) {
    const langDict = translations[lang];
    const missing = Array.from(activeHtmlKeys).filter(k => !langDict[k]);
    if (missing.length === 0) {
      console.log(`✅ [${lang}]: 100% of HTML keys are translated! (${activeHtmlKeys.size}/${activeHtmlKeys.size})`);
    } else {
      console.log(`❌ [${lang}]: Missing ${missing.length} active HTML keys:`);
      missing.forEach(k => console.log(`      - ${k}`));
    }
  }

  // 3. Check English Master dictionary vs other dictionaries
  console.log('\n[3] Master English Dictionary vs Other Languages:');
  const enKeys = Object.keys(translations['en']);
  console.log(`Master English Total Keys: ${enKeys.length}`);

  for (const lang of languages) {
    if (lang === 'en') continue;
    const langDict = translations[lang];
    const missingVsEn = enKeys.filter(k => !langDict[k]);
    if (missingVsEn.length === 0) {
      console.log(`✅ [${lang}]: 100% parity with English dictionary (${enKeys.length} keys)`);
    } else {
      console.log(`❌ [${lang}]: Missing ${missingVsEn.length} keys compared to English:`, missingVsEn);
    }
  }
}

runDeepAudit();
