const fs = require('fs');

function updateGetDashNotice(file) {
  let content = fs.readFileSync(file, 'utf8');
  const target = `    function getDashNotice(key) {\n      const lang = window.haichainI18n ? window.haichainI18n.current() : 'en';\n      const dict = DASH_NOTICES_I18N[lang] || DASH_NOTICES_I18N['en'];\n      return dict[key] || DASH_NOTICES_I18N['en'][key] || '';\n    }`;

  // also handle CRLF
  const targetCRLF = target.replace(/\n/g, '\r\n');

  const replacement = `    function getDashNotice(key) {\n      const lang = window.haichainI18n ? window.haichainI18n.current() : 'en';\n      const dict = DASH_NOTICES_I18N[lang] || DASH_NOTICES_I18N['en'] || {};\n      const enDict = DASH_NOTICES_I18N['en'] || {};\n      const viDict = DASH_NOTICES_I18N['vi'] || {};\n      return dict[key] || enDict[key] || viDict[key] || key;\n    }`;

  if (content.includes(target)) {
    content = content.replace(target, replacement);
    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated LF in', file);
  } else if (content.includes(targetCRLF)) {
    content = content.replace(targetCRLF, replacement.replace(/\n/g, '\r\n'));
    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated CRLF in', file);
  } else {
    console.error('Target not found in', file);
  }
}

updateGetDashNotice('dashboard.html');
updateGetDashNotice('app/dashboard.html');
