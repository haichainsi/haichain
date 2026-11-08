const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const regex = /isVi\s*\?/g;
let m;
while ((m = regex.exec(content)) !== null) {
  console.log('Index:', m.index);
  console.log(content.substring(m.index - 30, m.index + 120).replace(/\r?\n/g, ' '));
}
