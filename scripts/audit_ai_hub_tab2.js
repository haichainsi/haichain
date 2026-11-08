const fs = require('fs');
const content = fs.readFileSync('dashboard.html', 'utf8');

const idx = content.indexOf('<!-- ================= TAB 2: CLAUDE.AI ONLINE (STREAMABLE HTTP & SSE) ================= -->');
if (idx === -1) {
  const idx2 = content.indexOf('hub-section-online');
  console.log(content.substring(idx2 - 100, idx2 + 3000));
} else {
  console.log(content.substring(idx, idx + 3000));
}
