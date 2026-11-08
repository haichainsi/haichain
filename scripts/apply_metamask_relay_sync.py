import sys
sys.stdout.reconfigure(encoding='utf-8')

for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update MetaMask mobile button handler to start poller
    old_btn_block = """          } else if (isMobileDevice()) {
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

    new_btn_block = """          } else if (isMobileDevice()) {
            // MOBILE 1-CLICK DEEPLINK (Mirroring Phantom UX: Direct native app launch & seamless auto-return)
            walletConnectModal.classList.add('hidden');
            const isVi = window.haichainI18n?.currentLang === 'vi';
            walletBtnText.textContent = getDashNotice('connectingMetaMask') || (isVi ? 'Đang mở MetaMask...' : 'Opening MetaMask...');
            
            const sessId = 'mm_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2, 8);
            window.__currentMetaMaskSessionId = sessId;
            try { localStorage.setItem('haichain_metamask_pending_session', sessId); } catch (_) {}
            if (typeof startMetaMaskSessionPoller === 'function') startMetaMaskSessionPoller(sessId);

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
                const targetUrl = appOrigin + window.location.pathname + '?auto_connect=metamask&sess_id=' + sessId + '&return_url=' + encodeURIComponent(window.location.href);
                window.location.href = 'https://metamask.app.link/dapp/' + targetUrl.replace(/^https?:\\/\\//, '');
              }
            }, 150);
          }"""

    if old_btn_block in text:
        text = text.replace(old_btn_block, new_btn_block)
        print(f"Patched MetaMask mobile button block in {path}")
    else:
        print(f"WARNING: old_btn_block not found in {path}")

    # 2. Add startMetaMaskSessionPoller and update in-app auto-connect
    old_handoff_func = """    // Luxury Black & White Return Banner for MetaMask In-App Browser to Safari/Chrome
    function showMetaMaskMobileHandoffBar(account, returnUrl) {"""

    new_handoff_func = """    // Session Poller for Cross-Browser MetaMask Mobile Handshake
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
    }

    // Luxury Black & White Return Banner for MetaMask In-App Browser to Safari/Chrome
    function showMetaMaskMobileHandoffBar(account, returnUrl) {"""

    if old_handoff_func in text:
        text = text.replace(old_handoff_func, new_handoff_func)
        print(f"Patched startMetaMaskSessionPoller in {path}")
    else:
        print(f"WARNING: old_handoff_func not found in {path}")

    # 3. Update MetaMask In-App Browser Auto-Connect with 1-tap sheet, relay POST, and auto-intent
    old_mm_inapp = """        // A. METAMASK IN-APP AUTO-CONNECT (NATIVE MOBILE WEB3 HANDSHAKE)
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

    new_mm_inapp = """        // A. METAMASK IN-APP AUTO-CONNECT (NATIVE MOBILE WEB3 HANDSHAKE)
        if (autoProvider === 'metamask') {
          const sessIdParam = urlParams.get('sess_id') || urlParams.get('sessId');
          const returnUrlParam = urlParams.get('return_url') || urlParams.get('returnUrl');

          const cleanUrl = new URL(window.location.href);
          cleanUrl.searchParams.delete('autoConnect');
          cleanUrl.searchParams.delete('auto_connect');
          cleanUrl.searchParams.delete('autoDeposit');
          cleanUrl.searchParams.delete('auto_deposit');
          cleanUrl.searchParams.delete('depositAmount');
          cleanUrl.searchParams.delete('deposit_amount');
          cleanUrl.searchParams.delete('return_url');
          cleanUrl.searchParams.delete('returnUrl');
          cleanUrl.searchParams.delete('sess_id');
          cleanUrl.searchParams.delete('sessId');
          window.history.replaceState({}, document.title, cleanUrl.toString());

          // Render instant touch authorization overlay (prevents mobile popup suppression)
          const isVi = window.haichainI18n?.currentLang === 'vi';
          const promptSheet = document.createElement('div');
          promptSheet.id = 'metamask-inapp-prompt-sheet';
          promptSheet.className = 'fixed inset-0 z-[99999] bg-black/95 backdrop-blur-md flex items-center justify-center p-4 animate-fadeIn';
          promptSheet.innerHTML = `
            <div class="bg-neutral-950 border border-neutral-800 rounded-3xl p-6 max-w-sm w-full text-center space-y-4 shadow-2xl text-white">
              <div class="w-16 h-16 mx-auto rounded-2xl bg-white text-black flex items-center justify-center text-3xl font-bold shadow-lg">
                🦊
              </div>
              <div class="space-y-1">
                <h3 class="text-base font-bold text-white uppercase tracking-wider">${isVi ? 'Xác Nhận Kết Nối MetaMask' : 'Authorize MetaMask Wallet'}</h3>
                <p class="text-xs text-neutral-400">${isVi ? 'Chạm nút bên dưới để cấp quyền ví thật và đồng bộ về Dashboard HAICHAIN.' : 'Tap below to authorize your real wallet and sync to HAICHAIN Dashboard.'}</p>
              </div>
              <button type="button" id="btn-metamask-inapp-confirm" class="w-full py-3.5 px-4 rounded-xl bg-white text-black font-bold text-xs uppercase tracking-wider flex items-center justify-center space-x-2 shadow hover:bg-neutral-200 active:scale-95 transition-all cursor-pointer">
                <span>${isVi ? 'Xác Nhận Kết Nối Ví Ngay' : 'Authorize & Connect Wallet'}</span>
                <span>&rarr;</span>
              </button>
            </div>
          `;
          document.body.prepend(promptSheet);

          const executeMetaMaskConnect = async () => {
            const mm = getMetaMaskProvider() || window.ethereum;
            if (!mm || !mm.request) return;

            try {
              if (typeof walletBtnText !== 'undefined' && walletBtnText) {
                walletBtnText.textContent = 'Connecting MetaMask...';
              }
              const accounts = await mm.request({ method: 'eth_requestAccounts' });
              if (accounts && accounts[0]) {
                const account = accounts[0];
                let ethBal = '0.0000';
                try {
                  const rawHex = await mm.request({ method: 'eth_getBalance', params: [account, 'latest'] });
                  if (rawHex) {
                    const wei = BigInt(rawHex);
                    ethBal = (Number(wei) / 1e18).toFixed(4);
                  }
                } catch (_) {}

                await setConnectedWallet(account, 'MetaMask');
                if (userWallet) {
                  userWallet.evmBalance = ethBal;
                  userWallet.solBalance = ethBal + ' ETH';
                  updateWalletBtnUI();
                }

                try {
                  document.cookie = 'haichain-connected-wallet=' + encodeURIComponent(JSON.stringify(userWallet)) + '; Path=/; Max-Age=2592000; SameSite=Lax';
                } catch (_) {}

                // Notify session relay for external browser sync
                if (sessIdParam) {
                  try {
                    await fetch('/api/wallet-relay', {
                      method: 'POST',
                      headers: { 'Content-Type': 'application/json' },
                      body: JSON.stringify({ id: sessIdParam, address: account, provider: 'MetaMask', balance: ethBal })
                    });
                  } catch (_) {}
                }

                // Prepare return URL and Android Chrome Intent
                const baseReturn = returnUrlParam ? decodeURIComponent(returnUrlParam) : (window.location.origin + window.location.pathname);
                const cleanBase = baseReturn.split('?')[0];
                const handoffParams = `connectedWallet=${encodeURIComponent(account)}&provider=MetaMask&evmBalance=${encodeURIComponent(ethBal)}`;
                const finalReturnUrl = `${cleanBase}?${handoffParams}`;

                // Update prompt sheet to successful return UI with 1-click button
                promptSheet.innerHTML = `
                  <div class="bg-neutral-950 border border-neutral-800 rounded-3xl p-6 max-w-sm w-full text-center space-y-4 shadow-2xl text-white">
                    <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 flex items-center justify-center text-2xl font-bold">✓</div>
                    <div class="space-y-1">
                      <h3 class="text-base font-bold text-white">${isVi ? 'Đã Kết Nối Ví MetaMask Thực Tế!' : 'MetaMask Wallet Connected!'}</h3>
                      <p class="text-xs font-mono text-neutral-300">${account.slice(0, 6)}...${account.slice(-4)} (${ethBal} ETH)</p>
                    </div>
                    <a href="${finalReturnUrl}" id="btn-return-external-browser" class="w-full py-3.5 px-4 rounded-xl bg-white text-black font-bold text-xs uppercase tracking-wider flex items-center justify-center space-x-2 shadow hover:bg-neutral-200 transition-all cursor-pointer">
                      <span>${isVi ? 'Quay về Safari / Chrome Ngay' : 'Return to Safari / Chrome'}</span>
                      <span>&rarr;</span>
                    </a>
                    <button type="button" onclick="document.getElementById('metamask-inapp-prompt-sheet').remove()" class="w-full py-2 text-[11px] text-neutral-400 hover:text-white underline cursor-pointer">
                      ${isVi ? 'Hoặc tiếp tục sử dụng ngay trong MetaMask' : 'Or continue inside MetaMask browser'}
                    </button>
                  </div>
                `;

                // Auto-redirect via Android Intent or direct URL
                const isAndroid = /Android/i.test(navigator.userAgent);
                if (isAndroid) {
                  const host = window.location.host;
                  const path = cleanBase.replace(/^https?:\\/\\/[^\\/]+/, '');
                  window.location.href = `intent://${host}${path}?${handoffParams}#Intent;scheme=https;package=com.android.chrome;end`;
                } else {
                  setTimeout(() => {
                    window.location.href = finalReturnUrl;
                  }, 300);
                }

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
            } catch (err) {
              console.warn('MetaMask connect execution rejected:', err);
              if (promptSheet) promptSheet.remove();
              if (typeof updateWalletBtnUI === 'function') updateWalletBtnUI();
            }
          };

          const confirmBtn = document.getElementById('btn-metamask-inapp-confirm');
          if (confirmBtn) {
            confirmBtn.addEventListener('click', executeMetaMaskConnect);
          }

          // Also attempt immediate request
          executeMetaMaskConnect();
        }"""

    if old_mm_inapp in text:
        text = text.replace(old_mm_inapp, new_mm_inapp)
        print(f"Patched in-app auto-connect in {path}")
    else:
        print(f"WARNING: old_mm_inapp not found in {path}")

    # 4. Enhance onTabWakeup to poll relay on resume
    old_wakeup = """    const onTabWakeup = async () => {
      if (userWallet && userWallet.address) return;
      const isConnected = await checkMobileWalletSyncOrCallback();
      if (!isConnected) {
        if (walletConnectRevertTimer) clearTimeout(walletConnectRevertTimer);
        walletConnectRevertTimer = setTimeout(() => {
          if (!userWallet || !userWallet.address) {
            updateWalletBtnUI();
          }
        }, 1500);
      }
    };"""

    new_wakeup = """    const onTabWakeup = async () => {
      if (userWallet && userWallet.address) return;
      
      // 1. Check relay session
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
      }

      // 2. Check standard URL params or storage
      const isConnected = await checkMobileWalletSyncOrCallback();
      if (!isConnected) {
        if (walletConnectRevertTimer) clearTimeout(walletConnectRevertTimer);
        walletConnectRevertTimer = setTimeout(() => {
          if (!userWallet || !userWallet.address) {
            updateWalletBtnUI();
          }
        }, 1500);
      }
    };"""

    if old_wakeup in text:
        text = text.replace(old_wakeup, new_wakeup)
        print(f"Patched onTabWakeup in {path}")
    else:
        print(f"WARNING: old_wakeup not found in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

print("Finished updating dashboard.html files.")
