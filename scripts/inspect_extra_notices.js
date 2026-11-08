const fs = require('fs');
const code = fs.readFileSync('scripts/eliminate_all_remaining_isvi.js', 'utf8');
const p = code.indexOf('const EXTRA_NOTICES =');
const end = code.indexOf('function patchFile', p);
console.log('EXTRA_NOTICES length:', end - p);
console.log(code.substring(p, p + 1500));
