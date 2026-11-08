const fs = require('fs');
const path = require('path');

function searchDir(dir) {
  const files = fs.readdirSync(dir);
  for (const f of files) {
    if (f.startsWith('.') || f === 'node_modules' || f === 'scripts' || f === 'audits') continue;
    const full = path.join(dir, f);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      searchDir(full);
    } else if (f.endsWith('.html') || f.endsWith('.js')) {
      const content = fs.readFileSync(full, 'utf8');
      if (content.includes('1. Desktop') || content.includes('1. Desktop App')) {
        console.log('Found 1. Desktop in:', full);
      }
      if (content.includes('2. Claude Mobile')) {
        console.log('Found 2. Claude Mobile in:', full);
      }
      if (content.includes('3. Web Direct')) {
        console.log('Found 3. Web Direct in:', full);
      }
    }
  }
}

searchDir('.');
console.log('Search complete.');
