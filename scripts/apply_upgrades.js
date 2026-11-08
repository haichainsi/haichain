// Script to apply Claude feedback upgrades across HaiChain codebase
const fs = require('fs');
const path = require('path');

console.log('Starting Institutional Upgrade implementation based on Claude feedback...');

// Helper to replace text in file
function replaceInFile(filePath, replacements) {
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return;
  }
  let content = fs.readFileSync(filePath, 'utf8');
  let count = 0;
  for (const { from, to, label } of replacements) {
    if (typeof from === 'string') {
      if (content.includes(from)) {
        content = content.split(from).join(to);
        count++;
        console.log(`[${filePath}] Replaced: ${label || from.slice(0, 40)}`);
      } else {
        console.warn(`[${filePath}] Pattern not found: ${label || from.slice(0, 40)}`);
      }
    } else if (from instanceof RegExp) {
      if (from.test(content)) {
        content = content.replace(from, to);
        count++;
        console.log(`[${filePath}] Replaced regex: ${label || from.toString().slice(0, 40)}`);
      } else {
        console.warn(`[${filePath}] Regex pattern not found: ${label || from.toString().slice(0, 40)}`);
      }
    }
  }
  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Updated ${filePath} with ${count} changes.`);
}

console.log('Preparation complete.');
