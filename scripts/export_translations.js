
const fs = require('fs');
const content = fs.readFileSync('i18n.js', 'utf8');
const start = content.indexOf('const TRANSLATIONS = {');
const end = content.indexOf('function getInitialLanguage()');
let code = content.slice(start, end).trim();
if (code.endsWith(';')) code = code.slice(0, -1);
code = code.replace('const TRANSLATIONS =', 'const TRANSLATIONS =');
const t = eval('(() => { ' + code + '; return TRANSLATIONS; })()');

const keys = Object.keys(t.en).filter(k => k.startsWith('dev.') || k.startsWith('mcp.') || k.startsWith('btn.'));
const res = {};
for (const k of keys) {
  res[k] = {};
  for (const lang of Object.keys(t)) {
    res[k][lang] = t[lang][k];
  }
}
fs.writeFileSync('scripts/dev_mcp_all_langs.json', JSON.stringify(res, null, 2), 'utf8');
console.log('Successfully exported ' + keys.length + ' keys to scripts/dev_mcp_all_langs.json');
