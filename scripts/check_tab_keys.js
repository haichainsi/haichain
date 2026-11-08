const fs = require('fs');

function checkFile(path) {
  console.log('=== Checking', path, '===');
  const js = fs.readFileSync(path, 'utf8');
  const lines = js.split('\n');
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes('aiHub.tabDesktop') || lines[i].includes('aiHub.tabOnline') || lines[i].includes('aiHub.tabWeb')) {
      console.log(`${i+1}: ${lines[i].trim()}`);
    }
  }
}

checkFile('i18n.js');
checkFile('app/i18n.js');
