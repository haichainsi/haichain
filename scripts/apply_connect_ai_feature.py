import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from generate_modal_html import build_new_ai_hub_modal

NEW_MODAL_HTML = build_new_ai_hub_modal()

NEW_HEADER_BTN = '''<!-- Consolidated Unified AI Integration Hub Trigger (High-Visibility AI Connect Pill) -->
        <button id="ai-hub-btn" type="button" class="haichain-ai-connect-btn px-2.5 sm:px-3.5 py-1.5 sm:py-2 rounded-full bg-gradient-to-r from-emerald-600 via-teal-600 to-emerald-500 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-[11px] sm:text-xs shadow-md shadow-emerald-500/25 flex items-center space-x-1.5 sm:space-x-2 transition-all duration-200 active:scale-95 cursor-pointer shrink-0 border border-emerald-400/30" title="Kết nối HAICHAIN với AI (Claude Desktop, Web & Cursor)">
          <span class="relative flex h-2 w-2 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-white"></span>
          </span>
          <i data-lucide="bot" class="w-3.5 h-3.5 sm:w-4 sm:h-4 shrink-0 pointer-events-none"></i>
          <span class="font-bold tracking-tight pointer-events-none whitespace-nowrap">Kết nối AI</span>
        </button>'''

NEW_OVERVIEW_BANNER = '''<!-- High-Impact AI Integration Banner -->
        <div class="p-3.5 sm:p-5 rounded-2xl sm:rounded-3xl border border-emerald-500/30 bg-gradient-to-r from-emerald-500/10 via-teal-500/5 to-transparent dark:from-emerald-950/30 dark:via-teal-950/15 dark:to-black/50 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 sm:gap-4 relative overflow-hidden">
          <div class="flex items-center space-x-3 sm:space-x-4 min-w-0">
            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-2xl bg-gradient-to-tr from-emerald-600 to-teal-500 text-white flex items-center justify-center shrink-0 shadow-md shadow-emerald-500/25">
              <i data-lucide="bot" class="w-5 h-5 sm:w-6 sm:h-6"></i>
            </div>
            <div class="min-w-0">
              <div class="flex items-center space-x-2">
                <h3 class="font-bold text-sm sm:text-base text-black dark:text-white truncate">Kết nối HAICHAIN với AI</h3>
                <span class="px-2 py-0.5 rounded-full text-[9.5px] font-mono font-bold bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30 shrink-0">3 Lựa Chọn</span>
              </div>
              <p class="text-[11px] sm:text-xs text-neutral-500 dark:text-neutral-400 mt-0.5 truncate">Claude Desktop (1-Click) &bull; Claude.ai Web &bull; Web3 Playground</p>
            </div>
          </div>
          <button type="button" onclick="document.getElementById('ai-hub-btn').click()" class="w-full sm:w-auto px-4 py-2 sm:py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-bold text-xs shadow-sm flex items-center justify-center space-x-2 shrink-0 transition-all active:scale-95 cursor-pointer">
            <i data-lucide="zap" class="w-3.5 h-3.5 fill-current"></i>
            <span>Kết Nối AI Ngay</span>
          </button>
        </div>
'''

NEW_JS_BLOCK = '''// ================= UNIFIED AI INTEGRATION HUB (3 WAYS: DESKTOP, ONLINE, WEB) =================
    const aiHubBtn = document.getElementById('ai-hub-btn');
    const aiHubModal = document.getElementById('ai-hub-modal');
    const closeAiHubModal = document.getElementById('close-ai-hub-modal');
    const hubTabDesktop = document.getElementById('hub-tab-desktop');
    const hubTabOnline = document.getElementById('hub-tab-online');
    const hubTabWeb = document.getElementById('hub-tab-web');
    const hubSectionDesktop = document.getElementById('hub-section-desktop');
    const hubSectionOnline = document.getElementById('hub-section-online');
    const hubSectionWeb = document.getElementById('hub-section-web');

    // 1-Click Copy Buttons
    const copyDesktopInstallBtn = document.getElementById('copy-desktop-install-btn');
    const copyDesktopInstallText = document.getElementById('copy-desktop-install-text');
    const copyOnlineMcpBtn = document.getElementById('copy-online-mcp-btn');
    const copyOnlineMcpText = document.getElementById('copy-online-mcp-text');
    const btnOpenWebPlayground = document.getElementById('btn-open-web-playground');

    function switchAiHubTab(tabName) {
      const activeTabClass = "flex-1 py-2 sm:py-2.5 rounded-lg sm:rounded-xl bg-white dark:bg-neutral-800 text-black dark:text-white shadow-xs text-center transition-all cursor-pointer font-bold flex items-center justify-center space-x-1 sm:space-x-1.5 text-[11px] sm:text-xs";
      const inactiveTabClass = "flex-1 py-2 sm:py-2.5 rounded-lg sm:rounded-xl text-neutral-500 hover:text-black dark:hover:text-white text-center transition-all cursor-pointer font-bold flex items-center justify-center space-x-1 sm:space-x-1.5 text-[11px] sm:text-xs";

      // Map legacy tab names if any
      if (tabName === 'gateway' || tabName === 'mcp') tabName = 'desktop';
      if (tabName === 'stats') tabName = 'web';

      if (tabName === 'desktop') {
        if (hubTabDesktop) hubTabDesktop.className = activeTabClass;
        if (hubTabOnline) hubTabOnline.className = inactiveTabClass;
        if (hubTabWeb) hubTabWeb.className = inactiveTabClass;
        if (hubSectionDesktop) hubSectionDesktop.classList.remove('hidden');
        if (hubSectionOnline) hubSectionOnline.classList.add('hidden');
        if (hubSectionWeb) hubSectionWeb.classList.add('hidden');
      } else if (tabName === 'online') {
        if (hubTabDesktop) hubTabDesktop.className = inactiveTabClass;
        if (hubTabOnline) hubTabOnline.className = activeTabClass;
        if (hubTabWeb) hubTabWeb.className = inactiveTabClass;
        if (hubSectionDesktop) hubSectionDesktop.classList.add('hidden');
        if (hubSectionOnline) hubSectionOnline.classList.remove('hidden');
        if (hubSectionWeb) hubSectionWeb.classList.add('hidden');
      } else if (tabName === 'web') {
        if (hubTabDesktop) hubTabDesktop.className = inactiveTabClass;
        if (hubTabOnline) hubTabOnline.className = inactiveTabClass;
        if (hubTabWeb) hubTabWeb.className = activeTabClass;
        if (hubSectionDesktop) hubSectionDesktop.classList.add('hidden');
        if (hubSectionOnline) hubSectionOnline.classList.add('hidden');
        if (hubSectionWeb) hubSectionWeb.classList.remove('hidden');
      }
      if (window.lucide) window.safeCreateIcons();
    }

    function openAiHubModal(targetTab = 'desktop') {
      if (aiHubModal) {
        aiHubModal.classList.remove('hidden');
        switchAiHubTab(targetTab);
        if (window.lucide) window.safeCreateIcons();
      }
    }

    if (aiHubBtn) aiHubBtn.addEventListener('click', () => openAiHubModal('desktop'));
    if (closeAiHubModal) closeAiHubModal.addEventListener('click', () => aiHubModal.classList.add('hidden'));

    if (aiHubModal) {
      aiHubModal.addEventListener('click', (e) => {
        if (e.target === aiHubModal) aiHubModal.classList.add('hidden');
      });
    }

    if (hubTabDesktop) hubTabDesktop.addEventListener('click', () => switchAiHubTab('desktop'));
    if (hubTabOnline) hubTabOnline.addEventListener('click', () => switchAiHubTab('online'));
    if (hubTabWeb) hubTabWeb.addEventListener('click', () => switchAiHubTab('web'));

    // Copy Desktop Command
    if (copyDesktopInstallBtn) {
      copyDesktopInstallBtn.addEventListener('click', async () => {
        const cmd = "npx -y @haichainsi/mcp-server --install";
        try {
          await navigator.clipboard.writeText(cmd);
          if (copyDesktopInstallText) copyDesktopInstallText.textContent = "✓ Đã sao chép lệnh!";
          showToast({ title: "Đã sao chép!", message: "Dán vào Terminal/PowerShell để cài đặt tự động", icon: "check" });
          setTimeout(() => {
            if (copyDesktopInstallText) copyDesktopInstallText.textContent = "Sao chép lệnh cài đặt 1-Click";
          }, 2500);
        } catch (_) {
          showToast({ title: "Lệnh cài đặt:", message: cmd, icon: "terminal" });
        }
      });
    }

    // Copy Online MCP SSE URL
    if (copyOnlineMcpBtn) {
      copyOnlineMcpBtn.addEventListener('click', async () => {
        const url = "https://mcp.haichain.si/sse";
        try {
          await navigator.clipboard.writeText(url);
          if (copyOnlineMcpText) copyOnlineMcpText.textContent = "✓ Đã sao chép link!";
          showToast({ title: "Đã sao chép!", message: "Dán vào Settings -> Connectors trên claude.ai", icon: "check" });
          setTimeout(() => {
            if (copyOnlineMcpText) copyOnlineMcpText.textContent = "Sao chép đường dẫn Remote MCP";
          }, 2500);
        } catch (_) {
          showToast({ title: "Remote MCP URL:", message: url, icon: "link" });
        }
      });
    }

    // Direct Web Playground CTA
    if (btnOpenWebPlayground) {
      btnOpenWebPlayground.addEventListener('click', () => {
        if (aiHubModal) aiHubModal.classList.add('hidden');
        // Switch to tab-playground
        const navPlayground = document.querySelector('[data-tab="tab-playground"]');
        if (navPlayground) {
          navPlayground.click();
        } else {
          document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
          const pg = document.getElementById('tab-playground');
          if (pg) pg.classList.remove('hidden');
        }
        // Smooth scroll to playground area
        setTimeout(() => {
          const promptInput = document.getElementById('prompt-input');
          if (promptInput) {
            promptInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
            promptInput.focus();
          }
        }, 150);
        showToast({ title: "AI Playground", message: "Trải nghiệm suy luận AI trực tiếp qua Web3", icon: "zap" });
      });
    }

    // Backward-compatible triggers for legacy buttons
    const legacyClaudeBtn = document.getElementById('claude-mcp-btn');
    if (legacyClaudeBtn) legacyClaudeBtn.addEventListener('click', () => openAiHubModal('desktop'));
    const legacyGatewayBtn = document.getElementById('ai-gateway-btn');
    if (legacyGatewayBtn) legacyGatewayBtn.addEventListener('click', () => openAiHubModal('desktop'));
'''

def patch_file(filepath):
    print(f"--- Patching {filepath} ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace header button
    btn_regex = r'<!-- Consolidated Unified AI Integration Hub Trigger -->\s*<button id="ai-hub-btn"[\s\S]*?</button>'
    if re.search(btn_regex, content):
        content = re.sub(btn_regex, NEW_HEADER_BTN, content)
        print("✓ Header button replaced successfully")
    else:
        print("! Could not find header button regex, checking alternative")
        # Check if already patched or find button directly
        if 'haichain-ai-connect-btn' in content:
            print("✓ Header button already has new class")
        else:
            # Simple replacement
            idx1 = content.find('id="ai-hub-btn"')
            btn_start = content.rfind('<button', 0, idx1)
            btn_end = content.find('</button>', idx1) + 9
            content = content[:btn_start] + NEW_HEADER_BTN + content[btn_end:]
            print("✓ Header button replaced via index slice")

    # 2. Add Overview Banner inside tab-overview (if not present)
    if 'Kết nối HAICHAIN với AI của bạn' not in content and 'Kết nối HAICHAIN với AI' not in content:
        overview_marker = '<section id="tab-overview" class="tab-content space-y-6">'
        if overview_marker in content:
            content = content.replace(overview_marker, overview_marker + '\n\n        ' + NEW_OVERVIEW_BANNER)
            print("✓ Overview Banner added successfully")
        else:
            print("! Overview marker not found")
    else:
        print("✓ Overview Banner already present or accounted for")

    # 3. Replace the Modal HTML
    modal_start = content.find('id="ai-hub-modal"')
    if modal_start != -1:
        div_start = content.rfind('<div', 0, modal_start)
        # Find closing of this modal
        depth = 0
        div_end = -1
        for i in range(div_start, len(content)):
            if content[i:i+4] == '<div':
                depth += 1
            elif content[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    div_end = i + 6
                    break
        if div_end != -1:
            content = content[:div_start] + NEW_MODAL_HTML + content[div_end:]
            print("✓ Modal HTML replaced successfully")
        else:
            print("! Could not find modal end div")
    else:
        print("! Modal id not found")

    # 4. Replace the JS block
    js_marker_start = '// ================= UNIFIED AI INTEGRATION HUB'
    idx_js = content.find(js_marker_start)
    if idx_js != -1:
        idx_js_end = content.find('// ================= 8. ISSUE CAPABILITY TICKET MODAL', idx_js)
        if idx_js_end != -1:
            content = content[:idx_js] + NEW_JS_BLOCK + '\n\n    ' + content[idx_js_end:]
            print("✓ JS block replaced successfully")
        else:
            print("! Could not find end of JS block marker")
    else:
        print("! Could not find JS block start marker")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath} (new size: {len(content)} bytes)")

for p in ['dashboard.html', 'app/dashboard.html']:
    patch_file(p)
