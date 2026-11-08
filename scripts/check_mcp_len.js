const fs = require('fs');
console.log(fs.readFileSync('server/cloud-mcp-functions/_mcp_handler.js', 'utf8').length);
