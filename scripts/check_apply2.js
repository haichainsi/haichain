const fs = require('fs');
const code = fs.readFileSync('app/i18n.js', 'utf8');
const start = code.indexOf('document.querySelectorAll(\'[data-i18n]\').forEach');
console.log(code.substring(start, start + 1000));
