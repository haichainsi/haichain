import re

print("Patching sale-controller.js and app/sale-controller.js...")

def patch_sale_controller(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    c_norm = content.replace('\r\n', '\n')

    # Old btnAutofill and btnPayPhantom block
    pattern = r'(// 1-Click Auto-fill Connected Web3 Wallet Button[\s\S]*?)(const nameInput = container\.querySelector\(\'#preseed-name\'\))'
    m = re.search(pattern, c_norm)
    if not m:
        print(f"ERROR: Could not find target pattern in {path}")
        return

    new_block = '''// 1-Click Auto-fill Connected Web3 Wallet Button
    const btnAutofill = container.querySelector('#btn-autofill-phantom');
    if (btnAutofill) {
      btnAutofill.addEventListener('click', async () => {
        let savedW = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
        const walletInput = container.querySelector('#preseed-wallet');

        if (savedW && savedW.address) {
          if (walletInput) walletInput.value = savedW.address;
          return;
        }

        const solProvider = (typeof window.getSolanaProvider === 'function' ? window.getSolanaProvider() : null) || window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null) || window.solflare || window.solana;
        const evmProvider = (typeof window.getMetaMaskProvider === 'function' ? window.getMetaMaskProvider() : null) || window.ethereum;

        if (solProvider) {
          try {
            const resp = await solProvider.connect();
            const addr = resp.publicKey ? resp.publicKey.toString() : (solProvider.publicKey ? solProvider.publicKey.toString() : '');
            if (addr) {
              const provName = solProvider.isPhantom ? 'Phantom' : (solProvider.isSolflare ? 'Solflare' : 'Solana');
              if (walletInput) walletInput.value = addr;
              savedW = { address: addr, provider: provName };
              localStorage.setItem('haichain-connected-wallet', JSON.stringify(savedW));
              if (typeof setConnectedWallet === 'function') await setConnectedWallet(addr, provName);
              if (typeof window.userWallet !== 'undefined') window.userWallet = savedW;
              if (typeof updateWalletBtnUI === 'function') updateWalletBtnUI();
              const payBtnText = container.querySelector('#label-pay-1click-text');
              if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
              return;
            }
          } catch (_) {}
        }

        if (evmProvider) {
          try {
            const accounts = await evmProvider.request({ method: 'eth_requestAccounts' });
            if (accounts && accounts[0]) {
              const addr = accounts[0];
              if (walletInput) walletInput.value = addr;
              savedW = { address: addr, provider: 'MetaMask', isEVM: true };
              localStorage.setItem('haichain-connected-wallet', JSON.stringify(savedW));
              if (typeof setConnectedWallet === 'function') await setConnectedWallet(addr, 'MetaMask');
              if (typeof window.userWallet !== 'undefined') window.userWallet = savedW;
              if (typeof updateWalletBtnUI === 'function') updateWalletBtnUI();
              const payBtnText = container.querySelector('#label-pay-1click-text');
              if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
              return;
            }
          } catch (_) {}
        }

        const wBtn = document.getElementById('wallet-btn');
        if (wBtn) wBtn.click();
      });
    }

    // Universal 1-Click Pay with Connected Web3 Wallet (Strict Real-Fund & On-Chain Verification)
    const btnPayPhantom = container.querySelector('#btn-pay-phantom-1click');
    if (btnPayPhantom) {
      btnPayPhantom.addEventListener('click', async () => {
        const isVi = getActiveLang() === 'vi';
        let savedWallet = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
        
        // 1. If no wallet connected, auto-detect & auto-open extension!
        if (!savedWallet || !savedWallet.address) {
          const solProvider = (typeof window.getSolanaProvider === 'function' ? window.getSolanaProvider() : null) || window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null) || window.solflare || window.solana;
          const evmProvider = (typeof window.getMetaMaskProvider === 'function' ? window.getMetaMaskProvider() : null) || window.ethereum;

          if (solProvider) {
            try {
              const resp = await solProvider.connect();
              const pubKey = resp.publicKey ? resp.publicKey.toString() : (solProvider.publicKey ? solProvider.publicKey.toString() : '');
              if (pubKey) {
                const provName = solProvider.isPhantom ? 'Phantom' : (solProvider.isSolflare ? 'Solflare' : 'Solana');
                savedWallet = { address: pubKey, provider: provName };
                localStorage.setItem('haichain-connected-wallet', JSON.stringify(savedWallet));
                if (typeof setConnectedWallet === 'function') {
                  await setConnectedWallet(pubKey, provName);
                } else if (typeof updateWalletBtnUI === 'function') {
                  window.userWallet = savedWallet;
                  updateWalletBtnUI();
                }
                const walletInput = container.querySelector('#preseed-wallet') || document.getElementById('preseed-wallet');
                if (walletInput) walletInput.value = pubKey;
                const payBtnText = container.querySelector('#label-pay-1click-text') || document.getElementById('label-pay-1click-text');
                if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
                
                const boundDot = container.querySelector('.bg-amber-500');
                if (boundDot) boundDot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
                const boundAddr = container.querySelector('#panel-saft-1click .font-bold.text-black');
                if (boundAddr) boundAddr.textContent = `${pubKey.slice(0, 4)}...${pubKey.slice(-4)}`;

                if (typeof showToast === 'function') {
                  showToast({
                    title: 'Web3 Wallet Connected',
                    message: `${provName}: ${pubKey.slice(0, 4)}...${pubKey.slice(-4)}`,
                    icon: 'check-circle'
                  });
                }
                return; // Auto-connected! User can now click to execute
              }
            } catch (err) {
              console.warn("Solana auto-connect error:", err);
              const wBtn = document.getElementById('wallet-btn');
              if (wBtn) wBtn.click();
              return;
            }
          } else if (evmProvider) {
            try {
              const accounts = await evmProvider.request({ method: 'eth_requestAccounts' });
              if (accounts && accounts[0]) {
                const acc = accounts[0];
                savedWallet = { address: acc, provider: 'MetaMask', isEVM: true };
                localStorage.setItem('haichain-connected-wallet', JSON.stringify(savedWallet));
                if (typeof setConnectedWallet === 'function') {
                  await setConnectedWallet(acc, 'MetaMask');
                } else if (typeof updateWalletBtnUI === 'function') {
                  window.userWallet = savedWallet;
                  updateWalletBtnUI();
                }
                const walletInput = container.querySelector('#preseed-wallet') || document.getElementById('preseed-wallet');
                if (walletInput) walletInput.value = acc;
                const payBtnText = container.querySelector('#label-pay-1click-text') || document.getElementById('label-pay-1click-text');
                if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');

                const boundDot = container.querySelector('.bg-amber-500');
                if (boundDot) boundDot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
                const boundAddr = container.querySelector('#panel-saft-1click .font-bold.text-black');
                if (boundAddr) boundAddr.textContent = `${acc.slice(0, 6)}...${acc.slice(-4)}`;

                if (typeof showToast === 'function') {
                  showToast({
                    title: 'MetaMask Connected',
                    message: `${acc.slice(0, 6)}...${acc.slice(-4)}`,
                    icon: 'check-circle'
                  });
                }
                return;
              }
            } catch (err) {
              console.warn("MetaMask auto-connect error:", err);
              const wBtn = document.getElementById('wallet-btn');
              if (wBtn) wBtn.click();
              return;
            }
          }

          // Neither detected directly, open modal cleanly without blocking alert
          const wBtn = document.getElementById('wallet-btn');
          if (wBtn) wBtn.click();
          return;
        }

        '''

    c_norm = c_norm[:m.start()] + new_block + c_norm[m.end(1):]

    # Also add the haichain_wallet_connected listener if not present
    listener_code = '''
    // Listen for wallet connection from header modal or anywhere
    window.addEventListener('haichain_wallet_connected', (e) => {
      const w = e.detail;
      if (w && w.address) {
        const walletInput = container.querySelector('#preseed-wallet') || document.getElementById('preseed-wallet');
        if (walletInput) walletInput.value = w.address;
        const payBtnText = container.querySelector('#label-pay-1click-text') || document.getElementById('label-pay-1click-text');
        if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
        const boundDot = container.querySelector('.bg-amber-500');
        if (boundDot) boundDot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
        const boundAddr = container.querySelector('#panel-saft-1click .font-bold.text-black');
        if (boundAddr) boundAddr.textContent = `${w.address.slice(0, 4)}...${w.address.slice(-4)}`;
      }
    });
'''
    if 'window.addEventListener(\'haichain_wallet_connected\'' not in c_norm:
        # inject right before `return container;` or at end of setupFormListeners
        ret_idx = c_norm.find('return container;')
        if ret_idx != -1:
            c_norm = c_norm[:ret_idx] + listener_code + '\n    ' + c_norm[ret_idx:]
            print(f"Added haichain_wallet_connected listener in {path}")

    if '\r\n' in content:
        content = c_norm.replace('\n', '\r\n')
    else:
        content = c_norm

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully patched {path}")

patch_sale_controller('sale-controller.js')
patch_sale_controller('app/sale-controller.js')
print("Done patching sale controller.")
