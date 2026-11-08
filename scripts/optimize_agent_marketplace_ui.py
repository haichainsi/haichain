import os
import re

print("=== Optimizing Agent Marketplace for Mobile & Desktop (Strict Monochrome) ===")

target_files = ['dashboard.html', os.path.join('app', 'dashboard.html')]

for fpath in target_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update open-register-agent-modal-btn styling to pure monochrome (no emerald)
    html = re.sub(
        r'<button id="open-register-agent-modal-btn"[^>]*>',
        '<button id="open-register-agent-modal-btn" class="flex-1 sm:flex-none px-3.5 py-2.5 rounded-xl text-xs font-semibold bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 border border-black dark:border-white shrink-0 transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1.5 shadow-xs whitespace-nowrap">',
        html
    )

    # 2. Update sync-global-registries-btn styling for mobile & desktop
    html = re.sub(
        r'<button id="sync-global-registries-btn"[^>]*>',
        '<button id="sync-global-registries-btn" onclick="window.syncGlobalRegistries?.();" class="flex-1 sm:flex-none px-3.5 py-2.5 rounded-xl text-xs font-semibold bg-neutral-100 hover:bg-neutral-200 text-neutral-800 dark:bg-neutral-900 dark:hover:bg-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 shrink-0 transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1.5 shadow-xs whitespace-nowrap" title="Sync live mesh nodes">',
        html
    )

    # 3. Clean up category filters container and buttons
    old_cat_block = r'<div class="flex items-center gap-1\.5 overflow-x-auto no-scrollbar py-0\.5" id="market-category-filters">[\s\S]*?</div>\s*</div>'
    new_cat_block = '''<div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-0.5 -mx-1 px-1" id="market-category-filters">
              <button class="market-cat-btn px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-black text-white dark:bg-white dark:text-black border border-black dark:border-white shrink-0 transition-all cursor-pointer whitespace-nowrap shadow-xs active:scale-98" data-category="all" data-i18n="marketplace.catAll">
                All Categories
              </button>
              <button class="market-cat-btn px-3.5 py-1.5 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer whitespace-nowrap active:scale-98" data-category="data_extraction" data-i18n="marketplace.catScraping">
                Web Scraping
              </button>
              <button class="market-cat-btn px-3.5 py-1.5 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer whitespace-nowrap active:scale-98" data-category="financial_intelligence" data-i18n="marketplace.catAlpha">
                Market Alpha
              </button>
              <button class="market-cat-btn px-3.5 py-1.5 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer whitespace-nowrap active:scale-98" data-category="security_audit" data-i18n="marketplace.catSecurity">
                Security Audit
              </button>
              <button class="market-cat-btn px-3.5 py-1.5 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer whitespace-nowrap active:scale-98" data-category="automation" data-i18n="marketplace.catCompute">
                TEE Compute
              </button>
            </div>
          </div>'''
    html = re.sub(old_cat_block, new_cat_block, html)

    # 4. Remove all emerald SLA badges in tab-agents and replace with clean monochrome
    html = html.replace(
        'text-[10px] font-mono text-emerald-600 dark:text-emerald-400 font-semibold shrink-0',
        'text-[10px] font-mono text-neutral-600 dark:text-neutral-400 font-semibold shrink-0'
    )

    # 5. Hire modal: replace emerald colors with pure monochrome
    html = html.replace(
        '<span class="font-bold text-emerald-600 dark:text-emerald-400">Solana Devnet L1</span>',
        '<span class="font-bold text-black dark:text-white">Solana Devnet L1</span>'
    )
    html = html.replace(
        'bg-emerald-500/10 border border-emerald-500/20 text-xs space-y-2',
        'bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-xs space-y-2'
    )
    html = html.replace(
        'text-emerald-700 dark:text-emerald-400 font-semibold',
        'text-black dark:text-white font-semibold'
    )
    html = html.replace(
        'underline text-emerald-600 dark:text-emerald-400 hover:text-black dark:hover:text-white font-semibold',
        'underline text-black dark:text-white font-semibold'
    )

    # 6. Register Agent modal: replace emerald colors with monochrome
    html = html.replace(
        'bg-emerald-500/10 text-emerald-500 flex items-center justify-center font-bold text-sm',
        'bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white border border-neutral-200 dark:border-neutral-700 flex items-center justify-center font-bold text-sm'
    )
    html = html.replace(
        'px-5 py-2 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition-all active:scale-98 cursor-pointer',
        'px-5 py-2.5 rounded-xl text-xs font-semibold bg-black hover:bg-neutral-800 text-white dark:bg-white dark:hover:bg-neutral-200 dark:text-black border border-black dark:border-white transition-all active:scale-98 cursor-pointer shadow-xs'
    )

    # 7. Update JS category click handler classes to match clean styling
    old_cat_click = r'catBtns\.forEach\(btn => \{[\s\S]*?loadGlobalAgentMarketplace\(\);\s*\}\);'
    new_cat_click = '''catBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          catBtns.forEach(b => {
            b.className = "market-cat-btn px-3.5 py-1.5 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer whitespace-nowrap active:scale-98";
          });
          btn.className = "market-cat-btn px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-black text-white dark:bg-white dark:text-black border border-black dark:border-white shrink-0 transition-all cursor-pointer whitespace-nowrap shadow-xs active:scale-98";
          currentMarketCategory = btn.getAttribute('data-category') || 'all';
          loadGlobalAgentMarketplace();
        });
      });'''
    html = re.sub(old_cat_click, new_cat_click, html)

    # 8. Update renderGlobalAgentMarketplace JS template SLA badge
    html = html.replace(
        'text-emerald-600 dark:text-emerald-400 font-semibold shrink-0',
        'text-neutral-600 dark:text-neutral-400 font-semibold shrink-0'
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Optimized {fpath}")

print("=== All updates completed successfully ===")
