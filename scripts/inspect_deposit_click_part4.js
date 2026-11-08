const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf('Web3 wallet IS connected: Execute REAL on-chain');
console.log(content.substring(p, p + 2500));
