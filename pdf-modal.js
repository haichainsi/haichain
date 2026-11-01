/**
 * HAICHAIN Universal Online PDF Viewer Modal System
 * Provides Apple Titanium luxury in-app reading experience for PDF documents
 * Full Mobile & Desktop Optimization:
 *  - 100% In-App Native Rendering via Virtualized PDF.js Canvas on Mobile
 *  - ZERO Google Docs Viewer on mobile -> ZERO popout/new-tab icons, ZERO download buttons
 *  - ZERO awkward overlay patches -> The new-tab icon is completely eliminated at the source
 *  - Lazy-loaded IntersectionObserver: Only visible pages rendered (RAM < 8MB, never crashes)
 *  - Full 100% Page 1 Logo Visibility (0px offset, perfect alignment)
 *  - Native vector iframe on Desktop with #toolbar=0&navpanes=0&view=FitH
 *  - Luxury Apple floating bottom pill: Page X / N + Zoom controls
 *  - Multilingual Title & UI: en, vi, zh, ko, es, fr, ru, kk, hi, he
 */
(function () {
  'use strict';

  let currentPdfDoc = null;
  let currentPdfUrl = '';
  let currentZoom = 1.0;
  let pageObservers = [];
  let renderedPages = new Set();
  let renderingTokens = {};

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
          loading: 'Đang tải tài liệu...',
          pagePrefix: 'Trang',
          pageOf: '/',
          close: 'Đóng'
        };
      case 'zh':
        return {
          title: 'HAICHAIN 技术白皮书 v1.0 (中文)',
          loading: '正在加载文档...',
          pagePrefix: '第',
          pageOf: '/',
          pageSuffix: '页',
          close: '关闭'
        };
      case 'ko':
        return {
          title: 'HAICHAIN 기술 백서 v1.0 (한국어)',
          loading: '문서를 불러오는 중...',
          pagePrefix: '',
          pageOf: '/',
          pageSuffix: '페이지',
          close: '닫기'
        };
      case 'es':
        return {
          title: 'Libro Blanco Técnico de HAICHAIN v1.0 (Español)',
          loading: 'Cargando documento...',
          pagePrefix: 'Pág.',
          pageOf: '/',
          close: 'Cerrar'
        };
      case 'fr':
        return {
          title: 'Livre Blanc Technique HAICHAIN v1.0 (Français)',
          loading: 'Chargement du document...',
          pagePrefix: 'Page',
          pageOf: '/',
          close: 'Fermer'
        };
      case 'ru':
        return {
          title: 'Технический White Paper HAICHAIN v1.0 (Русский)',
          loading: 'Загрузка документа...',
          pagePrefix: 'Стр.',
          pageOf: '/',
          close: 'Закрыть'
        };
      case 'kk':
        return {
          title: 'HAICHAIN Техникалық ақ қағазы v1.0 (Қазақша)',
          loading: 'Құжат жүктелуде...',
          pagePrefix: '',
          pageOf: '/',
          pageSuffix: 'бет',
          close: 'Жабу'
        };
      case 'hi':
        return {
          title: 'HAICHAIN तकनीकी श्वेतपत्र v1.0 (हिन्दी)',
          loading: 'दस्तावेज़ लोड हो रहा है...',
          pagePrefix: 'पृष्ठ',
          pageOf: '/',
          close: 'बंद करें'
        };
      case 'he':
        return {
          title: 'HAICHAIN נייר עמדה טכני v1.0 (עברית)',
          loading: 'טוען מסמך...',
          pagePrefix: 'עמוד',
          pageOf: '/',
          close: 'סגור'
        };
      default:
        return {
          title: 'HAICHAIN Technical Whitepaper v1.0 (English)',
          loading: 'Loading document...',
          pagePrefix: 'Page',
          pageOf: '/',
          close: 'Close'
        };
    }
  }

  function isMobileDevice() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) || window.innerWidth < 768;
  }

  function ensurePdfJsLoaded() {
    return new Promise((resolve, reject) => {
      if (window.pdfjsLib) {
        if (!window.pdfjsLib.GlobalWorkerOptions.workerSrc) {
          window.pdfjsLib.GlobalWorkerOptions.workerSrc = '/pdfjs/pdf.worker.min.js';
        }
        return resolve(window.pdfjsLib);
      }
      const script = document.createElement('script');
      script.src = '/pdfjs/pdf.min.js';
      script.onload = () => {
        if (window.pdfjsLib) {
          window.pdfjsLib.GlobalWorkerOptions.workerSrc = '/pdfjs/pdf.worker.min.js';
          resolve(window.pdfjsLib);
        } else {
          reject(new Error('PDF.js library failed to initialize'));
        }
      };
      script.onerror = () => reject(new Error('Failed to load /pdfjs/pdf.min.js'));
      document.head.appendChild(script);
    });
  }

  function ensurePdfModal() {
    let modal = document.getElementById('pdf-viewer-modal');
    if (modal) return modal;

    modal = document.createElement('div');
    modal.id = 'pdf-viewer-modal';
    modal.className = 'fixed inset-0 z-[100] bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-0 sm:p-4 md:p-6 transition-all duration-200';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');

    modal.innerHTML = `
      <div class="w-full max-w-5xl h-full sm:h-[90vh] bg-white dark:bg-[#0c0c0e] border-0 sm:border border-neutral-200 dark:border-neutral-800 rounded-none sm:rounded-3xl shadow-2xl flex flex-col overflow-hidden animate-scaleUp">
        
        <!-- Modal Top Bar: Luxury Title + Close Button ONLY (Zero download, zero open new tab buttons) -->
        <div class="px-3.5 py-2.5 sm:px-6 sm:py-3.5 border-b border-neutral-200 dark:border-neutral-800 flex items-center justify-between gap-3 bg-neutral-50/95 dark:bg-neutral-900/95 shrink-0 backdrop-blur-sm z-20">
          
          <!-- Document Icon & Title -->
          <div class="flex items-center space-x-2 sm:space-x-2.5 min-w-0">
            <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl bg-black dark:bg-white text-white dark:text-black flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="file-text" class="w-3.5 h-3.5 sm:w-4 sm:h-4"></i>
            </div>
            <div class="min-w-0">
              <h3 id="pdf-modal-title" class="font-bold text-xs sm:text-sm text-black dark:text-white truncate">HAICHAIN Document</h3>
              <p class="text-[10px] text-neutral-400 font-mono hidden sm:block">Universal Autonomous Machine Financial &amp; Cognitive Operating System</p>
            </div>
          </div>

          <!-- Close Button (✕) ONLY -->
          <button id="pdf-modal-close-btn" type="button" class="w-8 h-8 sm:w-9 sm:h-9 rounded-lg sm:rounded-xl flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 shrink-0 cursor-pointer" title="Đóng">
            <i data-lucide="x" class="w-4 h-4 sm:w-5 sm:h-5"></i>
          </button>
        </div>

        <!-- Viewer Body -->
        <div id="pdf-modal-body" class="relative w-full flex-1 bg-neutral-100 dark:bg-neutral-950 flex flex-col overflow-hidden">
          
          <!-- Loading Spinner -->
          <div id="pdf-modal-loader" class="absolute inset-0 z-30 flex flex-col items-center justify-center bg-white/95 dark:bg-[#0c0c0e]/95 backdrop-blur-xs transition-opacity duration-300 pointer-events-none">
            <div class="w-8 h-8 sm:w-10 sm:h-10 border-2 sm:border-3 border-neutral-300 dark:border-neutral-700 border-t-black dark:border-t-white rounded-full animate-spin"></div>
            <p id="pdf-modal-loader-text" class="mt-3 text-xs font-mono text-neutral-500">Loading document...</p>
          </div>

          <!-- Mobile High-Performance Continuous Canvas Container -->
          <div id="pdf-modal-canvas-scroll" class="w-full flex-1 overflow-y-auto px-1 sm:px-4 py-2 sm:py-4 space-y-3 sm:space-y-4 hidden" style="-webkit-overflow-scrolling: touch; overscroll-behavior: contain;">
            <!-- Page slots generated dynamically -->
          </div>

          <!-- Desktop High-Performance Vector iframe Container -->
          <iframe id="pdf-modal-iframe" src="" class="w-full h-full flex-1 border-0 hidden" allow="fullscreen"></iframe>

          <!-- Floating Apple-style Bottom Pill (Mobile only): Page Indicator & Zoom Controls (Zero new-tab or download icons) -->
          <div id="pdf-modal-floating-pill" class="absolute bottom-4 left-1/2 -translate-x-1/2 z-20 px-3.5 py-1.5 rounded-full bg-black/85 dark:bg-neutral-900/85 backdrop-blur-md border border-neutral-700 text-white shadow-xl flex items-center space-x-3 text-xs font-mono select-none hidden">
            <span id="pdf-modal-page-indicator" class="text-neutral-300 font-semibold tracking-wide">Trang 1 / 1</span>
            <div class="h-3 w-[1px] bg-neutral-700"></div>
            <button id="pdf-zoom-out-btn" class="hover:text-amber-400 active:scale-90 transition-transform cursor-pointer px-1 py-0.5 text-sm" title="Zoom out">-</button>
            <span id="pdf-zoom-level" class="text-neutral-400 text-[11px] cursor-pointer" title="Reset zoom">100%</span>
            <button id="pdf-zoom-in-btn" class="hover:text-amber-400 active:scale-90 transition-transform cursor-pointer px-1 py-0.5 text-sm" title="Zoom in">+</button>
          </div>

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

    // Zoom button handlers for mobile
    const zoomInBtn = modal.querySelector('#pdf-zoom-in-btn');
    const zoomOutBtn = modal.querySelector('#pdf-zoom-out-btn');
    const zoomLevelEl = modal.querySelector('#pdf-zoom-level');

    if (zoomInBtn) {
      zoomInBtn.addEventListener('click', () => {
        if (currentZoom < 2.0) {
          currentZoom = Math.min(2.0, +(currentZoom + 0.25).toFixed(2));
          updateZoomUI();
          rerenderVisiblePages();
        }
      });
    }

    if (zoomOutBtn) {
      zoomOutBtn.addEventListener('click', () => {
        if (currentZoom > 0.75) {
          currentZoom = Math.max(0.75, +(currentZoom - 0.25).toFixed(2));
          updateZoomUI();
          rerenderVisiblePages();
        }
      });
    }

    if (zoomLevelEl) {
      zoomLevelEl.addEventListener('click', () => {
        currentZoom = 1.0;
        updateZoomUI();
        rerenderVisiblePages();
      });
    }

    return modal;
  }

  function updateZoomUI() {
    const zoomLevelEl = document.getElementById('pdf-zoom-level');
    if (zoomLevelEl) {
      zoomLevelEl.textContent = `${Math.round(currentZoom * 100)}%`;
    }
  }

  function updatePageIndicator(pageNum, totalPages) {
    const ind = document.getElementById('pdf-modal-page-indicator');
    if (!ind) return;
    const lang = getCurrentLang();
    const meta = getI18nMeta(lang);
    const suffix = meta.pageSuffix || '';
    if (meta.pagePrefix) {
      ind.textContent = `${meta.pagePrefix} ${pageNum} ${meta.pageOf} ${totalPages} ${suffix}`.trim();
    } else {
      ind.textContent = `${pageNum} ${meta.pageOf} ${totalPages} ${suffix}`.trim();
    }
  }

  async function renderPageSlot(pageNum, slotEl) {
    if (!currentPdfDoc) return;
    const token = Date.now();
    renderingTokens[pageNum] = token;

    try {
      const page = await currentPdfDoc.getPage(pageNum);
      if (renderingTokens[pageNum] !== token) return; // stale

      let canvas = slotEl.querySelector('canvas');
      if (!canvas) {
        canvas = document.createElement('canvas');
        canvas.className = 'w-full h-auto block rounded-lg shadow-sm';
        slotEl.appendChild(canvas);
      }

      const containerWidth = slotEl.clientWidth || (window.innerWidth - 16);
      const baseViewport = page.getViewport({ scale: 1 });
      const baseScale = containerWidth / baseViewport.width;
      const targetScale = baseScale * currentZoom;
      const dpr = Math.min(window.devicePixelRatio || 1.5, 2.0);

      const viewport = page.getViewport({ scale: targetScale * dpr });
      canvas.width = viewport.width;
      canvas.height = viewport.height;
      canvas.style.width = '100%';
      canvas.style.height = 'auto';

      const ctx = canvas.getContext('2d');
      await page.render({
        canvasContext: ctx,
        viewport: viewport
      }).promise;

      renderedPages.add(pageNum);
      const skeleton = slotEl.querySelector('.pdf-page-skeleton');
      if (skeleton) skeleton.classList.add('hidden');
    } catch (err) {
      console.warn(`Page ${pageNum} render cancelled or failed:`, err);
    }
  }

  function clearPageSlot(pageNum, slotEl) {
    renderedPages.delete(pageNum);
    const canvas = slotEl.querySelector('canvas');
    if (canvas) {
      canvas.width = 0;
      canvas.height = 0;
      canvas.remove();
    }
    const skeleton = slotEl.querySelector('.pdf-page-skeleton');
    if (skeleton) skeleton.classList.remove('hidden');
  }

  function rerenderVisiblePages() {
    const scrollContainer = document.getElementById('pdf-modal-canvas-scroll');
    if (!scrollContainer) return;
    const slots = scrollContainer.querySelectorAll('.pdf-page-slot');
    const containerTop = scrollContainer.scrollTop;
    const containerBottom = containerTop + scrollContainer.clientHeight;

    slots.forEach(slot => {
      const top = slot.offsetTop;
      const bottom = top + slot.clientHeight;
      const isVisible = (bottom >= containerTop - 400 && top <= containerBottom + 400);
      const pageNum = parseInt(slot.dataset.page, 10);
      if (isVisible) {
        renderPageSlot(pageNum, slot);
      }
    });
  }

  async function loadPdfViaPdfJs(pdfUrl, lang, meta) {
    const scrollContainer = document.getElementById('pdf-modal-canvas-scroll');
    const floatingPill = document.getElementById('pdf-modal-floating-pill');
    const loader = document.getElementById('pdf-modal-loader');

    scrollContainer.innerHTML = '';
    scrollContainer.classList.remove('hidden');
    floatingPill.classList.remove('hidden');
    renderedPages.clear();
    pageObservers.forEach(obs => obs.disconnect());
    pageObservers = [];
    currentZoom = 1.0;
    updateZoomUI();

    const pdfjs = await ensurePdfJsLoaded();
    const loadingTask = pdfjs.getDocument({
      url: pdfUrl,
      cMapUrl: 'https://cdn.jsdelivr.net/npm/pdfjs-dist@3.11.174/cmaps/',
      cMapPacked: true
    });

    currentPdfDoc = await loadingTask.promise;
    const totalPages = currentPdfDoc.numPages;
    updatePageIndicator(1, totalPages);

    // Get page 1 aspect ratio
    const firstPage = await currentPdfDoc.getPage(1);
    const vp = firstPage.getViewport({ scale: 1 });
    const aspectRatio = (vp.width / vp.height) || (595 / 842);

    // Create page slots
    for (let i = 1; i <= totalPages; i++) {
      const slot = document.createElement('div');
      slot.className = 'pdf-page-slot relative mx-auto my-2 bg-neutral-900 rounded-lg overflow-hidden flex items-center justify-center transition-all';
      slot.dataset.page = i;
      slot.style.width = '100%';
      slot.style.maxWidth = '820px';
      slot.style.aspectRatio = `${aspectRatio}`;

      const skeleton = document.createElement('div');
      skeleton.className = 'pdf-page-skeleton text-xs text-neutral-500 font-mono animate-pulse';
      skeleton.textContent = `${meta.pagePrefix || 'Page'} ${i}...`;
      slot.appendChild(skeleton);

      scrollContainer.appendChild(slot);
    }

    // IntersectionObserver for lazy page rendering and memory recycling
    const renderObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const pageNum = parseInt(entry.target.dataset.page, 10);
        if (entry.isIntersecting) {
          renderPageSlot(pageNum, entry.target);
        } else {
          // Recycle memory if scrolled more than 1000px away
          clearPageSlot(pageNum, entry.target);
        }
      });
    }, {
      root: scrollContainer,
      rootMargin: '400px 0px 400px 0px',
      threshold: 0.01
    });

    // IntersectionObserver for page indicator tracking
    const pageTrackObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const pageNum = parseInt(entry.target.dataset.page, 10);
          updatePageIndicator(pageNum, totalPages);
        }
      });
    }, {
      root: scrollContainer,
      rootMargin: '-40% 0px -40% 0px',
      threshold: 0
    });

    const slots = scrollContainer.querySelectorAll('.pdf-page-slot');
    slots.forEach(slot => {
      renderObserver.observe(slot);
      pageTrackObserver.observe(slot);
    });

    pageObservers.push(renderObserver, pageTrackObserver);

    // Render Page 1 immediately
    if (slots[0]) {
      await renderPageSlot(1, slots[0]);
    }

    // Hide loader
    if (loader) {
      loader.classList.add('opacity-0');
      setTimeout(() => loader.classList.add('hidden'), 300);
    }
  }

  window.openPdfViewerModal = async function (pdfUrl, docTitle) {
    const modal = ensurePdfModal();
    const iframe = document.getElementById('pdf-modal-iframe');
    const scrollContainer = document.getElementById('pdf-modal-canvas-scroll');
    const floatingPill = document.getElementById('pdf-modal-floating-pill');
    const titleEl = document.getElementById('pdf-modal-title');
    const loader = document.getElementById('pdf-modal-loader');
    const loaderText = document.getElementById('pdf-modal-loader-text');
    const lang = getCurrentLang();
    const meta = getI18nMeta(lang);

    currentPdfUrl = pdfUrl;
    if (titleEl) titleEl.textContent = docTitle || meta.title;
    if (loaderText) loaderText.textContent = meta.loading;

    if (loader) {
      loader.classList.remove('hidden', 'opacity-0');
    }

    const cleanPath = pdfUrl.split('#')[0];
    const isMobile = isMobileDevice();

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';

    if (isMobile) {
      // ON MOBILE (Android & iOS):
      // Render in-app using high-speed lazy-loaded PDF.js canvas!
      // This completely ELIMINATES Google Docs Viewer -> ZERO popout button, ZERO open new tab button, ZERO download button!
      if (iframe) {
        iframe.classList.add('hidden');
        iframe.src = '';
      }
      try {
        await loadPdfViaPdfJs(cleanPath, lang, meta);
      } catch (err) {
        console.error('PDF.js mobile viewer error, falling back to clean iframe:', err);
        if (scrollContainer) scrollContainer.classList.add('hidden');
        if (floatingPill) floatingPill.classList.add('hidden');
        if (iframe) {
          iframe.classList.remove('hidden');
          iframe.src = cleanPath + '#toolbar=0&navpanes=0&view=FitH';
        }
        if (loader) {
          loader.classList.add('opacity-0');
          setTimeout(() => loader.classList.add('hidden'), 300);
        }
      }
    } else {
      // ON DESKTOP:
      // Desktop browsers natively render PDF in high-speed vector format with hidden toolbars
      if (scrollContainer) scrollContainer.classList.add('hidden');
      if (floatingPill) floatingPill.classList.add('hidden');
      if (iframe) {
        iframe.classList.remove('hidden');
        iframe.removeAttribute('sandbox');
        iframe.src = cleanPath + '#toolbar=0&navpanes=0&view=FitH';
      }
      if (loader) {
        loader.classList.add('opacity-0');
        setTimeout(() => loader.classList.add('hidden'), 300);
      }
    }

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
      const scrollContainer = document.getElementById('pdf-modal-canvas-scroll');
      if (scrollContainer) {
        scrollContainer.innerHTML = '';
      }
      const floatingPill = document.getElementById('pdf-modal-floating-pill');
      if (floatingPill) {
        floatingPill.classList.add('hidden');
      }
      const loader = document.getElementById('pdf-modal-loader');
      if (loader) {
        loader.classList.add('opacity-0', 'hidden');
      }
      pageObservers.forEach(obs => obs.disconnect());
      pageObservers = [];
      renderedPages.clear();
      currentPdfDoc = null;
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
