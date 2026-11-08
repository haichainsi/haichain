import re

# 1. Update dashboard.html & app/dashboard.html
def update_dashboard(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # A. Update Title & Badge
    content = content.replace(
        '<span data-i18n="marketplace.title">Global Agent Marketplace</span>',
        '<span data-i18n="marketplace.title">Global Agent Federation Mesh</span>'
    )
    content = content.replace(
        '<span class="text-[10px] font-mono px-2 py-0.5 rounded-full bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700" data-i18n="marketplace.badge">Mesh Active</span>',
        '<span class="text-[10px] font-mono px-2 py-0.5 rounded-full bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700" data-i18n="marketplace.badge">Solana L1 Escrow Mesh</span>'
    )

    # B. Replace Register Agent button with Sync Registries (Primary) & Monetize SDK Docs (Secondary)
    old_actions = """              <!-- Action Buttons: Register Agent & Fast Sync -->
              <div class="flex items-center gap-2 shrink-0">
                <button id="open-register-agent-modal-btn" class="flex-1 sm:flex-none px-3.5 py-2.5 rounded-xl text-xs font-semibold bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 border border-black dark:border-white shrink-0 transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1.5 shadow-xs whitespace-nowrap">
                  <i data-lucide="plus" class="w-3.5 h-3.5 inline"></i>
                  <span data-i18n="marketplace.registerBtn">Register Agent</span>
                </button>
                <button id="sync-global-registries-btn" onclick="window.syncGlobalRegistries?.();" class="flex-1 sm:flex-none px-3.5 py-2.5 rounded-xl text-xs font-semibold bg-neutral-100 hover:bg-neutral-200 text-neutral-800 dark:bg-neutral-900 dark:hover:bg-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 shrink-0 transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1.5 shadow-xs whitespace-nowrap" title="Sync live mesh nodes">
                  <i data-lucide="refresh-cw" class="w-3.5 h-3.5 inline"></i>
                  <span data-i18n="marketplace.syncShort">Sync</span>
                </button>
              </div>"""

    new_actions = """              <!-- Action Buttons: Fast Sync Global Mesh & Monetize SDK Guide -->
              <div class="flex items-center gap-2 shrink-0">
                <button id="sync-global-registries-btn" onclick="window.syncGlobalRegistries?.();" class="flex-1 sm:flex-none px-4 py-2.5 rounded-xl text-xs font-semibold bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 border border-black dark:border-white shrink-0 transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1.5 shadow-xs whitespace-nowrap" title="Sync live mesh nodes from Smithery, Fetch.ai and Glama">
                  <i data-lucide="refresh-cw" class="w-3.5 h-3.5 inline"></i>
                  <span data-i18n="marketplace.syncRegistriesShort">Sync Global Registries</span>
                </button>
                <button onclick="switchTab('tab-docs');" class="flex-1 sm:flex-none px-3.5 py-2.5 rounded-xl text-xs font-semibold bg-neutral-100 hover:bg-neutral-200 text-neutral-800 dark:bg-neutral-900 dark:hover:bg-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 shrink-0 transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1.5 shadow-xs whitespace-nowrap" title="Monetize your agent with Haichain HTTP 402 Paywall">
                  <i data-lucide="code" class="w-3.5 h-3.5 inline"></i>
                  <span data-i18n="marketplace.devDocsBtn">Monetize Agent (SDK)</span>
                </button>
              </div>"""

    if old_actions in content:
        content = content.replace(old_actions, new_actions)
        print(f"Updated action buttons in {filepath}")
    else:
        print(f"Warning: old_actions not found in {filepath}")

    # C. Remove the modal JS
    js_marker = "const regModal = document.getElementById('register-agent-modal');"
    js_pos = content.find(js_marker)
    if js_pos != -1:
        script_end = content.find("</script>", js_pos)
        if script_end != -1:
            content = content[:js_pos] + content[script_end:]
            print(f"Removed modal JS handler from {filepath}")

    # D. Remove the modal HTML
    modal_start = content.find('<!-- ================= MODAL: REGISTER COMMUNITY AGENT ================= -->')
    if modal_start != -1:
        modal_end = content.find('</div>\n    </div>', modal_start)
        if modal_end != -1:
            modal_end += len('</div>\n    </div>')
            content = content[:modal_start] + content[modal_end:]
            print(f"Removed modal HTML from {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Finished {filepath}")

update_dashboard("dashboard.html")
update_dashboard("app/dashboard.html")

# 2. Update i18n.js & app/i18n.js
TITLES = {
    'kk': {'title': 'Жаһандық AI агенттер федеративті желісі', 'badge': 'Solana L1 Эскроу желісі', 'docs': 'Агентті монетизациялау (SDK)', 'sync': 'Жаһандық түйіндерді синхрондау'},
    'en': {'title': 'Global Agent Federation Mesh', 'badge': 'Solana L1 Escrow Mesh', 'docs': 'Monetize Agent (SDK)', 'sync': 'Sync Global Registries'},
    'zh': {'title': '全球智能体联邦结算网络', 'badge': 'Solana L1 托管网络', 'docs': '智能体收款接入 (SDK)', 'sync': '同步全球节点'},
    'fr': {'title': "Maillage Fédéré & Règlement d'Agents", 'badge': 'Maillage Escrow Solana L1', 'docs': "Monétiser l'Agent (SDK)", 'sync': 'Synchroniser les Registres'},
    'ko': {'title': '글로벌 AI 에이전트 연합 정산 네트워크', 'badge': 'Solana L1 에스크로 네트워크', 'docs': '에이전트 수익화 (SDK)', 'sync': '글로벌 레지스트리 동기화'},
    'es': {'title': 'Red Federada de Liquidación de Agentes', 'badge': 'Red de Custodia Solana L1', 'docs': 'Monetizar Agente (SDK)', 'sync': 'Sincronizar Registros'},
    'ru': {'title': 'Федеративная сеть расчетов AI-агентов', 'badge': 'Эскроу-сеть Solana L1', 'docs': 'Монетизация агента (SDK)', 'sync': 'Синхронизировать узлы'},
    'vi': {'title': 'Lưới Liên hợp & Thanh toán Agent Toàn cầu', 'badge': 'Mạng Bảo chứng Solana L1', 'docs': 'Tích hợp Thu tiền (SDK)', 'sync': 'Đồng bộ Lưới Toàn cầu'},
    'hi': {'title': 'वैश्विक एजेंट फेडरेशन निपटान नेटवर्क', 'badge': 'Solana L1 एस्क्रो मेश', 'docs': 'एजेंट मुद्रीकरण (SDK)', 'sync': 'वैश्विक रजिस्ट्रियां सिंक करें'},
    'he': {'title': 'רשת פדרציית סוכני AI וסליקה גלובלית', 'badge': 'רשת נאמנות Solana L1', 'docs': 'מונטיזציית סוכן (SDK)', 'sync': 'סנכרון רישומים גלובליים'}
}

def update_i18n(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    langs = ['kk', 'en', 'zh', 'fr', 'ko', 'es', 'ru', 'vi', 'hi', 'he']
    for l in langs:
        l_marker = '"' + l + '": {'
        pos1 = text.find(l_marker)
        if pos1 == -1: continue
        next_pos = len(text)
        for l2 in langs:
            if l2 != l:
                p = text.find('"' + l2 + '": {', pos1 + len(l_marker))
                if p != -1 and p < next_pos:
                    next_pos = p

        block = text[pos1:next_pos]
        t_data = TITLES[l]
        
        # Update marketplace.title
        block = re.sub(r'("marketplace\.title":\s*)"((?:\\.|[^"\\])*)"', f'\\1"{t_data["title"]}"', block)
        # Update marketplace.badge
        block = re.sub(r'("marketplace\.badge":\s*)"((?:\\.|[^"\\])*)"', f'\\1"{t_data["badge"]}"', block)
        # Update marketplace.syncRegistriesShort
        block = re.sub(r'("marketplace\.syncRegistriesShort":\s*)"((?:\\.|[^"\\])*)"', f'\\1"{t_data["sync"]}"', block)
        # Add marketplace.devDocsBtn if not exists
        if '"marketplace.devDocsBtn":' not in block:
            block = block.replace(
                f'"marketplace.title": "{t_data["title"]}",',
                f'"marketplace.title": "{t_data["title"]}",\n    "marketplace.devDocsBtn": "{t_data["docs"]}",'
            )

        text = text[:pos1] + block + text[next_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Finished {filepath}")

update_i18n("i18n.js")
update_i18n("app/i18n.js")
