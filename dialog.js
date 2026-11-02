/**
 * HAICHAIN Universal Dialog System v2.0
 * Architecture: Apple Luxury Monochrome & Titanium Minimalist
 * Responsive: Native Bottom Sheet on Mobile (<640px), Centered Modal on Desktop
 * Seamlessly integrates with HAICHAIN Dashboard theme and replaces native browser alert() & confirm()
 */

(function () {
  'use strict';

  // 1. INJECT STYLES
  const styleEl = document.createElement('style');
  styleEl.textContent = `
    .hc-dialog-overlay {
      position: fixed;
      inset: 0;
      z-index: 100000;
      display: flex;
      align-items: flex-end;
      justify-content: center;
      padding: 0;
      background-color: rgba(0, 0, 0, 0.72);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      opacity: 0;
      pointer-events: none;
      transition: opacity 220ms cubic-bezier(0.16, 1, 0.3, 1);
    }
    @media (min-width: 640px) {
      .hc-dialog-overlay {
        align-items: center;
        padding: 1.25rem;
      }
    }
    .hc-dialog-overlay.hc-active {
      opacity: 1;
      pointer-events: auto;
    }
    .hc-dialog-card {
      position: relative;
      width: 100%;
      max-width: 30rem;
      border-top-left-radius: 1.75rem;
      border-top-right-radius: 1.75rem;
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
      padding: 1.25rem 1.25rem 1.5rem 1.25rem;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.6);
      transform: translateY(100%);
      transition: transform 260ms cubic-bezier(0.16, 1, 0.3, 1);
      box-sizing: border-box;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
    }
    @media (min-width: 640px) {
      .hc-dialog-card {
        border-radius: 1.75rem;
        padding: 1.5rem 1.75rem;
        transform: scale(0.95) translateY(8px);
        max-height: 85vh;
      }
    }
    .hc-dialog-overlay.hc-active .hc-dialog-card {
      transform: translateY(0);
    }
    @media (min-width: 640px) {
      .hc-dialog-overlay.hc-active .hc-dialog-card {
        transform: scale(1) translateY(0);
      }
    }
    .hc-dialog-scroll {
      overflow-y: auto;
      scrollbar-width: none;
      -ms-overflow-style: none;
    }
    .hc-dialog-scroll::-webkit-scrollbar {
      display: none;
    }
  `;
  document.head.appendChild(styleEl);

  // 2. SVG ICONS
  const ICONS = {
    wallet: `
      <svg class="w-5 h-5 text-neutral-900 dark:text-neutral-100" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/>
      </svg>
    `,
    danger: `
      <svg class="w-5 h-5 text-rose-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
    `,
    warning: `
      <svg class="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    `,
    success: `
      <svg class="w-5 h-5 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
      </svg>
    `,
    info: `
      <svg class="w-5 h-5 text-neutral-700 dark:text-neutral-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    `
  };

  const BADGE_STYLES = {
    wallet: 'bg-neutral-100 dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-700 text-black dark:text-white',
    danger: 'bg-rose-50 dark:bg-rose-950/60 border border-rose-200 dark:border-rose-900/60 text-rose-600 dark:text-rose-400',
    warning: 'bg-amber-50 dark:bg-amber-950/60 border border-amber-200 dark:border-amber-900/60 text-amber-700 dark:text-amber-400',
    success: 'bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200 dark:border-emerald-900/60 text-emerald-700 dark:text-emerald-400',
    info: 'bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-800 dark:text-neutral-200'
  };

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function parseMessage(msg) {
    if (typeof msg !== 'string') msg = String(msg || '');
    let title = '';
    let body = '';
    let type = 'info';

    // Parse title if separated by double newline or colon at start
    const doubleNl = msg.indexOf('\n\n');
    if (doubleNl !== -1 && doubleNl < 100) {
      title = msg.substring(0, doubleNl).replace(/:\s*$/, '').trim();
      body = msg.substring(doubleNl + 2).trim();
    } else if (msg.includes('\n')) {
      const firstNl = msg.indexOf('\n');
      if (firstNl < 100) {
        title = msg.substring(0, firstNl).replace(/:\s*$/, '').trim();
        body = msg.substring(firstNl + 1).trim();
      } else {
        body = msg.trim();
      }
    } else {
      body = msg.trim();
    }

    const lower = (title + ' ' + body).toLowerCase();

    if (lower.includes('purchase') || lower.includes('thanh toán') || lower.includes('saft') || lower.includes('wallet') || lower.includes('metamask') || lower.includes('phantom') || lower.includes('solflare')) {
      type = 'wallet';
      if (!title) title = 'HAICHAIN Web3 Transaction';
    } else if (lower.includes('emergency') || lower.includes('kill-switch') || lower.includes('revoke') || lower.includes('frozen') || lower.includes('panic') || lower.includes('critical')) {
      type = 'danger';
      if (!title) title = 'Emergency Action';
    } else if (lower.includes('success') || lower.includes('thành công') || lower.includes('activated') || lower.includes('credited') || lower.includes('confirmed')) {
      type = 'success';
      if (!title) title = 'Confirmed';
    } else if (lower.includes('not connected') || lower.includes('invalid') || lower.includes('cancel') || lower.includes('rejected') || lower.includes('denied') || lower.includes('từ chối') || lower.includes('hủy')) {
      type = 'warning';
      if (!title) title = 'Notice';
    } else {
      type = 'info';
      if (!title) title = 'HAICHAIN System';
    }

    return { title, body, type };
  }

  function formatBodyHtml(body) {
    if (!body) return '';

    // Split body into main sections (bullet blocks vs normal paragraphs)
    const lines = body.split('\n');
    const bulletLines = [];
    const regularLines = [];
    let inBullets = false;

    lines.forEach(line => {
      const trimmed = line.trim();
      if (trimmed.startsWith('•') || trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
        inBullets = true;
        bulletLines.push(trimmed.replace(/^[•\-\*]\s*/, ''));
      } else if (inBullets && trimmed && !trimmed.includes(':') && bulletLines.length > 0) {
        // Multi-line value belonging to the previous bullet item (like a standalone long address)
        bulletLines[bulletLines.length - 1] += ' ' + trimmed;
      } else if (trimmed) {
        regularLines.push(trimmed);
      }
    });

    let html = '';

    // 1. Render structured bullet card if present
    if (bulletLines.length > 0) {
      html += `<div class="my-3 p-3.5 sm:p-4 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2.5 font-sans">`;
      bulletLines.forEach(item => {
        const colonIdx = item.indexOf(':');
        if (colonIdx !== -1) {
          const key = escapeHtml(item.substring(0, colonIdx).trim());
          const val = escapeHtml(item.substring(colonIdx + 1).trim());
          const isAddressOrHash = val.length > 25 && !val.includes(' ');
          html += `
            <div class="flex flex-col sm:flex-row sm:items-baseline justify-between py-1 border-b border-neutral-100 dark:border-neutral-800/60 last:border-0 gap-1">
              <span class="text-[11px] font-semibold text-neutral-500 dark:text-neutral-400 font-sans tracking-wide shrink-0">${key}:</span>
              ${isAddressOrHash ? `
                <span class="font-mono text-[11px] text-neutral-800 dark:text-neutral-200 px-2 py-0.5 rounded-lg bg-neutral-100 dark:bg-neutral-800/90 break-all select-all font-semibold leading-relaxed">${val}</span>
              ` : `
                <span class="font-mono text-xs sm:text-[13px] font-bold text-neutral-900 dark:text-white break-all sm:text-right">${val}</span>
              `}
            </div>
          `;
        } else {
          html += `
            <div class="flex items-start space-x-2 py-0.5 text-xs text-neutral-700 dark:text-neutral-300">
              <span class="text-neutral-400 mt-0.5">•</span>
              <span>${escapeHtml(item)}</span>
            </div>
          `;
        }
      });
      html += `</div>`;
    }

    // 2. Render regular paragraphs / callout notes
    if (regularLines.length > 0) {
      regularLines.forEach(para => {
        const pEsc = escapeHtml(para);
        const lower = pEsc.toLowerCase();
        if (lower.includes('wallet will open') || lower.includes('sẽ mở lên') || lower.includes('redirecting') || lower.includes('chuyển bạn đến')) {
          html += `
            <div class="p-3 rounded-2xl bg-neutral-100/70 dark:bg-neutral-900/80 border border-neutral-200/80 dark:border-neutral-800 flex items-center space-x-2.5 text-xs text-neutral-600 dark:text-neutral-300 font-sans mt-2.5">
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
              <span class="font-medium">${pEsc}</span>
            </div>
          `;
        } else {
          html += `<p class="leading-relaxed text-xs sm:text-[13px] text-neutral-600 dark:text-neutral-300 font-sans mt-2 first:mt-0">${pEsc}</p>`;
        }
      });
    }

    return html;
  }

  // 3. DIALOG MANAGER
  class DialogManager {
    constructor() {
      this.overlay = null;
      this.activeResolve = null;
      this._initDom();
    }

    _initDom() {
      if (document.getElementById('hc-dialog-root')) return;

      this.overlay = document.createElement('div');
      this.overlay.id = 'hc-dialog-root';
      this.overlay.className = 'hc-dialog-overlay';
      this.overlay.innerHTML = `
        <div class="hc-dialog-card bg-white dark:bg-[#0c0c0c] border border-neutral-200 dark:border-neutral-800 text-neutral-900 dark:text-neutral-100 shadow-2xl">
          <!-- Mobile Drag Handle Bar -->
          <div class="sm:hidden w-10 h-1 bg-neutral-300 dark:bg-neutral-700 rounded-full mx-auto mb-2.5 shrink-0"></div>

          <!-- Header -->
          <div class="flex items-center justify-between pb-3 border-b border-neutral-100 dark:border-neutral-800/80 shrink-0">
            <div class="flex items-center space-x-3 min-w-0 flex-1 pr-2">
              <div id="hc-dialog-icon-wrapper" class="w-9 h-9 sm:w-10 sm:h-10 rounded-2xl flex items-center justify-center shrink-0"></div>
              <div class="min-w-0 flex-1">
                <h3 id="hc-dialog-title" class="text-sm sm:text-base font-bold text-neutral-900 dark:text-white tracking-tight truncate leading-tight"></h3>
                <p id="hc-dialog-subtitle" class="text-[10px] font-mono uppercase tracking-wider text-neutral-400 dark:text-neutral-500 mt-0.5 truncate">HAICHAIN Autonomous Kernel</p>
              </div>
            </div>
            <button id="hc-dialog-close-x" type="button" class="p-1.5 rounded-full text-neutral-400 hover:text-black dark:hover:text-white bg-neutral-100 dark:bg-neutral-900 transition-colors cursor-pointer shrink-0" aria-label="Close">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>

          <!-- Scrollable Body Content -->
          <div id="hc-dialog-body" class="my-3.5 hc-dialog-scroll flex-1 pr-0.5"></div>

          <!-- Actions -->
          <div id="hc-dialog-actions" class="pt-3 border-t border-neutral-100 dark:border-neutral-800/80 flex items-center space-x-2 shrink-0"></div>
        </div>
      `;
      document.body.appendChild(this.overlay);

      // Event listeners
      this.overlay.addEventListener('click', (e) => {
        if (e.target === this.overlay) {
          this._close(false);
        }
      });

      document.getElementById('hc-dialog-close-x').addEventListener('click', () => {
        this._close(false);
      });

      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && this.overlay.classList.contains('hc-active')) {
          this._close(false);
        }
      });
    }

    _close(value) {
      if (!this.overlay) return;
      this.overlay.classList.remove('hc-active');
      if (this.activeResolve) {
        const resolve = this.activeResolve;
        this.activeResolve = null;
        resolve(value);
      }
    }

    alert(message, options = {}) {
      return new Promise((resolve) => {
        this.activeResolve = resolve;
        const parsed = parseMessage(message);
        const title = options.title || parsed.title;
        const body = options.body || parsed.body;
        const type = options.type || parsed.type;

        document.getElementById('hc-dialog-title').textContent = title;
        document.getElementById('hc-dialog-body').innerHTML = formatBodyHtml(body);

        const iconWrap = document.getElementById('hc-dialog-icon-wrapper');
        iconWrap.className = `w-9 h-9 sm:w-10 sm:h-10 rounded-2xl flex items-center justify-center shrink-0 ${BADGE_STYLES[type] || BADGE_STYLES.info}`;
        iconWrap.innerHTML = ICONS[type] || ICONS.info;

        const subEl = document.getElementById('hc-dialog-subtitle');
        if (options.subtitle) {
          subEl.textContent = options.subtitle;
        } else {
          subEl.textContent = type === 'wallet' ? 'Web3 Cryptographic Settlement' : 'HAICHAIN Autonomous Kernel';
        }

        const actions = document.getElementById('hc-dialog-actions');
        actions.innerHTML = `
          <button id="hc-dialog-ok-btn" type="button" class="w-full py-2.5 sm:py-3 rounded-xl bg-black dark:bg-white text-white dark:text-black font-bold text-xs sm:text-sm transition-all shadow-md active:scale-95 cursor-pointer hover:opacity-90">
            ${options.okText || 'OK'}
          </button>
        `;

        document.getElementById('hc-dialog-ok-btn').addEventListener('click', () => {
          this._close(true);
        });

        this.overlay.classList.add('hc-active');
        document.getElementById('hc-dialog-ok-btn').focus();
      });
    }

    confirm(message, options = {}) {
      return new Promise((resolve) => {
        this.activeResolve = resolve;
        const parsed = parseMessage(message);
        const title = options.title || parsed.title || 'Confirm Action';
        const body = options.body || parsed.body;
        const type = options.danger ? 'danger' : (options.type || parsed.type);

        document.getElementById('hc-dialog-title').textContent = title;
        document.getElementById('hc-dialog-body').innerHTML = formatBodyHtml(body);

        const iconWrap = document.getElementById('hc-dialog-icon-wrapper');
        iconWrap.className = `w-9 h-9 sm:w-10 sm:h-10 rounded-2xl flex items-center justify-center shrink-0 ${BADGE_STYLES[type] || BADGE_STYLES.wallet}`;
        iconWrap.innerHTML = ICONS[type] || ICONS.wallet;

        const subEl = document.getElementById('hc-dialog-subtitle');
        if (options.subtitle) {
          subEl.textContent = options.subtitle;
        } else {
          subEl.textContent = type === 'danger' ? 'High-Risk Authorization' : 'Web3 Smart Contract Verification';
        }

        const confirmBtnClass = type === 'danger'
          ? 'bg-rose-600 hover:bg-rose-700 text-white shadow-md'
          : 'bg-black dark:bg-white text-white dark:text-black hover:opacity-90 shadow-md';

        const isVi = (document.documentElement.lang === 'vi') || (localStorage.getItem('haichain_lang') === 'vi');
        const defaultConfirm = isVi ? 'Xác nhận & Mở ví' : 'Confirm & Authorize';
        const defaultCancel = isVi ? 'Huỷ' : 'Cancel';

        const actions = document.getElementById('hc-dialog-actions');
        actions.innerHTML = `
          <button id="hc-dialog-cancel-btn" type="button" class="flex-1 py-2.5 sm:py-3 rounded-xl border border-neutral-300 dark:border-neutral-700 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white font-medium text-xs sm:text-sm transition-all cursor-pointer active:scale-95">
            ${options.cancelText || defaultCancel}
          </button>
          <button id="hc-dialog-confirm-btn" type="button" class="flex-1 py-2.5 sm:py-3 rounded-xl ${confirmBtnClass} font-bold text-xs sm:text-sm transition-all active:scale-95 cursor-pointer flex items-center justify-center space-x-1.5">
            <span>${options.confirmText || defaultConfirm}</span>
            <span class="font-mono text-xs">&rarr;</span>
          </button>
        `;

        document.getElementById('hc-dialog-cancel-btn').addEventListener('click', () => {
          this._close(false);
        });

        document.getElementById('hc-dialog-confirm-btn').addEventListener('click', () => {
          this._close(true);
        });

        this.overlay.classList.add('hc-active');
        document.getElementById('hc-dialog-confirm-btn').focus();
      });
    }
  }

  // 4. INITIALIZE
  let manager = null;
  function getManager() {
    if (!manager) manager = new DialogManager();
    return manager;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => getManager());
  } else {
    getManager();
  }

  // 5. UNIVERSAL API
  window.haichainDialog = {
    alert: (msg, opts) => getManager().alert(msg, opts),
    confirm: (msg, opts) => getManager().confirm(msg, opts)
  };

  // Seamlessly override native window.alert
  window.alert = function (message) {
    return getManager().alert(message);
  };
})();
