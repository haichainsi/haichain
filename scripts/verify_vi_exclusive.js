const fs = require('fs');

const i18nCode = fs.readFileSync('i18n.js', 'utf8');

const mockWindow = {
  location: { search: '?lang=zh', origin: 'https://haichain.si' },
  localStorage: { getItem: () => 'zh', setItem: () => {} },
  navigator: { language: 'zh' },
  dispatchEvent: () => {},
  addEventListener: () => {}
};
const mockDocument = {
  documentElement: { setAttribute: () => {} },
  body: { style: {}, appendChild: () => {} },
  querySelectorAll: () => [],
  querySelector: () => null,
  getElementById: () => null,
  createElement: () => ({ setAttribute: () => {}, appendChild: () => {}, innerHTML: '', firstElementChild: {} }),
  head: { appendChild: () => {} },
  addEventListener: () => {},
  title: ''
};

const vm = require('vm');
const context = vm.createContext({
  window: mockWindow,
  document: mockDocument,
  location: mockWindow.location,
  localStorage: mockWindow.localStorage,
  navigator: mockWindow.navigator,
  CustomEvent: class {},
  URL: URL,
  console: console
});

vm.runInContext(i18nCode, context);
const haichainI18n = context.window.haichainI18n;

let html = fs.readFileSync('dashboard.html', 'utf8');

const testLangs = ['zh', 'en', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he'];
// Vietnamese-exclusive diacritics
const viOnlyPattern = /[ăắằẳẵặâấầẩẫậđêếềểễệơớờởỡợưứừửữựảãạẻẽẹỉĩịỏõọủũụỳỷỹỵĐ]/;

for (const lang of testLangs) {
  haichainI18n.setLanguage(lang);
  let translatedHtml = html.replace(/<([a-zA-Z0-9\-]+)([^>]*data-i18n="([^"]+)"[^>]*)>([\s\S]*?)<\/\1>/gi, (match, tag, attrs, key, inner) => {
    const val = haichainI18n.t(key);
    if (val !== undefined && val !== null) {
      return `<${tag}${attrs}>${val}</${tag}>`;
    }
    return match;
  });

  const bodyTextWithoutScripts = translatedHtml
    .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
    .replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, '')
    .replace(/<!--[\s\S]*?-->/g, '');

  const lines = bodyTextWithoutScripts.split('\n');
  const viMatches = [];
  lines.forEach((l, idx) => {
    if (viOnlyPattern.test(l)) {
      viMatches.push({ line: idx + 1, text: l.trim() });
    }
  });

  console.log(`Lang ${lang}: ${viMatches.length} Vietnamese-exclusive lines.`);
  if (viMatches.length > 0) {
    viMatches.forEach(m => console.log(`  L${m.line}: ${m.text.substring(0, 110)}`));
  }
}
