# -*- coding: utf-8 -*-
import re
import time

print("=== 1. OPTIMIZING TOP STATUS BANNER IN HTML FILES ===")

new_banner_snippet = '''  <!-- TOP STATUS BANNER: LIVE SOLANA DEVNET CLUSTER -->

  <div class="border-b border-brand-lightBorder dark:border-brand-border bg-neutral-100/90 dark:bg-neutral-950/90 backdrop-blur-md text-[11px] sm:text-xs py-1.5 sm:py-2 px-2.5 sm:px-4">

    <div class="max-w-7xl mx-auto flex items-center justify-between gap-1.5 sm:gap-2">

      <div class="flex items-center space-x-1.5 sm:space-x-2 shrink-0 min-w-0">

        <span class="inline-block w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full bg-black dark:bg-white animate-pulse shrink-0"></span>

        <span class="text-neutral-700 dark:text-neutral-300 font-medium whitespace-nowrap" data-i18n="cluster.devnetLive">Solana Devnet Live</span>

        <span class="text-neutral-400 dark:text-neutral-600 hidden sm:inline">|</span>

        <span class="text-neutral-500 dark:text-neutral-400 font-mono hidden sm:inline"><span data-i18n="cluster.programLabel">Program:</span> <a href="https://explorer.solana.com/address/DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk?cluster=devnet" target="_blank" class="underline hover:text-black dark:hover:text-white">DK4Q...w4xk</a></span>

        <span class="hidden md:inline text-neutral-400 dark:text-neutral-600">|</span>

        <span class="hidden md:inline text-black dark:text-white font-mono font-semibold whitespace-nowrap" data-i18n="cluster.auditsPassed">15/15 Test Vectors Verified</span>

      </div>

      <div class="flex items-center space-x-2 sm:space-x-4 shrink-0">

        <a href="https://explorer.solana.com/tx/4946birjjYz3DHxjNuq1D9gviny1xoGvYWxQop2gNzD1APykHJXUQZbNAhqeBS9oXEL6D1YMyZUNgKD1ikjrGcdA?cluster=devnet" target="_blank" class="text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 whitespace-nowrap">

          <span data-i18n="cluster.genesisTx">Verified Genesis Tx</span>

          <i data-lucide="external-link" class="w-3 h-3 shrink-0"></i>

        </a>

      </div>

    </div>

  </div>'''

for path in ['index.html', 'app/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    pattern = r'<!-- TOP STATUS BANNER: LIVE SOLANA DEVNET CLUSTER -->[\s\S]*?<!-- NAVIGATION BAR'
    replacement = new_banner_snippet + '\n\n\n\n  <!-- NAVIGATION BAR'
    c_new = re.sub(pattern, replacement, c, count=1)
    if c_new != c:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c_new)
        print(f"OK: Updated top status banner in {path}")
    else:
        print(f"WARN: Could not find top status banner in {path}")

print("\n=== 2. OPTIMIZING VIETNAMESE STRINGS IN i18n.js & app/i18n.js ===")
for p in ['i18n.js', 'app/i18n.js']:
    with open(p, 'r', encoding='utf-8') as f:
        txt = f.read()
    
    txt = txt.replace('"cluster.devnetLive": "Solana Devnet Đang Chạy"', '"cluster.devnetLive": "Solana Devnet Trực Tiếp"')
    txt = txt.replace('"cluster.genesisTx": "Giao dịch Genesis Đã xác thực"', '"cluster.genesisTx": "Tx Genesis Đã Xác Thực"')
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f"OK: Updated Vietnamese cluster strings in {p}")

print("\n=== 3. BUMPING SCRIPT CACHE VERSION ===")
new_cache = f"v31_mobile_top_banner_{int(time.time())}"
for fpath in ['index.html', 'app/index.html', 'dashboard.html', 'app/dashboard.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        fc = f.read()
    fc = re.sub(r'i18n\.js\?v=[^"\'\s>]+', f'i18n.js?v={new_cache}', fc)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(fc)
    print(f"OK: Bumped cache in {fpath} to {new_cache}")
