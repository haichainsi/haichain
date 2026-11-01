/**
 * HAICHAIN Universal Online PDF Viewer Modal System
 * Provides Apple Titanium luxury in-app reading experience for PDF documents
 * Clean & Minimalist:
 *  - Title + Close button ONLY (Zero download buttons, zero open in new tab buttons as requested)
 *  - Responsive: Fullscreen on mobile (94vh), max-w-5xl (88vh) on desktop
 *  - Mobile & Android Optimized:
 *      * Shifted Google Docs Viewer toolbar off-canvas (-54px) to eliminate Google header and popout button
 *      * Corner shield + sandbox to strictly prohibit opening new tabs or windows
 *      * 100% CJK & Asian font fidelity with touch scroll
 *  - Desktop / iOS: Native vector engine with #toolbar=0&navpanes=0&view=FitH
 *  - Multilingual Title Detection: en, vi, zh, ko, es, fr, ru, kk
 */
(function () {
  'use strict';

  function getCurrentLang() {
    if (window.haichainI18n && typeof window.haichainI18n.getLanguage === 'function') {
      return window.haichainI18n.getLanguage();
    }
    return localStorage.getItem('haichain_lang') || document.documentElement.getAttribute('lang') || 'en';
  }

  function getI18nTitle(lang) {
    switch (lang) {
      case 'vi':
        return 'Bạch Thư Kỹ Thuật HAICHAIN v1.0 (Tiếng Việt)';
      case 'zh':
        return 'HAICHAIN 技术白皮书 v1.0 (中文)';
      case 'ko':
        return 'HAICHAIN 기술 백서 v1.0 (한국어)';
      case 'es':
        return 'Libro Blanco Técnico de HAICHAIN v1.0 (Español)';
      case 'fr':
        return 'Livre Blanc Technique HAICHAIN v1.0 (Français)';
      case 'ru':
        return 'Технический White Paper HAICHAIN v1.0 (Русский)';
      case 'kk':
        return 'HAICHAIN Техникалық ақ қағазы v1.0 (Қазақша)';
      default:
        return 'HAICHAIN Technical Whitepaper v1.0 (English)';
    }
  }

  function isAndroidDevice() {
    const ua = navigator.userAgent || navigator.vendor || window.opera || '';
    return /Android/i.test(ua);
  }

  function ensurePdfModal() {
    let modal = document.getElementById('pdf-viewer-modal');
    if (modal) return modal;

    modal = document.createElement('div');
    modal.id = 'pdf-viewer-modal';
    modal.className = 'fixed inset-0 z-[100] bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-2 sm:p-4 md:p-6 transition-all duration-200';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');

    modal.innerHTML = `
      <div class="w-full max-w-5xl h-[94vh] sm:h-[88vh] bg-white dark:bg-[#0c0c0e] border border-neutral-200 dark:border-neutral-800 rounded-3xl shadow-2xl flex flex-col overflow-hidden animate-scaleUp">
        
        <!-- Modal Top Navigation Bar (Clean Minimalist: Title + Close Button ONLY) -->
        <div class="px-4 py-3 sm:px-6 sm:py-3.5 border-b border-neutral-200 dark:border-neutral-800 flex items-center justify-between gap-3 bg-neutral-50/95 dark:bg-neutral-900/95 shrink-0 backdrop-blur-sm z-20">
          
          <!-- Document Badge & Title -->
          <div class="flex items-center space-x-2.5 min-w-0">
            <div class="w-8 h-8 rounded-xl bg-black dark:bg-white text-white dark:text-black flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="file-text" class="w-4 h-4"></i>
            </div>
            <div class="min-w-0">
              <h3 id="pdf-modal-title" class="font-bold text-xs sm:text-sm text-black dark:text-white truncate">HAICHAIN Document</h3>
              <p class="text-[10px] text-neutral-400 font-mono hidden sm:block">HAICHAIN Universal Autonomous Machine Financial &amp; Cognitive OS</p>
            </div>
          </div>

          <!-- Close Button ONLY (Zero download, zero open new tab buttons) -->
          <button id="pdf-modal-close-btn" type="button" class="w-8 h-8 sm:w-9 sm:h-9 rounded-xl flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 shrink-0 cursor-pointer" title="Đóng">
            <i data-lucide="x" class="w-5 h-5"></i>
          </button>
        </div>

        <!-- Viewer Body -->
        <div id="pdf-modal-body" class="relative w-full flex-1 bg-neutral-100 dark:bg-neutral-950 flex flex-col overflow-hidden">
          <iframe id="pdf-modal-iframe" src="" class="w-full flex-1 border-0" allow="fullscreen"></iframe>
          <!-- Protective shield preventing any popout / new tab interaction -->
          <div id="pdf-modal-popout-shield" class="absolute top-0 right-0 w-24 h-16 z-30 pointer-events-auto bg-transparent hidden" title=""></div>
        </div>

      </div>
    `;

    document.body.appendChild(modal);

    const closeBtn = modal.querySelector('#pdf-modal-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', window.closePdfViewerModal);
    }

    modal.addEventListener('click', (e) => {
      if (e.target === modal) window.closePdfViewerModal();
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
    const shield = document.getElementById('pdf-modal-popout-shield');

    if (titleEl) titleEl.textContent = docTitle || 'HAICHAIN Document';

    if (iframe) {
      const cleanPath = pdfUrl.split('#')[0];
      const isAndroid = isAndroidDevice();

      if (isAndroid) {
        // On Android Chrome:
        // Embed Google Docs Viewer with 100% CJK & Asian font fidelity and touch scroll.
        // Shift iframe up by 54px so Google's top toolbar (and its popout icon) is pushed out of view.
        // Apply sandbox (without allow-popups) to prevent any new tabs or windows from ever opening.
        const origin = window.location.origin || 'https://haichain.si';
        const absolutePdfUrl = cleanPath.startsWith('http') ? cleanPath : origin + cleanPath;
        
        iframe.style.marginTop = '-54px';
        iframe.style.height = 'calc(100% + 54px)';
        iframe.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-forms');
        if (shield) shield.classList.remove('hidden');

        iframe.src = 'https://docs.google.com/viewer?embedded=true&url=' + encodeURIComponent(absolutePdfUrl);
      } else {
        // Desktop & iOS browsers natively support PDF iframes with vector scaling
        // #toolbar=0&navpanes=0 hides the PDF toolbar (no download, no print, no new tab)
        iframe.style.marginTop = '0px';
        iframe.style.height = '100%';
        iframe.removeAttribute('sandbox');
        if (shield) shield.classList.add('hidden');

        iframe.src = cleanPath + '#toolbar=0&navpanes=0&view=FitH';
      }
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
      if (iframe) {
        iframe.src = '';
        iframe.style.marginTop = '0px';
        iframe.style.height = '100%';
      }
      const shield = document.getElementById('pdf-modal-popout-shield');
      if (shield) shield.classList.add('hidden');
    }
    document.body.style.overflow = '';
  };

  window.openWhitepaperModal = function () {
    const lang = getCurrentLang();
    const title = getI18nTitle(lang);

    if (lang === 'vi') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_VI.pdf', title);
    } else if (lang === 'zh') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_ZH.pdf', title);
    } else if (lang === 'ko') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_KO.pdf', title);
    } else if (lang === 'es') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_ES.pdf', title);
    } else if (lang === 'fr') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_FR.pdf', title);
    } else if (lang === 'ru') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_RU.pdf', title);
    } else if (lang === 'kk') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_KK.pdf', title);
    } else {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_EN.pdf', title);
    }
  };

  // Delegated Click Handler for all Whitepaper links across the app
  document.addEventListener('click', function (e) {
    const trigger = e.target.closest('a[href="/whitepaper"], a[href="/whitepaper/"], a[href="/whitepaper.pdf"], a[href="/whitepaper-en.pdf"], a[href="/whitepaper-vi.pdf"], a[href="/whitepaper-zh.pdf"], a[href="/whitepaper-ko.pdf"], a[href="/whitepaper-es.pdf"], a[href="/whitepaper-fr.pdf"], a[href="/whitepaper-ru.pdf"], a[href="/whitepaper-kk.pdf"], a[href="/whitepaper-vi"], a[href="/whitepaper-zh"], a[href="/whitepaper-ko"], a[href="/whitepaper-es"], a[href="/whitepaper-fr"], a[href="/whitepaper-ru"], a[href="/whitepaper-kk"], [data-open-whitepaper], #nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link');
    if (trigger) {
      e.preventDefault();
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

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ensurePdfModal);
  } else {
    ensurePdfModal();
  }
})();
