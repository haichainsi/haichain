const fs = require('fs');
const code = fs.readFileSync('sale-controller.js', 'utf8');
const p = code.indexOf('btnPayPhantom');
console.log('Index of btnPayPhantom:', p);
if (p !== -1) {
  console.log(code.substring(p - 100, p + 400));
}
