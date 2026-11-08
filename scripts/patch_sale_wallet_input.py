import sys, re
sys.stdout.reconfigure(encoding='utf-8')

targets = ['sale-controller.js', 'app/sale-controller.js']

for fpath in targets:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix connected wallet address resolution & allocation display in renderTerminalContent
    # Replace lines 893-902
    old_alloc_res = """    let userAllocation = null;
    let connectedWalletAddr = '';
    try {
      const allocs = JSON.parse(localStorage.getItem('haichain_early_allocations') || '{}');
      const savedWallet = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
      connectedWalletAddr = savedWallet.address || '';
      const addr = connectedWalletAddr || Object.keys(allocs)[0];
      if (addr && allocs[addr]) {
        userAllocation = { ...allocs[addr], address: addr };
      }
    } catch (_) {}"""

    new_alloc_res = """    let userAllocation = null;
    let connectedWalletAddr = '';
    let isConnectedEVM = false;
    let savedWallet = {};
    try {
      const allocs = JSON.parse(localStorage.getItem('haichain_early_allocations') || '{}');
      savedWallet = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
      connectedWalletAddr = savedWallet.address || '';
      isConnectedEVM = connectedWalletAddr.startsWith('0x') || !!(savedWallet.provider && savedWallet.provider.toLowerCase().includes('metamask')) || !!savedWallet.isEVM;
      // Strictly bind userAllocation to the CURRENTLY connected wallet
      if (connectedWalletAddr && allocs[connectedWalletAddr]) {
        userAllocation = { ...allocs[connectedWalletAddr], address: connectedWalletAddr };
      }
    } catch (_) {}"""

    if old_alloc_res in content:
        content = content.replace(old_alloc_res, new_alloc_res)
        print(f"[{fpath}] Replaced userAllocation resolution")
    else:
        print(f"[{fpath}] Warning: old_alloc_res not matched exactly")

    # 2. Fix the label & autofill button in the terminal HTML
    old_wallet_html = """              <!-- Wallet Field (Primary) -->
              <div>
                <div class="flex justify-between items-center mb-1">
                  <label class="block text-[11px] text-neutral-500 font-sans font-medium">${getI18nText('labelWallet')}</label>
                  <button type="button" id="btn-autofill-phantom" class="text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white underline font-sans text-[10px] flex items-center space-x-1 cursor-pointer">
                    <i data-lucide="zap" class="w-3 h-3 text-emerald-500"></i>
                    <span id="calc-autofill-text">${getI18nText('autofillPhantom')}</span>
                  </button>
                </div>
                <input type="text" id="preseed-wallet" value="${connectedWalletAddr}" placeholder="${getI18nText('placeholderWallet')}" class="w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white font-mono text-[11px]">
              </div>"""

    new_wallet_html = """              <!-- Wallet Field (Primary) -->
              <div>
                <div class="flex justify-between items-center mb-1">
                  <label class="block text-[11px] text-neutral-500 font-sans font-medium">${isConnectedEVM ? (getActiveLang() === 'vi' ? 'Địa Chỉ Ví Nhận Token (MetaMask / EVM):' : 'Receiving & Bound Web3 Wallet (MetaMask / EVM):') : getI18nText('labelWallet')}</label>
                  <button type="button" id="btn-autofill-phantom" class="text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white underline font-sans text-[10px] flex items-center space-x-1 cursor-pointer">
                    <i data-lucide="zap" class="w-3 h-3 text-emerald-500"></i>
                    <span id="calc-autofill-text">${isConnectedEVM ? (getActiveLang() === 'vi' ? 'Tự Điền MetaMask' : 'Auto-fill MetaMask') : getI18nText('autofillPhantom')}</span>
                  </button>
                </div>
                <input type="text" id="preseed-wallet" value="${connectedWalletAddr}" placeholder="${isConnectedEVM ? '0x...' : getI18nText('placeholderWallet')}" class="w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white font-mono text-[11px]">
              </div>"""

    if old_wallet_html in content:
        content = content.replace(old_wallet_html, new_wallet_html)
        print(f"[{fpath}] Replaced wallet field HTML")
    else:
        print(f"[{fpath}] Warning: old_wallet_html not matched exactly")

    # 3. Replace btn-autofill-phantom handler
    old_autofill_handler = """    // 1-Click Auto-fill Phantom Wallet Button
    const btnAutofill = container.querySelector('#btn-autofill-phantom');
    if (btnAutofill) {
      btnAutofill.addEventListener('click', async () => {
        try {
          const provider = window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null);
          if (provider) {
            const resp = await provider.connect();
            const addr = resp.publicKey ? resp.publicKey.toString() : '';
            if (addr) {
              const walletInput = container.querySelector('#preseed-wallet');
              if (walletInput) walletInput.value = addr;
            }
          } else {
            alert(getActiveLang() === 'vi' 
              ? 'Không tìm thấy tiện ích Phantom. Hãy cài extension Phantom hoặc dán địa chỉ ví thủ công.' 
              : 'Phantom wallet extension not found. Please paste your Solana address manually.');
          }
        } catch (e) {
          console.warn('Phantom connect error:', e);
        }
      });
    }"""

    new_autofill_handler = """    // 1-Click Auto-fill Connected Web3 Wallet Button
    const btnAutofill = container.querySelector('#btn-autofill-phantom');
    if (btnAutofill) {
      btnAutofill.addEventListener('click', async () => {
        const isVi = getActiveLang() === 'vi';
        const savedW = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
        const walletInput = container.querySelector('#preseed-wallet');

        if (savedW && savedW.address) {
          if (walletInput) walletInput.value = savedW.address;
          return;
        }

        // Try MetaMask first if EVM
        if (window.ethereum) {
          try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            if (accounts && accounts[0]) {
              if (walletInput) walletInput.value = accounts[0];
              return;
            }
          } catch (_) {}
        }

        // Try Phantom / Solana
        try {
          const provider = window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null);
          if (provider) {
            const resp = await provider.connect();
            const addr = resp.publicKey ? resp.publicKey.toString() : '';
            if (addr && walletInput) walletInput.value = addr;
          } else {
            alert(isVi 
              ? 'Không tìm thấy tiện ích ví Web3. Vui lòng kết nối ví ở góc trên hoặc dán địa chỉ ví thủ công.' 
              : 'Web3 wallet extension not found. Please connect your wallet in the header or paste address manually.');
          }
        } catch (e) {
          console.warn('Wallet connect error:', e);
        }
      });
    }"""

    if old_autofill_handler in content:
        content = content.replace(old_autofill_handler, new_autofill_handler)
        print(f"[{fpath}] Replaced autofill handler")
    else:
        print(f"[{fpath}] Warning: old_autofill_handler not matched exactly")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Step 1 & 2 completed.")
