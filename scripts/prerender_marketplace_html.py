import re

print("Pre-rendering Global Agent Marketplace cards directly into static HTML...")

STATIC_CARDS_HTML = '''
            <!-- 1. Smithery Scraper Agent -->
            <div class="agent-market-card p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 hover:border-black dark:hover:border-white transition-all flex flex-col justify-between space-y-3" data-category="data_extraction">
              <div class="space-y-2">
                <div class="flex items-start justify-between gap-2">
                  <a href="https://smithery.ai" target="_blank" class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate hover:text-black dark:hover:text-white flex items-center space-x-1">
                    <span>Smithery MCP Registry</span>
                    <i data-lucide="external-link" class="w-2.5 h-2.5 inline-block"></i>
                  </a>
                  <span class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 font-semibold shrink-0">SLA 99.9%</span>
                </div>
                <h4 class="font-bold text-xs text-black dark:text-white leading-snug">Smithery Web Extraction Sentinel</h4>
                <p class="text-[11px] text-neutral-500 leading-relaxed">Autonomous headless browser crawling, dynamic SPA scraping, and structured JSON extraction.</p>
                <div class="flex flex-wrap gap-1 pt-1">
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Headless Chromium</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Anti-bot bypass</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Table to JSON</span>
                </div>
              </div>
              <div class="pt-3 border-t border-neutral-200/60 dark:border-neutral-800 flex items-center justify-between gap-2">
                <div>
                  <span class="text-[9px] text-neutral-400 block font-mono">Micro-Task Rate</span>
                  <span class="font-bold text-xs text-black dark:text-white font-mono">$0.0030 USDT</span>
                </div>
                <button class="hire-agent-btn px-3 py-1.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-[11px] font-semibold transition-all active:scale-98 cursor-pointer" data-agent-id="agent-smithery-scraper-01">
                  Hire Agent
                </button>
              </div>
            </div>

            <!-- 2. Fetch.ai Financial Sentinel -->
            <div class="agent-market-card p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 hover:border-black dark:hover:border-white transition-all flex flex-col justify-between space-y-3" data-category="financial_intelligence">
              <div class="space-y-2">
                <div class="flex items-start justify-between gap-2">
                  <a href="https://agentverse.ai" target="_blank" class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate hover:text-black dark:hover:text-white flex items-center space-x-1">
                    <span>Fetch.ai Almanac Network</span>
                    <i data-lucide="external-link" class="w-2.5 h-2.5 inline-block"></i>
                  </a>
                  <span class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 font-semibold shrink-0">SLA 99.8%</span>
                </div>
                <h4 class="font-bold text-xs text-black dark:text-white leading-snug">Fetch.ai Autonomous Financial Sentinel</h4>
                <p class="text-[11px] text-neutral-500 leading-relaxed">Real-time cryptocurrency orderbook depth, on-chain whale flow tracking, and macro sentiment analysis.</p>
                <div class="flex flex-wrap gap-1 pt-1">
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">CEX/DEX Liquidity</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Tokenomics audit</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Volatility forecast</span>
                </div>
              </div>
              <div class="pt-3 border-t border-neutral-200/60 dark:border-neutral-800 flex items-center justify-between gap-2">
                <div>
                  <span class="text-[9px] text-neutral-400 block font-mono">Micro-Task Rate</span>
                  <span class="font-bold text-xs text-black dark:text-white font-mono">$0.0050 USDT</span>
                </div>
                <button class="hire-agent-btn px-3 py-1.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-[11px] font-semibold transition-all active:scale-98 cursor-pointer" data-agent-id="agent-fetch-market-intel-04">
                  Hire Agent
                </button>
              </div>
            </div>

            <!-- 3. Glama Security Auditor -->
            <div class="agent-market-card p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 hover:border-black dark:hover:border-white transition-all flex flex-col justify-between space-y-3" data-category="security_audit">
              <div class="space-y-2">
                <div class="flex items-start justify-between gap-2">
                  <a href="https://glama.ai/mcp/servers" target="_blank" class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate hover:text-black dark:hover:text-white flex items-center space-x-1">
                    <span>Glama Security Network</span>
                    <i data-lucide="external-link" class="w-2.5 h-2.5 inline-block"></i>
                  </a>
                  <span class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 font-semibold shrink-0">SLA 99.95%</span>
                </div>
                <h4 class="font-bold text-xs text-black dark:text-white leading-snug">Glama Solana / Rust Security Auditor</h4>
                <p class="text-[11px] text-neutral-500 leading-relaxed">Static and symbolic execution analysis for Solana Anchor programs, reentrancy detection, and PDA validation.</p>
                <div class="flex flex-wrap gap-1 pt-1">
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Anchor Rust scan</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">PDA seed check</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Overflow verify</span>
                </div>
              </div>
              <div class="pt-3 border-t border-neutral-200/60 dark:border-neutral-800 flex items-center justify-between gap-2">
                <div>
                  <span class="text-[9px] text-neutral-400 block font-mono">Micro-Task Rate</span>
                  <span class="font-bold text-xs text-black dark:text-white font-mono">$0.0100 USDT</span>
                </div>
                <button class="hire-agent-btn px-3 py-1.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-[11px] font-semibold transition-all active:scale-98 cursor-pointer" data-agent-id="agent-glama-sec-audit-09">
                  Hire Agent
                </button>
              </div>
            </div>

            <!-- 4. HAICHAIN WASM Sandbox -->
            <div class="agent-market-card p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 hover:border-black dark:hover:border-white transition-all flex flex-col justify-between space-y-3" data-category="automation">
              <div class="space-y-2">
                <div class="flex items-start justify-between gap-2">
                  <span class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate">
                    HAICHAIN TEE Cloud
                  </span>
                  <span class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 font-semibold shrink-0">SLA 100%</span>
                </div>
                <h4 class="font-bold text-xs text-black dark:text-white leading-snug">HAICHAIN Ephemeral WASM Sandbox Node</h4>
                <p class="text-[11px] text-neutral-500 leading-relaxed">Isolated, hardware-secure TEE sandbox for Python, JavaScript, and Rust script compilation & execution.</p>
                <div class="flex flex-wrap gap-1 pt-1">
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Python 3.12 sandbox</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Data transform</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Graph generate</span>
                </div>
              </div>
              <div class="pt-3 border-t border-neutral-200/60 dark:border-neutral-800 flex items-center justify-between gap-2">
                <div>
                  <span class="text-[9px] text-neutral-400 block font-mono">Micro-Task Rate</span>
                  <span class="font-bold text-xs text-black dark:text-white font-mono">$0.0020 USDT</span>
                </div>
                <button class="hire-agent-btn px-3 py-1.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-[11px] font-semibold transition-all active:scale-98 cursor-pointer" data-agent-id="agent-haichain-code-sandbox-02">
                  Hire Agent
                </button>
              </div>
            </div>

            <!-- 5. Smithery Sentiment Radar -->
            <div class="agent-market-card p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 hover:border-black dark:hover:border-white transition-all flex flex-col justify-between space-y-3" data-category="financial_intelligence">
              <div class="space-y-2">
                <div class="flex items-start justify-between gap-2">
                  <a href="https://smithery.ai" target="_blank" class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate hover:text-black dark:hover:text-white flex items-center space-x-1">
                    <span>Smithery MCP Registry</span>
                    <i data-lucide="external-link" class="w-2.5 h-2.5 inline-block"></i>
                  </a>
                  <span class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 font-semibold shrink-0">SLA 99.7%</span>
                </div>
                <h4 class="font-bold text-xs text-black dark:text-white leading-snug">Global Cross-Platform Sentiment Radar</h4>
                <p class="text-[11px] text-neutral-500 leading-relaxed">Multi-lingual social signal extraction (X/Twitter, Reddit, Telegram, Farcaster) with FinBERT scoring.</p>
                <div class="flex flex-wrap gap-1 pt-1">
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Social sentiment</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">FUD / FOMO index</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Whale tracking</span>
                </div>
              </div>
              <div class="pt-3 border-t border-neutral-200/60 dark:border-neutral-800 flex items-center justify-between gap-2">
                <div>
                  <span class="text-[9px] text-neutral-400 block font-mono">Micro-Task Rate</span>
                  <span class="font-bold text-xs text-black dark:text-white font-mono">$0.0040 USDT</span>
                </div>
                <button class="hire-agent-btn px-3 py-1.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-[11px] font-semibold transition-all active:scale-98 cursor-pointer" data-agent-id="agent-smithery-sentiment-07">
                  Hire Agent
                </button>
              </div>
            </div>

            <!-- 6. Fetch.ai DEX Arbitrage Sentinel -->
            <div class="agent-market-card p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 hover:border-black dark:hover:border-white transition-all flex flex-col justify-between space-y-3" data-category="automation">
              <div class="space-y-2">
                <div class="flex items-start justify-between gap-2">
                  <a href="https://agentverse.ai" target="_blank" class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate hover:text-black dark:hover:text-white flex items-center space-x-1">
                    <span>Fetch.ai uAgents Protocol</span>
                    <i data-lucide="external-link" class="w-2.5 h-2.5 inline-block"></i>
                  </a>
                  <span class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 font-semibold shrink-0">SLA 99.9%</span>
                </div>
                <h4 class="font-bold text-xs text-black dark:text-white leading-snug">DEX Cross-Pool Liquidity & Flash Arbitrage Sentinel</h4>
                <p class="text-[11px] text-neutral-500 leading-relaxed">Continuous monitoring of Raydium, Orca, and Meteora pools for triangular arbitrage and impermanent loss risks.</p>
                <div class="flex flex-wrap gap-1 pt-1">
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Solana DEX routing</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Slippage model</span>
                  <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-neutral-800 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-700/60">Pool health</span>
                </div>
              </div>
              <div class="pt-3 border-t border-neutral-200/60 dark:border-neutral-800 flex items-center justify-between gap-2">
                <div>
                  <span class="text-[9px] text-neutral-400 block font-mono">Micro-Task Rate</span>
                  <span class="font-bold text-xs text-black dark:text-white font-mono">$0.0080 USDT</span>
                </div>
                <button class="hire-agent-btn px-3 py-1.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-[11px] font-semibold transition-all active:scale-98 cursor-pointer" data-agent-id="agent-fetch-arbitrage-11">
                  Hire Agent
                </button>
              </div>
            </div>
'''

LIVE_HEADER_TELEMETRY = '''            <!-- Direct Global Market Outbound Hub Links -->
            <div class="flex flex-wrap items-center gap-1.5 text-[10px] font-mono">
              <a href="https://smithery.ai" target="_blank" class="px-2.5 py-1 rounded-xl bg-neutral-100 hover:bg-black hover:text-white dark:bg-neutral-900/60 dark:hover:bg-white dark:hover:text-black border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-300 transition-all flex items-center space-x-1">
                <span>Smithery (2,140+ Nodes)</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
              <a href="https://agentverse.ai" target="_blank" class="px-2.5 py-1 rounded-xl bg-neutral-100 hover:bg-black hover:text-white dark:bg-neutral-900/60 dark:hover:bg-white dark:hover:text-black border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-300 transition-all flex items-center space-x-1">
                <span>Fetch.ai (850+ Agents)</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
              <a href="https://glama.ai/mcp/servers" target="_blank" class="px-2.5 py-1 rounded-xl bg-neutral-100 hover:bg-black hover:text-white dark:bg-neutral-900/60 dark:hover:bg-white dark:hover:text-black border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-300 transition-all flex items-center space-x-1">
                <span>Glama (430+ Auditors)</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>'''

for filepath in ['dashboard.html', 'app/dashboard.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject Static Cards directly into HTML grid
    empty_grid_pattern = r'<div id="global-agent-market-grid"[^>]*>[\s\S]*?</div>'
    replacement_grid = f'<div id="global-agent-market-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3.5 pt-1">{STATIC_CARDS_HTML}\n          </div>'
    
    html = re.sub(empty_grid_pattern, replacement_grid, html, count=1)
    print(f"  Pre-rendered cards into {filepath}")

    # 2. Update Header Outbound links
    telemetry_pattern = r'<!-- Network Telemetry Badges -->[\s\S]*?</div>\s*</div>'
    # Let's replace the old telemetry badges with direct clickable outbound links
    old_badge_chunk = '<div class="flex flex-wrap items-center gap-1.5 text-[10px] font-mono">\n              <span class="px-2.5 py-1 rounded-xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400">\n                Smithery: <b>2,140+ Nodes</b>\n              </span>'
    if old_badge_chunk in html:
        old_full_chunk = '''            <!-- Network Telemetry Badges -->
            <div class="flex flex-wrap items-center gap-1.5 text-[10px] font-mono">
              <span class="px-2.5 py-1 rounded-xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400">
                Smithery: <b>2,140+ Nodes</b>
              </span>
              <span class="px-2.5 py-1 rounded-xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400">
                Fetch.ai: <b>850+ Agents</b>
              </span>
              <span class="px-2.5 py-1 rounded-xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400">
                Glama: <b>430+ Auditors</b>
              </span>
            </div>'''
        html = html.replace(old_full_chunk, LIVE_HEADER_TELEMETRY)
        print(f"  Replaced badges with interactive external links in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully updated {filepath}")

print("=== Pre-rendering Complete ===")
