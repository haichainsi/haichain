const fs = require('fs');
const content = fs.readFileSync('i18n.js', 'utf8');

// Load window.HAICHAIN_I18N_DATA
let data;
const sandbox = { 
  window: {
    addEventListener: () => {},
    location: { search: '' }
  }, 
  document: { 
    addEventListener: () => {}, 
    documentElement: { lang: 'en' },
    querySelectorAll: () => []
  },
  navigator: { language: 'en-US' },
  localStorage: { getItem: () => null, setItem: () => {} }
};
sandbox.window.document = sandbox.document;
try {
  const fn = new Function('window', 'document', 'navigator', 'localStorage', content + '; return window.HAICHAIN_I18N_DATA || window.haichainTranslations || window.TRANSLATIONS;');
  data = fn(sandbox.window, sandbox.document, sandbox.navigator, sandbox.localStorage);
} catch (e) {
  console.log('Error evaluating i18n.js:', e.message);
}

if (!data && sandbox.window.haichainTranslations) {
  data = sandbox.window.haichainTranslations;
}

if (data) {
  const langs = Object.keys(data);
  console.log('Languages in i18n:', langs);
  const enKeys = Object.keys(data['en'] || {});
  console.log('Total keys in EN:', enKeys.length);
  const devKeys = enKeys.filter(k => /dev|mcp|doc|step|paywall|sdk|code/i.test(k));
  console.log('Developer-related keys count:', devKeys.length);
  devKeys.forEach(k => {
    console.log(`[${k}]`);
    console.log('  EN:', data['en'][k]);
    console.log('  VI:', (data['vi'] || {})[k]);
  });
} else {
  console.log('Could not extract data object directly, checking keys in file');
}
