const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const idx = content.indexOf("alert(getDashNotice('noWeb3DetectedFaucetGuide'))");
console.log('--- SURROUNDING CODE ---');
console.log(content.substring(idx - 150, idx + 800));
