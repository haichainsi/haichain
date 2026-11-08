const fs = require('fs');

const files = ['dashboard.html', 'app/dashboard.html', 'index.html', 'app/index.html'];

files.forEach(f => {
  if (fs.existsSync(f)) {
    let content = fs.readFileSync(f, 'utf8');
    content = content.replace(/i18n\.js\?v=[^"']+/g, 'i18n.js?v=v26_global_10lang_unification');
    content = content.replace(/sale-controller\.js\?v=[^"']+/g, 'sale-controller.js?v=v26_global_10lang_unification');
    fs.writeFileSync(f, content, 'utf8');
    console.log('Bumped cache version in:', f);
  }
});
