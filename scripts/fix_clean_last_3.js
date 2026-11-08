const fs = require('fs');

function fixFiles(file) {
  let content = fs.readFileSync(file, 'utf8');

  // Find all occurrences of isVi ?
  let pos = content.indexOf('isVi');
  while (pos !== -1) {
    const checkSnippet = content.substring(pos, pos + 20);
    if (/isVi\s*\?/.test(checkSnippet)) {
      console.log('Found isVi at', pos, 'in', file);
      // Let's see what is around it
      if (content.substring(pos, pos + 100).includes('shortAddr')) {
        const start = content.lastIndexOf('${', pos);
        const end = content.indexOf('}', pos + 50) + 1;
        console.log('Replacing shortAddr banner from', start, 'to', end);
        const replacement = '<strong class="text-black dark:text-white">${shortAddr}</strong>: <strong class="text-black dark:text-white font-bold underline">${haiTotal.toLocaleString()} $HAISI</strong> ($${paidUsdt.toLocaleString()} USDT) • Token-2022 Transfer-Hook Locked';
        content = content.substring(0, start) + replacement + content.substring(end);
        pos = start + replacement.length;
        continue;
      } else if (content.substring(pos, pos + 100).includes('Master Vault')) {
        if (content.substring(pos - 30, pos).includes('message:')) {
          const start = content.lastIndexOf('message:', pos);
          const end = content.indexOf('`', content.indexOf('Faucet', pos)) + 1;
          console.log('Replacing message from', start, 'to', end);
          const replacement = "message: getDashNotice('vaultBalanceInsufficientForTask')";
          content = content.substring(0, start) + replacement + content.substring(end);
          pos = start + replacement.length;
          continue;
        } else if (content.substring(pos - 30, pos).includes('alert(')) {
          const start = content.lastIndexOf('alert(', pos);
          const end = content.indexOf(');', pos) + 2;
          console.log('Replacing alert from', start, 'to', end);
          const replacement = "alert(getDashNotice('vaultBalanceInsufficientForTask'));";
          content = content.substring(0, start) + replacement + content.substring(end);
          pos = start + replacement.length;
          continue;
        }
      }
    }
    pos = content.indexOf('isVi', pos + 1);
  }

  fs.writeFileSync(file, content, 'utf8');
}

fixFiles('dashboard.html');
fixFiles('app/dashboard.html');
