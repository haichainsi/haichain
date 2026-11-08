const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const lines = html.split('\n');
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('hubTabDesktop')) {
    console.log(lines.slice(Math.max(0, i - 5), Math.min(lines.length, i + 35)).join('\n'));
    break;
  }
}
