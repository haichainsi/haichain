const fs = require('fs');

function enhanceWeb3DepositUX(file) {
  let content = fs.readFileSync(file, 'utf8');

  // 1. In (!activeWeb3)
  const pattern1 = "alert(getDashNotice('noWeb3DetectedFaucetGuide'));\r\n            return;";
  const pattern1LF = "alert(getDashNotice('noWeb3DetectedFaucetGuide'));\n            return;";
  const repl1 = "alert(getDashNotice('noWeb3DetectedFaucetGuide'));\r\n            if (dashPayTabFaucet) dashPayTabFaucet.click();\r\n            return;";

  if (content.includes(pattern1)) {
    content = content.replace(pattern1, repl1);
    console.log('Applied repl1 (CRLF) in', file);
  } else if (content.includes(pattern1LF)) {
    content = content.replace(pattern1LF, repl1.replace(/\r\n/g, '\n'));
    console.log('Applied repl1 (LF) in', file);
  } else {
    console.warn('pattern1 not found in', file);
  }

  // 2. In (!phantom)
  const pattern2 = "alert(getDashNotice('web3Disconnected'));\r\n          updateDepositWalletBanner();\r\n          return;";
  const pattern2LF = "alert(getDashNotice('web3Disconnected'));\n          updateDepositWalletBanner();\n          return;";
  const repl2 = "alert(getDashNotice('noWeb3DetectedFaucetGuide'));\r\n          if (dashPayTabFaucet) dashPayTabFaucet.click();\r\n          updateDepositWalletBanner();\r\n          return;";

  if (content.includes(pattern2)) {
    content = content.replace(pattern2, repl2);
    console.log('Applied repl2 (CRLF) in', file);
  } else if (content.includes(pattern2LF)) {
    content = content.replace(pattern2LF, repl2.replace(/\r\n/g, '\n'));
    console.log('Applied repl2 (LF) in', file);
  } else {
    console.warn('pattern2 not found in', file);
  }

  // 3. In depositConnectBtn else
  const pattern3 = "dashboardDepositModal.classList.add('hidden');\r\n          walletConnectModal.classList.remove('hidden');";
  const pattern3LF = "dashboardDepositModal.classList.add('hidden');\n          walletConnectModal.classList.remove('hidden');";
  const repl3 = "alert(getDashNotice('noWeb3DetectedFaucetGuide'));\r\n          if (dashPayTabFaucet) dashPayTabFaucet.click();";

  if (content.includes(pattern3)) {
    content = content.replace(pattern3, repl3);
    console.log('Applied repl3 (CRLF) in', file);
  } else if (content.includes(pattern3LF)) {
    content = content.replace(pattern3LF, repl3.replace(/\r\n/g, '\n'));
    console.log('Applied repl3 (LF) in', file);
  } else {
    console.warn('pattern3 not found in', file);
  }

  fs.writeFileSync(file, content, 'utf8');
}

enhanceWeb3DepositUX('dashboard.html');
enhanceWeb3DepositUX('app/dashboard.html');
