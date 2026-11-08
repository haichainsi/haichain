const fs = require('fs');
const code = fs.readFileSync('sale-controller.js', 'utf8');
const idx = code.indexOf('calc-step2');
console.log(code.substring(idx - 100, idx + 400));
