/**
 * HAICHAIN Universal Online PDF Viewer Modal System
 * Provides Apple Titanium luxury in-app reading experience for PDF documents
 * Full Mobile Optimization:
 *  - High-DPI Canvas Rendering via PDF.js on mobile (No new tabs, no blank iframes, no forced downloads)
 *  - Continuous vertical touch scrolling through all pages
 *  - Interactive Zoom Controls: [-], [100% Fit], [+], and Double-Tap to Zoom
 *  - Desktop Native iframe with toolbar + FitH for high performance
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

    const isVi = getCurrentLang() === 'vi';

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
              <h3 id="pdf-modal-title" class="font-bold text-xs sm:text-sm text-white truncate max-w-[150px] xs:max-w-[220px] sm:max-w-md">Document Viewer</h3>
              <div class="flex items-center space-x-2">
                <span class="text-[10px] text-emerald-400 font-mono flex items-center space-x-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse inline-block"></span>
                  <span>ONLINE READER</span>
                </span>
                <span id="pdf-modal-page-count" class="text-[10px] text-neutral-400 font-mono hidden xs:inline"></span>
              </div>
            </div>
          </div>

          <!-- Controls: Zoom Toolbar + Actions -->
          <div class="flex items-center space-x-1.5 sm:space-x-2 shrink-0">
            
            <!-- Mobile/Desktop Zoom Controls -->
            <div id="pdf-modal-zoom-group" class="flex items-center bg-neutral-800/90 border border-neutral-700/60 rounded-xl p-0.5 text-xs font-mono">
              <button id="pdf-modal-zoom-out" type="button" class="w-7 h-7 flex items-center justify-center rounded-lg hover:bg-neutral-700 text-neutral-300 transition-all active:scale-90" title="Thu nhỏ (-)">
                <i data-lucide="minus" class="w-3.5 h-3.5"></i>
              </button>
              <button id="pdf-modal-zoom-reset" type="button" class="px-2 h-7 flex items-center justify-center rounded-lg hover:bg-neutral-700 text-[11px] text-neutral-200 font-semibold transition-all active:scale-95" title="Vừa màn hình (100%)">
                <span id="pdf-modal-zoom-label">100%</span>
              </button>
              <button id="pdf-modal-zoom-in" type="button" class="w-7 h-7 flex items-center justify-center rounded-lg hover:bg-neutral-700 text-neutral-300 transition-all active:scale-90" title="Phóng to (+)">
                <i data-lucide="plus" class="w-3.5 h-3.5"></i>
              </button>
            </div>

            <!-- Download Button -->
            <a id="pdf-modal-download-btn" href="#" download class="px-2.5 sm:px-3 py-1.5 rounded-xl bg-white text-black hover:bg-neutral-200 text-xs font-mono font-bold transition-all flex items-center space-x-1.5 active:scale-95 shadow-sm" title="Tải PDF">
              <i data-lucide="download" class="w-3.5 h-3.5"></i>
              <span id="pdf-modal-download-label" class="hidden md:inline">${isVi ? 'Tải PDF' : 'Download'}</span>
            </a>

            <!-- Close Button (Large 36x36 for easy finger tap) -->
            <button id="pdf-modal-close-btn" type="button" class="w-8 h-8 sm:w-9 sm:h-9 rounded-xl flex items-center justify-center text-neutral-400 hover:text-white hover:bg-neutral-800 transition-colors active:scale-95 ml-1" title="Đóng">
              <i data-lucide="x" class="w-5 h-5"></i>
            </button>
          </div>
        </div>

        <!-- Viewer Body -->
        <div id="pdf-modal-body" class="relative w-full flex-1 bg-[#141418] flex flex-col overflow-hidden">
          
          <!-- Mobile & Universal High-DPI Canvas Stream Container -->
          <div id="pdf-modal-canvas-container" class="w-full flex-1 overflow-y-auto overflow-x-auto touch-pan-y flex flex-col items-center py-4 px-2 sm:px-4 space-y-4 sm:space-y-6">
            <!-- Dynamically rendered pages go here -->
          </div>

          <!-- Desktop Native iframe -->
          <iframe id="pdf-modal-iframe" src="" class="w-full flex-1 border-0 hidden" allow="fullscreen"></iframe>

          <!-- Loading State Overlay -->
          <div id="pdf-modal-loader" class="absolute inset-0 bg-[#09090b]/90 backdrop-blur-xs flex flex-col items-center justify-center z-30 text-neutral-300 transition-opacity">
            <div class="w-10 h-10 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mb-3"></div>
            <p id="pdf-modal-loader-text" class="text-xs font-mono font-semibold text-neutral-200">${isVi ? 'Đang hiển thị tài liệu trực tiếp...' : 'Rendering document online...'}</p>
            <p class="text-[10px] text-neutral-500 font-sans mt-1">HAICHAIN Mobile High-Precision Vector Engine</p>
          </div>

        </div>

        <!-- Mobile Touch Hint Footer -->
        <div class="py-1.5 px-4 bg-[#0d0d10] border-t border-neutral-800/80 text-[10px] font-mono text-neutral-500 flex items-center justify-between sm:hidden shrink-0">
          <span>Vuốt để cuộn trang</span>
          <span>Chạm đúp để phóng to / vừa màn hình</span>
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

    // Zoom Buttons
    const btnZoomIn = modal.querySelector('#pdf-modal-zoom-in');
    const btnZoomOut = modal.querySelector('#pdf-modal-zoom-out');
    const btnZoomReset = modal.querySelector('#pdf-modal-zoom-reset');

    if (btnZoomIn) {
      btnZoomIn.addEventListener('click', () => {
        if (currentZoom < 2.5) {
          currentZoom = Math.min(2.5, Math.round((currentZoom + 0.25) * 100) / 100);
          updateZoomUI();
          renderCanvasPages();
        }
      });
    }

    if (btnZoomOut) {
      btnZoomOut.addEventListener('click', () => {
        if (currentZoom > 0.6) {
          currentZoom = Math.max(0.6, Math.round((currentZoom - 0.25) * 100) / 100);
          updateZoomUI();
          renderCanvasPages();
        }
      });
    }

    if (btnZoomReset) {
      btnZoomReset.addEventListener('click', () => {
        currentZoom = 1.0;
        updateZoomUI();
        renderCanvasPages();
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
    const thisToken = ++renderToken;
    const container = document.getElementById('pdf-modal-canvas-container');
    const loader = document.getElementById('pdf-modal-loader');
    if (!container) return;

    if (loader) loader.classList.remove('hidden');

    try {
      container.innerHTML = '';
      const containerWidth = container.clientWidth || window.innerWidth;
      const baseWidth = Math.min(containerWidth - 20, 800);
      const targetWidth = Math.max(280, Math.round(baseWidth * currentZoom));

      for (let pageNum = 1; pageNum <= currentPdfDoc.numPages; pageNum++) {
        if (thisToken !== renderToken || !currentPdfDoc) return;

        const page = await currentPdfDoc.getPage(pageNum);
        const unscaledViewport = page.getViewport({ scale: 1 });
        const scale = targetWidth / unscaledViewport.width;
        const pixelRatio = Math.min(window.devicePixelRatio || 1, 2.5); // Retina clarity
        const viewport = page.getViewport({ scale: scale * pixelRatio });

        // Page Card Frame
        const card = document.createElement('div');
        card.className = 'relative bg-white shadow-2xl rounded-xl overflow-hidden border border-neutral-700 shrink-0 transition-transform select-none';
        card.style.width = `${targetWidth}px`;
        card.style.maxWidth = 'none';

        const canvas = document.createElement('canvas');
        canvas.width = viewport.width;
        canvas.height = viewport.height;
        canvas.style.width = `${targetWidth}px`;
        canvas.style.height = `${Math.round(unscaledViewport.height * scale)}px`;
        canvas.className = 'block';

        const ctx = canvas.getContext('2d');
        await page.render({ canvasContext: ctx, viewport: viewport }).promise;

        if (thisToken !== renderToken || !currentPdfDoc) return;

        // Bottom Page Number Strip
        const isVi = getCurrentLang() === 'vi';
        const footer = document.createElement('div');
        footer.className = 'py-1 px-3 bg-neutral-100 text-neutral-600 text-[10px] font-mono border-t border-neutral-200 flex items-center justify-between';
        footer.innerHTML = `
          <span class="font-bold">HAICHAIN</span>
          <span>${isVi ? 'Trang' : 'Page'} ${pageNum} / ${currentPdfDoc.numPages}</span>
          <span>Official Doc</span>
        `;

        card.appendChild(canvas);
        card.appendChild(footer);

        // Double tap on mobile to toggle zoom between 100% and 150%
        let lastTap = 0;
        card.addEventListener('touchend', (e) => {
          const now = Date.now();
          if (now - lastTap < 300) {
            e.preventDefault();
            if (currentZoom === 1.0) {
              currentZoom = 1.5;
            } else {
              currentZoom = 1.0;
            }
            updateZoomUI();
            renderCanvasPages();
          }
          lastTap = now;
        });

        container.appendChild(card);
      }
    } catch (err) {
      console.error('PDF page render error:', err);
    } finally {
      if (thisToken === renderToken && loader) {
        loader.classList.add('hidden');
      }
    }
  }

  window.openPdfViewerModal = async function (pdfUrl, docTitle) {
    const modal = ensurePdfModal();
    const iframe = document.getElementById('pdf-modal-iframe');
    const canvasContainer = document.getElementById('pdf-modal-canvas-container');
    const titleEl = document.getElementById('pdf-modal-title');
    const downloadEl = document.getElementById('pdf-modal-download-btn');
    const pageCountEl = document.getElementById('pdf-modal-page-count');
    const loader = document.getElementById('pdf-modal-loader');
    const zoomGroup = document.getElementById('pdf-modal-zoom-group');

    const isVi = getCurrentLang() === 'vi';
    currentPdfUrl = pdfUrl;
    currentZoom = 1.0;
    updateZoomUI();

    if (titleEl) titleEl.textContent = docTitle || 'HAICHAIN Document';
    if (pageCountEl) pageCountEl.textContent = '';
    if (downloadEl) {
      downloadEl.href = pdfUrl;
      downloadEl.download = pdfUrl.split('/').pop().split('?')[0];
    }

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
          pageCountEl.textContent = `• ${currentPdfDoc.numPages} ${isVi ? 'trang' : 'pages'}`;
        }
        await renderCanvasPages();
      } catch (err) {
        console.error('Failed to load PDF via PDF.js on mobile:', err);
        // Fallback: try iframe
        if (iframe) {
          iframe.classList.remove('hidden');
          iframe.src = pdfUrl.split('#')[0] + '#toolbar=1&navpanes=0&view=FitH';
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
        iframe.src = pdfUrl.split('#')[0] + '#toolbar=1&navpanes=0&view=FitH';
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
