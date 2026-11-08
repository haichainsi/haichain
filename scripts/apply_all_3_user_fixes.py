import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

# -------------------------------------------------------------
# 1. PATCH dashboard.html & app/dashboard.html
# -------------------------------------------------------------
def patch_dashboard(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # A. Replace payment tabs HTML with optimized 2-column grid (Faucet & Web3 only, hide Apple & Card)
    old_tabs_pattern = r'<!-- Payment Method Tabs: Faucet \| Apple Pay \| Card \| Web3 Wallet -->\s*<div class="flex space-x-1 p-1 rounded-2xl bg-neutral-100 dark:bg-neutral-900 text-xs font-medium">[\s\S]*?id="dash-pay-tab-web3"[\s\S]*?<\/button>\s*<\/div>'
    
    new_tabs_html = """<!-- Payment Method Tabs: Faucet | Web3 Wallet (Optimized 2-Column Responsive Grid) -->
        <div class="grid grid-cols-2 gap-2 p-1.5 rounded-2xl bg-neutral-100 dark:bg-neutral-900 text-xs font-mono font-medium">
          <button type="button" id="dash-pay-tab-faucet" class="w-full py-2.5 px-3 rounded-xl bg-white dark:bg-black text-black dark:text-white shadow-xs font-bold flex items-center justify-center space-x-1.5 transition-all cursor-pointer border border-neutral-300 dark:border-neutral-700">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
            <span class="truncate">Faucet (+$10)</span>
            <span class="text-[9px] px-1.5 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 font-mono hidden sm:inline-block">Free</span>
          </button>
          <button type="button" id="dash-pay-tab-apple" class="hidden" style="display: none !important;"></button>
          <button type="button" id="dash-pay-tab-card" class="hidden" style="display: none !important;"></button>
          <button type="button" id="dash-pay-tab-web3" class="w-full py-2.5 px-3 rounded-xl text-neutral-500 hover:text-black dark:hover:text-white font-semibold flex items-center justify-center space-x-1.5 transition-all cursor-pointer hover:bg-neutral-200/50 dark:hover:bg-neutral-800/50">
            <span class="w-2 h-2 rounded-full bg-neutral-400 dark:bg-neutral-500 shrink-0"></span>
            <span class="truncate">Web3 Wallet</span>
            <span class="text-[9px] px-1.5 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 font-mono hidden sm:inline-block">On-Chain</span>
          </button>
        </div>"""

    if re.search(old_tabs_pattern, content):
        content = re.sub(old_tabs_pattern, new_tabs_html, content)
        print(f'{filepath}: Successfully updated deposit modal tabs!')
    else:
        print(f'{filepath}: old_tabs_pattern not matched!')

    # B. Update selectDepositTab JS function
    old_js_pattern = r'function selectDepositTab\(method\) \{[\s\S]*?if \(dashPayTabWeb3\) dashPayTabWeb3\.className = method === \'web3\' \? activeClass : inactiveClass;'
    
    new_js = """function selectDepositTab(method) {
      selectedDepositMethod = method;
      const activeClass = "w-full py-2.5 px-3 rounded-xl bg-white dark:bg-black text-black dark:text-white shadow-xs font-bold flex items-center justify-center space-x-1.5 transition-all cursor-pointer border border-neutral-300 dark:border-neutral-700";
      const inactiveClass = "w-full py-2.5 px-3 rounded-xl text-neutral-500 hover:text-black dark:hover:text-white font-semibold flex items-center justify-center space-x-1.5 transition-all cursor-pointer hover:bg-neutral-200/50 dark:hover:bg-neutral-800/50";

      if (dashPayTabFaucet) dashPayTabFaucet.className = method === 'faucet' ? activeClass : inactiveClass;
      if (dashPayTabApple) dashPayTabApple.className = "hidden";
      if (dashPayTabCard) dashPayTabCard.className = "hidden";
      if (dashPayTabWeb3) dashPayTabWeb3.className = method === 'web3' ? activeClass : inactiveClass;"""

    if re.search(old_js_pattern, content):
        content = re.sub(old_js_pattern, new_js, content)
        print(f'{filepath}: Successfully updated selectDepositTab JS!')
    else:
        print(f'{filepath}: old_js_pattern not matched!')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# -------------------------------------------------------------
# 2. PATCH sale-controller.js & app/sale-controller.js
# -------------------------------------------------------------
def patch_sale_controller(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove lightning icon ⚡
    old_lightning = "if (!saved.address) return isVi ? '⚡ Kết Nối Ví Web3 Để Mua $HAISI' : '⚡ Connect Web3 Wallet to Buy $HAISI';"
    new_lightning = "if (!saved.address) return isVi ? 'Kết Nối Ví Web3 Để Mua $HAISI' : 'Connect Web3 Wallet to Buy $HAISI';"

    if old_lightning in content:
        content = content.replace(old_lightning, new_lightning)
        print(f'{filepath}: Successfully removed lightning icon ⚡!')
    else:
        print(f'{filepath}: old_lightning string not found directly, checking regex...')
        content = re.sub(
            r'if \(!saved\.address\)\s*return\s*isVi\s*\?\s*[\'"]⚡\s*Kết Nối Ví Web3 Để Mua \$HAISI[\'"]\s*:\s*[\'"]⚡\s*Connect Web3 Wallet to Buy \$HAISI[\'"];',
            "if (!saved.address) return isVi ? 'Kết Nối Ví Web3 Để Mua $HAISI' : 'Connect Web3 Wallet to Buy $HAISI';",
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# -------------------------------------------------------------
# 3. PATCH index.html & app/index.html
# -------------------------------------------------------------
def patch_index(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # A. Hide crossed out section (<main class="max-w-7xl mx-auto px-4 sm:px-6 py-12">)
    old_main = '<main class="max-w-7xl mx-auto px-4 sm:px-6 py-12">'
    new_main = '<main class="max-w-7xl mx-auto px-4 sm:px-6 py-12 hidden" style="display: none !important;">'

    if old_main in content:
        content = content.replace(old_main, new_main)
        print(f'{filepath}: Successfully hid crossed-out main section!')
    else:
        print(f'{filepath}: old_main not found directly!')

    # B. Hide Apple Pay and Card in index deposit-modal
    old_index_tabs = r'<div class="flex space-x-2 my-4 p-1 rounded-2xl bg-neutral-100 dark:bg-neutral-900 text-xs font-medium">\s*<button id="index-pay-apple"[\s\S]*?<button id="index-pay-card"[\s\S]*?<button id="index-pay-web3"[\s\S]*?<\/button>\s*<\/div>'

    new_index_tabs = """<div class="my-4 p-1 rounded-2xl bg-neutral-100 dark:bg-neutral-900 text-xs font-medium">
        <button id="index-pay-apple" type="button" class="hidden" style="display: none !important;"></button>
        <button id="index-pay-card" type="button" class="hidden" style="display: none !important;"></button>
        <button id="index-pay-web3" type="button" class="w-full py-2.5 rounded-xl bg-white dark:bg-black text-black dark:text-white shadow-xs font-semibold flex items-center justify-center space-x-2 transition-all">
          <span class="w-2 h-2 rounded-full bg-black dark:bg-white animate-pulse"></span>
          <span data-i18n="modal.depositWeb3">Web3 Wallet (Solana / EVM)</span>
        </button>
      </div>"""

    if re.search(old_index_tabs, content):
        content = re.sub(old_index_tabs, new_index_tabs, content)
        print(f'{filepath}: Successfully updated index deposit-modal tabs!')
    else:
        print(f'{filepath}: old_index_tabs not matched!')

    # C. Update default indexDepositMethod in script
    content = content.replace("let indexDepositMethod = 'apple';", "let indexDepositMethod = 'web3';")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

patch_dashboard('dashboard.html')
patch_dashboard('app/dashboard.html')
patch_sale_controller('sale-controller.js')
patch_sale_controller('app/sale-controller.js')
patch_index('index.html')
patch_index('app/index.html')

print('ALL 3 FIXES APPLIED!')
