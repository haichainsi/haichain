import re

def patch_frontend_sync(path):
    print(f"Patching {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Clean updateAiHubUrls: no &bal in personalizedUrl
    old_personalized = '''let personalizedUrl = `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`;
        if (typeof balance === 'number' && balance > 0) {
          personalizedUrl += `&bal=${balance.toFixed(2)}`;
        }'''
    new_personalized = 'const personalizedUrl = `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`;'

    if old_personalized in html:
        html = html.replace(old_personalized, new_personalized)
        print("Cleaned personalizedUrl to pure permanent link.")

    # 2. Clean copy button URL: no &bal in copied link
    old_copy_url = '''        let url = "https://mcp.haichain.si/api/mcp";
        if (hasWallet && activeAddr) {
          url = `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`;
          if (typeof balance === 'number' && balance > 0) {
            url += `&bal=${balance.toFixed(2)}`;
          }
        }'''
    new_copy_url = '''        const url = hasWallet && activeAddr 
          ? `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`
          : "https://mcp.haichain.si/api/mcp";'''

    if old_copy_url in html:
        html = html.replace(old_copy_url, new_copy_url)
        print("Cleaned copy button URL.")

    # 3. Add syncVaultToMcpServer function and wire into saveBalance
    old_save_balance = '''function saveBalance() {
  localStorage.setItem('haichain-vault-balance', balance.toFixed(4));
}'''

    new_save_balance = '''async function syncVaultToMcpServer(vaultAddr, balAmount) {
  if (!vaultAddr) return;
  try {
    const endpoints = [
      'https://mcp.haichain.si/api/vault/sync',
      'http://127.0.0.1:3600/api/vault/sync'
    ];
    for (const ep of endpoints) {
      try {
        fetch(ep, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            vault: vaultAddr,
            balance: balAmount
          })
        }).catch(() => {});
      } catch (_) {}
    }
  } catch (_) {}
}
window.syncVaultToMcpServer = syncVaultToMcpServer;

function saveBalance() {
  localStorage.setItem('haichain-vault-balance', balance.toFixed(4));
  if (userWallet && userWallet.address) {
    syncVaultToMcpServer(userWallet.address, balance);
  }
}'''

    if old_save_balance in html:
        html = html.replace(old_save_balance, new_save_balance)
        print("Wired syncVaultToMcpServer into saveBalance.")

    # 4. Also call syncVaultToMcpServer in updateWalletBtnUI
    old_wui = 'if (typeof updateAiHubUrls === \'function\') {\n        updateAiHubUrls();\n      }'
    new_wui = '''if (typeof updateAiHubUrls === 'function') {
        updateAiHubUrls();
      }
      if (userWallet && userWallet.address && typeof syncVaultToMcpServer === 'function') {
        syncVaultToMcpServer(userWallet.address, balance);
      }'''

    if old_wui in html:
        html = html.replace(old_wui, new_wui, 1)
        print("Wired syncVaultToMcpServer into updateWalletBtnUI.")

    # 5. Bump cache-buster
    html = re.sub(r'src="/app/i18n\.js\?v=[^"]*"', f'src="/app/i18n.js?v=v41_realtime_sync_{1793655000000}"', html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Finished {path}.")

patch_frontend_sync('dashboard.html')
patch_frontend_sync('app/dashboard.html')
