const fs = require('fs');

const NEW_SECTION_ONLINE = `      <!-- ================= TAB 2: CLOUD MCP GATEWAY (INFRASTRUCTURE IN PROGRESS) ================= -->
      <div id="hub-section-online" class="hidden space-y-3 font-mono text-xs">
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="text-black dark:text-white font-sans font-bold text-xs flex items-center space-x-1.5">
              <i data-lucide="cloud" class="w-3.5 h-3.5 text-amber-500"></i>
              <span data-i18n="aiHub.onlineTitle">Cloud MCP Gateway (Claude Mobile)</span>
            </span>
            <span class="text-[9.5px] px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20 font-mono uppercase tracking-wider font-semibold" data-i18n="aiHub.onlineBadge">Under Deployment</span>
          </div>
          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.onlineDesc">
            Direct remote integration for Claude Mobile requires a dedicated 24/7 Cloud Gateway server. For immediate verified testing, choose one of the two active options below:
          </p>
        </div>

        <!-- Infrastructure Status Card & Immediate Action -->
        <div class="p-3.5 sm:p-4 rounded-2xl bg-neutral-100/60 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-3 font-sans">
          <div class="flex items-start space-x-2.5 text-xs text-neutral-700 dark:text-neutral-300">
            <div class="w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse mt-1 shrink-0"></div>
            <div class="space-y-1 flex-1">
              <div class="font-bold text-black dark:text-white text-xs sm:text-[13px]" data-i18n="aiHub.onlineNoticeTitle">24/7 Cloud Gateway Server Under Deployment</div>
              <p class="text-[11px] text-neutral-500 dark:text-neutral-400 leading-relaxed" data-i18n="aiHub.onlineNoticeText">
                The site is currently hosted on a Static CDN, so remote requests return 404. We recommend using AI Playground directly on mobile or Claude Desktop on PC.
              </p>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
            <button type="button" id="online-switch-playground-btn" class="py-2.5 px-3 rounded-xl bg-black text-white dark:bg-white dark:text-black font-bold text-xs flex items-center justify-center space-x-1.5 hover:opacity-90 active:scale-98 transition-all cursor-pointer shadow-sm">
              <i data-lucide="zap" class="w-3.5 h-3.5"></i>
              <span data-i18n="aiHub.onlinePlaygroundBtn">⚡ Open AI Playground (Mobile)</span>
            </button>
            <button type="button" id="online-switch-desktop-btn" class="py-2.5 px-3 rounded-xl bg-neutral-200/80 dark:bg-neutral-800 text-black dark:text-white font-semibold text-xs border border-neutral-300 dark:border-neutral-700 flex items-center justify-center space-x-1.5 hover:bg-neutral-300 dark:hover:bg-neutral-700 active:scale-98 transition-all cursor-pointer">
              <i data-lucide="terminal" class="w-3.5 h-3.5"></i>
              <span data-i18n="aiHub.onlineDesktopBtn">💻 Claude Desktop (PC/Mac)</span>
            </button>
          </div>
        </div>

        <!-- On-Chain Ready Tools Card -->
        <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200 dark:border-neutral-800 text-[11px] text-neutral-600 dark:text-neutral-300 space-y-1.5 font-sans">
          <div class="font-bold text-black dark:text-white flex items-center space-x-1.5 text-xs">
            <i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-500 shrink-0"></i>
            <span data-i18n="aiHub.onlineReadyToolsTitle">4 On-Chain MCP Tools Ready on Kernel:</span>
          </div>
          <div class="space-y-1 font-mono text-[10.5px] text-neutral-500 dark:text-neutral-400 pl-5">
            <div>• <strong class="text-neutral-800 dark:text-neutral-200">get_spending_pot_balance</strong>: On-chain vault balance query</div>
            <div>• <strong class="text-neutral-800 dark:text-neutral-200">execute_micro_payment</strong>: Autonomous sub-cent disbursement</div>
            <div>• <strong class="text-neutral-800 dark:text-neutral-200">trigger_emergency_panic</strong>: Instant 380ms fund recall</div>
            <div>• <strong class="text-neutral-800 dark:text-neutral-200">verify_kernel_status</strong>: Cryptographic capability verification</div>
          </div>
        </div>
      </div>`;

const JS_LISTENERS = `
    const onlineSwitchPlaygroundBtn = document.getElementById('online-switch-playground-btn');
    if (onlineSwitchPlaygroundBtn) {
      onlineSwitchPlaygroundBtn.addEventListener('click', () => {
        switchAiHubTab('web');
      });
    }
    const onlineSwitchDesktopBtn = document.getElementById('online-switch-desktop-btn');
    if (onlineSwitchDesktopBtn) {
      onlineSwitchDesktopBtn.addEventListener('click', () => {
        switchAiHubTab('desktop');
      });
    }
`;

['dashboard.html', 'app/dashboard.html'].forEach(filePath => {
  let content = fs.readFileSync(filePath, 'utf8');

  // Replace hub-section-online
  const startTag = '<div id="hub-section-online"';
  const endTag = '<!-- ================= TAB 3: WEB DASHBOARD DIRECT (INSTANT PLAYGROUND) ================= -->';

  const sIdx = content.indexOf(startTag);
  const eIdx = content.indexOf(endTag);

  if (sIdx !== -1 && eIdx !== -1) {
    // Find the comment preceding startTag if any
    let cutStart = sIdx;
    const commentIdx = content.lastIndexOf('<!-- ================= TAB 2:', sIdx);
    if (commentIdx !== -1 && sIdx - commentIdx < 200) {
      cutStart = commentIdx;
    }
    content = content.slice(0, cutStart) + NEW_SECTION_ONLINE + '\n\n      ' + content.slice(eIdx);
    console.log(`Successfully replaced hub-section-online in ${filePath}`);
  } else {
    console.warn(`Could not find tags in ${filePath}: sIdx=${sIdx}, eIdx=${eIdx}`);
  }

  // Inject switch listeners if not already present
  if (!content.includes('onlineSwitchPlaygroundBtn')) {
    const anchor = "if (hubTabWeb) hubTabWeb.addEventListener('click', () => switchAiHubTab('web'));";
    if (content.includes(anchor)) {
      content = content.replace(anchor, anchor + '\n' + JS_LISTENERS);
      console.log(`Successfully injected switch listeners in ${filePath}`);
    }
  }

  fs.writeFileSync(filePath, content, 'utf8');
});
