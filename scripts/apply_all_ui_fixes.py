import re

def update_dashboard(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Agent Cards Headers (Claude, Cursor, SERP, Tesla)
    # Card 1: Claude Desktop (C3)
    c3_old = r'''<div class="flex items-start justify-between gap-2\.5">\s*<div class="flex items-start space-x-3 min-w-0 flex-1">\s*<div class="w-8 h-8 rounded-full bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0\.5">\s*C3\s*</div>\s*<div class="min-w-0 flex-1">\s*<h4 class="font-semibold text-sm text-black dark:text-white leading-tight">Claude Desktop \(MCP Worker\)</h4>\s*<div class="text-\[11px\] text-neutral-500 font-mono mt-1 truncate" title="ID: agent_claude_desktop_01">\s*<span class="text-neutral-400">ID:</span> agent_claude_desktop_01\s*</div>\s*</div>\s*</div>\s*<span class="agent-status-badge shrink-0 px-2 py-0\.5 rounded-full text-\[10px\] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent\.status\.active">Active</span>\s*</div>'''
    
    c3_new = '''<div class="flex items-start justify-between gap-2">
              <div class="flex items-center space-x-2.5 min-w-0 flex-1">
                <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white border border-neutral-200/80 dark:border-neutral-700/80 flex items-center justify-center font-bold text-xs shrink-0">
                  C3
                </div>
                <div class="min-w-0 flex-1">
                  <h4 class="font-bold text-xs sm:text-sm text-black dark:text-white leading-snug truncate" title="Claude Desktop (MCP Worker)">Claude Desktop (MCP Worker)</h4>
                  <div class="text-[10px] text-neutral-400 font-mono truncate" title="agent_claude_desktop_01">
                    agent_claude_desktop_01
                  </div>
                </div>
              </div>
              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-200 dark:border-neutral-800" data-i18n="agent.status.active">Active</span>
            </div>'''
    
    content, count_c3 = re.subn(c3_old, c3_new, content)
    print(f"Replaced C3 header: {count_c3} times in {filepath}")

    # Card 2: Cursor Composer (CR)
    cr_old = r'''<div class="flex items-start justify-between gap-2\.5">\s*<div class="flex items-start space-x-3 min-w-0 flex-1">\s*<div class="w-8 h-8 rounded-full bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0\.5">\s*CR\s*</div>\s*<div class="min-w-0 flex-1">\s*<h4 class="font-semibold text-sm text-black dark:text-white leading-tight">Cursor Composer Agent</h4>\s*<div class="text-\[11px\] text-neutral-500 font-mono mt-1 truncate" title="ID: agent_cursor_ide_02">\s*<span class="text-neutral-400">ID:</span> agent_cursor_ide_02\s*</div>\s*</div>\s*</div>\s*<span class="agent-status-badge shrink-0 px-2 py-0\.5 rounded-full text-\[10px\] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent\.status\.active">Active</span>\s*</div>'''
    
    cr_new = '''<div class="flex items-start justify-between gap-2">
              <div class="flex items-center space-x-2.5 min-w-0 flex-1">
                <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white border border-neutral-200/80 dark:border-neutral-700/80 flex items-center justify-center font-bold text-xs shrink-0">
                  CR
                </div>
                <div class="min-w-0 flex-1">
                  <h4 class="font-bold text-xs sm:text-sm text-black dark:text-white leading-snug truncate" title="Cursor Composer Agent">Cursor Composer Agent</h4>
                  <div class="text-[10px] text-neutral-400 font-mono truncate" title="agent_cursor_ide_02">
                    agent_cursor_ide_02
                  </div>
                </div>
              </div>
              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-200 dark:border-neutral-800" data-i18n="agent.status.active">Active</span>
            </div>'''

    content, count_cr = re.subn(cr_old, cr_new, content)
    print(f"Replaced CR header: {count_cr} times in {filepath}")

    # Card 3: Web SERP Scraper (SR)
    sr_old = r'''<div class="flex items-start justify-between gap-2\.5">\s*<div class="flex items-start space-x-3 min-w-0 flex-1">\s*<div class="w-8 h-8 rounded-full bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0\.5">\s*SR\s*</div>\s*<div class="min-w-0 flex-1">\s*<h4 class="font-semibold text-sm text-black dark:text-white leading-tight">Web SERP Scraper Swarm</h4>\s*<div class="text-\[11px\] text-neutral-500 font-mono mt-1 truncate" title="ID: agent_serp_crawler_03">\s*<span class="text-neutral-400">ID:</span> agent_serp_crawler_03\s*</div>\s*</div>\s*</div>\s*<span class="agent-status-badge shrink-0 px-2 py-0\.5 rounded-full text-\[10px\] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent\.status\.idle">Idle</span>\s*</div>'''

    sr_new = '''<div class="flex items-start justify-between gap-2">
              <div class="flex items-center space-x-2.5 min-w-0 flex-1">
                <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white border border-neutral-200/80 dark:border-neutral-700/80 flex items-center justify-center font-bold text-xs shrink-0">
                  SR
                </div>
                <div class="min-w-0 flex-1">
                  <h4 class="font-bold text-xs sm:text-sm text-black dark:text-white leading-snug truncate" title="Web SERP Scraper Swarm">Web SERP Scraper Swarm</h4>
                  <div class="text-[10px] text-neutral-400 font-mono truncate" title="agent_serp_crawler_03">
                    agent_serp_crawler_03
                  </div>
                </div>
              </div>
              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-200 dark:border-neutral-800" data-i18n="agent.status.idle">Idle</span>
            </div>'''

    content, count_sr = re.subn(sr_old, sr_new, content)
    print(f"Replaced SR header: {count_sr} times in {filepath}")

    # Card 4: Tesla Optimus (TX)
    tx_old = r'''<div class="flex items-start justify-between gap-2\.5">\s*<div class="flex items-start space-x-3 min-w-0 flex-1">\s*<div class="w-8 h-8 rounded-full bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0\.5">\s*TX\s*</div>\s*<div class="min-w-0 flex-1">\s*<h4 class="font-semibold text-sm text-black dark:text-white leading-tight">Tesla Optimus #12 Kinematics</h4>\s*<div class="text-\[11px\] text-neutral-500 font-mono mt-1 truncate" title="ID: edge_robot_sensor_04">\s*<span class="text-neutral-400">ID:</span> edge_robot_sensor_04\s*</div>\s*</div>\s*</div>\s*<span class="agent-status-badge shrink-0 px-2 py-0\.5 rounded-full text-\[10px\] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent\.status\.streaming">Streaming</span>\s*</div>'''

    tx_new = '''<div class="flex items-start justify-between gap-2">
              <div class="flex items-center space-x-2.5 min-w-0 flex-1">
                <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white border border-neutral-200/80 dark:border-neutral-700/80 flex items-center justify-center font-bold text-xs shrink-0">
                  TX
                </div>
                <div class="min-w-0 flex-1">
                  <h4 class="font-bold text-xs sm:text-sm text-black dark:text-white leading-snug truncate" title="Tesla Optimus #12 Kinematics">Tesla Optimus #12 Kinematics</h4>
                  <div class="text-[10px] text-neutral-400 font-mono truncate" title="edge_robot_sensor_04">
                    edge_robot_sensor_04
                  </div>
                </div>
              </div>
              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-200 dark:border-neutral-800" data-i18n="agent.status.streaming">Streaming</span>
            </div>'''

    content, count_tx = re.subn(tx_old, tx_new, content)
    print(f"Replaced TX header: {count_tx} times in {filepath}")

    # 2. Update Global Agent Federation Mesh Header & Badge
    mesh_header_old = r'''<div class="flex flex-col lg:flex-row lg:items-start justify-between gap-3">\s*<div class="space-y-1\.5 min-w-0">\s*<div class="flex flex-wrap items-center gap-2">\s*<div class="flex items-start space-x-2 min-w-0">\s*<i data-lucide="globe" class="w-4 h-4 text-black dark:text-white shrink-0 mt-0\.5"></i>\s*<h3 class="font-bold text-sm sm:text-base text-black dark:text-white leading-snug" data-i18n="marketplace\.title">Global Agent Federation Mesh</h3>\s*</div>\s*<span class="inline-flex items-center px-2\.5 py-0\.5 rounded-full text-\[10px\] font-mono whitespace-nowrap bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 shrink-0" data-i18n="marketplace\.badge">Solana L1 Escrow Mesh</span>\s*</div>'''

    mesh_header_new = '''<div class="flex flex-col lg:flex-row lg:items-start justify-between gap-3">
            <div class="space-y-1.5 min-w-0">
              <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1.5 sm:gap-2">
                <div class="flex items-center space-x-2 min-w-0">
                  <i data-lucide="globe" class="w-4 h-4 text-black dark:text-white shrink-0"></i>
                  <h3 class="font-bold text-sm sm:text-base text-black dark:text-white leading-snug truncate" data-i18n="marketplace.title">Global Agent Federation Mesh</h3>
                </div>
                <span class="inline-flex items-center self-start sm:self-auto px-2 py-0.5 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-200 dark:border-neutral-800 shrink-0" data-i18n="marketplace.badge">Solana L1 Escrow Mesh</span>
              </div>'''

    content, count_mesh = re.subn(mesh_header_old, mesh_header_new, content)
    print(f"Replaced mesh header: {count_mesh} times in {filepath}")

    # 3. Update Hire Agent Modal Header & Settlement Escrow color
    hire_modal_old = r'''<div class="flex items-start justify-between gap-3 pb-3 border-b border-neutral-100 dark:border-neutral-900">\s*<div class="flex items-center space-x-3 min-w-0">\s*<div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 flex items-center justify-center shrink-0">\s*<i data-lucide="zap" class="w-5 h-5 text-black dark:text-white"></i>\s*</div>\s*<div class="min-w-0 flex-1">\s*<h4 id="hire-modal-agent-name" class="font-bold text-sm sm:text-base text-black dark:text-white leading-snug break-words" data-i18n="marketplace\.hireModalTitle">Hire Global Sub-Agent</h4>\s*<div id="hire-modal-agent-provider" class="text-\[11px\] text-neutral-500 font-mono mt-0\.5 break-all">Smithery MCP Registry</div>\s*</div>\s*</div>\s*<button id="close-hire-agent-modal"'''

    hire_modal_new = '''<div class="flex items-start justify-between gap-3 pb-3 border-b border-neutral-100 dark:border-neutral-900">
              <div class="flex items-start space-x-2.5 min-w-0 flex-1">
                <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 flex items-center justify-center shrink-0 mt-0.5">
                  <i data-lucide="zap" class="w-4 h-4 text-black dark:text-white"></i>
                </div>
                <div class="min-w-0 flex-1">
                  <h4 id="hire-modal-agent-name" class="font-bold text-sm sm:text-base text-black dark:text-white leading-snug break-words" data-i18n="marketplace.hireModalTitle">Hire Global Sub-Agent</h4>
                  <div id="hire-modal-agent-provider" class="text-[11px] text-neutral-500 font-mono mt-0.5 break-all">Smithery MCP Registry</div>
                </div>
              </div>
              <button id="close-hire-agent-modal"'''

    content, count_hire = re.subn(hire_modal_old, hire_modal_new, content)
    print(f"Replaced hire modal header: {count_hire} times in {filepath}")

    # Settlement Escrow green text to monochrome
    content = content.replace(
      '<span class="font-bold text-emerald-500">Solana Devnet L1</span>',
      '<span class="font-bold text-black dark:text-white font-mono">Solana Devnet L1</span>'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {filepath}")

update_dashboard('dashboard.html')
update_dashboard('app/dashboard.html')
