const fs = require('fs');
const content = fs.readFileSync('dialog.js', 'utf8');
const p = content.indexOf("'HAICHAIN System'");
console.log(content.substring(p - 200, p + 500));
