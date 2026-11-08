const fs = require('fs');
const content = fs.readFileSync('i18n.js', 'utf8');
const lines = content.split('\n');
lines.forEach((l, i) => {
  const match = l.match(/^\s*"([a-z]{2})":\s*\{/);
  if (match) console.log(match[1], 'starts at line', i + 1);
});
