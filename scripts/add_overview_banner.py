import sys
sys.stdout.reconfigure(encoding='utf-8')

BANNER = '''<!-- High-Impact AI Integration Banner -->
        <div class="p-3.5 sm:p-5 rounded-2xl sm:rounded-3xl border border-emerald-500/30 bg-gradient-to-r from-emerald-500/10 via-teal-500/5 to-transparent dark:from-emerald-950/30 dark:via-teal-950/15 dark:to-black/50 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 sm:gap-4 relative overflow-hidden">
          <div class="flex items-center space-x-3 sm:space-x-4 min-w-0">
            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-2xl bg-gradient-to-tr from-emerald-600 to-teal-500 text-white flex items-center justify-center shrink-0 shadow-md shadow-emerald-500/25">
              <i data-lucide="bot" class="w-5 h-5 sm:w-6 sm:h-6"></i>
            </div>
            <div class="min-w-0">
              <div class="flex items-center space-x-2">
                <h3 class="font-bold text-sm sm:text-base text-black dark:text-white truncate">Kết nối HAICHAIN với AI</h3>
                <span class="px-2 py-0.5 rounded-full text-[9.5px] font-mono font-bold bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30 shrink-0">3 Lựa Chọn</span>
              </div>
              <p class="text-[11px] sm:text-xs text-neutral-500 dark:text-neutral-400 mt-0.5 truncate">Claude Desktop (1-Click) &bull; Claude.ai Web &bull; Web3 Playground</p>
            </div>
          </div>
          <button type="button" onclick="document.getElementById('ai-hub-btn').click()" class="w-full sm:w-auto px-4 py-2 sm:py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-bold text-xs shadow-sm flex items-center justify-center space-x-2 shrink-0 transition-all active:scale-95 cursor-pointer">
            <i data-lucide="zap" class="w-3.5 h-3.5 fill-current"></i>
            <span>Kết Nối AI Ngay</span>
          </button>
        </div>'''

for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    target = '<section id="tab-overview" class="tab-content space-y-6">'
    if target in text and 'High-Impact AI Integration Banner' not in text:
        text = text.replace(target, target + '\n        \n        ' + BANNER)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Added banner to {path}")
    else:
        print(f"Banner already in {path} or target missing")
