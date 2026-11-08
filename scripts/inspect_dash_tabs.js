const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');
const lines = html.split('\n');
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('aiHub.tab') || lines[i].includes('tabDesktop') || lines[i].includes('tabOnline') || lines[i].includes('tabWeb')) {
    console.log(`${i+1}: ${lines[i].trim()}`);
  }
}
