const https = require('https');

https.get(`https://haichain.si/app/dashboard?t=${Date.now()}`, { headers: { 'Cache-Control': 'no-cache, no-store' } }, res => {
  let data = '';
  res.on('data', c => data += c);
  res.on('end', () => {
    console.log('Total length:', data.length);
    const m = data.match(/i18n\.js\?v=([^\"]+)/);
    console.log('Cachebuster version:', m ? m[1] : 'not found');
    let pos = 0;
    while ((pos = data.indexOf('tab-mcp', pos)) !== -1) {
      console.log('Match at', pos, ':', data.slice(pos - 40, pos + 60));
      pos += 7;
    }
    process.exit(0);
  });
});
