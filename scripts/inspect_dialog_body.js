const fs = require('fs');
const content = fs.readFileSync('dialog.js', 'utf8');
const p = content.indexOf('hc-dialog-body');
console.log(content.substring(p - 300, p + 500));
