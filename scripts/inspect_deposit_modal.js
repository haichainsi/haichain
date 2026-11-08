const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf('Top Up Master Vault');
console.log(content.substring(p - 100, p + 2500));
