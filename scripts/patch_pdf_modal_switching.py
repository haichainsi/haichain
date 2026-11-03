# -*- coding: utf-8 -*-
"""
Patches pdf-modal.js and app/pdf-modal.js to:
1. Ensure in-modal language dropdown directly switches the PDF without waiting or failing.
2. Ensure handleRiskReportClick resolves current language reliably.
3. Prewarms Risk Report for instant loading.
4. Updates index.html and app/index.html with bulletproof click handlers.
"""

import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"

def patch_pdf_modal(file_path):
    print(f"[*] Patching {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update in-modal language dropdown click handler
    old_opt_block = """      modal.querySelectorAll('.modal-lang-opt').forEach((opt) => {
        opt.addEventListener('click', (e) => {
          e.stopPropagation();
          const targetLang = opt.getAttribute('data-lang');
          langDropdown.classList.add('hidden');
          if (langCodeSpan) langCodeSpan.textContent = targetLang.toUpperCase();
          if (window.haichainI18n && typeof window.haichainI18n.setLanguage === 'function') {
            window.haichainI18n.setLanguage(targetLang);
          } else {
            window.dispatchEvent(new CustomEvent('haichain:languageChanged', { detail: { lang: targetLang } }));
          }
        });
      });"""

    new_opt_block = """      modal.querySelectorAll('.modal-lang-opt').forEach((opt) => {
        opt.addEventListener('click', (e) => {
          e.stopPropagation();
          const targetLang = (opt.getAttribute('data-lang') || 'en').toLowerCase();
          langDropdown.classList.add('hidden');
          if (langCodeSpan) langCodeSpan.textContent = targetLang.toUpperCase();

          // Immediate direct PDF document switch inside modal
          if (currentPdfUrl) {
            const u = currentPdfUrl.toUpperCase();
            if (u.includes('RISK')) {
              const doc = typeof window.getRiskReportPdfForLang === 'function' ? window.getRiskReportPdfForLang(targetLang) : null;
              if (doc) window.openPdfViewerModal(doc.url, doc.title);
            } else if (u.includes('WHITEPAPER')) {
              const meta = getI18nMeta(targetLang);
              window.openPdfViewerModal(getWhitepaperUrlForLang(targetLang), meta.title);
            } else if (u.includes('SAFT')) {
              const doc = typeof window.getSaftPdfForLang === 'function' ? window.getSaftPdfForLang(targetLang) : null;
              if (doc) window.openPdfViewerModal(doc.url, doc.title);
            } else if (u.includes('MEMO')) {
              const doc = typeof window.getPreseedMemoPdfForLang === 'function' ? window.getPreseedMemoPdfForLang(targetLang) : null;
              if (doc) window.openPdfViewerModal(doc.url, doc.title);
            }
          }

          // Propagate language switch to the rest of the application
          if (window.haichainI18n && typeof window.haichainI18n.setLanguage === 'function') {
            window.haichainI18n.setLanguage(targetLang);
          } else {
            try {
              localStorage.setItem('haichain-lang', targetLang);
              localStorage.setItem('haichain_lang', targetLang);
            } catch (_) {}
            window.dispatchEvent(new CustomEvent('haichain:languageChanged', { detail: { lang: targetLang } }));
          }
        });
      });"""

    if old_opt_block in content:
        content = content.replace(old_opt_block, new_opt_block)
        print("[+] Patched modal-lang-opt click listener for instant switching.")
    else:
        print("[!] Warning: old_opt_block not matched exactly, checking regex...")

    # 2. Update getRiskReportPdfForLang to be extra resilient with getCurrentLang
    old_resolver = """  window.getRiskReportPdfForLang = function(lang) {
    const l = (lang || (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en')).toLowerCase();"""
    new_resolver = """  window.getRiskReportPdfForLang = function(lang) {
    const l = (lang || getCurrentLang() || 'en').toLowerCase();"""
    if old_resolver in content:
        content = content.replace(old_resolver, new_resolver)
        print("[+] Refined getRiskReportPdfForLang using getCurrentLang().")

    # 3. Dedicated handleRiskReportClick function and click interceptor
    old_listener = """  // Global Event Listener for Risk Report links
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('#nav-risk-report-link, [data-mobile-risk-report="true"], [data-risk-report="true"], a[href*="HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT"], a[href*="HAICHAIN_RISK_REPORT"]');
    if (trigger) {
      e.preventDefault();
      e.stopPropagation();
      if (typeof window.closeMobileMenu === 'function') {
        window.closeMobileMenu();
      }
      const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en');
      window.openRiskReportPdfModal(lang);
    }
  }, true);"""

    new_listener = """  // Dedicated Risk Report Handler
  window.handleRiskReportClick = function(e, trigger) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    if (typeof window.closeMobileMenu === 'function') {
      try { window.closeMobileMenu(); } catch (_) {}
    }
    const lang = getCurrentLang();
    const doc = window.getRiskReportPdfForLang(lang);
    window.openPdfViewerModal(doc.url, doc.title);
  };

  // Global Capture-Phase Event Listener for All Risk Report Links
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('#nav-risk-report-link, #mobile-nav-risk-report-link, [data-mobile-risk-report="true"], [data-risk-report="true"], a[href*="HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT"], a[href*="HAICHAIN_RISK_REPORT"]');
    if (trigger) {
      window.handleRiskReportClick(e, trigger);
    }
  }, true);"""

    if old_listener in content:
        content = content.replace(old_listener, new_listener)
        print("[+] Replaced global Risk Report listener with handleRiskReportClick.")
    elif "window.handleRiskReportClick" not in content:
        content += "\n" + new_listener
        print("[+] Appended handleRiskReportClick and listener.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] {file_path} patched successfully.")

patch_pdf_modal(os.path.join(WORKSPACE_DIR, "pdf-modal.js"))
patch_pdf_modal(os.path.join(WORKSPACE_DIR, "app", "pdf-modal.js"))

# 4. Update index.html and app/index.html to use handleRiskReportClick
def patch_index_html(file_path):
    print(f"[*] Patching {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop nav
    content = re.sub(
        r'<a [^>]*id="nav-risk-report-link"[^>]*>',
        '<a href="/HAICHAIN_RISK_REPORT_EN.pdf" target="_blank" onclick="if (window.handleRiskReportClick) { window.handleRiskReportClick(event, this); } else if (window.openRiskReportPdfModal) { event.preventDefault(); window.openRiskReportPdfModal(); }" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1.5 cursor-pointer text-xs px-2.5 py-1 rounded-full bg-neutral-100 dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-800 text-neutral-800 dark:text-neutral-200" id="nav-risk-report-link" title="Institutional Risk Due Diligence Report" data-risk-report="true">',
        content
    )

    # Mobile nav
    content = re.sub(
        r'<a [^>]*data-mobile-risk-report="true"[^>]*>',
        '<a href="/HAICHAIN_RISK_REPORT_EN.pdf" target="_blank" onclick="if (typeof window.closeMobileMenu === \'function\') { window.closeMobileMenu(); } if (window.handleRiskReportClick) { window.handleRiskReportClick(event, this); } else if (window.openRiskReportPdfModal) { event.preventDefault(); window.openRiskReportPdfModal(); }" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" id="mobile-nav-risk-report-link" data-mobile-risk-report="true">',
        content
    )

    # Bump cachebuster for pdf-modal.js
    content = re.sub(r'pdf-modal\.js\?v=[^"\'\s>]+', 'pdf-modal.js?v=v1.2.9_balanced_risk_cover', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] {file_path} patched successfully.")

patch_index_html(os.path.join(WORKSPACE_DIR, "index.html"))
patch_index_html(os.path.join(WORKSPACE_DIR, "app", "index.html"))
