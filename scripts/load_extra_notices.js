const fs = require('fs');

const elCode = fs.readFileSync('scripts/eliminate_all_remaining_isvi.js', 'utf8');
const p1 = elCode.indexOf('const EXTRA_NOTICES =');
const pEnd1 = elCode.indexOf('function patchFile', p1);
eval(elCode.substring(p1, pEnd1));

const mmCode = fs.readFileSync('scripts/patch_final_isvi.js', 'utf8');
const p2 = mmCode.indexOf('const MM_KEYS =');
const pEnd2 = mmCode.indexOf('function patchFinal', p2);
eval(mmCode.substring(p2, pEnd2));

// Merge MM_KEYS into EXTRA_NOTICES
const ALL_EXTRA = {};
const langs = ['kk', 'en', 'zh', 'vi', 'ko', 'fr', 'es', 'ru', 'hi', 'he'];
langs.forEach(lang => {
  ALL_EXTRA[lang] = Object.assign({}, EXTRA_NOTICES[lang] || {}, MM_KEYS[lang] || {});
});

module.exports = { ALL_EXTRA };
