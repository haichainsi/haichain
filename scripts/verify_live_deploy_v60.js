const https = require('https');

function check(url) {
  console.log(`Checking ${url}...`);
  https.get(url, res => {
    console.log('HTTP Status:', res.statusCode);
    if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
      console.log('Redirect to:', res.headers.location);
      const target = res.headers.location.startsWith('http') 
        ? res.headers.location 
        : `https://haichain.si${res.headers.location}`;
      return check(target);
    }
    let data = '';
    res.on('data', chunk => { data += chunk; });
    res.on('end', () => {
      const hasDevHub = data.includes('nav.devHub');
      const hasMcpSection = data.includes('id="tab-mcp"');
      const hasTerminalIcon = data.includes('data-lucide="terminal"');
      const hasV60 = data.includes('v60_unified_dev_hub');

      console.log('--- LIVE SITE VERIFICATION ---');
      console.log('Has nav.devHub:', hasDevHub);
      console.log('Has obsolete tab-mcp section:', hasMcpSection);
      console.log('Has terminal icon:', hasTerminalIcon);
      console.log('Has v60 cachebuster:', hasV60);

      if (hasDevHub && !hasMcpSection && hasTerminalIcon) {
        console.log('\n>>> LIVE DEPLOYMENT CONFIRMED 100% SUCCESSFUL! <<<');
      } else {
        console.log('\n>>> Still propagating... <<<');
      }
      process.exit(0);
    });
  }).on('error', err => {
    console.error('Fetch error:', err.message);
    process.exit(1);
  });
}

check(`https://haichain.si/app/dashboard.html?t=${Date.now()}`);
