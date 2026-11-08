const fs = require('fs');

function cleanLines(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  const oldBlock = `        if (typeof showToast === 'function') {
          showToast({
            title: getDashNotice('insufficientVaultBalance'),
            message: getDashNotice('vaultBalanceInsufficientForTask')
              : \`Vault balance (\$\${balance.toFixed(4)}) is insufficient for \$\${selectedCost.toFixed(4)}. Please top up via Devnet Faucet.\`,
            icon: 'alert-circle'
          });
        }
        alert(isVi
          ? \`Số dư không đủ!\\n\\nSố dư Master Vault của bạn hiện tại là \$\${balance.toFixed(4)} USDT.\\nTác vụ AI "\${selectedModel}" yêu cầu tối thiểu \$\${selectedCost.toFixed(4)} USDT.\\n\\nVui lòng nạp thêm tiền thử nghiệm qua Faucet để tiếp tục.\`
          : \`Insufficient Vault Balance!\\n\\nYour Master Vault balance is \$\${balance.toFixed(4)} USDT.\\nSelected model "\${selectedModel}" requires \$\${selectedCost.toFixed(4)} USDT.\\n\\nPlease claim test funds via Faucet to execute.\`);
        return;`;

  const newBlock = `        if (typeof showToast === 'function') {
          showToast({
            title: getDashNotice('insufficientVaultBalance'),
            message: getDashNotice('vaultBalanceInsufficientForTask'),
            icon: 'alert-circle'
          });
        }
        alert(getDashNotice('vaultBalanceInsufficientForTask'));
        return;`;

  if (content.includes(oldBlock)) {
    content = content.replace(oldBlock, newBlock);
    console.log('Successfully replaced oldBlock in', filePath);
  } else {
    console.log('oldBlock not matched directly, trying normalized newlines');
    const normContent = content.replace(/\r\n/g, '\n');
    const normOld = oldBlock.replace(/\r\n/g, '\n');
    if (normContent.includes(normOld)) {
      content = normContent.replace(normOld, newBlock);
      console.log('Successfully replaced normalized oldBlock in', filePath);
    } else {
      console.log('Still not matched!');
    }
  }

  fs.writeFileSync(filePath, content, 'utf8');
}

cleanLines('dashboard.html');
cleanLines('app/dashboard.html');
