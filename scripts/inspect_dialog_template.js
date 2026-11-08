const fs = require('fs');
const content = fs.readFileSync('dialog.js', 'utf8');
const p = content.indexOf('hc-dialog-card');
console.log(content.substring(p, p + 1500));
