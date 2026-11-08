const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const regex = /isVi\s*\?/g;
let m;
let i = 0;
while ((m = regex.exec(content)) !== null) {
  i++;
  console.log(`=== MATCH ${i} ===`);
  const chunk = content.substring(m.index - 20, m.index + 250);
  console.log(JSON.stringify(chunk));
}
