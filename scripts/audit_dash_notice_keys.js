const fs = require('fs');
const file = process.argv[2] || 'dashboard.html';
const content = fs.readFileSync(file, 'utf8');

// Find all getDashNotice('key')
const regex = /getDashNotice\(['"]([^'"]+)['"]\)/g;
let m;
const keysUsed = new Set();
while ((m = regex.exec(content)) !== null) {
  keysUsed.add(m[1]);
}

console.log(file, 'total unique keys used with getDashNotice:', keysUsed.size);

// Extract DASH_NOTICES_I18N
const pStart = content.indexOf('const DASH_NOTICES_I18N =');
const pEnd = content.indexOf('function getDashNotice', pStart);
const dictCode = content.substring(pStart, pEnd).replace('const DASH_NOTICES_I18N =', 'global.DASH_NOTICES_I18N =');
eval(dictCode);

const langs = ['en', 'vi', 'zh', 'kk', 'ko', 'fr', 'es', 'ru', 'hi', 'he'];

const missing = {};
for (const key of keysUsed) {
  for (const lang of langs) {
    if (!global.DASH_NOTICES_I18N[lang] || !global.DASH_NOTICES_I18N[lang][key]) {
      if (!missing[key]) missing[key] = [];
      missing[key].push(lang);
    }
  }
}

console.log(file, 'MISSING KEYS:', JSON.stringify(missing, null, 2));
