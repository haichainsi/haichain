const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const start = html.indexOf('<section id="tab-overview"');
const end = html.indexOf('</section>', start);
console.log(html.slice(end - 1000, end));
