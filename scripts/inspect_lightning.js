const fs = require('fs');
const code = fs.readFileSync('sale-controller.js', 'utf8');
const p = code.indexOf('Connect Web3 Wallet to Buy $HAISI');
console.log('Index:', p);
if (p !== -1) {
  console.log(code.substring(p - 300, p + 400));
}
