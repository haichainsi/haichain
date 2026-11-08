const fs = require('fs');

function checkScriptSyntax(file) {
  const content = fs.readFileSync(file, 'utf8');
  const scriptRegex = /<script\b([^>]*)>([\s\S]*?)<\/script>/gi;
  let match;
  let count = 0;
  let jsCount = 0;
  while ((match = scriptRegex.exec(content)) !== null) {
    count++;
    const attrs = match[1] || '';
    const code = match[2];
    if (attrs.includes('src=')) continue;
    if (attrs.includes('application/ld+json')) {
      try {
        JSON.parse(code);
      } catch (e) {
        console.error(`JSON-LD syntax error in ${file} script #${count}:`, e.message);
        return false;
      }
      continue;
    }
    jsCount++;
    try {
      new Function(code);
    } catch (e) {
      console.error(`Script syntax error in ${file} JS script #${jsCount} (total tag #${count}):`, e.message);
      return false;
    }
  }
  console.log(`[PASS] ${file}: ${jsCount} inline JS blocks + JSON-LD verified with valid syntax.`);
  return true;
}

function checkI18nSyntax(file) {
  const content = fs.readFileSync(file, 'utf8');
  try {
    new Function(content);
    console.log(`[PASS] ${file}: valid JavaScript syntax.`);
    return true;
  } catch (e) {
    console.error(`[FAIL] ${file} syntax error:`, e.message);
    return false;
  }
}

function checkSectionI18n(file) {
  const content = fs.readFileSync(file, 'utf8');
  const docsIdx = content.indexOf('id="tab-docs"');
  const docsEnd = content.indexOf('</section>', docsIdx);
  const section = content.slice(docsIdx, docsEnd);

  const i18nMatches = Array.from(section.matchAll(/data-i18n="([^"]+)"/g)).map(m => m[1]);
  console.log(`Found ${i18nMatches.length} data-i18n keys in tab-docs of ${file}:`, Array.from(new Set(i18nMatches)));

  const i18nContent = fs.readFileSync('i18n.js', 'utf8');
  const match = i18nContent.match(/const TRANSLATIONS\s*=\s*(\{[\s\S]*?\n\s*\});\s*\n/);
  const translations = new Function(`return ${match[1]};`)();

  const langs = ['en', 'vi', 'zh', 'fr', 'ko', 'es', 'ru', 'hi', 'he', 'kk'];
  let missing = 0;
  for (const lang of langs) {
    for (const key of new Set(i18nMatches)) {
      if (!translations[lang] || !translations[lang][key]) {
        console.error(`Missing translation for [${lang}][${key}] in i18n.js`);
        missing++;
      }
    }
  }
  if (missing === 0) {
    console.log(`[PASS] All keys in tab-docs are fully translated across all 10 languages!`);
  }
  return missing === 0;
}

const s1 = checkScriptSyntax('dashboard.html');
const s2 = checkScriptSyntax('app/dashboard.html');
const i1 = checkI18nSyntax('i18n.js');
const i2 = checkI18nSyntax('app/i18n.js');
const d1 = checkSectionI18n('dashboard.html');
const d2 = checkSectionI18n('app/dashboard.html');

if (s1 && s2 && i1 && i2 && d1 && d2) {
  console.log('\n=== ALL INTEGRITY CHECKS PASSED PERFECTLY! ===');
} else {
  console.error('\n=== INTEGRITY CHECKS FAILED! ===');
  process.exit(1);
}
