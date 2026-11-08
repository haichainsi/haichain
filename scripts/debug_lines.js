const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const lines = content.split('\n');
console.log(lines.slice(6825, 6845).join('\n'));
