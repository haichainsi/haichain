const fs = require('fs');

function fixFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  // Fix favicon
  content = content.replace('href="../assets/icon.png"', 'href="/assets/icon.png"');

  // Fix official logo with error fallback
  content = content.replace(
    /src="\/assets\/haichain-official-logo\.png\?v=geom2026_v4" alt="HAICHAIN"([^>]*)>/g,
    'src="/assets/haichain-official-logo.png?v=geom2026_v4" alt="HAICHAIN"$1 onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src=\'/app/assets/haichain-official-logo.png?v=geom2026_v4\';}">'
  );

  // Fix haisi icon with error fallback
  content = content.replace(
    /src="\/assets\/haisi-icon\.png" alt="HAISI"([^>]*)>/g,
    'src="/assets/haisi-icon.png" alt="HAISI"$1 onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src=\'/app/assets/haisi-icon.png\';}">'
  );

  // Fix video sources
  if (content.includes('trailer-hai-web.mp4') && !content.includes('/app/assets/trailer-hai-web.mp4')) {
    content = content.replace(
      '<source src="/assets/trailer-hai-web.mp4" type="video/mp4">',
      '<source src="/assets/trailer-hai-web.mp4" type="video/mp4">\n        <source src="/app/assets/trailer-hai-web.mp4" type="video/mp4">\n        <source src="assets/trailer-hai-web.mp4" type="video/mp4">'
    );
  }

  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Updated ${filePath}`);
}

fixFile('app/index.html');
fixFile('app/dashboard.html');

// Now copy updated files to root
fs.copyFileSync('app/index.html', 'index.html');
fs.copyFileSync('app/dashboard.html', 'dashboard.html');
console.log('Synchronized index.html and dashboard.html to root');
