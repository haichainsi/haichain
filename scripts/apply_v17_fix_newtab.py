import json
import re

# 1. Update pdf-modal.js and app/pdf-modal.js
for path in ['pdf-modal.js', 'app/pdf-modal.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where initPdfTriggers begins
    idx = content.find('  // Auto-bind triggers across the app')
    if idx == -1:
        print(f"ERROR: trigger comment not found in {path}")
        continue

    new_trigger_code = """  // Universal In-App Whitepaper Click Handler (100% Prevents Opening in New Tab)
  function handleWhitepaperClick(e, trigger) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }

    // Close mobile nav menu if open
    if (typeof window.closeMobileMenu === 'function') {
      try { window.closeMobileMenu(); } catch (_) {}
    }
    const mobMenu = document.getElementById('mobile-menu');
    if (mobMenu) {
      mobMenu.classList.remove('menu-open', 'opacity-100');
      mobMenu.classList.add('hidden', 'opacity-0');
    }

    const explicitHref = trigger ? (trigger.getAttribute('data-pdf-url') || trigger.getAttribute('href')) : '';
    if (explicitHref && explicitHref.endsWith('.pdf') && !explicitHref.includes('whitepaper') && !explicitHref.includes('WHITEPAPER')) {
      window.openPdfViewerModal(explicitHref, trigger.getAttribute('title') || 'HAICHAIN Document');
      return;
    }

    const lang = getCurrentLang();
    const pdfUrl = getWhitepaperUrlForLang(lang);
    const meta = getI18nMeta(lang);
    window.openPdfViewerModal(pdfUrl, meta.title);
  }

  // 1. Capture-phase Global Listener: Catches ANY click on any whitepaper link immediately
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest(
      '#nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link, [data-open-whitepaper], [data-pdf-whitepaper], a[href*="whitepaper"], a[href*="WHITEPAPER"]'
    );
    if (trigger) {
      handleWhitepaperClick(e, trigger);
    }
  }, true);

  // 2. Direct Element Binding & Prewarming
  function initPdfTriggers() {
    const selector = '#nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link, [data-open-whitepaper], [data-pdf-whitepaper], a[href*="whitepaper"], a[href*="WHITEPAPER"]';
    document.querySelectorAll(selector).forEach((btn) => {
      if (btn.dataset.pdfBound === 'true') return;
      btn.dataset.pdfBound = 'true';
      btn.addEventListener('click', (e) => handleWhitepaperClick(e, btn));
    });

    checkAutoOpen();

    // Idle background pre-warming: parse Whitepaper so opening takes <10ms
    if (typeof requestIdleCallback === 'function') {
      requestIdleCallback(() => {
        const lang = getCurrentLang();
        prewarmDocument(getWhitepaperUrlForLang(lang));
      }, { timeout: 3000 });
    } else {
      setTimeout(() => {
        const lang = getCurrentLang();
        prewarmDocument(getWhitepaperUrlForLang(lang));
      }, 1500);
    }
  }

  // Auto-open modal if URL specifies ?open_whitepaper=1 or pathname is /whitepaper
  function checkAutoOpen() {
    try {
      const params = new URLSearchParams(window.location.search);
      if (params.get('open_whitepaper') === '1' || window.location.pathname === '/whitepaper') {
        const lang = getCurrentLang();
        const pdfUrl = getWhitepaperUrlForLang(lang);
        const meta = getI18nMeta(lang);
        window.openPdfViewerModal(pdfUrl, meta.title);
      }
    } catch (_) {}
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPdfTriggers);
  } else {
    initPdfTriggers();
  }

  window.addEventListener('haichain-language-changed', () => {
    setTimeout(initPdfTriggers, 50);
  });
})();
"""

    updated_content = content[:idx] + new_trigger_code
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated {path}")

# 2. Update index.html and app/index.html to use explicit inline onclick and href='javascript:void(0)'
for path in ['index.html', 'app/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop nav
    content = re.sub(
        r'<a\s+href="/whitepaper"\s+class="([^"]*)"\s+id="nav-whitepaper-link"[^>]*>',
        r'<a href="javascript:void(0)" onclick="event.preventDefault(); window.openPdfViewerModal && window.openPdfViewerModal(\'/HAICHAIN_WHITEPAPER_V1.0_\' + ((window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem(\'haichain_lang\') || \'en\')).toUpperCase() + \'.pdf\');" class="\1" id="nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">',
        content
    )

    # Mobile nav
    content = re.sub(
        r'<a\s+href="/whitepaper"\s+class="([^"]*)"\s+id="mobile-nav-whitepaper-link"[^>]*>',
        r'<a href="javascript:void(0)" onclick="event.preventDefault(); if (typeof closeMobileMenu === \'function\') closeMobileMenu(); window.openPdfViewerModal && window.openPdfViewerModal(\'/HAICHAIN_WHITEPAPER_V1.0_\' + ((window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem(\'haichain_lang\') || \'en\')).toUpperCase() + \'.pdf\');" class="\1" id="mobile-nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">',
        content
    )

    # Footer
    content = re.sub(
        r'<a\s+href="/whitepaper"\s+class="([^"]*)"\s+id="footer-whitepaper-link"[^>]*>',
        r'<a href="javascript:void(0)" onclick="event.preventDefault(); window.openPdfViewerModal && window.openPdfViewerModal(\'/HAICHAIN_WHITEPAPER_V1.0_\' + ((window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem(\'haichain_lang\') || \'en\')).toUpperCase() + \'.pdf\');" class="\1" id="footer-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">',
        content
    )

    # Update cache-buster query string
    content = content.replace('v16_razorsharp_mobile_pinch_zoom', 'v17_inapp_modal_strict_interceptor')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

# 3. Update dashboard.html and app/dashboard.html cache-buster
for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('v16_razorsharp_mobile_pinch_zoom', 'v17_inapp_modal_strict_interceptor')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

# 4. Update vercel.json: change /whitepaper to rewrite to index with open_whitepaper=1
with open('vercel.json', 'r', encoding='utf-8') as f:
    v = json.load(f)

# Filter out /whitepaper and /whitepaper/ from redirects
redirects = [r for r in v.get('redirects', []) if r.get('source') not in ['/whitepaper', '/whitepaper/']]
v['redirects'] = redirects

# Add /whitepaper rewrite at the top of rewrites
rewrites = v.get('rewrites', [])
# Ensure /whitepaper -> /app/index.html?open_whitepaper=1 is first
new_rewrites = [
    { "source": "/whitepaper", "destination": "/app/index.html?open_whitepaper=1" },
    { "source": "/whitepaper/", "destination": "/app/index.html?open_whitepaper=1" }
]
for r in rewrites:
    if r.get('source') not in ['/whitepaper', '/whitepaper/']:
        new_rewrites.append(r)
v['rewrites'] = new_rewrites

with open('vercel.json', 'w', encoding='utf-8') as f:
    json.dump(v, f, indent=2)
print("Updated vercel.json")
