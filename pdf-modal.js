/**
 * HAICHAIN Universal Online PDF Viewer Modal System
 * Provides Apple Titanium luxury modal experience for reading PDF documents online
 * Optimized for Mobile (94vh, touch friendly) & Desktop (88vh, max-w-5xl, FitH view)
 */
(function () {
  'use strict';

  function getCurrentLang() {
    if (window.haichainI18n && typeof window.haichainI18n.getLanguage === 'function') {
      return window.haichainI18n.getLanguage();
    }
    return localStorage.getItem('haichain_lang') || document.documentElement.getAttribute('lang') || 'en';
  }

  function ensurePdfModal() {
    let modal = document.getElementById('pdf-viewer-modal');
    if (modal) return modal;

    modal = document.createElement('div');
    modal.id = 'pdf-viewer-modal';
    modal.className = 'fixed inset-0 z-[100] bg-black/80 backdrop-blur-md hidden flex items-center justify-center p-2 sm:p-4 md:p-6 transition-all duration-200';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');

    const isVi = getCurrentLang() === 'vi';

    modal.innerHTML = `
      <div class="w-full max-w-5xl h-[94vh] sm:h-[88vh] bg-white dark:bg-[#0c0c0e] border border-neutral-200 dark:border-neutral-800 rounded-3xl shadow-2xl flex flex-col overflow-hidden animate-scaleUp">
        <!-- Modal Header Bar -->
        <div class="px-4 py-3 sm:px-6 sm:py-3.5 border-b border-neutral-200 dark:border-neutral-800 flex items-center justify-between gap-3 bg-neutral-50/95 dark:bg-neutral-900/95 shrink-0 backdrop-blur-sm">
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
              <span id="pdf-modal-fullscreen-label" class="hidden md:inline">${isVi ? 'Toàn Màn Hình' : 'Fullscreen'}</span>
            </a>
            <a id="pdf-modal-download-btn" href="#" download class="px-3 py-1.5 rounded-xl bg-black dark:bg-white text-white dark:text-black text-xs font-mono font-bold transition-all flex items-center space-x-1.5 hover:opacity-90 active:scale-95 shadow-sm" title="Tải PDF về máy">
              <i data-lucide="download" class="w-3.5 h-3.5"></i>
              <span id="pdf-modal-download-label" class="hidden sm:inline">${isVi ? 'Tải PDF' : 'Download'}</span>
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

    return modal;
  }

  window.openPdfViewerModal = function (pdfUrl, docTitle) {
    const modal = ensurePdfModal();
    const iframe = document.getElementById('pdf-modal-iframe');
    const titleEl = document.getElementById('pdf-modal-title');
    const newTabEl = document.getElementById('pdf-modal-open-new-tab');
    const downloadEl = document.getElementById('pdf-modal-download-btn');
    const fsLabel = document.getElementById('pdf-modal-fullscreen-label');
    const dlLabel = document.getElementById('pdf-modal-download-label');

    const isVi = getCurrentLang() === 'vi';
    if (fsLabel) fsLabel.textContent = isVi ? 'Toàn Màn Hình' : 'Fullscreen';
    if (dlLabel) dlLabel.textContent = isVi ? 'Tải PDF' : 'Download';

    if (titleEl) titleEl.textContent = docTitle || 'HAICHAIN Document';
    if (newTabEl) newTabEl.href = pdfUrl;
    if (downloadEl) {
      downloadEl.href = pdfUrl;
      downloadEl.download = pdfUrl.split('/').pop().split('?')[0];
    }
    if (iframe) {
      // Append FitH toolbar params for responsive reading
      const cleanUrl = pdfUrl.split('#')[0];
      iframe.src = cleanUrl + '#toolbar=1&navpanes=0&view=FitH';
    }

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';

    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }
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

  window.openWhitepaperModal = function () {
    const lang = getCurrentLang();
    if (lang === 'vi') {
      window.openPdfViewerModal(
        '/HAICHAIN_WHITEPAPER_V1.0_VI.pdf',
        'Bạch Thư Kỹ Thuật HAICHAIN v1.0 (Tiếng Việt)'
      );
    } else {
      window.openPdfViewerModal(
        '/HAICHAIN_WHITEPAPER_V1.0_EN.pdf',
        'HAICHAIN Technical Whitepaper v1.0 (English)'
      );
    }
  };

  // Delegated Click Handler for all Whitepaper links across the app
  document.addEventListener('click', function (e) {
    const trigger = e.target.closest('a[href="/whitepaper"], a[href="/whitepaper/"], a[href="/whitepaper.pdf"], a[href="/whitepaper-en.pdf"], a[href="/whitepaper-vi.pdf"], [data-open-whitepaper], #nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link');
    if (trigger) {
      e.preventDefault();

      // If mobile navigation drawer/menu is open, close it cleanly
      if (window.haichainI18n && typeof window.haichainI18n.closeMobileDrawer === 'function') {
        window.haichainI18n.closeMobileDrawer();
      }
      const mobileMenu = document.getElementById('mobile-menu');
      if (mobileMenu && !mobileMenu.classList.contains('menu-closed')) {
        mobileMenu.classList.add('menu-closed');
      }

      window.openWhitepaperModal();
    }
  });

  // Ensure DOM ready initialization
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ensurePdfModal);
  } else {
    ensurePdfModal();
  }
})();
