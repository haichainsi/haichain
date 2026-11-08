const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const p = content.indexOf('id="deposit-modal"');
console.log(content.substring(p, p + 2500));
