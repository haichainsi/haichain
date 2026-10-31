const fs = require('fs');

// Simple PNG pixel color inspector
// Find first pixel with alpha > 0
function getFirstOpaqueColor(filename) {
  const buf = fs.readFileSync(filename);
  console.log(`Checking ${filename}... size: ${buf.length}`);
}
getFirstOpaqueColor('assets/logo-text-1.png');
getFirstOpaqueColor('assets/logo-text-2.png');
