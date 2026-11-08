const fs = require('fs');
const content = fs.readFileSync('dialog.js', 'utf8');
const p = content.indexOf('function parseMessage');
console.log(content.substring(p, p + 1200));
