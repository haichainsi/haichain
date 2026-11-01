/**
 * HAICHAIN Universal In-App PDF Reader Modal System
 * Provides Apple Titanium luxury in-app reading experience for original PDF documents
 *
 * Core Architecture (Original Vector PDF Engine):
 *  - 100% Original Vector PDF: Uses direct native vector rendering for flawless, crisp typography. Zero broken characters.
 *  - ZERO "Open in New Tab" or Pop-out buttons:
 *      * Desktop & iOS Safari: Native vector engine with #toolbar=0&navpanes=0&view=FitH.
 *      * Android: High-Fidelity Google Docs Viewer secured with strict sandbox (no allow-popups) + corner shield.
 *  - Clean Minimalist Header: Luxury Document Title + Close (✕) button ONLY. Zero download or external links.
 *  - Multilingual Title & Loading states for all 10 languages: en, vi, zh, ko, es, fr, ru, kk, hi, he.
 */
(function () {
  'use strict';

  function getCurrentLang() {
    if (window.haichainI18n && typeof window.haichainI18n.getLanguage === 'function') {
      return window.haichainI18n.getLanguage();
    }
    return localStorage.getItem('haichain_lang') || document.documentElement.getAttribute('lang') || 'en';
  }

  function getI18nMeta(lang) {
    switch (lang) {
      case 'vi':
        return {
          title: 'Bạch Thư Kỹ Thuật HAICHAIN v1.0 (Tiếng Việt)',
          loading: 'Đang mở tài liệu gốc sắc nét...',
          close: 'Đóng'
        };
      case 'zh':
        return {
          title: 'HAICHAIN 技术白皮书 v1.0 (中文)',
          loading: '正在载入高清原版文档...',
          close: '关闭'
        };
      case 'ko':
        return {
          title: 'HAICHAIN 기술 백서 v1.0 (한국어)',
          loading: '고해상도 원본 백서를 불러오는 중...',
          close: '닫기'
        };
      case 'es':
        return {
          title: 'Libro Blanco Técnico de HAICHAIN v1.0 (Español)',
          loading: 'Cargando documento original en alta definición...',
          close: 'Cerrar'
        };
      case 'fr':
        return {
          title: 'Livre Blanc Technique HAICHAIN v1.0 (Français)',
          loading: 'Chargement du document original haute définition...',
          close: 'Fermer'
        };
      case 'ru':
        return {
          title: 'Технический White Paper HAICHAIN v1.0 (Русский)',
          loading: 'Загрузка оригинального документа высокого качества...',
          close: 'Закрыть'
        };
      case 'kk':
        return {
          title: 'HAICHAIN Техникалық ақ қағазы v1.0 (Қазақша)',
          loading: 'Түпнұсқа анық құжат жүктелуде...',
          close: 'Жабу'
        };
      case 'hi':
        return {
          title: 'HAICHAIN तकनीकी श्वेतपत्र v1.0 (हिन्दी)',
          loading: 'मूल उच्च-रिज़ॉल्यूशन दस्तावेज़ लोड हो रहा है...',
          close: 'बंद करें'
        };
      case 'he':
        return {
          title: 'HAICHAIN נייר עמדה טכני v1.0 (עברית)',
          loading: 'טוען מסמך מקורי ברזולוציה גבוהה...',
          close: 'סגור'
        };
      default:
        return {
          title: 'HAICHAIN Technical Whitepaper v1.0 (English)',
          loading: 'Loading high-definition original document...',
          close: 'Close'
        };
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
    modal.className = 'fixed inset-0 z-[100] bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-1 sm:p-4 md:p-6 transition-all duration-200';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');

    modal.innerHTML = `
      <div class="relative w-full max-w-5xl h-[96dvh] sm:h-[90vh] bg-white dark:bg-[#0c0c0e] border border-neutral-200 dark:border-neutral-800 rounded-2xl sm:rounded-3xl shadow-2xl flex flex-col overflow-hidden animate-scaleUp">
        
        <!-- Modal Top Bar: Minimalist Title + Close Button ONLY -->
        <div class="px-3 py-2.5 sm:px-6 sm:py-3.5 border-b border-neutral-200 dark:border-neutral-800 flex items-center justify-between gap-3 bg-neutral-50/95 dark:bg-neutral-900/95 shrink-0 backdrop-blur-sm z-20">
          
          <!-- Document Icon & Title -->
          <div class="flex items-center space-x-2 sm:space-x-2.5 min-w-0">
            <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl bg-black dark:bg-white text-white dark:text-black flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="file-text" class="w-3.5 h-3.5 sm:w-4 sm:h-4"></i>
            </div>
            <div class="min-w-0">
              <h3 id="pdf-modal-title" class="font-bold text-xs sm:text-sm text-black dark:text-white truncate">HAICHAIN Document</h3>
              <p class="text-[10px] text-neutral-400 font-mono hidden sm:block truncate">Universal Autonomous Machine Financial &amp; Cognitive Operating System</p>
            </div>
          </div>

          <!-- Close Button (✕) ONLY -->
          <button id="pdf-modal-close-btn" type="button" class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 shrink-0 cursor-pointer" title="Đóng">
            <i data-lucide="x" class="w-4 h-4 sm:w-5 sm:h-5"></i>
          </button>
        </div>

        <!-- Viewer Body: Renders the ORIGINAL PDF directly via high-speed native vector engine -->
        <div id="pdf-modal-body" class="relative w-full flex-1 bg-neutral-100 dark:bg-neutral-950 flex flex-col overflow-hidden" style="-webkit-overflow-scrolling: touch; overscroll-behavior: contain;">
          
          <!-- Sleek Loading Spinner -->
          <div id="pdf-modal-loader" class="absolute inset-0 z-30 flex flex-col items-center justify-center bg-white/95 dark:bg-[#0c0c0e]/95 backdrop-blur-xs transition-opacity duration-200">
            <div class="w-8 h-8 sm:w-10 sm:h-10 border-2 sm:border-3 border-neutral-300 dark:border-neutral-700 border-t-black dark:border-t-white rounded-full animate-spin"></div>
            <p id="pdf-modal-loader-text" class="mt-3 text-xs font-mono text-neutral-500">Loading original PDF...</p>
          </div>

          <!-- Protective Pop-out Blocker Shield (Strictly neutralizes any corner pop-out button on mobile) -->
          <div id="pdf-modal-popout-blocker" class="absolute top-0 right-0 w-[80px] h-[58px] z-20 pointer-events-auto bg-[#323639] hidden" style="touch-action: none;"></div>

          <!-- Direct Vector PDF Iframe -->
          <iframe id="pdf-modal-iframe" src="" class="w-full h-full flex-1 border-0" allow="fullscreen"></iframe>
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

    const blocker = modal.querySelector('#pdf-modal-popout-blocker');
    if (blocker) {
      blocker.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); });
      blocker.addEventListener('touchstart', (e) => { e.preventDefault(); e.stopPropagation(); }, { passive: false });
    }

    const iframe = modal.querySelector('#pdf-modal-iframe');
    const loader = modal.querySelector('#pdf-modal-loader');
    if (iframe && loader) {
      iframe.addEventListener('load', function () {
        loader.classList.add('opacity-0');
        setTimeout(() => {
          loader.classList.add('hidden');
        }, 200);
      });
    }

    return modal;
  }

  window.openPdfViewerModal = function (pdfUrl, docTitle) {
    const modal = ensurePdfModal();
    const iframe = document.getElementById('pdf-modal-iframe');
    const titleEl = document.getElementById('pdf-modal-title');
    const loader = document.getElementById('pdf-modal-loader');
    const loaderText = document.getElementById('pdf-modal-loader-text');
    const blocker = document.getElementById('pdf-modal-popout-blocker');
    const lang = getCurrentLang();
    const meta = getI18nMeta(lang);

    if (titleEl) titleEl.textContent = docTitle || meta.title;
    if (loaderText) loaderText.textContent = meta.loading;

    // Reset and show loader
    if (loader) {
      loader.classList.remove('hidden', 'opacity-0');
    }

    if (iframe) {
      const cleanPath = pdfUrl.split('#')[0];
      const isAndroid = isAndroidDevice();

      if (isAndroid) {
        // Android Chrome / Mobile: Route via Google Docs Viewer for 100% CJK & Asian vector font clarity
        const origin = window.location.origin || 'https://haichain.si';
        const absolutePdfUrl = cleanPath.startsWith('http') ? cleanPath : origin + cleanPath;
        
        // Strict Sandbox: strictly omit allow-popups and allow-popups-to-escape-sandbox
        iframe.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-forms');
        if (blocker) blocker.classList.remove('hidden');
        
        iframe.src = 'https://docs.google.com/viewer?embedded=true&url=' + encodeURIComponent(absolutePdfUrl);
      } else {
        // Desktop & iOS Safari: High-speed native vector rendering of the original PDF
        // #toolbar=0&navpanes=0 hides browser toolbars, delivering 100% crisp original vector display
        iframe.removeAttribute('sandbox');
        if (blocker) blocker.classList.add('hidden');
        iframe.src = cleanPath + '#toolbar=0&navpanes=0&view=FitH';
      }

      // Safety timeout: auto-hide loader after 3s if iframe onload doesn't fire due to sandbox
      setTimeout(() => {
        if (loader && !loader.classList.contains('opacity-0')) {
          loader.classList.add('opacity-0');
          setTimeout(() => loader.classList.add('hidden'), 200);
        }
      }, 3000);
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
      }
      const loader = document.getElementById('pdf-modal-loader');
      if (loader) {
        loader.classList.add('opacity-0', 'hidden');
      }
      const blocker = document.getElementById('pdf-modal-popout-blocker');
      if (blocker) {
        blocker.classList.add('hidden');
      }
    }
    document.body.style.overflow = '';
  };

  window.openWhitepaperModal = function () {
    const lang = getCurrentLang();
    const meta = getI18nMeta(lang);

    if (lang === 'vi') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_VI.pdf', meta.title);
    } else if (lang === 'zh') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_ZH.pdf', meta.title);
    } else if (lang === 'ko') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_KO.pdf', meta.title);
    } else if (lang === 'es') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_ES.pdf', meta.title);
    } else if (lang === 'fr') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_FR.pdf', meta.title);
    } else if (lang === 'ru') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_RU.pdf', meta.title);
    } else if (lang === 'kk') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_KK.pdf', meta.title);
    } else if (lang === 'hi') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_HI.pdf', meta.title);
    } else if (lang === 'he') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_HE.pdf', meta.title);
    } else {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_EN.pdf', meta.title);
    }
  };

  // Delegated Click Handler for all Whitepaper links across the app
  document.addEventListener('click', function (e) {
    const trigger = e.target.closest('a[href="/whitepaper"], a[href="/whitepaper/"], a[href="/whitepaper.pdf"], a[href="/whitepaper-en.pdf"], a[href="/whitepaper-vi.pdf"], a[href="/whitepaper-zh.pdf"], a[href="/whitepaper-ko.pdf"], a[href="/whitepaper-es.pdf"], a[href="/whitepaper-fr.pdf"], a[href="/whitepaper-ru.pdf"], a[href="/whitepaper-kk.pdf"], a[href="/whitepaper-hi.pdf"], a[href="/whitepaper-he.pdf"], a[href="/whitepaper-vi"], a[href="/whitepaper-zh"], a[href="/whitepaper-ko"], a[href="/whitepaper-es"], a[href="/whitepaper-fr"], a[href="/whitepaper-ru"], a[href="/whitepaper-kk"], a[href="/whitepaper-hi"], a[href="/whitepaper-he"], [data-open-whitepaper], #nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link');
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
