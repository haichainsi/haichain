import sys, re
sys.stdout.reconfigure(encoding='utf-8')

targets = ['dashboard.html', 'app/dashboard.html']

for fpath in targets:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update initial HTML for header-panic-btn
    old_html = """        <!-- Emergency Panic Button -->
        <button id="header-panic-btn" type="button" class="haichain-action-btn has-label text-neutral-700 dark:text-neutral-300 hover:text-red-600 dark:hover:text-red-400" title="Emergency Stop">
          <i data-lucide="alert-octagon" class="w-3.5 h-3.5 shrink-0 pointer-events-none"></i>
          <span class="hidden md:inline text-xs font-semibold" data-i18n="btn.panicStop">Emergency Stop</span>
          <span class="hidden sm:inline md:hidden text-[10px] font-bold uppercase" data-i18n="btn.panicStopMobile">Panic</span>
        </button>"""

    new_html = """        <!-- Emergency Panic Button (Clean Icon-Only on Mobile, Label on Desktop) -->
        <button id="header-panic-btn" type="button" class="haichain-action-btn has-label text-neutral-700 dark:text-neutral-300 hover:text-red-600 dark:hover:text-red-400" title="Emergency Stop" aria-label="Emergency Stop">
          <i data-lucide="alert-octagon" class="w-3.5 h-3.5 sm:w-4 sm:h-4 shrink-0 pointer-events-none"></i>
          <span class="hidden md:inline text-xs font-semibold ml-1.5" data-i18n="btn.panicStop">Emergency Stop</span>
        </button>"""

    if old_html in content:
        content = content.replace(old_html, new_html)
        print(f"[{fpath}] Replaced initial panic button HTML")
    else:
        print(f"[{fpath}] Warning: old_html not found")

    # 2. Update JavaScript in Block 1 & Block 2
    # Replace normal state innerHTML
    old_js_normal = 'headerPanicBtn.innerHTML = `<i data-lucide="alert-octagon" class="w-3.5 h-3.5"></i><span class="hidden sm:inline" data-i18n="btn.panicStop">${window.haichainI18n ? window.haichainI18n.t(\'btn.panicStop\') : \'Emergency Stop\'}</span><span class="sm:hidden" data-i18n="btn.panicStopMobile">${window.haichainI18n ? window.haichainI18n.t(\'btn.panicStopMobile\') : \'Panic\'}</span>`;'
    new_js_normal = 'headerPanicBtn.innerHTML = `<i data-lucide="alert-octagon" class="w-3.5 h-3.5 sm:w-4 sm:h-4 shrink-0 pointer-events-none"></i><span class="hidden md:inline text-xs font-semibold ml-1.5" data-i18n="btn.panicStop">${window.haichainI18n ? window.haichainI18n.t(\'btn.panicStop\') : \'Emergency Stop\'}</span>`; headerPanicBtn.setAttribute(\'title\', window.haichainI18n ? window.haichainI18n.t(\'btn.panicStop\') : \'Emergency Stop\');'

    if old_js_normal in content:
        content = content.replace(old_js_normal, new_js_normal)
        print(f"[{fpath}] Replaced normal JS innerHTML")
    else:
        # Regex replacement if needed
        content = re.sub(
            r'headerPanicBtn\.innerHTML\s*=\s*`<i data-lucide="alert-octagon"[^`]*`;',
            new_js_normal,
            content
        )
        print(f"[{fpath}] Replaced normal JS innerHTML via regex")

    # Replace panic / frozen state innerHTML
    old_js_panic = 'headerPanicBtn.innerHTML = `<i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i><span data-i18n="btn.panicReset">${window.haichainI18n ? window.haichainI18n.t(\'btn.panicReset\') : \'Reset Vault\'}</span>`;'
    new_js_panic = 'headerPanicBtn.innerHTML = `<i data-lucide="rotate-ccw" class="w-3.5 h-3.5 sm:w-4 sm:h-4 shrink-0 pointer-events-none text-amber-500 animate-spin-slow"></i><span class="hidden md:inline text-xs font-semibold ml-1.5 text-amber-500" data-i18n="btn.panicReset">${window.haichainI18n ? window.haichainI18n.t(\'btn.panicReset\') : \'Reset Vault\'}</span>`; headerPanicBtn.setAttribute(\'title\', window.haichainI18n ? window.haichainI18n.t(\'btn.panicReset\') : \'Reset Vault\');'

    if old_js_panic in content:
        content = content.replace(old_js_panic, new_js_panic)
        print(f"[{fpath}] Replaced panic JS innerHTML")
    else:
        content = re.sub(
            r'headerPanicBtn\.innerHTML\s*=\s*`<i data-lucide="refresh-cw"[^`]*`;',
            new_js_panic,
            content
        )
        print(f"[{fpath}] Replaced panic JS innerHTML via regex")

    # 3. Add CSS fail-safe: hide ALL spans inside .haichain-action-btn on screens under 768px (mobile)
    old_css_media = """    @media (min-width: 640px) {
      .haichain-action-btn.has-label {
        width: auto !important;
        height: auto !important;
        padding: 6px 10px !important;
        gap: 6px !important;
      }
    }"""

    new_css_media = """    @media (max-width: 767px) {
      .haichain-action-btn span,
      #header-panic-btn span,
      #ai-hub-btn span {
        display: none !important;
      }
      .haichain-action-btn {
        width: 28px !important;
        height: 28px !important;
        min-width: 28px !important;
        padding: 0 !important;
        border-radius: 9999px !important;
        overflow: hidden !important;
      }
    }
    @media (min-width: 768px) {
      .haichain-action-btn.has-label {
        width: auto !important;
        height: auto !important;
        padding: 6px 10px !important;
        gap: 6px !important;
      }
    }"""

    if old_css_media in content:
        content = content.replace(old_css_media, new_css_media)
        print(f"[{fpath}] Updated CSS media query for action buttons")
    else:
        print(f"[{fpath}] Warning: old_css_media not found")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Patch complete.")
