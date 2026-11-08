const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const p = content.indexOf("dashConfirmDepositBtn.addEventListener('click'");
console.log(content.substring(p + 2500, p + 6500));
