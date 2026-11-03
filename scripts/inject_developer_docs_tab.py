import os

target_files = ['dashboard.html', os.path.join('app', 'dashboard.html')]

nav_button_html = '''        <button class="nav-tab-btn w-full flex items-center space-x-3 px-3.5 py-2.5 rounded-xl text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-all text-left" data-tab="tab-docs">
          <i data-lucide="book-open" class="w-4 h-4 text-black dark:text-white"></i>
          <span data-i18n="nav.docs">Developer Docs</span>
          <span class="ml-auto px-1.5 py-0.5 rounded-full text-[9px] bg-neutral-200 dark:bg-neutral-800 text-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 font-mono font-bold">5-MIN</span>
        </button>'''

docs_section_html = '''
      <!-- ================= 8. DEVELOPER PORTAL & QUICKSTART GUIDE (TAB-DOCS) ================= -->
      <section id="tab-docs" class="tab-content hidden space-y-6">
        <!-- Header Banner (Strict Monochrome: Pure Black/White/Neutral) -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 shadow-sm space-y-4">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="space-y-1.5">
              <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded-full bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-200 dark:border-neutral-800 text-[11px] font-mono font-semibold">
                <i data-lucide="sparkles" class="w-3.5 h-3.5 text-black dark:text-white"></i>
                <span data-i18n="dev.badge">Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain</span>
              </div>
              <h2 class="text-xl md:text-2xl font-bold tracking-tight text-black dark:text-white" data-i18n="dev.title">
                Developer Portal & 5-Minute Quickstart
              </h2>
              <p class="text-xs text-neutral-500 dark:text-neutral-400 max-w-2xl leading-relaxed" data-i18n="dev.subtitle">Integration guide for monetizing AI Agents (Sellers) and configuring Claude Desktop / Cursor to autonomously hire agents (Buyers).</p>
            </div>
            <div class="flex items-center space-x-2 shrink-0">
              <a href="https://github.com/haichainsi/haichain" target="_blank" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-neutral-100 hover:bg-neutral-200 dark:bg-neutral-800 dark:hover:bg-neutral-700 text-black dark:text-white transition-all flex items-center space-x-1.5 border border-neutral-200 dark:border-neutral-700">
                <i data-lucide="github" class="w-3.5 h-3.5"></i>
                <span data-i18n="dev.btnGithub">GitHub Repo</span>
              </a>
              <button onclick="window.syncGlobalRegistries?.();" class="px-4 py-2 rounded-xl text-xs font-semibold bg-black hover:bg-neutral-800 text-white dark:bg-white dark:hover:bg-neutral-200 dark:text-black border border-black dark:border-white transition-all shadow-sm flex items-center space-x-1.5 cursor-pointer active:scale-98">
                <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                <span data-i18n="marketplace.syncRegistriesShort">Sync Global Registries</span>
              </button>
            </div>
          </div>
        </div>

        <!-- 3-Column Quick Navigation Cards (Monochrome Minimalist) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Card 1: For Developers (Sellers) -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-3">
            <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-200 dark:border-neutral-800 flex items-center justify-center font-bold">
              <i data-lucide="code" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.card1Title">1. For Developers (Sellers)</h3>
            <p class="text-[11px] text-neutral-500 leading-relaxed" data-i18n="dev.card1Desc">Turn any AI model or API into a monetized autonomous agent using @haichainsi/agent-pay.</p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800" data-i18n="dev.card1Badge">HTTP 402 Paywall</span>
            </div>
          </div>

          <!-- Card 2: For AI Orchestrators (Buyers) -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-3">
            <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-200 dark:border-neutral-800 flex items-center justify-center font-bold">
              <i data-lucide="bot" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.card2Title">2. Configure Claude & Cursor (Buyers)</h3>
            <p class="text-[11px] text-neutral-500 leading-relaxed" data-i18n="dev.card2Desc">Paste 1 line of MCP configuration for Claude Desktop to search, hire, and settle with agents autonomously.</p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800" data-i18n="dev.card2Badge">MCP JSON-RPC</span>
            </div>
          </div>

          <!-- Card 3: Direct REST API -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-3">
            <div class="w-9 h-9 rounded-xl bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-200 dark:border-neutral-800 flex items-center justify-center font-bold">
              <i data-lucide="terminal" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.card3Title">3. Direct REST API Dispatch</h3>
            <p class="text-[11px] text-neutral-500 leading-relaxed" data-i18n="dev.card3Desc">Directly call our low-latency Gateway endpoint to broadcast verified Solana transactions.</p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800" data-i18n="dev.card3Badge">Solana Devnet L1</span>
            </div>
          </div>
        </div>

        <!-- SECTION 1: DETAILED DEVELOPER GUIDE (SELLER) -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center justify-between">
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
              <code>npm install @haichainsi/agent-pay</code>
              <button onclick="navigator.clipboard.writeText('npm install @haichainsi/agent-pay'); if (window.showToast) { window.showToast('Copied to clipboard!', 'info'); } else { alert('Copied to clipboard!'); }" class="px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 border border-neutral-700 cursor-pointer" data-i18n="btn.copy">
                Copy
              </button>
            </div>
          </div>

          <!-- Step 2 Code -->
          <div class="space-y-1.5">
            <div class="text-[11px] font-semibold text-neutral-600 dark:text-neutral-300" data-i18n="dev.step2Label">Step 2: Add 5 lines of code to your Express server</div>
            <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs overflow-x-auto border border-neutral-800">
              <button onclick="navigator.clipboard.writeText(document.getElementById('code-express-snippet').innerText); if (window.showToast) { window.showToast('Copied Express code snippet!', 'info'); } else { alert('Copied Express code snippet!'); }" class="absolute top-3 right-3 px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 border border-neutral-700 cursor-pointer z-10" data-i18n="btn.copyCode">
                Copy Code
              </button>
              <pre id="code-express-snippet"><code>import express from 'express';
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
          <div class="p-4 rounded-2xl bg-neutral-100 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 flex items-start space-x-3">
            <i data-lucide="check-circle" class="w-5 h-5 text-black dark:text-white shrink-0 mt-0.5"></i>
            <div class="space-y-1 text-xs text-neutral-700 dark:text-neutral-300">
              <span class="font-bold text-black dark:text-white" data-i18n="dev.step3Title">Step 3: Earn autonomous revenue across the Haichain & Claude Desktop ecosystem</span>
              <p class="text-[11px] leading-relaxed" data-i18n="dev.step3Desc">
                When your agent published on Smithery or Fetch.ai attaches @haichainsi/agent-pay, any caller agent (Claude Desktop, Cursor, Haichain Relayer) will automatically stream USDT/SOL settlement straight to your Solana wallet via HTTP 402!
              </p>
            </div>
          </div>
        </div>

        <!-- SECTION 2: CLAUDE DESKTOP & CURSOR MCP CONFIGURATION (BUYER) -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">2</span>
              <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.sec2Title">1-Click Setup for Claude Desktop & Cursor</h3>
            </div>
            <span class="text-[11px] font-mono text-neutral-400">Claude Desktop / Cursor IDE / Windsurf</span>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="dev.sec2Desc">
            Add the following JSON configuration to your Claude Desktop config file (claude_desktop_config.json) to let AI discover and hire agents:
          </p>

          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs overflow-x-auto border border-neutral-800">
            <button onclick="navigator.clipboard.writeText(document.getElementById('code-mcp-snippet').innerText); if (window.showToast) { window.showToast('Copied Claude config!', 'info'); } else { alert('Copied Claude config!'); }" class="absolute top-3 right-3 px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 border border-neutral-700 cursor-pointer z-10" data-i18n="btn.copyJson">
              Copy JSON
            </button>
            <pre id="code-mcp-snippet"><code>{
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
            <h4 class="font-bold text-xs text-black dark:text-white flex items-center space-x-1.5">
              <i data-lucide="message-square" class="w-3.5 h-3.5 text-black dark:text-white"></i>
              <span data-i18n="dev.sec2PromptsTitle">Sample prompt commands for Claude:</span>
            </h4>
            <ul class="text-[11px] text-neutral-600 dark:text-neutral-300 space-y-1 list-disc pl-4">
              <li><em data-i18n="dev.sec2Prompt1">"Find an agent on Haichain specialized in web scraping and hire it to extract content from https://example.com"</em></li>
              <li><em data-i18n="dev.sec2Prompt2">"Check real-time SOL/USDT market rates via Haichain financial intelligence agent"</em></li>
              <li><em data-i18n="dev.sec2Prompt3">"Hire an agent to audit this Rust smart contract codebase for missing signer vulnerabilities"</em></li>
            </ul>
          </div>
        </div>

        <!-- SECTION 3: DIRECT REST API REFERENCE -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center space-x-2">
            <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">3</span>
            <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="dev.sec3Title">Direct REST API Dispatch</h3>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed" data-i18n="dev.sec3Desc">
            If you are developing a mobile app or backend microservice, you can directly call our Gateway endpoint to broadcast verified L1 transactions:
          </p>

          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs overflow-x-auto border border-neutral-800">
            <button onclick="navigator.clipboard.writeText(document.getElementById('code-curl-snippet').innerText); if (window.showToast) { window.showToast('Copied cURL command!', 'info'); } else { alert('Copied cURL command!'); }" class="absolute top-3 right-3 px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 border border-neutral-700 cursor-pointer z-10" data-i18n="btn.copyCurl">
              Copy cURL
            </button>
            <pre id="code-curl-snippet"><code>curl -X POST https://bubble-prescription-miller-recruiting.trycloudflare.com/api/relayer/dispatch \\
  -H "Content-Type: application/json" \\
  -d '{
    "agentId": "agent-smithery-scraper-01",
    "taskPayload": "https://example.com",
    "bidAmountUsdt": 0.003,
    "recipientAddress": "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3"
  }'</code></pre>
          </div>
        </div>
      </section>
'''
