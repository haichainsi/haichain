const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf("dashConfirmDepositBtn.addEventListener('click'");
console.log('Index:', p);
if (p !== -1) {
  console.log(content.substring(p, p + 3000));
}
