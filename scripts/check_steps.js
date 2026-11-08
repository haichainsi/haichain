const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');

const regex = /"onlineStep3":\s*"([^"]+)"/g;
let m;
while ((m = regex.exec(content)) !== null) {
  console.log('onlineStep3:', m[1]);
}
