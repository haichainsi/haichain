import re

def update_cards(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    cards = [
        ('C3', 'Claude Desktop (MCP Worker)', 'agent_claude_desktop_01', 'agent.status.active', 'Active'),
        ('CR', 'Cursor Composer Agent', 'agent_cursor_ide_02', 'agent.status.active', 'Active'),
        ('SR', 'Web SERP Scraper Swarm', 'agent_serp_crawler_03', 'agent.status.idle', 'Idle'),
        ('TX', 'Tesla Optimus #12 Kinematics', 'edge_robot_sensor_04', 'agent.status.streaming', 'Streaming'),
    ]

    for icon, title, agent_id, status_key, status_text in cards:
        # Regex to match the old header block for this card
        pattern = re.compile(
            rf'<div class="flex items-start space-x-3 min-w-0 flex-1">\s*'
            rf'<div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0\.5">\s*'
            rf'{icon}\s*'
            rf'</div>\s*'
            rf'<div class="min-w-0 flex-1">\s*'
            rf'<h4 class="font-semibold text-sm text-black dark:text-white leading-tight">{re.escape(title)}</h4>\s*'
            rf'<div class="text-\[11px\] text-neutral-500 font-mono mt-1 truncate"[^>]*>[\s\S]*?{re.escape(agent_id)}\s*</div>\s*'
            rf'</div>\s*'
            rf'</div>\s*'
            rf'<span class="agent-status-badge shrink-0 px-2 py-0\.5 rounded-full text-\[10px\] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="{re.escape(status_key)}">{status_text}</span>'
        )

        replacement = (
            f'<div class="flex items-center space-x-2.5 min-w-0 flex-1">\n'
            f'                <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white border border-neutral-200/80 dark:border-neutral-700/80 flex items-center justify-center font-bold text-xs shrink-0">\n'
            f'                  {icon}\n'
            f'                </div>\n'
            f'                <div class="min-w-0 flex-1">\n'
            f'                  <h4 class="font-semibold text-xs sm:text-sm text-black dark:text-white leading-tight truncate" title="{title}">{title}</h4>\n'
            f'                  <div class="text-[10px] text-neutral-400 font-mono truncate mt-0.5" title="ID: {agent_id}">ID: {agent_id}</div>\n'
            f'                </div>\n'
            f'              </div>\n'
            f'              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-200 dark:border-neutral-800" data-i18n="{status_key}">{status_text}</span>'
        )

        c, count = pattern.subn(replacement, c)
        print(f"Card {icon}: replaced {count} in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

update_cards('dashboard.html')
update_cards('app/dashboard.html')
