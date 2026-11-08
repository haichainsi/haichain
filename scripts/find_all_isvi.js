const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const regex = /isVi\s*\?/g;
let m;
let count = 0;
while ((m = regex.exec(content)) !== null) {
  count++;
  console.log(`[${count}] Index: ${m.index}`);
  console.log(content.substring(m.index - 30, m.index + 100).replace(/\r?\n/g, ' '));
}
