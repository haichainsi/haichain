import os

for filepath in ['dashboard.html', 'app/dashboard.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add connectedWallet URL param reading in checkMobileWalletSyncOrCallback
    target_sync = "// 3. Check for official E2EE Redirect Callback or Handoff in URL"
    replacement_sync = """// 2.5. Check URL parameters for direct connectedWallet handoff
      try {
        const urlParams = new URLSearchParams(window.location.search);
        const qWallet = urlParams.get('connectedWallet') || urlParams.get('wallet');
        const qProvider = urlParams.get('provider') || 'MetaMask';
        const qEvmBal = urlParams.get('evmBalance');
        if (qWallet && (/^0x[a-fA-F0-9]{40}$/i.test(qWallet) || /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(qWallet))) {
          console.log('[MobileWallet] Found connectedWallet in URL query:', qWallet, qProvider);
          await setConnectedWallet(qWallet, qProvider);
          if (qEvmBal && userWallet) {
            userWallet.evmBalance = qEvmBal;
            userWallet.solBalance = qEvmBal + ' ETH';
          }
          updateWalletBtnUI();
          if (typeof updateEarlyAllocationsUI === 'function') updateEarlyAllocationsUI();
          const cleanUrl = new URL(window.location.href);
          cleanUrl.searchParams.delete('connectedWallet');
          cleanUrl.searchParams.delete('wallet');
          cleanUrl.searchParams.delete('provider');
          cleanUrl.searchParams.delete('evmBalance');
          window.history.replaceState({}, document.title, cleanUrl.pathname + (cleanUrl.search ? cleanUrl.search : ''));
          return true;
        }
      } catch (_) {}

      // 3. Check for official E2EE Redirect Callback or Handoff in URL"""

    if target_sync in content and "// 2.5. Check URL parameters for direct connectedWallet handoff" not in content:
        content = content.replace(target_sync, replacement_sync, 1)
        print(f"Added URL param handler to {filepath}")

    # 2. Replace the MetaMask in-app prompt sheet success UI and remove intent://
    old_handoff_block = """                // Prepare return URL and Android Chrome Intent
                const baseReturn = returnUrlParam ? decodeURIComponent(returnUrlParam) : (window.location.origin + window.location.pathname);
                const cleanBase = baseReturn.split('?')[0];
                const handoffParams = `connectedWallet=${encodeURIComponent(account)}&provider=MetaMask&evmBalance=${encodeURIComponent(ethBal)}`;
                const finalReturnUrl = `${cleanBase}?${handoffParams}`;
                const host = window.location.host;
                const path = cleanBase.replace(/^https?:\\/\\/[^\\/]+/, '') || '/dashboard.html';

                const isAndroid = /Android/i.test(navigator.userAgent);
                const chromeIntent = `intent://${host}${path}?${handoffParams}#Intent;scheme=https;package=com.android.chrome;end`;
                const browsableIntent = `intent://${host}${path}?${handoffParams}#Intent;scheme=https;action=android.intent.action.VIEW;category=android.intent.category.BROWSABLE;end`;

                // Update prompt sheet to successful return UI with active user gesture button & auto-return
                promptSheet.innerHTML = `
                  <div class="bg-neutral-950 border border-neutral-800 rounded-3xl p-6 max-w-sm w-full text-center space-y-4 shadow-2xl text-white">
                    <div class="w-14 h-14 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 flex items-center justify-center text-2xl font-bold">✓</div>
                    <div class="space-y-1">
                      <h3 class="text-base font-bold text-white">${isVi ? 'Đã Kết Nối Ví MetaMask Thực Tế!' : 'MetaMask Wallet Connected!'}</h3>
                      <p class="text-xs font-mono text-neutral-300">${account.slice(0, 6)}...${account.slice(-4)} (${ethBal} ETH)</p>
                      <p class="text-[11px] text-neutral-400 font-sans">${isVi ? 'Đang tự động chuyển về trình duyệt của bạn...' : 'Returning to your browser...'}</p>
                    </div>
                    <button type="button" id="btn-return-external-browser" class="w-full py-3.5 px-4 rounded-xl bg-white text-black font-bold text-xs uppercase tracking-wider flex items-center justify-center space-x-2 shadow hover:bg-neutral-200 active:scale-95 transition-all cursor-pointer">
                      <span>${isVi ? 'Quay Về Trình Duyệt Ngay (Chrome/Safari)' : 'Return to Browser (Chrome/Safari)'}</span>
                      <span>&rarr;</span>
                    </button>
                    <button type="button" id="btn-stay-in-metamask" class="w-full py-2 text-[11px] text-neutral-400 hover:text-white underline cursor-pointer">
                      ${isVi ? 'Hoặc tiếp tục sử dụng ngay trong MetaMask (Đã kết nối)' : 'Or continue inside MetaMask browser (Connected)'}
                    </button>
                  </div>
                `;

                const executeAutoHandoff = () => {
                  console.log('[MetaMask] Executing handoff to mobile browser...');
                  if (isAndroid) {
                    try {
                      window.location.href = chromeIntent;
                    } catch (_) {
                      window.location.href = browsableIntent;
                    }
                  } else {
                    window.location.href = finalReturnUrl;
                  }
                };

                const returnBtn = document.getElementById('btn-return-external-browser');
                if (returnBtn) returnBtn.addEventListener('click', executeAutoHandoff);

                const stayBtn = document.getElementById('btn-stay-in-metamask');
                if (stayBtn) {
                  stayBtn.addEventListener('click', () => {
                    promptSheet.remove();
                    updateWalletBtnUI();
                    if (typeof openAccountModal === 'function') openAccountModal();
                  });
                }

                // Automatic redirect attempt immediately
                setTimeout(executeAutoHandoff, 250);"""

    new_handoff_block = """                // Prepare clean HTTPS return URL (No blocked intent:// schemes)
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

    if old_handoff_block in content:
        content = content.replace(old_handoff_block, new_handoff_block, 1)
        print(f"Replaced MetaMask handoff block in {filepath}")
    else:
        print(f"WARNING: old_handoff_block not found in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
