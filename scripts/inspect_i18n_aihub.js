const fs = require('fs');
const js = fs.readFileSync('i18n.js', 'utf8');
const lines = js.split('\n');
const viHub = [];
let inVi = false;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('"vi":')) inVi = true;
  if (lines[i].includes('"en":')) inVi = false;
  if (inVi && lines[i].includes('"aiHub.')) {
    viHub.push(lines[i].trim());
  }
}
console.log(viHub.join('\n'));
