import re
import shutil

def patch_phantom_deeplink():
    path = 'assets/phantom-deeplink.js'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    target_old = """        var handoffWallet = params['connectedWallet'];
        var handoffProvider = params['provider'] || 'Phantom';
        var isSolanaAddr = /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(handoffWallet);
        var isEvmAddr = /^0x[a-fA-F0-9]{40}$/i.test(handoffWallet);
        if (handoffWallet && (isSolanaAddr || isEvmAddr)) {
          this.stripParamsAndCleanUrl(['connectedWallet', 'provider']);
          var finalProvider = isEvmAddr ? (handoffProvider || 'MetaMask') : handoffProvider;
          var handoffResult = {
            publicKey: handoffWallet,
            provider: finalProvider,
            isEVM: isEvmAddr,
            source: 'handoff'
          };"""

    replacement_new = """        var handoffWallet = params['connectedWallet'];
        var handoffProvider = params['provider'] || 'Phantom';
        var handoffBalance = params['evmBalance'] || params['balance'] || null;
        var isSolanaAddr = /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(handoffWallet);
        var isEvmAddr = /^0x[a-fA-F0-9]{40}$/i.test(handoffWallet);
        if (handoffWallet && (isSolanaAddr || isEvmAddr)) {
          this.stripParamsAndCleanUrl(['connectedWallet', 'provider', 'evmBalance', 'balance']);
          var finalProvider = isEvmAddr ? (handoffProvider || 'MetaMask') : handoffProvider;
          var handoffResult = {
            publicKey: handoffWallet,
            provider: finalProvider,
            balance: handoffBalance,
            isEVM: isEvmAddr,
            source: 'handoff'
          };"""

    if target_old in content:
        content = content.replace(target_old, replacement_new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Patched assets/phantom-deeplink.js")
    else:
        print("target_old not found in assets/phantom-deeplink.js")

    shutil.copyfile(path, 'app/assets/phantom-deeplink.js')
    print("Synced to app/assets/phantom-deeplink.js")

def patch_dashboard():
    path = 'dashboard.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Cloudflare Ethereum RPC live balance lookup in setConnectedWallet
    old_evm_bal = """      if (isEVM) {
        const mm = getMetaMaskProvider() || window.ethereum;
        if (mm && mm.request) {
          try {
            const rawHex = await mm.request({ method: 'eth_getBalance', params: [pubkeyStr, 'latest'] });
            if (rawHex) {
              const wei = BigInt(rawHex);
              const eth = Number(wei) / 1e18;
              evmBalStr = eth.toFixed(4);
            }
          } catch (e) {
            console.warn("Could not fetch EVM balance:", e);
          }
        }
      }"""

    new_evm_bal = """      if (isEVM) {
        const mm = getMetaMaskProvider() || window.ethereum;
        if (mm && mm.request) {
          try {
            const rawHex = await mm.request({ method: 'eth_getBalance', params: [pubkeyStr, 'latest'] });
            if (rawHex) {
              const wei = BigInt(rawHex);
              const eth = Number(wei) / 1e18;
              evmBalStr = eth.toFixed(4);
            }
          } catch (e) {
            console.warn("Could not fetch EVM balance via provider:", e);
          }
        }
        // Fallback to fast public Cloudflare Ethereum RPC if provider not present or failed
        if (!evmBalStr) {
          try {
            const rpcRes = await fetch('https://cloudflare-eth.com', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                jsonrpc: '2.0',
                method: 'eth_getBalance',
                params: [pubkeyStr, 'latest'],
                id: 1
              })
            });
            if (rpcRes.ok) {
              const rpcData = await rpcRes.json();
              if (rpcData && rpcData.result) {
                const wei = BigInt(rpcData.result);
                evmBalStr = (Number(wei) / 1e18).toFixed(4);
              }
            }
          } catch (rpcErr) {
            console.warn("Could not fetch EVM balance via public RPC:", rpcErr);
          }
        }
      }"""

    if old_evm_bal in content:
        content = content.replace(old_evm_bal, new_evm_bal)
        print("Patched setConnectedWallet in dashboard.html")
    else:
        print("old_evm_bal not found in dashboard.html")

    # 2. Update executeMetaMaskConnect in in-app auto-connect
    old_inapp_return = """                // Prepare return URL and Android Chrome Intent
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
                  const path = cleanBase.replace(/^https?:\/\/[^\/]+/, '');
                  window.location.href = `intent://${host}${path}?${handoffParams}#Intent;scheme=https;package=com.android.chrome;end`;
                } else {
                  setTimeout(() => {
                    window.location.href = finalReturnUrl;
                  }, 400);
                }"""

    new_inapp_return = """                // Prepare return URL and Android Chrome Intent
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

    if old_inapp_return in content:
        content = content.replace(old_inapp_return, new_inapp_return)
        print("Patched in-app auto-connect in dashboard.html")
    else:
        print("old_inapp_return not found in dashboard.html")

    # 3. Patch Remote MCP URL Box (Target 2)
    old_mcp_box = """        <!-- Remote MCP URL Box -->
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-950 border border-neutral-800 space-y-2">
          <div class="flex items-center justify-between gap-2 text-[11px] text-neutral-400">
            <span class="flex items-center space-x-1.5 font-sans truncate min-w-0">
              <i data-lucide="link" class="w-3.5 h-3.5 text-neutral-300 shrink-0"></i>
              <span class="truncate">Remote MCP Connector URL:</span>
            </span>
            <span class="text-[9.5px] bg-neutral-900 border border-neutral-800 px-2 py-0.5 rounded-full text-neutral-300 font-mono shrink-0 whitespace-nowrap">SSE / HTTPS</span>
          </div>"""

    new_mcp_box = """        <!-- Remote MCP URL Box -->
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-950 border border-neutral-800 space-y-2">
          <div class="flex flex-wrap items-center justify-between gap-1.5 text-[11px] text-neutral-400">
            <span class="flex items-center space-x-1.5 font-sans">
              <i data-lucide="link" class="w-3.5 h-3.5 text-neutral-300 shrink-0"></i>
              <span class="text-neutral-300 font-medium">Remote MCP Connector URL:</span>
            </span>
            <span class="text-[9px] bg-neutral-900 border border-neutral-800 px-2 py-0.5 rounded-full text-neutral-400 font-mono shrink-0 whitespace-nowrap">SSE / HTTPS</span>
          </div>"""

    if old_mcp_box in content:
        content = content.replace(old_mcp_box, new_mcp_box)
        print("Patched Remote MCP URL Box in dashboard.html")
    else:
        print("old_mcp_box not found in dashboard.html")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Wrote dashboard.html")

    shutil.copyfile(path, 'app/dashboard.html')
    print("Synced to app/dashboard.html")

patch_phantom_deeplink()
patch_dashboard()
