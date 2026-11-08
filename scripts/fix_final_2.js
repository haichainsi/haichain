const fs = require('fs');

function fixFinal2(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  // Block 1: search by unique substring
  const m1 = content.search(/\$\{isVi\s*\?\s*`Ví/);
  console.log('m1:', m1);
  if (m1 !== -1) {
    const end1 = content.indexOf('Transfer-Hook locked until TGE.`}', m1);
    console.log('end1:', end1);
    if (end1 !== -1) {
      const fullEnd = end1 + 'Transfer-Hook locked until TGE.`}'.length;
      const replacement1 = '<strong class="text-black dark:text-white">${shortAddr}</strong>: <strong class="text-black dark:text-white font-bold underline">${haiTotal.toLocaleString()} $HAISI</strong> ($${paidUsdt.toLocaleString()} USDT) • Token-2022 Transfer-Hook Locked';
      content = content.substring(0, m1) + replacement1 + content.substring(fullEnd);
    }
  }

  // Block 2: search by unique substring
  const m2 = content.search(/message:\s*isVi\s*\?\s*`Số dư Master Vault/);
  console.log('m2:', m2);
  if (m2 !== -1) {
    const end2 = content.indexOf('Faucet', m2);
    console.log('end2:', end2);
    if (end2 !== -1) {
      const fullEnd = content.indexOf('`', end2) + 1;
      const replacement2 = "message: getDashNotice('vaultBalanceInsufficientForTask')";
      content = content.substring(0, m2) + replacement2 + content.substring(fullEnd);
    }
  }

  fs.writeFileSync(filePath, content, 'utf8');
}

fixFinal2('dashboard.html');
fixFinal2('app/dashboard.html');
