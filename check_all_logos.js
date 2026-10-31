const fs = require('fs');
const zlib = require('zlib');

const files = fs.readdirSync('assets/branding').filter(f => f.endsWith('.png'));
files.forEach(f => {
  const filePath = 'assets/branding/' + f;
  const data = fs.readFileSync(filePath);
  const width = data.readUInt32BE(16);
  const height = data.readUInt32BE(20);
  const colorType = data[25];
  console.log(`${f}: ${width}x${height}, colorType=${colorType}, size=${data.length}`);
});
