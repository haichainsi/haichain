const fs = require('fs');
const code = fs.readFileSync('sale-controller.js', 'utf8');
const langs = ['kk', 'en', 'zh', 'vi', 'ko', 'fr', 'es', 'ru', 'hi', 'he'];

const idx = code.indexOf('const SALE_I18N =');
const end = code.indexOf('function getActiveLang()', idx);
const saleI18nSnippet = code.substring(idx, end);
eval(saleI18nSnippet);

langs.forEach(lang => {
  const dict = SALE_I18N[lang];
  console.log(`[${lang}] cliffCard:`, dict?.vestingCliffCard, '| linearCard:', dict?.vestingLinearCard);
});
