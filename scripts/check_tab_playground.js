const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const idx = content.indexOf('id="tab-playground"');
console.log(content.substring(idx, idx + 1500));
