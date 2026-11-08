import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# The perfect, robust, mobile + desktop optimized wallet modal HTML
CLEAN_MODAL_CARDS = '''        <!-- 1. Phantom Card with Nested Mobile Action Tray -->
        <div class="rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/60 dark:bg-neutral-900/50 hover:border-neutral-400 dark:hover:border-neutral-600 transition-all overflow-hidden">
          <button class="wallet-provider-btn w-full p-2.5 sm:p-3 flex items-center justify-between text-left cursor-pointer active:opacity-75" data-provider="phantom">
            <div class="flex items-center space-x-3 min-w-0 flex-1">
              <div class="w-8 h-8 rounded-xl bg-purple-500/10 text-purple-600 dark:text-purple-400 flex items-center justify-center text-lg shrink-0">
                👻
              </div>
              <div class="min-w-0 flex-1 pr-2">
                <div class="font-semibold text-xs sm:text-sm text-black dark:text-white truncate" data-i18n="modal.walletPhantom">Phantom Wallet</div>
                <div class="text-[11px] text-neutral-500 truncate" id="phantom-status-desc" data-i18n="modal.walletPhantomDesc">Popular Solana mobile app & browser extension</div>
              </div>
            </div>
            <span id="phantom-arrow" class="text-xs font-mono text-neutral-400 transition-transform duration-200 shrink-0">&rarr;</span>
          </button>
          
          <!-- Inline Phantom Mobile Action Tray -->
          <div id="phantom-mobile-tray" class="hidden px-2.5 pb-2.5 pt-1 space-y-1.5 border-t border-neutral-200 dark:border-neutral-800/80 bg-neutral-100/60 dark:bg-neutral-900/80">
            <button type="button" id="btn-tray-phantom-app" class="w-full py-2 px-3 rounded-xl bg-black text-white dark:bg-white dark:text-black font-semibold text-[11px] flex items-center justify-between transition-opacity active:opacity-75 cursor-pointer">
              <span class="flex items-center space-x-1.5 truncate">
                <span>🚀</span>
                <span>Open in Phantom App (Recommended)</span>
              </span>
              <span class="font-mono text-xs">&rarr;</span>
            </button>
            <div class="grid grid-cols-2 gap-1.5">
              <button type="button" id="btn-tray-phantom-deeplink" class="py-1.5 px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-800 text-black dark:text-white text-[10px] font-medium flex items-center justify-center space-x-1 transition-opacity active:opacity-75 cursor-pointer truncate">
                <span>🔄</span>
                <span>2-Way Chrome</span>
              </button>
              <button type="button" id="btn-tray-phantom-paste" class="py-1.5 px-2.5 rounded-xl border border-dashed border-neutral-300 dark:border-neutral-700 text-neutral-600 dark:text-neutral-300 text-[10px] font-medium flex items-center justify-center space-x-1 transition-opacity active:opacity-75 cursor-pointer hover:bg-neutral-200 dark:hover:bg-neutral-800 truncate">
                <i data-lucide="clipboard" class="w-3 h-3"></i>
                <span>Paste Address</span>
              </button>
            </div>
          </div>
        </div>

        <!-- 2. Solflare Card with Nested Mobile Action Tray -->
        <div class="rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/60 dark:bg-neutral-900/50 hover:border-neutral-400 dark:hover:border-neutral-600 transition-all overflow-hidden">
          <button class="wallet-provider-btn w-full p-2.5 sm:p-3 flex items-center justify-between text-left cursor-pointer active:opacity-75" data-provider="solflare">
            <div class="flex items-center space-x-3 min-w-0 flex-1">
              <div class="w-8 h-8 rounded-xl bg-orange-500/10 text-orange-600 dark:text-orange-400 flex items-center justify-center text-lg shrink-0">
                🔥
              </div>
              <div class="min-w-0 flex-1 pr-2">
                <div class="font-semibold text-xs sm:text-sm text-black dark:text-white truncate" data-i18n="modal.walletSolflare">Solflare Wallet</div>
                <div class="text-[11px] text-neutral-500 truncate" data-i18n="modal.walletSolflareDesc">Browser extension & mobile support</div>
              </div>
            </div>
            <span id="solflare-arrow" class="text-xs font-mono text-neutral-400 transition-transform duration-200 shrink-0">&rarr;</span>
          </button>
          
          <!-- Inline Solflare Mobile Action Tray -->
          <div id="solflare-mobile-tray" class="hidden px-2.5 pb-2.5 pt-1 space-y-1.5 border-t border-neutral-200 dark:border-neutral-800/80 bg-neutral-100/60 dark:bg-neutral-900/80">
            <button type="button" id="btn-tray-solflare-app" class="w-full py-2 px-3 rounded-xl bg-black text-white dark:bg-white dark:text-black font-semibold text-[11px] flex items-center justify-between transition-opacity active:opacity-75 cursor-pointer">
              <span class="flex items-center space-x-1.5 truncate">
                <span>🚀</span>
                <span>Open in Solflare App</span>
              </span>
              <span class="font-mono text-xs">&rarr;</span>
            </button>
            <button type="button" id="btn-tray-solflare-deeplink" class="w-full py-1.5 px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-800 text-black dark:text-white text-[10px] font-medium flex items-center justify-center space-x-1 transition-opacity active:opacity-75 cursor-pointer truncate">
              <span>🔄</span>
              <span>2-Way Connect to Chrome</span>
            </button>
          </div>
        </div>

        <!-- 3. MetaMask Card with Nested Mobile Action Tray -->
        <div class="rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/60 dark:bg-neutral-900/50 hover:border-neutral-400 dark:hover:border-neutral-600 transition-all overflow-hidden">
          <button class="wallet-provider-btn w-full p-2.5 sm:p-3 flex items-center justify-between text-left cursor-pointer active:opacity-75" data-provider="metamask">
            <div class="flex items-center space-x-3 min-w-0 flex-1">
              <div class="w-8 h-8 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400 flex items-center justify-center text-lg shrink-0">
                🦊
              </div>
              <div class="min-w-0 flex-1 pr-2">
                <div class="font-semibold text-xs sm:text-sm text-black dark:text-white truncate" data-i18n="modal.walletMetamask">MetaMask Wallet</div>
                <div class="text-[11px] text-neutral-500 truncate" id="metamask-status-desc" data-i18n="modal.walletMetamaskDesc">EVM Multi-Chain & Solana Snap (Ethereum, BSC, Arbitrum)</div>
              </div>
            </div>
            <span id="metamask-arrow" class="text-xs font-mono text-neutral-400 transition-transform duration-200 shrink-0">&rarr;</span>
          </button>
          
          <!-- Inline MetaMask Mobile Action Tray -->
          <div id="metamask-mobile-tray" class="hidden px-2.5 pb-2.5 pt-1 space-y-1.5 border-t border-neutral-200 dark:border-neutral-800/80 bg-neutral-100/60 dark:bg-neutral-900/80">
            <button type="button" id="btn-tray-metamask-app" class="w-full py-2 px-3 rounded-xl bg-black text-white dark:bg-white dark:text-black font-semibold text-[11px] flex items-center justify-between transition-opacity active:opacity-75 cursor-pointer">
              <span class="flex items-center space-x-1.5 truncate">
                <span>🦊</span>
                <span>Open in MetaMask App (Mobile Browser)</span>
              </span>
              <span class="font-mono text-xs">&rarr;</span>
            </button>
            <div class="grid grid-cols-2 gap-1.5">
              <button type="button" id="btn-tray-metamask-connect" class="py-1.5 px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-800 text-black dark:text-white text-[10px] font-medium flex items-center justify-center space-x-1 transition-opacity active:opacity-75 cursor-pointer truncate">
                <span>⚡</span>
                <span>Connect Browser</span>
              </button>
              <a href="https://metamask.io/download/" target="_blank" rel="noopener" class="py-1.5 px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-neutral-800 text-black dark:text-white text-[10px] font-medium flex items-center justify-center space-x-1 transition-opacity active:opacity-75 cursor-pointer truncate">
                <span>📥</span>
                <span>Get MetaMask</span>
              </a>
            </div>
          </div>
        </div>

        <!-- 4. Custom Solana Address with Inline Input Panel -->
        <div class="rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/60 dark:bg-neutral-900/50 hover:border-neutral-400 dark:hover:border-neutral-600 transition-all overflow-hidden">
          <button class="wallet-provider-btn w-full p-2.5 sm:p-3 flex items-center justify-between text-left cursor-pointer active:opacity-75" data-provider="manual">
            <div class="flex items-center space-x-3 min-w-0 flex-1">
              <div class="w-8 h-8 rounded-xl bg-neutral-200 dark:bg-neutral-800 flex items-center justify-center text-black dark:text-white shrink-0">
                <i data-lucide="key" class="w-4 h-4"></i>
              </div>
              <div class="min-w-0 flex-1 pr-2">
                <div class="font-semibold text-xs sm:text-sm text-black dark:text-white truncate" data-i18n="modal.walletManual">Custom Solana Public Key</div>
                <div class="text-[11px] text-neutral-500 truncate" data-i18n="modal.walletManualDesc">Paste your personal Solana address to read real balance</div>
              </div>
            </div>
            <span id="manual-arrow" class="text-xs font-mono text-neutral-400 transition-transform duration-200 shrink-0">&rarr;</span>
          </button>
          
          <!-- Inline Manual Address Panel -->
          <div id="manual-address-panel" class="hidden px-2.5 pb-2.5 pt-1.5 space-y-2 border-t border-neutral-200 dark:border-neutral-800/80 bg-neutral-100/60 dark:bg-neutral-900/80">
            <div class="flex items-center gap-1.5">
              <input type="text" id="manual-wallet-input" placeholder="Paste Solana address (7xKX...)" data-i18n-placeholder="modal.manualWalletPlaceholder" class="flex-1 px-2.5 py-1.5 text-xs font-mono rounded-xl border border-neutral-300 dark:border-neutral-700 bg-white dark:bg-black text-black dark:text-white focus:outline-none">
              <button type="button" id="quick-paste-manual-btn" class="px-2 py-1.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-100 dark:bg-neutral-800 text-[10px] font-medium flex items-center space-x-1 shrink-0 cursor-pointer hover:bg-neutral-200 dark:hover:bg-neutral-700" title="Paste from clipboard">
                <i data-lucide="clipboard" class="w-3 h-3"></i>
                <span>Paste</span>
              </button>
            </div>
            <div class="flex gap-1.5">
              <button type="button" id="cancel-manual-wallet-btn" class="flex-1 py-1.5 rounded-xl text-xs font-medium border border-neutral-300 dark:border-neutral-700 cursor-pointer" data-i18n="modal.walletManualCancel">Cancel</button>
              <button type="button" id="submit-manual-wallet-btn" class="flex-1 py-1.5 rounded-xl text-xs font-semibold bg-black text-white dark:bg-white dark:text-black cursor-pointer" data-i18n="modal.walletManualConfirm">Confirm</button>
            </div>
          </div>
        </div>'''

def fix_file(filepath):
    print(f"Fixing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the region between "<!-- 1. Phantom Card with Nested Mobile Action Tray -->" and "<!-- Compact Notice Box"
    start_tag = '<!-- 1. Phantom Card with Nested Mobile Action Tray -->'
    end_tag = '<!-- Compact Notice Box (For desktop missing extension prompt or errors) -->'

    s_idx = content.find(start_tag)
    e_idx = content.find(end_tag)

    if s_idx == -1 or e_idx == -1:
        print(f"[{filepath}] ERROR: Could not locate markers. s_idx={s_idx}, e_idx={e_idx}")
        return

    # Replace everything between s_idx and e_idx with CLEAN_MODAL_CARDS
    # Note: the region between them ends with </div>\n\n (closing of <div class="my-2.5 sm:my-3 space-y-2">)
    new_content = content[:s_idx] + CLEAN_MODAL_CARDS + '\n\n      </div>\n\n      ' + content[e_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"[{filepath}] Successfully replaced with clean modal markup.")

fix_file('dashboard.html')
fix_file('app/dashboard.html')
