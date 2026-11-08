const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf('function getDashNotice');
console.log(content.substring(p, p + 400));
