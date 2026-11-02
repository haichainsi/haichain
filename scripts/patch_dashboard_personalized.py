import os

def patch_dashboard(fp):
    if not os.path.exists(fp):
        return False
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the HTML snippet to include the personalized badge
    old_html = """          <div class="flex items-center justify-between text-xs">
            <span class="text-neutral-500 font-mono" data-i18n="aiHub.onlineUrlLabel">MCP Server URL (for Claude Mobile):</span>
            <span class="text-[10px] border border-emerald-800/80 px-2 py-0.5 rounded-full text-emerald-400 font-mono shrink-0 whitespace-nowrap">Streamable HTTP / SSL</span>
          </div>
          <div class="p-2.5 rounded-xl bg-black border border-neutral-800 font-mono text-emerald-400 text-xs sm:text-[13px] overflow-x-auto select-all break-all flex items-center justify-between">
            <code id="online-mcp-url-snippet">https://mcp.haichain.si/api/mcp</code>
          </div>"""

    new_html = """          <div class="flex items-center justify-between text-xs">
            <span class="text-neutral-500 font-mono flex items-center space-x-1.5">
              <span data-i18n="aiHub.onlineUrlLabel">MCP Server URL:</span>
              <span id="personalized-mcp-badge" class="px-2 py-0.5 rounded-full text-[9px] font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">✨ 1-CLICK DEDICATED VAULT</span>
            </span>
            <span class="text-[10px] border border-emerald-800/80 px-2 py-0.5 rounded-full text-emerald-400 font-mono shrink-0 whitespace-nowrap">Streamable HTTP / SSL</span>
          </div>
          <div class="p-2.5 rounded-xl bg-black border border-neutral-800 font-mono text-emerald-400 text-xs sm:text-[13px] overflow-x-auto select-all break-all flex items-center justify-between">
            <code id="online-mcp-url-snippet">https://mcp.haichain.si/api/mcp</code>
          </div>"""

    if old_html in content:
        content = content.replace(old_html, new_html)

    # 2. Update JavaScript to dynamically calculate and copy personalized URL
    old_js = """    // Copy Online MCP SSE URL
    if (copyOnlineMcpBtn) {
      copyOnlineMcpBtn.addEventListener('click', async () => {
        const url = "https://mcp.haichain.si/api/mcp";
        try {
          await navigator.clipboard.writeText(url);
          if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopied');
          showToast({ title: getDashNotice('copiedToastTitle'), message: getDashNotice('linkCopyToastMsg'), icon: 'check' });
          setTimeout(() => {
            if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopyBtn');
          }, 2000);
        } catch (_) {
          showToast({ title: getDashNotice('copiedToastTitle'), message: url, icon: 'copy' });
        }
      });
    }"""

    new_js = """    // Helper: compute personalized 1-click dedicated MCP URL
    function getPersonalizedMcpUrl() {
      const addr = (userWallet && userWallet.address) 
                 ? userWallet.address 
                 : (localStorage.getItem('haichain_active_wallet') || 'CsFDFFED6nwNotjLEt4V52yZQqd2dFEKj4hedAtdDQEw');
      return addr ? `https://mcp.haichain.si/api/mcp?vault=${addr}` : 'https://mcp.haichain.si/api/mcp';
    }

    function updatePersonalizedMcpUI() {
      const url = getPersonalizedMcpUrl();
      const snippet = document.getElementById('online-mcp-url-snippet');
      const badge = document.getElementById('personalized-mcp-badge');
      if (snippet) snippet.textContent = url;
      if (badge) {
        const addr = (userWallet && userWallet.address) || localStorage.getItem('haichain_active_wallet') || 'CsFDFFED6nwNotjLEt4V52yZQqd2dFEKj4hedAtdDQEw';
        badge.textContent = `✨ DEDICATED: ${addr.slice(0, 4)}...${addr.slice(-4)}`;
      }
    }

    // Copy Online MCP SSE URL (Personalized 1-Click Vault)
    if (copyOnlineMcpBtn) {
      copyOnlineMcpBtn.addEventListener('click', async () => {
        const url = getPersonalizedMcpUrl();
        try {
          await navigator.clipboard.writeText(url);
          if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopied');
          showToast({ 
            title: "✓ 1-Click Dedicated MCP Link Copied!", 
            message: "Đã sao chép link MCP cá nhân hóa! Dán vào Claude để AI tự động nhận diện ví của bạn trọn đời.", 
            icon: 'check' 
          });
          setTimeout(() => {
            if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopyBtn');
          }, 2500);
        } catch (_) {
          showToast({ title: getDashNotice('copiedToastTitle'), message: url, icon: 'copy' });
        }
      });
    }"""

    if old_js in content:
        content = content.replace(old_js, new_js)

    # 3. Call updatePersonalizedMcpUI in switchAiHubTab
    old_switch = "if (tabName === 'online' || tabName === 'tab2' || tabName === 'claude-mobile') {"
    new_switch = "if (tabName === 'online' || tabName === 'tab2' || tabName === 'claude-mobile') {\n        updatePersonalizedMcpUI();"

    if old_switch in content and "updatePersonalizedMcpUI();" not in content:
        content = content.replace(old_switch, new_switch)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched:", fp)
    return True

patch_dashboard('dashboard.html')
patch_dashboard('app/dashboard.html')
