const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const tabs = html.match(/data-tab="[^"]+"/g);
console.log('Tabs:', tabs);

const sections = html.match(/<section id="tab-[^"]+"/g);
console.log('Sections:', sections);
