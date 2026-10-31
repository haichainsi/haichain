/**
 * HAICHAIN Universal Dialog System v1.0
 * Replaces native browser alert() and confirm() with Apple-minimalist,
 * responsive, accessible modal dialogs for desktop & mobile.
 */

(function () {
  'use strict';

  // Inject Dialog Styles
  const styleEl = document.createElement('style');
  styleEl.textContent = `
    .hc-dialog-overlay {
      position: fixed;
      inset: 0;
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
      background-color: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      opacity: 0;
      pointer-events: none;
      transition: opacity 200ms cubic-bezier(0.16, 1, 0.3, 1);
    }
    .hc-dialog-overlay.hc-active {
      opacity: 1;
      pointer-events: auto;
    }
    .hc-dialog-card {
      position: relative;
      width: 100%;
      max-width: 26rem;
      border-radius: 1.5rem;
      padding: 1.5rem;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.45);
      transform: scale(0.94) translateY(6px);
      transition: transform 220ms cubic-bezier(0.16, 1, 0.3, 1);
      box-sizing: border-box;
    }
    @media (min-width: 640px) {
      .hc-dialog-card {
        padding: 1.75rem;
      }
    }
    .hc-dialog-overlay.hc-active .hc-dialog-card {
      transform: scale(1) translateY(0);
    }
  `;
  document.head.appendChild(styleEl);

  // SVG Icons
  const ICONS = {
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
      <svg class="w-5 h-5 text-neutral-500 dark:text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    `
  };

  const BADGE_STYLES = {
    danger: 'bg-rose-50 dark:bg-rose-950/60 border border-rose-200 dark:border-rose-900/60 text-rose-600 dark:text-rose-400',
    warning: 'bg-amber-50 dark:bg-amber-950/60 border border-amber-200 dark:border-amber-900/60 text-amber-700 dark:text-amber-400',
    success: 'bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200 dark:border-emerald-900/60 text-emerald-700 dark:text-emerald-400',
    info: 'bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-800 dark:text-neutral-200'
  };

  function parseMessage(msg) {
    if (typeof msg !== 'string') msg = String(msg || '');
    let title = '';
    let body = '';
    let type = 'info';

    // Parse double newline title delimiter
    const doubleNl = msg.indexOf('\n\n');
    if (doubleNl !== -1 && doubleNl < 90) {
      title = msg.substring(0, doubleNl).replace(/:\s*$/, '').trim();
      body = msg.substring(doubleNl + 2).trim();
    } else if (msg.includes('\n')) {
      const firstNl = msg.indexOf('\n');
      title = msg.substring(0, firstNl).replace(/:\s*$/, '').trim();
      body = msg.substring(firstNl + 1).trim();
    } else {
      body = msg.trim();
    }

    const lower = (title + ' ' + body).toLowerCase();

    if (lower.includes('emergency') || lower.includes('kill-switch') || lower.includes('revoke') || lower.includes('frozen') || lower.includes('panic') || lower.includes('critical')) {
      type = 'danger';
      if (!title) title = 'Emergency Action';
    } else if (lower.includes('success') || lower.includes('activated') || lower.includes('credited') || lower.includes('validated') || lower.includes('disbursed')) {
      type = 'success';
      if (!title) title = 'Success';
    } else if (lower.includes('not connected') || lower.includes('wallet required') || lower.includes('insufficient') || lower.includes('invalid') || lower.includes('cancel') || lower.includes('rejected') || lower.includes('cannot') || lower.includes('too low') || lower.includes('attention')) {
      type = 'warning';
      if (!title) title = 'Notice';
    } else {
      type = 'info';
      if (!title) title = 'HAICHAIN System';
    }

    return { title, body, type };
  }

  function escapeHtml(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function formatBodyHtml(body) {
    const paragraphs = body.split(/\n\n+/);
    return paragraphs.map(p => {
      let html = escapeHtml(p.trim());
      // Convert single line breaks to <br/>
      html = html.replace(/\n/g, '<br/>');
      // Highlight inline quotes
      html = html.replace(/&quot;([^&]+)&quot;/g, '<strong class="text-neutral-900 dark:text-neutral-100 font-semibold font-mono">"$1"</strong>');
      // Highlight key-value lines like "Address: ..."
      html = html.replace(/^([A-Za-z0-9\s]+):\s*(.+)$/gm, '<span class="text-neutral-500 font-mono text-[11px] block uppercase">$1</span><span class="font-mono text-xs text-neutral-800 dark:text-neutral-200 font-bold block mb-1.5 break-all">$2</span>');
      return `<p class="leading-relaxed mt-2 first:mt-0">${html}</p>`;
    }).join('');
  }

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
        <div class="hc-dialog-card bg-white dark:bg-[#121212] border border-neutral-200 dark:border-neutral-800 text-neutral-900 dark:text-neutral-100">
          <div class="flex items-start space-x-3.5">
            <div id="hc-dialog-icon-wrapper" class="w-10 h-10 rounded-2xl flex items-center justify-center shrink-0"></div>
            <div class="flex-1 min-w-0 pt-0.5">
              <h3 id="hc-dialog-title" class="text-sm sm:text-base font-bold text-neutral-900 dark:text-white tracking-tight truncate"></h3>
              <p class="text-[10px] font-mono uppercase tracking-wider text-neutral-400 dark:text-neutral-500 mt-0.5">HAICHAIN Autonomous Kernel</p>
            </div>
            <button id="hc-dialog-close-x" type="button" class="p-1 rounded-full text-neutral-400 hover:text-black dark:hover:text-white transition-colors cursor-pointer shrink-0" aria-label="Close">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>

          <div id="hc-dialog-body" class="my-4 text-xs sm:text-[13px] text-neutral-600 dark:text-neutral-300 font-sans leading-relaxed"></div>

          <div id="hc-dialog-actions" class="mt-5 flex items-center space-x-2 pt-2 border-t border-neutral-100 dark:border-neutral-800/80"></div>
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
        iconWrap.className = `w-10 h-10 rounded-2xl flex items-center justify-center shrink-0 ${BADGE_STYLES[type] || BADGE_STYLES.info}`;
        iconWrap.innerHTML = ICONS[type] || ICONS.info;

        const actions = document.getElementById('hc-dialog-actions');
        actions.innerHTML = `
          <button id="hc-dialog-ok-btn" type="button" class="w-full py-2.5 sm:py-3 rounded-2xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-xs sm:text-sm transition-all shadow-sm active:scale-95 cursor-pointer">
            ${options.okText || 'OK'}
          </button>
        `;

        document.getElementById('hc-dialog-ok-btn').addEventListener('click', () => {
          this._close(true);
        });

        // Trigger smooth entrance
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
        iconWrap.className = `w-10 h-10 rounded-2xl flex items-center justify-center shrink-0 ${BADGE_STYLES[type] || BADGE_STYLES.warning}`;
        iconWrap.innerHTML = ICONS[type] || ICONS.warning;

        const confirmBtnClass = type === 'danger'
          ? 'bg-rose-600 hover:bg-rose-700 text-white shadow-sm'
          : 'bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 shadow-sm';

        const actions = document.getElementById('hc-dialog-actions');
        actions.innerHTML = `
          <button id="hc-dialog-cancel-btn" type="button" class="flex-1 py-2.5 sm:py-3 rounded-2xl border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:bg-neutral-100 dark:hover:bg-neutral-900 font-semibold text-xs sm:text-sm transition-colors cursor-pointer active:scale-95">
            ${options.cancelText || 'Huỷ'}
          </button>
          <button id="hc-dialog-confirm-btn" type="button" class="flex-1 py-2.5 sm:py-3 rounded-2xl ${confirmBtnClass} font-semibold text-xs sm:text-sm transition-all active:scale-95 cursor-pointer">
            ${options.confirmText || 'Xác nhận'}
          </button>
        `;

        document.getElementById('hc-dialog-cancel-btn').addEventListener('click', () => {
          this._close(false);
        });

        document.getElementById('hc-dialog-confirm-btn').addEventListener('click', () => {
          this._close(true);
        });

        // Trigger smooth entrance
        this.overlay.classList.add('hc-active');
        document.getElementById('hc-dialog-confirm-btn').focus();
      });
    }
  }

  // Initialize dialog manager when DOM is ready
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

  // Universal API
  window.haichainDialog = {
    alert: (msg, opts) => getManager().alert(msg, opts),
    confirm: (msg, opts) => getManager().confirm(msg, opts)
  };

  // Seamlessly override native window.alert
  window.alert = function (message) {
    return getManager().alert(message);
  };
})();
