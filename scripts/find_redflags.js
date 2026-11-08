const fs = require('fs');
const path = require('path');

const files = [
  'index.html',
  'dashboard.html',
  'i18n.js',
  'sale-controller.js'
];

const terms = [
  '100% Exploit Immune',
  '100% Cryptographic',
  'Exploit Immune',
  '142x',
  '15/15',
  'Audits Passed',
  'Bittensor',
  'Render',
  'Virtuals',
  'FinCEN',
  'MiCA',
  '15.9M',
  '0.14ms',
  '142,857',
  '50x'
];

files.forEach(f => {
  if (!fs.existsSync(f)) return;
  const lines = fs.readFileSync(f, 'utf8').split('\n');
  terms.forEach(term => {
    const matches = [];
    lines.forEach((line, idx) => {
      if (line.toLowerCase().includes(term.toLowerCase())) {
        matches.push(`${idx + 1}: ${line.trim().slice(0, 120)}`);
      }
    });
    if (matches.length > 0) {
      console.log(`=== ${f} -> "${term}" (${matches.length} matches) ===`);
      matches.slice(0, 5).forEach(m => console.log('   ' + m));
    }
  });
});
