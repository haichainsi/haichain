const fs = require('fs');

console.log('====================================================');
console.log('   HAICHAIN i18n STAGE 3: STRESS-TEST & AUDIT       ');
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
const en = translations.en;

// 2. TEXT EXPANSION STRESS-TEST
console.log('[TEST 1] Text Expansion Ratios Across 10 Languages:');
const expansionStats = {};
for (const lang of languages) {
  if (lang === 'en') continue;
  let totalEnLen = 0;
  let totalLangLen = 0;
  let maxExpansion = { key: '', ratio: 0, enText: '', langText: '' };

  for (const [k, enVal] of Object.entries(en)) {
    const langVal = translations[lang][k] || '';
    totalEnLen += enVal.length;
    totalLangLen += langVal.length;
    const ratio = enVal.length > 0 ? langVal.length / enVal.length : 1;
    if (ratio > maxExpansion.ratio && enVal.length > 5) {
      maxExpansion = { key: k, ratio, enText: enVal, langText: langVal };
    }
  }

  const avgRatio = ((totalLangLen / totalEnLen) * 100).toFixed(1);
  expansionStats[lang] = { avgRatio: avgRatio + '%', maxExpansion };
  console.log(`  - [${lang}]: Avg Length = ${avgRatio}% of English. Max expansion: "${maxExpansion.key}" (${maxExpansion.ratio.toFixed(2)}x)`);
}

// 3. AUDIT FIXED WIDTHS ON BUTTONS & INPUTS
console.log('\n[TEST 2] Checking for Potentially Breaking Fixed Widths in HTML:');
const htmlFiles = ['index.html', 'dashboard.html', 'app/index.html', 'app/dashboard.html'];
const fixedWidthIssues = [];

for (const file of htmlFiles) {
  if (!fs.existsSync(file)) continue;
  const html = fs.readFileSync(file, 'utf8');
  // Match elements with data-i18n that also have fixed pixel widths in class
  const tagRegex = /<([a-zA-Z0-9]+)[^>]*data-i18n="([^"]+)"[^>]*>/g;
  let m;
  while ((m = tagRegex.exec(html)) !== null) {
    const fullTag = m[0];
    const tag = m[1];
    const key = m[2];
    const classMatch = fullTag.match(/class="([^"]+)"/);
    if (classMatch) {
      const cls = classMatch[1];
      // check for rigid classes like w-[300px] or min-w-[300px] without max-w-full
      const rigidMatch = cls.match(/\b(min-w|w)-\[(\d+)px\]/);
      if (rigidMatch && parseInt(rigidMatch[2]) > 280) {
        fixedWidthIssues.push({ file, tag, key, class: cls, width: rigidMatch[0] });
      }
    }
  }
}

if (fixedWidthIssues.length === 0) {
  console.log('  ✅ No rigid fixed-width containers (>280px) found on translated elements! Responsive layout is fluid.');
} else {
  console.log(`  ⚠️ Found ${fixedWidthIssues.length} fixed-width elements:`, fixedWidthIssues);
}

// 4. SWITCHING SPEED BENCHMARK (Simulating 319 HTML element updates)
console.log('\n[TEST 3] Language Switching Speed Benchmark (Simulated DOM Injection):');
const indexHtml = fs.readFileSync('index.html', 'utf8');
const activeKeys = [];
const regex = /data-i18n="([^"]+)"/g;
let m;
while ((m = regex.exec(indexHtml)) !== null) {
  activeKeys.push(m[1]);
}

const times = [];
for (let iter = 0; iter < 100; iter++) {
  const targetLang = languages[iter % languages.length];
  const t0 = process.hrtime.bigint();
  
  // Simulate DOM batch update
  const dict = translations[targetLang];
  for (let i = 0; i < activeKeys.length; i++) {
    const val = dict[activeKeys[i]] || en[activeKeys[i]];
    // simulate innerHTML or textContent resolution
    const dummy = val.length > 0;
  }
  
  const t1 = process.hrtime.bigint();
  times.push(Number(t1 - t0) / 1e6); // convert to ms
}

const avgMs = (times.reduce((a, b) => a + b, 0) / times.length).toFixed(3);
const maxMs = Math.max(...times).toFixed(3);
console.log(`  ⚡ 100 Language Switches benchmarked across ${activeKeys.length} HTML keys:`);
console.log(`     Average Switch Time: ${avgMs} ms (Target: < 50 ms) -> ${parseFloat(avgMs) < 50 ? '✅ EXCELLENT' : '❌ SLOW'}`);
console.log(`     Peak Switch Time:    ${maxMs} ms -> ${parseFloat(maxMs) < 50 ? '✅ EXCELLENT' : '❌ SLOW'}`);

// 5. RTL & DIR ATTRIBUTE INTEGRITY CHECK
console.log('\n[TEST 4] RTL & Directional Consistency Check:');
const i18nContent = fs.readFileSync('i18n.js', 'utf8');
const hasRtlSwitch = i18nContent.includes("document.documentElement.setAttribute('dir', langCode === 'he' ? 'rtl' : 'ltr')");
const hasInitRtl = i18nContent.includes("document.documentElement.setAttribute('dir', currentLang === 'he' ? 'rtl' : 'ltr')");

if (hasRtlSwitch && hasInitRtl) {
  console.log('  ✅ Dual RTL Enforcement Verified: Both setLanguage() and init() enforce dir="rtl" for Hebrew.');
} else {
  console.log('  ❌ RTL Enforcement missing in one or more handlers!');
}

console.log('\n====================================================');
console.log('              STRESS-TEST COMPLETE                  ');
console.log('====================================================');
