const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const lines = html.split('\n');
console.log(lines.slice(7325, 7365).join('\n'));
