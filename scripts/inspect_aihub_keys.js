const fs = require('fs');
const content = fs.readFileSync('i18n.js', 'utf8');
const lines = content.split('\n');
const enKeys = [];
lines.slice(510, 560).forEach(l => {
  if (l.trim().startsWith('"aiHub.')) {
    enKeys.push(l.trim());
  }
});
console.log(enKeys.join('\n'));
