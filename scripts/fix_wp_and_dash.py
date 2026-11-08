import re

def fix_index(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Desktop nav link
    html = re.sub(
        r'<a\s+href="javascript:void\(0\)"[^>]*id="nav-whitepaper-link"[^>]*>',
        r'<a href="/HAICHAIN_WHITEPAPER_V1.0_EN.pdf" target="_blank" onclick="if (window.openPdfViewerModal) { event.preventDefault(); const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem(\'haichain_lang\') || \'en\').toUpperCase(); window.openPdfViewerModal(\'/HAICHAIN_WHITEPAPER_V1.0_\' + lang + \'.pdf\'); }" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 cursor-pointer" id="nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">',
        html
    )

    # Mobile nav link
    html = re.sub(
        r'<a\s+href="javascript:void\(0\)"[^>]*id="mobile-nav-whitepaper-link"[^>]*>',
        r'<a href="/HAICHAIN_WHITEPAPER_V1.0_EN.pdf" target="_blank" onclick="if (typeof window.closeMobileMenu === \'function\') { window.closeMobileMenu(); } if (window.openPdfViewerModal) { event.preventDefault(); const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem(\'haichain_lang\') || \'en\').toUpperCase(); window.openPdfViewerModal(\'/HAICHAIN_WHITEPAPER_V1.0_\' + lang + \'.pdf\'); }" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" id="mobile-nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">',
        html
    )

    # Footer whitepaper link
    html = re.sub(
        r'<a\s+href="javascript:void\(0\)"[^>]*data-open-whitepaper="true"[^>]*>',
        r'<a href="/HAICHAIN_WHITEPAPER_V1.0_EN.pdf" target="_blank" onclick="if (window.openPdfViewerModal) { event.preventDefault(); const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem(\'haichain_lang\') || \'en\').toUpperCase(); window.openPdfViewerModal(\'/HAICHAIN_WHITEPAPER_V1.0_\' + lang + \'.pdf\'); }" class="hover:text-black dark:hover:text-white transition-colors cursor-pointer" data-open-whitepaper="true">',
        html
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Patched {path}")

def fix_dash(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'/app/i18n\.js\?v=[^"\'>\s]+', r'/app/i18n.js?v=v29_institutional_audit_upgrade_1793593000000', html)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Patched {path}")

fix_index('index.html')
fix_index('app/index.html')
fix_dash('dashboard.html')
fix_dash('app/dashboard.html')
