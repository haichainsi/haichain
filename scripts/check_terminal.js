const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const idx = content.indexOf('id="playground-terminal"');
console.log(content.substring(idx, idx + 800));
