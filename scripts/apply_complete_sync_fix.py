import re

def apply_fix(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure syncVaultToMcpServer is defined before saveBalance
    if 'function syncVaultToMcpServer' not in content:
        sync_fn = '''
    async function syncVaultToMcpServer(vaultAddr, balAmount) {
      if (!vaultAddr) return;
      try {
        const payload = JSON.stringify({
          vault: vaultAddr,
          balance: typeof balAmount === 'number' ? balAmount : parseFloat(balAmount) || 0
        });
        const endpoints = [
          'https://mcp.haichain.si/api/vault/sync',
          '/api/vault/sync',
          'http://127.0.0.1:3600/api/vault/sync'
        ];
        endpoints.forEach(ep => {
          try {
            fetch(ep, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: payload,
              mode: 'cors'
            }).catch(() => {});
          } catch (_) {}
        });
      } catch (_) {}
    }
    window.syncVaultToMcpServer = syncVaultToMcpServer;
'''
        # Inject right before function saveBalance
        target = "    function saveBalance() {"
        if target in content:
            content = content.replace(target, sync_fn + target)
            print("Injected syncVaultToMcpServer definition.")
        else:
            print("WARNING: target 'function saveBalance() {' not found!")

    # 2. Wire syncVaultToMcpServer inside saveBalance
    old_save = '''    function saveBalance() {
      localStorage.setItem('haichain-vault-balance', balance.toFixed(4));
    }'''
    new_save = '''    function saveBalance() {
      localStorage.setItem('haichain-vault-balance', balance.toFixed(4));
      if (userWallet && userWallet.address && typeof syncVaultToMcpServer === 'function') {
        syncVaultToMcpServer(userWallet.address, balance);
      }
    }'''
    if old_save in content:
        content = content.replace(old_save, new_save)
        print("Updated saveBalance to call syncVaultToMcpServer.")

    # 3. Ensure no &bal in updateAiHubUrls
    # Replace any leftover &bal in personalizedUrl
    content = re.sub(
        r'let personalizedUrl = `https://mcp\.haichain\.si/api/mcp\?vault=\$\{encodeURIComponent\(activeAddr\)\}`;\s*if \(typeof balance === [^}]+\}\s*\}',
        'const personalizedUrl = `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`;',
        content
    )

    # 4. Ensure no &bal in copyOnlineMcpBtn
    content = re.sub(
        r'url = `https://mcp\.haichain\.si/api/mcp\?vault=\$\{encodeURIComponent\(activeAddr\)\}`;\s*if \(typeof balance === [^}]+\}\s*\}',
        'url = `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`;',
        content
    )

    # 5. Remove any 1. 2. 3. from tabs if present
    content = content.replace('>1. Desktop App<', '>Desktop App<')
    content = content.replace('>2. Claude Mobile<', '>Claude Mobile<')
    content = content.replace('>3. Web Direct<', '>Web Direct<')

    # 6. Bump cache-buster for i18n and scripts
    ts = 1793660000000
    content = re.sub(r'src="/app/i18n\.js\?v=[^"]*"', f'src="/app/i18n.js?v=v42_sync_{ts}"', content)
    content = re.sub(r'src="/i18n\.js\?v=[^"]*"', f'src="/i18n.js?v=v42_sync_{ts}"', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Completed {file_path}.")

apply_fix('dashboard.html')
apply_fix('app/dashboard.html')
