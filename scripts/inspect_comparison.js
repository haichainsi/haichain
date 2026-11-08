const fs = require('fs');

function inspectSection(filePath, startRegex, endRegex) {
  const lines = fs.readFileSync(filePath, 'utf8').split('\n');
  let recording = false;
  const result = [];
  lines.forEach((line, idx) => {
    if (startRegex.test(line)) recording = true;
    if (recording) {
      result.push(`${idx + 1}: ${line}`);
      if (endRegex && endRegex.test(line) && result.length > 5) recording = false;
    }
  });
  console.log(`=== ${filePath} ===`);
  console.log(result.slice(0, 60).join('\n'));
}

inspectSection('index.html', /id="comparison"/i, /<\/table>/i);
