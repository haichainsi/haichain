const fs = require('fs');
const c = fs.readFileSync('dashboard.html', 'utf8');

const regex = /<(div|span|h3|h4|p)\b[^>]*data-i18n="([^"]+)"[^>]*>([\s\S]*?)<\/\1>/gi;
let m;
while ((m = regex.exec(c)) !== null) {
  const key = m[2];
  const inner = m[3].trim();
  if (inner.includes('Step') || key.includes('step') || inner.includes('Bước')) {
    console.log(`KEY: ${key} -> INNER: ${inner}`);
  }
}
