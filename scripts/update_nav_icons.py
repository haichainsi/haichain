import os

# 1. Update index.html and app/index.html
for html_path in ['index.html', 'app/index.html']:
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop nav Whitepaper link: remove external-link icon, replace with file-text or clean
    content = content.replace(
        '<a href="/whitepaper" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 cursor-pointer" id="nav-whitepaper-link" data-open-whitepaper="true">\n\n          <span data-i18n="nav.whitepaper">Whitepaper</span>\n\n          <i data-lucide="external-link" class="w-3.5 h-3.5"></i>\n\n        </a>',
        '<a href="/whitepaper" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 cursor-pointer" id="nav-whitepaper-link" data-open-whitepaper="true">\n\n          <span data-i18n="nav.whitepaper">Whitepaper</span>\n\n        </a>'
    )

    # Mobile nav Whitepaper link: remove external-link icon
    content = content.replace(
        '<a href="/whitepaper" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" id="mobile-nav-whitepaper-link" data-open-whitepaper="true">\n        <span data-i18n="nav.whitepaper">Technical Whitepaper v1.0</span>\n        <i data-lucide="external-link" class="w-4 h-4 text-neutral-400"></i>\n      </a>',
        '<a href="/whitepaper" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" id="mobile-nav-whitepaper-link" data-open-whitepaper="true">\n        <span data-i18n="nav.whitepaper">Technical Whitepaper v1.0</span>\n        <i data-lucide="file-text" class="w-4 h-4 text-neutral-400"></i>\n      </a>'
    )

    # Footer Whitepaper link: remove external-link icon
    content = content.replace(
        '<a href="/whitepaper" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 cursor-pointer" id="footer-whitepaper-link" data-open-whitepaper="true">\n            <span data-i18n="nav.whitepaper">Whitepaper</span>\n            <i data-lucide="external-link" class="w-3 h-3"></i>\n          </a>',
        '<a href="/whitepaper" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 cursor-pointer" id="footer-whitepaper-link" data-open-whitepaper="true">\n            <span data-i18n="nav.whitepaper">Whitepaper</span>\n          </a>'
    )

    # Bump cache version to v6_no_newtab
    content = content.replace('/app/pdf-modal.js?v=v5_clean_viewer', '/app/pdf-modal.js?v=v6_no_newtab')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {html_path}")

# 2. Update dashboard.html and app/dashboard.html cache version
for dash_path in ['dashboard.html', 'app/dashboard.html']:
    with open(dash_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('/app/pdf-modal.js?v=v5_clean_viewer', '/app/pdf-modal.js?v=v6_no_newtab')
    with open(dash_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {dash_path}")
