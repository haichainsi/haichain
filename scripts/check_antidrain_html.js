const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const idx = content.indexOf('Anti-Drain');
console.log('Index:', idx);
if (idx !== -1) {
  console.log(content.substring(idx - 250, idx + 450));
}
