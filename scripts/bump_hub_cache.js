const fs = require('fs');

const ts = Date.now();
const ver = `v22_hub_transparency_${ts}`;

['dashboard.html', 'app/dashboard.html'].forEach(filePath => {
  let content = fs.readFileSync(filePath, 'utf8');
  content = content.replace(/i18n\.js\?v=[^"']+/g, `i18n.js?v=${ver}`);
  content = content.replace(/dialog\.js\?v=[^"']+/g, `dialog.js?v=${ver}`);
  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Bumped cache in ${filePath} to ${ver}`);
});
