const fs = require('fs');

function buildMergedDevHubSection() {
  return `<!-- ================= TAB: DEVELOPER & MCP HUB ================= -->
      <section id="tab-docs" class="tab-content hidden space-y-6">
        <!-- Header Banner (Strict Monochrome: Pure Black/White/Neutral) -->
        <div class="p-5 sm:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 shadow-sm space-y-3">
          <div class="space-y-1.5">
            <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded-full bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-200 dark:border-neutral-800 text-[11px] font-mono font-semibold">
              <span data-i18n="dev.badge">Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain</span>
            </div>
            <h2 class="text-xl md:text-2xl font-bold tracking-tight text-black dark:text-white" data-i18n="nav.devHub">
              Developer & MCP Hub
            </h2>
            <p class="text-xs text-neutral-500 dark:text-neutral-400 max-w-2xl leading-relaxed" data-i18n="dev.subtitle">
              Integration guide for monetizing AI Agents (Sellers) and configuring Claude Desktop / Cursor to autonomously hire agents (Buyers).
            </p>
          </div>
        </div>

        <!-- 3-Column Quick Navigation Cards (Monochrome Minimalist) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Card 1: For Developers (Sellers) -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-3">
            <div class="w-8 h-8 rounded-xl bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-200 dark:border-neutral-800 flex items-center justify-center font-bold text-xs">
              01
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.card1Title">1. For Developers (Sellers)</h3>
            <p class="text-[11px] text-neutral-500 dark:text-neutral-400 leading-relaxed" data-i18n="dev.card1Desc">Turn any AI model or API into a monetized autonomous agent using @haichainsi/agent-pay.</p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800" data-i18n="dev.card1Badge">HTTP 402 Paywall</span>
            </div>
          </div>

          <!-- Card 2: For AI Orchestrators (Buyers) -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-3">
            <div class="w-8 h-8 rounded-xl bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-200 dark:border-neutral-800 flex items-center justify-center font-bold text-xs">
              02
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.card2Title">2. Configure Claude & Cursor (Buyers)</h3>
            <p class="text-[11px] text-neutral-500 dark:text-neutral-400 leading-relaxed" data-i18n="dev.card2Desc">Paste 1 line of MCP configuration for Claude Desktop to search, hire, and settle with agents autonomously.</p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800" data-i18n="dev.card2Badge">MCP JSON-RPC</span>
            </div>
          </div>

          <!-- Card 3: Direct REST API & SDK -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-3">
            <div class="w-8 h-8 rounded-xl bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-200 dark:border-neutral-800 flex items-center justify-center font-bold text-xs">
              03
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.card3Title">3. Direct REST API Dispatch</h3>
            <p class="text-[11px] text-neutral-500 dark:text-neutral-400 leading-relaxed" data-i18n="dev.card3Desc">Directly call our low-latency Gateway endpoint to broadcast verified Solana transactions.</p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800" data-i18n="dev.card3Badge">Solana Devnet L1</span>
            </div>
          </div>
        </div>

        <!-- SECTION 1: DETAILED DEVELOPER GUIDE (SELLER) -->
        <div class="p-5 sm:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">1</span>
              <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.sec1Title">Integrate Paywall to Monetize Agents in 5 Minutes</h3>
            </div>
            <span class="text-[11px] font-mono text-neutral-400">Node.js / Express / TypeScript</span>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="dev.sec1Desc">
            Install official Haichain middleware to activate Replay Attack protection and verify on-chain Solana L1 transactions:
          </p>

          <!-- Step 1 Command -->
          <div class="space-y-1.5">
            <div class="text-[11px] font-semibold text-neutral-600 dark:text-neutral-300" data-i18n="dev.step1Label">Step 1: Install package</div>
            <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-3 font-mono text-xs flex items-center justify-between border border-neutral-800">
              <code class="overflow-x-auto text-[11px] sm:text-xs">npm install @haichainsi/agent-pay</code>
              <button onclick="navigator.clipboard.writeText('npm install @haichainsi/agent-pay'); if (window.showToast) { window.showToast('Copied to clipboard!', 'info'); } else { alert('Copied to clipboard!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer ml-2 shrink-0 transition-colors" data-i18n="btn.copy">
                Copy
              </button>
            </div>
          </div>

          <!-- Step 2 Code -->
          <div class="space-y-1.5">
            <div class="text-[11px] font-semibold text-neutral-600 dark:text-neutral-300" data-i18n="dev.step2Label">Step 2: Add 5 lines of code to your Express server</div>
            <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs border border-neutral-800">
              <div class="flex justify-between items-center pb-2 mb-2 border-b border-neutral-800 text-[10px] text-neutral-400">
                <span>server.ts</span>
                <button onclick="navigator.clipboard.writeText(document.getElementById('code-express-snippet').innerText); if (window.showToast) { window.showToast('Copied Express code snippet!', 'info'); } else { alert('Copied Express code snippet!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer transition-colors" data-i18n="btn.copyCode">
                  Copy Code
                </button>
              </div>
              <pre id="code-express-snippet" class="overflow-x-auto text-[11px] sm:text-xs leading-relaxed"><code>import express from 'express';
import { haichainPaywall } from '@haichainsi/agent-pay';

const app = express();
app.use(express.json());

// Attach HTTP 402 Paywall: auto-collect 0.003 USDT on Solana Devnet
app.use('/api/my-agent-task', haichainPaywall({
  recipient: '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3', // Your Solana recipient wallet address
  priceUsdt: 0.003,
  cluster: 'devnet',
  maxAgeSeconds: 300 // Replay attack defense, expires after 5 minutes
}));

app.post('/api/my-agent-task', (req, res) => {
  // Only requests with valid verified on-chain payment reach this handler
  res.json({
    status: 'SUCCESS',
    result: 'AI task completed, payment settled to your Solana wallet!',
    taskEcho: req.body.taskPayload
  });
});

app.listen(4020, () => console.log('Agent live on port 4020'));</code></pre>
            </div>
          </div>

          <!-- Step 3 Connect -->
          <div class="p-4 rounded-2xl bg-neutral-100 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-1 text-xs text-neutral-700 dark:text-neutral-300">
            <span class="font-bold text-black dark:text-white" data-i18n="dev.step3Title">Step 3: Earn autonomous revenue across the Haichain & Claude Desktop ecosystem</span>
            <p class="text-[11px] leading-relaxed" data-i18n="dev.step3Desc">
              When your agent published on Smithery or Fetch.ai attaches @haichainsi/agent-pay, any caller agent (Claude Desktop, Cursor, Haichain Relayer) will automatically stream USDT/SOL settlement straight to your Solana wallet via HTTP 402!
            </p>
          </div>
        </div>

        <!-- SECTION 2: CLAUDE DESKTOP & CURSOR MCP CONFIGURATION (BUYER) -->
        <div class="p-5 sm:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">2</span>
              <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.sec2Title">1-Click Setup for Claude Desktop & Cursor</h3>
            </div>
            <span class="text-[11px] font-mono text-neutral-400">Claude Desktop / Cursor IDE / Windsurf</span>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="dev.sec2Desc">
            Add the following JSON configuration to your Claude Desktop config file (claude_desktop_config.json) to let AI discover and hire agents:
          </p>

          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs border border-neutral-800">
            <div class="flex justify-between items-center pb-2 mb-2 border-b border-neutral-800 text-[10px] text-neutral-400">
              <span class="font-semibold text-neutral-200">claude_desktop_config.json</span>
              <button id="copy-mcp-code-btn" onclick="navigator.clipboard.writeText(document.getElementById('code-mcp-snippet').innerText); if (window.showToast) { window.showToast('Copied Claude config!', 'info'); } else { alert('Copied Claude config!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer transition-colors" data-i18n="btn.copyJson">
                Copy JSON
              </button>
            </div>
            <pre id="code-mcp-snippet" class="overflow-x-auto text-[11px] sm:text-xs leading-relaxed"><code>{
  "mcpServers": {
    "haichain-agent-economy": {
      "command": "node",
      "args": [
        "c:/Users/Surface/Documents/8. HAICHAIN/mcp-server/dist/index.js"
      ],
      "env": {
        "HAICHAIN_CLUSTER": "devnet"
      }
    }
  }
}</code></pre>
          </div>

          <div class="p-4 rounded-2xl bg-neutral-100 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2">
            <h4 class="font-bold text-xs text-black dark:text-white" data-i18n="dev.sec2PromptsTitle">
              Sample prompt commands for Claude:
            </h4>
            <ul class="text-[11px] text-neutral-600 dark:text-neutral-300 space-y-1 list-disc pl-4">
              <li><em data-i18n="dev.sec2Prompt1">"Find an agent on Haichain specialized in web scraping and hire it to extract content from https://example.com"</em></li>
              <li><em data-i18n="dev.sec2Prompt2">"Check real-time SOL/USDT market rates via Haichain financial intelligence agent"</em></li>
              <li><em data-i18n="dev.sec2Prompt3">"Hire an agent to audit this Rust smart contract codebase for missing signer vulnerabilities"</em></li>
            </ul>
          </div>
        </div>

        <!-- SECTION 3: TYPESCRIPT SDK -->
        <div class="p-5 sm:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">3</span>
              <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="mcp.sdkTitle">TypeScript SDK Integration</h3>
            </div>
            <span class="text-[11px] font-mono text-neutral-400">@haichainsi/sdk</span>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="mcp.sdkDesc">
            Issue capability tickets and programmatically execute micro-escrows via @haichainsi/sdk:
          </p>

          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs border border-neutral-800">
            <div class="flex justify-between items-center pb-2 mb-2 border-b border-neutral-800 text-[10px] text-neutral-400">
              <span class="font-semibold text-neutral-200">client.ts</span>
              <button onclick="navigator.clipboard.writeText(document.getElementById('code-sdk-snippet').innerText); if (window.showToast) { window.showToast('Copied SDK code snippet!', 'info'); } else { alert('Copied SDK code snippet!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer transition-colors" data-i18n="btn.copyCode">
                Copy Code
              </button>
            </div>
            <pre id="code-sdk-snippet" class="overflow-x-auto text-[11px] sm:text-xs leading-relaxed"><code>import { HaiChainClient } from "@haichainsi/sdk";

const client = new HaiChainClient({ network: "devnet" });
const ticket = client.issueCapabilityTicket({
  maxSpendMicroUsdt: 50_000, // 0.05 USDT
  expirySlotDelta: 1000
});

console.log("Ticket ready for autonomous execution:", ticket.nonce);</code></pre>
          </div>
        </div>

        <!-- SECTION 4: DIRECT REST API REFERENCE -->
        <div class="p-5 sm:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center space-x-2">
            <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">4</span>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.sec3Title">Direct REST API Dispatch</h3>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="dev.sec3Desc">
            If you are developing a mobile app or backend microservice, you can directly call our Gateway endpoint to broadcast verified L1 transactions:
          </p>

          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs border border-neutral-800">
            <div class="flex justify-between items-center pb-2 mb-2 border-b border-neutral-800 text-[10px] text-neutral-400">
              <span class="font-semibold text-neutral-200">POST /api/relayer/dispatch</span>
              <button onclick="navigator.clipboard.writeText(document.getElementById('code-curl-snippet').innerText); if (window.showToast) { window.showToast('Copied cURL command!', 'info'); } else { alert('Copied cURL command!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer transition-colors" data-i18n="btn.copyCurl">
                Copy cURL
              </button>
            </div>
            <pre id="code-curl-snippet" class="overflow-x-auto text-[11px] sm:text-xs leading-relaxed"><code>curl -X POST https://bubble-prescription-miller-recruiting.trycloudflare.com/api/relayer/dispatch \\
  -H "Content-Type: application/json" \\
  -d '{
    "agentId": "agent-smithery-scraper-01",
    "taskPayload": "https://example.com",
    "bidAmountUsdt": 0.003,
    "recipientAddress": "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3"
  }'</code></pre>
          </div>
        </div>
      </section>`;
}

function processDashboardFile(filePath) {
  console.log(`Processing ${filePath}...`);
  let content = fs.readFileSync(filePath, 'utf8');

  // 1. Replace the two sidebar buttons with the unified button
  const sidebarOldRegex = /<button class="nav-tab-btn[^>]*data-tab="tab-mcp"[\s\S]*?<span[^>]*data-i18n="nav\.mcp"[^>]*>[\s\S]*?<\/button>\s*<button class="nav-tab-btn[^>]*data-tab="tab-docs"[\s\S]*?<span[^>]*data-i18n="nav\.docs"[^>]*>[\s\S]*?<\/button>/;
  
  const unifiedSidebarBtn = `<button class="nav-tab-btn w-full flex items-center space-x-3 px-3.5 py-2.5 rounded-xl text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-all text-left" data-tab="tab-docs">
          <i data-lucide="terminal" class="w-4 h-4 text-black dark:text-white"></i>
          <span data-i18n="nav.devHub">Developer & MCP Hub</span>
        </button>`;

  if (sidebarOldRegex.test(content)) {
    content = content.replace(sidebarOldRegex, unifiedSidebarBtn);
    console.log(`  [OK] Replaced sidebar nav buttons in ${filePath}`);
  } else {
    console.warn(`  [WARN] Sidebar regex did not match in ${filePath}, checking alternative`);
  }

  // 2. Replace the mobile bottom bar button
  const mobileOldRegex = /<button class="nav-tab-btn[^>]*data-tab="tab-mcp"[\s\S]*?<span[^>]*data-i18n="nav\.mcp"[^>]*>[\s\S]*?<\/button>/;
  const unifiedMobileBtn = `<button class="nav-tab-btn flex flex-col items-center justify-center py-1 px-1 transition-all active:opacity-70 group cursor-pointer" data-tab="tab-docs">
        <div class="tab-icon-wrapper w-10 h-7 flex items-center justify-center rounded-xl text-neutral-400 dark:text-neutral-500 group-[.active]:bg-black dark:group-[.active]:bg-white group-[.active]:text-white dark:group-[.active]:text-black transition-all">
          <i data-lucide="terminal" class="w-4 h-4 stroke-[2]"></i>
        </div>
        <span class="text-[9px] font-medium tracking-tight text-neutral-400 dark:text-neutral-500 group-[.active]:text-black dark:group-[.active]:text-white mt-0.5 truncate max-w-[56px]" data-i18n="nav.devHubShort">Dev & MCP</span>
      </button>`;

  if (mobileOldRegex.test(content)) {
    content = content.replace(mobileOldRegex, unifiedMobileBtn);
    console.log(`  [OK] Replaced mobile bottom bar button in ${filePath}`);
  } else {
    console.warn(`  [WARN] Mobile bottom bar regex did not match in ${filePath}`);
  }

  // 3. Remove <section id="tab-mcp"> ... </section>
  const mcpSectionRegex = /(?:<!--[^\n]*TAB:\s*MCP[^\n]*-->\s*)?<section id="tab-mcp"[\s\S]*?<\/section>/;
  if (mcpSectionRegex.test(content)) {
    content = content.replace(mcpSectionRegex, '');
    console.log(`  [OK] Removed <section id="tab-mcp"> in ${filePath}`);
  } else {
    console.warn(`  [WARN] <section id="tab-mcp"> not found in ${filePath}`);
  }

  // 4. Replace <section id="tab-docs"> with the merged section
  const docsSectionRegex = /(?:<!--[^\n]*TAB:\s*DEVELOPER[^\n]*-->\s*)?<section id="tab-docs"[\s\S]*?<\/section>/;
  if (docsSectionRegex.test(content)) {
    content = content.replace(docsSectionRegex, buildMergedDevHubSection());
    console.log(`  [OK] Replaced <section id="tab-docs"> with merged Developer & MCP Hub in ${filePath}`);
  } else {
    console.warn(`  [WARN] <section id="tab-docs"> not found in ${filePath}`);
  }

  // 5. Update JavaScript tabTitles and routing
  // In tabTitles objects: 'tab-mcp': 'nav.mcp' -> 'tab-mcp': 'nav.devHub', 'tab-docs': 'nav.docs' -> 'tab-docs': 'nav.devHub'
  content = content.replace(/'tab-mcp':\s*'nav\.mcp'/g, "'tab-mcp': 'nav.devHub'");
  content = content.replace(/'tab-docs':\s*'nav\.docs'/g, "'tab-docs': 'nav.devHub'");
  content = content.replace(/'tab-mcp':\s*'MCP & Developer Center'/g, "'tab-mcp': 'Developer & MCP Hub'");
  content = content.replace(/'tab-docs':\s*'Developer Docs & Quickstart'/g, "'tab-docs': 'Developer & MCP Hub'");

  // Route URL params:
  content = content.replace(
    /if\s*\(\s*urlTab\s*===\s*'mcp'\s*\)\s*urlTab\s*=\s*'tab-mcp';\s*if\s*\(\s*urlTab\s*===\s*'docs'\s*\|\|\s*urlTab\s*===\s*'dev'\s*\|\|\s*urlTab\s*===\s*'quickstart'\s*\)\s*urlTab\s*=\s*'tab-docs';/,
    "if (urlTab === 'mcp' || urlTab === 'docs' || urlTab === 'dev' || urlTab === 'quickstart') urlTab = 'tab-docs';"
  );

  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`  [DONE] Saved updated ${filePath}\n`);
}

processDashboardFile('dashboard.html');
processDashboardFile('app/dashboard.html');
