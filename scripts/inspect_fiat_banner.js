const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf('deposit-fiat-banner');
console.log('Index:', p);
if (p !== -1) {
  console.log(content.substring(p - 100, p + 800));
}
