const fs = require('fs');

const files = ['index.html', 'dashboard.html', 'app/index.html', 'app/dashboard.html'];

files.forEach(f => {
  if (!fs.existsSync(f)) return;
  let content = fs.readFileSync(f, 'utf8');
  content = content.replace(
    /\/app\/i18n\.js\?v=[^"']*/g,
    '/app/i18n.js?v=v29_institutional_audit_upgrade_1793593000000'
  );
  content = content.replace(
    /\/app\/sale-controller\.js\?v=[^"']*/g,
    '/app/sale-controller.js?v=v23_institutional_calculator_clean_1793593000000'
  );
  fs.writeFileSync(f, content, 'utf8');
  console.log(`Bumped cache-busters in ${f}`);
});
