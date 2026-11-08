const fs = require('fs');

function patchGetDashNotice(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  const oldCode = `    function getDashNotice(key) {
      const lang = window.haichainI18n ? window.haichainI18n.current() : 'en';
      const dict = DASH_NOTICES_I18N[lang] || DASH_NOTICES_I18N['en'];
      return dict[key] || DASH_NOTICES_I18N['en'][key] || '';
    }`;

  const newCode = `    function getDashNotice(key) {
      const lang = window.haichainI18n ? window.haichainI18n.current() : 'en';
      const dict = DASH_NOTICES_I18N[lang] || DASH_NOTICES_I18N['en'] || {};
      const enDict = DASH_NOTICES_I18N['en'] || {};
      const viDict = DASH_NOTICES_I18N['vi'] || {};
      return dict[key] || enDict[key] || viDict[key] || key;
    }`;

  if (content.includes(oldCode)) {
    content = content.replace(oldCode, newCode);
    fs.writeFileSync(filePath, content, 'utf8');
    console.log('Successfully updated getDashNotice in', filePath);
  } else {
    console.log('Target oldCode not found in', filePath, 'checking alternative pattern...');
    const regex = /function getDashNotice\(key\)\s*\{[\s\S]*?return dict\[key\][\s\S]*?;\s*\}/;
    if (regex.test(content)) {
      content = content.replace(regex, `function getDashNotice(key) {
      const lang = window.haichainI18n ? window.haichainI18n.current() : 'en';
      const dict = DASH_NOTICES_I18N[lang] || DASH_NOTICES_I18N['en'] || {};
      const enDict = DASH_NOTICES_I18N['en'] || {};
      const viDict = DASH_NOTICES_I18N['vi'] || {};
      return dict[key] || enDict[key] || viDict[key] || key;
    }`);
      fs.writeFileSync(filePath, content, 'utf8');
      console.log('Successfully updated getDashNotice with regex in', filePath);
    } else {
      console.error('Could not find getDashNotice in', filePath);
    }
  }
}

patchGetDashNotice('dashboard.html');
patchGetDashNotice('app/dashboard.html');
