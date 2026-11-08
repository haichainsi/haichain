const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const idx = content.indexOf('id="tab-playground"');
console.log(content.substring(idx + 1500, idx + 3500));
