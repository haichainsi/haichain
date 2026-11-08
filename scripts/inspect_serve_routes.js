const fs = require('fs');
const text = fs.readFileSync('serve.js', 'utf8');

const lines = text.split('\n');
lines.forEach((l, i) => {
  if (l.includes('url ===') || l.includes('pathname ===') || l.includes('/api/')) {
    console.log(`Line ${i+1}: ${l.trim()}`);
  }
});
