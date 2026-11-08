const fs = require('fs');

const i18nCode = fs.readFileSync('i18n.js', 'utf8');

const mockWindow = {
  location: { search: '?lang=es', origin: 'https://haichain.si' },
  localStorage: { getItem: () => 'es', setItem: () => {} },
  navigator: { language: 'es' },
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
const viPattern = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]/;

['es', 'fr'].forEach(lang => {
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
  console.log(`\n=================== ${lang.toUpperCase()} DETAILS ===================`);
  lines.forEach((l, idx) => {
    if (viPattern.test(l)) {
      console.log(`L${idx + 1}: ${l.trim().substring(0, 120)}`);
    }
  });
});
