const fs = require('fs');
const code = fs.readFileSync('sale-controller.js', 'utf8');
const p = code.indexOf('renderTerminalContent(container, isAuthorized);');
console.log(code.substring(p, p + 800));
