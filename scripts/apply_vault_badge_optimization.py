import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update i18n.js and app/i18n.js
i18n_files = ['i18n.js', 'app/i18n.js']

frozen_replacements = {
    '"vault.status.frozen": "Мұздатылған (Апаттық күйде)"': '"vault.status.frozen": "Бұғатталған"',
    '"vault.status.frozen": "Frozen (Panic Tripped)"': '"vault.status.frozen": "Frozen"',
    '"vault.status.frozen": "已冻结 (熔断已触发)"': '"vault.status.frozen": "已冻结"',
    '"vault.status.frozen": "Gelé (Arrêt d\'Urgence Déclenché)"': '"vault.status.frozen": "Gelé"',
    '"vault.status.frozen": "동결됨 (비상 차단 활성화)"': '"vault.status.frozen": "동결됨"',
    '"vault.status.frozen": "Congelada (Pánico Activado)"': '"vault.status.frozen": "Congelada"',
    '"vault.status.frozen": "Заморожено (Сработал Стоп)"': '"vault.status.frozen": "Заморожено"',
    '"vault.status.frozen": "Đã Đóng Băng (Kích Hoạt Panic)"': '"vault.status.frozen": "Đã Đóng Băng"',
    '"vault.status.frozen": "फ्रोजन (पैनिक ट्रिगर)"': '"vault.status.frozen": "फ्रोजन"',
    '"vault.status.frozen": "מוקפא (מצב חירום הופעל)"': '"vault.status.frozen": "מוקפא"'
}

for fpath in i18n_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    for old_k, new_k in frozen_replacements.items():
        if old_k in c:
            c = c.replace(old_k, new_k)
            print(f"[{fpath}] Replaced {old_k}")
        else:
            print(f"[{fpath}] Note: {old_k} not found directly")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("i18n files updated.")

# 2. Update dashboard.html and app/dashboard.html
dash_files = ['dashboard.html', 'app/dashboard.html']

for fpath in dash_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # A. Restructure Main Balance Card header so badge and title share the top line,
    # and $0.0000 balance sits on its own line below
    old_card_head = """          <!-- Main Balance Card (Spans 2 Cols - Mobile Optimized) -->
          <div class="md:col-span-2 p-4 sm:p-6 rounded-2xl sm:rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm relative overflow-hidden">
            <div class="flex justify-between items-start gap-2">
              <div class="min-w-0">
                <span class="text-xs uppercase tracking-wider text-neutral-400 font-mono font-medium truncate block" data-i18n="vault.activePot">Active Spending Pot</span>
                <div class="text-3xl sm:text-5xl font-extrabold tracking-tight font-mono text-black dark:text-white tabular-nums mt-1.5 sm:mt-2 flex items-baseline">
                  <span>$</span>
                  <span id="overview-balance">0.0000</span>
                  <span class="text-xs font-mono text-neutral-500 ml-1.5 sm:ml-2">USDT</span>
                </div>
                <p class="text-xs text-neutral-500 font-mono mt-0.5 sm:mt-1 truncate" id="overview-credits" data-i18n="vault.actionCredits">&asymp; 0 Action Credits Available</p>
              </div>
              <span id="vault-status-badge" class="px-2 py-0.5 sm:px-2.5 sm:py-1 rounded-full text-[10px] sm:text-[11px] font-mono font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 flex items-center space-x-1.5 shrink-0 shadow-xs">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                <span data-i18n="vault.status.active">Active</span>
              </span>
            </div>"""

    new_card_head = """          <!-- Main Balance Card (Spans 2 Cols - Mobile Optimized) -->
          <div class="md:col-span-2 p-4 sm:p-6 rounded-2xl sm:rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm relative overflow-hidden">
            <!-- Top Line: Label & Status Badge (Clean Space Allocation, Zero Collision) -->
            <div class="flex items-center justify-between gap-2">
              <span class="text-[11px] sm:text-xs uppercase tracking-wider text-neutral-400 font-mono font-medium truncate" data-i18n="vault.activePot">Active Spending Pot</span>
              <span id="vault-status-badge" class="px-2 py-0.5 sm:px-2.5 sm:py-1 rounded-full text-[10px] sm:text-[11px] font-mono font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 inline-flex items-center space-x-1.5 shrink-0 whitespace-nowrap shadow-xs">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
                <span data-i18n="vault.status.active" class="whitespace-nowrap">Active</span>
              </span>
            </div>

            <!-- Value Row: Prominent Balance Display -->
            <div class="text-3xl sm:text-5xl font-extrabold tracking-tight font-mono text-black dark:text-white tabular-nums mt-1.5 sm:mt-2 flex items-baseline">
              <span>$</span>
              <span id="overview-balance">0.0000</span>
              <span class="text-xs font-mono text-neutral-500 ml-1.5 sm:ml-2">USDT</span>
            </div>

            <!-- Subtitle Row: Credits (Never Truncated by Badge) -->
            <p class="text-xs text-neutral-500 font-mono mt-0.5 sm:mt-1 truncate" id="overview-credits" data-i18n="vault.actionCredits">&asymp; 0 Action Credits Available</p>"""

    if old_card_head in content:
        content = content.replace(old_card_head, new_card_head)
        print(f"[{fpath}] Replaced card header HTML structure")
    else:
        print(f"[{fpath}] Note: old_card_head not matched exactly")

    # B. Update JS lines where vaultStatusBadge is updated
    # 1. Normal state:
    old_badge_normal = 'vaultStatusBadge.className = "px-2.5 py-1 rounded-full text-[11px] font-medium bg-black text-white dark:bg-white dark:text-black flex items-center space-x-1.5 font-mono shadow-xs";'
    new_badge_normal = 'vaultStatusBadge.className = "px-2 py-0.5 sm:px-2.5 sm:py-1 rounded-full text-[10px] sm:text-[11px] font-mono font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 inline-flex items-center space-x-1.5 shrink-0 whitespace-nowrap shadow-xs";'

    content = content.replace(old_badge_normal, new_badge_normal)

    # 2. Normal innerHTML:
    old_badge_normal_inner = 'vaultStatusBadge.innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-white dark:bg-black animate-ping"></span><span data-i18n="vault.status.active">${window.haichainI18n ? window.haichainI18n.t(\'vault.status.active\') : \'Active\'}</span>`;'
    new_badge_normal_inner = 'vaultStatusBadge.innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse shrink-0"></span><span data-i18n="vault.status.active" class="whitespace-nowrap">${window.haichainI18n ? window.haichainI18n.t(\'vault.status.active\') : \'Active\'}</span>`;'

    content = content.replace(old_badge_normal_inner, new_badge_normal_inner)

    # 3. Frozen state:
    old_badge_frozen = 'vaultStatusBadge.className = "px-2.5 py-1 rounded-full text-[11px] font-medium border-2 border-black dark:border-white text-black dark:text-white bg-neutral-100 dark:bg-neutral-900 flex items-center space-x-1.5 font-mono";'
    new_badge_frozen = 'vaultStatusBadge.className = "px-2 py-0.5 sm:px-2.5 sm:py-1 rounded-full text-[10px] sm:text-[11px] font-mono font-semibold bg-red-500/10 text-red-600 dark:text-red-400 border border-red-500/20 inline-flex items-center space-x-1.5 shrink-0 whitespace-nowrap shadow-xs";'

    content = content.replace(old_badge_frozen, new_badge_frozen)

    # 4. Frozen innerHTML:
    old_badge_frozen_inner = 'vaultStatusBadge.innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white"></span><span data-i18n="vault.status.frozen">${window.haichainI18n ? window.haichainI18n.t(\'vault.status.frozen\') : \'Frozen (Panic Tripped)\'}</span>`;'
    new_badge_frozen_inner = 'vaultStatusBadge.innerHTML = `<span class="w-1.5 h-1.5 rounded-full bg-red-500 animate-ping shrink-0"></span><span data-i18n="vault.status.frozen" class="whitespace-nowrap">${window.haichainI18n ? window.haichainI18n.t(\'vault.status.frozen\') : \'Frozen\'}</span>`;'

    content = content.replace(old_badge_frozen_inner, new_badge_frozen_inner)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Dashboard files updated.")
