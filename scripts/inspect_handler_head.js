const fs = require('fs');
const lines = fs.readFileSync('server/cloud-mcp-functions/_mcp_handler.js', 'utf8').split('\n');
console.log(lines.slice(0, 80).join('\n'));
