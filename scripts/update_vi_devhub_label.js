const fs = require('fs');

['i18n.js', 'app/i18n.js'].forEach(filePath => {
  let content = fs.readFileSync(filePath, 'utf8');
  if (content.includes('"nav.devHub": "Trung Tâm Lập Trình & MCP"')) {
    content = content.replace(
      '"nav.devHub": "Trung Tâm Lập Trình & MCP"',
      '"nav.devHub": "Lập Trình & MCP"'
    );
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`[OK] Updated nav.devHub in ${filePath}`);
  } else {
    console.warn(`[WARN] Target string not found in ${filePath}`);
  }
});

// Bump cachebuster to v61_devhub_vi_label_clean
const files = ['index.html', 'app/index.html', 'dashboard.html', 'app/dashboard.html'];
const newVersion = 'v61_devhub_vi_label_clean';

files.forEach(filePath => {
  if (!fs.existsSync(filePath)) return;
  let content = fs.readFileSync(filePath, 'utf8');
  content = content.replace(/i18n\.js\?v=[a-zA-Z0-9_\.-]+/g, `i18n.js?v=${newVersion}`);
  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`[OK] Bumped cachebuster in ${filePath} to ${newVersion}`);
});
