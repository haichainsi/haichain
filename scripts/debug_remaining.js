const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const regex = /isVi\s*\?/g;
let m;
while ((m = regex.exec(content)) !== null) {
  console.log('INDEX:', m.index);
  console.log('SURROUNDING:', JSON.stringify(content.substring(m.index - 50, m.index + 100)));
}
