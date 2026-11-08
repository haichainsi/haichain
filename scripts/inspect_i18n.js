const fs = require('fs');

const content = fs.readFileSync('i18n.js', 'utf8');
const lines = content.split('\n');

console.log('Total lines in i18n.js:', lines.length);
lines.forEach((l, i) => {
  if (l.trim().startsWith('"comp.') || l.trim().startsWith('"footer.compliance"') || l.trim().startsWith('"cluster.auditsPassed"') || l.trim().startsWith('"roadmap.stage1Item3"')) {
    if (i < 800) {
      console.log(`${i+1}: ${l.trim().slice(0, 100)}`);
    }
  }
});
