const fs = require('fs');

function patchPlayground(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  content = content.replace(
    '<span>Quick Demos:</span>',
    '<span data-i18n="playground.quickDemos">Quick Demos:</span>'
  );
  content = content.replace(
    '<span class="truncate">Anti-Drain</span>',
    '<span class="truncate" data-i18n="playground.demoAntiDrain">Anti-Drain</span>'
  );
  content = content.replace(
    '<span class="truncate">Micro-Escrow</span>',
    '<span class="truncate" data-i18n="playground.demoMicroEscrow">Micro-Escrow</span>'
  );
  content = content.replace(
    '<span class="truncate">Optimus AI</span>',
    '<span class="truncate" data-i18n="playground.demoOptimus">Optimus AI</span>'
  );
  content = content.replace(
    '<span class="truncate">Anchor CPI</span>',
    '<span class="truncate" data-i18n="playground.demoAnchor">Anchor CPI</span>'
  );

  fs.writeFileSync(filePath, content, 'utf8');
}

patchPlayground('dashboard.html');
patchPlayground('app/dashboard.html');
console.log('Playground patched');
