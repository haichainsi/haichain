/**
 * HAICHAIN Universal Online PDF Viewer Modal System
 * Provides Apple Titanium luxury in-app reading experience for PDF documents
 * Full Mobile Optimization:
 *  - High-DPI Canvas Rendering via PDF.js on mobile (No new tabs, no blank iframes, no forced downloads)
 *  - Continuous vertical touch scrolling through all pages
 *  - Interactive Zoom Controls: [-], [100% Fit], [+], and Double-Tap to Zoom
 *  - Desktop Native iframe with toolbar + FitH for high performance
 *  - Multilingual Support: English (en), Vietnamese (vi), Chinese (zh), Korean (ko)
 */
(function () {
  'use strict';

  window.__HAICHAIN_PDF_MODAL_ADVANCED__ = true;

  let currentPdfDoc = null;
  let currentPdfUrl = '';
  let currentZoom = 1.0;
  let isRendering = false;
  let renderToken = 0;

  function getCurrentLang() {
    if (window.haichainI18n && typeof window.haichainI18n.getLanguage === 'function') {
      return window.haichainI18n.getLanguage();
    }
    return localStorage.getItem('haichain_lang') || document.documentElement.getAttribute('lang') || 'en';
  }

  function getI18nStrings(lang) {
    switch (lang) {
      case 'vi':
        return {
          readerBadge: 'ĐỌC TRỰC TIẾP',
          pageSuffix: 'trang',
          zoomOut: 'Thu nhỏ (-)',
          zoomReset: 'Vừa màn hình (100%)',
          zoomIn: 'Phóng to (+)',
          openNewTab: 'Mở toàn màn hình',
          download: 'Tải PDF về máy',
          close: 'Đóng',
          loading: 'Đang hiển thị tài liệu trực tiếp...',
          hintScroll: 'Vuốt để cuộn trang',
          hintZoom: 'Chạm đúp để phóng to / vừa màn hình',
          whitepaperTitle: 'Bạch Thư Kỹ Thuật HAICHAIN v1.0 (Tiếng Việt)',
          saftTitle: 'Hợp Đồng SAFT Pre-Seed HAICHAIN (Song Ngữ VI & EN)',
          memoTitle: 'Bản Tóm Tắt Chiến Lược 1 Trang - Vòng Pre-Seed'
        };
      case 'zh':
        return {
          readerBadge: '在线阅读',
          pageSuffix: '页',
          zoomOut: '缩小 (-)',
          zoomReset: '适应屏幕 (100%)',
          zoomIn: '放大 (+)',
          openNewTab: '全屏在新标签页打开',
          download: '下载 PDF 文件',
          close: '关闭',
          loading: '正在在线加载文档...',
          hintScroll: '上下滑动浏览页面',
          hintZoom: '双击放大 / 适应屏幕',
          whitepaperTitle: 'HAICHAIN 技术白皮书 v1.0 (中文)',
          saftTitle: 'HAICHAIN 种子轮 SAFT 协议 (双语)',
          memoTitle: 'HAICHAIN 种子轮 1页核心备忘录'
        };
      case 'ko':
        return {
          readerBadge: '온라인 리더',
          pageSuffix: '페이지',
          zoomOut: '축소 (-)',
          zoomReset: '화면 맞춤 (100%)',
          zoomIn: '확대 (+)',
          openNewTab: '새 탭에서 전체 화면 보기',
          download: 'PDF 다운로드',
          close: '닫기',
          loading: '온라인으로 문서를 로딩 중입니다...',
          hintScroll: '위아래로 스크롤하여 페이지 보기',
          hintZoom: '더블 탭하여 확대 / 화면 맞춤',
          whitepaperTitle: 'HAICHAIN 기술 백서 v1.0 (한국어)',
          saftTitle: 'HAICHAIN 프리시드 SAFT 계약서',
          memoTitle: 'HAICHAIN 1페이지 투자 메모'
        };
      default:
        return {
          readerBadge: 'ONLINE READER',
          pageSuffix: 'pages',
          zoomOut: 'Zoom Out (-)',
          zoomReset: 'Fit Screen (100%)',
          zoomIn: 'Zoom In (+)',
          openNewTab: 'Open in New Tab',
          download: 'Download PDF',
          close: 'Close',
          loading: 'Rendering document online...',
          hintScroll: 'Swipe to scroll pages',
          hintZoom: 'Double-tap to zoom / fit screen',
          whitepaperTitle: 'HAICHAIN Technical Whitepaper v1.0 (English)',
          saftTitle: 'HAICHAIN Pre-Seed SAFT Agreement (Bilingual)',
          memoTitle: 'HAICHAIN Pre-Seed 1-Pager Investment Teaser Memo'
        };
    }
  }

  function isMobileDevice() {
    const ua = navigator.userAgent || navigator.vendor || window.opera || '';
    const isMobileUA = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(ua);
    const isSmallScreen = window.innerWidth <= 820;
    const isTouch = (navigator.maxTouchPoints > 0) || ('ontouchstart' in window);
    return isMobileUA || (isSmallScreen && isTouch);
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
          reject(new Error('PDF.js failed to initialize'));
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

    const i18n = getI18nStrings(getCurrentLang());

    modal.innerHTML = `
      <div class="w-full h-full sm:h-[90vh] sm:max-w-5xl bg-[#09090b] text-neutral-100 sm:border border-neutral-800 sm:rounded-3xl shadow-2xl flex flex-col overflow-hidden animate-scaleUp">
        
        <!-- Modal Top Navigation Bar -->
        <div class="px-3 py-2.5 sm:px-6 sm:py-3.5 border-b border-neutral-800 flex items-center justify-between gap-2 bg-[#121215]/95 shrink-0 backdrop-blur-sm z-20">
          
          <!-- Document Badge & Title -->
          <div class="flex items-center space-x-2.5 min-w-0">
            <div class="w-8 h-8 rounded-xl bg-white text-black flex items-center justify-center shrink-0 shadow-sm">
              <i data-lucide="file-text" class="w-4 h-4"></i>
            </div>
            <div class="min-w-0">
              <h3 id="pdf-modal-title" class="font-bold text-xs sm:text-sm text-white truncate max-w-[140px] xs:max-w-[200px] sm:max-w-md">Document Viewer</h3>
              <div class="flex items-center space-x-2">
                <span class="text-[10px] text-emerald-400 font-mono flex items-center space-x-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse inline-block"></span>
                  <span id="pdf-modal-reader-badge">${i18n.readerBadge}</span>
                </span>
                <span id="pdf-modal-page-count" class="text-[10px] text-neutral-400 font-mono hidden xs:inline"></span>
              </div>
            </div>
          </div>

          <!-- Controls: Zoom Toolbar + Actions -->
          <div class="flex items-center space-x-1 sm:space-x-2 shrink-0">
            
            <!-- Mobile/Desktop Zoom Controls -->
            <div id="pdf-modal-zoom-group" class="flex items-center bg-neutral-800/90 border border-neutral-700/60 rounded-xl p-0.5 text-xs font-mono">
              <button id="pdf-modal-zoom-out" type="button" class="w-7 h-7 flex items-center justify-center rounded-lg hover:bg-neutral-700 text-neutral-300 transition-all active:scale-90" title="${i18n.zoomOut}">
                <i data-lucide="minus" class="w-3.5 h-3.5"></i>
              </button>
              <button id="pdf-modal-zoom-reset" type="button" class="px-2 h-7 flex items-center justify-center rounded-lg hover:bg-neutral-700 text-[11px] text-neutral-200 font-semibold transition-all active:scale-95" title="${i18n.zoomReset}">
                <span id="pdf-modal-zoom-label">100%</span>
              </button>
              <button id="pdf-modal-zoom-in" type="button" class="w-7 h-7 flex items-center justify-center rounded-lg hover:bg-neutral-700 text-neutral-300 transition-all active:scale-90" title="${i18n.zoomIn}">
                <i data-lucide="plus" class="w-3.5 h-3.5"></i>
              </button>
            </div>

            <!-- External Fullscreen New Tab Button -->
            <a id="pdf-modal-open-new-tab" href="#" target="_blank" class="w-8 h-8 rounded-xl flex items-center justify-center text-neutral-400 hover:text-white hover:bg-neutral-800 transition-colors active:scale-95" title="${i18n.openNewTab}">
              <i data-lucide="external-link" class="w-4 h-4"></i>
            </a>

            <!-- Download Button -->
            <a id="pdf-modal-download-btn" href="#" download class="w-8 h-8 rounded-xl flex items-center justify-center text-neutral-400 hover:text-white hover:bg-neutral-800 transition-colors active:scale-95" title="${i18n.download}">
              <i data-lucide="download" class="w-4 h-4"></i>
            </a>

            <!-- Close Button (Large 36x36 for easy finger tap) -->
            <button id="pdf-modal-close-btn" type="button" class="w-8 h-8 sm:w-9 sm:h-9 rounded-xl flex items-center justify-center text-neutral-400 hover:text-white hover:bg-neutral-800 transition-colors active:scale-95" title="${i18n.close}">
              <i data-lucide="x" class="w-5 h-5"></i>
            </button>
          </div>
        </div>

        <!-- Viewer Body -->
        <div id="pdf-modal-body" class="relative w-full flex-1 bg-[#141418] flex flex-col overflow-hidden">
          
          <!-- Mobile & Universal High-DPI Canvas Stream Container -->
          <div id="pdf-modal-canvas-container" oncontextmenu="return false;" class="w-full flex-1 overflow-y-auto overflow-x-auto touch-pan-y flex flex-col items-center py-4 px-2 sm:px-4 space-y-4 sm:space-y-6 select-none">
            <!-- Dynamically rendered pages go here -->
          </div>

          <!-- Desktop Native iframe -->
          <iframe id="pdf-modal-iframe" src="" class="w-full flex-1 border-0 hidden" allow="fullscreen"></iframe>

          <!-- Loading State Overlay -->
          <div id="pdf-modal-loader" class="absolute inset-0 bg-[#09090b]/90 backdrop-blur-xs flex flex-col items-center justify-center z-30 text-neutral-300 transition-opacity">
            <div class="w-10 h-10 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mb-3"></div>
            <p id="pdf-modal-loader-text" class="text-xs font-mono font-semibold text-neutral-200">${i18n.loading}</p>
            <p class="text-[10px] text-neutral-500 font-sans mt-1">HAICHAIN Mobile High-Precision Vector Engine</p>
          </div>

        </div>

        <!-- Mobile Touch Hint Footer -->
        <div id="pdf-modal-mobile-footer" class="py-1.5 px-4 bg-[#0d0d10] border-t border-neutral-800/80 text-[10px] font-mono text-neutral-500 flex items-center justify-between sm:hidden shrink-0">
          <span id="pdf-modal-hint-scroll">${i18n.hintScroll}</span>
          <span id="pdf-modal-hint-zoom">${i18n.hintZoom}</span>
        </div>

      </div>
    `;

    document.body.appendChild(modal);

    // Event listeners
    const closeBtn = modal.querySelector('#pdf-modal-close-btn');
    if (closeBtn) closeBtn.addEventListener('click', window.closePdfViewerModal);

    modal.addEventListener('click', (e) => {
      if (e.target === modal) window.closePdfViewerModal();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        window.closePdfViewerModal();
      }
    });

    // Zoom button listeners
    const zoomInBtn = modal.querySelector('#pdf-modal-zoom-in');
    const zoomOutBtn = modal.querySelector('#pdf-modal-zoom-out');
    const zoomResetBtn = modal.querySelector('#pdf-modal-zoom-reset');

    if (zoomInBtn) {
      zoomInBtn.addEventListener('click', () => {
        if (currentZoom < 2.5) {
          currentZoom = Math.min(2.5, currentZoom + 0.25);
          updateZoomUI();
          renderCanvasPages();
        }
      });
    }

    if (zoomOutBtn) {
      zoomOutBtn.addEventListener('click', () => {
        if (currentZoom > 0.6) {
          currentZoom = Math.max(0.6, currentZoom - 0.25);
          updateZoomUI();
          renderCanvasPages();
        }
      });
    }

    if (zoomResetBtn) {
      zoomResetBtn.addEventListener('click', () => {
        currentZoom = 1.0;
        updateZoomUI();
        renderCanvasPages();
      });
    }

    // Double-tap on mobile canvas container to zoom / toggle fit
    let lastTapTime = 0;
    const canvasContainer = modal.querySelector('#pdf-modal-canvas-container');
    if (canvasContainer) {
      canvasContainer.addEventListener('touchend', (e) => {
        const currentTime = new Date().getTime();
        const tapLength = currentTime - lastTapTime;
        if (tapLength < 300 && tapLength > 0) {
          e.preventDefault();
          currentZoom = currentZoom === 1.0 ? 1.5 : 1.0;
          updateZoomUI();
          renderCanvasPages();
        }
        lastTapTime = currentTime;
      });
    }

    return modal;
  }

  function updateZoomUI() {
    const label = document.getElementById('pdf-modal-zoom-label');
    if (label) {
      label.textContent = `${Math.round(currentZoom * 100)}%`;
    }
  }

  async function renderCanvasPages() {
    if (!currentPdfDoc) return;
    const token = ++renderToken;
    const container = document.getElementById('pdf-modal-canvas-container');
    const loader = document.getElementById('pdf-modal-loader');
    if (!container) return;

    if (loader) loader.classList.remove('hidden');

    const totalPages = currentPdfDoc.numPages;
    const containerWidth = Math.max(280, container.clientWidth - 16);
    const dpr = window.devicePixelRatio || 1.5;

    // Remove obsolete pages
    while (container.children.length > totalPages) {
      container.removeChild(container.lastChild);
    }

    for (let pageNum = 1; pageNum <= totalPages; pageNum++) {
      if (token !== renderToken) return;

      let pageWrapper = container.querySelector(`[data-page-num="${pageNum}"]`);
      if (!pageWrapper) {
        pageWrapper = document.createElement('div');
        pageWrapper.className = 'pdf-page-wrapper relative bg-white shadow-xl rounded-sm sm:rounded-md overflow-hidden flex flex-col items-center transition-transform origin-top';
        pageWrapper.setAttribute('data-page-num', pageNum);
        
        const canvas = document.createElement('canvas');
        canvas.className = 'block max-w-full';
        canvas.style.display = 'block';
        pageWrapper.appendChild(canvas);

        const pageLabel = document.createElement('div');
        pageLabel.className = 'py-1 text-[10px] font-mono text-neutral-400 bg-neutral-900 w-full text-center border-t border-neutral-800';
        pageLabel.textContent = `${pageNum} / ${totalPages}`;
        pageWrapper.appendChild(pageLabel);

        container.appendChild(pageWrapper);
      }

      const page = await currentPdfDoc.getPage(pageNum);
      if (token !== renderToken) return;

      const unscaledViewport = page.getViewport({ scale: 1.0 });
      const baseScale = (containerWidth / unscaledViewport.width);
      const targetScale = baseScale * currentZoom;
      const viewport = page.getViewport({ scale: targetScale });

      const canvas = pageWrapper.querySelector('canvas');
      const outputScale = Math.min(dpr, 2.5);

      canvas.width = Math.floor(viewport.width * outputScale);
      canvas.height = Math.floor(viewport.height * outputScale);
      canvas.style.width = `${Math.floor(viewport.width)}px`;
      canvas.style.height = `${Math.floor(viewport.height)}px`;

      const ctx = canvas.getContext('2d', { alpha: false });
      ctx.imageSmoothingEnabled = true;
      ctx.imageSmoothingQuality = 'high';

      const renderContext = {
        canvasContext: ctx,
        transform: outputScale !== 1 ? [outputScale, 0, 0, outputScale, 0, 0] : null,
        viewport: viewport
      };

      await page.render(renderContext).promise;
    }

    if (token === renderToken && loader) {
      loader.classList.add('hidden');
    }
  }

  window.openPdfViewerModal = async function (pdfUrl, docTitle) {
    const modal = ensurePdfModal();
    const iframe = document.getElementById('pdf-modal-iframe');
    const canvasContainer = document.getElementById('pdf-modal-canvas-container');
    const titleEl = document.getElementById('pdf-modal-title');
    const pageCountEl = document.getElementById('pdf-modal-page-count');
    const loader = document.getElementById('pdf-modal-loader');
    const loaderText = document.getElementById('pdf-modal-loader-text');
    const zoomGroup = document.getElementById('pdf-modal-zoom-group');
    const newTabEl = document.getElementById('pdf-modal-open-new-tab');
    const downloadEl = document.getElementById('pdf-modal-download-btn');
    const readerBadge = document.getElementById('pdf-modal-reader-badge');
    const hintScroll = document.getElementById('pdf-modal-hint-scroll');
    const hintZoom = document.getElementById('pdf-modal-hint-zoom');

    const lang = getCurrentLang();
    const i18n = getI18nStrings(lang);

    // Update dynamic localized labels
    if (readerBadge) readerBadge.textContent = i18n.readerBadge;
    if (loaderText) loaderText.textContent = i18n.loading;
    if (hintScroll) hintScroll.textContent = i18n.hintScroll;
    if (hintZoom) hintZoom.textContent = i18n.hintZoom;
    if (newTabEl) {
      newTabEl.href = pdfUrl;
      newTabEl.title = i18n.openNewTab;
    }
    if (downloadEl) {
      downloadEl.href = pdfUrl;
      downloadEl.download = pdfUrl.split('/').pop().split('?')[0];
      downloadEl.title = i18n.download;
    }

    currentPdfUrl = pdfUrl;
    currentZoom = 1.0;
    updateZoomUI();

    if (titleEl) titleEl.textContent = docTitle || 'HAICHAIN Document';
    if (pageCountEl) pageCountEl.textContent = '';
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    if (loader) loader.classList.remove('hidden');

    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }

    const mobile = isMobileDevice();

    if (mobile) {
      // ON MOBILE: Always use PDF.js high-DPI canvas view inside the modal
      if (iframe) iframe.classList.add('hidden');
      if (canvasContainer) canvasContainer.classList.remove('hidden');
      if (zoomGroup) zoomGroup.classList.remove('hidden');

      try {
        const pdfjs = await ensurePdfJsLoaded();
        const loadingTask = pdfjs.getDocument({
          url: pdfUrl,
          cMapUrl: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/cmaps/',
          cMapPacked: true
        });
        currentPdfDoc = await loadingTask.promise;
        if (pageCountEl) {
          pageCountEl.textContent = `• ${currentPdfDoc.numPages} ${i18n.pageSuffix}`;
        }
        await renderCanvasPages();
      } catch (err) {
        console.error('Failed to load PDF via PDF.js on mobile:', err);
        // Fallback: try iframe
        if (iframe) {
          iframe.classList.remove('hidden');
          iframe.src = pdfUrl.split('#')[0] + '#toolbar=0&navpanes=0&view=FitH';
        }
        if (loader) loader.classList.add('hidden');
      }
    } else {
      // ON DESKTOP:
      // Desktop browsers natively support PDF iframes with full features
      if (canvasContainer) canvasContainer.classList.add('hidden');
      if (zoomGroup) zoomGroup.classList.add('hidden');
      if (iframe) {
        iframe.classList.remove('hidden');
        iframe.src = pdfUrl.split('#')[0] + '#toolbar=0&navpanes=0&view=FitH';
      }
      if (loader) loader.classList.add('hidden');
    }
  };

  window.closePdfViewerModal = function () {
    renderToken++;
    const modal = document.getElementById('pdf-viewer-modal');
    if (modal) {
      modal.classList.add('hidden');
      const iframe = document.getElementById('pdf-modal-iframe');
      if (iframe) iframe.src = '';
      const canvasContainer = document.getElementById('pdf-modal-canvas-container');
      if (canvasContainer) canvasContainer.innerHTML = '';
      currentPdfDoc = null;
    }
    document.body.style.overflow = '';
  };

  window.openWhitepaperModal = function () {
    const lang = getCurrentLang();
    const i18n = getI18nStrings(lang);

    if (lang === 'vi') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_VI.pdf', i18n.whitepaperTitle);
    } else if (lang === 'zh') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_ZH.pdf', i18n.whitepaperTitle);
    } else if (lang === 'ko') {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_KO.pdf', i18n.whitepaperTitle);
    } else {
      window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_EN.pdf', i18n.whitepaperTitle);
    }
  };

  // Delegated Click Handler for all Whitepaper links across the app
  document.addEventListener('click', function (e) {
    const trigger = e.target.closest('a[href="/whitepaper"], a[href="/whitepaper/"], a[href="/whitepaper.pdf"], a[href="/whitepaper-en.pdf"], a[href="/whitepaper-vi.pdf"], a[href="/whitepaper-zh.pdf"], a[href="/whitepaper-ko.pdf"], a[href="/whitepaper-vi"], a[href="/whitepaper-zh"], a[href="/whitepaper-ko"], [data-open-whitepaper], #nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link');
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
