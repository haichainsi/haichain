import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

print("=== 1. Updating i18n.js ===")
with open('i18n.js', 'r', encoding='utf-8') as f:
    i18n_content = f.read()

replacements = [
    ('    "hero.exploreArch": "Архитектураны зерттеу",\n',
     '    "hero.exploreArch": "Ақ Қағаз",\n    "hero.whitepaper": "Ақ Қағаз",\n'),
    ('    "hero.exploreArch": "Explore Architecture",\n',
     '    "hero.exploreArch": "Whitepaper",\n    "hero.whitepaper": "Whitepaper",\n'),
    ('    "hero.exploreArch": "探索技术架构",\n',
     '    "hero.exploreArch": "白皮书",\n    "hero.whitepaper": "白皮书",\n'),
    ('    "hero.exploreArch": "Explorer l\'Architecture",\n',
     '    "hero.exploreArch": "Livre Blanc",\n    "hero.whitepaper": "Livre Blanc",\n'),
    ('    "hero.exploreArch": "기술 구조 둘러보기",\n',
     '    "hero.exploreArch": "백서",\n    "hero.whitepaper": "백서",\n'),
    ('    "hero.exploreArch": "Explorar Arquitectura",\n',
     '    "hero.exploreArch": "Libro Blanco",\n    "hero.whitepaper": "Libro Blanco",\n'),
    ('    "hero.exploreArch": "Изучить Архитектуру",\n',
     '    "hero.exploreArch": "Whitepaper",\n    "hero.whitepaper": "Whitepaper",\n'),
    ('    "hero.exploreArch": "Khám Phá Kiến Trúc",\n',
     '    "hero.exploreArch": "Whitepaper",\n    "hero.whitepaper": "Whitepaper",\n'),
    ('    "hero.exploreArch": "आर्किटेक्चर देखें",\n',
     '    "hero.exploreArch": "श्वेतपत्र",\n    "hero.whitepaper": "श्वेतपत्र",\n'),
    ('    "hero.exploreArch": "חקור ארכיטקטורה",\n',
     '    "hero.exploreArch": "ספר לבן",\n    "hero.whitepaper": "ספר לבן",\n'),
]

for old, new in replacements:
    if old not in i18n_content:
        raise ValueError(f"Pattern not found in i18n.js:\n{old}")
    i18n_content = i18n_content.replace(old, new, 1)

with open('i18n.js', 'w', encoding='utf-8') as f:
    f.write(i18n_content)
with open('app/i18n.js', 'w', encoding='utf-8') as f:
    f.write(i18n_content)
print("Updated i18n.js and app/i18n.js successfully.")

print("=== 2. Updating pdf-modal.js ===")
with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    pdf_content = f.read()

old_sel = "'#nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link, [data-open-whitepaper], [data-pdf-whitepaper], a[href*=\"whitepaper\"], a[href*=\"WHITEPAPER\"]'"
new_sel = "'#nav-whitepaper-link, #hero-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link, [data-open-whitepaper], [data-pdf-whitepaper], a[href*=\"whitepaper\"], a[href*=\"WHITEPAPER\"]'"

if old_sel not in pdf_content:
    raise ValueError("Selector string not found in pdf-modal.js")
pdf_content = pdf_content.replace(old_sel, new_sel)

with open('pdf-modal.js', 'w', encoding='utf-8') as f:
    f.write(pdf_content)
with open('app/pdf-modal.js', 'w', encoding='utf-8') as f:
    f.write(pdf_content)
print("Updated pdf-modal.js and app/pdf-modal.js successfully.")

print("=== 3. Updating index.html ===")
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

old_button = """        <a href="#spending-pot" class="w-full sm:w-auto px-6 py-3.5 rounded-2xl border border-neutral-300/90 dark:border-neutral-700 bg-white/90 dark:bg-neutral-900/80 backdrop-blur-md hover:bg-neutral-100 dark:hover:bg-neutral-800 text-neutral-950 dark:text-neutral-100 font-semibold text-sm transition-all flex items-center justify-center space-x-2 shadow-sm active:scale-95">







          <span data-i18n="hero.exploreArch">Explore Architecture</span>







          <i data-lucide="arrow-down" class="w-4 h-4"></i>







        </a>"""

new_button = """        <a href="/HAICHAIN_WHITEPAPER_V1.0_EN.pdf" target="_blank" onclick="if (window.openPdfViewerModal) { event.preventDefault(); const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en').toUpperCase(); window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_' + lang + '.pdf'); }" class="w-full sm:w-auto px-6 py-3.5 rounded-2xl border border-neutral-300/90 dark:border-neutral-700 bg-white/90 dark:bg-neutral-900/80 backdrop-blur-md hover:bg-neutral-100 dark:hover:bg-neutral-800 text-neutral-950 dark:text-neutral-100 font-semibold text-sm transition-all flex items-center justify-center space-x-2 shadow-sm active:scale-95 cursor-pointer" id="hero-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">
          <span data-i18n="hero.whitepaper">Whitepaper</span>
          <i data-lucide="file-text" class="w-4 h-4"></i>
        </a>"""

if old_button not in html_content:
    raise ValueError("old_button not found in index.html")

html_content = html_content.replace(old_button, new_button, 1)

# Bump cache buster for i18n.js and pdf-modal.js
html_content = html_content.replace(
    'src="/app/i18n.js?v=v67_guaranteed_scroll_to_top_20261104"',
    'src="/app/i18n.js?v=v68_hero_whitepaper_modal_20261104"'
)
html_content = html_content.replace(
    'src="/app/pdf-modal.js?v=v67_guaranteed_scroll_to_top_20261104"',
    'src="/app/pdf-modal.js?v=v68_hero_whitepaper_modal_20261104"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
with open('app/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Updated index.html and app/index.html successfully.")
