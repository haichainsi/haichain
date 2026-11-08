const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const p = content.indexOf('Active Spending Pot');
console.log('Index of Active Spending Pot:', p);
if (p !== -1) {
  // Find opening tag before this
  const before = content.substring(p - 1200, p);
  console.log('BEFORE:');
  console.log(before);
  // Find where this container ends
  const pStream = content.indexOf('Live Micro-Settlement Stream');
  console.log('Index of Live Micro-Settlement Stream:', pStream);
  const after = content.substring(pStream, pStream + 1200);
  console.log('AFTER:');
  console.log(after);
}
