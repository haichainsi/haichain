/**
 * HAICHAIN Universal In-App PDF Reader Modal System
 * Provides Apple Titanium luxury reading experience rendered natively via HTML5 Canvas (PDF.js)
 *
 * Ultra-Crisp High-DPI Mobile & Desktop Architecture (v16 Razor-Sharp Typography):
 *  - Zero Pixelation / Zero Shattered Letters: Completely removed nearest-neighbor crisp-edges.
 *  - Official PDF.js High-DPI Transform: Uses exact [outputScale, 0, 0, outputScale, 0, 0] matrix
 *    matching native physical device pixels (DPR 2.0 - 3.0).
 *  - Full Pinch-to-Zoom & Pan: Smooth 2-finger multi-touch pinch zooming (100% to 250%) and double-tap toggle.
 *  - Horizontal Pan Enabled: Uses overflow-x-auto with w-fit container so zoomed pages never get cropped.
 *  - Edge-to-Edge Mobile Layout: Minimal 4px gutter maximizes readable document size by +15%.
 *  - 1-Tap Comfort Zoom: Header zoom button toggles between 100% (Fit) and 140% (Comfort Read).
 *  - 100% Pristine Display: ZERO popout blocker divs, ZERO grey patches, ZERO 'open in new tab' buttons.
 *  - Virtual Memory Pruning: Pages > 3 screens away are freed to guarantee RAM < 18MB at all times.
 *  - 100% Multilingual: en, vi, zh, ko, es, fr, ru, kk, hi, he.
 */
(function () {
  'use strict';

  let currentPdfDoc = null;
  let currentPdfUrl = '';
  let currentScale = 1.0;
  let activePageObserver = null;
  let renderedPages = new Set();
  let renderingTasks = new Map();
  let currentPageIndex = 1;
  let isQueueBusy = false;
  let renderQueue = [];
  let lastTapTime = 0;

  // Touch Pinch-to-Zoom State
  let initialPinchDist = null;
  let initialPinchScale = 1.0;

  // Global cache for pre-loaded documents
  window.__HAICHAIN_PDF_CACHE__ = window.__HAICHAIN_PDF_CACHE__ || {};

  function getCurrentLang() {
    if (window.haichainI18n && typeof window.haichainI18n.getLanguage === 'function') {
      return window.haichainI18n.getLanguage();
    }
    return localStorage.getItem('haichain_lang') || document.documentElement.getAttribute('lang') || 'en';
  }

  function getWhitepaperUrlForLang(lang) {
    const versionParam = '?v=v31_perfect_10lang_audit';
    switch (lang) {
      case 'vi': return '/HAICHAIN_WHITEPAPER_V1.0_VI.pdf' + versionParam;
      case 'zh': return '/HAICHAIN_WHITEPAPER_V1.0_ZH.pdf' + versionParam;
      case 'ko': return '/HAICHAIN_WHITEPAPER_V1.0_KO.pdf' + versionParam;
      case 'es': return '/HAICHAIN_WHITEPAPER_V1.0_ES.pdf' + versionParam;
      case 'fr': return '/HAICHAIN_WHITEPAPER_V1.0_FR.pdf' + versionParam;
      case 'ru': return '/HAICHAIN_WHITEPAPER_V1.0_RU.pdf' + versionParam;
      case 'kk': return '/HAICHAIN_WHITEPAPER_V1.0_KK.pdf' + versionParam;
      case 'hi': return '/HAICHAIN_WHITEPAPER_V1.0_HI.pdf' + versionParam;
      case 'he': return '/HAICHAIN_WHITEPAPER_V1.0_HE.pdf' + versionParam;
      default:   return '/HAICHAIN_WHITEPAPER_V1.0_EN.pdf' + versionParam;
    }
  }

  function getI18nMeta(lang) {
    switch (lang) {
      case 'vi':
        return {
          title: 'Bạch Thư Kỹ Thuật HAICHAIN v1.0 (Tiếng Việt)',
          loading: 'Đang mở tài liệu sắc nét...',
          pagePrefix: 'Trang',
          pageSuffix: 'trang',
          fit: 'Vừa trang',
          comfort: 'Dễ đọc',
          close: 'Đóng'
        };
      case 'zh':
        return {
          title: 'HAICHAIN 技术白皮书 v1.0 (中文)',
          loading: '正在载入高清文档...',
          pagePrefix: '页',
          pageSuffix: '页',
          fit: '适应宽度',
          comfort: '舒适阅读',
          close: '关闭'
        };
      case 'ko':
        return {
          title: 'HAICHAIN 기술 백서 v1.0 (한국어)',
          loading: '고해상도 백서 불러오는 중...',
          pagePrefix: '페이지',
          pageSuffix: '페이지',
          fit: '너비 맞춤',
          comfort: '편안한 읽기',
          close: '닫기'
        };
      case 'es':
        return {
          title: 'Libro Blanco Técnico de HAICHAIN v1.0 (Español)',
          loading: 'Cargando documento en alta definición...',
          pagePrefix: 'Página',
          pageSuffix: 'págs',
          fit: 'Ajustar',
          comfort: 'Lectura',
          close: 'Cerrar'
        };
      case 'fr':
        return {
          title: 'Livre Blanc Technique HAICHAIN v1.0 (Français)',
          loading: 'Chargement en haute définition...',
          pagePrefix: 'Page',
          pageSuffix: 'pages',
          fit: 'Ajuster',
          comfort: 'Confort',
          close: 'Fermer'
        };
      case 'ru':
        return {
          title: 'Технический White Paper HAICHAIN v1.0 (Русский)',
          loading: 'Загрузка документа высокой четкости...',
          pagePrefix: 'Стр.',
          pageSuffix: 'стр.',
          fit: 'По ширине',
          comfort: 'Удобный',
          close: 'Закрыть'
        };
      case 'kk':
        return {
          title: 'HAICHAIN Техникалық ақ қағазы v1.0 (Қазақша)',
          loading: 'Анық құжат жүктелуде...',
          pagePrefix: 'Бет',
          pageSuffix: 'бет',
          fit: 'Сәйкестеу',
          comfort: 'Ыңғайлы',
          close: 'Жабу'
        };
      case 'hi':
        return {
          title: 'HAICHAIN तकनीकी श्वेतपत्र v1.0 (हिन्दी)',
          loading: 'दस्तावेज़ लोड हो रहा है...',
          pagePrefix: 'पृष्ठ',
          pageSuffix: 'पृष्ठ',
          fit: 'फ़िट',
          comfort: 'आसान पाठ',
          close: 'बंद करें'
        };
      case 'he':
        return {
          title: 'HAICHAIN נייר עמדה טכני v1.0 (עברית)',
          loading: 'טוען באיכות גבוהה...',
          pagePrefix: 'עמוד',
          pageSuffix: 'עמודים',
          fit: 'התאם',
          comfort: 'נוח',
          close: 'סגור'
        };
      default:
        return {
          title: 'HAICHAIN Technical Whitepaper v1.0 (English)',
          loading: 'Loading high-definition document...',
          pagePrefix: 'Page',
          pageSuffix: 'pages',
          fit: 'Fit',
          comfort: 'Comfort',
          close: 'Close'
        };
    }
  }

  async function ensurePdfJs() {
    if (window.pdfjsLib) {
      if (!window.pdfjsLib.GlobalWorkerOptions.workerSrc) {
        window.pdfjsLib.GlobalWorkerOptions.workerSrc = '/pdfjs/pdf.worker.min.js';
      }
      return window.pdfjsLib;
    }

    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = '/pdfjs/pdf.min.js';
      script.onload = () => {
        if (window.pdfjsLib) {
          window.pdfjsLib.GlobalWorkerOptions.workerSrc = '/pdfjs/pdf.worker.min.js';
          resolve(window.pdfjsLib);
        } else {
          reject(new Error('PDF.js failed to initialize'));
        }
      };
      script.onerror = () => reject(new Error('Failed to load /pdfjs/pdf.min.js'));
      document.head.appendChild(script);
    });
  }

  // Pre-load & cache active language PDF in background during idle moments
  async function prewarmDocument(url) {
    if (!url || window.__HAICHAIN_PDF_CACHE__[url]) return;
    try {
      const pdfjs = await ensurePdfJs();
      const loadingTask = pdfjs.getDocument({
        url: url,
        cMapPacked: true
      });
      const doc = await loadingTask.promise;
      window.__HAICHAIN_PDF_CACHE__[url] = doc;
    } catch (e) {
      // Quiet fail in background prewarm
    }
  }

  // Precise device pixel ratio for razor-sharp typography without fragmentation
  function getOptimalDpr() {
    const rawDpr = window.devicePixelRatio || 2;
    const isMobile = window.innerWidth < 768;
    if (isMobile) {
      // Mobile screens are dense OLED/Retina; 2.25x - 3.0x guarantees 3 physical pixels per 1pt font stem
      return Math.min(Math.max(rawDpr, 2.25), 3.0);
    }
    return Math.min(Math.max(rawDpr, 1.5), 2.5);
  }

  function getPageWidth() {
    const scrollEl = document.getElementById('pdf-modal-scroll');
    const available = scrollEl ? scrollEl.clientWidth : window.innerWidth;
    const isMobile = window.innerWidth < 768;
    // On mobile, maximize readable width: minimal 4px margins so text is as large as possible
    const padding = isMobile ? 4 : 48;
    const maxDesktopWidth = 880;
    return Math.min(maxDesktopWidth, Math.max(280, available - padding));
  }

  function ensurePdfModal() {
    let modal = document.getElementById('pdf-viewer-modal');
    if (modal) return modal;

    modal = document.createElement('div');
    modal.id = 'pdf-viewer-modal';
    modal.className = 'fixed inset-0 z-[100] bg-black/90 backdrop-blur-md hidden flex items-center justify-center p-0 sm:p-4 md:p-6 transition-all duration-200';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');

    modal.innerHTML = `
      <div class="relative w-full max-w-5xl h-[100dvh] sm:h-[92vh] bg-white dark:bg-[#0c0c0e] sm:border sm:border-neutral-200 dark:sm:border-neutral-800 sm:rounded-3xl shadow-2xl flex flex-col overflow-hidden animate-scaleUp">
        
        <!-- Modal Top Bar: Minimalist Title + Zoom Controls + Close Button ONLY -->
        <div class="px-2 py-2 sm:px-6 sm:py-3 border-b border-neutral-200 dark:border-neutral-800 flex items-center justify-between gap-1.5 sm:gap-4 bg-neutral-50/95 dark:bg-neutral-900/95 shrink-0 backdrop-blur-sm z-20 select-none">
          
          <!-- Document Icon, Title & Page Count Badge -->
          <div class="flex items-center space-x-1.5 sm:space-x-2.5 min-w-0">
            <div class="w-6 h-6 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl bg-black dark:bg-white text-white dark:text-black flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="file-text" class="w-3.5 h-3.5 sm:w-4 sm:h-4"></i>
            </div>
            <div class="min-w-0">
              <div class="flex items-center space-x-1.5 sm:space-x-2">
                <h3 id="pdf-modal-title" class="font-bold text-xs sm:text-sm text-black dark:text-white truncate">HAICHAIN Document</h3>
                <span id="pdf-modal-badge" class="hidden sm:inline-flex px-2 py-0.5 rounded-full text-[10px] font-mono bg-neutral-200 dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 shrink-0"></span>
              </div>
              <p class="text-[10px] text-neutral-400 font-mono hidden sm:block truncate">Universal Autonomous Machine Financial &amp; Cognitive Operating System</p>
            </div>
          </div>

          <!-- Header Controls: Zoom Out / 1-Tap Comfort Zoom / Zoom In + Close (✕) -->
          <div class="flex items-center space-x-1 sm:space-x-1.5 shrink-0">
            <!-- Zoom Out (-) -->
            <button id="pdf-modal-zoom-out" type="button" class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 cursor-pointer" title="Thu nhỏ (-)">
              <i data-lucide="zoom-out" class="w-3.5 h-3.5 sm:w-4 sm:h-4"></i>
            </button>
            
            <!-- 1-Tap Toggle: 100% Fit vs 140% Comfort Read -->
            <button id="pdf-modal-zoom-fit" type="button" class="px-2 h-7 sm:h-8 rounded-lg flex items-center justify-center text-[10px] sm:text-[11px] font-mono font-medium text-neutral-600 dark:text-neutral-300 hover:text-black dark:hover:text-white bg-neutral-200/60 dark:bg-neutral-800/60 hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 cursor-pointer" title="Nhấn để đổi: Vừa trang (100%) / To rõ (140%)">
              <span id="pdf-modal-zoom-label">100%</span>
            </button>

            <!-- Zoom In (+) -->
            <button id="pdf-modal-zoom-in" type="button" class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 cursor-pointer" title="Phóng to (+)">
              <i data-lucide="zoom-in" class="w-3.5 h-3.5 sm:w-4 sm:h-4"></i>
            </button>

            <div class="h-4 w-px bg-neutral-300 dark:bg-neutral-700 mx-0.5 sm:mx-1"></div>

            <!-- Close Button (✕) ONLY -->
            <button id="pdf-modal-close-btn" type="button" class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 shrink-0 cursor-pointer" title="Đóng">
              <i data-lucide="x" class="w-4 h-4 sm:w-4.5 sm:h-4.5"></i>
            </button>
          </div>
        </div>

        <!-- Viewer Scroll Body: Overflow-X-Auto & Pinch-to-Zoom Enabled (ZERO grey boxes, ZERO overlays) -->
        <div id="pdf-modal-scroll" class="relative w-full flex-1 bg-neutral-100 dark:bg-[#111113] overflow-y-auto overflow-x-auto p-1 sm:p-6" style="-webkit-overflow-scrolling: touch; overscroll-behavior: contain; touch-action: pan-x pan-y pinch-zoom;">
          
          <!-- Instant Loading Spinner (Auto-dismisses in <100ms on prewarmed docs) -->
          <div id="pdf-modal-loader" class="absolute inset-0 z-30 flex flex-col items-center justify-center bg-white/95 dark:bg-[#0c0c0e]/95 backdrop-blur-xs transition-opacity duration-200">
            <div class="w-8 h-8 sm:w-10 sm:h-10 border-2 sm:border-3 border-neutral-300 dark:border-neutral-700 border-t-black dark:border-t-white rounded-full animate-spin"></div>
            <p id="pdf-modal-loader-text" class="mt-3 text-xs font-mono text-neutral-500">Loading document...</p>
          </div>

          <!-- Pure Canvas Pages Container (Auto-centers when fit, scrollable when zoomed) -->
          <div id="pdf-pages-container" class="flex flex-col items-center gap-2 sm:gap-5 w-fit min-w-full mx-auto transition-all duration-100"></div>

          <!-- Fallback Container if PDF.js is unavailable -->
          <iframe id="pdf-modal-fallback-iframe" class="w-full h-full flex-1 border-0 hidden"></iframe>
        </div>

        <!-- Floating Sticky Bottom Pill: Current Page & Jump Controls -->
        <div id="pdf-modal-pill" class="absolute bottom-3 sm:bottom-5 left-1/2 -translate-x-1/2 z-20 px-3 sm:px-4 py-1.5 rounded-full bg-black/85 dark:bg-white/95 text-white dark:text-black shadow-2xl backdrop-blur-md flex items-center space-x-2 text-xs font-mono select-none pointer-events-auto transition-transform duration-200">
          <button id="pdf-modal-prev-page" type="button" class="hover:opacity-70 active:scale-90 transition-transform cursor-pointer px-1 py-0.5" title="Trang trước (▲)">
            <i data-lucide="chevron-up" class="w-3.5 h-3.5 sm:w-4 sm:h-4"></i>
          </button>
          <span id="pdf-modal-page-indicator" class="font-bold tracking-wide text-[11px] sm:text-xs">Trang 1 / --</span>
          <button id="pdf-modal-next-page" type="button" class="hover:opacity-70 active:scale-90 transition-transform cursor-pointer px-1 py-0.5" title="Trang sau (▼)">
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 sm:w-4 sm:h-4"></i>
          </button>
        </div>

      </div>
    `;

    document.body.appendChild(modal);

    // Close button
    const closeBtn = modal.querySelector('#pdf-modal-close-btn');
    if (closeBtn) closeBtn.addEventListener('click', window.closePdfViewerModal);

    // Backdrop click
    modal.addEventListener('click', (e) => {
      if (e.target === modal) window.closePdfViewerModal();
    });

    // ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        window.closePdfViewerModal();
      }
    });

    // Zoom Buttons
    const btnZoomOut = modal.querySelector('#pdf-modal-zoom-out');
    const btnZoomFit = modal.querySelector('#pdf-modal-zoom-fit');
    const btnZoomIn = modal.querySelector('#pdf-modal-zoom-in');

    if (btnZoomOut) {
      btnZoomOut.addEventListener('click', () => {
        changeZoom(Math.max(0.75, currentScale - 0.2));
      });
    }

    if (btnZoomFit) {
      btnZoomFit.addEventListener('click', () => {
        // 1-Tap toggle: If 100%, switch to 140% Comfort Read; if >100%, return to 100% Fit
        if (currentScale < 1.2) {
          changeZoom(1.4);
        } else {
          changeZoom(1.0);
        }
      });
    }

    if (btnZoomIn) {
      btnZoomIn.addEventListener('click', () => {
        changeZoom(Math.min(2.5, currentScale + 0.25));
      });
    }

    // Page Jump Buttons in Pill
    const btnPrev = modal.querySelector('#pdf-modal-prev-page');
    const btnNext = modal.querySelector('#pdf-modal-next-page');

    if (btnPrev) {
      btnPrev.addEventListener('click', () => {
        jumpToPage(Math.max(1, currentPageIndex - 1));
      });
    }

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        if (currentPdfDoc) {
          jumpToPage(Math.min(currentPdfDoc.numPages, currentPageIndex + 1));
        }
      });
    }

    // Multitouch Pinch-to-Zoom & Double-Tap on Mobile
    const scrollBody = modal.querySelector('#pdf-modal-scroll');
    if (scrollBody) {
      function getTouchDistance(touches) {
        if (touches.length < 2) return 0;
        const dx = touches[0].clientX - touches[1].clientX;
        const dy = touches[0].clientY - touches[1].clientY;
        return Math.sqrt(dx * dx + dy * dy);
      }

      scrollBody.addEventListener('touchstart', (e) => {
        if (e.touches.length === 2) {
          initialPinchDist = getTouchDistance(e.touches);
          initialPinchScale = currentScale;
        }
      }, { passive: true });

      scrollBody.addEventListener('touchmove', (e) => {
        if (e.touches.length === 2 && initialPinchDist > 0) {
          const dist = getTouchDistance(e.touches);
          if (dist > 0) {
            const factor = dist / initialPinchDist;
            const targetScale = Math.min(2.5, Math.max(0.8, Math.round(initialPinchScale * factor * 10) / 10));
            const label = document.getElementById('pdf-modal-zoom-label');
            if (label) label.textContent = `${Math.round(targetScale * 100)}%`;
          }
        }
      }, { passive: true });

      scrollBody.addEventListener('touchend', (e) => {
        if (initialPinchDist) {
          if (e.touches.length < 2) {
            const label = document.getElementById('pdf-modal-zoom-label');
            if (label && label.textContent) {
              const parsed = parseInt(label.textContent, 10) / 100;
              if (!isNaN(parsed) && Math.abs(parsed - currentScale) >= 0.1) {
                changeZoom(parsed);
              } else {
                if (label) label.textContent = `${Math.round(currentScale * 100)}%`;
              }
            }
            initialPinchDist = null;
          }
        } else {
          // Double-tap handler: 100% <-> 140%
          const currentTime = new Date().getTime();
          const tapLength = currentTime - lastTapTime;
          if (tapLength < 300 && tapLength > 0) {
            e.preventDefault();
            if (currentScale < 1.2) {
              changeZoom(1.4);
            } else {
              changeZoom(1.0);
            }
          }
          lastTapTime = currentTime;
        }
      });
    }

    // Window resize handler: resize slots seamlessly
    window.addEventListener('resize', debounce(() => {
      if (!modal.classList.contains('hidden') && currentPdfDoc) {
        syncSlotDimensions();
      }
    }, 150));

    return modal;
  }

  function debounce(fn, ms) {
    let t;
    return function (...args) {
      clearTimeout(t);
      t = setTimeout(() => fn.apply(this, args), ms);
    };
  }

  function syncSlotDimensions() {
    const container = document.getElementById('pdf-pages-container');
    if (!container || !currentPdfDoc) return;
    const baseW = getPageWidth();
    const targetW = Math.round(baseW * currentScale);

    const slots = container.querySelectorAll('.pdf-page-slot');
    slots.forEach((slot) => {
      const origW = parseFloat(slot.dataset.origW) || 595;
      const origH = parseFloat(slot.dataset.origH) || 842;
      const targetH = Math.round(targetW * (origH / origW));
      slot.style.width = `${targetW}px`;
      slot.style.height = `${targetH}px`;
      slot.style.minHeight = `${targetH}px`;

      const canvas = slot.querySelector('canvas');
      if (canvas && !canvas.classList.contains('hidden')) {
        canvas.style.width = `${targetW}px`;
        canvas.style.height = `${targetH}px`;
      }
    });
  }

  function changeZoom(newScale) {
    if (!currentPdfDoc) return;
    currentScale = Math.round(newScale * 100) / 100;
    const label = document.getElementById('pdf-modal-zoom-label');
    if (label) {
      label.textContent = `${Math.round(currentScale * 100)}%`;
    }

    // Cancel in-flight tasks and clear rendered cache
    renderingTasks.forEach((task) => {
      try { task.cancel(); } catch (err) {}
    });
    renderingTasks.clear();
    renderedPages.clear();
    renderQueue = [];

    syncSlotDimensions();

    // Render immediately visible page
    enqueueRender(currentPageIndex, true);
    if (currentPageIndex + 1 <= currentPdfDoc.numPages) {
      enqueueRender(currentPageIndex + 1, false);
    }
  }

  function jumpToPage(targetPage) {
    const slot = document.getElementById(`pdf-slot-${targetPage}`);
    if (slot) {
      slot.scrollIntoView({ behavior: 'smooth', block: 'start' });
      enqueueRender(targetPage, true);
    }
  }

  function updatePageIndicator(pageNum, total) {
    currentPageIndex = pageNum;
    const lang = getCurrentLang();
    const meta = getI18nMeta(lang);
    const indicator = document.getElementById('pdf-modal-page-indicator');
    if (indicator) {
      if (meta.pagePrefix) {
        indicator.textContent = `${meta.pagePrefix} ${pageNum} / ${total}`;
      } else {
        indicator.textContent = `${pageNum} / ${total} ${meta.pageSuffix || ''}`.trim();
      }
    }
  }

  // Prioritized single-flight render queue (prevents CPU lockup and keeps scrolling 60fps)
  function enqueueRender(pageNum, isPriority) {
    if (!currentPdfDoc || renderedPages.has(pageNum)) return;

    if (isPriority) {
      renderQueue = renderQueue.filter(p => p !== pageNum);
      renderQueue.unshift(pageNum);
    } else {
      if (!renderQueue.includes(pageNum)) {
        renderQueue.push(pageNum);
      }
    }

    processRenderQueue();
  }

  async function processRenderQueue() {
    if (isQueueBusy || renderQueue.length === 0) return;
    isQueueBusy = true;

    const pageNum = renderQueue.shift();
    try {
      await renderPageSlot(pageNum);
    } finally {
      isQueueBusy = false;
      if (renderQueue.length > 0) {
        if (typeof requestAnimationFrame === 'function') {
          requestAnimationFrame(processRenderQueue);
        } else {
          setTimeout(processRenderQueue, 16);
        }
      }
    }
  }

  // Virtual memory cleanup: prune canvases far outside viewport (keeps RAM < 18MB)
  function pruneOffscreenCanvases(currentVisiblePage, totalPages) {
    const preserveRange = 3;
    renderedPages.forEach((pageNum) => {
      if (Math.abs(pageNum - currentVisiblePage) > preserveRange) {
        const slot = document.getElementById(`pdf-slot-${pageNum}`);
        if (slot) {
          const canvas = slot.querySelector('canvas');
          const skeleton = slot.querySelector('.pdf-skeleton');
          if (canvas && !canvas.classList.contains('hidden')) {
            const ctx = canvas.getContext('2d');
            if (ctx) ctx.clearRect(0, 0, canvas.width, canvas.height);
            canvas.width = 0;
            canvas.height = 0;
            canvas.classList.add('hidden');
          }
          if (skeleton) skeleton.classList.remove('hidden');
        }
        renderedPages.delete(pageNum);
      }
    });
  }

  // Official Mozilla High-DPI Vector Rendering Engine
  async function renderPageSlot(pageNum) {
    if (!currentPdfDoc || renderedPages.has(pageNum)) return;

    const slot = document.getElementById(`pdf-slot-${pageNum}`);
    if (!slot) return;

    const canvas = slot.querySelector('canvas');
    const skeleton = slot.querySelector('.pdf-skeleton');
    if (!canvas) return;

    try {
      const page = await currentPdfDoc.getPage(pageNum);
      const unscaled = page.getViewport({ scale: 1.0 });

      slot.dataset.origW = unscaled.width;
      slot.dataset.origH = unscaled.height;

      const baseW = getPageWidth();
      const displayW = Math.max(280, Math.round(baseW * currentScale));
      const baseScale = displayW / unscaled.width;
      const viewport = page.getViewport({ scale: baseScale });

      if (viewport.width <= 0 || viewport.height <= 0) return;

      const outputScale = getOptimalDpr();
      const cssW = Math.floor(viewport.width);
      const cssH = Math.floor(viewport.height);
      const scaledW = Math.floor(viewport.width * outputScale);
      const scaledH = Math.floor(viewport.height * outputScale);

      // Exact pixel matching with outputScale matrix (ZERO aspect ratio drift, ZERO subpixel blur)
      canvas.width = scaledW;
      canvas.height = scaledH;
      canvas.style.width = `${cssW}px`;
      canvas.style.height = `${cssH}px`;
      canvas.style.imageRendering = 'auto';

      slot.style.width = `${cssW}px`;
      slot.style.height = `${cssH}px`;
      slot.style.minHeight = `${cssH}px`;

      const ctx = canvas.getContext('2d', { alpha: false });
      if (ctx) {
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
      }

      // Official high-DPI transform matrix
      const transform = outputScale !== 1 
        ? [outputScale, 0, 0, outputScale, 0, 0] 
        : null;

      const renderTask = page.render({
        canvasContext: ctx,
        viewport: viewport,
        transform: transform,
        intent: 'display'
      });

      renderingTasks.set(pageNum, renderTask);
      await renderTask.promise;
      renderingTasks.delete(pageNum);

      // Successfully rendered
      renderedPages.add(pageNum);
      canvas.classList.remove('hidden');
      if (skeleton) skeleton.classList.add('hidden');

    } catch (err) {
      if (err?.name === 'RenderingCancelledException') return;
      console.warn(`Error rendering page ${pageNum}:`, err);
      renderedPages.delete(pageNum);
    }
  }

  function setupIntersectionObserver(scrollContainer, totalPages) {
    if (activePageObserver) {
      activePageObserver.disconnect();
    }

    activePageObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const pageNum = parseInt(entry.target.dataset.page, 10);
          
          // Priority render for the visible page
          enqueueRender(pageNum, true);

          // Lazy pre-render next page
          if (pageNum + 1 <= totalPages) {
            enqueueRender(pageNum + 1, false);
          }

          updatePageIndicator(pageNum, totalPages);

          // Prune canvases outside active viewport to free RAM
          pruneOffscreenCanvases(pageNum, totalPages);
        }
      });
    }, {
      root: scrollContainer,
      rootMargin: '350px 0px 350px 0px',
      threshold: 0.1
    });

    const slots = scrollContainer.querySelectorAll('.pdf-page-slot');
    slots.forEach((s) => activePageObserver.observe(s));
  }

  window.openPdfViewerModal = async function (pdfUrl, docTitle) {
    const modal = ensurePdfModal();
    const titleEl = document.getElementById('pdf-modal-title');
    const badgeEl = document.getElementById('pdf-modal-badge');
    const loader = document.getElementById('pdf-modal-loader');
    const loaderText = document.getElementById('pdf-modal-loader-text');
    const container = document.getElementById('pdf-pages-container');
    const scrollContainer = document.getElementById('pdf-modal-scroll');
    const fallbackIframe = document.getElementById('pdf-modal-fallback-iframe');
    const lang = getCurrentLang();
    const meta = getI18nMeta(lang);

    currentPdfUrl = pdfUrl;
    currentScale = 1.0;
    renderedPages.clear();
    renderingTasks.clear();
    renderQueue = [];
    currentPageIndex = 1;

    if (titleEl) titleEl.textContent = docTitle || meta.title;
    if (loaderText) loaderText.textContent = meta.loading;
    if (badgeEl) badgeEl.textContent = '';

    const zoomLabel = document.getElementById('pdf-modal-zoom-label');
    if (zoomLabel) zoomLabel.textContent = '100%';

    // Reset viewport and show modal
    if (container) container.innerHTML = '';
    if (fallbackIframe) {
      fallbackIframe.classList.add('hidden');
      fallbackIframe.src = '';
    }
    if (loader) loader.classList.remove('hidden', 'opacity-0');
    if (scrollContainer) {
      scrollContainer.scrollTop = 0;
      scrollContainer.scrollLeft = 0;
    }

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';

    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }

    try {
      let doc = window.__HAICHAIN_PDF_CACHE__[pdfUrl];
      if (!doc) {
        const pdfjs = await ensurePdfJs();
        let fetchUrl = pdfUrl;
        const bust = 'v=v1.2_inst_1793593000000';
        if (!fetchUrl.includes('?')) {
          fetchUrl += '?' + bust;
        } else if (!fetchUrl.includes('v=')) {
          fetchUrl += '&' + bust;
        }
        const loadingTask = pdfjs.getDocument({
          url: fetchUrl,
          cMapPacked: true
        });
        doc = await loadingTask.promise;
        window.__HAICHAIN_PDF_CACHE__[pdfUrl] = doc;
      }

      currentPdfDoc = doc;
      const totalPages = currentPdfDoc.numPages;

      if (badgeEl) {
        badgeEl.textContent = `${totalPages} ${meta.pageSuffix}`;
      }

      updatePageIndicator(1, totalPages);

      const baseW = getPageWidth();

      // Create lightweight placeholder slots for every page with pixel-exact dimensions
      for (let i = 1; i <= totalPages; i++) {
        const slot = document.createElement('div');
        slot.id = `pdf-slot-${i}`;
        slot.className = 'pdf-page-slot relative bg-white dark:bg-[#0c0c0e] shadow-md sm:shadow-xl rounded-md overflow-hidden flex items-center justify-center transition-all duration-150 border border-neutral-200/50 dark:border-neutral-800/50';
        slot.dataset.page = i;
        slot.dataset.origW = '595';
        slot.dataset.origH = '842';
        slot.style.width = `${baseW}px`;
        slot.style.height = `${Math.round(baseW * (842 / 595))}px`;
        slot.style.minHeight = `${Math.round(baseW * (842 / 595))}px`;

        slot.innerHTML = `
          <div class="pdf-skeleton absolute inset-0 flex flex-col items-center justify-center text-neutral-400 bg-neutral-50 dark:bg-neutral-900/60 font-mono text-xs select-none">
            <div class="w-5 h-5 border-2 border-neutral-300 dark:border-neutral-700 border-t-black dark:border-t-white rounded-full animate-spin mb-1.5"></div>
            <span>${meta.pagePrefix || 'Page'} ${i} / ${totalPages}</span>
          </div>
          <canvas class="hidden block shadow-xs select-none" style="pointer-events: none; margin: 0 auto; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;"></canvas>
        `;

        container.appendChild(slot);
      }

      // Hide loader instantly
      if (loader) {
        loader.classList.add('opacity-0');
        setTimeout(() => loader.classList.add('hidden'), 150);
      }

      // Setup virtual observer & kickstart page 1
      setupIntersectionObserver(scrollContainer, totalPages);
      enqueueRender(1, true);
      if (totalPages >= 2) enqueueRender(2, false);

    } catch (err) {
      console.error('PDF.js reader error, falling back to embedded frame:', err);
      if (loader) loader.classList.add('hidden');
      if (fallbackIframe) {
        let fetchUrl = pdfUrl;
        const bust = 'v=v1.2_inst_1793593000000';
        if (!fetchUrl.includes('?')) fetchUrl += '?' + bust;
        fallbackIframe.src = fetchUrl;
        fallbackIframe.classList.remove('hidden');
      }
    }
  };

  window.closePdfViewerModal = function () {
    const modal = document.getElementById('pdf-viewer-modal');
    if (modal) {
      modal.classList.add('hidden');
    }
    document.body.style.overflow = '';

    // Guarantee mobile menu state is fully clean and responsive
    if (typeof window.closeMobileMenu === 'function') {
      try { window.closeMobileMenu(); } catch (_) {}
    } else {
      const mobMenu = document.getElementById('mobile-menu');
      if (mobMenu) {
        mobMenu.classList.remove('menu-open', 'hidden', 'opacity-0', 'opacity-100');
        mobMenu.classList.add('menu-closed');
      }
      const hIcon = document.getElementById('hamburger-icon');
      const cIcon = document.getElementById('close-menu-icon');
      if (hIcon) hIcon.classList.remove('hidden');
      if (cIcon) {
        cIcon.classList.add('hidden');
        cIcon.classList.remove('inline-flex');
      }
      const mobileMenuBtn = document.getElementById('mobile-menu-btn');
      if (mobileMenuBtn) mobileMenuBtn.setAttribute('aria-expanded', 'false');
    }

    // Stop observer & cancel rendering
    if (activePageObserver) {
      activePageObserver.disconnect();
      activePageObserver = null;
    }

    renderingTasks.forEach((task) => {
      try { task.cancel(); } catch (err) {}
    });
    renderingTasks.clear();
    renderedPages.clear();
    renderQueue = [];

    const container = document.getElementById('pdf-pages-container');
    if (container) container.innerHTML = '';
  };

  // Universal In-App Whitepaper Click Handler (100% Prevents Opening in New Tab)
  function handleWhitepaperClick(e, trigger) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }

    // Properly close mobile nav menu and restore hamburger icon
    if (typeof window.closeMobileMenu === 'function') {
      try { window.closeMobileMenu(); } catch (_) {}
    } else {
      const mobMenu = document.getElementById('mobile-menu');
      if (mobMenu) {
        mobMenu.classList.remove('menu-open', 'hidden', 'opacity-0', 'opacity-100');
        mobMenu.classList.add('menu-closed');
      }
      const hIcon = document.getElementById('hamburger-icon');
      const cIcon = document.getElementById('close-menu-icon');
      if (hIcon) hIcon.classList.remove('hidden');
      if (cIcon) {
        cIcon.classList.add('hidden');
        cIcon.classList.remove('inline-flex');
      }
      const mobileMenuBtn = document.getElementById('mobile-menu-btn');
      if (mobileMenuBtn) mobileMenuBtn.setAttribute('aria-expanded', 'false');
    }

    const explicitHref = trigger ? (trigger.getAttribute('data-pdf-url') || trigger.getAttribute('href')) : '';
    if (explicitHref && explicitHref.endsWith('.pdf') && !explicitHref.includes('whitepaper') && !explicitHref.includes('WHITEPAPER')) {
      window.openPdfViewerModal(explicitHref, trigger.getAttribute('title') || 'HAICHAIN Document');
      return;
    }

    const lang = getCurrentLang();
    const pdfUrl = getWhitepaperUrlForLang(lang);
    const meta = getI18nMeta(lang);
    window.openPdfViewerModal(pdfUrl, meta.title);
  }

  // 1. Capture-phase Global Listener: Catches ANY click on any whitepaper link immediately
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest(
      '#nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link, [data-open-whitepaper], [data-pdf-whitepaper], a[href*="whitepaper"], a[href*="WHITEPAPER"]'
    );
    if (trigger) {
      handleWhitepaperClick(e, trigger);
    }
  }, true);

  // 2. Direct Element Binding & Prewarming
  function initPdfTriggers() {
    const selector = '#nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link, [data-open-whitepaper], [data-pdf-whitepaper], a[href*="whitepaper"], a[href*="WHITEPAPER"]';
    document.querySelectorAll(selector).forEach((btn) => {
      if (btn.dataset.pdfBound === 'true') return;
      btn.dataset.pdfBound = 'true';
      btn.addEventListener('click', (e) => handleWhitepaperClick(e, btn));
    });

    checkAutoOpen();

    // Idle background pre-warming: parse Whitepaper so opening takes <10ms
    if (typeof requestIdleCallback === 'function') {
      requestIdleCallback(() => {
        const lang = getCurrentLang();
        prewarmDocument(getWhitepaperUrlForLang(lang));
      }, { timeout: 3000 });
    } else {
      setTimeout(() => {
        const lang = getCurrentLang();
        prewarmDocument(getWhitepaperUrlForLang(lang));
      }, 1500);
    }
  }

  // Auto-open modal if URL specifies ?open_whitepaper=1 or pathname is /whitepaper
  function checkAutoOpen() {
    try {
      const params = new URLSearchParams(window.location.search);
      if (params.get('open_whitepaper') === '1' || window.location.pathname === '/whitepaper') {
        const lang = getCurrentLang();
        const pdfUrl = getWhitepaperUrlForLang(lang);
        const meta = getI18nMeta(lang);
        window.openPdfViewerModal(pdfUrl, meta.title);
      }
    } catch (_) {}
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPdfTriggers);
  } else {
    initPdfTriggers();
  }

  window.addEventListener('haichain-language-changed', () => {
    setTimeout(initPdfTriggers, 50);
  });
})();
