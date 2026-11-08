const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p11 = content.indexOf('generatedResponse = isVi\n              ? `[Mã Lệnh');
console.log('Match 11 snippet:');
console.log(content.substring(p11, p11 + 600));

const p12 = content.indexOf('generatedResponse = isVi\n              ? `[Phân Tích');
console.log('Match 12 snippet:');
console.log(content.substring(p12, p12 + 600));
