const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const lines = html.split('\n');
console.log(lines.slice(7320, 7395).join('\n'));
