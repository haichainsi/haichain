const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const idx = content.indexOf('QUICK DEMOS');
console.log('Index of QUICK DEMOS:', idx);
if (idx !== -1) {
  console.log(content.substring(idx - 60, idx + 200));
}
