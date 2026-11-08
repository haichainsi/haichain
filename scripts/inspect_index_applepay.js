const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const p = content.indexOf('Apple Pay');
console.log('Index of Apple Pay in index.html:', p);
if (p !== -1) {
  console.log(content.substring(p - 300, p + 500));
}
