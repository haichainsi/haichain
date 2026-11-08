import sys
import time
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    code = f.read()

target = """              <!-- Social Quick Share Action Bar -->
              <div class="flex flex-wrap items-center gap-2 pt-1 text-xs">
                <span class="text-neutral-400 font-sans text-[11px]">${getActiveLang() === 'vi' ? 'Chia sẻ nhanh:' : 'Quick Share:'}</span>
                <button type="button" id="btn-share-ref-x" class="min-h-[34px] px-3 py-1.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-medium text-xs flex items-center space-x-1.5 cursor-pointer transition-colors active:scale-95">
                  <i data-lucide="twitter" class="w-3.5 h-3.5"></i>
                  <span>${getI18nText('refShareX')}</span>
                </button>
                <button type="button" id="btn-share-ref-tg" class="min-h-[34px] px-3 py-1.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-medium text-xs flex items-center space-x-1.5 cursor-pointer transition-colors active:scale-95">
                  <i data-lucide="send" class="w-3.5 h-3.5"></i>
                  <span>${getI18nText('refShareTelegram')}</span>
                </button>
              </div>"""

replacement = """              <!-- Social Quick Share Action Bar (Always 1 Row, Balanced 2-Col Grid) -->
              <div class="space-y-1.5 pt-1.5">
                <span class="text-neutral-400 font-sans text-[11px] block">${getActiveLang() === 'vi' ? 'Chia sẻ nhanh qua mạng xã hội:' : 'Quick Share:'}</span>
                <div class="grid grid-cols-2 gap-2 w-full">
                  <button type="button" id="btn-share-ref-x" class="min-h-[40px] w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-semibold text-xs flex items-center justify-center space-x-2 cursor-pointer transition-all active:scale-95 bg-white dark:bg-neutral-900 shadow-2xs">
                    <i data-lucide="twitter" class="w-3.5 h-3.5 shrink-0"></i>
                    <span class="truncate">${getI18nText('refShareX')}</span>
                  </button>
                  <button type="button" id="btn-share-ref-tg" class="min-h-[40px] w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-semibold text-xs flex items-center justify-center space-x-2 cursor-pointer transition-all active:scale-95 bg-white dark:bg-neutral-900 shadow-2xs">
                    <i data-lucide="send" class="w-3.5 h-3.5 shrink-0"></i>
                    <span class="truncate">${getI18nText('refShareTelegram')}</span>
                  </button>
                </div>
              </div>"""

if target in code:
    code = code.replace(target, replacement, 1)
    with open('sale-controller.js', 'w', encoding='utf-8') as f:
        f.write(code)
    with open('app/sale-controller.js', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Successfully replaced quick share buttons in sale-controller.js and app/sale-controller.js!")
else:
    print("Target not found in sale-controller.js!")
    sys.exit(1)

# Bump cachebuster in dashboard.html and app/dashboard.html
new_ver = f"v45_mobile_share_row_balanced_{int(time.time()*1000)}"

with open('dashboard.html', 'r', encoding='utf-8') as f:
    dhtml = f.read()

dhtml = re.sub(
    r'/app/sale-controller\.js\?v=[^\"]+',
    f'/app/sale-controller.js?v={new_ver}',
    dhtml
)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dhtml)
with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dhtml)

print("Bumped cachebuster to:", new_ver)
