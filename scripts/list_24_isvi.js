const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const lines = content.split('\n');

lines.forEach((line, i) => {
  if (/isVi\s*\?/.test(line)) {
    console.log(`Line ${i + 1}: ${line.trim().substring(0, 100)}`);
  }
});
