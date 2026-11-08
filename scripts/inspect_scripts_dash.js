const fs = require('fs');
['dashboard.html', 'app/dashboard.html'].forEach(file => {
  console.log('=== ' + file + ' ===');
  const d = fs.readFileSync(file, 'utf8');
  const lines = d.split('\n');
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes('script src="/app/')) {
      console.log(`${i+1}: ${lines[i].trim()}`);
    }
  }
});
