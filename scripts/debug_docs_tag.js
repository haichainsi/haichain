const fs = require('fs');

const content = fs.readFileSync('dashboard.html', 'utf8');
const docsIdx = content.indexOf('id="tab-docs"');
console.log('docsIdx:', docsIdx);
if (docsIdx !== -1) {
  console.log('Before docs:');
  console.log(content.slice(docsIdx - 100, docsIdx));
  console.log('After docs:');
  console.log(content.slice(docsIdx, docsIdx + 300));
}
