const fs = require('fs');
const path = require('path');

// Check sample bytes of PNG to see if it has transparent or white/black
const dir = path.join(__dirname, 'assets', 'branding');
['logo haichain  (2) (1).png', 'logo haichain  (2) (2).png', 'Logo công nghệ tối giản HAICHAIN.SI.png', 'Logo công nghệ tương lai HAICHAIN.SI.png', 'logo haichain .png', 'logo haichain  (1).png'].forEach(f => {
  const p = path.join(dir, f);
  if (fs.existsSync(p)) {
    const stats = fs.statSync(p);
    console.log(`${f}: size ${stats.size} bytes`);
  }
});
