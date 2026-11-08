const fs = require('fs');

const content = fs.readFileSync('dashboard.html', 'utf8');

const matches = [222984, 232741, 235564, 238707, 240906];
for (const pos of matches) {
  console.log(`=== Around pos ${pos} ===`);
  console.log(content.slice(Math.max(0, pos - 150), Math.min(content.length, pos + 250)));
}
