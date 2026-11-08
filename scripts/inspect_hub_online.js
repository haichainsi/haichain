const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const s = html.indexOf('id="hub-section-online"');
const e = html.indexOf('id="hub-section-web"');
console.log(html.slice(s, e));
