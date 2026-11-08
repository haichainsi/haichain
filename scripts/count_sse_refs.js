const fs = require('fs');

['i18n.js', 'app/i18n.js', 'dashboard.html', 'app/dashboard.html'].forEach(f => {
  if (!fs.existsSync(f)) return;
  const c = fs.readFileSync(f, 'utf8');
  const count = (c.match(/mcp\.haichain\.si\/sse/g) || []).length;
  console.log(f, 'count of mcp.haichain.si/sse:', count);
});
