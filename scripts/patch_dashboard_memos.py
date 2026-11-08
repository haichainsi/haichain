import re

for dash_path in ['dashboard.html', 'app/dashboard.html']:
    with open(dash_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update pdf-modal script version
    content = content.replace(
        '/app/pdf-modal.js?v=v18_inapp_modal_menu_sync',
        '/app/pdf-modal.js?v=v19_cachebust_institutional_1793600000'
    )

    # 2. Add openPreseedMemoModal and modernize openSaftPdfModal
    old_saft_func = """    window.openSaftPdfModal = function() {
      if (typeof window.openPdfViewerModal === 'function') {
        window.openPdfViewerModal('/HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf', 'HAICHAIN Official SAFT Agreement (Mainnet Guaranteed)');
      } else {
        window.open('/HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf', '_blank');
      }
    };"""

    new_saft_and_memo_func = """    window.openSaftPdfModal = function() {
      const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en').toLowerCase();
      const pdfUrl = (lang === 'vi') ? '/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf' : '/HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf';
      const title = (lang === 'vi') ? 'Thỏa Thuận Pháp Lý SAFT HAICHAIN (Bảo Lãnh Mainnet)' : 'HAICHAIN Official SAFT Agreement (Mainnet Guaranteed)';
      if (typeof window.openPdfViewerModal === 'function') {
        window.openPdfViewerModal(pdfUrl, title);
      } else {
        window.open(pdfUrl, '_blank');
      }
    };

    window.openPreseedMemoModal = function() {
      const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en').toLowerCase();
      const pdfUrl = (lang === 'vi') ? '/HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf' : '/HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.pdf';
      const title = (lang === 'vi') ? 'Bản Tóm Tắt Đầu Tư Pre-Seed (1-Pager Executive Memo)' : 'HAICHAIN Pre-Seed Strategic Investment Memo';
      if (typeof window.openPdfViewerModal === 'function') {
        window.openPdfViewerModal(pdfUrl, title);
      } else {
        window.open(pdfUrl, '_blank');
      }
    };"""

    # Normalize CRLF
    content_norm = content.replace('\r\n', '\n')
    if old_saft_func in content_norm:
        content_norm = content_norm.replace(old_saft_func, new_saft_and_memo_func)
        print(f"Updated saft/memo functions in {dash_path}")
    else:
        print(f"Could not find exact old_saft_func in {dash_path}")

    # 3. Add Preseed Memo button in Tab 7 action buttons
    old_buttons = """              <button type="button" onclick="if(window.openSaftPdfModal){window.openSaftPdfModal();}else{window.switchTab('tab-preseed');}" class="py-2 px-3.5 rounded-xl bg-white text-black hover:bg-neutral-200 font-medium text-xs font-mono transition-all flex items-center space-x-1.5 shadow-sm active:scale-95 cursor-pointer">
                <i data-lucide="file-text" class="w-3.5 h-3.5"></i>
                <span>${getVestingText('viewLegalSaftBtn', lang)}</span>
              </button>"""

    new_buttons = """              <button type="button" onclick="if(window.openSaftPdfModal){window.openSaftPdfModal();}else{window.switchTab('tab-preseed');}" class="py-2 px-3.5 rounded-xl bg-white text-black hover:bg-neutral-200 font-medium text-xs font-mono transition-all flex items-center space-x-1.5 shadow-sm active:scale-95 cursor-pointer">
                <i data-lucide="file-text" class="w-3.5 h-3.5"></i>
                <span>${getVestingText('viewLegalSaftBtn', lang)}</span>
              </button>
              <button type="button" onclick="if(window.openPreseedMemoModal){window.openPreseedMemoModal();}" class="py-2 px-3.5 rounded-xl border border-neutral-700 bg-neutral-900/60 text-white hover:border-white font-medium text-xs font-mono transition-all flex items-center space-x-1.5 active:scale-95 cursor-pointer">
                <i data-lucide="file-check" class="w-3.5 h-3.5"></i>
                <span>${lang === 'vi' ? 'Xem 1-Pager Memo' : 'View 1-Pager Memo'}</span>
              </button>"""

    if old_buttons in content_norm:
        content_norm = content_norm.replace(old_buttons, new_buttons)
        print(f"Added Pre-Seed Memo button in {dash_path}")
    else:
        print(f"Could not find exact old_buttons in {dash_path}")

    with open(dash_path, 'w', encoding='utf-8') as f:
        f.write(content_norm)

# Also update index.html and app/index.html for pdf-modal version
for idx_path in ['index.html', 'app/index.html']:
    with open(idx_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(
        '/app/pdf-modal.js?v=v18_inapp_modal_menu_sync',
        '/app/pdf-modal.js?v=v19_cachebust_institutional_1793600000'
    )
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated pdf-modal script in {idx_path}")
