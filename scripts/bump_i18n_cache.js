const fs = require('fs');

const files = ['dashboard.html', 'app/dashboard.html', 'index.html', 'app/index.html'];
const newVer = 'v28_cloud_mcp_streamable_http_' + Date.now();

files.forEach(f => {
  if (!fs.existsSync(f)) return;
  let c = fs.readFileSync(f, 'utf8');
  c = c.replace(/i18n\.js(\?v=[a-zA-Z0-9_\-]+)?/g, 'i18n.js?v=' + newVer);
  fs.writeFileSync(f, c, 'utf8');
  console.log('Bumped i18n.js in', f);
});
