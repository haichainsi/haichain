import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from generate_luxury_bw_modal import build_luxury_bw_modal

LUXURY_MODAL_HTML = build_luxury_bw_modal()

LUXURY_HEADER_BTN = '''<!-- Consolidated Unified AI Integration Hub Trigger (Premium Luxury Monochrome Pill) -->
        <button id="ai-hub-btn" type="button" class="haichain-ai-connect-btn px-2.5 sm:px-3.5 py-1.5 sm:py-2 rounded-full bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-[11px] sm:text-xs shadow-xs flex items-center space-x-1.5 sm:space-x-2 transition-all duration-200 active:scale-95 cursor-pointer shrink-0 border border-neutral-700/60 dark:border-neutral-300/60" title="Kết nối HAICHAIN với AI">
          <span class="relative flex h-1.5 w-1.5 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-neutral-400 dark:bg-neutral-600 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-1.5 w-1.5 bg-white dark:bg-black"></span>
          </span>
          <i data-lucide="bot" class="w-3.5 h-3.5 sm:w-4 sm:h-4 shrink-0 pointer-events-none"></i>
          <span class="font-semibold tracking-tight pointer-events-none whitespace-nowrap">Kết nối AI</span>
        </button>'''

LUXURY_OVERVIEW_BANNER = '''<!-- High-Impact AI Integration Banner (Premium Luxury Monochrome) -->
        <div class="p-3.5 sm:p-5 rounded-2xl sm:rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 sm:gap-4 relative overflow-hidden">
          <div class="flex items-center space-x-3 sm:space-x-4 min-w-0">
            <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-2xl bg-black text-white dark:bg-white dark:text-black flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="bot" class="w-5 h-5 sm:w-5.5 sm:h-5.5"></i>
            </div>
            <div class="min-w-0">
              <div class="flex items-center space-x-2">
                <h3 class="font-bold text-sm sm:text-base text-black dark:text-white truncate">Kết nối HAICHAIN với AI</h3>
                <span class="px-2 py-0.5 rounded-full text-[9px] font-mono font-semibold bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-300 border border-neutral-300 dark:border-neutral-800 shrink-0 uppercase tracking-wider">3 Lựa Chọn</span>
              </div>
              <p class="text-[11px] sm:text-xs text-neutral-500 mt-0.5 truncate">Claude Desktop (1-Click) &bull; Claude.ai Web &bull; Web3 Playground</p>
            </div>
          </div>
          <button type="button" onclick="document.getElementById('ai-hub-btn').click()" class="w-full sm:w-auto px-4 py-2 sm:py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-xs shadow-xs flex items-center justify-center space-x-2 shrink-0 transition-all active:scale-95 cursor-pointer">
            <i data-lucide="zap" class="w-3.5 h-3.5 fill-current"></i>
            <span>Kết Nối AI Ngay</span>
          </button>
        </div>'''

LUXURY_JS_BLOCK = '''// ================= UNIFIED AI INTEGRATION HUB (PREMIUM LUXURY MONOCHROME) =================
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
      const activeTabClass = "flex-1 py-2 sm:py-2.5 rounded-lg sm:rounded-xl bg-black text-white dark:bg-white dark:text-black shadow-xs text-center transition-all cursor-pointer font-bold flex items-center justify-center space-x-1 sm:space-x-1.5 text-[11px] sm:text-xs";
      const inactiveTabClass = "flex-1 py-2 sm:py-2.5 rounded-lg sm:rounded-xl text-neutral-500 hover:text-black dark:hover:text-white text-center transition-all cursor-pointer font-medium flex items-center justify-center space-x-1 sm:space-x-1.5 text-[11px] sm:text-xs";

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

def apply_luxury_bw(filepath):
    print(f"=== Applying Luxury Black & White to {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace header button
    btn_start = content.find('id="ai-hub-btn"')
    if btn_start != -1:
        tag_start = content.rfind('<button', 0, btn_start)
        tag_end = content.find('</button>', btn_start) + 9
        content = content[:tag_start] + LUXURY_HEADER_BTN + content[tag_end:]
        print("✓ Luxury Header button applied")
    else:
        print("! Header button not found")

    # 2. Replace Overview banner
    banner_start = content.find('<!-- High-Impact AI Integration Banner')
    if banner_start != -1:
        banner_end = content.find('</div>', content.find('</button>', banner_start)) + 6
        content = content[:banner_start] + LUXURY_OVERVIEW_BANNER + content[banner_end:]
        print("✓ Luxury Overview banner applied")
    else:
        print("! Overview banner not found")

    # 3. Replace Modal HTML
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
            content = content[:div_start] + LUXURY_MODAL_HTML + content[div_end:]
            print("✓ Luxury Modal HTML applied")
        else:
            print("! Could not find modal end div")
    else:
        print("! Modal id not found")

    # 4. Replace JS block
    js_marker_start = '// ================= UNIFIED AI INTEGRATION HUB'
    idx_js = content.find(js_marker_start)
    if idx_js != -1:
        idx_js_end = content.find('// ================= 8. ISSUE CAPABILITY TICKET MODAL', idx_js)
        if idx_js_end != -1:
            content = content[:idx_js] + LUXURY_JS_BLOCK + '\n\n    ' + content[idx_js_end:]
            print("✓ Luxury JS block applied")
        else:
            print("! Could not find end of JS block marker")
    else:
        print("! Could not find JS block start marker")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath} ({len(content)} bytes)\n")

for p in ['dashboard.html', 'app/dashboard.html']:
    apply_luxury_bw(p)
