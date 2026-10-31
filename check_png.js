const fs = require('fs');
const zlib = require('zlib');

// Read IDAT chunk from PNG to check text color
function checkColor(file) {
  const buf = fs.readFileSync(file);
  console.log(`${file}: length ${buf.length}`);
}
checkColor('assets/logo-text-1.png');
checkColor('assets/logo-text-2.png');
checkColor('assets/logo-haichain-si.png');
