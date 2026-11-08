import re

def update_sr(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    pattern = re.compile(
        r'<div class="flex items-start space-x-3 min-w-0 flex-1">\s*'
        r'<div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0\.5">\s*'
        r'SR\s*'
        r'</div>\s*'
        r'<div class="min-w-0 flex-1">\s*'
        r'<h4 class="font-semibold text-sm text-black dark:text-white leading-tight">Web SERP Scraper Swarm</h4>\s*'
        r'<div class="text-\[11px\] text-neutral-500 font-mono mt-1 truncate"[^>]*>[\s\S]*?agent_serp_crawler_03\s*</div>\s*'
        r'</div>\s*'
        r'</div>\s*'
        r'<span class="agent-status-badge shrink-0 px-2 py-0\.5 rounded-full text-\[10px\] font-mono whitespace-nowrap [^"]*" data-i18n="agent\.status\.idle">Idle</span>'
    )

    replacement = (
        '<div class="flex items-center space-x-2.5 min-w-0 flex-1">\n'
        '                <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white border border-neutral-200/80 dark:border-neutral-700/80 flex items-center justify-center font-bold text-xs shrink-0">\n'
        '                  SR\n'
        '                </div>\n'
        '                <div class="min-w-0 flex-1">\n'
        '                  <h4 class="font-semibold text-xs sm:text-sm text-black dark:text-white leading-tight truncate" title="Web SERP Scraper Swarm">Web SERP Scraper Swarm</h4>\n'
        '                  <div class="text-[10px] text-neutral-400 font-mono truncate mt-0.5" title="ID: agent_serp_crawler_03">ID: agent_serp_crawler_03</div>\n'
        '                </div>\n'
        '              </div>\n'
        '              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-200 dark:border-neutral-800" data-i18n="agent.status.idle">Idle</span>'
    )

    c, count = pattern.subn(replacement, c)
    print(f"Card SR replaced: {count} in {filepath}")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

update_sr('dashboard.html')
update_sr('app/dashboard.html')
