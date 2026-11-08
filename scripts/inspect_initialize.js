const fs = require('fs');
const code = fs.readFileSync('server/haichain-mcp-worker.js', 'utf8');
const lines = code.split('\n');
console.log(lines.slice(295, 335).join('\n'));
