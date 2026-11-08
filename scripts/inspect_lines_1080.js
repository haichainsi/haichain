const fs = require('fs');
const lines = fs.readFileSync('sale-controller.js', 'utf8').split('\n');
console.log(lines.slice(1075, 1100).join('\n'));
