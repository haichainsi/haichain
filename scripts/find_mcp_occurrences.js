const fs = require('fs');

const content = fs.readFileSync('dashboard.html', 'utf8');

let pos = 0;
while ((pos = content.indexOf('tab-mcp', pos)) !== -1) {
  console.log(`Pos ${pos}:`);
  console.log(content.slice(pos - 100, pos + 250));
  pos += 7;
}
