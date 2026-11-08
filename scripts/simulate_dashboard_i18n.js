const fs = require('fs');

// Read i18n.js
const i18nCode = fs.readFileSync('i18n.js', 'utf8');

// Mock browser environment for i18n.js
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

// Evaluate i18n.js
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

console.log('haichainI18n loaded successfully!');

// Now read dashboard.html
let html = fs.readFileSync('dashboard.html', 'utf8');

// Test for several languages
const testLangs = ['zh', 'en', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he'];
const viPattern = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]/;

for (const lang of testLangs) {
  haichainI18n.setLanguage(lang);
  
  // Replace all [data-i18n="..."] in HTML with translation
  let translatedHtml = html.replace(/<([a-zA-Z0-9\-]+)([^>]*data-i18n="([^"]+)"[^>]*)>([\s\S]*?)<\/\1>/gi, (match, tag, attrs, key, inner) => {
    const val = haichainI18n.t(key);
    if (val !== undefined && val !== null) {
      return `<${tag}${attrs}>${val}</${tag}>`;
    }
    return match;
  });

  // Remove <script> and <style>
  const bodyTextWithoutScripts = translatedHtml
    .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
    .replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, '')
    .replace(/<!--[\s\S]*?-->/g, '');

  // Find any lines in body that contain Vietnamese characters
  const lines = bodyTextWithoutScripts.split('\n');
  const viMatches = [];
  lines.forEach((l, idx) => {
    if (viPattern.test(l)) {
      viMatches.push({ line: idx + 1, text: l.trim() });
    }
  });

  console.log(`Lang ${lang}: ${viMatches.length} lines with Vietnamese remaining.`);
  if (lang === 'zh') {
    viMatches.forEach(m => console.log(`  L${m.line}: ${m.text.substring(0, 110)}`));
  }
}
