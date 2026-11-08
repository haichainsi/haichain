const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const lines = html.split('\n');
console.log('=== LINES 1565 - 1620 ===');
console.log(lines.slice(1565, 1620).join('\n'));
console.log('\n=== LINES 7390 - 7425 ===');
console.log(lines.slice(7390, 7425).join('\n'));
