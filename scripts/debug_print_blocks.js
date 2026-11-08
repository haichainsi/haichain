const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
console.log('INDEX 252270:');
console.log(content.substring(252260, 252800));

console.log('INDEX 410917:');
console.log(content.substring(410900, 411200));
