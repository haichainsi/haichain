import re

print("Injecting missing renderGlobalAgentMarketplace() JS into dashboard.html and app/dashboard.html...")

JS_CODE = '''
    // ==============================================================================
    // 12. GLOBAL AGENT LABOR MARKETPLACE (SMITHERY • FETCH.AI • GLAMA) - PHASE 1
    // ==============================================================================
    const GLOBAL_MARKET_AGENTS = [
      {
        agentId: 'agent-smithery-scraper-01',
        name: 'Smithery Web Extraction Sentinel',
        provider: 'Smithery MCP Registry',
        category: 'data_extraction',
        pricingUsdt: 0.003,
        slaUptime: '99.9%',
        description: 'Autonomous headless browser crawling, dynamic SPA scraping, and structured JSON extraction.',
        recipientAddress: 'Sm1thScrap3rPo1nt782VbX4nNmK9q1zEwR2Ty7LpA',
        capabilities: ['Headless Chromium', 'Anti-bot bypass', 'Table to JSON']
      },
      {
        agentId: 'agent-fetch-market-intel-04',
        name: 'Fetch.ai Autonomous Financial Sentinel',
        provider: 'Fetch.ai Almanac Network',
        category: 'financial_intelligence',
        pricingUsdt: 0.005,
        slaUptime: '99.8%',
        description: 'Real-time cryptocurrency orderbook depth, on-chain whale flow tracking, and macro sentiment analysis.',
        recipientAddress: 'F3tchA1m4n4cMkt1nt3l8890xVcZbPqQwErTy44Kz',
        capabilities: ['CEX/DEX Liquidity', 'Tokenomics audit', 'Volatility forecast']
      },
      {
        agentId: 'agent-glama-sec-audit-09',
        name: 'Glama Solana / Rust Security Auditor',
        provider: 'Glama Verified Security Network',
        category: 'security_audit',
        pricingUsdt: 0.010,
        slaUptime: '99.95%',
        description: 'Static and symbolic execution analysis for Solana Anchor programs, reentrancy detection, and PDA validation.',
        recipientAddress: 'G14m4Aud1t0rSecur1ty998811VvBbNnMmKkLlJjHh',
        capabilities: ['Anchor Rust scan', 'PDA seed check', 'Overflow verification']
      },
      {
        agentId: 'agent-haichain-code-sandbox-02',
        name: 'HAICHAIN Ephemeral WASM Sandbox Node',
        provider: 'HAICHAIN TEE Compute Cloud',
        category: 'automation',
        pricingUsdt: 0.002,
        slaUptime: '100.0%',
        description: 'Isolated, hardware-secure TEE sandbox for Python, JavaScript, and Rust script compilation & execution.',
        recipientAddress: 'H41Ch41nS4ndb0xT33C0mput38827VbNmKqLpA1zX',
        capabilities: ['Python 3.12 sandbox', 'Data transformation', 'Graph generation']
      },
      {
        agentId: 'agent-smithery-sentiment-07',
        name: 'Global Cross-Platform Sentiment Radar',
        provider: 'Smithery MCP Registry',
        category: 'financial_intelligence',
        pricingUsdt: 0.004,
        slaUptime: '99.7%',
        description: 'Multi-lingual social signal extraction (X/Twitter, Reddit, Telegram, Farcaster) with FinBERT scoring.',
        recipientAddress: 'S3nt1m3ntR4d4rSm1th3ry8811VbNmKqLpA1zX99',
        capabilities: ['Social sentiment', 'FUD / FOMO index', 'Influencer tracking']
      },
      {
        agentId: 'agent-fetch-arbitrage-11',
        name: 'DEX Cross-Pool Liquidity & Flash Arbitrage Sentinel',
        provider: 'Fetch.ai uAgents Protocol',
        category: 'automation',
        pricingUsdt: 0.008,
        slaUptime: '99.9%',
        description: 'Continuous monitoring of Raydium, Orca, and Meteora pools for triangular arbitrage and impermanent loss risks.',
        recipientAddress: 'Arb1tr4g3F3tchS3nt1n3l776655VvBbNnMmKkLlL',
        capabilities: ['Solana DEX routing', 'Slippage modeling', 'Pool health score']
      }
    ];

    let currentMarketCategory = 'all';
    let currentMarketSearch = '';
    let selectedHireAgent = null;

    function renderGlobalAgentMarketplace() {
      const grid = document.getElementById('global-agent-market-grid');
      if (!grid) return;

      const filtered = GLOBAL_MARKET_AGENTS.filter(a => {
        if (currentMarketCategory !== 'all' && a.category !== currentMarketCategory) return false;
        if (!currentMarketSearch) return true;
        const s = `${a.name} ${a.description} ${a.provider} ${a.capabilities.join(' ')}`.toLowerCase();
        return s.includes(currentMarketSearch);
      });

      if (filtered.length === 0) {
        grid.innerHTML = `
          <div class="col-span-full py-8 text-center text-neutral-400 font-mono text-xs">
            No agents found matching "${currentMarketSearch}". Try searching for 'scraping', 'audit', or 'crypto'.
          </div>
        `;
        return;
      }

      grid.innerHTML = filtered.map(agent => `
        <div class="p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 hover:border-black dark:hover:border-white transition-all flex flex-col justify-between space-y-3">
          <div class="space-y-2">
            <div class="flex items-start justify-between gap-2">
              <span class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate max-w-[170px]">
                ${agent.provider}
              </span>
              <span class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 font-semibold shrink-0">
                SLA ${agent.slaUptime}
              </span>
            </div>
            <h4 class="font-bold text-xs text-black dark:text-white leading-snug">${agent.name}</h4>
            <p class="text-[11px] text-neutral-500 leading-relaxed">${agent.description}</p>
            <div class="flex flex-wrap gap-1 pt-1">
              ${agent.capabilities.map(c => `
                <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">
                  ${c}
                </span>
              `).join('')}
            </div>
          </div>

          <div class="pt-3 border-t border-neutral-200/60 dark:border-neutral-800 flex items-center justify-between gap-2">
            <div>
              <span class="text-[9px] text-neutral-400 block font-mono">Micro-Task Rate</span>
              <span class="font-bold text-xs text-black dark:text-white font-mono">$${agent.pricingUsdt.toFixed(4)} USDT</span>
            </div>
            <button class="hire-agent-btn px-3 py-1.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-[11px] font-semibold transition-all active:scale-98 cursor-pointer" data-agent-id="${agent.agentId}">
              Hire Agent
            </button>
          </div>
        </div>
      `).join('');

      grid.querySelectorAll('.hire-agent-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const id = btn.getAttribute('data-agent-id');
          openHireAgentModal(id);
        });
      });

      if (typeof safeCreateIcons === 'function') safeCreateIcons();
    }

    function openHireAgentModal(agentId) {
      const agent = GLOBAL_MARKET_AGENTS.find(a => a.agentId === agentId);
      if (!agent) return;
      selectedHireAgent = agent;

      const nameEl = document.getElementById('hire-modal-agent-name');
      const provEl = document.getElementById('hire-modal-agent-provider');
      const rateEl = document.getElementById('hire-modal-rate');
      const recipEl = document.getElementById('hire-modal-recipient');
      const payloadEl = document.getElementById('hire-task-payload-input');
      const resultBox = document.getElementById('hire-execution-result-box');
      const confirmBtn = document.getElementById('confirm-hire-agent-btn');
      const btnText = document.getElementById('confirm-hire-btn-text');

      if (nameEl) nameEl.textContent = agent.name;
      if (provEl) provEl.textContent = `${agent.provider} • ID: ${agent.agentId}`;
      if (rateEl) rateEl.textContent = `$${agent.pricingUsdt.toFixed(4)} USDT`;
      if (recipEl) recipEl.textContent = agent.recipientAddress;

      const defaultPayloads = {
        data_extraction: 'Crawl target URL https://solana.com/ecosystem and parse active developer metrics into JSON.',
        financial_intelligence: 'Scan liquidity depth across Raydium & Orca for SOL/USDC. Highlight volatility spreads.',
        security_audit: 'Execute invariant audit and Anchor PDA collision check on program DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk.',
        automation: 'Run sandboxed Python script to compute moving averages and format KaTeX report.'
      };

      if (payloadEl) payloadEl.value = defaultPayloads[agent.category] || 'Execute autonomous task payload with verified cryptographic receipt.';
      if (resultBox) resultBox.classList.add('hidden');
      if (confirmBtn) confirmBtn.disabled = false;
      if (btnText) btnText.textContent = 'Execute Micro-Escrow';

      const modal = document.getElementById('hire-agent-modal');
      if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
      }
      if (typeof safeCreateIcons === 'function') safeCreateIcons();
    }

    function closeHireModal() {
      const modal = document.getElementById('hire-agent-modal');
      if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }
    }

    function initGlobalAgentMarketplaceEvents() {
      const closeHireBtn = document.getElementById('close-hire-agent-modal');
      if (closeHireBtn) closeHireBtn.addEventListener('click', closeHireModal);

      const cancelHireBtn = document.getElementById('cancel-hire-btn');
      if (cancelHireBtn) cancelHireBtn.addEventListener('click', closeHireModal);

      const modalEl = document.getElementById('hire-agent-modal');
      if (modalEl) {
        modalEl.addEventListener('click', (e) => {
          if (e.target === modalEl) closeHireModal();
        });
      }

      const confirmHireBtn = document.getElementById('confirm-hire-agent-btn');
      if (confirmHireBtn) {
        confirmHireBtn.addEventListener('click', async () => {
          if (!selectedHireAgent) return;
          const payloadInput = document.getElementById('hire-task-payload-input');
          const taskPayload = payloadInput ? payloadInput.value.trim() : '';
          if (!taskPayload) {
            alert('Please enter a task instruction or payload.');
            return;
          }

          const btnText = document.getElementById('confirm-hire-btn-text');
          confirmHireBtn.disabled = true;
          if (btnText) btnText.innerHTML = '<span class="w-3 h-3 rounded-full border-2 border-current border-t-transparent animate-spin inline-block mr-1"></span> Settling on Solana...';

          // Simulate 600ms network execution for high fidelity
          await new Promise(r => setTimeout(r, 600));

          const jobId = 'JOB-' + Date.now().toString(36).toUpperCase() + '-' + Math.floor(Math.random() * 9000 + 1000);
          const sig = '4AgntH1re' + Array.from({length: 78}, () => Math.floor(Math.random()*36).toString(36)).join('');
          
          let execResult = '';
          if (selectedHireAgent.category === 'data_extraction') {
            execResult = `[Executed by ${selectedHireAgent.name}]: Crawled target payload (${taskPayload.slice(0, 60)}...). Extracted 14 verified data entities into structured JSON schema with zero CAPTCHA delays.`;
          } else if (selectedHireAgent.category === 'security_audit') {
            execResult = `[Executed by ${selectedHireAgent.name}]: Completed AST static symbolic audit. Invariant I1-I9 integrity verified 100%, 0 reentrancy vulnerabilities discovered.`;
          } else if (selectedHireAgent.category === 'financial_intelligence') {
            execResult = `[Executed by ${selectedHireAgent.name}]: Scanned live orderbook liquidity and whale transaction volume for payload query. Consolidated real-time alpha signal into quantitative score.`;
          } else {
            execResult = `[Executed by ${selectedHireAgent.name}]: Completed autonomous workload (${taskPayload.slice(0, 80)}). Cryptographic settlement proof verified on Solana L1.`;
          }

          const resultBox = document.getElementById('hire-execution-result-box');
          const resJobId = document.getElementById('hire-result-job-id');
          const resSummary = document.getElementById('hire-result-summary');
          const resTxLink = document.getElementById('hire-result-tx-link');

          if (resultBox) resultBox.classList.remove('hidden');
          if (resJobId) resJobId.textContent = jobId;
          if (resSummary) resSummary.textContent = execResult;
          if (resTxLink) {
            resTxLink.href = `https://explorer.solana.com/tx/${sig}?cluster=devnet`;
            resTxLink.textContent = `Tx: ${sig.slice(0, 16)}... (Confirmed)`;
          }

          if (btnText) btnText.textContent = 'Settled & Completed';

          // Append to Ledger
          if (typeof appendLedgerRow === 'function') {
            appendLedgerRow({
              nonce: Math.floor(Math.random() * 8000 + 1000),
              service: `${selectedHireAgent.name} (Global Agent)`,
              proof: `Escrow: ${sig.slice(0, 8)}...`,
              amount: `$${selectedHireAgent.pricingUsdt.toFixed(4)}`,
              latency: '342ms',
              txSig: sig
            });
          }

          // Show Toast Notification
          if (typeof showToast === 'function') {
            showToast({
              title: 'Agent Hired & Settled On-Chain',
              message: `Paid $${selectedHireAgent.pricingUsdt.toFixed(4)} USDT to ${selectedHireAgent.provider}`,
              icon: 'check-circle'
            });
          }

          if (typeof safeCreateIcons === 'function') safeCreateIcons();
        });
      }

      // Search Input
      const searchInp = document.getElementById('agent-market-search-input');
      if (searchInp) {
        searchInp.addEventListener('input', (e) => {
          currentMarketSearch = e.target.value.toLowerCase().trim();
          renderGlobalAgentMarketplace();
        });
      }

      // Category buttons
      const catBtns = document.querySelectorAll('.market-cat-btn');
      catBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          catBtns.forEach(b => {
            b.className = "market-cat-btn px-3 py-2 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer";
          });
          btn.className = "market-cat-btn px-3 py-2 rounded-xl text-xs font-medium bg-black text-white dark:bg-white dark:text-black border border-black dark:border-white shrink-0 transition-all cursor-pointer";
          currentMarketCategory = btn.getAttribute('data-category') || 'all';
          renderGlobalAgentMarketplace();
        });
      });

      // Render initially
      renderGlobalAgentMarketplace();
    }
'''

for filepath in ['dashboard.html', 'app/dashboard.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'function renderGlobalAgentMarketplace()' in content:
        print(f"  {filepath} already contains function renderGlobalAgentMarketplace(). Skipping.")
        continue

    # Insert right before "initHeartbeatSession();"
    target = "initHeartbeatSession();"
    if target in content:
        injection = JS_CODE + "\n    initGlobalAgentMarketplaceEvents();\n\n    " + target
        content = content.replace(target, injection, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Successfully injected marketplace JS into {filepath}")
    else:
        print(f"  ERROR: Could not find target '{target}' in {filepath}")

print("=== Injection Finished ===")
