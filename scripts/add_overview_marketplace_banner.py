import re

banner_html = '''        <!-- ================= GLOBAL AGENT MARKETPLACE QUICK GATEWAY BANNER ================= -->
        <div class="p-5 sm:p-6 rounded-2xl sm:rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/70 dark:bg-neutral-900/40 space-y-4">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="space-y-1">
              <div class="flex items-center space-x-2">
                <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-mono font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 mr-1.5 animate-pulse"></span>
                  CONNECTED & LIVE
                </span>
                <span class="text-xs font-mono text-neutral-400">Phase 1 Integration</span>
              </div>
              <h3 class="text-sm sm:text-base font-bold text-black dark:text-white">
                Global Agent Labor Marketplace (Sàn Việc Làm Agent Quốc Tế)
              </h3>
              <p class="text-xs text-neutral-500 max-w-2xl leading-relaxed">
                Hệ thống HAICHAIN đã kết nối với các sàn Agent hàng đầu thế giới: <strong class="text-black dark:text-white">Smithery MCP Registry</strong> (2,140+ Nodes cào dữ liệu & tự động hóa), <strong class="text-black dark:text-white">Fetch.ai Agentverse</strong> (850+ Agents tài chính & Arbitrage DEX), và <strong class="text-black dark:text-white">Glama</strong> (430+ Nodes kiểm toán bảo mật).
              </p>
            </div>
            <div class="flex items-center gap-2 shrink-0">
              <button onclick="document.querySelector('[data-tab=\\'tab-agents\\']')?.click(); window.scrollTo({top: 400, behavior: 'smooth'});" class="px-4 py-2.5 rounded-xl bg-black text-white dark:bg-white dark:text-black hover:opacity-90 font-semibold text-xs transition-all shadow-sm flex items-center space-x-2 cursor-pointer">
                <span>Vào Sàn Agent Quốc Tế (Tab 2)</span>
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </button>
            </div>
          </div>

          <div class="pt-3 border-t border-neutral-200/60 dark:border-neutral-800 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div class="flex flex-wrap items-center gap-2 font-mono text-[11px]">
              <a href="https://smithery.ai" target="_blank" class="px-2.5 py-1 rounded-lg bg-white dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-700 hover:text-black dark:hover:text-white flex items-center space-x-1">
                <span>Smithery Registry</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
              <a href="https://agentverse.ai" target="_blank" class="px-2.5 py-1 rounded-lg bg-white dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-700 hover:text-black dark:hover:text-white flex items-center space-x-1">
                <span>Fetch.ai Agentverse</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
              <a href="https://glama.ai/mcp/servers" target="_blank" class="px-2.5 py-1 rounded-lg bg-white dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-700 hover:text-black dark:hover:text-white flex items-center space-x-1">
                <span>Glama MCP Hub</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>
            <span class="text-[11px] font-mono text-neutral-400">
              Giao thức: <code class="text-neutral-600 dark:text-neutral-300">discover_global_agents</code> + <code class="text-neutral-600 dark:text-neutral-300">hire_global_agent</code>
            </span>
          </div>
        </div>
'''

for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    target = '<!-- ================= EARLY BACKER ALLOCATIONS & VESTING'
    if target in html and 'GLOBAL AGENT MARKETPLACE QUICK GATEWAY BANNER' not in html:
        html = html.replace(target, banner_html + '\n        ' + target)
        print(f"Added Quick Gateway Banner to {path}")
    else:
        print(f"Already present or target not found in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Done inserting banner!")
