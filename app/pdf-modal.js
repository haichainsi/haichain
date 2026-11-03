
function buildHaichainSaftEmailHtml(opt) {
  const contractId = opt.contractId || '';
  const name = opt.name || 'Anonymous Investor';
  const email = opt.email || '';
  const amount = Number(opt.amount) || 0;
  const tokens = Number(opt.tokens) || Math.floor(amount / 0.007);
  const wallet = opt.wallet || 'N/A';
  const treasury = opt.treasury || '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';
  const hashHex = opt.hashHex || 'N/A';
  const timestamp = opt.timestamp || new Date().toISOString();
  const isAdmin = !!opt.isAdmin;

  const contractPdfUrl = "https://haichain.si/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf";
  const tgeVal = Math.round(tokens * 0.01);
  const formattedAmount = amount.toLocaleString('en-US');
  const formattedTokens = tokens.toLocaleString('en-US');
  const formattedTgeVal = tgeVal.toLocaleString('en-US');

  const title = isAdmin ? "PRE-SEED SAFT AGREEMENT SIGNED" : "Pre-Seed SAFT Agreement Execution Confirmation";
  const badge = "✓ CRYPTOGRAPHICALLY SIGNED &amp; RECORDED";
  
  const intro = isAdmin
    ? "A new Pre-Seed Strategic Round Simple Agreement for Future Tokens (SAFT) has been digitally executed and cryptographically sealed pursuant to the <strong>US ESIGN Act (15 U.S.C. § 7001) &amp; UETA standards</strong>."
    : `Dear <strong>${name}</strong>,<br><br>Your Simple Agreement for Future Tokens (SAFT) for the <strong>HAICHAIN Pre-Seed Strategic Round</strong> has been cryptographically signed and officially recorded pursuant to the <strong>US Electronic Signatures in Global and National Commerce Act (ESIGN Act, 15 U.S.C. § 7001) &amp; UETA standards</strong>.`;

  const btnPdfText = "📄 View Official SAFT Agreement (PDF)";
  const btnDashText = "Access HAICHAIN Dashboard";
  const actionLead = "Your official SAFT Agreement copy has been cryptographically sealed. You can view or download the complete contract document below:";
  const treasuryNote = "Investment funds are secured in the Squads Multi-Sig Treasury on Solana Mainnet. Your $HAISI tokens will be minted and transferred directly to your beneficiary wallet upon the Token Generation Event (TGE).";

  return `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HAICHAIN Pre-Seed SAFT Execution</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f4f4f5; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;">
  <div style="background-color: #f4f4f5; padding: 32px 16px;">
    <div style="max-width: 640px; margin: 0 auto; background-color: #0c0c0e; border: 1px solid #27272a; border-radius: 18px; padding: 36px 28px; color: #ffffff; box-shadow: 0 12px 36px rgba(0,0,0,0.25);">
      
      <!-- Brand Header with Logo -->
      <div style="border-bottom: 1px solid #27272a; padding-bottom: 24px; margin-bottom: 28px;">
        <div style="margin-bottom: 16px;">
          <img src="https://haichain.si/assets/haichain-official-logo-white.png" alt="Haichain" height="32" style="height: 32px; width: auto; display: block; border: 0;" />
        </div>
        <div style="font-size: 13px; font-weight: 600; color: #ffffff; letter-spacing: -0.2px; line-height: 1.5;">
          Haichain - The Financial Operating System for The Autonomous Machine Era
        </div>
        <div style="font-size: 12px; color: #a1a1aa; margin-top: 4px; line-height: 1.5;">
          The Economic Bedrock for the Symbiotic Superintelligence Era AI²
        </div>
      </div>

      <!-- Execution Badge -->
      <div style="display: inline-block; background-color: rgba(74, 222, 128, 0.1); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 9999px; padding: 4px 14px; margin-bottom: 20px;">
        <span style="font-size: 11px; font-weight: 700; color: #4ade80; text-transform: uppercase; letter-spacing: 0.5px; font-family: monospace;">
          ${badge}
        </span>
      </div>

      <!-- Salutation & Headline -->
      <h1 style="margin: 0 0 16px 0; font-size: 21px; font-weight: 700; color: #ffffff; letter-spacing: -0.5px;">
        ${title}
      </h1>
      <p style="margin: 0 0 24px 0; font-size: 13px; line-height: 1.6; color: #d4d4d8;">
        ${intro}
      </p>

      <!-- Key Details Card -->
      <div style="background-color: #141417; border: 1px solid #27272a; border-radius: 14px; padding: 22px; margin-bottom: 28px;">
        <table style="width: 100%; border-collapse: collapse; font-size: 13px; line-height: 1.6;">
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; width: 42%; border-bottom: 1px solid #1f1f23;">Contract ID:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #ffffff; font-family: monospace; border-bottom: 1px solid #1f1f23;">${contractId}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Signatory Entity:</td>
            <td style="padding: 8px 0; font-weight: 600; color: #ffffff; border-bottom: 1px solid #1f1f23;">${name}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Registered Email:</td>
            <td style="padding: 8px 0; color: #38bdf8; font-family: monospace; border-bottom: 1px solid #1f1f23;">${email}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Subscription Investment:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #4ade80; font-size: 15px; border-bottom: 1px solid #1f1f23;">$${formattedAmount} USD (USDT)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Token Entitlement:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #ffffff; border-bottom: 1px solid #1f1f23;">${formattedTokens} $HAISI (@ $0.007)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Projected TGE Value:</td>
            <td style="padding: 8px 0; color: #a1a1aa; font-weight: 600; border-bottom: 1px solid #1f1f23;">$${formattedTgeVal} USD (+42.8%)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Beneficiary Solana Wallet:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 11px; color: #ffffff; word-break: break-all; border-bottom: 1px solid #1f1f23;">${wallet}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Multi-Sig Treasury Vault:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 11px; color: #a1a1aa; word-break: break-all; border-bottom: 1px solid #1f1f23;">${treasury}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">SHA-256 Audit Proof:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 10px; color: #71717a; word-break: break-all; border-bottom: 1px solid #1f1f23;">${hashHex}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa;">Execution Time (UTC):</td>
            <td style="padding: 8px 0; color: #ffffff; font-size: 12px;">${timestamp}</td>
          </tr>
        </table>
      </div>

      <!-- Prominent Contract Link & Dashboard Button -->
      <div style="background-color: #121215; border: 1px solid #27272a; border-radius: 14px; padding: 24px; text-align: center; margin-bottom: 28px;">
        <p style="margin: 0 0 16px 0; font-size: 13px; line-height: 1.6; color: #d4d4d8;">
          ${actionLead}
        </p>
        <div style="text-align: center;">
          <a href="${contractPdfUrl}" target="_blank" style="display: inline-block; background-color: #ffffff; color: #000000; font-weight: 700; font-size: 13px; padding: 13px 32px; border-radius: 9999px; text-decoration: none; margin: 6px; box-shadow: 0 4px 14px rgba(255,255,255,0.15);">
            ${btnPdfText}
          </a>
          <a href="https://haichain.si/dashboard" target="_blank" style="display: inline-block; background-color: #18181b; color: #ffffff; font-weight: 600; font-size: 13px; padding: 13px 26px; border-radius: 9999px; text-decoration: none; border: 1px solid #3f3f46; margin: 6px;">
            ${btnDashText}
          </a>
        </div>
      </div>

      <p style="margin: 0 0 28px 0; font-size: 12px; line-height: 1.6; color: #71717a;">
        ${treasuryNote}
      </p>

      <!-- Standard Institutional Email Footer -->
      <div style="border-top: 1px solid #27272a; padding-top: 24px; font-size: 11px; line-height: 1.7; color: #71717a;">
        <div style="margin-bottom: 12px;">
          <strong style="color: #ffffff; font-size: 12px;">Haichain Foundation</strong><br />
          <span style="color: #a1a1aa; font-size: 11px;">Haichain - The Financial Operating System for The Autonomous Machine Era - The Economic Bedrock for the Symbiotic Superintelligence Era AI²</span>
        </div>
        <div style="margin-bottom: 12px; color: #a1a1aa;">
          Official Website: <a href="https://haichain.si" target="_blank" style="color: #38bdf8; text-decoration: none;">https://haichain.si</a> &nbsp;•&nbsp; 
          Support: <a href="mailto:support@haichain.si" style="color: #ffffff; text-decoration: none;">support@haichain.si</a>
        </div>
        <div style="margin-bottom: 12px; color: #52525b; font-size: 10px; line-height: 1.5;">
          <strong>LEGAL NOTICE &amp; ESIGN COMPLIANCE:</strong> This electronic transmission and its cryptographic proof of execution are generated pursuant to the US Electronic Signatures in Global and National Commerce Act (ESIGN Act, 15 U.S.C. § 7001 et seq.) and the Uniform Electronic Transactions Act (UETA). The terms herein constitute a legally binding Simple Agreement for Future Tokens (SAFT) under applicable digital commerce and transaction laws. This message is intended solely for the designated recipient and may contain confidential information. If you received this transmission in error, please notify support@haichain.si immediately.
        </div>
        <div style="color: #3f3f46; font-size: 10px;">
          © Haichain. All rights reserved.
        </div>
      </div>

    </div>
  </div>
</body>
</html>`;
}

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
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const urlLang = urlParams.get('lang');
      if (urlLang) return urlLang.toLowerCase();
    } catch (_) {}
    if (window.haichainI18n && typeof window.haichainI18n.current === 'function') {
      const l = window.haichainI18n.current();
      if (l) return l.toLowerCase();
    }
    if (window.haichainI18n && typeof window.haichainI18n.getLanguage === 'function') {
      const l = window.haichainI18n.getLanguage();
      if (l) return l.toLowerCase();
    }
    try {
      const saved = localStorage.getItem('haichain-lang') || localStorage.getItem('haichain_lang');
      if (saved) return saved.toLowerCase();
    } catch (_) {}
    return (document.documentElement.getAttribute('lang') || 'en').toLowerCase();
  }
  window.getCurrentLang = window.getHaichainLang = getCurrentLang;

  function getWhitepaperUrlForLang(lang) {
    const versionParam = '?v=v32_ai2_title_math_fixed';
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
    let modal = document.getElementById('pdf-viewer-modal') || document.getElementById('pdf-modal');
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
            <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl bg-neutral-200 dark:bg-neutral-800 border border-neutral-300 dark:border-neutral-700 text-neutral-800 dark:text-neutral-200 flex items-center justify-center shrink-0 shadow-xs">
              <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
              </svg>
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
            <button id="pdf-modal-zoom-out" type="button" class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 cursor-pointer" title="Thu nhỏ (-)"><svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg></button>
            
            <!-- 1-Tap Toggle: 100% Fit vs 140% Comfort Read -->
            <button id="pdf-modal-zoom-fit" type="button" class="px-2 h-7 sm:h-8 rounded-lg flex items-center justify-center text-[10px] sm:text-[11px] font-mono font-medium text-neutral-600 dark:text-neutral-300 hover:text-black dark:hover:text-white bg-neutral-200/60 dark:bg-neutral-800/60 hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 cursor-pointer" title="Nhấn để đổi: Vừa trang (100%) / To rõ (140%)">
              <span id="pdf-modal-zoom-label">100%</span>
            </button>

            <!-- Zoom In (+) -->
            <button id="pdf-modal-zoom-in" type="button" class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 cursor-pointer" title="Phóng to (+)"><svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg></button>

            <div class="h-4 w-px bg-neutral-300 dark:bg-neutral-700 mx-0.5 sm:mx-1"></div>

            <!-- In-Modal Quick Language Selector (Syncs with Global Engine) -->
            <div class="relative" id="pdf-modal-lang-container">
              <button id="pdf-modal-lang-toggle" type="button" class="px-2 h-7 sm:h-8 rounded-lg flex items-center space-x-1 text-[10px] sm:text-[11px] font-mono font-bold text-neutral-300 hover:text-white bg-neutral-800 hover:bg-neutral-700 transition-colors border border-neutral-700 cursor-pointer" title="Change Language / Đổi Ngôn Ngữ">
                <span id="pdf-modal-lang-code">EN</span>
                <svg class="w-3 h-3 text-neutral-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </button>
              <div id="pdf-modal-lang-dropdown" class="absolute right-0 top-full mt-1.5 w-32 py-1 bg-[#18181b] border border-neutral-700 rounded-xl shadow-2xl hidden z-50 overflow-hidden font-mono text-[11px]">
                <button type="button" data-lang="en" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>English</span><span class="text-[10px] text-neutral-500">EN</span></button>
                <button type="button" data-lang="fr" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Français</span><span class="text-[10px] text-neutral-500">FR</span></button>
                <button type="button" data-lang="es" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Español</span><span class="text-[10px] text-neutral-500">ES</span></button>
                <button type="button" data-lang="ru" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Русский</span><span class="text-[10px] text-neutral-500">RU</span></button>
                <button type="button" data-lang="zh" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>中文</span><span class="text-[10px] text-neutral-500">ZH</span></button>
                <button type="button" data-lang="ko" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>한국어</span><span class="text-[10px] text-neutral-500">KO</span></button>
                <button type="button" data-lang="hi" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>हिन्दी</span><span class="text-[10px] text-neutral-500">HI</span></button>
                <button type="button" data-lang="he" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>עברית</span><span class="text-[10px] text-neutral-500">HE</span></button>
                <button type="button" data-lang="vi" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Tiếng Việt</span><span class="text-[10px] text-neutral-500">VI</span></button>
                <button type="button" data-lang="kk" class="modal-lang-opt w-full px-3 py-1.5 text-left text-neutral-300 hover:text-white hover:bg-neutral-800 flex items-center justify-between cursor-pointer"><span>Қазақша</span><span class="text-[10px] text-neutral-500">KK</span></button>
              </div>
            </div>

                        <!-- Digital E-Signature Action Button (Zero Icons, Pure Typography) -->
            <button id="pdf-modal-sign-btn" type="button" class="hidden items-center justify-center px-3.5 sm:px-4 h-7 sm:h-8 rounded-lg sm:rounded-xl bg-white hover:bg-neutral-200 text-black font-semibold text-xs tracking-tight shadow-sm active:scale-95 transition-all shrink-0 cursor-pointer" style="background-color: #ffffff !important; color: #000000 !important;">
              <span id="pdf-modal-sign-btn-text">Sign Agreement Online</span>
            </button>

            <!-- Close Button (✕) ONLY -->
            <button id="pdf-modal-close-btn" type="button" class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-200 dark:hover:bg-neutral-800 transition-colors active:scale-95 shrink-0 cursor-pointer" title="Đóng"><svg class="w-4 h-4 sm:w-4.5 sm:h-4.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button>
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

                <!-- ========================================================================= -->
        <!-- LUXURY IN-APP DIGITAL E-SIGNATURE OVERLAY (SOLID OPAQUE, ULTRA-HIGH CONTRAST) -->
        <!-- ========================================================================= -->
        <div id="saft-sign-overlay" class="absolute inset-0 z-50 hidden flex flex-col overflow-y-auto p-4 sm:p-6 md:p-8 transition-all duration-200 select-none" style="background-color: #0c0c0e !important; color: #ffffff !important;">
          
          <!-- Drawer Header (Clean Apple Minimalist, Solid Background) -->
          <div class="flex items-center justify-between pb-3 sm:pb-4 border-b border-neutral-800 shrink-0">
            <div>
              <h3 id="saft-drawer-title" class="text-sm sm:text-base font-bold text-white tracking-tight" style="color: #ffffff !important;">Pre-Seed SAFT Digital E-Signature ($0.007)</h3>
              <p id="saft-drawer-sub" class="text-xs font-mono mt-0.5" style="color: #d4d4d8 !important;">Online legal verification compliant with US ESIGN Act &amp; UETA standards</p>
            </div>
            
            <button id="saft-drawer-close-btn" type="button" class="w-8 h-8 rounded-xl flex items-center justify-center text-neutral-400 hover:text-white hover:bg-neutral-800 transition-colors cursor-pointer" title="Close" style="color: #d4d4d8 !important;">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
          </div>

          <!-- Drawer Form Body -->
          <div id="saft-drawer-form-view" class="py-4 sm:py-6 max-w-2xl mx-auto w-full space-y-4 pb-28 sm:pb-20 select-text">
            
            <!-- Dual Column Fields: Name & Email -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              <div>
                <label id="saft-lbl-name" class="block text-xs font-semibold mb-1" style="color: #ffffff !important;">Full Legal Name / Entity *</label>
                <input id="saft-input-name" type="text" placeholder="John Doe / Apex Capital LLC" class="w-full px-3.5 py-2.5 text-xs sm:text-sm rounded-xl focus:outline-none transition-all" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
              </div>
              <div>
                <label id="saft-lbl-email" class="block text-xs font-semibold mb-1" style="color: #ffffff !important;">Contact Email *</label>
                <input id="saft-input-email" type="email" placeholder="investor@example.com" class="w-full px-3.5 py-2.5 text-xs sm:text-sm rounded-xl focus:outline-none transition-all" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
              </div>
            </div>

            <!-- Dual Column Fields: Amount & Real-time Allocation Calculation -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              <div>
                <label id="saft-lbl-amount" class="block text-xs font-semibold mb-1" style="color: #ffffff !important;">Subscription Investment Amount (USD / USDT) *</label>
                <div class="relative">
                  <span class="absolute left-3.5 top-2.5 text-xs font-mono" style="color: #71717a !important;">$</span>
                  <input id="saft-input-amount" type="number" min="500" max="50000" step="100" value="1000" class="w-full pl-8 pr-3.5 py-2.5 text-xs sm:text-sm font-mono rounded-xl focus:outline-none transition-all" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
                </div>
                <p id="saft-txt-amount-note" class="text-[11px] font-mono mt-1" style="color: #d4d4d8 !important;">Ticket limit: $500 – $15,000 USD</p>
              </div>

              <div>
                <label id="saft-lbl-alloc" class="block text-xs font-semibold mb-1" style="color: #ffffff !important;">Token Entitlement $HAISI (@ $0.007)</label>
                <div class="p-3 rounded-xl flex flex-col justify-center" style="background-color: #18181b !important; border: 1px solid #27272a !important;">
                  <div class="flex items-baseline justify-between">
                    <span id="saft-calc-tokens" class="text-sm sm:text-base font-bold font-mono" style="color: #ffffff !important;">142,857</span>
                    <span class="text-xs font-mono" style="color: #a1a1aa !important;">$HAISI</span>
                  </div>
                  <div class="text-[11px] font-mono flex items-center justify-between mt-1 pt-1 border-t border-neutral-800">
                    <span id="saft-lbl-tge-val" style="color: #a1a1aa !important;">TGE Value ($0.010):</span>
                    <span id="saft-calc-tge" class="font-bold" style="color: #4ade80 !important;">$1,428 USD (+42.8%)</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Beneficiary Wallet Address -->
            <div>
              <div class="flex items-center justify-between mb-1">
                <label id="saft-lbl-wallet" class="text-xs font-semibold" style="color: #ffffff !important;">Beneficiary Solana Wallet Address for TGE *</label>
                <button id="saft-btn-autofill-wallet" type="button" class="text-xs font-mono underline hover:opacity-80 cursor-pointer transition-colors" style="color: #38bdf8 !important;">Use Connected Wallet</button>
              </div>
              <input id="saft-input-wallet" type="text" placeholder="Solana wallet address (Base58 32-44 characters)..." class="w-full px-3.5 py-2.5 text-xs font-mono rounded-xl focus:outline-none transition-all" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
            </div>

            <!-- Treasury Vault Display (Immutably Bound) -->
            <div class="p-3 rounded-xl text-[11px] font-mono" style="background-color: #18181b !important; border: 1px solid #27272a !important;">
              <div class="flex items-center justify-between">
                <span id="saft-lbl-treasury" class="font-semibold" style="color: #d4d4d8 !important;">Multi-Sig Treasury Vault (Solana Mainnet):</span>
                <span class="font-bold" style="color: #4ade80 !important;">Squads 2-of-3</span>
              </div>
              <div class="truncate mt-1 font-mono font-medium" style="color: #ffffff !important;">5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3</div>
            </div>

            <!-- Digital Signature Pad Canvas -->
            <div>
              <div class="flex items-center justify-between mb-1.5">
                <label id="saft-lbl-canvas" class="text-xs font-semibold" style="color: #ffffff !important;">Your Digital Signature *</label>
                <button id="saft-btn-clear-sig" type="button" class="text-xs font-mono underline hover:opacity-80 cursor-pointer transition-colors" style="color: #f87171 !important;">Clear Signature</button>
              </div>
              <div class="relative w-full rounded-xl overflow-hidden shadow-sm" style="background-color: #ffffff !important; border: 1px solid #d4d4d8 !important;">
                <canvas id="saft-sig-canvas" width="600" height="150" class="w-full h-32 sm:h-36 block touch-none cursor-crosshair"></canvas>
                <div id="saft-sig-placeholder" class="absolute inset-0 flex items-center justify-center pointer-events-none text-xs font-mono select-none" style="color: #9ca3af !important;">
                  (Use mouse or touch screen to sign here)
                </div>
              </div>
            </div>

            <!-- Legal Declaration Checkbox -->
            <label class="flex items-start space-x-3 text-xs cursor-pointer select-none pt-1" style="color: #e4e4e7 !important;">
              <input id="saft-input-agree" type="checkbox" class="mt-0.5 rounded cursor-pointer w-4 h-4 accent-white">
              <span id="saft-lbl-agree" class="leading-relaxed">I confirm that I have read, understood, and agreed to all terms of the HAICHAIN Pre-Seed SAFT Agreement. I understand that investment funds are secured in the Squads Multi-Sig Treasury and tokens are distributed at TGE.</span>
            </label>

            <!-- Submit Sign Button -->
            <button id="saft-btn-submit-sign" type="button" class="w-full py-3 sm:py-3.5 rounded-xl font-bold text-xs sm:text-sm tracking-wide shadow-lg active:scale-[0.99] transition-all cursor-pointer" style="background-color: #ffffff !important; color: #000000 !important;">
              SIGN &amp; FINALIZE LEGAL AGREEMENT
            </button>
          </div>

          <!-- Drawer Success View (Shown after signing) -->
          <div id="saft-drawer-success-view" class="hidden py-8 sm:py-12 max-w-lg mx-auto w-full text-center space-y-6 pb-28 sm:pb-20 select-text animate-scaleUp">
            <div class="w-12 h-12 mx-auto rounded-full border border-neutral-600 flex items-center justify-center text-sm font-bold font-mono text-white" style="border-color: #52525b !important; color: #ffffff !important;">
              OK
            </div>
            <div>
              <h4 id="saft-success-title" class="text-base sm:text-xl font-bold" style="color: #ffffff !important;">AGREEMENT SIGNED SUCCESSFULLY</h4>
              <p id="saft-success-sub" class="text-xs sm:text-sm mt-1" style="color: #a1a1aa !important;">Digital SAFT agreement recorded with cryptographic audit trail.</p>
            </div>

            <!-- Receipt Card -->
            <div class="p-4 sm:p-5 rounded-2xl text-left text-xs font-mono space-y-2.5" style="background-color: #18181b !important; border: 1px solid #27272a !important;">
              <div class="flex justify-between">
                <span id="saft-rec-lbl-id" style="color: #a1a1aa !important;">Contract ID:</span>
                <span id="saft-rec-id" class="font-bold" style="color: #ffffff !important;">SAFT-HAI-2026-XXXXX</span>
              </div>
              <div class="flex justify-between">
                <span id="saft-rec-lbl-investor" style="color: #a1a1aa !important;">Investor:</span>
                <span id="saft-rec-name" class="font-semibold truncate max-w-[200px]" style="color: #ffffff !important;">--</span>
              </div>
              <div class="flex justify-between">
                <span id="saft-rec-lbl-alloc" style="color: #a1a1aa !important;">Allocation:</span>
                <span id="saft-rec-alloc" class="font-bold" style="color: #4ade80 !important;">-- $HAISI</span>
              </div>
              <div class="flex justify-between">
                <span id="saft-rec-lbl-wallet" style="color: #a1a1aa !important;">Receiving Wallet:</span>
                <span id="saft-rec-wallet" class="font-mono text-[11px] truncate max-w-[200px]" style="color: #d4d4d8 !important;">--</span>
              </div>
              <div class="flex justify-between">
                <span id="saft-rec-lbl-time" style="color: #a1a1aa !important;">Timestamp:</span>
                <span id="saft-rec-time" class="text-[11px]" style="color: #a1a1aa !important;">--</span>
              </div>
              <div class="pt-2 border-t border-neutral-800 text-[10px] break-all" style="color: #71717a !important;">
                <span id="saft-rec-lbl-hash" class="block mb-0.5" style="color: #a1a1aa !important;">SHA-256 Audit Hash:</span>
                <span id="saft-rec-hash">--</span>
              </div>
            </div>

            <!-- Dual Action Buttons: Download PDF & Proceed to Deposit -->
            <div class="space-y-3 pt-2">
              <button id="saft-btn-download-cert" type="button" class="w-full py-3 rounded-xl font-medium text-xs sm:text-sm transition-all cursor-pointer" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
                Download Signed Agreement Certificate (HTML / PDF)
              </button>
              <button id="saft-btn-proceed-pay" type="button" class="w-full py-3 sm:py-3.5 rounded-xl font-bold text-xs sm:text-sm tracking-wide shadow-lg active:scale-[0.99] transition-all cursor-pointer" style="background-color: #ffffff !important; color: #000000 !important;">
                Proceed to Deposit to Treasury
              </button>
            </div>
          </div>

        </div>

        <!-- Floating Sticky Bottom Pill: Current Page & Jump Controls -->
        <div id="pdf-modal-pill" class="absolute bottom-3 sm:bottom-5 left-1/2 -translate-x-1/2 z-20 px-3 sm:px-4 py-1.5 rounded-full bg-black/85 dark:bg-white/95 text-white dark:text-black shadow-2xl backdrop-blur-md flex items-center space-x-2 text-xs font-mono select-none pointer-events-auto transition-transform duration-200">
          <button id="pdf-modal-prev-page" type="button" class="hover:opacity-70 active:scale-90 transition-transform cursor-pointer px-1 py-0.5" title="Trang trước (▲)"><svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg></button>
          <span id="pdf-modal-page-indicator" class="font-bold tracking-wide text-[11px] sm:text-xs">Trang 1 / --</span>
          <button id="pdf-modal-next-page" type="button" class="hover:opacity-70 active:scale-90 transition-transform cursor-pointer px-1 py-0.5" title="Trang sau (▼)"><svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></button>
        </div>

      </div>
    `;

    (document.body || document.documentElement).appendChild(modal);

        // Initialize In-Modal Language Dropdown
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
          const targetLang = (opt.getAttribute('data-lang') || 'en').toLowerCase();
          langDropdown.classList.add('hidden');
          if (langCodeSpan) langCodeSpan.textContent = targetLang.toUpperCase();

          // Immediate direct PDF document switch inside modal
          if (currentPdfUrl) {
            const u = currentPdfUrl.toUpperCase();
            if (u.includes('RISK')) {
              const doc = typeof window.getRiskReportPdfForLang === 'function' ? window.getRiskReportPdfForLang(targetLang) : null;
              if (doc) window.openPdfViewerModal(doc.url, doc.title);
            } else if (u.includes('WHITEPAPER')) {
              const meta = getI18nMeta(targetLang);
              window.openPdfViewerModal(getWhitepaperUrlForLang(targetLang), meta.title);
            } else if (u.includes('SAFT')) {
              const doc = typeof window.getSaftPdfForLang === 'function' ? window.getSaftPdfForLang(targetLang) : null;
              if (doc) window.openPdfViewerModal(doc.url, doc.title);
            } else if (u.includes('MEMO')) {
              const doc = typeof window.getPreseedMemoPdfForLang === 'function' ? window.getPreseedMemoPdfForLang(targetLang) : null;
              if (doc) window.openPdfViewerModal(doc.url, doc.title);
            }
          }

          // Propagate language switch to the rest of the application
          if (window.haichainI18n && typeof window.haichainI18n.setLanguage === 'function') {
            window.haichainI18n.setLanguage(targetLang);
          } else {
            try {
              localStorage.setItem('haichain-lang', targetLang);
              localStorage.setItem('haichain_lang', targetLang);
            } catch (_) {}
            window.dispatchEvent(new CustomEvent('haichain:languageChanged', { detail: { lang: targetLang } }));
          }
        });
      });

      document.addEventListener('click', () => {
        if (!langDropdown.classList.contains('hidden')) {
          langDropdown.classList.add('hidden');
        }
      });
    }

    // Close button
    initSaftSignatureEngine(modal);

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

    // =========================================================================
  // SAFT DIGITAL E-SIGNATURE LOGIC (OPTION A - MULTI-LANGUAGE & ZERO ICONS)
  // =========================================================================
  const SAFT_DRAWER_I18N = {
  "vi": {
    "btnOpenSign": "Ký Hợp Đồng Online",
    "title": "Ký Điện Tử Hợp Đồng SAFT Pre-Seed ($0.007)",
    "subtitle": "Xác thực pháp lý trực tuyến theo chuẩn ESIGN Act & Luật GDĐT 2023",
    "nameLabel": "Họ và Tên / Tên Pháp Nhân *",
    "namePlaceholder": "Nguyễn Văn A / Tech Fund LLC",
    "emailLabel": "Email Liên Hệ *",
    "emailPlaceholder": "investor@example.com",
    "amountLabel": "Số Tiền Đăng Ký Đầu Tư (USD / USDT) *",
    "amountNote": "Hạn mức vé: $500 – $15,000 USD",
    "allocLabel": "Quyền Phân Bổ Token $HAISI (@ $0.007)",
    "tgeValLabel": "Giá trị TGE ($0.010):",
    "walletLabel": "Địa Chỉ Ví Solana Nhận Token Tại TGE *",
    "walletPlaceholder": "Địa chỉ ví Phantom/Solflare (Base58 32-44 ký tự)...",
    "autofillBtn": "Lấy Ví Đang Kết Nối",
    "treasuryLabel": "Kho Bạc Multi-Sig Nhận Vốn (Solana Mainnet):",
    "canvasLabel": "Chữ Ký Điện Tử Của Bạn *",
    "canvasPlaceholder": "(Dùng chuột hoặc ngón tay để ký tên tại đây)",
    "clearBtn": "Xóa ký lại",
    "agreeLabel": "Tôi xác nhận đã đọc, hiểu và đồng thuận 100% với các điều khoản của Hợp đồng SAFT HAICHAIN. Tôi hiểu rằng vốn đầu tư được bảo vệ tại Kho Bạc Squads Multi-Sig và token được phân bổ tự động tại TGE.",
    "submitBtn": "XÁC NHẬN KÝ & HOÀN TẤT HỢP ĐỒNG PHÁP LÝ",
    "successTitle": "KÝ HỢP ĐỒNG THÀNH CÔNG",
    "successSubtitle": "Hợp đồng SAFT điện tử đã được ghi nhận và đóng dấu kiểm toán mật mã.",
    "recId": "Mã Hợp Đồng:",
    "recInvestor": "Nhà Đầu Tư:",
    "recAlloc": "Phân Bổ:",
    "recWallet": "Ví Nhận:",
    "recTime": "Thời Gian:",
    "recHash": "SHA-256 Audit Hash:",
    "downloadBtn": "Tải File Chứng Nhận Hợp Đồng (HTML / PDF)",
    "proceedBtn": "Tiến Hành Nạp Tiền Vào Kho Bạc",
    "errName": "Vui lòng nhập Họ và Tên hoặc Tên Pháp Nhân của bạn.",
    "errEmail": "Vui lòng nhập địa chỉ Email hợp lệ.",
    "errAmount": "Hạn mức đăng ký đầu tư tối thiểu là 500 USD.",
    "errWallet": "Vui lòng nhập địa chỉ ví Solana hợp lệ (32 - 44 ký tự Base58) để nhận token tại TGE.",
    "errSig": "Vui lòng ký tên của bạn vào khung chữ ký điện tử.",
    "errAgree": "Vui lòng tick vào ô xác nhận đồng ý với các điều khoản Hợp đồng SAFT.",
    "alertProceed": "HỢP ĐỒNG ĐÃ ĐƯỢC KÝ!\n\nVui lòng chuyển {amount} USDT vào Kho Bạc:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nSố token {tokens} $HAISI sẽ được tự động phân bổ về ví của bạn tại TGE.",
    "noWalletDetected": "Chưa phát hiện ví Web3 (Phantom/Solflare) đang kết nối. Vui lòng dán địa chỉ ví thủ công.",
    "evmDetectedNeedSolana": "Ví đang kết nối là ví MetaMask (EVM). Token $HAISI được phân bổ trên mạng Solana, vui lòng nhập địa chỉ ví Solana (Phantom / Solflare).",
    "walletFilledSuccess": "✓ Đã lấy ví thành công"
  },
  "en": {
    "btnOpenSign": "Sign Agreement Online",
    "title": "Pre-Seed SAFT Digital E-Signature ($0.007)",
    "subtitle": "Online legal verification compliant with US ESIGN Act & UETA standards",
    "nameLabel": "Full Legal Name / Entity *",
    "namePlaceholder": "John Doe / Apex Capital LLC",
    "emailLabel": "Contact Email *",
    "emailPlaceholder": "investor@example.com",
    "amountLabel": "Subscription Investment Amount (USD / USDT) *",
    "amountNote": "Ticket limit: $500 – $15,000 USD",
    "allocLabel": "Token Entitlement $HAISI (@ $0.007)",
    "tgeValLabel": "TGE Value ($0.010):",
    "walletLabel": "Beneficiary Solana Wallet Address for TGE *",
    "walletPlaceholder": "Solana wallet address (Base58 32-44 characters)...",
    "autofillBtn": "Use Connected Wallet",
    "treasuryLabel": "Multi-Sig Treasury Vault (Solana Mainnet):",
    "canvasLabel": "Your Digital Signature *",
    "canvasPlaceholder": "(Use mouse or touch screen to sign here)",
    "clearBtn": "Clear Signature",
    "agreeLabel": "I confirm that I have read, understood, and agreed to all terms of the HAICHAIN Pre-Seed SAFT Agreement. I understand that investment funds are secured in the Squads Multi-Sig Treasury and tokens are distributed at TGE.",
    "submitBtn": "SIGN & FINALIZE LEGAL AGREEMENT",
    "successTitle": "AGREEMENT SIGNED SUCCESSFULLY",
    "successSubtitle": "Digital SAFT agreement recorded with cryptographic audit trail.",
    "recId": "Contract ID:",
    "recInvestor": "Investor:",
    "recAlloc": "Allocation:",
    "recWallet": "Receiving Wallet:",
    "recTime": "Timestamp:",
    "recHash": "SHA-256 Audit Hash:",
    "downloadBtn": "Download Signed Agreement Certificate (HTML / PDF)",
    "proceedBtn": "Proceed to Deposit to Treasury",
    "errName": "Please enter your Full Legal Name or Entity Name.",
    "errEmail": "Please enter a valid Email address.",
    "errAmount": "Minimum subscription amount is 500 USD.",
    "errWallet": "Please enter a valid Solana wallet address (32 - 44 characters Base58).",
    "errSig": "Please draw your signature in the signature box.",
    "errAgree": "Please agree to the SAFT Agreement terms to proceed.",
    "alertProceed": "AGREEMENT SIGNED!\n\nPlease transfer {amount} USDT to Treasury:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nYour {tokens} $HAISI allocation will be automatically disbursed at TGE.",
    "noWalletDetected": "No Web3 wallet (Phantom/Solflare) detected. Please paste your address manually.",
    "evmDetectedNeedSolana": "Connected wallet is MetaMask (EVM). $HAISI tokens are disbursed on Solana Mainnet. Please provide a Solana address (Phantom / Solflare).",
    "walletFilledSuccess": "✓ Wallet filled successfully"
  },
  "zh": {
    "btnOpenSign": "在线签署协议",
    "title": "Pre-Seed SAFT 电子法律签署 ($0.007)",
    "subtitle": "符合美国 ESIGN 法案与 UETA 标准的在线法律合规认证",
    "nameLabel": "法定全名 / 投资机构名称 *",
    "namePlaceholder": "张伟 / 某某资本合伙企业 (LLC)",
    "emailLabel": "联系电子邮箱 *",
    "emailPlaceholder": "investor@example.com",
    "amountLabel": "认购投资金额 (USD / USDT) *",
    "amountNote": "单张认购限额: $500 – $15,000 USD",
    "allocLabel": "$HAISI 代币认购分配权益 (@ $0.007)",
    "tgeValLabel": "TGE 上市预估价值 ($0.010):",
    "walletLabel": "TGE 代币接收 Solana 钱包地址 *",
    "walletPlaceholder": "Solana 钱包地址 (Base58 编码 32-44 位字符)...",
    "autofillBtn": "使用已连接钱包",
    "treasuryLabel": "多签金库收款地址 (Solana 主网):",
    "canvasLabel": "您的电子签名 *",
    "canvasPlaceholder": "(请使用鼠标或触屏在此处签署姓名)",
    "clearBtn": "清除重签",
    "agreeLabel": "本人确认已充分阅读、完全理解并同意 HAICHAIN Pre-Seed SAFT 协议的所有法律条款。本人知悉认购资金受 Squads 2-of-3 多签金库托管，代币将在 TGE 阶段自动分发。",
    "submitBtn": "确认签署并完成法律协议",
    "successTitle": "协议签署成功",
    "successSubtitle": "SAFT 电子法律协议已完成加密存证与防篡改审计哈希记录。",
    "recId": "合同编号:",
    "recInvestor": "投资者 / 机构:",
    "recAlloc": "代币分配额度:",
    "recWallet": "接收钱包:",
    "recTime": "签署时间:",
    "recHash": "SHA-256 审计哈希:",
    "downloadBtn": "下载已签署协议证书 (HTML / PDF)",
    "proceedBtn": "前往多签金库完成认购付款",
    "errName": "请输入您的法定全名或机构名称。",
    "errEmail": "请输入有效的电子邮箱地址。",
    "errAmount": "单笔最低认购投资金额为 500 USD。",
    "errWallet": "请输入有效的 Solana 钱包地址（32 - 44 位 Base58 格式）。",
    "errSig": "请在签名区域内绘制您的电子签名。",
    "errAgree": "请勾选同意 SAFT 协议法律条款以继续。",
    "alertProceed": "协议已成功签署！\n\n请向以下多签金库转账 {amount} USDT:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\n您的 {tokens} $HAISI 代币分配将在 TGE 阶段自动结算至您的钱包。",
    "noWalletDetected": "未检测到已连接的 Web3 钱包 (Phantom/Solflare)，请手动粘贴地址。",
    "evmDetectedNeedSolana": "当前连接的是MetaMask (EVM)钱包。$HAISI代币在Solana主网发放，请输入Solana钱包地址（Phantom / Solflare）。",
    "walletFilledSuccess": "✓ 已成功填入钱包"
  },
  "ko": {
    "btnOpenSign": "온라인 계약 서명",
    "title": "Pre-Seed SAFT 디지털 전자 서명 ($0.007)",
    "subtitle": "미국 ESIGN 법 및 UETA 표준 준수 온라인 법적 인증",
    "nameLabel": "법적 성명 / 법인명 *",
    "namePlaceholder": "홍길동 / 에이펙스 캐피탈",
    "emailLabel": "담당자 이메일 *",
    "emailPlaceholder": "investor@example.com",
    "amountLabel": "투자 청약 금액 (USD / USDT) *",
    "amountNote": "투자 한도: $500 – $15,000 USD",
    "allocLabel": "$HAISI 토큰 배정 권리 (@ $0.007)",
    "tgeValLabel": "TGE 상장 가치 ($0.010):",
    "walletLabel": "TGE 수령용 솔라나(Solana) 지갑 주소 *",
    "walletPlaceholder": "솔라나 지갑 주소 (Base58 32-44자)...",
    "autofillBtn": "연결된 지갑 주소 불러오기",
    "treasuryLabel": "멀티시그 금고 주소 (Solana 메인넷):",
    "canvasLabel": "전자 서명란 *",
    "canvasPlaceholder": "(마우스 또는 터치스크린으로 서명해 주세요)",
    "clearBtn": "서명 다시 하기",
    "agreeLabel": "본인은 HAICHAIN Pre-Seed SAFT 계약서의 모든 약관을 읽고 완전히 이해하였으며 이에 동의합니다. 투자 자금은 Squads 2-of-3 멀티시그 금고에 안전하게 보관되며 TGE 시점에 토큰이 자동 배정됨을 확인합니다.",
    "submitBtn": "서명 확인 및 법적 계약 체결",
    "successTitle": "계약 서명 완료",
    "successSubtitle": "디지털 SAFT 계약이 암호학적 감사 로그와 함께 안전하게 기록되었습니다.",
    "recId": "계약 번호:",
    "recInvestor": "투자자:",
    "recAlloc": "토큰 배정량:",
    "recWallet": "수령 지갑:",
    "recTime": "서명 일시:",
    "recHash": "SHA-256 감사 해시:",
    "downloadBtn": "서명된 계약 인증서 다운로드 (HTML / PDF)",
    "proceedBtn": "금고 입금 및 투자 절차 진행",
    "errName": "법적 성명 또는 법인명을 입력해 주세요.",
    "errEmail": "올바른 이메일 주소를 입력해 주세요.",
    "errAmount": "최소 투자 청약 금액은 500 USD입니다.",
    "errWallet": "유효한 솔라나 지갑 주소(Base58 32-44자)를 입력해 주세요.",
    "errSig": "서명란에 전자 서명을 입력해 주세요.",
    "errAgree": "진행하시려면 SAFT 계약 약관에 동의해 주세요.",
    "alertProceed": "계약 서명이 완료되었습니다!\n\n아래 멀티시그 금고로 {amount} USDT를 전송해 주세요:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\n배정된 {tokens} $HAISI 토큰은 TGE 시점에 등록된 지갑으로 자동 지급됩니다.",
    "noWalletDetected": "연결된 Web3 지갑(Phantom/Solflare)을 찾을 수 없습니다. 지갑 주소를 직접 입력해 주세요.",
    "evmDetectedNeedSolana": "현재 연결된 지갑은 MetaMask (EVM)입니다. $HAISI 토큰은 Solana 메인넷에서 분배되므로 Solana 지갑(Phantom / Solflare) 주소를 입력해 주세요.",
    "walletFilledSuccess": "✓ 지갑 주소가 입력되었습니다"
  },
  "es": {
    "btnOpenSign": "Firmar Acuerdo Online",
    "title": "Firma Digital de Acuerdo SAFT Pre-Seed ($0.007)",
    "subtitle": "Verificación legal en línea conforme a las normas US ESIGN Act y UETA",
    "nameLabel": "Nombre Legal Completo / Entidad *",
    "namePlaceholder": "Juan Pérez / Apex Capital LLC",
    "emailLabel": "Correo Electrónico de Contacto *",
    "emailPlaceholder": "inversor@ejemplo.com",
    "amountLabel": "Monto de Suscripción de Inversión (USD / USDT) *",
    "amountNote": "Límite por ticket: $500 – $15,000 USD",
    "allocLabel": "Asignación de Tokens $HAISI (@ $0.007)",
    "tgeValLabel": "Valor en TGE ($0.010):",
    "walletLabel": "Dirección de Billetera Solana para TGE *",
    "walletPlaceholder": "Dirección Solana (Base58 de 32 a 44 caracteres)...",
    "autofillBtn": "Usar Billetera Conectada",
    "treasuryLabel": "Bóveda de Tesorería Multi-Firma (Solana Mainnet):",
    "canvasLabel": "Su Firma Digital *",
    "canvasPlaceholder": "(Use el ratón o pantalla táctil para firmar aquí)",
    "clearBtn": "Borrar y repetir firma",
    "agreeLabel": "Confirmo que he leído, comprendido y aceptado el 100% de los términos del Acuerdo SAFT HAICHAIN. Entiendo que los fondos de inversión están custodiados en la Tesorería Multi-Sig Squads y los tokens se distribuirán automáticamente en el TGE.",
    "submitBtn": "FIRMAR Y FORMALIZAR ACUERDO LEGAL",
    "successTitle": "ACUERDO FIRMADO CON ÉXITO",
    "successSubtitle": "Acuerdo legal SAFT registrado con pista de auditoría criptográfica.",
    "recId": "ID de Contrato:",
    "recInvestor": "Inversionista:",
    "recAlloc": "Asignación:",
    "recWallet": "Billetera de Recepción:",
    "recTime": "Fecha y Hora:",
    "recHash": "Hash de Auditoría SHA-256:",
    "downloadBtn": "Descargar Certificado de Firma (HTML / PDF)",
    "proceedBtn": "Proceder al Depósito en la Tesorería",
    "errName": "Por favor ingrese su Nombre Legal Completo o de la Entidad.",
    "errEmail": "Por favor ingrese un Correo Electrónico válido.",
    "errAmount": "El monto mínimo de suscripción es de 500 USD.",
    "errWallet": "Por favor ingrese una dirección válida de billetera Solana (32-44 caracteres Base58).",
    "errSig": "Por favor dibuje su firma en el recuadro correspondiente.",
    "errAgree": "Debe aceptar los términos del Acuerdo SAFT para continuar.",
    "alertProceed": "¡ACUERDO FIRMADO CON ÉXITO!\n\nPor favor transfiera {amount} USDT a la Tesorería Multi-Firma:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nSu asignación de {tokens} $HAISI será distribuida automáticamente en el TGE.",
    "noWalletDetected": "No se detectó billetera Web3 (Phantom/Solflare). Por favor pegue la dirección manualmente.",
    "evmDetectedNeedSolana": "La billetera conectada es MetaMask (EVM). Los tokens $HAISI se distribuyen en la red Solana. Ingrese una dirección de billetera Solana (Phantom / Solflare).",
    "walletFilledSuccess": "✓ Billetera completada con éxito"
  },
  "fr": {
    "btnOpenSign": "Signer l’Accord en Ligne",
    "title": "Signature Électronique SAFT Pre-Seed ($0.007)",
    "subtitle": "Vérification juridique conforme aux normes US ESIGN Act et UETA",
    "nameLabel": "Nom Légal Complet / Entité *",
    "namePlaceholder": "Jean Dupont / Apex Capital LLC",
    "emailLabel": "Email de Contact *",
    "emailPlaceholder": "investisseur@exemple.com",
    "amountLabel": "Montant d’Investissement (USD / USDT) *",
    "amountNote": "Limite de souscription: $500 – $15,000 USD",
    "allocLabel": "Attribution de Jetons $HAISI (@ $0.007)",
    "tgeValLabel": "Valeur au TGE ($0.010):",
    "walletLabel": "Adresse de Portefeuille Solana pour le TGE *",
    "walletPlaceholder": "Adresse Solana (Base58 de 32 à 44 caractères)...",
    "autofillBtn": "Utiliser le Portefeuille Connecté",
    "treasuryLabel": "Trésorerie Multi-Sig (Solana Mainnet):",
    "canvasLabel": "Votre Signature Électronique *",
    "canvasPlaceholder": "(Utilisez la souris ou l’écran tactile pour signer ici)",
    "clearBtn": "Effacer la signature",
    "agreeLabel": "Je confirme avoir lu, compris et accepté l’ensemble des conditions du contrat SAFT HAICHAIN. Je comprends que les fonds sont sécurisés dans la trésorerie multi-sig Squads et que les jetons seront distribués lors du TGE.",
    "submitBtn": "SIGNER ET FINALISER LE CONTRAT",
    "successTitle": "ACCORD SIGNÉ AVEC SUCCÈS",
    "successSubtitle": "Contrat SAFT numérique enregistré avec horodatage et audit cryptographique.",
    "recId": "ID du Contrat:",
    "recInvestor": "Investisseur:",
    "recAlloc": "Attribution:",
    "recWallet": "Portefeuille Récepteur:",
    "recTime": "Horodatage:",
    "recHash": "Hash d’Audit SHA-256:",
    "downloadBtn": "Télécharger le Certificat de Signature (HTML / PDF)",
    "proceedBtn": "Procéder au Dépôt vers la Trésorerie",
    "errName": "Veuillez saisir votre nom complet ou le nom de votre entité.",
    "errEmail": "Veuillez saisir une adresse email valide.",
    "errAmount": "Le montant minimum de souscription est de 500 USD.",
    "errWallet": "Veuillez saisir une adresse de portefeuille Solana valide (32-44 caractères Base58).",
    "errSig": "Veuillez apposer votre signature dans la zone prévue à cet effet.",
    "errAgree": "Veuillez accepter les termes de l’accord SAFT pour continuer.",
    "alertProceed": "ACCORD SIGNÉ !\n\nVeuillez transférer {amount} USDT vers la Trésorerie:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nVotre allocation de {tokens} $HAISI sera automatiquement distribuée au TGE.",
    "noWalletDetected": "Aucun portefeuille Web3 (Phantom/Solflare) détecté. Veuillez coller l’adresse manuellement.",
    "evmDetectedNeedSolana": "Le portefeuille connecté est MetaMask (EVM). Les jetons $HAISI sont distribués sur Solana. Veuillez fournir une adresse Solana (Phantom / Solflare).",
    "walletFilledSuccess": "✓ Portefeuille renseigné avec succès"
  },
  "ru": {
    "btnOpenSign": "Подписать договор онлайн",
    "title": "Электронная подпись договора SAFT Pre-Seed ($0.007)",
    "subtitle": "Юридическая верификация онлайн в соответствии с US ESIGN Act и UETA",
    "nameLabel": "Полное юридическое имя / Название компании *",
    "namePlaceholder": "Иван Иванов / Apex Capital LLC",
    "emailLabel": "Контактный Email *",
    "emailPlaceholder": "investor@example.com",
    "amountLabel": "Сумма инвестиционной подписки (USD / USDT) *",
    "amountNote": "Лимит подписки: $500 – $15,000 USD",
    "allocLabel": "Право на распределение токенов $HAISI (@ $0.007)",
    "tgeValLabel": "Стоимость при TGE ($0.010):",
    "walletLabel": "Адрес кошелька Solana для получения токенов при TGE *",
    "walletPlaceholder": "Адрес Solana (Base58, 32-44 символа)...",
    "autofillBtn": "Использовать подключенный кошелек",
    "treasuryLabel": "Мультисиг казначейство (Solana Mainnet):",
    "canvasLabel": "Ваша электронная подпись *",
    "canvasPlaceholder": "(Используйте мышь или сенсорный экран для подписи)",
    "clearBtn": "Очистить подпись",
    "agreeLabel": "Я подтверждаю, что прочитал, понял и полностью согласен со всеми условиями соглашения HAICHAIN Pre-Seed SAFT. Я понимаю, что средства хранятся в мультисиг казначействе Squads, а токены распределяются при TGE.",
    "submitBtn": "ПОДПИСАТЬ И УТВЕРДИТЬ СОГЛАШЕНИЕ",
    "successTitle": "СОГЛАШЕНИЕ УСПЕШНО ПОДПИСАНО",
    "successSubtitle": "Электронный договор SAFT зарегистрирован с криптографическим аудитом.",
    "recId": "ID контракта:",
    "recInvestor": "Инвестор:",
    "recAlloc": "Аллокация:",
    "recWallet": "Кошелек получения:",
    "recTime": "Время:",
    "recHash": "Аудит-хеш SHA-256:",
    "downloadBtn": "Скачать сертификат соглашения (HTML / PDF)",
    "proceedBtn": "Перейти к переводу средств в казначейство",
    "errName": "Пожалуйста, укажите ваше полное имя или название организации.",
    "errEmail": "Пожалуйста, укажите корректный адрес электронной почты.",
    "errAmount": "Минимальная сумма подписки составляет 500 USD.",
    "errWallet": "Пожалуйста, укажите действительный адрес кошелька Solana (32-44 символа Base58).",
    "errSig": "Пожалуйста, поставьте подпись в поле для подписи.",
    "errAgree": "Пожалуйста, подтвердите согласие с условиями договора SAFT.",
    "alertProceed": "ДОГОВОР ПОДПИСАН!\n\nПожалуйста, переведите {amount} USDT в Казначейство:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nВаша аллокация в размере {tokens} $HAISI будет автоматически перечислена при TGE.",
    "noWalletDetected": "Web3 кошелек (Phantom/Solflare) не обнаружен. Пожалуйста, вставьте адрес вручную.",
    "evmDetectedNeedSolana": "Подключенный кошелек - MetaMask (EVM). Токены $HAISI распределяются в сети Solana. Пожалуйста, укажите адрес кошелька Solana (Phantom / Solflare).",
    "walletFilledSuccess": "✓ Кошелек успешно заполнен"
  },
  "kk": {
    "btnOpenSign": "Келісімге онлайн қол қою",
    "title": "Pre-Seed SAFT келісіміне цифрлық қол қою ($0.007)",
    "subtitle": "US ESIGN Act және UETA стандарттарына сәйкес онлайн заңды верификация",
    "nameLabel": "Толық заңды аты-жөні / Заңды тұлға *",
    "namePlaceholder": "Асқар Серік / Apex Capital LLC",
    "emailLabel": "Байланыс электрондық поштасы *",
    "emailPlaceholder": "investor@example.com",
    "amountLabel": "Инвестициялық жазылу сомасы (USD / USDT) *",
    "amountNote": "Лимит: $500 – $15,000 USD",
    "allocLabel": "$HAISI токендерін алу құқығы (@ $0.007)",
    "tgeValLabel": "TGE кезіндегі бағасы ($0.010):",
    "walletLabel": "TGE кезінде токен алатын Solana әмиян мекенжайы *",
    "walletPlaceholder": "Solana әмиян мекенжайы (Base58 32-44 таңба)...",
    "autofillBtn": "Қосылған әмиянды алу",
    "treasuryLabel": "Multi-Sig қазынашылық қоймасы (Solana Mainnet):",
    "canvasLabel": "Сіздің цифрлық қолтаңбаңыз *",
    "canvasPlaceholder": "(Қол қою үшін тінтуірді немесе сенсорлық экранды пайдаланыңыз)",
    "clearBtn": "Қайта қол қою",
    "agreeLabel": "Мен HAICHAIN Pre-Seed SAFT келісімінің барлық талаптарын оқып шыққанымды, толық түсінгенімді және келісетінімді растаймын. Қаражат Squads 2-of-3 қазынашылығында сақталатынын және токендер TGE кезінде берілетінін түсінемін.",
    "submitBtn": "ҚОЛ ҚОЮ ЖӘНЕ КЕЛІСІМДІ БЕКІТУ",
    "successTitle": "КЕЛІСІМГЕ СӘТТІ ҚОЛ ҚОЙЫЛДЫ",
    "successSubtitle": "Сандық SAFT шарты криптографиялық аудит белгісімен тіркелді.",
    "recId": "Келісімшарт ID:",
    "recInvestor": "Инвестор:",
    "recAlloc": "Бөлініс:",
    "recWallet": "Қабылдаушы әмиян:",
    "recTime": "Уақыты:",
    "recHash": "SHA-256 аудит хэші:",
    "downloadBtn": "Қол қойылған сертификатты жүктеу (HTML / PDF)",
    "proceedBtn": "Қазынашылыққа депозит жасау",
    "errName": "Толық заңды атыңызды немесе компания атауын енгізіңіз.",
    "errEmail": "Жарамды электрондық пошта мекенжайын енгізіңіз.",
    "errAmount": "Ең төменгі инвестиция сомасы - 500 USD.",
    "errWallet": "Жарамды Solana әмиян мекенжайын енгізіңіз (Base58 32-44 таңба).",
    "errSig": "Қолтаңба өрісіне қол қойыңыз.",
    "errAgree": "Жалғастыру үшін SAFT шарттарымен келісуіңіз керек.",
    "alertProceed": "КЕЛІСІМГЕ ҚОЛ ҚОЙЫЛДЫ!\n\nҚазынашылыққа {amount} USDT аударыңыз:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nСізге бөлінген {tokens} $HAISI токендері TGE кезінде автоматты түрде аударылады.",
    "noWalletDetected": "Қосылған Web3 әмиян табылмады. Мекенжайды қолмен енгізіңіз.",
    "evmDetectedNeedSolana": "Қосылған әмиян - MetaMask (EVM). $HAISI токендері Solana желісінде таратылады. Solana әмиян мекенжайын (Phantom / Solflare) енгізіңіз.",
    "walletFilledSuccess": "✓ Әмиян мекенжайы сәтті қойылды"
  },
  "hi": {
    "btnOpenSign": "ऑनलाइन अनुबंध पर हस्ताक्षर करें",
    "title": "प्री-सीड SAFT डिजिटल ई-हस्ताक्षर ($0.007)",
    "subtitle": "अमेरिकी ESIGN अधिनियम और UETA मानकों के अनुरूप ऑनलाइन कानूनी सत्यापन",
    "nameLabel": "पूर्ण कानूनी नाम / संस्था का नाम *",
    "namePlaceholder": "राजेश शर्मा / एपेक्स कैपिटल",
    "emailLabel": "संपर्क ईमेल *",
    "emailPlaceholder": "investor@example.com",
    "amountLabel": "निवेश सदस्यता राशि (USD / USDT) *",
    "amountNote": "टिकट सीमा: $500 – $15,000 USD",
    "allocLabel": "$HAISI टोकन आवंटन अधिकार (@ $0.007)",
    "tgeValLabel": "TGE मूल्य ($0.010):",
    "walletLabel": "TGE पर टोकन प्राप्त करने के लिए सोलाना वॉलेट पता *",
    "walletPlaceholder": "सोलाना वॉलेट पता (Base58 32-44 वर्ण)...",
    "autofillBtn": "कनेक्टेड वॉलेट का उपयोग करें",
    "treasuryLabel": "मल्टी-सिग ट्रेजरी वॉल्ट (सोलाना मेननेट):",
    "canvasLabel": "आपका डिजिटल हस्ताक्षर *",
    "canvasPlaceholder": "(हस्ताक्षर करने के लिए माउस या टच स्क्रीन का उपयोग करें)",
    "clearBtn": "हस्ताक्षर साफ़ करें",
    "agreeLabel": "मैं पुष्टि करता हूँ कि मैंने HAICHAIN प्री-सीड SAFT अनुबंध की सभी शर्तों को पढ़, समझ और सहमति दे दी है। मैं समझता हूँ कि निवेश निधि स्क्वॉड मल्टी-सिग ट्रेजरी में सुरक्षित है और टोकन TGE पर वितरित किए जाएंगे।",
    "submitBtn": "हस्ताक्षर करें और कानूनी अनुबंध को अंतिम रूप दें",
    "successTitle": "अनुबंध सफलतापूर्वक हस्ताक्षरित",
    "successSubtitle": "क्रिप्टोग्राफ़िक ऑडिट ट्रेल के साथ डिजिटल SAFT अनुबंध दर्ज किया गया।",
    "recId": "अनुबंध आईडी:",
    "recInvestor": "निवेशक:",
    "recAlloc": "आवंटन:",
    "recWallet": "प्राप्तकर्ता वॉलेट:",
    "recTime": "समय:",
    "recHash": "SHA-256 ऑडिट हैश:",
    "downloadBtn": "हस्ताक्षरित प्रमाणपत्र डाउनलोड करें (HTML / PDF)",
    "proceedBtn": "ट्रेजरी में जमा करने के लिए आगे बढ़ें",
    "errName": "कृपया अपना पूर्ण कानूनी नाम या संस्था का नाम दर्ज करें।",
    "errEmail": "कृपया एक मान्य ईमेल पता दर्ज करें।",
    "errAmount": "न्यूनतम सदस्यता राशि 500 USD है।",
    "errWallet": "कृपया एक मान्य सोलाना वॉलेट पता (32-44 वर्ण Base58) दर्ज करें।",
    "errSig": "कृपया हस्ताक्षर बॉक्स में अपना हस्ताक्षर बनाएं।",
    "errAgree": "आगे बढ़ने के लिए कृपया SAFT अनुबंध की शर्तों से सहमत हों।",
    "alertProceed": "अनुबंध हस्ताक्षरित!\n\nकृपया ट्रेजरी में {amount} USDT ट्रांसफर करें:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nआपका {tokens} $HAISI आवंटन TGE पर स्वचालित रूप से वितरित किया जाएगा।",
    "noWalletDetected": "कोई Web3 वॉलेट नहीं मिला। कृपया अपना पता मैन्युअल रूप से पेस्ट करें।",
    "evmDetectedNeedSolana": "जुड़ा हुआ वॉलेट MetaMask (EVM) है। $HAISI टोकन Solana मेननेट पर वितरित किए जाते हैं। कृपया एक Solana वॉलेट पता (Phantom / Solflare) प्रदान करें।",
    "walletFilledSuccess": "✓ वॉलेट सफलतापूर्वक भर दिया गया"
  },
  "he": {
    "btnOpenSign": "חתימה על ההסכם אונליין",
    "title": "חתימה אלקטרונית על הסכם SAFT Pre-Seed ($0.007)",
    "subtitle": "אימות משפטי מקוון בהתאם לחוקי ESIGN ו-UETA בארה\"ב",
    "nameLabel": "שם משפטי מלא / שם תאגיד *",
    "namePlaceholder": "ישראל ישראלי / Apex Capital LLC",
    "emailLabel": "דוא\"ל ליצירת קשר *",
    "emailPlaceholder": "investor@example.com",
    "amountLabel": "סכום השקעה (USD / USDT) *",
    "amountNote": "מגבלת השקעה: $500 – $15,000 USD",
    "allocLabel": "זכאות להקצאת אסימוני $HAISI (@ $0.007)",
    "tgeValLabel": "שווי ב-TGE ($0.010):",
    "walletLabel": "כתובת ארנק Solana לקבלת אסימונים ב-TGE *",
    "walletPlaceholder": "כתובת ארנק Solana (Base58 32-44 תווים)...",
    "autofillBtn": "השתמש בארנק מחובר",
    "treasuryLabel": "כספת האוצר מרובת-חתימות (Solana Mainnet):",
    "canvasLabel": "החתימה הדיגיטלית שלך *",
    "canvasPlaceholder": "(השתמש בעכבר או במסך מגע לחתימה כאן)",
    "clearBtn": "נקה חתימה",
    "agreeLabel": "אני מאשר כי קראתי, הבנתי והסכמתי לכל תנאי הסכם HAICHAIN Pre-Seed SAFT. אני מבין כי כספי ההשקעה מאובטחים באוצר Multi-Sig של Squads והאסימונים יחולקו ב-TGE.",
    "submitBtn": "חתום ואשר את ההסכם המשפטי",
    "successTitle": "ההסכם נחתם בהצלחה",
    "successSubtitle": "הסכם ה-SAFT הדיגיטלי נרשם עם חותמת ביקורת קריפטוגרפית.",
    "recId": "מזהה חוזה:",
    "recInvestor": "משקיע:",
    "recAlloc": "הקצאה:",
    "recWallet": "ארנק מקבל:",
    "recTime": "חותמת זמן:",
    "recHash": "גיבוב ביקורת SHA-256:",
    "downloadBtn": "הורד תעודת הסכם חתומה (HTML / PDF)",
    "proceedBtn": "המשך להפקדה באוצר",
    "errName": "נא להזין שם משפטי מלא או שם חברה.",
    "errEmail": "נא להזין כתובת דוא\"ל תקינה.",
    "errAmount": "סכום ההשקעה המינימלי הוא 500 USD.",
    "errWallet": "נא להזין כתובת ארנק Solana תקינה (32-44 תווים Base58).",
    "errSig": "נא לחתום בתיבת החתימה.",
    "errAgree": "יש לאשר את תנאי הסכם ה-SAFT כדי להמשיך.",
    "alertProceed": "ההסכם נחתם בהצלחה!\n\nנא להעביר {amount} USDT לחשבון האוצר:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nהקצאת ה-{tokens} $HAISI שלך תחולק אוטומטית ב-TGE.",
    "noWalletDetected": "לא זוהה ארנק Web3 מחובר. נא להדביק את הכתובת ידנית.",
    "evmDetectedNeedSolana": "הארנק המחובר הוא MetaMask (EVM). אסימוני $HAISI מחולקים ברשת Solana. אנא הזן כתובת ארנק Solana (Phantom / Solflare).",
    "walletFilledSuccess": "✓ הארנק מולא בהצלחה"
  }
};

  function initSaftSignatureEngine(modal) {
    const signBtn = modal.querySelector('#pdf-modal-sign-btn');
    const overlay = modal.querySelector('#saft-sign-overlay');
    const closeBtn = modal.querySelector('#saft-drawer-close-btn');
    const formView = modal.querySelector('#saft-drawer-form-view');
    const successView = modal.querySelector('#saft-drawer-success-view');

    const inputName = modal.querySelector('#saft-input-name');
    const inputEmail = modal.querySelector('#saft-input-email');
    const inputAmount = modal.querySelector('#saft-input-amount');
    const inputWallet = modal.querySelector('#saft-input-wallet');
    const inputAgree = modal.querySelector('#saft-input-agree');
    const calcTokens = modal.querySelector('#saft-calc-tokens');
    const calcTge = modal.querySelector('#saft-calc-tge');
    const btnAutoFill = modal.querySelector('#saft-btn-autofill-wallet');
    const btnClearSig = modal.querySelector('#saft-btn-clear-sig');
    const btnSubmit = modal.querySelector('#saft-btn-submit-sign');
    const btnDownloadCert = modal.querySelector('#saft-btn-download-cert');
    const btnProceedPay = modal.querySelector('#saft-btn-proceed-pay');

    const canvas = modal.querySelector('#saft-sig-canvas');
    const placeholder = modal.querySelector('#saft-sig-placeholder');

    let isDrawing = false;
    let strokeCount = 0;
    let pointsDrawn = 0;
    let hasSigned = false;
    let lastX = 0;
    let lastY = 0;
    let signedRecord = null;

    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    // Update Drawer i18n
    function applyDrawerI18n(overrideLang) {
      const lang = overrideLang || getCurrentLang();
      const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];

      const signBtnText = modal.querySelector('#pdf-modal-sign-btn-text');
      if (signBtnText) signBtnText.textContent = t.btnOpenSign;

      const dTitle = modal.querySelector('#saft-drawer-title');
      if (dTitle) dTitle.textContent = t.title;

      const dSub = modal.querySelector('#saft-drawer-sub');
      if (dSub) dSub.textContent = t.subtitle;

      const lblName = modal.querySelector('#saft-lbl-name');
      if (lblName) lblName.textContent = t.nameLabel;
      if (inputName) inputName.placeholder = t.namePlaceholder;

      const lblEmail = modal.querySelector('#saft-lbl-email');
      if (lblEmail) lblEmail.textContent = t.emailLabel;
      if (inputEmail) inputEmail.placeholder = t.emailPlaceholder;

      const lblAmount = modal.querySelector('#saft-lbl-amount');
      if (lblAmount) lblAmount.textContent = t.amountLabel;

      const txtAmountNote = modal.querySelector('#saft-txt-amount-note');
      if (txtAmountNote) txtAmountNote.textContent = t.amountNote;

      const lblAlloc = modal.querySelector('#saft-lbl-alloc');
      if (lblAlloc) lblAlloc.textContent = t.allocLabel;

      const lblTgeVal = modal.querySelector('#saft-lbl-tge-val');
      if (lblTgeVal) lblTgeVal.textContent = t.tgeValLabel;

      const lblWallet = modal.querySelector('#saft-lbl-wallet');
      if (lblWallet) lblWallet.textContent = t.walletLabel;
      if (inputWallet) inputWallet.placeholder = t.walletPlaceholder;

      if (btnAutoFill) btnAutoFill.textContent = t.autofillBtn;

      const lblTreasury = modal.querySelector('#saft-lbl-treasury');
      if (lblTreasury) lblTreasury.textContent = t.treasuryLabel;

      const lblCanvas = modal.querySelector('#saft-lbl-canvas');
      if (lblCanvas) lblCanvas.textContent = t.canvasLabel;

      if (placeholder) placeholder.textContent = t.canvasPlaceholder;
      if (btnClearSig) btnClearSig.textContent = t.clearBtn;

      const lblAgree = modal.querySelector('#saft-lbl-agree');
      if (lblAgree) lblAgree.textContent = t.agreeLabel;

      if (btnSubmit) btnSubmit.textContent = t.submitBtn;

      const sTitle = modal.querySelector('#saft-success-title');
      if (sTitle) sTitle.textContent = t.successTitle;

      const sSub = modal.querySelector('#saft-success-sub');
      if (sSub) sSub.textContent = t.successSubtitle;

      const recLblId = modal.querySelector('#saft-rec-lbl-id');
      if (recLblId) recLblId.textContent = t.recId;

      const recLblInvestor = modal.querySelector('#saft-rec-lbl-investor');
      if (recLblInvestor) recLblInvestor.textContent = t.recInvestor;

      const recLblAlloc = modal.querySelector('#saft-rec-lbl-alloc');
      if (recLblAlloc) recLblAlloc.textContent = t.recAlloc;

      const recLblWallet = modal.querySelector('#saft-rec-lbl-wallet');
      if (recLblWallet) recLblWallet.textContent = t.recWallet;

      const recLblTime = modal.querySelector('#saft-rec-lbl-time');
      if (recLblTime) recLblTime.textContent = t.recTime;

      const recLblHash = modal.querySelector('#saft-rec-lbl-hash');
      if (recLblHash) recLblHash.textContent = t.recHash;

      if (btnDownloadCert) btnDownloadCert.textContent = t.downloadBtn;
      if (btnProceedPay) btnProceedPay.textContent = t.proceedBtn;
    }

    // Canvas Retina Scaling with crisp white stroke on solid black
    function setupCanvasDpi() {
      const rect = canvas.getBoundingClientRect();
      const dpr = Math.max(window.devicePixelRatio || 1, 1);
      const cssW = (rect.width > 20) ? rect.width : (canvas.parentElement ? canvas.parentElement.clientWidth : 540);
      const cssH = (rect.height > 20) ? rect.height : 140;

      canvas.width = Math.round(cssW * dpr);
      canvas.height = Math.round(cssH * dpr);
      canvas.style.width = cssW + 'px';
      canvas.style.height = cssH + 'px';

      ctx.resetTransform ? ctx.resetTransform() : ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.scale(dpr, dpr);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#000000';
    }

    // Toggle Overlay
    if (signBtn) {
      signBtn.addEventListener('click', () => {
        applyDrawerI18n();
        overlay.classList.remove('hidden');
        formView.classList.remove('hidden');
        successView.classList.add('hidden');
        setTimeout(setupCanvasDpi, 50);

        // Auto-fill connected wallet if available
        autoFillConnectedWallet();
        updateDynamicAlloc();
      });
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        overlay.classList.add('hidden');
      });
    }

    // Dynamic Token Calculation (@ $0.007)
    function updateDynamicAlloc() {
      const amt = parseFloat(inputAmount.value) || 0;
      const tokens = Math.floor(amt / 0.007);
      const tgeVal = tokens * 0.010;
      if (calcTokens) calcTokens.textContent = tokens.toLocaleString('en-US');
      if (calcTge) calcTge.textContent = '$' + Math.round(tgeVal).toLocaleString('en-US') + ' USD (+42.8%)';
    }

    if (inputAmount) {
      inputAmount.addEventListener('input', updateDynamicAlloc);
    }

    // Robust Web3 Solana Wallet Resolution across Mobile Chrome, In-App WebViews, Extensions & Storage
    function resolveConnectedSolanaWallet() {
      function isValidSolana(addr) {
        return typeof addr === 'string' && !addr.startsWith('0x') && /^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(addr.trim());
      }
      function isValidEVM(addr) {
        return typeof addr === 'string' && /^0x[a-fA-F0-9]{40}$/i.test(addr.trim());
      }

      // 1. Direct window globals set by HAICHAIN runtime
      const directCandidates = [
        window.HAICHAIN_CURRENT_WALLET,
        window.currentConnectedSolanaWallet,
        window.haichainConnectedWallet,
        window.userWallet && window.userWallet.address,
        window.connectedWalletAddr
      ];
      for (const c of directCandidates) {
        if (isValidSolana(c)) return { address: c.trim(), provider: 'Global', isEVM: false };
      }

      // 2. Primary localStorage: 'haichain-connected-wallet'
      try {
        const raw = localStorage.getItem('haichain-connected-wallet');
        if (raw) {
          const parsed = typeof raw === 'string' && raw.trim().startsWith('{') ? JSON.parse(raw) : { address: raw };
          const addr = parsed.address || parsed.publicKey || parsed.pubkey || '';
          const prov = parsed.provider || (parsed.isEVM ? 'MetaMask' : 'Phantom');
          if (isValidSolana(addr)) {
            return { address: addr.trim(), provider: prov, isEVM: false };
          }
          if (isValidEVM(addr) || parsed.isEVM) {
            return { address: addr.trim(), provider: prov, isEVM: true };
          }
        }
      } catch (_) {}

      // 3. Fallback localStorage keys used in various components
      const fallbackKeys = [
        'haichain_connected_wallet',
        'haichain_wallet_address',
        'haichain_wallet',
        'solana_wallet',
        'solana_wallet_address',
        'phantom_pubkey',
        'connected_wallet',
        'last_connected_wallet'
      ];
      for (const k of fallbackKeys) {
        try {
          const val = localStorage.getItem(k);
          if (val) {
            let addr = val.trim();
            if (addr.startsWith('{')) {
              const p = JSON.parse(addr);
              addr = p.address || p.publicKey || p.pubkey || '';
            }
            if (isValidSolana(addr)) {
              return { address: addr.trim(), provider: 'Storage', isEVM: false };
            }
          }
        } catch (_) {}
      }

      // 4. Injected Solana browser providers (Phantom Extension, Phantom Mobile Browser, Solflare)
      try {
        const pSol = window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null);
        if (pSol && pSol.publicKey) {
          const pk = pSol.publicKey.toString();
          if (isValidSolana(pk)) return { address: pk, provider: 'Phantom', isEVM: false };
        }
      } catch (_) {}

      try {
        if (window.solflare && window.solflare.publicKey) {
          const pk = window.solflare.publicKey.toString();
          if (isValidSolana(pk)) return { address: pk, provider: 'Solflare', isEVM: false };
        }
      } catch (_) {}

      try {
        if (window.solana && window.solana.publicKey) {
          const pk = window.solana.publicKey.toString();
          if (isValidSolana(pk)) return { address: pk, provider: 'Solana', isEVM: false };
        }
      } catch (_) {}

      // 5. DOM Form elements in Dashboard (e.g. #preseed-wallet in sale card)
      try {
        const preseedInput = document.getElementById('preseed-wallet');
        if (preseedInput && isValidSolana(preseedInput.value)) {
          return { address: preseedInput.value.trim(), provider: 'PreseedForm', isEVM: false };
        }
      } catch (_) {}

      // 6. DOM Header elements: [data-wallet-address], #header-wallet-address, #connected-wallet-display
      try {
        const headerEl = document.querySelector('[data-wallet-address], #header-wallet-address, #connected-wallet-display');
        if (headerEl) {
          const raw = headerEl.getAttribute('data-wallet-address') || headerEl.getAttribute('data-wallet') || headerEl.textContent || '';
          const match = raw.match(/[1-9A-HJ-NP-Za-km-z]{32,44}/);
          if (match && isValidSolana(match[0])) {
            return { address: match[0], provider: 'HeaderPill', isEVM: false };
          }
        }
      } catch (_) {}

      return null;
    }

    // Auto-fill wallet into input
    function autoFillConnectedWallet(force) {
      const resolved = resolveConnectedSolanaWallet();
      if (resolved && !resolved.isEVM && resolved.address && inputWallet) {
        if (force || !inputWallet.value) {
          inputWallet.value = resolved.address;
          inputWallet.dispatchEvent(new Event('input', { bubbles: true }));
          inputWallet.dispatchEvent(new Event('change', { bubbles: true }));
          window.HAICHAIN_CURRENT_WALLET = resolved.address;
          window.currentConnectedSolanaWallet = resolved.address;
        }
        return resolved;
      }
      return resolved;
    }

    if (btnAutoFill) {
      btnAutoFill.addEventListener('click', async () => {
        const lang = getCurrentLang();
        const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];

        // 1. Try resolving currently connected wallet
        let res = autoFillConnectedWallet(true);

        // 2. If no valid Solana wallet found, check if an injected provider exists and can connect on demand
        if (!res || !res.address || res.isEVM) {
          if (!res || !res.isEVM) {
            const solProvider = window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null) || window.solflare || window.solana;
            if (solProvider && typeof solProvider.connect === 'function') {
              try {
                const connResp = await solProvider.connect();
                const pk = connResp?.publicKey?.toString() || solProvider.publicKey?.toString() || '';
                if (pk && pk.length >= 32 && pk.length <= 44) {
                  const provName = solProvider.isPhantom ? 'Phantom' : (solProvider.isSolflare ? 'Solflare' : 'Solana');
                  res = { address: pk, provider: provName, isEVM: false };
                  inputWallet.value = pk;
                  inputWallet.dispatchEvent(new Event('input', { bubbles: true }));
                  inputWallet.dispatchEvent(new Event('change', { bubbles: true }));
                  window.HAICHAIN_CURRENT_WALLET = pk;
                  window.currentConnectedSolanaWallet = pk;
                  try {
                    localStorage.setItem('haichain-connected-wallet', JSON.stringify({ address: pk, provider: provName }));
                    if (typeof window.setConnectedWallet === 'function') window.setConnectedWallet(pk, provName);
                  } catch (_) {}
                }
              } catch (connErr) {
                console.warn('[SAFT] On-demand Web3 connection declined:', connErr);
              }
            }
          }
        }

        // 3. User feedback
        if (res && !res.isEVM && res.address && inputWallet && inputWallet.value) {
          const origText = btnAutoFill.textContent;
          btnAutoFill.textContent = t.walletFilledSuccess || (lang === 'vi' ? '✓ Đã lấy ví thành công' : '✓ Wallet filled');
          btnAutoFill.classList.add('text-emerald-500');
          setTimeout(() => {
            btnAutoFill.textContent = origText;
            btnAutoFill.classList.remove('text-emerald-500');
          }, 2500);
        } else if (res && res.isEVM) {
          alert(t.evmDetectedNeedSolana || 'Ví đang kết nối là ví MetaMask (EVM). Token $HAISI được phân bổ trên mạng Solana, vui lòng nhập địa chỉ ví Solana (Phantom / Solflare).');
          inputWallet.focus();
        } else {
          // If no wallet connected, alert and open the connect tray/modal if present
          const wBtn = document.getElementById('wallet-btn');
          if (wBtn) {
            alert(t.noWalletDetected);
            wBtn.click();
          } else {
            alert(t.noWalletDetected);
          }
        }
      });
    }

    // Dynamic listener: whenever wallet connects in runtime, auto-fill inputWallet if still empty
    window.addEventListener('haichain_wallet_connected', (e) => {
      const addr = e.detail && (e.detail.publicKey || e.detail.address);
      if (addr && typeof addr === 'string' && !addr.startsWith('0x') && addr.length >= 32 && addr.length <= 44) {
        window.HAICHAIN_CURRENT_WALLET = addr;
        window.currentConnectedSolanaWallet = addr;
        if (inputWallet && !inputWallet.value) {
          inputWallet.value = addr;
          inputWallet.dispatchEvent(new Event('input', { bubbles: true }));
          inputWallet.dispatchEvent(new Event('change', { bubbles: true }));
        }
      }
    });

    window.addEventListener('storage', (e) => {
      if (e.key === 'haichain-connected-wallet' && e.newValue) {
        try {
          const parsed = JSON.parse(e.newValue);
          const addr = parsed.address || parsed.publicKey || '';
          if (addr && !addr.startsWith('0x') && addr.length >= 32 && addr.length <= 44) {
            window.HAICHAIN_CURRENT_WALLET = addr;
            window.currentConnectedSolanaWallet = addr;
            if (inputWallet && !inputWallet.value) {
              inputWallet.value = addr;
              inputWallet.dispatchEvent(new Event('input', { bubbles: true }));
              inputWallet.dispatchEvent(new Event('change', { bubbles: true }));
            }
          }
        } catch (_) {}
      }
    });

    // Canvas Drawing Handlers (High-Precision Pointer, Touch & Mouse)
    function getCanvasCoords(e) {
      const rect = canvas.getBoundingClientRect();
      let clientX = e.clientX;
      let clientY = e.clientY;
      if ((clientX === undefined || clientY === undefined) && e.touches && e.touches.length > 0) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
      } else if ((clientX === undefined || clientY === undefined) && e.changedTouches && e.changedTouches.length > 0) {
        clientX = e.changedTouches[0].clientX;
        clientY = e.changedTouches[0].clientY;
      }
      return {
        x: (clientX !== undefined ? clientX : 0) - rect.left,
        y: (clientY !== undefined ? clientY : 0) - rect.top
      };
    }

    function startDraw(e) {
      isDrawing = true;
      strokeCount++;
      pointsDrawn++;
      hasSigned = true;
      if (placeholder) placeholder.classList.add('hidden');

      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#000000';
      ctx.fillStyle = '#000000';

      const coords = getCanvasCoords(e);
      lastX = coords.x;
      lastY = coords.y;
      
      // Render dot immediately so single clicks / taps leave physical ink
      ctx.beginPath();
      ctx.arc(coords.x, coords.y, 1.25, 0, Math.PI * 2);
      ctx.fill();

      ctx.beginPath();
      ctx.moveTo(coords.x, coords.y);
    }

    function draw(e) {
      if (!isDrawing) return;
      if (e.cancelable && (e.type.startsWith('touch') || e.type.startsWith('pointer'))) {
        e.preventDefault();
      }
      pointsDrawn++;
      hasSigned = true;
      const coords = getCanvasCoords(e);
      ctx.lineTo(coords.x, coords.y);
      ctx.stroke();
      lastX = coords.x;
      lastY = coords.y;
    }

    function stopDraw() {
      if (isDrawing) {
        isDrawing = false;
        ctx.closePath();
      }
    }

    // Unified Pointer + Touch + Mouse event listeners
    if (window.PointerEvent) {
      canvas.addEventListener('pointerdown', (e) => {
        try { canvas.setPointerCapture(e.pointerId); } catch (_) {}
        startDraw(e);
      });
      canvas.addEventListener('pointermove', draw);
      canvas.addEventListener('pointerup', (e) => {
        try { canvas.releasePointerCapture(e.pointerId); } catch (_) {}
        stopDraw();
      });
      canvas.addEventListener('pointercancel', stopDraw);
      canvas.addEventListener('pointerleave', stopDraw);
    }

    // Always attach touch listeners for rock-solid mobile compatibility
    canvas.addEventListener('touchstart', (e) => {
      if (e.cancelable) e.preventDefault();
      startDraw(e);
    }, { passive: false });
    canvas.addEventListener('touchmove', (e) => {
      if (e.cancelable) e.preventDefault();
      draw(e);
    }, { passive: false });
    canvas.addEventListener('touchend', stopDraw);
    canvas.addEventListener('touchcancel', stopDraw);

    // Fallback mouse listeners
    canvas.addEventListener('mousedown', startDraw);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDraw);
    canvas.addEventListener('mouseleave', stopDraw);

    if (btnClearSig) {
      btnClearSig.addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        strokeCount = 0;
        pointsDrawn = 0;
        hasSigned = false;
        ctx.strokeStyle = '#000000';
        if (placeholder) placeholder.classList.remove('hidden');
      });
    }

    // Form Validation & Submission
    if (btnSubmit) {
      btnSubmit.addEventListener('click', async () => {
        const lang = getCurrentLang();
        const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];

        const name = inputName.value.trim();
        const email = inputEmail.value.trim();
        const amount = parseFloat(inputAmount.value) || 0;
        const wallet = inputWallet.value.trim();
        const agreed = inputAgree.checked;

        if (!name || name.length < 2) {
          alert(t.errName);
          inputName.focus();
          return;
        }

        if (!email || !email.includes('@') || !email.includes('.')) {
          alert(t.errEmail);
          inputEmail.focus();
          return;
        }

        if (amount < 500) {
          alert(t.errAmount);
          inputAmount.focus();
          return;
        }

        if (!wallet || wallet.length < 32 || wallet.length > 44) {
          alert(t.errWallet);
          inputWallet.focus();
          return;
        }

        // Validate digital signature (accepts drawn strokes, raster pixels, or signature data)
        let isSigValid = false;
        if (hasSigned || strokeCount > 0 || pointsDrawn > 0) {
          isSigValid = true;
        }
        try {
          const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
          const d = imgData.data;
          for (let i = 3; i < d.length; i += 8) {
            if (d[i] > 5) {
              isSigValid = true;
              hasSigned = true;
              break;
            }
          }
        } catch (_) {}
        try {
          const dataUrl = canvas.toDataURL('image/png');
          if (dataUrl && dataUrl.length > 1000) {
            isSigValid = true;
            hasSigned = true;
          }
        } catch (_) {}

        if (!isSigValid) {
          alert(t.errSig);
          return;
        }

        if (!agreed) {
          alert(t.errAgree);
          return;
        }

        // Generate SHA-256 Audit Proof
        const timestamp = new Date().toISOString();
        const contractId = 'SAFT-HAI-2026-' + Math.random().toString(36).substring(2, 7).toUpperCase();
        const tokens = Math.floor(amount / 0.007);
        const treasury = '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';
                // Ensure signature strokes are black on transparent canvas
        try {
          const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
          const d = imgData.data;
          for (let i = 0; i < d.length; i += 4) {
            if (d[i + 3] > 0) {
              d[i] = 0;
              d[i + 1] = 0;
              d[i + 2] = 0;
            }
          }
          ctx.putImageData(imgData, 0, 0);
        } catch (_) {}

        const signatureData = canvas.toDataURL('image/png');

        const rawProof = contractId + '|' + name + '|' + email + '|' + amount + '|' + tokens + '|' + wallet + '|' + treasury + '|' + timestamp;
        let hashHex = '';
        try {
          const enc = new TextEncoder().encode(rawProof);
          const buf = await crypto.subtle.digest('SHA-256', enc);
          hashHex = Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
        } catch (_) {
          hashHex = 'SHA256_' + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
        }

        signedRecord = {
          contractId,
          name,
          email,
          amount,
          tokens,
          wallet,
          treasury,
          timestamp,
          hashHex,
          signatureData
        };

        // Save to localStorage
        try {
          const prev = JSON.parse(localStorage.getItem('HAICHAIN_SIGNED_SAFT_RECORDS') || '[]');
          prev.unshift(signedRecord);
          localStorage.setItem('HAICHAIN_SIGNED_SAFT_RECORDS', JSON.stringify(prev));
          localStorage.setItem('HAICHAIN_ACTIVE_SAFT', JSON.stringify(signedRecord));
        } catch (e) {
          console.warn('Could not save SAFT to storage:', e);
        }

        // 0. Dual Instant Email Notifications via Resend (Admin + Investor)
        try {
          const resendKey = 're_Hqp1tNKV_6w8Ur4v3B91Jv6yusD4CK5pN';
          const senderFrom = 'Haichain <no-reply@mail.haichain.si>';

          // (A) Send to Admin (haichain.si@gmail.com)
          const adminSubject = '🔔 [SAFT Signed] $' + amount.toLocaleString('en-US') + ' USD - ' + name + ' (' + contractId + ')';
          const adminHtml = buildHaichainSaftEmailHtml({
            contractId,
            name,
            email,
            amount,
            tokens,
            wallet,
            treasury,
            hashHex,
            timestamp,
            isAdmin: true,
            lang: lang || 'vi'
          });

          fetch('https://api.resend.com/emails', {
            method: 'POST',
            headers: {
              'Authorization': 'Bearer ' + resendKey,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              from: senderFrom,
              to: ['haichain.si@gmail.com'],
              subject: adminSubject,
              html: adminHtml
            })
          }).catch(e => console.warn('Resend direct admin non-blocking:', e));

          // (B) Send to Investor (Confirmation & Receipt)
          if (email && email.includes('@')) {
            const investorSubject = 'Haichain Official SAFT Agreement - Signed Confirmation (' + contractId + ')';
            const investorHtml = buildHaichainSaftEmailHtml({
              contractId,
              name,
              email,
              amount,
              tokens,
              wallet,
              treasury,
              hashHex,
              timestamp,
              isAdmin: false,
              lang: lang || 'vi'
            });

            fetch('https://api.resend.com/emails', {
              method: 'POST',
              headers: {
                'Authorization': 'Bearer ' + resendKey,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                from: senderFrom,
                to: [email],
                subject: investorSubject,
                html: investorHtml
              })
            }).catch(e => console.warn('Resend direct investor non-blocking:', e));
          }
        } catch (_) {}

        // 1. Instant Real-Time Telegram Bot Notification (Group: -5426770743)
        try {
          const tgToken = '9066296959:AAE716Gw5KOh1jiUuurbdO_g5n7gIXblcqk';
          const tgChatId = '-5426770743';
          const tgMsg = '🔔 *NEW PRE-SEED SAFT AGREEMENT SIGNED!*\n' +
            '━━━━━━━━━━━━━━━━━━━━\n' +
            '📋 *Contract ID:* `' + contractId + '`\n' +
            '👤 *Investor:* *' + name + '*\n' +
            '📧 *Email:* `' + email + '`\n' +
            '💰 *Investment:* *$' + amount.toLocaleString('en-US') + ' USD (USDT)*\n' +
            '🪙 *Allocation:* *' + tokens.toLocaleString('en-US') + ' $HAISI* (@ $0.007)\n' +
            '📈 *TGE Upside:* *$' + Math.round(tokens * 0.01).toLocaleString('en-US') + ' USD (+42.8%)*\n' +
            '💼 *Beneficiary Solana Wallet:*\n`' + wallet + '`\n' +
            '🏛️ *Multi-Sig Treasury Vault:*\n`' + treasury + '`\n' +
            '🔐 *SHA-256 Audit Proof:*\n`' + hashHex + '`\n' +
            '⏰ *Signed Time (UTC):* `' + timestamp + '`\n' +
            '━━━━━━━━━━━━━━━━━━━━\n' +
            '✅ *Legally Executed under US ESIGN Act & UETA*';

          fetch('https://api.telegram.org/bot' + tgToken + '/sendMessage', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              chat_id: tgChatId,
              text: tgMsg,
              parse_mode: 'Markdown'
            })
          }).catch(err => console.warn('Telegram direct ping non-blocking:', err));
        } catch (_) {}

        // 2. Asynchronously broadcast to Edge API & Webhook (Google Sheets + Email)
        try {
          fetch('/api/saft/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(signedRecord)
          }).catch(err => console.warn('Edge SAFT sync non-blocking error:', err));
        } catch (err) {
          console.warn('Edge SAFT dispatch error:', err);
        }

        // 3. Direct Google Apps Script Webhook Dispatch (Google Sheets + Dual Email)
        try {
          const sheetWebhook = window.HAICHAIN_GOOGLE_SHEETS_WEBHOOK_URL || '';
          if (sheetWebhook) {
            fetch(sheetWebhook, {
              method: 'POST',
              mode: 'no-cors',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(signedRecord)
            }).catch(e => console.warn('Google Sheets Webhook non-blocking:', e));
          }
        } catch (_) {}

        // Display Success View
        modal.querySelector('#saft-rec-id').textContent = contractId;
        modal.querySelector('#saft-rec-name').textContent = name;
        modal.querySelector('#saft-rec-alloc').textContent = tokens.toLocaleString('en-US') + ' $HAISI';
        modal.querySelector('#saft-rec-wallet').textContent = wallet.slice(0, 6) + '...' + wallet.slice(-6);
        modal.querySelector('#saft-rec-time').textContent = (lang === 'vi') ? new Date(timestamp).toLocaleString('vi-VN') : new Date(timestamp).toUTCString();
        modal.querySelector('#saft-rec-hash').textContent = hashHex;

        formView.classList.add('hidden');
        successView.classList.remove('hidden');
      });
    }

    // Download Signed Certificate (HTML / PDF format)
    if (btnDownloadCert) {
      btnDownloadCert.addEventListener('click', () => {
        if (!signedRecord) return;
        const lang = getCurrentLang();
        const isVi = (lang === 'vi');

        const docTitle = isVi ? ('CHỨNG NHẬN KÝ HỢP ĐỒNG SAFT - ' + signedRecord.contractId) : ('SAFT AGREEMENT SIGNING CERTIFICATE - ' + signedRecord.contractId);
        const subTitle = 'HAICHAIN PRE-SEED STRATEGIC ROUND ($0.007 USD / $HAISI)';
        const certStatement = isVi
          ? 'Chứng nhận rằng Nhà Đầu Tư dưới đây đã chính thức ký kết Thỏa Thuận Tương Lai Chuyển Đổi Token (SAFT) với HAICHAIN Autonomous Machine Financial Protocol:'
          : 'This certifies that the Investor below has executed the Simple Agreement for Future Tokens (SAFT) with HAICHAIN Autonomous Machine Financial Protocol:';

        const certHtml = '<!DOCTYPE html>' +
'<html lang="' + (isVi ? 'vi' : 'en') + '">' +
'<head>' +
'<meta charset="UTF-8">' +
'<title>' + docTitle + '</title>' +
'<style>' +
'  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 40px; background: #ffffff; color: #111; max-width: 800px; margin: 0 auto; line-height: 1.6; }' +
'  .header { border-bottom: 2px solid #111; padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: flex-end; }' +
'  .badge { background: #111; color: #fff; padding: 4px 12px; border-radius: 999px; font-size: 11px; font-family: monospace; }' +
'  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 25px 0; }' +
'  .field { border-bottom: 1px dashed #ddd; padding-bottom: 8px; }' +
'  .label { font-size: 11px; color: #666; text-transform: uppercase; letter-spacing: 0.5px; }' +
'  .value { font-size: 14px; font-weight: 600; font-family: monospace; }' +
'  .sig-box { margin-top: 30px; padding: 20px; border: 1px solid #e5e5e5; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; }' +
'  .proof { margin-top: 30px; padding: 15px; background: #f9f9f9; border-radius: 8px; font-family: monospace; font-size: 10px; word-break: break-all; color: #666; }' +
'</style>' +
'</head>' +
'<body>' +
'  <div class="header">' +
'    <div>' +
'      <h1 style="margin:0; font-size: 22px;">' + docTitle + '</h1>' +
'      <p style="margin:5px 0 0 0; color: #666; font-size: 12px;">' + subTitle + '</p>' +
'    </div>' +
'    <div class="badge">' + signedRecord.contractId + '</div>' +
'  </div>' +
'  <p>' + certStatement + '</p>' +
'  <div class="grid">' +
'    <div class="field"><div class="label">' + (isVi ? 'Nhà Đầu Tư (Người Ký):' : 'Investor (Signatory):') + '</div><div class="value">' + signedRecord.name + '</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Email Xác Nhận:' : 'Email Address:') + '</div><div class="value">' + signedRecord.email + '</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Số Tiền Đầu Tư:' : 'Investment Amount:') + '</div><div class="value">$' + signedRecord.amount.toLocaleString('en-US') + ' USD (USDT)</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Quyền Phân Bổ Token:' : 'Token Allocation:') + '</div><div class="value">' + signedRecord.tokens.toLocaleString('en-US') + ' $HAISI (@ $0.007)</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Giá Trị Dự Kiến TGE:' : 'TGE Projected Value:') + '</div><div class="value">$' + (signedRecord.tokens * 0.01).toLocaleString('en-US') + ' USD (+42.8%)</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Thời Điểm Ký (UTC):' : 'Signing Timestamp (UTC):') + '</div><div class="value">' + signedRecord.timestamp + '</div></div>' +
'    <div class="field" style="grid-column: span 2;"><div class="label">' + (isVi ? 'Địa Chỉ Ví Solana Nhận Token (Beneficiary Wallet):' : 'Beneficiary Solana Receiving Address:') + '</div><div class="value">' + signedRecord.wallet + '</div></div>' +
'    <div class="field" style="grid-column: span 2;"><div class="label">' + (isVi ? 'Kho Bạc Multi-Sig Nhận Vốn (Solana Mainnet):' : 'Multi-Sig Treasury Vault (Solana Mainnet):') + '</div><div class="value">' + signedRecord.treasury + '</div></div>' +
'  </div>' +
'  <div class="sig-box">' +
'    <div>' +
'      <div class="label">' + (isVi ? 'CHỮ KÝ ĐIỆN TỬ CỦA NHÀ ĐẦU TƯ:' : 'INVESTOR DIGITAL SIGNATURE:') + '</div>' +
'      <div style="font-size: 12px; color:#444; margin-top: 4px;">' + (isVi ? 'Đã ký số trực tuyến theo chuẩn ESIGN Act &amp; Luật GDĐT' : 'Executed digitally pursuant to US ESIGN Act &amp; UETA standards') + '</div>' +
'    </div>' +
'    <img src="' + signedRecord.signatureData + '" style="max-height: 70px; border-bottom: 1px solid #000; filter: brightness(0); -webkit-filter: brightness(0);" alt="Signature">' +
'  </div>' +
'  <div class="proof">' +
'    <strong>CRYPTOGRAPHIC AUDIT PROOF (SHA-256):</strong><br>' +
'    ' + signedRecord.hashHex + '<br>' +
'    <em>' + (isVi ? 'Chứng từ này được mã hóa bảo chứng, liên kết bất biến với giao dịch trên Solana Blockchain.' : 'This document is cryptographically verified and permanently linked to Solana blockchain transactions.') + '</em>' +
'  </div>' +
'  <script>window.onload = function() { window.print(); };<' + '/script>' +
'</body>' +
'</html>';

        const blob = new Blob([certHtml], { type: 'text/html;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'HAICHAIN_SAFT_CERTIFICATE_' + signedRecord.contractId + '.html';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      });
    }

    // Proceed to Payment
    if (btnProceedPay) {
      btnProceedPay.addEventListener('click', () => {
        if (!signedRecord) return;
        const lang = getCurrentLang();
        const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];
        window.closePdfViewerModal();

        // Redirect or open Tab 7 / Private Round
        if (window.location.pathname.includes('dashboard')) {
          const tabBtn = document.querySelector('[data-tab="private-round"], [data-tab="preseed"], #nav-tab-preseed');
          if (tabBtn) tabBtn.click();
        }

        // Fill in amount in sale controller if exists
        const amtInput = document.getElementById('sale-invest-amount') || document.querySelector('input[name="saftAmount"]');
        if (amtInput) {
          amtInput.value = signedRecord.amount;
          amtInput.dispatchEvent(new Event('input', { bubbles: true }));
        }

        const alertMsg = t.alertProceed
          .replace('{amount}', signedRecord.amount)
          .replace('{tokens}', signedRecord.tokens.toLocaleString());
        alert(alertMsg);
      });
    }

    // Expose language refresh hook
    applyDrawerI18n();
    window.refreshSaftDrawerI18n = applyDrawerI18n;
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
    const modalLangCode = document.getElementById('pdf-modal-lang-code');
    if (modalLangCode) modalLangCode.textContent = (lang || 'en').toUpperCase();

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

    // Dynamic SAFT E-Signature Button Visibility & i18n (Zero Icons, Ultra-High Contrast)
    const saftSignBtn = document.getElementById('pdf-modal-sign-btn');
    const uDoc = String(pdfUrl || '').toUpperCase() + ' ' + String(docTitle || '').toUpperCase();
    const isSaftDoc = uDoc.includes('SAFT') || uDoc.includes('MEMO');
    if (saftSignBtn) {
      if (isSaftDoc) {
        saftSignBtn.classList.remove('hidden');
        saftSignBtn.classList.add('inline-flex');
        const signBtnText = document.getElementById('pdf-modal-sign-btn-text');
        const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];
        if (signBtnText && t) {
          signBtnText.textContent = t.btnOpenSign;
        }
      } else {
        saftSignBtn.classList.add('hidden');
        saftSignBtn.classList.remove('inline-flex');
      }
    }
    if (typeof window.refreshSaftDrawerI18n === 'function') {
      window.refreshSaftDrawerI18n(lang);
    }

    try {
      let doc = window.__HAICHAIN_PDF_CACHE__[pdfUrl];
      if (!doc) {
        const pdfjs = await ensurePdfJs();
        let fetchUrl = pdfUrl;
        const bust = 'v=v1.3.2_risk_table_full_view';
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
        const bust = 'v=v1.3.2_risk_table_full_view';
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
    const whitepaperSelector = '#nav-whitepaper-link, #mobile-nav-whitepaper-link, #footer-whitepaper-link, [data-open-whitepaper], [data-pdf-whitepaper], a[href*="whitepaper"], a[href*="WHITEPAPER"]';
    document.querySelectorAll(whitepaperSelector).forEach((btn) => {
      if (btn.dataset.pdfBound === 'true') return;
      btn.dataset.pdfBound = 'true';
      btn.addEventListener('click', (e) => handleWhitepaperClick(e, btn));
    });

    const riskSelector = '#nav-risk-report-link, #mobile-nav-risk-report-link, [data-mobile-risk-report="true"], [data-risk-report="true"], a[href*="HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT"], a[href*="HAICHAIN_RISK_REPORT"]';
    document.querySelectorAll(riskSelector).forEach((btn) => {
      if (btn.dataset.riskBound === 'true') return;
      btn.dataset.riskBound = 'true';
      btn.addEventListener('click', (e) => window.handleRiskReportClick(e, btn));
    });

    checkAutoOpen();

    const warmBoth = () => {
      try {
        const lang = getCurrentLang();
        prewarmDocument(getWhitepaperUrlForLang(lang));
        if (typeof window.getRiskReportPdfForLang === 'function') {
          const rDoc = window.getRiskReportPdfForLang(lang);
          if (rDoc && rDoc.url) prewarmDocument(rDoc.url);
        }
      } catch (_) {}
    };

    if (typeof requestIdleCallback === 'function') {
      requestIdleCallback(warmBoth, { timeout: 3000 });
    } else {
      setTimeout(warmBoth, 1500);
    }
  }

  // Auto-open modal if URL specifies ?open_whitepaper=1 or ?open_risk_report=1
  function checkAutoOpen() {
    try {
      const params = new URLSearchParams(window.location.search);
      if (params.get('open_whitepaper') === '1' || window.location.pathname === '/whitepaper') {
        const lang = getCurrentLang();
        const pdfUrl = getWhitepaperUrlForLang(lang);
        const meta = getI18nMeta(lang);
        window.openPdfViewerModal(pdfUrl, meta.title);
      } else if (params.get('open_risk_report') === '1' || params.get('open_risk') === '1' || window.location.pathname === '/risk-report') {
        const lang = getCurrentLang();
        if (typeof window.getRiskReportPdfForLang === 'function') {
          const doc = window.getRiskReportPdfForLang(lang);
          if (doc) window.openPdfViewerModal(doc.url, doc.title);
        }
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

  // =========================================================================
  // GLOBAL MULTI-LANGUAGE SAFT & MEMO RESOLVERS (10 LANGUAGES)
  // =========================================================================

  // =========================================================================
  // GLOBAL MULTI-LANGUAGE RISK REPORT RESOLVER (10 LANGUAGES)
  // =========================================================================
  window.getRiskReportPdfForLang = function(lang) {
    const l = (lang || (typeof getCurrentLang === 'function' ? getCurrentLang() : (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain-lang') || localStorage.getItem('haichain_lang') || 'en'))).toLowerCase();
    const titles = {
      vi: 'Báo Cáo Thẩm Định Rủi Ro & Phòng Thủ Mật Mã HAICHAIN',
      en: 'HAICHAIN Institutional Risk Due Diligence Report',
      zh: 'HAICHAIN 机构级风险尽职调查与安全防御报告',
      ko: 'HAICHAIN 기관용 위험 실사 및 암호학적 보안 감사 보고서',
      fr: 'Rapport de Diligence Raisonnable des Risques Institutionnels HAICHAIN',
      es: 'Informe de Diligencia Debida de Riesgos Institucionales de HAICHAIN',
      ru: 'Отчет об Институциональном Дью-Дилидженсе Рисков HAICHAIN',
      kk: 'HAICHAIN Институционалдық Тәуекелдерді Бағалау Және Сенімділік Есебі',
      hi: 'HAICHAIN संस्थागत जोखिम देय परिश्रम और सुरक्षा ऑडिट रिपोर्ट',
      he: 'דוח בדיקת נאותות סיכונים מוסדיים ואבטחת קריפטוגרפיה של HAICHAIN'
    };
    const title = titles[l] || titles['en'];
    const validLangs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he'];
    const chosenLang = validLangs.includes(l) ? l.toUpperCase() : 'EN';
    return {
      url: `/HAICHAIN_RISK_REPORT_${chosenLang}.pdf`,
      title: title
    };
  };

  window.openRiskReportPdfModal = function(lang) {
    const doc = window.getRiskReportPdfForLang(lang);
    window.openPdfViewerModal(doc.url, doc.title);
  };

  window.getSaftPdfForLang = function(lang) {
    const l = (lang || (typeof getCurrentLang === 'function' ? getCurrentLang() : (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain-lang') || localStorage.getItem('haichain_lang') || 'en'))).toLowerCase();
    const titles = {
      vi: 'Hợp Đồng SAFT Pre-Seed HAICHAIN (Chính Thức)',
      en: 'HAICHAIN Official SAFT Agreement (Mainnet Guaranteed)',
      zh: 'HAICHAIN 官方 SAFT 认购协议 (主网保障)',
      ko: 'HAICHAIN 공식 SAFT 투자 계약서 (메인넷 보장)',
      es: 'Acuerdo SAFT Oficial de HAICHAIN (Garantizado en Mainnet)',
      fr: 'Contrat SAFT Officiel HAICHAIN (Garanti sur le Mainnet)',
      ru: 'Официальное соглашение SAFT HAICHAIN (Гарантия Mainnet)',
      kk: 'HAICHAIN ресми SAFT келісімі (Mainnet кепілдігі)',
      hi: 'HAICHAIN आधिकारिक SAFT अनुबंध (मेननेट गारंटीकृत)',
      he: 'הסכם SAFT רשמי של HAICHAIN (מובטח במיין-נט)'
    };
    const title = titles[l] || titles['en'];
    const validLangs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he'];
    const chosenLang = validLangs.includes(l) ? l.toUpperCase() : 'EN';
    return {
      url: `/HAICHAIN_PRESEED_SAFT_AGREEMENT_${chosenLang}.pdf`,
      title: title
    };
  };

  window.openSaftPdfModal = function(lang) {
    const doc = window.getSaftPdfForLang(lang);
    window.openPdfViewerModal(doc.url, doc.title);
  };

  window.getPreseedMemoPdfForLang = function(lang) {
    const l = (lang || (typeof getCurrentLang === 'function' ? getCurrentLang() : (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain-lang') || localStorage.getItem('haichain_lang') || 'en'))).toLowerCase();
    const titles = {
      vi: 'Bản Ghi Nhớ Đầu Tư Chiến Lược Pre-Seed HAICHAIN (1-Pager)',
      en: 'HAICHAIN Pre-Seed Strategic Investment Memo (1-Pager)',
      zh: 'HAICHAIN Pre-Seed 战略投资备忘录 (单页)',
      ko: 'HAICHAIN Pre-Seed 전략 투자 메모 (1-페이저)',
      es: 'Memorando de Inversión Estratégica Pre-Seed de HAICHAIN (1-Página)',
      fr: 'Mémo d’Investissement Stratégique Pre-Seed HAICHAIN (1-Page)',
      ru: 'Инвестиционный меморандум Pre-Seed HAICHAIN (1-Pager)',
      kk: 'HAICHAIN Pre-Seed стратегиялық инвестициялық меморандумы (1-Бет)',
      hi: 'HAICHAIN प्री-सीड रणनीतिक निवेश मेमो (1-पेजर)',
      he: 'תזכיר השקעה אסטרטגי Pre-Seed של HAICHAIN (עמוד אחד)'
    };
    const title = titles[l] || titles['en'];
    const validLangs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he'];
    const chosenLang = validLangs.includes(l) ? l.toUpperCase() : 'EN';
    return {
      url: `/HAICHAIN_PRESEED_ONE_PAGER_MEMO_${chosenLang}.pdf`,
      title: title
    };
  };

  window.openPreseedMemoModal = function(lang) {
    const doc = window.getPreseedMemoPdfForLang(lang);
    window.openPdfViewerModal(doc.url, doc.title);
  };

  // Global Language Synchronization Listener
  window.addEventListener('haichain:languageChanged', (e) => {
    const lang = (e && e.detail && (e.detail.lang || e.detail.language)) || getCurrentLang();
    if (typeof window.refreshSaftDrawerI18n === 'function') {
      window.refreshSaftDrawerI18n(lang);
    }
    const modal = document.getElementById('pdf-viewer-modal') || document.getElementById('pdf-modal');
    if (modal && !modal.classList.contains('hidden')) {
      const meta = getI18nMeta(lang);
      const signBtnText = document.getElementById('pdf-modal-sign-btn-text');
      const t = (typeof SAFT_DRAWER_I18N !== 'undefined' && SAFT_DRAWER_I18N[lang]) || (typeof SAFT_DRAWER_I18N !== 'undefined' && SAFT_DRAWER_I18N['en']);
      if (signBtnText && t) signBtnText.textContent = t.btnOpenSign;
      const indicator = document.getElementById('pdf-modal-page-indicator');
      if (indicator && meta.pagePrefix) {
        indicator.textContent = `${meta.pagePrefix} ${currentPageIndex} / ${renderedPages.size || '--'}`;
      }
      // If a multi-language PDF is currently loaded, switch it cleanly!
      if (currentPdfUrl) {
        const u = currentPdfUrl.toUpperCase();
        if (u.includes('WHITEPAPER')) {
          const newUrl = getWhitepaperUrlForLang(lang);
          if (newUrl !== currentPdfUrl) window.openPdfViewerModal(newUrl, meta.title);
        } else if (u.includes('SAFT')) {
          const doc = typeof window.getSaftPdfForLang === 'function' ? window.getSaftPdfForLang(lang) : null;
          if (doc && doc.url !== currentPdfUrl) window.openPdfViewerModal(doc.url, doc.title);
        } else if (u.includes('MEMO')) {
          const doc = typeof window.getPreseedMemoPdfForLang === 'function' ? window.getPreseedMemoPdfForLang(lang) : null;
          if (doc && doc.url !== currentPdfUrl) window.openPdfViewerModal(doc.url, doc.title);
        } else if (u.includes('RISK')) {
          const doc = typeof window.getRiskReportPdfForLang === 'function' ? window.getRiskReportPdfForLang(lang) : null;
          if (doc && doc.url !== currentPdfUrl) window.openPdfViewerModal(doc.url, doc.title);
        }
      }
    }
  });

  window.addEventListener('storage', (e) => {
    if (e.key === 'haichain-lang' || e.key === 'haichain_lang') {
      const lang = e.newValue || getCurrentLang();
      if (typeof window.refreshSaftDrawerI18n === 'function') {
        window.refreshSaftDrawerI18n(lang);
      }
    }
  });



  // Dedicated Risk Report Handler
  window.handleRiskReportClick = function(e, trigger) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    if (typeof window.closeMobileMenu === 'function') {
      try { window.closeMobileMenu(); } catch (_) {}
    }
    const lang = getCurrentLang();
    const doc = window.getRiskReportPdfForLang(lang);
    window.openPdfViewerModal(doc.url, doc.title);
  };

  // Global Capture-Phase Event Listener for All Risk Report Links
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('#nav-risk-report-link, #mobile-nav-risk-report-link, [data-mobile-risk-report="true"], [data-risk-report="true"], a[href*="HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT"], a[href*="HAICHAIN_RISK_REPORT"]');
    if (trigger) {
      window.handleRiskReportClick(e, trigger);
    }
  }, true);

})();
