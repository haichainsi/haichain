const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const m1 = content.search(/\$\{isVi\s*\?\s*`Ví/);
console.log(content.substring(m1, m1 + 700));
