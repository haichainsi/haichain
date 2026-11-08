const fs = require('fs');

function check(file) {
    const code = fs.readFileSync(file, 'utf8');
    const r1 = [...code.matchAll(/tabDesktop:\s*['"]([^'"]+)['"]/g)].map(m => m[1]);
    const r2 = [...code.matchAll(/tabOnline:\s*['"]([^'"]+)['"]/g)].map(m => m[1]);
    const r3 = [...code.matchAll(/tabWeb:\s*['"]([^'"]+)['"]/g)].map(m => m[1]);
    console.log(file, 'tabDesktop:', r1);
    console.log(file, 'tabOnline:', r2);
    console.log(file, 'tabWeb:', r3);
}

check('i18n.js');
check('app/i18n.js');
