const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');
const indices = [91857, 95324, 342048, 356223];
indices.forEach(idx => {
  console.log(`=== At ${idx} ===`);
  console.log(content.substring(idx - 60, idx + 140).replace(/\r?\n/g, ' '));
});
