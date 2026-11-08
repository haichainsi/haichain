const fs = require('fs');

function fixLastOne(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  const m1 = content.search(/\$\{isVi\s*\?\s*`Ví/);
  console.log('m1 in', filePath, ':', m1);
  if (m1 !== -1) {
    const end1 = content.indexOf('Transfer-Hook active until TGE.`}', m1);
    if (end1 !== -1) {
      const fullEnd = end1 + 'Transfer-Hook active until TGE.`}'.length;
      const replacement1 = '<strong class="text-black dark:text-white">${shortAddr}</strong>: <strong class="text-black dark:text-white font-bold underline">${haiTotal.toLocaleString()} $HAISI</strong> ($${paidUsdt.toLocaleString()} USDT) • Token-2022 Transfer-Hook Locked';
      content = content.substring(0, m1) + replacement1 + content.substring(fullEnd);
    }
  }

  fs.writeFileSync(filePath, content, 'utf8');
}

fixLastOne('dashboard.html');
fixLastOne('app/dashboard.html');
console.log('Done!');
