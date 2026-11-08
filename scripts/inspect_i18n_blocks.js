const fs = require('fs');
const lines = fs.readFileSync('i18n.js', 'utf8').split('\n');

function inspectLang(lang, startLine) {
  console.log('=== ' + lang + ' ===');
  for (let i = startLine; i < startLine + 400 && i < lines.length; i++) {
    const l = lines[i];
    if (l.includes('"cluster.auditsPassed"') || l.includes('"footer.compliance"') || l.includes('"comp.colTao"') || l.includes('"comp.row4Hai"') || l.includes('"aud.investorFutureDesc"')) {
      console.log((i+1) + ': ' + l.trim());
    }
  }
}

inspectLang('en', 500);
inspectLang('vi', 3236);
