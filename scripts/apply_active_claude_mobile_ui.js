const fs = require('fs');

const ACTIVE_HUB_SECTION_ONLINE = `      <!-- ================= TAB 2: CLAUDE MOBILE MCP GATEWAY (24/7 ACTIVE) ================= -->
      <div id="hub-section-online" class="hidden space-y-3 font-mono text-xs">
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="text-black dark:text-white font-sans font-bold text-xs flex items-center space-x-1.5">
              <i data-lucide="smartphone" class="w-3.5 h-3.5 text-neutral-700 dark:text-neutral-300"></i>
              <span data-i18n="aiHub.onlineTitle">Claude Mobile MCP Gateway</span>
            </span>
            <span class="text-[9.5px] px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 font-mono uppercase tracking-wider font-semibold" data-i18n="aiHub.onlineBadge">ONLINE (24/7)</span>
          </div>
          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.onlineDesc">
            Direct 24/7 cloud integration for the Claude app on iOS & Android. Connects directly to the global HAICHAIN Cloud MCP Gateway via Streamable HTTP with zero desktop software required.
          </p>
        </div>

        <!-- Official Server URL Box -->
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-950 border border-neutral-800 space-y-2">
          <div class="flex flex-wrap items-center justify-between gap-1.5 text-[11px] text-neutral-400">
            <span class="flex items-center space-x-1.5 font-sans">
              <i data-lucide="link" class="w-3.5 h-3.5 text-neutral-300 shrink-0"></i>
              <span class="text-neutral-300 font-medium" data-i18n="aiHub.onlineUrlLabel">MCP Server URL (For Claude Mobile):</span>
            </span>
            <span class="text-[9px] bg-emerald-950/80 border border-emerald-800/80 px-2 py-0.5 rounded-full text-emerald-400 font-mono shrink-0 whitespace-nowrap">Streamable HTTP / SSL</span>
          </div>
          <div class="p-2.5 rounded-xl bg-black border border-neutral-800 font-mono text-emerald-400 text-xs sm:text-[13px] overflow-x-auto select-all break-all flex items-center justify-between">
            <code id="online-mcp-url-snippet">https://mcp.haichain.si/api/mcp</code>
          </div>
        </div>

        <button id="copy-online-mcp-btn" type="button" class="w-full py-3 px-4 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-bold text-xs sm:text-sm flex items-center justify-center space-x-2 shadow-sm transition-all active:scale-98 cursor-pointer">
          <i data-lucide="copy" class="w-4 h-4"></i>
          <span id="copy-online-mcp-text" data-i18n="aiHub.onlineCopyBtn">Copy Server URL</span>
        </button>

        <!-- 3 Step Mobile Connection Guide -->
        <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200 dark:border-neutral-800 text-[11px] text-neutral-600 dark:text-neutral-300 space-y-2 font-sans">
          <div class="font-bold text-black dark:text-white flex items-center space-x-1.5 text-xs">
            <i data-lucide="info" class="w-3.5 h-3.5 text-neutral-400 shrink-0"></i>
            <span data-i18n="aiHub.onlineStepsTitle">3 Steps to Connect on Claude Mobile:</span>
          </div>
          <div class="space-y-1.5 text-[10.5px] sm:text-[11px]">
            <div class="flex items-start space-x-2">
              <span class="w-4 h-4 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">1</span>
              <span data-i18n="aiHub.onlineStep1">Open Claude app on phone -> Settings -> Connectors -> Add custom connector.</span>
            </div>
            <div class="flex items-start space-x-2">
              <span class="w-4 h-4 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">2</span>
              <span data-i18n="aiHub.onlineStep2">Set Name to 'HAICHAIN' and paste the Server URL https://mcp.haichain.si/api/mcp into the URL field.</span>
            </div>
            <div class="flex items-start space-x-2">
              <span class="w-4 h-4 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">3</span>
              <span data-i18n="aiHub.onlineStep3">Click Connect -> Select 'No authentication' (or click 'Continue anyway') -> Done!</span>
            </div>
          </div>
        </div>

        <!-- 4 On-Chain Ready Tools Card -->
        <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200 dark:border-neutral-800 text-[11px] text-neutral-600 dark:text-neutral-300 space-y-1.5 font-sans">
          <div class="font-bold text-black dark:text-white flex items-center space-x-1.5 text-xs">
            <i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-500 shrink-0"></i>
            <span data-i18n="aiHub.onlineReadyToolsTitle">4 On-Chain MCP Tools Ready:</span>
          </div>
          <div class="space-y-1 font-mono text-[10px] sm:text-[10.5px] text-neutral-500 dark:text-neutral-400 pl-2 sm:pl-4 break-words">
            <div>• <strong class="text-neutral-800 dark:text-neutral-200">get_spending_pot_balance</strong>: On-chain vault balance query</div>
            <div>• <strong class="text-neutral-800 dark:text-neutral-200">execute_micro_payment</strong>: Autonomous sub-cent disbursement</div>
            <div>• <strong class="text-neutral-800 dark:text-neutral-200">trigger_emergency_panic</strong>: Instant 380ms fund recall</div>
            <div>• <strong class="text-neutral-800 dark:text-neutral-200">verify_kernel_status</strong>: Cryptographic capability verification</div>
          </div>
        </div>
      </div>`;

['dashboard.html', 'app/dashboard.html'].forEach(filePath => {
  let content = fs.readFileSync(filePath, 'utf8');

  // Replace hub-section-online
  const startTag = '<div id="hub-section-online"';
  const endTag = '<!-- ================= TAB 3: WEB DASHBOARD DIRECT (INSTANT PLAYGROUND) ================= -->';

  const sIdx = content.indexOf(startTag);
  const eIdx = content.indexOf(endTag);

  if (sIdx !== -1 && eIdx !== -1) {
    let cutStart = sIdx;
    const commentIdx = content.lastIndexOf('<!-- ================= TAB 2:', sIdx);
    if (commentIdx !== -1 && sIdx - commentIdx < 200) {
      cutStart = commentIdx;
    }
    content = content.slice(0, cutStart) + ACTIVE_HUB_SECTION_ONLINE + '\n\n      ' + content.slice(eIdx);
    console.log(`Replaced hub-section-online in ${filePath}`);
  }

  // Update copy URL target
  content = content.replace(
    'const url = "https://haichain.si/api/mcp";',
    'const url = "https://mcp.haichain.si/api/mcp";'
  );

  fs.writeFileSync(filePath, content, 'utf8');
});
