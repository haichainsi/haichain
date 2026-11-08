import re

print("Patching dashboard.html and app/dashboard.html...")

# 1. First add getSolanaProvider and expose getMetaMaskProvider on window
def patch_dashboard(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize newlines
    c_norm = content.replace('\r\n', '\n')

    # Find getMetaMaskProvider definition
    old_mm_fn = '''    function getMetaMaskProvider() {
      if (typeof window === 'undefined') return null;
      if (window.ethereum?.providers && Array.isArray(window.ethereum.providers)) {
        return window.ethereum.providers.find(p => p.isMetaMask && !p.isPhantom) || window.ethereum.providers.find(p => p.isMetaMask) || window.ethereum;
      }
      if (window.ethereum?.isMetaMask) {
        return window.ethereum;
      }
      if (window.ethereum) {
        return window.ethereum;
      }
      return null;
    }'''

    new_providers_fn = '''    function getSolanaProvider(preferred = 'any') {
      if (typeof window === 'undefined') return null;
      if (preferred === 'phantom') {
        if (window.phantom?.solana) return window.phantom.solana;
        if (window.solana?.isPhantom) return window.solana;
      }
      if (preferred === 'solflare') {
        if (window.solflare?.isSolflare || window.solflare) return window.solflare;
        if (window.solana?.isSolflare) return window.solana;
      }
      // Any detected Solana provider
      if (window.phantom?.solana) return window.phantom.solana;
      if (window.solflare) return window.solflare;
      if (window.solana) return window.solana;
      return null;
    }
    window.getSolanaProvider = getSolanaProvider;

    function getMetaMaskProvider() {
      if (typeof window === 'undefined') return null;
      if (window.ethereum?.providers && Array.isArray(window.ethereum.providers)) {
        return window.ethereum.providers.find(p => p.isMetaMask && !p.isPhantom) || window.ethereum.providers.find(p => p.isMetaMask) || window.ethereum.providers[0];
      }
      if (window.ethereum?.isMetaMask) {
        return window.ethereum;
      }
      if (window.ethereum) {
        return window.ethereum;
      }
      return null;
    }
    window.getMetaMaskProvider = getMetaMaskProvider;'''

    if old_mm_fn.replace('\r\n', '\n') in c_norm:
        c_norm = c_norm.replace(old_mm_fn.replace('\r\n', '\n'), new_providers_fn)
        print(f"Added getSolanaProvider and exposed to window in {path}")
    else:
        print(f"WARNING: getMetaMaskProvider not found in {path}")

    # Now patch the wallet-provider-btn handlers
    # Find block from "// 2. PHANTOM WALLET" to "// 4. MANUAL ADDRESS"
    pattern = r'(// 2\. PHANTOM WALLET\s*if\s*\(provider === \'phantom\'\) \{[\s\S]*?)(// 4\. MANUAL ADDRESS)'
    m = re.search(pattern, c_norm)
    if m:
        new_wallet_block = '''// 2. PHANTOM WALLET
        if (provider === 'phantom') {
          const phantom = getSolanaProvider('phantom') || window.solana;
          if (phantom) {
            try {
              walletBtnText.textContent = getDashNotice('connectingPhantom');
              const resp = await phantom.connect();
              const pubKey = resp.publicKey ? resp.publicKey.toString() : (phantom.publicKey ? phantom.publicKey.toString() : '');
              if (!pubKey) throw new Error("No public key returned by Phantom");
              await setConnectedWallet(pubKey, phantom.isPhantom ? 'Phantom' : 'Solana');
              walletConnectModal.classList.add('hidden');
              showToast({
                title: 'Phantom Connected',
                message: pubKey.slice(0, 4) + '...' + pubKey.slice(-4),
                icon: 'check-circle'
              });
              openAccountModal();
              window.dispatchEvent(new CustomEvent('haichain_wallet_connected', { detail: { address: pubKey, provider: 'Phantom' } }));
            } catch (err) {
              console.error("Phantom connection rejected:", err);
              updateWalletBtnUI();
              showToast({
                title: 'Phantom',
                message: getDashNotice('connectionRejected'),
                icon: 'alert-triangle'
              });
            }
          } else if (isMobileDevice()) {
            closeAllWalletTrays('phantom-mobile-tray');
            const tray = document.getElementById('phantom-mobile-tray');
            const arrow = document.getElementById('phantom-arrow');
            if (tray) {
              const isHidden = tray.classList.contains('hidden');
              if (isHidden) {
                tray.classList.remove('hidden');
                if (arrow) arrow.classList.add('rotate-90');
                safeCreateIcons();
              } else {
                tray.classList.add('hidden');
                if (arrow) arrow.classList.remove('rotate-90');
              }
            }
          } else {
            walletNoticeText.innerHTML = getDashNotice('phantomNotDetected');
            walletInstallLink.href = "https://phantom.app/";
            walletInstallLink.parentElement.classList.remove('hidden');
            walletNoticeBox.classList.remove('hidden');
            safeCreateIcons();
          }
          return;
        }

        // METAMASK WALLET (EVM & Solana Snap Support)
        if (provider === 'metamask') {
          const mm = getMetaMaskProvider() || window.ethereum;
          if (mm) {
            try {
              walletBtnText.textContent = getDashNotice('connectingMetaMask');
              const accounts = await mm.request({ method: 'eth_requestAccounts' });
              if (!accounts || accounts.length === 0) {
                throw new Error("No accounts authorized in MetaMask");
              }
              const account = accounts[0];
              let chainId = null;
              try {
                chainId = await mm.request({ method: 'eth_chainId' });
              } catch (_) {}

              await setConnectedWallet(account, 'MetaMask');
              walletConnectModal.classList.add('hidden');
              const shortAddr = account.slice(0, 6) + '...' + account.slice(-4);
              showToast({
                title: 'MetaMask Connected',
                message: shortAddr + (chainId ? ` (Chain ${parseInt(chainId, 16)})` : ''),
                icon: 'check-circle'
              });
              openAccountModal();
              window.dispatchEvent(new CustomEvent('haichain_wallet_connected', { detail: { address: account, provider: 'MetaMask', isEVM: true } }));

              if (mm.on && !mm._haichainListenersBound) {
                mm._haichainListenersBound = true;
                mm.on('accountsChanged', (newAccounts) => {
                  if (!newAccounts || newAccounts.length === 0) {
                    userWallet = null;
                    localStorage.removeItem('haichain-connected-wallet');
                    updateWalletBtnUI();
                  } else {
                    setConnectedWallet(newAccounts[0], 'MetaMask');
                  }
                });
                mm.on('chainChanged', () => {
                  if (userWallet && userWallet.provider === 'MetaMask') {
                    setConnectedWallet(userWallet.address, 'MetaMask');
                  }
                });
              }
            } catch (err) {
              console.error("MetaMask connection error:", err);
              updateWalletBtnUI();
              if (err.code === 4001) {
                showToast({
                  title: 'MetaMask',
                  message: getDashNotice('connectionRejected'),
                  icon: 'alert-triangle'
                });
              } else {
                walletNoticeText.innerHTML = '<strong>MetaMask Error:</strong> ' + (err.message || err);
                walletNoticeBox.classList.remove('hidden');
                safeCreateIcons();
              }
            }
          } else if (isMobileDevice()) {
            walletConnectModal.classList.add('hidden');
            walletBtnText.textContent = getDashNotice('connectingMetaMask');
            
            const sessId = 'mm_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2, 8);
            window.__currentMetaMaskSessionId = sessId;
            try { localStorage.setItem('haichain_metamask_pending_session', sessId); } catch (_) {}
            if (typeof startMetaMaskSessionPoller === 'function') startMetaMaskSessionPoller(sessId);

            showToast({
              title: getDashNotice('metaMaskMobileTitle'),
              message: getDashNotice('launchingMetaMaskApp'),
              icon: 'arrow-right'
            });
            setTimeout(() => {
              if (window.HaichainMobileWallet && typeof window.HaichainMobileWallet.connectMetaMask === 'function') {
                window.HaichainMobileWallet.connectMetaMask();
              } else {
                const appOrigin = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') ? 'https://haichain.pages.dev' : window.location.origin;
                const targetUrl = appOrigin + window.location.pathname + '?auto_connect=metamask&sess_id=' + sessId + '&return_url=' + encodeURIComponent(window.location.href);
                window.location.href = 'https://metamask.app.link/dapp/' + targetUrl.replace(/^https?:\/\//, '');
              }
            }, 150);
          } else {
            walletNoticeText.innerHTML = getDashNotice('metaMaskNotDetectedFull');
            walletInstallLink.href = "https://metamask.io/download/";
            walletInstallLink.parentElement.classList.remove('hidden');
            walletNoticeBox.classList.remove('hidden');
            safeCreateIcons();
          }
          return;
        }

        // 3. SOLFLARE WALLET
        if (provider === 'solflare') {
          const solflare = getSolanaProvider('solflare') || window.solflare;
          if (solflare) {
            try {
              walletBtnText.textContent = getDashNotice('connectingSolflare');
              await solflare.connect();
              const pubKey = solflare.publicKey ? solflare.publicKey.toString() : '';
              if (!pubKey) throw new Error("No public key returned by Solflare");
              await setConnectedWallet(pubKey, 'Solflare');
              walletConnectModal.classList.add('hidden');
              showToast({
                title: 'Solflare Connected',
                message: pubKey.slice(0, 4) + '...' + pubKey.slice(-4),
                icon: 'check-circle'
              });
              openAccountModal();
              window.dispatchEvent(new CustomEvent('haichain_wallet_connected', { detail: { address: pubKey, provider: 'Solflare' } }));
            } catch (err) {
              console.error("Solflare error:", err);
              updateWalletBtnUI();
              showToast({
                title: 'Solflare',
                message: getDashNotice('connectionRejected'),
                icon: 'alert-triangle'
              });
            }
          } else if (isMobileDevice()) {
            closeAllWalletTrays('solflare-mobile-tray');
            const tray = document.getElementById('solflare-mobile-tray');
            const arrow = document.getElementById('solflare-arrow');
            if (tray) {
              const isHidden = tray.classList.contains('hidden');
              if (isHidden) {
                tray.classList.remove('hidden');
                if (arrow) arrow.classList.add('rotate-90');
                safeCreateIcons();
              } else {
                tray.classList.add('hidden');
                if (arrow) arrow.classList.remove('rotate-90');
              }
            }
          } else {
            walletNoticeText.innerHTML = getDashNotice('solflareNotDetected');
            walletInstallLink.href = "https://solflare.com/";
            walletInstallLink.parentElement.classList.remove('hidden');
            walletNoticeBox.classList.remove('hidden');
            safeCreateIcons();
          }
          return;
        }

        '''
        c_norm = c_norm[:m.start()] + new_wallet_block + c_norm[m.end(1):]
        print(f"Patched wallet-provider-btn logic in {path}")
    else:
        print(f"WARNING: Wallet provider block regex not matched in {path}")

    # Patch depositConnectBtn to support any installed wallet
    old_dep_btn = '''        const phantom = window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null);
        const solflare = window.solflare?.isSolflare ? window.solflare : null;
        if (phantom) {
          try {
            depositConnectBtn.textContent = getDashNotice('connectingBtn');
            const resp = await phantom.connect();
            await setConnectedWallet(resp.publicKey ? resp.publicKey.toString() : phantom.publicKey.toString(), 'Phantom');
            updateDepositWalletBanner();
          } catch (err) {
            console.warn("Phantom connection rejected:", err);
            updateDepositWalletBanner();
          }
        } else if (solflare) {
          try {
            depositConnectBtn.textContent = getDashNotice('connectingBtn');
            await solflare.connect();
            await setConnectedWallet(solflare.publicKey.toString(), 'Solflare');
            updateDepositWalletBanner();
          } catch (err) {
            console.warn("Solflare connection rejected:", err);
            updateDepositWalletBanner();
          }
        }'''

    new_dep_btn = '''        const phantom = getSolanaProvider('phantom') || window.solana;
        const solflare = getSolanaProvider('solflare') || window.solflare;
        const mm = getMetaMaskProvider() || window.ethereum;

        if (phantom) {
          try {
            depositConnectBtn.textContent = getDashNotice('connectingBtn');
            const resp = await phantom.connect();
            const pk = resp.publicKey ? resp.publicKey.toString() : (phantom.publicKey ? phantom.publicKey.toString() : '');
            await setConnectedWallet(pk, phantom.isPhantom ? 'Phantom' : 'Solana');
            updateDepositWalletBanner();
          } catch (err) {
            console.warn("Phantom connection rejected:", err);
            updateDepositWalletBanner();
          }
        } else if (solflare) {
          try {
            depositConnectBtn.textContent = getDashNotice('connectingBtn');
            await solflare.connect();
            const pk = solflare.publicKey ? solflare.publicKey.toString() : '';
            await setConnectedWallet(pk, 'Solflare');
            updateDepositWalletBanner();
          } catch (err) {
            console.warn("Solflare connection rejected:", err);
            updateDepositWalletBanner();
          }
        } else if (mm) {
          try {
            depositConnectBtn.textContent = getDashNotice('connectingBtn');
            const accounts = await mm.request({ method: 'eth_requestAccounts' });
            if (accounts && accounts[0]) {
              await setConnectedWallet(accounts[0], 'MetaMask');
              updateDepositWalletBanner();
            }
          } catch (err) {
            console.warn("MetaMask connection rejected:", err);
            updateDepositWalletBanner();
          }
        }'''

    if old_dep_btn.replace('\r\n', '\n') in c_norm:
        c_norm = c_norm.replace(old_dep_btn.replace('\r\n', '\n'), new_dep_btn)
        print(f"Patched depositConnectBtn in {path}")
    else:
        print(f"WARNING: old_dep_btn not matched in {path}")

    # Write back
    if '\r\n' in content:
        content = c_norm.replace('\n', '\r\n')
    else:
        content = c_norm

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

patch_dashboard('dashboard.html')
patch_dashboard('app/dashboard.html')
print("Dashboard patch completed.")
