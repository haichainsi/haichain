const fs = require('fs');

function patchWeb3DepositUX(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');

  // Regex for target 1
  const re1 = /if\s*\(\s*isMobileDevice\(\)\s*\)\s*\{[\s\S]*?window\.location\.href\s*=\s*'https:\/\/phantom\.com\/ul\/browse\/[\s\S]*?return;\s*\}\s*alert\(getDashNotice\('noWeb3DetectedFaucetGuide'\)\);\s*return;/;

  if (re1.test(content)) {
    content = content.replace(re1, `alert(getDashNotice('noWeb3DetectedFaucetGuide'));
            if (typeof selectDepositTab === 'function') selectDepositTab('faucet');
            return;`);
    console.log('Replaced re1 in', filePath);
  } else {
    console.warn('re1 not matched in', filePath);
  }

  // Regex for target 2 (if (!phantom))
  const re2 = /if\s*\(!phantom\)\s*\{[\s\S]*?alert\(getDashNotice\('web3Disconnected'\)\);[\s\S]*?return;\s*\}/;

  if (re2.test(content)) {
    content = content.replace(re2, `if (!phantom) {
          alert(getDashNotice('noWeb3DetectedFaucetGuide'));
          if (typeof selectDepositTab === 'function') selectDepositTab('faucet');
          updateDepositWalletBanner();
          return;
        }`);
    console.log('Replaced re2 in', filePath);
  } else {
    console.warn('re2 not matched in', filePath);
  }

  fs.writeFileSync(filePath, content, 'utf8');
}

patchWeb3DepositUX('dashboard.html');
patchWeb3DepositUX('app/dashboard.html');
