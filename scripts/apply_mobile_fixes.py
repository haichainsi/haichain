import sys

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Marketplace Header Title & Badge
    target_header = '''          <!-- Header & Telemetry Badges -->
          <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-3">
            <div>
              <div class="flex items-center space-x-2">
                <h3 class="font-bold text-base text-black dark:text-white flex items-center space-x-2">
                  <i data-lucide="globe" class="w-4 h-4 text-black dark:text-white"></i>
                  <span data-i18n="marketplace.title">Global Agent Federation Mesh</span>
                </h3>
                <span class="text-[10px] font-mono px-2 py-0.5 rounded-full bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700" data-i18n="marketplace.badge">Solana L1 Escrow Mesh</span>
              </div>
              <p class="text-xs text-neutral-500 mt-1" data-i18n="marketplace.subtitle">Universal decentralized execution mesh interconnecting Smithery MCP, Fetch.ai Almanac, and Glama. Enables autonomous AI agents to discover, negotiate, and hire specialized sub-agents with cryptographically verified micro-escrows.</p>
            </div>'''

    replacement_header = '''          <!-- Header & Telemetry Badges -->
          <div class="flex flex-col lg:flex-row lg:items-start justify-between gap-3">
            <div class="space-y-1.5 min-w-0">
              <div class="flex flex-wrap items-center gap-2">
                <div class="flex items-start space-x-2 min-w-0">
                  <i data-lucide="globe" class="w-4 h-4 text-black dark:text-white shrink-0 mt-0.5"></i>
                  <h3 class="font-bold text-sm sm:text-base text-black dark:text-white leading-snug" data-i18n="marketplace.title">Global Agent Federation Mesh</h3>
                </div>
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[10px] font-mono whitespace-nowrap bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 shrink-0" data-i18n="marketplace.badge">Solana L1 Escrow Mesh</span>
              </div>
              <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="marketplace.subtitle">Universal decentralized execution mesh interconnecting Smithery MCP, Fetch.ai Almanac, and Glama. Enables autonomous AI agents to discover, negotiate, and hire specialized sub-agents with cryptographically verified micro-escrows.</p>
            </div>'''

    if target_header not in content:
        print(f"Error: target_header not found in {filepath}")
        return False
    content = content.replace(target_header, replacement_header, 1)

    # 2. Marketplace Search Bar & Action Buttons
    target_search_row = '''          <!-- Interactive Search & Action Bar + Category Filter Bar -->
          <div class="space-y-3">
            <!-- Row 1: Search Input & Action Buttons (Desktop: 1 Row, Mobile: Stacked) -->
            <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-2.5">
              <div class="relative flex-1 min-w-[220px]">
                <i data-lucide="search" class="w-4 h-4 text-neutral-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none"></i>
                <input id="agent-market-search-input" type="text" data-i18n-placeholder="marketplace.searchPlaceholder" placeholder="Search by skill, capability or keyword (e.g. scraping, security audit, market alpha)..." 
                       class="w-full pl-10 pr-4 py-2.5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/50 text-xs text-black dark:text-white placeholder-neutral-400 focus:outline-none focus:border-black dark:focus:border-white transition-all shadow-2xs">
              </div>

              <!-- Action Buttons: Fast Sync Global Mesh & Monetize SDK Guide -->
              <div class="flex items-center gap-2 shrink-0">
                <button id="sync-global-registries-btn" onclick="window.syncGlobalRegistries?.();" class="flex-1 sm:flex-none px-4 py-2.5 rounded-xl text-xs font-semibold bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 border border-black dark:border-white shrink-0 transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1.5 shadow-xs whitespace-nowrap" title="Sync live mesh nodes from Smithery, Fetch.ai and Glama">
                  <i data-lucide="refresh-cw" class="w-3.5 h-3.5 inline"></i>
                  <span data-i18n="marketplace.syncRegistriesShort">Sync Global Registries</span>
                </button>
                <button onclick="switchTab('tab-docs');" class="flex-1 sm:flex-none px-3.5 py-2.5 rounded-xl text-xs font-semibold bg-neutral-100 hover:bg-neutral-200 text-neutral-800 dark:bg-neutral-900 dark:hover:bg-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 shrink-0 transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1.5 shadow-xs whitespace-nowrap" title="Monetize your agent with Haichain HTTP 402 Paywall">
                  <i data-lucide="code" class="w-3.5 h-3.5 inline"></i>
                  <span data-i18n="marketplace.devDocsBtn">Monetize Agent (SDK)</span>
                </button>
              </div>
            </div>

            <!-- Row 2: Category Filter Pills (Horizontal Scroll with NO Native Scrollbar) -->
            <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-0.5 -mx-1 px-1" id="market-category-filters">'''

    replacement_search_row = '''          <!-- Interactive Search & Action Bar + Category Filter Bar -->
          <div class="space-y-2.5">
            <!-- Row 1: Search Input & Action Buttons (Desktop: 1 Row, Mobile: Stacked with 50/50 Grid Buttons) -->
            <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-2">
              <div class="relative flex-1 min-w-0">
                <i data-lucide="search" class="w-4 h-4 text-neutral-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none"></i>
                <input id="agent-market-search-input" type="text" data-i18n-placeholder="marketplace.searchPlaceholder" placeholder="Search by skill, capability or keyword (e.g. scraping, security audit, market alpha)..." 
                       class="w-full pl-10 pr-4 py-2.5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/50 text-xs text-black dark:text-white placeholder-neutral-400 focus:outline-none focus:border-black dark:focus:border-white transition-all shadow-2xs">
              </div>

              <!-- Action Buttons: 2 equal-width columns on mobile, auto-width on desktop -->
              <div class="grid grid-cols-2 gap-2 w-full sm:w-auto sm:flex sm:items-center sm:gap-2 shrink-0">
                <button id="sync-global-registries-btn" onclick="window.syncGlobalRegistries?.();" class="w-full sm:w-auto px-2.5 sm:px-4 py-2 sm:py-2.5 rounded-xl text-[11px] sm:text-xs font-semibold bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 border border-black dark:border-white transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1 sm:space-x-1.5 shadow-xs" title="Sync live mesh nodes from Smithery, Fetch.ai and Glama">
                  <i data-lucide="refresh-cw" class="w-3.5 h-3.5 shrink-0"></i>
                  <span class="truncate" data-i18n="marketplace.syncRegistriesShort">Sync Global Registries</span>
                </button>
                <button onclick="switchTab('tab-docs');" class="w-full sm:w-auto px-2.5 sm:px-4 py-2 sm:py-2.5 rounded-xl text-[11px] sm:text-xs font-semibold bg-neutral-100 hover:bg-neutral-200 text-neutral-800 dark:bg-neutral-900 dark:hover:bg-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 transition-all active:scale-98 cursor-pointer flex items-center justify-center space-x-1 sm:space-x-1.5 shadow-xs" title="Monetize your agent with Haichain HTTP 402 Paywall">
                  <i data-lucide="code" class="w-3.5 h-3.5 shrink-0"></i>
                  <span class="truncate" data-i18n="marketplace.devDocsBtn">Monetize Agent (SDK)</span>
                </button>
              </div>
            </div>

            <!-- Row 2: Category Filter Pills (Horizontal Scroll with NO Native Scrollbar) -->
            <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-0.5 -mx-1 px-1 touch-pan-x" id="market-category-filters">'''

    if target_search_row not in content:
        print(f"Error: target_search_row not found in {filepath}")
        return False
    content = content.replace(target_search_row, replacement_search_row, 1)

    # 3. Hire Agent Modal Header
    target_modal_header = '''            <div class="flex items-center justify-between border-b border-neutral-100 dark:border-neutral-900 pb-3">
              <div class="flex items-center space-x-2.5">
                <div class="w-8 h-8 rounded-xl bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-xs">
                  <i data-lucide="zap" class="w-4 h-4"></i>
                </div>
                <div>
                  <h4 id="hire-modal-agent-name" class="font-bold text-sm text-black dark:text-white" data-i18n="marketplace.hireModalTitle">Hire Global Sub-Agent</h4>
                  <span id="hire-modal-agent-provider" class="text-[11px] text-neutral-400 font-mono">Smithery MCP Registry</span>
                </div>
              </div>
              <button id="close-hire-agent-modal" class="p-1.5 rounded-lg text-neutral-400 hover:text-black dark:hover:text-white transition-colors cursor-pointer">
                <i data-lucide="x" class="w-4 h-4"></i>
              </button>
            </div>'''

    replacement_modal_header = '''            <div class="flex items-start justify-between gap-3 border-b border-neutral-100 dark:border-neutral-900 pb-3">
              <div class="flex items-start space-x-3 min-w-0 flex-1">
                <div class="w-9 h-9 rounded-xl bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
                  <i data-lucide="zap" class="w-4 h-4"></i>
                </div>
                <div class="min-w-0 flex-1">
                  <h4 id="hire-modal-agent-name" class="font-bold text-sm sm:text-base text-black dark:text-white leading-snug break-words" data-i18n="marketplace.hireModalTitle">Hire Global Sub-Agent</h4>
                  <div id="hire-modal-agent-provider" class="text-[11px] text-neutral-500 font-mono mt-0.5 break-all">Smithery MCP Registry</div>
                </div>
              </div>
              <button id="close-hire-agent-modal" class="p-1.5 -mr-1 -mt-1 rounded-xl text-neutral-400 hover:text-black dark:hover:text-white transition-colors cursor-pointer shrink-0">
                <i data-lucide="x" class="w-4 h-4"></i>
              </button>
            </div>'''

    if target_modal_header not in content:
        print(f"Error: target_modal_header not found in {filepath}")
        return False
    content = content.replace(target_modal_header, replacement_modal_header, 1)

    # 4. Static Agent Cards 1-4
    target_card_1 = '''          <!-- Agent 1 -->
          <div class="agent-card p-5 rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm space-y-3">
            <div class="flex justify-between items-start">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center font-bold text-xs">
                  C3
                </div>
                <div>
                  <h4 class="font-semibold text-sm text-black dark:text-white">Claude Desktop (MCP Worker)</h4>
                  <span class="text-[11px] text-neutral-500 font-mono">ID: agent_claude_desktop_01</span>
                </div>
              </div>
              <span class="agent-status-badge px-2 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent.status.active">Active</span>
            </div>'''

    replacement_card_1 = '''          <!-- Agent 1 -->
          <div class="agent-card p-5 rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-2.5">
              <div class="flex items-start space-x-3 min-w-0 flex-1">
                <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
                  C3
                </div>
                <div class="min-w-0 flex-1">
                  <h4 class="font-semibold text-sm text-black dark:text-white leading-tight">Claude Desktop (MCP Worker)</h4>
                  <div class="text-[11px] text-neutral-500 font-mono mt-1 truncate" title="ID: agent_claude_desktop_01">
                    <span class="text-neutral-400">ID:</span> agent_claude_desktop_01
                  </div>
                </div>
              </div>
              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-full text-[10px] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent.status.active">Active</span>
            </div>'''

    if target_card_1 not in content:
        print(f"Error: target_card_1 not found in {filepath}")
        return False
    content = content.replace(target_card_1, replacement_card_1, 1)

    target_card_2 = '''          <!-- Agent 2 -->
          <div class="agent-card p-5 rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm space-y-3">
            <div class="flex justify-between items-start">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center font-bold text-xs">
                  CR
                </div>
                <div>
                  <h4 class="font-semibold text-sm text-black dark:text-white">Cursor Composer Agent</h4>
                  <span class="text-[11px] text-neutral-500 font-mono">ID: agent_cursor_ide_02</span>
                </div>
              </div>
              <span class="agent-status-badge px-2 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent.status.active">Active</span>
            </div>'''

    replacement_card_2 = '''          <!-- Agent 2 -->
          <div class="agent-card p-5 rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-2.5">
              <div class="flex items-start space-x-3 min-w-0 flex-1">
                <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
                  CR
                </div>
                <div class="min-w-0 flex-1">
                  <h4 class="font-semibold text-sm text-black dark:text-white leading-tight">Cursor Composer Agent</h4>
                  <div class="text-[11px] text-neutral-500 font-mono mt-1 truncate" title="ID: agent_cursor_ide_02">
                    <span class="text-neutral-400">ID:</span> agent_cursor_ide_02
                  </div>
                </div>
              </div>
              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-full text-[10px] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent.status.active">Active</span>
            </div>'''

    if target_card_2 not in content:
        print(f"Error: target_card_2 not found in {filepath}")
        return False
    content = content.replace(target_card_2, replacement_card_2, 1)

    target_card_3 = '''          <!-- Agent 3 -->
          <div class="agent-card p-5 rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm space-y-3">
            <div class="flex justify-between items-start">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center font-bold text-xs">
                  SR
                </div>
                <div>
                  <h4 class="font-semibold text-sm text-black dark:text-white">Web SERP Scraper Swarm</h4>
                  <span class="text-[11px] text-neutral-500 font-mono">ID: agent_serp_crawler_03</span>
                </div>
              </div>
              <span class="agent-status-badge px-2 py-0.5 rounded-full text-[10px] font-mono bg-neutral-200 text-neutral-800 dark:bg-neutral-800 dark:text-neutral-300" data-i18n="agent.status.idle">Idle</span>
            </div>'''

    replacement_card_3 = '''          <!-- Agent 3 -->
          <div class="agent-card p-5 rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-2.5">
              <div class="flex items-start space-x-3 min-w-0 flex-1">
                <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
                  SR
                </div>
                <div class="min-w-0 flex-1">
                  <h4 class="font-semibold text-sm text-black dark:text-white leading-tight">Web SERP Scraper Swarm</h4>
                  <div class="text-[11px] text-neutral-500 font-mono mt-1 truncate" title="ID: agent_serp_crawler_03">
                    <span class="text-neutral-400">ID:</span> agent_serp_crawler_03
                  </div>
                </div>
              </div>
              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-full text-[10px] font-mono whitespace-nowrap bg-neutral-200 text-neutral-800 dark:bg-neutral-800 dark:text-neutral-300 border border-neutral-300 dark:border-neutral-700" data-i18n="agent.status.idle">Idle</span>
            </div>'''

    if target_card_3 not in content:
        print(f"Error: target_card_3 not found in {filepath}")
        return False
    content = content.replace(target_card_3, replacement_card_3, 1)

    target_card_4 = '''          <!-- Agent 4 -->
          <div class="agent-card p-5 rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm space-y-3">
            <div class="flex justify-between items-start">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center font-bold text-xs">
                  TX
                </div>
                <div>
                  <h4 class="font-semibold text-sm text-black dark:text-white">Tesla Optimus #12 Kinematics</h4>
                  <span class="text-[11px] text-neutral-500 font-mono">ID: edge_robot_sensor_04</span>
                </div>
              </div>
              <span class="agent-status-badge px-2 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent.status.streaming">Streaming</span>
            </div>'''

    replacement_card_4 = '''          <!-- Agent 4 -->
          <div class="agent-card p-5 rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-white dark:bg-brand-card shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-2.5">
              <div class="flex items-start space-x-3 min-w-0 flex-1">
                <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
                  TX
                </div>
                <div class="min-w-0 flex-1">
                  <h4 class="font-semibold text-sm text-black dark:text-white leading-tight">Tesla Optimus #12 Kinematics</h4>
                  <div class="text-[11px] text-neutral-500 font-mono mt-1 truncate" title="ID: edge_robot_sensor_04">
                    <span class="text-neutral-400">ID:</span> edge_robot_sensor_04
                  </div>
                </div>
              </div>
              <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-full text-[10px] font-mono whitespace-nowrap bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="agent.status.streaming">Streaming</span>
            </div>'''

    if target_card_4 not in content:
        print(f"Error: target_card_4 not found in {filepath}")
        return False
    content = content.replace(target_card_4, replacement_card_4, 1)

    # 5. Dynamic Agent Card Template 1 (issueTicketModal)
    target_dyn_1 = '''        <div class="flex justify-between items-start">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center font-bold text-xs">
              ${initials}
            </div>
            <div>
              <h4 class="font-semibold text-sm text-black dark:text-white">${agentName}</h4>
              <span class="text-[11px] text-neutral-500 font-mono">ID: ${agentId}</span>
            </div>
          </div>
          <span class="agent-status-badge px-2 py-0.5 rounded-full text-[10px] font-mono bg-black text-white dark:bg-white dark:text-black border border-black dark:border-white font-bold" data-i18n="agent.status.active">Active</span>
        </div>'''

    replacement_dyn_1 = '''        <div class="flex items-start justify-between gap-2.5">
          <div class="flex items-start space-x-3 min-w-0 flex-1">
            <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
              ${initials}
            </div>
            <div class="min-w-0 flex-1">
              <h4 class="font-semibold text-sm text-black dark:text-white leading-tight">${agentName}</h4>
              <div class="text-[11px] text-neutral-500 font-mono mt-1 truncate" title="ID: ${agentId}">
                <span class="text-neutral-400">ID:</span> ${agentId}
              </div>
            </div>
          </div>
          <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-full text-[10px] font-mono whitespace-nowrap bg-black text-white dark:bg-white dark:text-black border border-black dark:border-white font-bold" data-i18n="agent.status.active">Active</span>
        </div>'''

    if target_dyn_1 not in content:
        print(f"Error: target_dyn_1 not found in {filepath}")
        return False
    content = content.replace(target_dyn_1, replacement_dyn_1, 1)

    # 6. Dynamic Agent Card Template 2 (ensureAgentCard)
    target_dyn_2 = '''        <div class="flex justify-between items-start">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs">
              ${initials}
            </div>
            <div>
              <h4 class="font-semibold text-sm text-black dark:text-white">${provider} Worker</h4>
              <span class="text-[11px] text-neutral-500 font-mono">${note || 'Active'}</span>
            </div>
          </div>
          <span class="agent-status-badge px-2 py-0.5 rounded-full text-[10px] font-mono bg-black text-white dark:bg-white dark:text-black border border-black dark:border-white font-bold">${statusType}</span>
        </div>'''

    replacement_dyn_2 = '''        <div class="flex items-start justify-between gap-2.5">
          <div class="flex items-start space-x-3 min-w-0 flex-1">
            <div class="w-10 h-10 rounded-2xl bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
              ${initials}
            </div>
            <div class="min-w-0 flex-1">
              <h4 class="font-semibold text-sm text-black dark:text-white leading-tight">${provider} Worker</h4>
              <div class="text-[11px] text-neutral-500 font-mono mt-1 truncate">
                ${note || 'Active'}
              </div>
            </div>
          </div>
          <span class="agent-status-badge shrink-0 px-2 py-0.5 rounded-full text-[10px] font-mono whitespace-nowrap bg-black text-white dark:bg-white dark:text-black border border-black dark:border-white font-bold">${statusType}</span>
        </div>'''

    if target_dyn_2 not in content:
        print(f"Error: target_dyn_2 not found in {filepath}")
        return False
    content = content.replace(target_dyn_2, replacement_dyn_2, 1)

    # Bump cache buster for dialog / dashboard
    content = content.replace('i18n.js?v=v59_fix_language_and_escrow_prompts', 'i18n.js?v=v60_mobile_round_fixes_all_cards')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully patched {filepath}")
    return True

ok1 = patch_file('dashboard.html')
ok2 = patch_file('app/dashboard.html')
if not (ok1 and ok2):
    sys.exit(1)
