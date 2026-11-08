const fs = require('fs');

const elCode = fs.readFileSync('scripts/eliminate_all_remaining_isvi.js', 'utf8');
const p1 = elCode.indexOf('const EXTRA_NOTICES =');
const pEnd1 = elCode.indexOf('function patchFile', p1);
const extraCode = elCode.substring(p1, pEnd1).replace('const EXTRA_NOTICES =', 'var EXTRA_NOTICES =');
eval(extraCode);

const mmCode = fs.readFileSync('scripts/patch_final_isvi.js', 'utf8');
const p2 = mmCode.indexOf('const MM_KEYS =');
const pEnd2 = mmCode.indexOf('function patchFinal', p2);
const mmSnippet = mmCode.substring(p2, pEnd2).replace('const MM_KEYS =', 'var MM_KEYS =');
eval(mmSnippet);

const langs = ['kk', 'en', 'zh', 'vi', 'ko', 'fr', 'es', 'ru', 'hi', 'he'];
const ALL_EXTRA = {};
langs.forEach(lang => {
  ALL_EXTRA[lang] = Object.assign({}, EXTRA_NOTICES[lang] || {}, MM_KEYS[lang] || {});
});

function injectFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');
  const dashStart = content.indexOf('const DASH_NOTICES_I18N =');
  const dashEnd = content.indexOf('function getDashNotice', dashStart);
  let dashBlock = content.substring(dashStart, dashEnd);

  langs.forEach(lang => {
    const searchPattern = `"${lang}": {`;
    let pos = dashBlock.indexOf(searchPattern);
    if (pos !== -1) {
      // Find end of this line
      const lineEnd = dashBlock.indexOf('\n', pos) + 1;
      let injectStr = '';
      for (const [k, v] of Object.entries(ALL_EXTRA[lang])) {
        // Find next language or end
        const nextLangIdx = langs.indexOf(lang) < langs.length - 1 ? dashBlock.indexOf(`"${langs[langs.indexOf(lang)+1]}":`, pos + 10) : dashBlock.length;
        const searchRegion = nextLangIdx !== -1 ? dashBlock.substring(pos, nextLangIdx) : dashBlock.substring(pos, pos + 25000);
        if (!searchRegion.includes(`"${k}":`)) {
          injectStr += `    "${k}": ${JSON.stringify(v)},\n`;
        }
      }
      if (injectStr) {
        dashBlock = dashBlock.substring(0, lineEnd) + injectStr + dashBlock.substring(lineEnd);
        console.log(`Injected keys into ${lang} in ${filePath}`);
      }
    } else {
      console.warn(`Pattern for lang ${lang} not found in ${filePath}`);
    }
  });

  content = content.substring(0, dashStart) + dashBlock + content.substring(dashEnd);
  fs.writeFileSync(filePath, content, 'utf8');
}

injectFile('dashboard.html');
injectFile('app/dashboard.html');
console.log('Done injection!');
