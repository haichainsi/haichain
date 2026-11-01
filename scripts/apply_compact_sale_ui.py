import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Define start and end of container.innerHTML in renderTerminalContent
start_marker = "    container.innerHTML = `"
end_marker = "    setupCalculatorLogic(container);"

idx_start = text.find(start_marker)
idx_end = text.find(end_marker)

if idx_start == -1 or idx_end == -1:
    print(f"Error: Markers not found. idx_start={idx_start}, idx_end={idx_end}")
    sys.exit(1)

new_inner_html = """    container.innerHTML = `
      <!-- 1. TOP DEAL OVERVIEW & ALLOCATION PROGRESS CARD (COMPACT APPLE TITANIUM LUXURY) -->
      <div class="p-4 sm:p-5 md:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-xs space-y-4">
        <div class="flex flex-col lg:flex-row justify-between lg:items-center gap-3 sm:gap-4">
          <div class="space-y-1.5 max-w-2xl">
            <div class="inline-flex items-center space-x-2 px-2.5 py-0.5 rounded-full bg-neutral-100 dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-800 text-black dark:text-white text-[10px] sm:text-xs font-mono font-semibold tracking-wide">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
              <span>${getI18nText('heroBadge')}</span>
            </div>
            <h1 class="text-lg sm:text-2xl md:text-3xl font-black tracking-tight text-black dark:text-white leading-tight">
              ${getI18nText('heroTitle')}
            </h1>
            <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans">
              ${getI18nText('heroSubtitle')}
            </p>
          </div>

          <!-- Document Action Buttons (Compact Sleek Pill Cluster) -->
          <div class="flex items-center gap-2 shrink-0">
            <a href="${phase.saftUrl}" download class="px-3.5 py-2 rounded-xl bg-black dark:bg-white text-white dark:text-black font-semibold text-xs font-mono transition-all flex items-center justify-center space-x-1.5 hover:opacity-90 active:scale-95 shadow-sm">
              <i data-lucide="file-check" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('downloadSaft')}</span>
            </a>
            <a href="${phase.memoUrl}" download class="px-3.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-medium text-xs font-mono transition-all flex items-center justify-center space-x-1.5 active:scale-95">
              <i data-lucide="book-open" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('downloadMemo')}</span>
            </a>
          </div>
        </div>

        <!-- Allocation Progress Track (Clean & Slim Minimalist) -->
        <div class="pt-3 border-t border-neutral-100 dark:border-neutral-800/80 space-y-1.5 font-mono text-xs">
          <div class="flex justify-between items-center text-[11px] sm:text-xs">
            <span class="text-neutral-500">${getI18nText('allocationProgress')} <strong class="text-black dark:text-white font-bold">${(phase.allocatedSoFar / 1000000).toFixed(2)}M / ${(phase.totalAllocation / 1000000).toFixed(1)}M $HAISI</strong></span>
            <span class="text-emerald-600 dark:text-emerald-400 font-bold">${percentClaimed}% ${getI18nText('claimedLabel')}</span>
          </div>
          <div class="w-full h-1.5 rounded-full bg-neutral-200 dark:bg-neutral-800 overflow-hidden relative">
            <div class="h-full bg-black dark:bg-white rounded-full transition-all duration-1000" style="width: ${percentClaimed}%"></div>
          </div>
          <div class="flex flex-wrap justify-between gap-y-0.5 text-[10px] sm:text-[11px] text-neutral-500 dark:text-neutral-400">
            <span>${getI18nText('floorPrice')}</span>
            <span>${getI18nText('hardCapLabel')}</span>
            <span>${getI18nText('publicPriceLabel')}</span>
          </div>
        </div>

        ${userAllocation ? `
        <!-- Sleek 1-Line Active Allocation Pill -->
        <div class="p-2.5 sm:p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs font-mono">
          <div class="flex items-center space-x-2 text-black dark:text-white">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
            <span class="text-neutral-500 font-sans">${getActiveLang() === 'vi' ? 'Đã phân bổ:' : 'Your Allocation:'}</span>
            <strong class="font-bold underline text-black dark:text-white">${userAllocation.haiTokens.toLocaleString()} $HAISI</strong>
            <span class="text-[11px] text-neutral-400">($${userAllocation.amountUsdt.toLocaleString()} USDT • Token-2022 Locked)</span>
          </div>
          <button onclick="window.switchTab('tab-vesting')" class="px-3 py-1.5 rounded-xl bg-black dark:bg-white text-white dark:text-black font-semibold text-[11px] transition-all hover:opacity-90 shrink-0 self-start sm:self-auto">
            ${getActiveLang() === 'vi' ? 'Xem Két Vesting →' : 'View Vesting Vault →'}
          </button>
        </div>
        ` : ''}
      </div>

      <!-- 2. TWO-COLUMN BALANCED WORKFLOW (STEP 1: CALCULATE | STEP 2: RESERVE) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 sm:gap-5">

        <!-- STEP 1: CALCULATOR (COL 7) -->
        <div class="lg:col-span-7 p-4 sm:p-5 md:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card space-y-4 shadow-xs flex flex-col justify-between">
          <div class="space-y-3.5">
            <div class="flex items-center space-x-2">
              <span class="w-5 h-5 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-[11px] font-mono font-bold shrink-0">1</span>
              <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-black dark:text-white font-mono">
                ${getI18nText('calcTitle')}
              </h2>
            </div>

            <!-- USDT Input Container with Quick Buttons -->
            <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2 font-mono">
              <div class="flex justify-between items-center text-[11px]">
                <label for="calc-usdt-input" class="text-neutral-500 font-medium">${getI18nText('subscriptionAmount')}</label>
                <span class="text-[10px] text-neutral-400">${getI18nText('subscriptionLimits')}</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="flex items-center space-x-1.5 flex-1 px-3 py-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-300 dark:border-neutral-800 focus-within:border-black dark:focus-within:border-white transition-colors">
                  <span class="text-lg sm:text-xl font-bold text-neutral-400">$</span>
                  <input type="number" id="calc-usdt-input" value="1000" min="500" max="15000" step="100" class="w-full bg-transparent text-lg sm:text-xl font-black text-black dark:text-white focus:outline-none tabular-nums min-w-0">
                </div>
                <div class="flex gap-1 shrink-0">
                  <button type="button" class="btn-quick-calc px-2.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all active:scale-95" data-amount="1000">$1k</button>
                  <button type="button" class="btn-quick-calc px-2.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all active:scale-95" data-amount="2500">$2.5k</button>
                  <button type="button" class="btn-quick-calc px-2.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all active:scale-95" data-amount="5000">$5k</button>
                  <button type="button" class="btn-quick-calc px-2.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all active:scale-95" data-amount="10000">$10k</button>
                </div>
              </div>
            </div>

            <!-- 3 Minimalist Outcome Cards -->
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 font-mono">
              <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 space-y-0.5">
                <span class="text-[9px] uppercase text-neutral-400 font-semibold block">${getI18nText('totalAllocationTitle')}</span>
                <div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-total-hai">142,857</div>
                <span class="text-[9px] text-neutral-500 font-medium block">${getI18nText('fixedPriceBadge')}</span>
              </div>
              <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 space-y-0.5">
                <span class="text-[9px] uppercase text-neutral-400 font-semibold block">${getI18nText('tgeValueTitle')}</span>
                <div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-tge-value">$1,428.57</div>
                <span class="text-[9px] text-emerald-600 dark:text-emerald-400 font-bold block">${getI18nText('unvestedYield')}</span>
              </div>
              <div class="col-span-2 sm:col-span-1 p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 space-y-0.5">
                <span class="text-[9px] uppercase text-neutral-400 font-semibold block">${getI18nText('l1ValueTitle')}</span>
                <div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-l1-value">$142,857</div>
                <span class="text-[9px] text-neutral-500 font-medium block">142x Multiple</span>
              </div>
            </div>

            <!-- Compact Linear Vesting Schedule Row -->
            <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200 dark:border-neutral-800 space-y-1.5 text-xs font-mono">
              <span class="text-neutral-500 font-semibold text-[10px] uppercase tracking-wider block">${getI18nText('vestingScheduleTitle')}</span>
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-[11px] pt-0.5">
                <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                  <span class="text-neutral-400 text-[10px] block">1. TGE (20%)</span>
                  <strong class="text-black dark:text-white font-bold" id="calc-tge-tokens">28,571 $HAISI</strong>
                </div>
                <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                  <span class="text-neutral-400 text-[10px] block">2. Cliff (2 Tháng)</span>
                  <span class="text-neutral-500 font-medium">Khóa 0% (Anti-dump)</span>
                </div>
                <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                  <span class="text-neutral-400 text-[10px] block">3. Linear (6 Tháng)</span>
                  <strong class="text-black dark:text-white font-bold" id="calc-stream-tokens">114,286 $HAISI</strong>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- STEP 2: SAFT TERMINAL & DEPOSIT (COL 5) -->
        <div class="lg:col-span-5 p-4 sm:p-5 md:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card space-y-4 shadow-xs flex flex-col justify-between">
          <div class="space-y-3.5">
            <div class="flex items-center space-x-2">
              <span class="w-5 h-5 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-[11px] font-mono font-bold shrink-0">2</span>
              <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-black dark:text-white font-mono">
                ${getI18nText('terminalTitle')}
              </h2>
            </div>

            <!-- Form Fields -->
            <div class="space-y-2.5 font-mono text-xs">
              <!-- Wallet Field (Primary) -->
              <div>
                <div class="flex justify-between items-center mb-1">
                  <label class="block text-[11px] text-neutral-500 font-sans font-medium">${getI18nText('labelWallet')}</label>
                  <button type="button" id="btn-autofill-phantom" class="text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white underline font-sans text-[10px] flex items-center space-x-1 cursor-pointer">
                    <i data-lucide="zap" class="w-3 h-3 text-emerald-500"></i>
                    <span>${getActiveLang() === 'vi' ? 'Lấy ví Phantom' : 'Auto-fill Phantom'}</span>
                  </button>
                </div>
                <input type="text" id="preseed-wallet" value="${connectedWalletAddr}" placeholder="${getI18nText('placeholderWallet')}" class="w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white font-mono text-[11px]">
              </div>

              <!-- Name & Email (Compact Grid) -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                <div>
                  <label class="block text-[10px] text-neutral-500 mb-1 font-sans font-medium">${getI18nText('labelName')}</label>
                  <input type="text" id="preseed-name" placeholder="${getI18nText('placeholderName')}" class="w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none text-[11px]">
                </div>
                <div>
                  <label class="block text-[10px] text-neutral-500 mb-1 font-sans font-medium">${getI18nText('labelEmail')}</label>
                  <input type="email" id="preseed-email" placeholder="${getI18nText('placeholderEmail')}" class="w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none text-[11px]">
                </div>
              </div>
            </div>

            <!-- Multi-Sig Treasury & Payment Actions -->
            <div class="p-3 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 font-mono text-xs space-y-2">
              <!-- Primary: 1-Click Pay with Phantom -->
              <button type="button" id="btn-pay-phantom-1click" class="w-full py-2.5 px-3 rounded-xl bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs font-mono flex items-center justify-center space-x-2 transition-all shadow-xs cursor-pointer active:scale-95">
                <i data-lucide="wallet" class="w-3.5 h-3.5 shrink-0"></i>
                <span>${getActiveLang() === 'vi' ? 'Thanh Toán 1-Click Ví Phantom' : 'Pay with Phantom (1-Click)'}</span>
              </button>

              <div class="flex items-center justify-between text-[10px] text-neutral-400 font-sans py-0.5">
                <span class="uppercase tracking-wider font-semibold">${getActiveLang() === 'vi' ? 'Hoặc chuyển ví kho bạc:' : 'Or manual treasury transfer:'}</span>
                <button type="button" id="btn-copy-treasury" class="text-neutral-700 dark:text-neutral-300 hover:text-black dark:hover:text-white underline font-mono text-[10px]">${getI18nText('copyBtn')}</button>
              </div>

              <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 flex items-center justify-between gap-1 text-[10px]">
                <span class="truncate select-all font-mono font-bold text-black dark:text-white" id="treasury-pubkey">${config.TREASURY_ADDRESS}</span>
              </div>
            </div>
          </div>

          <!-- Submit CTA Button -->
          <div class="pt-1">
            <button id="btn-submit-saft-reservation" class="w-full py-2.5 sm:py-3 rounded-2xl bg-black dark:bg-white text-white dark:text-black font-extrabold text-xs font-mono transition-all flex items-center justify-center space-x-2 shadow-sm cursor-pointer hover:opacity-90 active:scale-[0.98]">
              <i data-lucide="send" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('submitBtn')}</span>
            </button>
            <p class="text-[9px] text-neutral-400 text-center font-mono mt-1.5 flex items-center justify-center space-x-1">
              <i data-lucide="shield" class="w-2.5 h-2.5 text-neutral-400"></i>
              <span>${getI18nText('protectedFooter')}</span>
            </p>
          </div>
        </div>

      </div>
    `;

"""

new_text = text[:idx_start] + new_inner_html + text[idx_end:]

with open('sale-controller.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

with open('app/sale-controller.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("SUCCESS: Compact luxury Titanium UI applied and synced to app/sale-controller.js.")
