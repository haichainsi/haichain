const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const lines = html.split('\n');
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('function updateAiHubUrls()')) {
    console.log(lines.slice(i, i + 35).join('\n'));
    break;
  }
}
