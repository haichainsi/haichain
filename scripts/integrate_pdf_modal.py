import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# 1. Replace the download links with interactive popup buttons
old_buttons = """          <!-- Document Action Buttons (Compact Sleek Pill Cluster) -->
          <div class="flex items-center gap-2 shrink-0">
            <a href="${phase.saftUrl}" download class="px-3.5 py-2 rounded-xl bg-black dark:bg-white text-white dark:text-black font-semibold text-xs font-mono transition-all flex items-center justify-center space-x-1.5 hover:opacity-90 active:scale-95 shadow-sm">
              <i data-lucide="file-check" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('downloadSaft')}</span>
            </a>
            <a href="${phase.memoUrl}" download class="px-3.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-medium text-xs font-mono transition-all flex items-center justify-center space-x-1.5 active:scale-95">
              <i data-lucide="book-open" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('downloadMemo')}</span>
            </a>
          </div>"""

new_buttons = """          <!-- Document Action Buttons (Interactive Online PDF Viewer Popups) -->
          <div class="flex items-center gap-2 shrink-0">
            <button type="button" id="btn-open-saft-pdf" class="px-3.5 py-2 rounded-xl bg-black dark:bg-white text-white dark:text-black font-semibold text-xs font-mono transition-all flex items-center justify-center space-x-1.5 hover:opacity-90 active:scale-95 shadow-sm cursor-pointer" title="Đọc hợp đồng SAFT online">
              <i data-lucide="file-text" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('downloadSaft')}</span>
            </button>
            <button type="button" id="btn-open-memo-pdf" class="px-3.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-medium text-xs font-mono transition-all flex items-center justify-center space-x-1.5 active:scale-95 cursor-pointer" title="Đọc bản tóm tắt Memo online">
              <i data-lucide="book-open" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('downloadMemo')}</span>
            </button>
          </div>"""

if old_buttons in text:
    text = text.replace(old_buttons, new_buttons)
    print("SUCCESS: Replaced buttons with interactive PDF viewer triggers.")
else:
    print("WARNING: old_buttons not found directly.")

# 2. Add PDF modal controller logic before setupCalculatorLogic
modal_logic_code = """  // 6.5 UNIVERSAL ONLINE PDF VIEWER POPUP MODAL (DESKTOP & MOBILE OPTIMIZED)
  function ensurePdfModal() {
    if (document.getElementById('pdf-viewer-modal')) return;
    const modal = document.createElement('div');
    modal.id = 'pdf-viewer-modal';
    modal.className = 'fixed inset-0 z-[100] bg-black/80 backdrop-blur-md hidden flex items-center justify-center p-2 sm:p-4 md:p-6 transition-all duration-200';
    modal.innerHTML = `
      <div class="w-full max-w-5xl h-[94vh] sm:h-[88vh] bg-white dark:bg-[#0c0c0e] border border-neutral-200 dark:border-neutral-800 rounded-3xl shadow-2xl flex flex-col overflow-hidden animate-scaleUp">
        <!-- Modal Header -->
        <div class="px-4 py-3 sm:px-6 sm:py-3.5 border-b border-neutral-200 dark:border-neutral-800 flex items-center justify-between gap-3 bg-neutral-50/90 dark:bg-neutral-900/90 shrink-0">
          <div class="flex items-center space-x-2.5 min-w-0">
            <div class="w-8 h-8 rounded-xl bg-black dark:bg-white text-white dark:text-black flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="file-text" class="w-4 h-4"></i>
            </div>
            <div class="min-w-0">
              <h3 id="pdf-modal-title" class="font-bold text-xs sm:text-sm text-black dark:text-white truncate">Document Viewer</h3>
              <p class="text-[10px] text-neutral-400 font-mono hidden sm:block">HAICHAIN Official Institutional Documentation</p>
            </div>
          </div>
          <!-- Action Buttons -->
          <div class="flex items-center space-x-2 shrink-0">
            <a id="pdf-modal-open-new-tab" href="#" target="_blank" class="px-3 py-1.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white text-xs font-mono font-medium transition-all flex items-center space-x-1.5 active:scale-95" title="Mở toàn màn hình">
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
              <span class="hidden md:inline">${getActiveLang() === 'vi' ? 'Toàn Màn Hình' : 'Fullscreen'}</span>
            </a>
            <a id="pdf-modal-download-btn" href="#" download class="px-3 py-1.5 rounded-xl bg-black dark:bg-white text-white dark:text-black text-xs font-mono font-bold transition-all flex items-center space-x-1.5 hover:opacity-90 active:scale-95 shadow-sm" title="Tải PDF về máy">
              <i data-lucide="download" class="w-3.5 h-3.5"></i>
              <span class="hidden sm:inline">${getActiveLang() === 'vi' ? 'Tải PDF' : 'Download'}</span>
            </a>
            <button id="pdf-modal-close-btn" class="p-1.5 sm:p-2 rounded-xl text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors" title="Đóng">
              <i data-lucide="x" class="w-5 h-5"></i>
            </button>
          </div>
        </div>

        <!-- Viewer Body -->
        <div class="relative w-full flex-1 bg-neutral-100 dark:bg-neutral-950 flex flex-col overflow-hidden">
          <iframe id="pdf-modal-iframe" src="" class="w-full flex-1 border-0" allow="fullscreen"></iframe>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    const closeBtn = modal.querySelector('#pdf-modal-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', window.closePdfViewerModal);
    }

    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        window.closePdfViewerModal();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        window.closePdfViewerModal();
      }
    });
  }

  window.openPdfViewerModal = function (pdfUrl, docTitle) {
    ensurePdfModal();
    const modal = document.getElementById('pdf-viewer-modal');
    const iframe = document.getElementById('pdf-modal-iframe');
    const titleEl = document.getElementById('pdf-modal-title');
    const newTabEl = document.getElementById('pdf-modal-open-new-tab');
    const downloadEl = document.getElementById('pdf-modal-download-btn');

    if (titleEl) titleEl.textContent = docTitle;
    if (newTabEl) newTabEl.href = pdfUrl;
    if (downloadEl) {
      downloadEl.href = pdfUrl;
      downloadEl.download = pdfUrl.split('/').pop();
    }
    if (iframe) {
      iframe.src = pdfUrl + '#toolbar=1&navpanes=0&view=FitH';
    }

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    if (window.lucide) window.lucide.createIcons();
  };

  window.closePdfViewerModal = function () {
    const modal = document.getElementById('pdf-viewer-modal');
    if (modal) {
      modal.classList.add('hidden');
      const iframe = document.getElementById('pdf-modal-iframe');
      if (iframe) iframe.src = '';
    }
    document.body.style.overflow = '';
  };

"""

# Insert before setupCalculatorLogic
target_setup = "  // 7. CALCULATOR LOGIC\n  function setupCalculatorLogic(container) {"
if target_setup in text:
    text = text.replace(target_setup, modal_logic_code + target_setup)
    print("SUCCESS: Injected PDF modal controller logic.")
else:
    print("WARNING: target_setup not found.")

# 3. Add event listeners inside setupCalculatorLogic
target_listeners = "    if (inputUsdt) {"
new_pdf_listeners = """    // Document PDF Online Viewer Triggers
    const btnSaft = container.querySelector('#btn-open-saft-pdf');
    if (btnSaft) {
      btnSaft.addEventListener('click', (e) => {
        e.preventDefault();
        const title = getActiveLang() === 'vi' 
          ? 'Hợp Đồng SAFT Pre-Seed HAICHAIN (Song Ngữ VI & EN)' 
          : 'HAICHAIN Pre-Seed SAFT Agreement (Bilingual VI & EN)';
        window.openPdfViewerModal('/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf', title);
      });
    }

    const btnMemo = container.querySelector('#btn-open-memo-pdf');
    if (btnMemo) {
      btnMemo.addEventListener('click', (e) => {
        e.preventDefault();
        const title = getActiveLang() === 'vi' 
          ? 'Bản Tóm Tắt Chiến Lược 1 Trang - Vòng Pre-Seed' 
          : 'HAICHAIN Pre-Seed 1-Pager Investment Teaser Memo';
        window.openPdfViewerModal('/HAICHAIN_PRESEED_ONE_PAGER_MEMO_VI_EN.pdf', title);
      });
    }

    if (inputUsdt) {"""

if target_listeners in text:
    text = text.replace(target_listeners, new_pdf_listeners)
    print("SUCCESS: Added PDF viewer event listeners in setupCalculatorLogic.")
else:
    print("WARNING: target_listeners not found.")

with open('sale-controller.js', 'w', encoding='utf-8') as f:
    f.write(text)

with open('app/sale-controller.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: sale-controller.js updated and synced to app/sale-controller.js.")
