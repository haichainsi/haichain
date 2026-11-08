import re
import time

timestamp = int(time.time() * 1000)
new_cachebuster = f"v43_mobile_header_viewport_lock_{timestamp}"

# 1. Update sale-controller.js
for path in ['sale-controller.js', 'app/sale-controller.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # A. Input font-size & styling to prevent mobile zoom
    old_input = 'id="vip-gatekeeper-input" placeholder="${getI18nText(\'accessPlaceholder\')}" class="w-full px-4 py-3.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white placeholder-neutral-400 text-xs sm:text-sm font-mono focus:outline-hidden focus:border-black dark:focus:border-white transition-all text-center tracking-wider font-semibold"'
    new_input = 'id="vip-gatekeeper-input" placeholder="${getI18nText(\'accessPlaceholder\')}" class="w-full px-4 py-3.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white placeholder-neutral-400 text-base sm:text-sm font-mono focus:outline-hidden focus:border-black dark:focus:border-white transition-all text-center tracking-wider font-semibold" style="font-size: 16px !important;"'
    if old_input in content:
        content = content.replace(old_input, new_input)
        print(f"[OK] Replaced vip input font-size in {path}")
    else:
        print(f"[WARN] Old input pattern not found in {path}")

    # B. attemptGateUnlock keyboard blur & scroll reset
    old_unlock = '''      function attemptGateUnlock() {
        if (!gateInput) return;
        const val = (gateInput.value || '').toLowerCase().trim();
        if (config.ACCESS_KEYS.includes(val)) {
          try {
            localStorage.setItem('haichain_vip_access', val);
          } catch (_) {}
          injectNavigationTabs(true);
          renderTerminalContent(container, true);
        } else {'''

    new_unlock = '''      function attemptGateUnlock() {
        if (!gateInput) return;
        const val = (gateInput.value || '').toLowerCase().trim();
        if (config.ACCESS_KEYS.includes(val)) {
          try {
            localStorage.setItem('haichain_vip_access', val);
          } catch (_) {}

          // 1. Force blur active element and input to immediately collapse mobile virtual keyboard
          if (document.activeElement && typeof document.activeElement.blur === 'function') {
            document.activeElement.blur();
          }
          gateInput.blur();

          // 2. Immediate scroll reset to ensure header remains pinned cleanly at top
          window.scrollTo(0, 0);
          document.documentElement.scrollTop = 0;
          document.body.scrollTop = 0;
          const mainCanvas = document.querySelector('main');
          if (mainCanvas) mainCanvas.scrollTop = 0;

          // 3. Render authenticated VIP terminal
          injectNavigationTabs(true);
          renderTerminalContent(container, true);

          // 4. Multi-frame scroll enforcement as mobile virtual keyboard collapses
          const resetScroll = () => {
            window.scrollTo(0, 0);
            document.documentElement.scrollTop = 0;
            document.body.scrollTop = 0;
            if (mainCanvas) mainCanvas.scrollTop = 0;
          };
          requestAnimationFrame(resetScroll);
          setTimeout(resetScroll, 50);
          setTimeout(resetScroll, 150);
          setTimeout(resetScroll, 350);
        } else {'''

    if old_unlock in content:
        content = content.replace(old_unlock, new_unlock)
        print(f"[OK] Replaced attemptGateUnlock in {path}")
    else:
        print(f"[WARN] Old attemptGateUnlock pattern not found in {path}")

    # C. renderTerminalContent top scroll reset
    old_render_term = '''    let userAllocation = null;
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
    } catch (_) {}

    container.innerHTML = `'''

    new_render_term = '''    let userAllocation = null;
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
    } catch (_) {}

    // Ensure clean viewport alignment on terminal render
    window.scrollTo(0, 0);
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
    const mainCanvas = document.querySelector('main');
    if (mainCanvas) mainCanvas.scrollTop = 0;

    container.innerHTML = `'''

    if old_render_term in content:
        content = content.replace(old_render_term, new_render_term)
        print(f"[OK] Replaced renderTerminalContent scroll reset in {path}")
    else:
        print(f"[WARN] Old renderTerminalContent pattern not found in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update dashboard.html and app/dashboard.html
for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # A. Viewport meta tag
    old_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    new_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">'
    if old_viewport in content:
        content = content.replace(old_viewport, new_viewport)
        print(f"[OK] Updated viewport meta in {path}")

    # B. CSS Mobile Viewport Lock
    old_css_anchor = '/* ==========================================================================\n       IMMUTABLE TOP HEADER & MOBILE CONTROLS ARCHITECTURE (PERMANENT LOCK)\n       ========================================================================== */'
    new_css_block = '''/* Global Viewport & Mobile Scroll Lock (Guarantees Header Never Scrolls or Clips on Mobile) */
    html {
      height: 100% !important;
      height: 100dvh !important;
      overflow: hidden !important;
    }
    body {
      height: 100% !important;
      height: 100dvh !important;
      max-height: 100dvh !important;
      overflow: hidden !important;
      width: 100% !important;
    }
    @media (max-width: 767.98px) {
      html, body {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        width: 100% !important;
        height: 100% !important;
        height: 100dvh !important;
        max-height: 100dvh !important;
        overflow: hidden !important;
      }
    }

    /* ==========================================================================
       IMMUTABLE TOP HEADER & MOBILE CONTROLS ARCHITECTURE (PERMANENT LOCK)
       ========================================================================== */'''

    if old_css_anchor in content:
        content = content.replace(old_css_anchor, new_css_block)
        print(f"[OK] Added viewport CSS lock in {path}")
    else:
        print(f"[WARN] Old CSS anchor not found in {path}")

    # C. Main wrapper div: h-screen -> h-full h-[100dvh] max-h-[100dvh]
    old_wrapper = '<div class="flex-1 flex flex-col h-screen overflow-hidden">'
    new_wrapper = '<div class="flex-1 flex flex-col h-full h-[100dvh] max-h-[100dvh] overflow-hidden">'
    if old_wrapper in content:
        content = content.replace(old_wrapper, new_wrapper)
        print(f"[OK] Updated wrapper div in {path}")

    # D. switchTab scroll reset & blur
    old_switch = '''    function switchTab(targetTab) {
      if (!targetTab) return;
      try {
        if (targetTab === \'tab-vesting\' && typeof renderVestingVaultPage === \'function\') {
          renderVestingVaultPage();
        }
        if (targetTab === \'tab-preseed\' && typeof window.renderPreseedSalePage === \'function\') {
          window.renderPreseedSalePage();
        }
      } catch (err) {
        console.warn(\'Tab preload warning:\', err);
      }'''

    new_switch = '''    function switchTab(targetTab) {
      if (!targetTab) return;
      if (document.activeElement && typeof document.activeElement.blur === 'function') {
        document.activeElement.blur();
      }
      window.scrollTo(0, 0);
      document.documentElement.scrollTop = 0;
      document.body.scrollTop = 0;
      try {
        if (targetTab === \'tab-vesting\' && typeof renderVestingVaultPage === \'function\') {
          renderVestingVaultPage();
        }
        if (targetTab === \'tab-preseed\' && typeof window.renderPreseedSalePage === \'function\') {
          window.renderPreseedSalePage();
        }
      } catch (err) {
        console.warn(\'Tab preload warning:\', err);
      }'''

    if old_switch in content:
        content = content.replace(old_switch, new_switch)
        print(f"[OK] Updated switchTab in {path}")

    # E. Update cachebuster for sale-controller.js
    content = re.sub(r'sale-controller\.js\?v=[^"\'\s]+', f'sale-controller.js?v={new_cachebuster}', content)
    print(f"[OK] Updated sale-controller cachebuster to {new_cachebuster} in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("[COMPLETE] All files updated and synchronized successfully.")
