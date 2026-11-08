const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf('const DASH_NOTICES_I18N =');
console.log(content.substring(p, p + 400));
