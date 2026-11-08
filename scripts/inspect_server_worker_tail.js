const fs = require('fs');
const lines = fs.readFileSync('server/haichain-mcp-worker.js', 'utf8').split('\n');
console.log(lines.slice(Math.max(0, lines.length - 25)).join('\n'));
