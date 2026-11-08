const https = require('https');

https.get('https://haichain.si/dashboard?t=' + Date.now(), { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const lines = data.split('\n');
    for (const l of lines) {
      if (l.includes('Desktop App') || l.includes('Claude Mobile') || l.includes('Web Direct')) {
        console.log('LIVE LINE:', l.trim());
      }
    }
  });
});
