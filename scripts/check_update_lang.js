const fs = require('fs');
const code = fs.readFileSync('sale-controller.js', 'utf8');
const p = code.indexOf('function updateLanguage(');
console.log(code.substring(p, p + 1200));
