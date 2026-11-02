import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Vietnamese translation for vaultTitle to be concise and natural
old_vi_title = '"vaultTitle": "Két Vesting Token-2022 & Danh Mục Phân Bổ",'
new_vi_title = '"vaultTitle": "Két Vesting & Phân Bổ Token-2022",'

assert old_vi_title in content, "old_vi_title not found in dashboard.html"
content = content.replace(old_vi_title, new_vi_title, 1)

# 2. Update overview banner gap
old_banner_row = '<div class="flex items-center space-x-2">\n              <span class="w-2 h-2 rounded-full bg-black dark:bg-white animate-pulse"></span>'
new_banner_row = '<div class="flex flex-wrap items-center gap-2">\n              <span class="w-2 h-2 rounded-full bg-black dark:bg-white animate-pulse"></span>'
if old_banner_row in content:
    content = content.replace(old_banner_row, new_banner_row, 1)

# 3. Update State 1 Header
old_state1 = '''            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4">
              <div>
                <div class="flex items-start space-x-3">
                  <div class="w-10 h-10 rounded-xl bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1.5 mt-0.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
                  </div>
                  <div class="flex-1 min-w-0">
                    <div class="flex items-start justify-between gap-2">
                      <h2 class="font-bold text-base sm:text-xl text-black dark:text-white leading-tight">
                        ${getVestingText('vaultTitle', lang)}
                      </h2>
                      <span class="shrink-0 whitespace-nowrap px-2 py-0.5 rounded-full text-[9.5px] sm:text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800 mt-0.5">
                        Solana L1
                      </span>
                    </div>
                  </div>
                </div>
                <p class="text-xs text-neutral-500 mt-1">
                  ${getVestingText('vaultSubtitle', lang)}
                </p>
              </div>
              <div class="flex items-center space-x-2 shrink-0"></div>
            </div>'''

new_state1 = '''            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4">
              <div class="flex-1 min-w-0">
                <div class="flex items-start space-x-3">
                  <div class="w-10 h-10 rounded-xl bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1.5 mt-0.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
                  </div>
                  <div class="flex-1 min-w-0 space-y-1.5">
                    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1.5 sm:gap-2">
                      <h2 class="font-bold text-base sm:text-xl text-black dark:text-white leading-snug">
                        ${getVestingText('vaultTitle', lang)}
                      </h2>
                      <span class="self-start sm:self-center shrink-0 whitespace-nowrap px-2.5 py-0.5 rounded-full text-[9.5px] sm:text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800">
                        Solana L1
                      </span>
                    </div>
                    <p class="text-xs text-neutral-500 leading-relaxed">
                      ${getVestingText('vaultSubtitle', lang)}
                    </p>
                  </div>
                </div>
              </div>
              <div class="flex items-center space-x-2 shrink-0"></div>
            </div>'''

assert old_state1 in content, "old_state1 not found in dashboard.html"
content = content.replace(old_state1, new_state1, 1)

# 4. Update State 2 Header (The one circled in user screenshot)
old_state2 = '''            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4">
              <div>
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-xl bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
                  </div>
                  <div>
                    <div class="flex items-center space-x-2">
                      <h2 class="font-bold text-lg sm:text-xl text-black dark:text-white">
                        ${getVestingText('vaultTitle', lang)}
                      </h2>
                      <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800">
                        ${shortAddr}
                      </span>
                    </div>
                  </div>
                </div>
                <p class="text-xs text-neutral-500 mt-1">
                  ${getVestingText('authAddress', lang)} <span class="font-mono text-black dark:text-white font-bold">${currentAddress}</span>
                </p>
              </div>
              <div class="flex items-center space-x-2 shrink-0"></div>
            </div>'''

new_state2 = '''            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4">
              <div class="flex-1 min-w-0">
                <div class="flex items-start space-x-3">
                  <div class="w-10 h-10 rounded-xl bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1.5 mt-0.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
                  </div>
                  <div class="flex-1 min-w-0 space-y-1.5">
                    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1.5 sm:gap-2">
                      <h2 class="font-bold text-base sm:text-xl text-black dark:text-white leading-snug">
                        ${getVestingText('vaultTitle', lang)}
                      </h2>
                      <span class="self-start sm:self-center shrink-0 px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800">
                        ${shortAddr}
                      </span>
                    </div>
                    <p class="text-xs text-neutral-500 font-mono break-all leading-relaxed">
                      ${getVestingText('authAddress', lang)} <span class="text-black dark:text-white font-bold">${currentAddress}</span>
                    </p>
                  </div>
                </div>
              </div>
              <div class="flex items-center space-x-2 shrink-0"></div>
            </div>'''

assert old_state2 in content, "old_state2 not found in dashboard.html"
content = content.replace(old_state2, new_state2, 1)

# 5. Update State 3 Header
old_state3 = '''          <div class="flex flex-col lg:flex-row lg:items-center justify-between pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4">
            <div class="flex items-center space-x-3.5 min-w-0">
              <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-2xl bg-black border border-neutral-800 flex items-center justify-center shadow-sm shrink-0 overflow-hidden p-1.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
              </div>
              <div class="min-w-0 space-y-1">
                <div class="flex flex-wrap items-center gap-2">
                  <h2 class="font-bold text-lg sm:text-xl text-black dark:text-white whitespace-nowrap">
                    ${getVestingText('portfolioTitle', lang)}
                  </h2>
                  <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-200 dark:border-neutral-800 font-semibold">
                    ${getVestingText('trancheBadge', lang)}
                  </span>
                  <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-300 dark:border-neutral-700 flex items-center space-x-1.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>
                    <span>${getVestingText('transferHookStatus', lang)}</span>
                  </span>
                </div>
                <div class="flex items-center space-x-2 text-xs text-neutral-500 font-mono">
                  <span>${getVestingText('authAddress', lang)}</span>
                  <span class="text-black dark:text-white font-bold">${shortAddr}</span>
                </div>
              </div>
            </div>'''

new_state3 = '''          <div class="flex flex-col lg:flex-row lg:items-center justify-between pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4">
            <div class="flex items-start space-x-3.5 min-w-0 flex-1">
              <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-2xl bg-black border border-neutral-800 flex items-center justify-center shadow-sm shrink-0 overflow-hidden p-1.5 mt-0.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
              </div>
              <div class="min-w-0 space-y-1.5 flex-1">
                <div class="flex flex-wrap items-center gap-2">
                  <h2 class="font-bold text-base sm:text-xl text-black dark:text-white leading-snug">
                    ${getVestingText('portfolioTitle', lang)}
                  </h2>
                  <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-200 dark:border-neutral-800 font-semibold shrink-0">
                    ${getVestingText('trancheBadge', lang)}
                  </span>
                  <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-300 dark:border-neutral-700 flex items-center space-x-1.5 shrink-0">
                    <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>
                    <span>${getVestingText('transferHookStatus', lang)}</span>
                  </span>
                </div>
                <div class="flex items-center space-x-2 text-xs text-neutral-500 font-mono">
                  <span>${getVestingText('authAddress', lang)}</span>
                  <span class="text-black dark:text-white font-bold">${shortAddr}</span>
                </div>
              </div>
            </div>'''

assert old_state3 in content, "old_state3 not found in dashboard.html"
content = content.replace(old_state3, new_state3, 1)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated dashboard.html and app/dashboard.html!")
