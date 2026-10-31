const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, 'assets', 'branding');
fs.readdirSync(dir).forEach(file => {
  if (file.endsWith('.png')) {
    const fullPath = path.join(dir, file);
    const buf = fs.readFileSync(fullPath);
    if (buf.length > 24) {
      const width = buf.readUInt32BE(16);
      const height = buf.readUInt32BE(20);
      console.log(`${file} => ${width} x ${height} (ratio: ${(width/height).toFixed(2)})`);
    }
  }
});
