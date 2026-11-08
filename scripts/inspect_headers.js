const https = require('https');

https.get(`https://haichain.si/app/i18n.js?v=v61_devhub_vi_label_clean&t=${Date.now()}`, res => {
  console.log('Headers:', res.headers);
  let data = '';
  res.on('data', c => data += c);
  res.on('end', () => {
    console.log('Data length:', data.length);
    console.log('Includes Lap Trinh & MCP:', data.includes('"nav.devHub": "Lập Trình & MCP"'));
    process.exit(0);
  });
});
