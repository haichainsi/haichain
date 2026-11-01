const fs = require('fs');

console.log('====================================================');
console.log('  MOBILE & RESPONSIVE OVERFLOW AUDIT ACROSS 10 LANGS ');
console.log('====================================================\n');

// 1. Load Translations
const content = fs.readFileSync('i18n.js', 'utf8');
const start = content.indexOf('const TRANSLATIONS = {');
const end = content.indexOf('function getInitialLanguage()');
let code = content.slice(start, end).trim();
if (code.endsWith(';')) code = code.slice(0, -1);
code = code.replace('const TRANSLATIONS =', 'global.TRANSLATIONS =');
eval(code);

const translations = global.TRANSLATIONS;
const languages = Object.keys(translations);

const files = ['index.html', 'dashboard.html', 'app/index.html', 'app/dashboard.html'];

files.forEach(file => {
  if (!fs.existsSync(file)) return;
  console.log(`\n--- Inspecting [${file}] ---`);
  const html = fs.readFileSync(file, 'utf8');

  // Regex to extract tags with data-i18n
  const tagRegex = /<([a-zA-Z0-9]+)\s+([^>]*data-i18n=["']([^"']+)["'][^>]*)>/gi;
  let m;
  let nowrapCount = 0;
  let fixedWidthCount = 0;
  const warnings = [];

  while ((m = tagRegex.exec(html)) !== null) {
    const tag = m[1];
    const attrs = m[2];
    const key = m[3];

    const classMatch = attrs.match(/class=["']([^"']*)["']/);
    const cls = classMatch ? classMatch[1] : '';

    if (cls.includes('whitespace-nowrap')) {
      nowrapCount++;
      // Check maximum length of this key across all 10 languages
      let maxLen = 0;
      let maxLang = '';
      let maxText = '';
      for (const lang of languages) {
        const text = (translations[lang] && translations[lang][key]) || '';
        if (text.length > maxLen) {
          maxLen = text.length;
          maxLang = lang;
          maxText = text;
        }
      }
      console.log(`    [whitespace-nowrap] key="${key}" -> max len ${maxLen} chars (${maxLang})`);
      // If text is very long (>35 chars) with whitespace-nowrap, it may cause horizontal scroll on 360px viewport
      if (maxLen > 35) {
        warnings.push({
          key,
          tag,
          cls,
          maxLen,
          maxLang,
          maxText: maxText.slice(0, 40) + '...'
        });
      }
    }
  }

  console.log(`  Total elements with whitespace-nowrap: ${nowrapCount}`);
  if (warnings.length > 0) {
    console.log(`  ⚠️ Found ${warnings.length} elements with whitespace-nowrap and long text (>35 chars):`);
    warnings.forEach(w => {
      console.log(`    - Key: "${w.key}" in <${w.tag}>: max len ${w.maxLen} chars in [${w.maxLang}] ("${w.maxText}")`);
    });
  } else {
    console.log(`  ✅ All whitespace-nowrap elements have compact labels (<=35 chars) that fit mobile viewports safely!`);
  }
});

console.log('\n====================================================');
console.log('              OVERFLOW AUDIT COMPLETE               ');
console.log('====================================================');
