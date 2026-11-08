const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const idx = content.indexOf('Anti-Drain');
console.log(content.substring(idx - 600, idx));
