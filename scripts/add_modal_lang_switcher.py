import re

MODAL_LANG_HTML = '''            <!-- In-Modal Quick Language Selector (Syncs with Global Engine) -->
            <div class="relative" id="pdf-modal-lang-container">
              <button id="pdf-modal-lang-toggle" type="button" class="px-2 h-7 sm:h-8 rounded-lg flex items-center space-x-1 text-[10px] sm:text-[11px] font-mono font-bold text-neutral-300 hover:text-white bg-neutral-800 hover:bg-neutral-700 transition-colors border border-neutral-700 cursor-pointer" title="Change Language / Đổi Ngôn Ngữ">
                <span id="pdf-modal-lang-code">EN</span>
                <svg class="w-3 h-3 text-neutral-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </button>
              <div id="pdf-modal-lang-dropdown" class="absolute right-0 top-full mt-1.5 w-32 py-1 bg-[#18181b] border border-neutral-700 rounded-xl shadow-2xl hidden z-50 overflow-hidden font-mono text-[11px]">
                <button type="button" data-lang="en" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>English</span><span class="text-[10px] text-neutral-500">EN</span></button>
                <button type="button" data-lang="vi" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Tiếng Việt</span><span class="text-[10px] text-neutral-500">VI</span></button>
                <button type="button" data-lang="zh" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>中文</span><span class="text-[10px] text-neutral-500">ZH</span></button>
                <button type="button" data-lang="ko" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>한국어</span><span class="text-[10px] text-neutral-500">KO</span></button>
                <button type="button" data-lang="es" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Español</span><span class="text-[10px] text-neutral-500">ES</span></button>
                <button type="button" data-lang="fr" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Français</span><span class="text-[10px] text-neutral-500">FR</span></button>
                <button type="button" data-lang="ru" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Русский</span><span class="text-[10px] text-neutral-500">RU</span></button>
                <button type="button" data-lang="kk" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Қазақша</span><span class="text-[10px] text-neutral-500">KK</span></button>
                <button type="button" data-lang="hi" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>हिन्दी</span><span class="text-[10px] text-neutral-500">HI</span></button>
                <button type="button" data-lang="he" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>עברית</span><span class="text-[10px] text-neutral-500">HE</span></button>
              </div>
            </div>'''

INIT_LANG_SWITCHER_JS = '''    // Initialize In-Modal Language Dropdown
    const langToggle = modal.querySelector('#pdf-modal-lang-toggle');
    const langDropdown = modal.querySelector('#pdf-modal-lang-dropdown');
    const langCodeSpan = modal.querySelector('#pdf-modal-lang-code');

    if (langToggle && langDropdown) {
      langToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        langDropdown.classList.toggle('hidden');
      });

      modal.querySelectorAll('.modal-lang-opt').forEach((opt) => {
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
      });

      document.addEventListener('click', () => {
        if (!langDropdown.classList.contains('hidden')) {
          langDropdown.classList.add('hidden');
        }
      });
    }'''

def add_switcher(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert HTML before Digital E-Signature Action Button
    target_html = '<div class="h-4 w-px bg-neutral-300 dark:bg-neutral-700 mx-0.5 sm:mx-1"></div>'
    replacement_html = target_html + '\n\n' + MODAL_LANG_HTML
    if 'id="pdf-modal-lang-container"' not in content:
        content = content.replace(target_html, replacement_html, 1)

    # Insert JS logic inside ensurePdfModal before close button logic
    target_js = '// Close button'
    replacement_js = INIT_LANG_SWITCHER_JS + '\n\n    // Close button'
    if 'Initialize In-Modal Language Dropdown' not in content:
        content = content.replace(target_js, replacement_js, 1)

    # In openPdfViewerModal, update #pdf-modal-lang-code
    target_open = "if (zoomLabel) zoomLabel.textContent = '100%';"
    replacement_open = "if (zoomLabel) zoomLabel.textContent = '100%';\n    const modalLangCode = document.getElementById('pdf-modal-lang-code');\n    if (modalLangCode) modalLangCode.textContent = (lang || 'en').toUpperCase();"
    if 'modalLangCode.textContent' not in content:
        content = content.replace(target_open, replacement_open, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added modal language switcher to {filepath}")

add_switcher('app/pdf-modal.js')
add_switcher('pdf-modal.js')

# Update cachebusters in dashboard.html & app/dashboard.html
for html_path in ['dashboard.html', 'app/dashboard.html']:
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'pdf-modal\.js\?v=v3[0-9]_[^"]+', 'pdf-modal.js?v=v38_inmodal_lang_sync_1793642000000', html)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated cachebuster in {html_path}")
