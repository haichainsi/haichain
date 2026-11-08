const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');

const idx = content.indexOf('id="ai-hub-modal"');
const endIdx = content.indexOf('<!-- Multi-Phase Private SAFT Tokenomics Modal -->', idx);
console.log('--- CONNECT AI MODAL FULL CONTENT ---');
console.log(content.substring(idx + 1500, idx + 8000));
