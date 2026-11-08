const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const tab2Idx = html.indexOf('id="hub-section-online"');
const tab3Idx = html.indexOf('id="hub-section-playground"');
console.log(html.slice(tab2Idx, tab3Idx));
