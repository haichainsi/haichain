import os

def update_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            modified = True
            print(f"[OK] Replaced in {filepath}")
        else:
            print(f"[WARN] Target not found in {filepath}: {old[:50]}...")

    if modified:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        print(f"[SAVED] {filepath}")

# Update index.html and app/index.html
index_replacements = [
    (
        '<script src="/app/i18n.js?v=v25_back_to_home"></script>',
        '<script src="/app/i18n.js?v=v25_back_to_home"></script>\n  <!-- HAICHAIN Universal Online PDF Viewer Modal -->\n  <script src="/app/pdf-modal.js?v=v1_whitepaper"></script>'
    ),
    (
        '<a href="/whitepaper" target="_blank" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1">\n\n          <span data-i18n="nav.whitepaper">Whitepaper</span>',
        '<a href="/whitepaper" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 cursor-pointer" id="nav-whitepaper-link" data-open-whitepaper="true">\n\n          <span data-i18n="nav.whitepaper">Whitepaper</span>'
    ),
    (
        '<a href="/whitepaper" target="_blank" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors">\n        <span data-i18n="nav.whitepaper">Technical Whitepaper v1.0</span>',
        '<a href="/whitepaper" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" id="mobile-nav-whitepaper-link" data-open-whitepaper="true">\n        <span data-i18n="nav.whitepaper">Technical Whitepaper v1.0</span>'
    ),
    (
        '<a href="/whitepaper" target="_blank" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1">\n            <span data-i18n="nav.whitepaper">Whitepaper</span>',
        '<a href="/whitepaper" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 cursor-pointer" id="footer-whitepaper-link" data-open-whitepaper="true">\n            <span data-i18n="nav.whitepaper">Whitepaper</span>'
    )
]

for p in ['index.html', 'app/index.html']:
    update_file(p, index_replacements)

# Update dashboard.html and app/dashboard.html
dashboard_replacements = [
    (
        '<script src="/app/i18n.js?v=v25_back_to_home"></script>',
        '<script src="/app/i18n.js?v=v25_back_to_home"></script>\n  <!-- HAICHAIN Universal Online PDF Viewer Modal -->\n  <script src="/app/pdf-modal.js?v=v1_whitepaper"></script>'
    )
]

for p in ['dashboard.html', 'app/dashboard.html']:
    update_file(p, dashboard_replacements)
