const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf("dash-pay-tab-apple");
console.log('Index of dash-pay-tab-apple:', p);
if (p !== -1) {
  // Find where it's used in script
  let idx = 0;
  while ((idx = content.indexOf('dash-pay-tab-', idx)) !== -1) {
    console.log(content.substring(idx - 40, idx + 100).replace(/\r?\n/g, ' '));
    idx += 15;
  }
}
