import re

def update_dashboard_file(filepath):
    print(f"Patching {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Tab 2 HTML
    old_hub_box = '''        <!-- Official Server URL Box -->
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-950 border border-neutral-800 space-y-2">
          <div class="flex flex-wrap items-center justify-between gap-1.5 text-[11px] text-neutral-400">
            <span class="flex items-center space-x-1.5 font-sans">
              <i data-lucide="link" class="w-3.5 h-3.5 text-neutral-300 shrink-0"></i>
              <span class="text-neutral-300 font-medium" data-i18n="aiHub.onlineUrlLabel">MCP Server URL (For Claude Mobile):</span>
            </span>
            <span class="text-[9px] bg-emerald-950/80 border border-emerald-800/80 px-2 py-0.5 rounded-full text-emerald-400 font-mono shrink-0 whitespace-nowrap">Streamable HTTP / SSL</span>
          </div>
          <div class="p-2.5 rounded-xl bg-black border border-neutral-800 font-mono text-emerald-400 text-xs sm:text-[13px] overflow-x-auto select-all break-all flex items-center justify-between">
            <code id="online-mcp-url-snippet">https://mcp.haichain.si/api/mcp</code>
          </div>
        </div>'''

    new_hub_box = '''        <!-- Official Server URL Box (Dynamic Dedicated Vault Binding) -->
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-950 border border-neutral-800 space-y-2.5">
          <div class="flex flex-wrap items-center justify-between gap-1.5 text-[11px] text-neutral-400">
            <span class="flex items-center space-x-1.5 font-sans">
              <i data-lucide="link" class="w-3.5 h-3.5 text-neutral-300 shrink-0"></i>
              <span class="text-neutral-300 font-medium" data-i18n="aiHub.onlineUrlLabel">MCP Server URL (For Claude Mobile):</span>
            </span>
            <span id="online-mcp-badge" class="text-[9px] bg-amber-950/80 border border-amber-800/80 px-2 py-0.5 rounded-full text-amber-400 font-mono shrink-0 whitespace-nowrap flex items-center space-x-1">
              <span class="w-1.5 h-1.5 rounded-full bg-amber-400 shrink-0"></span>
              <span data-i18n="aiHub.badgeGeneric">⚡ URL CHUNG (CHƯA GẮN VÍ)</span>
            </span>
          </div>
          <div class="p-2.5 rounded-xl bg-black border border-neutral-800 font-mono text-emerald-400 text-xs sm:text-[13px] overflow-x-auto select-all break-all flex items-center justify-between">
            <code id="online-mcp-url-snippet">https://mcp.haichain.si/api/mcp</code>
          </div>

          <!-- Vault Binding Dynamic Status Card -->
          <div id="online-mcp-connected-box" class="hidden p-2.5 rounded-xl bg-emerald-950/30 border border-emerald-800/40 flex items-start space-x-2 text-[11px] text-emerald-300 font-sans">
            <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-400 shrink-0 mt-0.5"></i>
            <div>
              <span class="font-bold text-white" data-i18n="aiHub.connectedTitle">URL Cá Nhân Hóa Dành Riêng Cho Ví:</span> 
              <span id="online-mcp-bound-addr" class="font-mono text-emerald-400 underline font-semibold"></span>
              <p class="text-[10px] text-neutral-400 mt-0.5" data-i18n="aiHub.connectedDesc">AI Claude Mobile sẽ tự động liên kết thẳng vào két chi tiêu của ví này mà không cần nhập thủ công địa chỉ trong khung chat.</p>
            </div>
          </div>

          <div id="online-mcp-unconnected-box" class="p-2.5 rounded-xl bg-amber-950/20 border border-amber-800/40 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-[11px] font-sans">
            <div class="flex items-start space-x-2 text-amber-200">
              <i data-lucide="wallet" class="w-4 h-4 text-amber-400 shrink-0 mt-0.5"></i>
              <div>
                <span class="font-semibold text-white" data-i18n="aiHub.unconnectedTitle">Bạn muốn AI cá nhân hóa theo ví riêng?</span>
                <p class="text-[10px] text-neutral-400" data-i18n="aiHub.unconnectedDesc">Kết nối ví ngay để hệ thống tự động sinh Server URL độc quyền gắn mã két của bạn.</p>
              </div>
            </div>
            <button id="online-mcp-trigger-connect-btn" type="button" class="shrink-0 px-3 py-1.5 rounded-lg bg-white text-black hover:bg-neutral-200 font-bold text-[11px] flex items-center justify-center space-x-1.5 transition-all cursor-pointer shadow-xs active:scale-98">
              <i data-lucide="zap" class="w-3.5 h-3.5 text-black"></i>
              <span data-i18n="aiHub.btnConnectForLink">⚡ Kết nối ví để nhận link riêng</span>
            </button>
          </div>
        </div>'''

    if old_hub_box in html:
        html = html.replace(old_hub_box, new_hub_box)
        print("Replaced old_hub_box successfully.")
    else:
        print("WARNING: old_hub_box not found directly, checking partial...")

    # 2. Update Step 2 in Guide
    old_step2 = '<span data-i18n="aiHub.onlineStep2">Set Name to \'HAICHAIN\' and paste the Server URL https://mcp.haichain.si/api/mcp into the URL field.</span>'
    new_step2 = '<span data-i18n="aiHub.onlineStep2">Set Name to \'HAICHAIN\' and paste the copied Server URL from above into the URL field.</span>'
    if old_step2 in html:
        html = html.replace(old_step2, new_step2)
        print("Replaced old_step2 successfully.")

    # 3. Add updateAiHubUrls() in updateWalletBtnUI
    old_wallet_ui_tail = '      safeCreateIcons();\n    }'
    new_wallet_ui_tail = '''      safeCreateIcons();
      if (typeof updateAiHubUrls === 'function') {
        updateAiHubUrls();
      }
    }'''
    if old_wallet_ui_tail in html:
        html = html.replace(old_wallet_ui_tail, new_wallet_ui_tail, 1)
        print("Wired updateAiHubUrls into updateWalletBtnUI.")

    # 4. Replace copyOnlineMcpBtn logic and add updateAiHubUrls function
    old_copy_mcp_block = '''    // Copy Online MCP SSE URL
    if (copyOnlineMcpBtn) {
      copyOnlineMcpBtn.addEventListener('click', async () => {
        const url = "https://mcp.haichain.si/api/mcp";
        try {
          await navigator.clipboard.writeText(url);
          if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopied');
          showToast({ title: getDashNotice('copiedToastTitle'), message: getDashNotice('linkCopyToastMsg'), icon: 'check' });
          setTimeout(() => {
            if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopyBtn');
          }, 2500);
        } catch (_) {
          showToast({ title: "Remote MCP URL:", message: url, icon: "link" });
        }
      });
    }'''

    new_copy_mcp_block = '''    // Update AI Hub Dynamic Dedicated URLs (1-Click Personalized Vault)
    function updateAiHubUrls() {
      const codeSnippet = document.getElementById('online-mcp-url-snippet');
      const badgeEl = document.getElementById('online-mcp-badge');
      const connectedBox = document.getElementById('online-mcp-connected-box');
      const unconnectedBox = document.getElementById('online-mcp-unconnected-box');
      const boundAddrSpan = document.getElementById('online-mcp-bound-addr');

      const hasWallet = !!(userWallet && userWallet.address);
      const activeAddr = hasWallet ? String(userWallet.address).trim() : '';

      if (hasWallet && activeAddr) {
        const personalizedUrl = `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`;
        if (codeSnippet) codeSnippet.textContent = personalizedUrl;
        if (badgeEl) {
          badgeEl.className = "text-[9px] bg-emerald-950/80 border border-emerald-800/80 px-2 py-0.5 rounded-full text-emerald-400 font-mono shrink-0 whitespace-nowrap flex items-center space-x-1 font-semibold";
          const shortAddr = activeAddr.length > 10 ? `${activeAddr.slice(0, 4)}...${activeAddr.slice(-4)}` : activeAddr;
          const badgeText = window.haichainI18n ? window.haichainI18n.t('aiHub.badgeDedicated', '🔒 DEDICATED VAULT BOUND') : '🔒 DEDICATED VAULT BOUND';
          badgeEl.innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse shrink-0"></span><span>${badgeText} (${shortAddr})</span>`;
        }
        if (connectedBox) connectedBox.classList.remove('hidden');
        if (unconnectedBox) unconnectedBox.classList.add('hidden');
        if (boundAddrSpan) boundAddrSpan.textContent = activeAddr;
      } else {
        const genericUrl = "https://mcp.haichain.si/api/mcp";
        if (codeSnippet) codeSnippet.textContent = genericUrl;
        if (badgeEl) {
          badgeEl.className = "text-[9px] bg-amber-950/80 border border-amber-800/80 px-2 py-0.5 rounded-full text-amber-400 font-mono shrink-0 whitespace-nowrap flex items-center space-x-1";
          const genericText = window.haichainI18n ? window.haichainI18n.t('aiHub.badgeGeneric', '⚡ GENERIC URL (UNBOUND)') : '⚡ GENERIC URL (UNBOUND)';
          badgeEl.innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-amber-400 shrink-0"></span><span>${genericText}</span>`;
        }
        if (connectedBox) connectedBox.classList.add('hidden');
        if (unconnectedBox) unconnectedBox.classList.remove('hidden');
        if (boundAddrSpan) boundAddrSpan.textContent = '';
      }
      if (window.lucide && typeof window.safeCreateIcons === 'function') window.safeCreateIcons();
    }
    window.updateAiHubUrls = updateAiHubUrls;

    // Copy Online MCP SSE URL (Personalized when wallet connected)
    if (copyOnlineMcpBtn) {
      copyOnlineMcpBtn.addEventListener('click', async () => {
        const hasWallet = !!(userWallet && userWallet.address);
        const activeAddr = hasWallet ? String(userWallet.address).trim() : '';
        const url = hasWallet && activeAddr 
          ? `https://mcp.haichain.si/api/mcp?vault=${encodeURIComponent(activeAddr)}`
          : "https://mcp.haichain.si/api/mcp";

        try {
          await navigator.clipboard.writeText(url);
          if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopied');
          const toastMsg = hasWallet 
            ? (window.haichainI18n ? window.haichainI18n.t('aiHub.copiedPersonalizedToastMsg', 'Dedicated personalized MCP URL copied! Claude Mobile will automatically bind to your vault.') : 'Dedicated personalized MCP URL copied! Claude Mobile will automatically bind to your vault.')
            : (window.haichainI18n ? window.haichainI18n.t('aiHub.copiedGenericToastMsg', 'Generic MCP URL copied. Connect wallet to get dedicated URL.') : 'Generic MCP URL copied.');
          showToast({ title: getDashNotice('copiedToastTitle'), message: toastMsg, icon: 'check' });
          setTimeout(() => {
            if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopyBtn');
          }, 2500);
        } catch (_) {
          showToast({ title: "Remote MCP URL:", message: url, icon: "link" });
        }
      });
    }

    // Trigger wallet connection from Tab 2
    const onlineMcpTriggerConnectBtn = document.getElementById('online-mcp-trigger-connect-btn');
    if (onlineMcpTriggerConnectBtn) {
      onlineMcpTriggerConnectBtn.addEventListener('click', () => {
        if (typeof openWalletModal === 'function') {
          openWalletModal();
        } else if (walletConnectModal) {
          walletConnectModal.classList.remove('hidden');
        }
      });
    }'''

    if old_copy_mcp_block in html:
        html = html.replace(old_copy_mcp_block, new_copy_mcp_block)
        print("Replaced copyOnlineMcpBtn and added updateAiHubUrls.")
    else:
        print("WARNING: old_copy_mcp_block not found directly!")

    # 5. Also ensure openAiHubModal calls updateAiHubUrls()
    old_open_hub = '''    function openAiHubModal(targetTab = 'desktop') {
      if (aiHubModal) {
        aiHubModal.classList.remove('hidden');
        switchAiHubTab(targetTab);
        if (window.lucide) window.safeCreateIcons();
      }
    }'''

    new_open_hub = '''    function openAiHubModal(targetTab = 'desktop') {
      if (aiHubModal) {
        aiHubModal.classList.remove('hidden');
        if (typeof updateAiHubUrls === 'function') updateAiHubUrls();
        switchAiHubTab(targetTab);
        if (window.lucide) window.safeCreateIcons();
      }
    }'''

    if old_open_hub in html:
        html = html.replace(old_open_hub, new_open_hub)
        print("Updated openAiHubModal to call updateAiHubUrls.")

    # 6. Bump cache-buster of i18n.js
    cachebuster_pattern = r'src="/app/i18n\.js\?v=[^"]*"'
    new_cb = f'src="/app/i18n.js?v=v39_personalized_vault_mcp_{1793648000000}"'
    html = re.sub(cachebuster_pattern, new_cb, html)
    print("Bumped i18n.js cache-buster.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Completed patching {filepath} successfully.")

update_dashboard_file('dashboard.html')
update_dashboard_file('app/dashboard.html')
