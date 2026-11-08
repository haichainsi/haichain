const fs = require('fs');

const files = ['dashboard.html', 'app/dashboard.html', 'index.html', 'app/index.html'];
const newVer = 'v21_fix_alert_body_' + Date.now();

files.forEach(f => {
  if (!fs.existsSync(f)) return;
  let c = fs.readFileSync(f, 'utf8');
  
  // dialog.js bump
  c = c.replace(/dialog\.js(\?v=[a-zA-Z0-9_\-]+)?/g, 'dialog.js?v=' + newVer);
  
  // sale-controller.js bump
  c = c.replace(/sale-controller\.js(\?v=[a-zA-Z0-9_\-]+)?/g, 'sale-controller.js?v=' + newVer);
  
  fs.writeFileSync(f, c, 'utf8');
  console.log('Bumped cachebuster in', f);
});
