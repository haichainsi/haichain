const fs = require('fs');
const lines = fs.readFileSync('_worker.js', 'utf8').split('\n');
console.log(lines.slice(Math.max(0, lines.length - 40)).join('\n'));
