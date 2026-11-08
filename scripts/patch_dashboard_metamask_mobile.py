import sys
sys.stdout.reconfigure(encoding='utf-8')

for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update MetaMask mobile 1-click deeplink in wallet-provider-btn click handler
    old_mm_btn_block = """          } else if (isMobileDevice()) {
            closeAllWalletTrays('metamask-mobile-tray');
            const tray = document.getElementById('metamask-mobile-tray');
            const arrow = document.getElementById('metamask-arrow');
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
          }"""

    new_mm_btn_block = """          } else if (isMobileDevice()) {
            // MOBILE 1-CLICK DEEPLINK (Mirroring Phantom UX: Direct native app launch & seamless auto-return)
            walletConnectModal.classList.add('hidden');
            const isVi = window.haichainI18n?.currentLang === 'vi';
            walletBtnText.textContent = getDashNotice('connectingMetaMask') || (isVi ? 'Đang mở MetaMask...' : 'Opening MetaMask...');
            armWalletConnectRevert(4500);
            showToast({
              title: isVi ? 'Ví MetaMask Mobile' : 'MetaMask Mobile',
              message: isVi ? 'Đang kết nối tới ứng dụng MetaMask...' : 'Launching MetaMask App...',
              icon: 'arrow-right'
            });
            setTimeout(() => {
              if (window.HaichainMobileWallet && typeof window.HaichainMobileWallet.connectMetaMask === 'function') {
                window.HaichainMobileWallet.connectMetaMask();
              } else {
                const appOrigin = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') ? 'https://haichain.pages.dev' : window.location.origin;
                const targetUrl = appOrigin + window.location.pathname + '?auto_connect=metamask&return_url=' + encodeURIComponent(window.location.href);
                window.location.href = 'https://metamask.app.link/dapp/' + targetUrl.replace(/^https?:\\/\\//, '');
              }
            }, 150);
          }"""

    if old_mm_btn_block in text:
        text = text.replace(old_mm_btn_block, new_mm_btn_block)
        print(f"Patched MetaMask mobile button in {path}")
    else:
        print(f"WARNING: old_mm_btn_block not found in {path}")

    # 2. Update checkMobileWalletSyncOrCallback to accept EVM addresses from localStorage
    old_sync_regex = """        const stored = localStorage.getItem('haichain-connected-wallet');
        if (stored) {
          const parsed = JSON.parse(stored);
          if (parsed && parsed.address && /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(parsed.address)) {"""

    new_sync_regex = """        const stored = localStorage.getItem('haichain-connected-wallet');
        if (stored) {
          const parsed = JSON.parse(stored);
          const isSol = parsed && parsed.address && /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(parsed.address);
          const isEvm = parsed && parsed.address && /^0x[a-fA-F0-9]{40}$/i.test(parsed.address);
          if (parsed && parsed.address && (isSol || isEvm)) {"""

    if old_sync_regex in text:
        text = text.replace(old_sync_regex, new_sync_regex)
        print(f"Patched checkMobileWalletSyncOrCallback address regex in {path}")
    else:
        print(f"WARNING: old_sync_regex not found in {path}")

    # 3. Add showMetaMaskMobileHandoffBar and MetaMask in-app browser auto-connect
    old_auto_connect = """      // Auto-connect inside Phantom / Solflare in-app browser
      try {
        const urlParams = new URLSearchParams(window.location.search);
        const autoProvider = urlParams.get('autoConnect');
        const autoDeposit = urlParams.get('autoDeposit');
        const depositAmountParam = urlParams.get('depositAmount');"""

    new_auto_connect = """    // Luxury Black & White Return Banner for MetaMask In-App Browser to Safari/Chrome
    function showMetaMaskMobileHandoffBar(account, returnUrl) {
      const existing = document.getElementById('metamask-mobile-handoff-bar');
      if (existing) existing.remove();

      const isVi = window.haichainI18n?.currentLang === 'vi';
      const shortAddr = account.slice(0, 6) + '...' + account.slice(-4);
      const balText = (userWallet && userWallet.evmBalance) ? userWallet.evmBalance + ' ETH' : (userWallet?.solBalance || 'Ví Thật');

      let destUrl = returnUrl ? decodeURIComponent(returnUrl) : (window.location.origin + window.location.pathname);
      const sep = destUrl.indexOf('?') === -1 ? '?' : '&';
      const returnHref = destUrl + sep + 'connectedWallet=' + encodeURIComponent(account) + '&provider=MetaMask';

      const bar = document.createElement('div');
      bar.id = 'metamask-mobile-handoff-bar';
      bar.className = 'fixed top-0 left-0 right-0 z-[100] bg-black text-white border-b border-neutral-700 px-3 py-2.5 shadow-2xl flex items-center justify-between text-xs font-mono';
      bar.innerHTML = `
        <div class="flex items-center space-x-2 min-w-0 pr-2">
          <span class="text-sm shrink-0">🦊</span>
          <div class="truncate">
            <span class="font-bold text-white">${isVi ? 'Đã kết nối ví MetaMask' : 'MetaMask Wallet Connected'}</span>: 
            <span class="text-neutral-300 font-mono text-[11px]">${shortAddr} (${balText})</span>
          </div>
        </div>
        <div class="flex items-center space-x-2 shrink-0">
          <a href="${returnHref}" class="py-1 px-2.5 rounded-lg bg-white text-black font-bold text-[10px] sm:text-xs hover:bg-neutral-200 transition-colors shadow flex items-center space-x-1 whitespace-nowrap">
            <span>${isVi ? 'Quay về Safari / Chrome' : 'Return to Safari / Chrome'}</span>
            <span>&rarr;</span>
          </a>
          <button type="button" onclick="document.getElementById('metamask-mobile-handoff-bar').remove()" class="text-neutral-400 hover:text-white p-1 text-sm font-bold leading-none cursor-pointer">&times;</button>
        </div>
      `;
      document.body.prepend(bar);
    }

    // Auto-connect inside MetaMask / Phantom / Solflare in-app browser
      try {
        const urlParams = new URLSearchParams(window.location.search);
        const autoProvider = (urlParams.get('autoConnect') || urlParams.get('auto_connect') || '').toLowerCase();
        const autoDeposit = urlParams.get('autoDeposit') || urlParams.get('auto_deposit');
        const depositAmountParam = urlParams.get('depositAmount') || urlParams.get('deposit_amount');
        const returnUrlParam = urlParams.get('return_url') || urlParams.get('returnUrl');

        // A. METAMASK IN-APP AUTO-CONNECT (NATIVE MOBILE WEB3 HANDSHAKE)
        if (autoProvider === 'metamask') {
          const cleanUrl = new URL(window.location.href);
          cleanUrl.searchParams.delete('autoConnect');
          cleanUrl.searchParams.delete('auto_connect');
          cleanUrl.searchParams.delete('autoDeposit');
          cleanUrl.searchParams.delete('auto_deposit');
          cleanUrl.searchParams.delete('depositAmount');
          cleanUrl.searchParams.delete('deposit_amount');
          cleanUrl.searchParams.delete('return_url');
          cleanUrl.searchParams.delete('returnUrl');
          window.history.replaceState({}, document.title, cleanUrl.toString());

          let mmAttempts = 0;
          const mmPoll = setInterval(async () => {
            mmAttempts++;
            const mm = getMetaMaskProvider() || window.ethereum;
            if (mm && mm.request) {
              clearInterval(mmPoll);
              try {
                if (typeof walletBtnText !== 'undefined' && walletBtnText) {
                  walletBtnText.textContent = 'Connecting MetaMask...';
                }
                const accounts = await mm.request({ method: 'eth_requestAccounts' });
                if (accounts && accounts[0]) {
                  const account = accounts[0];
                  await setConnectedWallet(account, 'MetaMask');
                  
                  try {
                    document.cookie = 'haichain-connected-wallet=' + encodeURIComponent(JSON.stringify(userWallet)) + '; Path=/; Max-Age=2592000; SameSite=Lax';
                  } catch (_) {}

                  const isVi = window.haichainI18n?.currentLang === 'vi';
                  if (typeof showToast === 'function') {
                    showToast({
                      title: isVi ? '✓ MetaMask Đã Kết Nối Thực Tế!' : '✓ MetaMask Real Wallet Connected!',
                      message: account.slice(0, 6) + '...' + account.slice(-4) + (userWallet.evmBalance ? ` (${userWallet.evmBalance} ETH)` : ''),
                      icon: 'check-circle'
                    });
                  }

                  showMetaMaskMobileHandoffBar(account, returnUrlParam);

                  if (autoDeposit === 'web3') {
                    setTimeout(() => {
                      const dModal = document.getElementById('dashboard-deposit-modal');
                      const dAmount = document.getElementById('dash-deposit-amount');
                      const cBtn = document.getElementById('dash-confirm-deposit-btn');
                      if (typeof selectDepositTab === 'function') selectDepositTab('web3');
                      if (dAmount && depositAmountParam) {
                        dAmount.value = depositAmountParam;
                      }
                      if (dModal) dModal.classList.remove('hidden');
                      if (typeof updateDepositWalletBanner === 'function') updateDepositWalletBanner();

                      setTimeout(() => {
                        if (cBtn && !cBtn.disabled) {
                          cBtn.click();
                        }
                      }, 400);
                    }, 350);
                  }
                }
              } catch (mmErr) {
                console.warn('MetaMask auto-connect error:', mmErr);
                if (typeof updateWalletBtnUI === 'function') updateWalletBtnUI();
              }
            } else if (mmAttempts >= 30) {
              clearInterval(mmPoll);
            }
          }, 150);
        }"""

    if old_auto_connect in text:
        text = text.replace(old_auto_connect, new_auto_connect)
        print(f"Patched in-app auto-connect in {path}")
    else:
        print(f"WARNING: old_auto_connect not found in {path}")

    # 4. Enhance MetaMask Deposit in dashConfirmDepositBtn with mobile browser redirect fallback
    old_mm_deposit = """        // A. METAMASK (EVM) ON-CHAIN / SIGNATURE DEPOSIT
        if ((activeWeb3 && activeWeb3.provider === 'MetaMask') || (userWallet && (userWallet.isEVM || (userWallet.provider && userWallet.provider.toLowerCase().includes('metamask'))))) {
          const mm = getMetaMaskProvider() || window.ethereum;
          if (!mm) {
            alert(getDashNotice('metaMaskNotDetected'));
            return;
          }"""

    new_mm_deposit = """        // A. METAMASK (EVM) ON-CHAIN / SIGNATURE DEPOSIT
        if ((activeWeb3 && activeWeb3.provider === 'MetaMask') || (userWallet && (userWallet.isEVM || (userWallet.provider && userWallet.provider.toLowerCase().includes('metamask'))))) {
          const mm = getMetaMaskProvider() || window.ethereum;
          if (!mm) {
            if (isMobileDevice()) {
              const currentUrl = new URL(window.location.href);
              currentUrl.searchParams.set('autoConnect', 'metamask');
              currentUrl.searchParams.set('autoDeposit', 'web3');
              if (dashDepositAmount) currentUrl.searchParams.set('depositAmount', dashDepositAmount.value);
              const appOrigin = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') ? 'https://haichain.pages.dev' : window.location.origin;
              const targetUrl = appOrigin + currentUrl.pathname + currentUrl.search;
              alert(isVi ? "Đang chuyển sang ứng dụng MetaMask để bạn xác nhận giao dịch bằng tiền thật..." : "Redirecting to MetaMask App to approve transaction with real funds...");
              window.location.href = 'https://metamask.app.link/dapp/' + targetUrl.replace(/^https?:\\/\\//, '');
              return;
            }
            alert(getDashNotice('metaMaskNotDetected'));
            return;
          }"""

    if old_mm_deposit in text:
        text = text.replace(old_mm_deposit, new_mm_deposit)
        print(f"Patched MetaMask deposit fallback in {path}")
    else:
        print(f"WARNING: old_mm_deposit not found in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

print("Finished updating dashboard.html files.")
