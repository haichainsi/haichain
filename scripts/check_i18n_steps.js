const fs = require('fs');
const content = fs.readFileSync('i18n.js', 'utf8');

const idx = content.indexOf('onlineStep3');
console.log('Index of onlineStep3 in i18n.js:', idx);
if (idx !== -1) {
  console.log(content.substring(idx - 100, idx + 200));
}
