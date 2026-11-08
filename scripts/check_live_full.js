const https = require('https');

https.get('https://haichain.si/dashboard.html?cb=' + Date.now(), res => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const idx = data.indexOf('"noWeb3DetectedFaucetGuide"');
    console.log('Live contains noWeb3DetectedFaucetGuide:', idx !== -1);
    if (idx !== -1) {
      console.log('Snippet:', data.substring(idx, idx + 250));
    }
    console.log('Live contains v21_fix_alert_body:', data.includes('v21_fix_alert_body'));
  });
});
