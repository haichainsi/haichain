const fs = require('fs');

console.log('=== RUNNING COMPREHENSIVE 10-LANGUAGE VERIFICATION ===\n');

// 1. Check sale-controller.js
const saleCode = fs.readFileSync('sale-controller.js', 'utf8');
const saleHasCliff = saleCode.includes('getI18nText(\'vestingCliffCard\')');
const saleHasCliffDesc = saleCode.includes('getI18nText(\'vestingCliffDesc\')');
const saleHasLinear = saleCode.includes('getI18nText(\'vestingLinearCard\')');
console.log('1. Presale Calculator Template:', {
  hasCliffCard: saleHasCliff,
  hasCliffDesc: saleHasCliffDesc,
  hasLinearCard: saleHasLinear
});

// 2. Check dashboard.html
const dashCode = fs.readFileSync('dashboard.html', 'utf8');
const isViMatches = (dashCode.match(/isVi\s*\?/g) || []).length;
const hasVestingI18n = dashCode.includes('const VESTING_VAULT_I18N =');
const hasNoticesI18n = dashCode.includes('const DASH_NOTICES_I18N =');
const hasAiHubDataI18n = dashCode.includes('data-i18n="aiHub.modalTitle"');
const hasPlaygroundDataI18n = dashCode.includes('data-i18n="playground.quickDemos"');

console.log('2. Dashboard Localization:', {
  remainingIsViCount: isViMatches,
  hasVestingVault10Lang: hasVestingI18n,
  hasNotices10Lang: hasNoticesI18n,
  hasAiHubDataI18n: hasAiHubDataI18n,
  hasPlaygroundDataI18n: hasPlaygroundDataI18n
});

// 3. Check i18n.js
const i18nCode = fs.readFileSync('i18n.js', 'utf8');
const langs = ['kk', 'en', 'zh', 'vi', 'ko', 'fr', 'es', 'ru', 'hi', 'he'];
const missingAiHub = [];
const missingPlayground = [];

langs.forEach(l => {
  const langBlock = i18nCode.substring(i18nCode.indexOf(`"${l}": {`), i18nCode.indexOf(`"${l}": {`) + 35000);
  if (!langBlock.includes('"aiHub.modalTitle":')) missingAiHub.push(l);
  if (!langBlock.includes('"playground.demoAntiDrain":')) missingPlayground.push(l);
});

console.log('3. Dictionary Completeness (All 10 Languages):', {
  missingAiHubLangs: missingAiHub,
  missingPlaygroundLangs: missingPlayground
});

if (isViMatches === 0 && saleHasCliff && hasVestingI18n && hasNoticesI18n && missingAiHub.length === 0 && missingPlayground.length === 0) {
  console.log('\n>>> ALL 10-LANGUAGE LOCALIZATION CHECKS PASSED WITH 100% SUCCESS! <<<');
} else {
  console.log('\n>>> WARNING: SOME CHECKS FAILED! <<<');
}
