import sys
sys.stdout.reconfigure(encoding='utf-8')

for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove startMetaMaskSessionPoller definition
    old_poller_def = """    // Session Poller for Cross-Browser MetaMask Mobile Handshake
    function startMetaMaskSessionPoller(sessId) {
      if (!sessId) return;
      let attempts = 0;
      const maxAttempts = 150; // ~3 minutes
      if (window.__metaMaskPoller) clearInterval(window.__metaMaskPoller);

      const poll = async () => {
        attempts++;
        if (attempts > maxAttempts || (userWallet && userWallet.address)) {
          clearInterval(window.__metaMaskPoller);
          return;
        }
        try {
          const res = await fetch(`/api/wallet-relay?id=${sessId}`);
          if (res.ok) {
            const data = await res.json();
            if (data && data.connected && data.data && data.data.address) {
              clearInterval(window.__metaMaskPoller);
              const addr = data.data.address;
              console.log('[MetaMaskRelay] Real wallet received from relay:', addr);
              localStorage.removeItem('haichain_metamask_pending_session');
              window.__currentMetaMaskSessionId = null;
              await setConnectedWallet(addr, 'MetaMask');
              if (data.data.balance && userWallet) {
                userWallet.evmBalance = data.data.balance;
                userWallet.solBalance = data.data.balance + ' ETH';
                updateWalletBtnUI();
              }
              const isVi = window.haichainI18n?.currentLang === 'vi';
              showToast({
                title: isVi ? '✓ MetaMask Đã Kết Nối!' : '✓ MetaMask Connected!',
                message: addr.slice(0, 6) + '...' + addr.slice(-4) + (data.data.balance ? ` (${data.data.balance} ETH)` : ''),
                icon: 'check-circle'
              });
              if (walletConnectModal) walletConnectModal.classList.add('hidden');
              openAccountModal();
            }
          }
        } catch (_) {}
      };

      window.__metaMaskPoller = setInterval(poll, 1200);
      poll();
    }"""

    if old_poller_def in text:
        text = text.replace(old_poller_def, "")
        print(f"Removed old_poller_def from {path}")

    # Remove fetch /api/wallet-relay in in-app block
    old_fetch_relay = """                // Notify session relay for external browser sync
                if (sessIdParam) {
                  try {
                    await fetch('/api/wallet-relay', {
                      method: 'POST',
                      headers: { 'Content-Type': 'application/json' },
                      body: JSON.stringify({ id: sessIdParam, address: account, provider: 'MetaMask', balance: ethBal })
                    });
                  } catch (_) {}
                }"""

    if old_fetch_relay in text:
        text = text.replace(old_fetch_relay, "")
        print(f"Removed old_fetch_relay from {path}")

    # Remove relay check in onTabWakeup
    old_wakeup_relay = """      // 1. Check relay session
      const pendingSess = window.__currentMetaMaskSessionId || localStorage.getItem('haichain_metamask_pending_session');
      if (pendingSess) {
        try {
          const res = await fetch(`/api/wallet-relay?id=${pendingSess}`);
          if (res.ok) {
            const data = await res.json();
            if (data && data.connected && data.data && data.data.address) {
              localStorage.removeItem('haichain_metamask_pending_session');
              window.__currentMetaMaskSessionId = null;
              await setConnectedWallet(data.data.address, 'MetaMask');
              if (data.data.balance && userWallet) {
                userWallet.evmBalance = data.data.balance;
                userWallet.solBalance = data.data.balance + ' ETH';
                updateWalletBtnUI();
              }
              const isVi = window.haichainI18n?.currentLang === 'vi';
              showToast({
                title: isVi ? '✓ MetaMask Đã Kết Nối!' : '✓ MetaMask Connected!',
                message: data.data.address.slice(0, 6) + '...' + data.data.address.slice(-4),
                icon: 'check-circle'
              });
              if (walletConnectModal) walletConnectModal.classList.add('hidden');
              openAccountModal();
              return;
            }
          }
        } catch (_) {}
      }"""

    if old_wakeup_relay in text:
        text = text.replace(old_wakeup_relay, "")
        print(f"Removed old_wakeup_relay from {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

print("Finished cleaning up wallet-relay references.")
