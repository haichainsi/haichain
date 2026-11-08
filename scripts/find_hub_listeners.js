const fs = require('fs');
const html = fs.readFileSync('dashboard.html', 'utf8');

const lines = html.split('\n');
lines.forEach((l, idx) => {
  if (l.includes('hubTabDesktop') || l.includes('hub-tab-desktop') || l.includes('copy-online-mcp-btn')) {
    console.log((idx + 1) + ': ' + l.trim());
  }
});
