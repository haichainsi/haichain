import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

# 1. Add startMetaMaskSessionPoller and update onTabWakeup
old_on_tab_wakeup = """    const onTabWakeup = async () => {
      if (userWallet && userWallet.address) return;
      


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

new_on_tab_wakeup = """    function startMetaMaskSessionPoller(sessId) {
      if (!sessId) return;
      console.log('[MetaMaskRelay] Starting poller for session:', sessId);
      let pollCount = 0;
      const maxPolls = 120;
      if (window.__metaMaskPollerInterval) clearInterval(window.__metaMaskPollerInterval);
      
      window.__metaMaskPollerInterval = setInterval(async () => {
        pollCount++;
        if (pollCount > maxPolls || (userWallet && userWallet.address)) {
          clearInterval(window.__metaMaskPollerInterval);
          return;
        }

        try {
          const res = await fetch(`/api/wallet-relay?sess_id=${encodeURIComponent(sessId)}`, {
            headers: { 'Cache-Control': 'no-cache' }
          });
          if (res.ok) {
            const data = await res.json();
            if (data && data.address && /^0x[a-fA-F0-9]{40}$/i.test(data.address)) {
              console.log('[MetaMaskRelay] Poller received connected wallet:', data.address);
              clearInterval(window.__metaMaskPollerInterval);
              try { localStorage.removeItem('haichain_metamask_pending_session'); } catch (_) {}
              await setConnectedWallet(data.address, data.provider || 'MetaMask');
              if (data.evmBalance && userWallet) {
                userWallet.evmBalance = data.evmBalance;
                userWallet.solBalance = data.evmBalance + ' ETH';
              }
              updateWalletBtnUI();
              if (walletConnectModal) walletConnectModal.classList.add('hidden');
              showToast({
                title: 'MetaMask Connected',
                message: data.address.slice(0, 6) + '...' + data.address.slice(-4),
                icon: 'check-circle'
              });
              openAccountModal();
            }
          }
        } catch (e) {
          console.warn('[MetaMaskRelay] Polling error:', e);
        }
      }, 1000);
    }

    const onTabWakeup = async () => {
      if (userWallet && userWallet.address) return;

      // 1. Check Cloudflare Session Relay for pending MetaMask mobile session
      try {
        const pendingSess = window.__currentMetaMaskSessionId || localStorage.getItem('haichain_metamask_pending_session');
        if (pendingSess && (!userWallet || !userWallet.address)) {
          const resp = await fetch(`/api/wallet-relay?sess_id=${encodeURIComponent(pendingSess)}`, { headers: { 'Cache-Control': 'no-cache' } });
          if (resp.ok) {
            const data = await resp.json();
            if (data && data.address && /^0x[a-fA-F0-9]{40}$/i.test(data.address)) {
              console.log('[MetaMaskRelay] onTabWakeup found connected session:', data.address);
              try { localStorage.removeItem('haichain_metamask_pending_session'); } catch (_) {}
              await setConnectedWallet(data.address, data.provider || 'MetaMask');
              if (data.evmBalance && userWallet) {
                userWallet.evmBalance = data.evmBalance;
                userWallet.solBalance = data.evmBalance + ' ETH';
              }
              updateWalletBtnUI();
              if (walletConnectModal) walletConnectModal.classList.add('hidden');
              showToast({
                title: 'MetaMask Connected',
                message: data.address.slice(0, 6) + '...' + data.address.slice(-4),
                icon: 'check-circle'
              });
              openAccountModal();
              return;
            }
          }
        }
      } catch (_) {}

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

if old_on_tab_wakeup in dash:
    dash = dash.replace(old_on_tab_wakeup, new_on_tab_wakeup, 1)
    print("Updated onTabWakeup and added startMetaMaskSessionPoller")
else:
    print("WARNING: old_on_tab_wakeup not matched exactly")

# 2. Update executeMetaMaskConnect in dashboard.html
old_mm_connect_handoff = """                // Prepare clean HTTPS return URL (No blocked intent:// schemes)
                const baseReturn = returnUrlParam ? decodeURIComponent(returnUrlParam) : (window.location.origin + window.location.pathname);
                const cleanBase = baseReturn.split('?')[0];
                const handoffParams = `connectedWallet=${encodeURIComponent(account)}&provider=MetaMask&evmBalance=${encodeURIComponent(ethBal)}`;
                const finalReturnUrl = `${cleanBase}?${handoffParams}`;

                // Update prompt sheet with clear, seamless Web3 actions (Eliminating Android intent block)
                promptSheet.innerHTML = `
                  <div class="bg-neutral-950 border border-neutral-800 rounded-3xl p-6 max-w-sm w-full text-center space-y-4 shadow-2xl text-white animate-scaleUp">
                    <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 flex items-center justify-center text-2xl font-bold shadow-lg">✓</div>
                    <div class="space-y-1.5">
                      <h3 class="text-base font-bold text-white uppercase tracking-wider">${isVi ? 'Đã Kết Nối MetaMask Thành Công!' : 'MetaMask Wallet Connected!'}</h3>
                      <div class="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-xs font-mono text-emerald-400">
                        <span>●</span>
                        <span>${account.slice(0, 6)}...${account.slice(-4)} (${ethBal} ETH)</span>
                      </div>
                      <p class="text-[12px] text-neutral-300 font-sans leading-relaxed pt-1">
                        ${isVi 
                          ? 'Ví thật đã kết nối thành công. Bạn có thể sử dụng ngay trong MetaMask hoặc quay về trình duyệt ngoài.' 
                          : 'Real wallet connected. You can use it directly inside MetaMask or return to your browser.'}
                      </p>
                    </div>

                    <!-- Primary Action: Continue in MetaMask -->
                    <button type="button" id="btn-continue-in-metamask" class="w-full py-3.5 px-4 rounded-xl bg-white text-black font-bold text-xs uppercase tracking-wider flex items-center justify-center space-x-2 shadow-lg hover:bg-neutral-200 active:scale-95 transition-all cursor-pointer">
                      <span>${isVi ? 'Tiếp Tục Sử Dụng Trong MetaMask' : 'Continue Inside MetaMask'}</span>
                      <span>&rarr;</span>
                    </button>

                    <!-- Secondary Action: Return / Copy Link for Chrome/Safari -->
                    <div class="pt-2 border-t border-neutral-800/80 space-y-2">
                      <button type="button" id="btn-copy-return-link" class="w-full py-2.5 px-3 rounded-xl bg-neutral-900 border border-neutral-700/80 text-[11px] font-mono text-neutral-300 hover:text-white hover:bg-neutral-800 transition-all flex items-center justify-center space-x-1.5 cursor-pointer">
                        <svg class="w-3.5 h-3.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                        <span id="btn-copy-return-link-text">${isVi ? 'Sao chép link có ví (để dán vào Chrome)' : 'Copy Link With Wallet (Paste into Chrome)'}</span>
                      </button>
                      <a href="${finalReturnUrl}" class="block w-full py-1.5 text-[11px] text-neutral-400 hover:text-white underline transition-colors">
                        ${isVi ? 'Quay về trình duyệt ngoài (HTTPS)' : 'Return to browser (HTTPS)'}
                      </a>
                    </div>
                  </div>
                `;

                let autoCloseTimer = null;

                const handleContinueInMetaMask = () => {
                  if (autoCloseTimer) clearTimeout(autoCloseTimer);
                  if (promptSheet && promptSheet.parentNode) {
                    promptSheet.remove();
                  }
                  updateWalletBtnUI();
                  showMetaMaskMobileHandoffBar(account, returnUrlParam);

                  if (autoDeposit === 'web3') {
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
                  } else {
                    if (typeof openAccountModal === 'function') openAccountModal();
                  }
                };

                const continueBtn = document.getElementById('btn-continue-in-metamask');
                if (continueBtn) continueBtn.addEventListener('click', handleContinueInMetaMask);

                const copyBtn = document.getElementById('btn-copy-return-link');
                if (copyBtn) {
                  copyBtn.addEventListener('click', async () => {
                    const textSpan = document.getElementById('btn-copy-return-link-text');
                    try {
                      if (navigator.clipboard && navigator.clipboard.writeText) {
                        await navigator.clipboard.writeText(finalReturnUrl);
                      } else {
                        const tArea = document.createElement('textarea');
                        tArea.value = finalReturnUrl;
                        document.body.appendChild(tArea);
                        tArea.select();
                        document.execCommand('copy');
                        document.body.removeChild(tArea);
                      }
                      if (textSpan) {
                        textSpan.textContent = isVi ? '✓ Đã sao chép link! Dán vào Chrome/Safari' : '✓ Copied! Paste into Chrome/Safari';
                        textSpan.className = 'text-emerald-400 font-bold';
                      }
                      if (typeof showToast === 'function') {
                        showToast({
                          title: isVi ? 'Đã sao chép link ví' : 'Wallet Link Copied',
                          message: isVi ? 'Mở Chrome hoặc Safari và dán link để tiếp tục phiên ví' : 'Paste into Chrome or Safari to continue',
                          icon: 'check-circle'
                        });
                      }
                    } catch (e) {
                      console.warn('Copy failed:', e);
                    }
                  });
                }

                // Smooth auto-transition after 3.5s so user is never stuck
                autoCloseTimer = setTimeout(() => {
                  if (promptSheet && promptSheet.parentNode) {
                    handleContinueInMetaMask();
                  }
                }, 3500);"""

new_mm_connect_handoff = """                // 1. Post to Cloudflare Session Relay for instant background cross-browser sync
                try {
                  const sessIdParam = urlParams.get('sess_id') || urlParams.get('sessId');
                  if (sessIdParam) {
                    fetch('/api/wallet-relay', {
                      method: 'POST',
                      headers: { 'Content-Type': 'application/json' },
                      body: JSON.stringify({
                        sessId: sessIdParam,
                        address: account,
                        provider: 'MetaMask',
                        evmBalance: ethBal
                      })
                    }).catch(e => console.warn('Relay POST error:', e));
                  }
                } catch (_) {}

                // 2. Prepare return URLs and browser schemes
                const baseReturn = returnUrlParam ? decodeURIComponent(returnUrlParam) : (window.location.origin + window.location.pathname);
                const cleanBase = baseReturn.split('?')[0];
                const handoffParams = `connectedWallet=${encodeURIComponent(account)}&provider=MetaMask&evmBalance=${encodeURIComponent(ethBal)}`;
                const finalReturnUrl = `${cleanBase}?${handoffParams}`;
                const host = window.location.host;
                const path = cleanBase.replace(/^https?:\\/\\/[^\\/]+/, '') || '/dashboard.html';

                const isAndroid = /Android/i.test(navigator.userAgent);
                const chromeSchemeUrl = `googlechrome://navigate?url=${encodeURIComponent(finalReturnUrl)}`;
                const browsableIntentUrl = `intent://${host}${path}?${handoffParams}#Intent;scheme=https;action=android.intent.action.VIEW;category=android.intent.category.BROWSABLE;end`;

                // 3. Update prompt sheet to successful return UI with clear auto-return countdown
                promptSheet.innerHTML = `
                  <div class="bg-neutral-950 border border-neutral-800 rounded-3xl p-6 max-w-sm w-full text-center space-y-4 shadow-2xl text-white animate-scaleUp">
                    <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 flex items-center justify-center text-2xl font-bold shadow-lg">✓</div>
                    <div class="space-y-1.5">
                      <h3 class="text-base font-bold text-white uppercase tracking-wider">${isVi ? 'Đã Kết Nối MetaMask!' : 'MetaMask Connected!'}</h3>
                      <div class="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-neutral-900 border border-neutral-800 text-xs font-mono text-emerald-400">
                        <span>●</span>
                        <span>${account.slice(0, 6)}...${account.slice(-4)} (${ethBal} ETH)</span>
                      </div>
                      <p id="return-countdown-msg" class="text-[12px] text-neutral-300 font-sans leading-relaxed pt-1">
                        ${isVi 
                          ? 'Đang tự động quay lại Dashboard trong <span id="return-timer-sec" class="text-white font-bold">1s</span>...' 
                          : 'Auto-returning to Dashboard in <span id="return-timer-sec" class="text-white font-bold">1s</span>...'}
                      </p>
                    </div>

                    <!-- Primary Action Button: Return Immediately (Active User Gesture) -->
                    <button type="button" id="btn-return-external-browser" class="w-full py-3.5 px-4 rounded-xl bg-white text-black font-bold text-xs uppercase tracking-wider flex items-center justify-center space-x-2 shadow-lg hover:bg-neutral-200 active:scale-95 transition-all cursor-pointer">
                      <span>${isVi ? 'Quay Lại Dashboard Ngay' : 'Return to Dashboard Now'}</span>
                      <span>&rarr;</span>
                    </button>

                    <!-- Secondary Option: Continue inside MetaMask -->
                    <div class="pt-2 border-t border-neutral-800/80 space-y-2">
                      <button type="button" id="btn-stay-in-metamask" class="w-full py-2 text-[11px] text-neutral-400 hover:text-white underline cursor-pointer">
                        ${isVi ? 'Hoặc tiếp tục sử dụng ngay trong MetaMask' : 'Or continue inside MetaMask browser'}
                      </button>
                    </div>
                  </div>
                `;

                const executeHandoff = () => {
                  console.log('[MetaMask] Returning to mobile browser dashboard:', finalReturnUrl);
                  if (isAndroid) {
                    try {
                      window.location.href = chromeSchemeUrl;
                    } catch (_) {
                      window.location.href = browsableIntentUrl;
                    }
                    setTimeout(() => {
                      try {
                        window.location.href = browsableIntentUrl;
                      } catch (_) {
                        window.location.href = finalReturnUrl;
                      }
                    }, 400);
                  } else {
                    window.location.href = finalReturnUrl;
                  }
                };

                let returnTimer = null;
                const returnBtn = document.getElementById('btn-return-external-browser');
                if (returnBtn) {
                  returnBtn.addEventListener('click', () => {
                    if (returnTimer) clearTimeout(returnTimer);
                    executeHandoff();
                  });
                }

                const stayBtn = document.getElementById('btn-stay-in-metamask');
                if (stayBtn) {
                  stayBtn.addEventListener('click', () => {
                    if (returnTimer) clearTimeout(returnTimer);
                    promptSheet.remove();
                    updateWalletBtnUI();
                    showMetaMaskMobileHandoffBar(account, returnUrlParam);
                    if (typeof openAccountModal === 'function') openAccountModal();
                  });
                }

                // Automatic handoff countdown after 800ms
                returnTimer = setTimeout(() => {
                  executeHandoff();
                }, 800);"""

if old_mm_connect_handoff in dash:
    dash = dash.replace(old_mm_connect_handoff, new_mm_connect_handoff, 1)
    print("Updated MetaMask in-app connect handoff with auto-return and session relay")
else:
    print("WARNING: old_mm_connect_handoff not matched exactly")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash)

with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash)

print("Synchronized dashboard.html and app/dashboard.html successfully!")
