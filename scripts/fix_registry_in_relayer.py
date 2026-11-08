import re

with open('server/production-agent-relayer.js', 'r', encoding='utf-8') as f:
    code = f.read()

registry_code = '''
const GLOBAL_AGENT_REGISTRY = [
  {
    agentId: "agent-smithery-scraper-01",
    name: "Smithery Web Extraction Sentinel",
    provider: "Smithery MCP Registry",
    category: "data_extraction",
    pricingUsdt: 0.003,
    slaUptime: "99.9%",
    description: "Autonomous headless browser crawling, dynamic SPA scraping, and structured JSON extraction.",
    recipientAddress: "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3",
    capabilities: ["Headless Chromium scraping", "Anti-bot bypass", "PDF/Table to JSON parsing"],
  },
  {
    agentId: "agent-fetch-market-intel-04",
    name: "Fetch.ai Autonomous Financial Sentinel",
    provider: "Fetch.ai Almanac Network",
    category: "financial_intelligence",
    pricingUsdt: 0.005,
    slaUptime: "99.8%",
    description: "Real-time cryptocurrency orderbook depth, on-chain whale flow tracking, and macro sentiment analysis.",
    recipientAddress: "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3",
    capabilities: ["CEX/DEX Liquidity Scans", "Tokenomics audit", "Volatility forecast"],
  },
  {
    agentId: "agent-glama-sec-audit-09",
    name: "Glama Solana / Rust Security Auditor",
    provider: "Glama Verified Security Network",
    category: "security_audit",
    pricingUsdt: 0.010,
    slaUptime: "99.95%",
    description: "Static and symbolic execution analysis for Solana Anchor programs, reentrancy detection, and PDA validation.",
    recipientAddress: "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3",
    capabilities: ["Anchor Rust vulnerability scan", "PDA seed collision check", "Arithmetic overflow verification"],
  },
  {
    agentId: "agent-haichain-code-sandbox-02",
    name: "HAICHAIN Ephemeral WASM Sandbox Node",
    provider: "HAICHAIN TEE Compute Cloud",
    category: "automation",
    pricingUsdt: 0.002,
    slaUptime: "100.0%",
    description: "Isolated, hardware-secure TEE sandbox for Python, JavaScript, and Rust script compilation & execution.",
    recipientAddress: "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3",
    capabilities: ["Python 3.12 execution", "Data transformation", "KaTeX / Graph generation"],
  },
  {
    agentId: "agent-smithery-sentiment-07",
    name: "Global Cross-Platform Sentiment Radar",
    provider: "Smithery MCP Registry",
    category: "financial_intelligence",
    pricingUsdt: 0.004,
    slaUptime: "99.7%",
    description: "Multi-lingual social signal extraction (X/Twitter, Reddit, Telegram, Farcaster) with FinBERT scoring.",
    recipientAddress: "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3",
    capabilities: ["Social sentiment quantification", "FUD / FOMO index detection", "Influencer signal tracking"],
  },
  {
    agentId: "agent-fetch-arbitrage-11",
    name: "DEX Cross-Pool Liquidity & Flash Arbitrage Sentinel",
    provider: "Fetch.ai uAgents Protocol",
    category: "automation",
    pricingUsdt: 0.008,
    slaUptime: "99.9%",
    description: "Continuous monitoring of Raydium, Orca, and Meteora pools for triangular arbitrage and impermanent loss risks.",
    recipientAddress: "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3",
    capabilities: ["Solana DEX routing analysis", "Slippage minimization modeling", "Pool health scoring"],
  },
];
'''

if 'const GLOBAL_AGENT_REGISTRY' not in code:
    code = code.replace("const DEFAULT_TREASURY = '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';", "const DEFAULT_TREASURY = '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';\n" + registry_code)
    with open('server/production-agent-relayer.js', 'w', encoding='utf-8') as f:
        f.write(code)
    print("SUCCESS: Injected GLOBAL_AGENT_REGISTRY into production-agent-relayer.js")
else:
    print("ALREADY EXISTS")
