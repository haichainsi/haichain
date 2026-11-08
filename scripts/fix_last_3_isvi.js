const fs = require('fs');

function fixLast3(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  // 1. Banner in vesting overview card
  const target1 = `\${isVi 
                ? \`Ví <strong class="text-black dark:text-white">\${shortAddr}</strong> đang sở hữu <strong class="text-black dark:text-white font-bold underline">\${haiTotal.toLocaleString()} \$HAISI</strong> (\$\${paidUsdt.toLocaleString()} USDT). Khóa chuyển nhượng on-chain đến ngày TGE.\`
                : \`Investor <strong class="text-black dark:text-white">\${shortAddr}</strong> holds <strong class="text-black dark:text-white font-bold underline">\${haiTotal.toLocaleString()} \$HAISI</strong> (\$\${paidUsdt.toLocaleString()} USDT). Transfer-Hook locked until TGE.\`}`;
  
  // Also regex to be flexible with CRLF and whitespace
  const regex1 = /\$\{isVi\s*\?\s*`Ví <strong class="text-black dark:text-white">\$\{shortAddr\}<\/strong>[\s\S]*?Transfer-Hook locked until TGE\.`\}/;
  content = content.replace(regex1, `<strong class="text-black dark:text-white">\${shortAddr}</strong>: <strong class="text-black dark:text-white font-bold underline">\${haiTotal.toLocaleString()} \$HAISI</strong> (\$\${paidUsdt.toLocaleString()} USDT) • Token-2022 Transfer-Hook Locked`);

  // 2. Playground toast message
  const regex2 = /message:\s*isVi\s*\?\s*`Số dư Master Vault \(\$\$\{balance\.toFixed\(4\)\}\) không đủ cho tác vụ \$\$\{selectedCost\.toFixed\(4\)\}\. Vui lòng nạp thêm qua Faucet Devnet\.`\s*:\s*`Vault balance \(\$\$\{balance\.toFixed\(4\)\}\) is insufficient for \$\$\{selectedCost\.toFixed\(4\)\}\. Please top up via Faucet\.`/;
  content = content.replace(regex2, `message: getDashNotice('vaultBalanceInsufficientForTask')`);

  // 3. Playground alert message
  const regex3 = /alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault của bạn hiện tại là \$\$\{balance\.toFixed\(4\)\} USDT\.[\s\S]*?để tiếp tục\.`\s*:\s*`Insufficient Balance![\s\S]*?to continue\.`\s*\);/;
  content = content.replace(regex3, `alert(getDashNotice('vaultBalanceInsufficientForTask'));`);

  fs.writeFileSync(filePath, content, 'utf8');
  console.log('Fixed last 3 in:', filePath);
}

fixLast3('dashboard.html');
fixLast3('app/dashboard.html');
