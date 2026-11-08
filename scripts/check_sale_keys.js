const fs = require('fs');
const code = fs.readFileSync('sale-controller.js', 'utf8');
const langs = ['kk', 'en', 'zh', 'vi', 'ko', 'fr', 'es', 'ru', 'hi', 'he'];

langs.forEach(lang => {
  const p = code.indexOf(`"${lang}": {`);
  const cliff = code.includes(`vestingCliffCard`, p) && code.indexOf(`vestingCliffCard`, p) < p + 4000;
  console.log(`Lang ${lang} has cliff:`, cliff);
});
