const fs = require('fs');

function applyFix(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  // Match 1
  const search1 = '${isVi \n                ? `Ví <strong class="text-black dark:text-white">${shortAddr}</strong> đang sở hữu <strong class="text-black dark:text-white font-bold underline">${haiTotal.toLocaleString()} $HAISI</strong> ($${paidUsdt.toLocaleString()} USDT). Khóa chuyển nhượng on-chain đến ngày TGE.`\n                : `Investor <strong class="text-black dark:text-white">${shortAddr}</strong> holds <strong class="text-black dark:text-white font-bold underline">${haiTotal.toLocaleString()} $HAISI</strong> ($${paidUsdt.toLocaleString()} USDT). Transfer-Hook locked until TGE.`}';
  const replace1 = '<strong class="text-black dark:text-white">${shortAddr}</strong>: <strong class="text-black dark:text-white font-bold underline">${haiTotal.toLocaleString()} $HAISI</strong> ($${paidUsdt.toLocaleString()} USDT) • Token-2022 Transfer-Hook Locked';

  // Also handle CRLF if needed
  content = content.replace(search1, replace1);
  content = content.replace(search1.replace(/\n/g, '\r\n'), replace1);

  // Match 2
  const search2 = 'message: isVi \n              ? `Số dư Master Vault ($${balance.toFixed(4)}) không đủ cho tác vụ $${selectedCost.toFixed(4)}. Vui lòng nạp thêm qua Faucet Devnet.`\n              : `Vault balance ($${balance.toFixed(4)}) is insufficient for $${selectedCost.toFixed(4)}. Please top up via Faucet.`';
  const replace2 = 'message: getDashNotice("vaultBalanceInsufficientForTask")';

  content = content.replace(search2, replace2);
  content = content.replace(search2.replace(/\n/g, '\r\n'), replace2);

  // Match 3
  const search3 = 'alert(isVi\n          ? `Số dư không đủ!\\n\\nSố dư Master Vault của bạn hiện tại là $${balance.toFixed(4)} USDT.\\nTác vụ AI "${selectedModel}" yêu cầu tối thiểu $${selectedCost.toFixed(4)} USDT.\\n\\nVui lòng nạp thêm tiền thử nghiệm qua Faucet để tiếp tục.`\n          : `Insufficient Balance!\\n\\nYour current Master Vault balance is $${balance.toFixed(4)} USDT.\\nThe AI task "${selectedModel}" requires at least $${selectedCost.toFixed(4)} USDT.\\n\\nPlease top up test funds via Faucet to continue.`\n        );';
  const replace3 = 'alert(getDashNotice("vaultBalanceInsufficientForTask"));';

  content = content.replace(search3, replace3);
  content = content.replace(search3.replace(/\n/g, '\r\n'), replace3);

  fs.writeFileSync(filePath, content, 'utf8');
  console.log('Processed:', filePath);
}

applyFix('dashboard.html');
applyFix('app/dashboard.html');
