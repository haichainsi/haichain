const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');

const idx = content.indexOf('id="ai-hub-modal"');
console.log('--- CONNECT AI MODAL AUDIT ---');
console.log(content.substring(idx, idx + 4000));
