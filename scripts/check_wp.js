const fs = require('fs');

['index.html', 'dashboard.html'].forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  const lines = content.split('\n');
  lines.forEach((line, i) => {
    if (/whitepaper/i.test(line)) {
      console.log(`${f}:${i+1}: ${line.trim().slice(0, 120)}`);
    }
  });
});
