const fs = require('fs');
const code = fs.readFileSync('app/i18n.js', 'utf8');
const start = code.indexOf('function applyTranslations()');
console.log(code.substring(start, start + 1200));
