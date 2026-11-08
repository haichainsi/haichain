import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 1. PATCH sale-controller.js and app/sale-controller.js (Items 1, 2, 5)
# ==============================================================================
def patch_sale_controller(filepath):
    print(f"--- Patching {filepath} ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- Item 1: Purple button -> Stealth Black Luxury button ---
    old_btn1 = r'<button type="button" id="btn-pay-phantom-1click" class="[^"]*bg-purple-600[^"]*">'
    new_btn1 = '<button type="button" id="btn-pay-phantom-1click" class="w-full py-3 px-4 rounded-xl bg-black hover:bg-neutral-900 text-white font-bold text-xs font-mono flex items-center justify-center space-x-2 transition-all shadow-sm cursor-pointer active:scale-98 border border-neutral-700/80 hover:border-neutral-400">'

    if re.search(old_btn1, content):
        content = re.sub(old_btn1, new_btn1, content)
        print("✓ Item 1 (Phantom Pay button) changed to Premium Black Luxury")
    else:
        # Fallback check if already modified
        idx = content.find('id="btn-pay-phantom-1click"')
        if idx != -1:
            tag_start = content.rfind('<button', 0, idx)
            tag_end = content.find('>', idx) + 1
            content = content[:tag_start] + new_btn1 + content[tag_end:]
            print("✓ Item 1 changed via fallback index slice")

    # --- Item 2: Calculator input `$ 2500` truncation on mobile ---
    # Look for the container holding calc-usdt-input and btn-quick-calc
    old_calc_container = r'<div class="flex items-center gap-2">\s*<div class="flex items-center space-x-1\.5 flex-1 px-3 py-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-300 dark:border-neutral-800[^"]*">\s*<span class="[^"]*">\$</span>\s*<input type="number" id="calc-usdt-input"[^>]*>\s*</div>\s*<div class="flex gap-1 shrink-0">[\s\S]*?</div>\s*</div>'
    new_calc_container = '''<div class="flex flex-col sm:flex-row sm:items-center gap-2">
                <div class="flex items-center space-x-2 flex-1 px-3.5 py-2.5 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-300 dark:border-neutral-800 focus-within:border-black dark:focus-within:border-white transition-colors">
                  <span class="text-lg sm:text-xl font-bold text-neutral-400">$</span>
                  <input type="number" id="calc-usdt-input" value="1000" min="500" max="15000" step="100" class="w-full bg-transparent text-lg sm:text-xl font-black text-black dark:text-white focus:outline-none tabular-nums">
                </div>
                <div class="grid grid-cols-4 sm:flex gap-1.5 shrink-0">
                  <button type="button" class="btn-quick-calc py-2 px-1 sm:px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all text-center active:scale-95 cursor-pointer" data-amount="1000">$1k</button>
                  <button type="button" class="btn-quick-calc py-2 px-1 sm:px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all text-center active:scale-95 cursor-pointer" data-amount="2500">$2.5k</button>
                  <button type="button" class="btn-quick-calc py-2 px-1 sm:px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all text-center active:scale-95 cursor-pointer" data-amount="5000">$5k</button>
                  <button type="button" class="btn-quick-calc py-2 px-1 sm:px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all text-center active:scale-95 cursor-pointer" data-amount="10000">$10k</button>
                </div>
              </div>'''

    if re.search(old_calc_container, content):
        content = re.sub(old_calc_container, new_calc_container, content)
        print("✓ Item 2 (Calculator input) optimized for 100% width on mobile + 4-col preset grid")
    else:
        # Fallback index search
        idx2 = content.find('id="calc-usdt-input"')
        if idx2 != -1:
            div_start = content.rfind('<div class="flex items-center gap-2">', 0, idx2)
            btn10k = content.find('data-amount="10000"', idx2)
            div_end = content.find('</div>', content.find('</div>', btn10k) + 1) + 6
            content = content[:div_start] + new_calc_container + content[div_end:]
            print("✓ Item 2 replaced via fallback index slice")

    # --- Item 5: View SAFT Agreement & 1-Pager Memo buttons ---
    old_item5 = r'<div class="flex flex-wrap gap-2 pt-1">\s*<button type="button" id="btn-open-saft-pdf"[\s\S]*?</button>\s*<button type="button" id="btn-open-memo-pdf"[\s\S]*?</button>\s*</div>'
    new_item5 = '''<div class="grid grid-cols-2 sm:flex gap-2 pt-1">
            <button type="button" id="btn-open-saft-pdf" class="flex-1 py-2.5 px-2 sm:px-3.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-medium text-[11px] sm:text-xs font-mono transition-all flex items-center justify-center space-x-1 sm:space-x-1.5 hover:opacity-90 active:scale-95 shadow-sm cursor-pointer truncate" title="Đọc hợp đồng SAFT online">
              <i data-lucide="file-text" class="w-3.5 h-3.5 shrink-0"></i>
              <span class="truncate whitespace-nowrap">${getI18nText('downloadSaft')}</span>
            </button>
            <button type="button" id="btn-open-memo-pdf" class="flex-1 py-2.5 px-2 sm:px-3.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-medium text-[11px] sm:text-xs font-mono transition-all flex items-center justify-center space-x-1 sm:space-x-1.5 active:scale-95 cursor-pointer truncate" title="Đọc bản tóm tắt Memo online">
              <i data-lucide="book-open" class="w-3.5 h-3.5 shrink-0"></i>
              <span class="truncate whitespace-nowrap">${getI18nText('downloadMemo')}</span>
            </button>
          </div>'''

    if re.search(old_item5, content):
        content = re.sub(old_item5, new_item5, content)
        print("✓ Item 5 (SAFT / Memo buttons) converted to balanced 2-column mobile grid")
    else:
        idx5 = content.find('id="btn-open-saft-pdf"')
        if idx5 != -1:
            div_start = content.rfind('<div class="flex flex-wrap gap-2 pt-1">', 0, idx5)
            btn_memo = content.find('id="btn-open-memo-pdf"', idx5)
            div_end = content.find('</div>', content.find('</button>', btn_memo)) + 6
            content = content[:div_start] + new_item5 + content[div_end:]
            print("✓ Item 5 replaced via fallback index slice")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath} ({len(content)} bytes)\n")

# ==============================================================================
# 2. PATCH dashboard.html and app/dashboard.html (Items 3, 4)
# ==============================================================================
def patch_dashboard(filepath):
    print(f"--- Patching {filepath} ---")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- Item 3A: Sub-Agent Capability Tree header & Issue Ticket Button ---
    old_item3a = r'<div class="flex justify-between items-center">\s*<div>\s*<h2 class="font-bold text-lg text-black dark:text-white" data-i18n="swarm\.title">Sub-Agent Capability Tree</h2>\s*<p class="text-xs text-neutral-500" data-i18n="swarm\.subtitle">Issue ephemeral, mathematically bounded spending tickets for your autonomous AI agents\.</p>\s*</div>\s*<button id="open-issue-ticket-modal" class="px-4 py-2 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-xs font-semibold flex items-center space-x-2">\s*<i data-lucide="plus" class="w-3\.5 h-3\.5"></i>\s*<span data-i18n="swarm\.issueTicket">Issue Capability Ticket</span>\s*</button>\s*</div>'
    new_item3a = '''<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h2 class="font-bold text-base sm:text-lg text-black dark:text-white" data-i18n="swarm.title">Sub-Agent Capability Tree</h2>
            <p class="text-xs text-neutral-500 mt-0.5" data-i18n="swarm.subtitle">Issue ephemeral, mathematically bounded spending tickets for your autonomous AI agents.</p>
          </div>
          <button id="open-issue-ticket-modal" class="w-full sm:w-auto px-4 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-xs font-semibold flex items-center justify-center space-x-2 shrink-0 shadow-xs active:scale-98 cursor-pointer">
            <i data-lucide="plus" class="w-3.5 h-3.5 shrink-0"></i>
            <span class="whitespace-nowrap font-medium" data-i18n="swarm.issueTicket">Issue Capability Ticket</span>
          </button>
        </div>'''

    if re.search(old_item3a, content):
        content = re.sub(old_item3a, new_item3a, content)
        print("✓ Item 3A (Sub-Agent Tree header & Issue Ticket button) optimized for mobile")
    else:
        idx3a = content.find('id="open-issue-ticket-modal"')
        if idx3a != -1:
            div_start = content.rfind('<div class="flex justify-between items-center">', 0, idx3a)
            div_end = content.find('</div>', content.find('</button>', idx3a)) + 6
            content = content[:div_start] + new_item3a + content[div_end:]
            print("✓ Item 3A replaced via fallback index slice")

    # --- Item 3B: Symmetrical 4 AI Platform Connector Cards ---
    # In Claude card, balance the button layout to match OpenAI, Gemini, DeepSeek perfectly
    old_claude_card = r'<!-- 2\. Claude -->\s*<div class="p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 flex flex-col justify-between space-y-3">\s*<div class="flex items-center space-x-2\.5">[\s\S]*?</div>\s*<div class="space-y-1\.5 w-full">\s*<button class="connect-ai-provider-btn[^"]*"[^>]*>\s*Connect\s*</button>\s*<button type="button" onclick="document\.getElementById\(\'ai-hub-btn\'\)\.click\(\)"[^>]*>[\s\S]*?</button>\s*</div>\s*</div>'
    new_claude_card = '''<!-- 2. Claude -->
            <div class="p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 flex flex-col justify-between space-y-3">
              <div class="flex items-center space-x-2.5">
                <div class="w-8 h-8 rounded-xl bg-neutral-200 dark:bg-neutral-800 flex items-center justify-center font-bold text-sm text-black dark:text-white">
                  <i data-lucide="sparkles" class="w-4 h-4"></i>
                </div>
                <div>
                  <div class="flex items-center space-x-1.5">
                    <div class="font-semibold text-xs text-black dark:text-white">Claude</div>
                    <span class="text-[9px] font-mono px-1 py-0.2 rounded bg-neutral-200 dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400">MCP</span>
                  </div>
                  <div class="text-[10px] text-neutral-400">3.5 Sonnet, 3.7</div>
                </div>
              </div>
              <button class="connect-ai-provider-btn w-full py-1.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-xs font-semibold text-black dark:text-white transition-all cursor-pointer" data-i18n="connectors.btnConnect" data-provider="Anthropic Claude" data-models="Claude 3.5 Sonnet">
                Connect
              </button>
            </div>'''

    if re.search(old_claude_card, content):
        content = re.sub(old_claude_card, new_claude_card, content)
        print("✓ Item 3B (Claude card) balanced with single Connect button & MCP badge for 100% grid symmetry")
    else:
        idx_c = content.find('<!-- 2. Claude -->')
        if idx_c != -1:
            card_end = content.find('<!-- 3. Gemini -->', idx_c)
            content = content[:idx_c] + new_claude_card + '\n\n            ' + content[card_end:]
            print("✓ Item 3B replaced via fallback index slice")

    # --- Item 4: Token-2022 Vesting Vault & Solana L1 badge in renderVestingVaultPage ---
    old_item4 = r'<div class="flex items-center space-x-3">\s*<div class="w-10 h-10 rounded-xl bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1\.5"><img src="/assets/haisi-icon\.png\?v=haisi_symbol_2026"[^>]*>\s*</div>\s*<div>\s*<div class="flex items-center space-x-2">\s*<h2 class="font-bold text-lg sm:text-xl text-black dark:text-white">\s*\$\{getVestingText\(\'vaultTitle\', lang\)\}\s*</h2>\s*<span class="px-2\.5 py-0\.5 rounded-full text-\[10px\] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800">\s*Solana L1\s*</span>\s*</div>\s*</div>\s*</div>'
    new_item4 = '''<div class="flex items-start space-x-3">
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
                </div>'''

    if re.search(old_item4, content):
        content = re.sub(old_item4, new_item4, content)
        print("✓ Item 4 (Vesting Title & Solana L1 badge) optimized with items-start justify-between and shrink-0")
    else:
        idx4 = content.find("getVestingText('vaultTitle', lang)")
        if idx4 != -1:
            div_start = content.rfind('<div class="flex items-center space-x-3">', 0, idx4)
            div_end = content.find('</div>\n                  </div>\n                </div>', idx4) + 40
            content = content[:div_start] + new_item4 + content[div_end:]
            print("✓ Item 4 replaced via fallback index slice")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath} ({len(content)} bytes)\n")

# Run patches
for p in ['sale-controller.js', 'app/sale-controller.js']:
    patch_sale_controller(p)

for p in ['dashboard.html', 'app/dashboard.html']:
    patch_dashboard(p)

print("All patches completed successfully!")
