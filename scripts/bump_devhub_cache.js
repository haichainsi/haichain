const fs = require('fs');

const files = ['index.html', 'app/index.html', 'dashboard.html', 'app/dashboard.html'];
const newVersion = 'v60_unified_dev_hub';

files.forEach(filePath => {
  if (!fs.existsSync(filePath)) return;
  let content = fs.readFileSync(filePath, 'utf8');
  let updated = false;

  // Replace i18n.js?v=...
  if (content.includes('i18n.js?v=')) {
    content = content.replace(/i18n\.js\?v=[a-zA-Z0-9_\.-]+/g, `i18n.js?v=${newVersion}`);
    updated = true;
  }

  // Also if there's dashboard.js?v= or similar
  if (content.includes('dashboard.js?v=')) {
    content = content.replace(/dashboard\.js\?v=[a-zA-Z0-9_\.-]+/g, `dashboard.js?v=${newVersion}`);
    updated = true;
  }

  if (updated) {
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`[OK] Bumped cachebuster in ${filePath} to ${newVersion}`);
  }
});
