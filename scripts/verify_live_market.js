async function check() {
  const url = `https://haichain.si/dashboard?t=${Date.now()}`;
  const res = await fetch(url);
  const text = await res.text();
  console.log({
    status: res.status,
    len: text.length,
    hasSmitheryLink: text.includes('https://smithery.ai'),
    hasAgentverseLink: text.includes('https://agentverse.ai'),
    hasGlamaLink: text.includes('https://glama.ai/mcp/servers'),
    hasGrid: text.includes('global-agent-market-grid'),
    hasPreRenderedCards: text.includes('agent-smithery-scraper-01')
  });
}

check();
