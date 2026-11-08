const fs = require('fs');
const files = ['dashboard.html', 'index.html', 'sale-controller.js', 'i18n.js'];
files.forEach(f => {
  if (fs.existsSync(f)) {
    const content = fs.readFileSync(f, 'utf8');
    if (content.includes('HAICHAIN System') || content.includes('AUTONOMOUS KERNEL')) {
      console.log('Found in', f);
      let idx = content.indexOf('AUTONOMOUS KERNEL');
      if (idx !== -1) {
        console.log(content.substring(idx - 200, idx + 400));
      }
    }
  }
});
