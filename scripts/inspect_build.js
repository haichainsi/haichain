const fs = require('fs');
const content = fs.readFileSync('dialog.js', 'utf8');
const p = content.indexOf('_build()');
console.log(content.substring(p, p + 2000));
