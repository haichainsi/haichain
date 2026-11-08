const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p11 = content.indexOf('generatedResponse = isVi\n              ? `[Mã Lệnh');
const colon11 = content.indexOf(':\n              `[Solana Anchor', p11);
const semi11 = content.indexOf(';\n          }', colon11);
console.log('Match 11 end:', content.substring(semi11 - 50, semi11 + 20));

const p12 = content.indexOf('generatedResponse = isVi\n              ? `[Phân Tích');
const colon12 = content.indexOf(':\n              `[Autonomous Enterprise', p12);
const semi12 = content.indexOf(';\n          }', colon12);
console.log('Match 12 end:', content.substring(semi12 - 50, semi12 + 20));
