const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');

const start = html.indexOf('id="hub-section-online"');
const end = html.indexOf('id="hub-section-web"');

console.log('START-END LENGTH:', end - start);
console.log(html.slice(start, end));
