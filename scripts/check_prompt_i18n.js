const fs = require('fs');
const code = fs.readFileSync('app/i18n.js', 'utf8');
const regex = /"playground\.promptPlaceholder":\s*"([^"]+)"/g;
let m;
while ((m = regex.exec(code)) !== null) {
  console.log(m[1]);
}
