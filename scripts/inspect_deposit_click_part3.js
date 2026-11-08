const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf('Web3 MetaMask Deposit');
console.log(content.substring(p, p + 3500));
