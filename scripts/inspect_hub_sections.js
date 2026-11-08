const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');

let idx = 0;
while ((idx = content.indexOf('id="hub-section', idx)) !== -1) {
  console.log('--- Match at', idx, '---');
  console.log(content.substring(idx, idx + 600));
  idx += 16;
}
