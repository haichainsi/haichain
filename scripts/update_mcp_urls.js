const fs = require('fs');

function updateMcpUrls(file) {
  let content = fs.readFileSync(file, 'utf8');

  // Replace mcp.haichain.si/sse with haichain.si/api/mcp
  const updated = content.replace(/https:\/\/mcp\.haichain\.si\/sse/g, 'https://haichain.si/api/mcp');

  if (content !== updated) {
    fs.writeFileSync(file, updated, 'utf8');
    console.log(`Updated URLs in ${file}`);
  } else {
    console.log(`No URLs to update in ${file}`);
  }
}

['i18n.js', 'app/i18n.js', 'dashboard.html', 'app/dashboard.html'].forEach(updateMcpUrls);
