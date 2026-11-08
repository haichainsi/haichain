const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf("const dashPayTabFaucet = document.getElementById('dash-pay-tab-faucet');");
console.log(content.substring(p, p + 2500));
