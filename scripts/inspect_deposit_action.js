const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const lines = html.split('\n');
console.log(lines.slice(6610, 6720).join('\n'));
