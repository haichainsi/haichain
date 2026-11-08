const fs = require('fs');

['dashboard.html', 'app/dashboard.html'].forEach(filePath => {
  let content = fs.readFileSync(filePath, 'utf8');

  // Replace mobile button
  const mobileRegex = /<!-- Tab 6: MCP -->\s*<button class="mobile-tab-btn[^>]*data-tab="tab-mcp"[\s\S]*?<\/button>/;
  const newMobileBtn = `<!-- Tab 6: Dev & MCP Hub -->
      <button class="mobile-tab-btn flex-1 py-1 flex flex-col items-center justify-center transition-all active:opacity-70 group cursor-pointer" data-tab="tab-docs">
        <div class="tab-icon-wrapper w-10 h-7 flex items-center justify-center rounded-xl text-neutral-400 dark:text-neutral-500 transition-all relative">
          <i data-lucide="terminal" class="w-4 h-4"></i>
          <span class="tab-indicator opacity-0 scale-0 absolute -bottom-1 left-1/2 -translate-x-1/2 w-4 h-0.5 rounded-full bg-black dark:bg-white transition-all duration-300"></span>
        </div>
        <span class="mobile-tab-label mt-0.5 text-[10px] font-sans font-medium tracking-tight text-neutral-400 dark:text-neutral-500 whitespace-nowrap truncate max-w-[68px]" data-i18n="nav.devHubShort">Dev & MCP</span>
      </button>`;

  if (mobileRegex.test(content)) {
    content = content.replace(mobileRegex, newMobileBtn);
    console.log(`[OK] Updated mobile bottom bar in ${filePath}`);
    fs.writeFileSync(filePath, content, 'utf8');
  } else {
    console.warn(`[WARN] Mobile regex not matched in ${filePath}`);
  }
});
