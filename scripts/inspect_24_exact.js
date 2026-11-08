const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const regex = /isVi\s*\?/g;
let m;
let i = 0;
while ((m = regex.exec(content)) !== null) {
  i++;
  console.log(`=== MATCH ${i} (Index ${m.index}) ===`);
  console.log(content.substring(Math.max(0, m.index - 50), Math.min(content.length, m.index + 200)));
}
