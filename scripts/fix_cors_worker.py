for p in ['_worker.js', 'app/_worker.js']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    old = """    if (url.pathname === '/api/agents/marketplace') {
      const q = url.searchParams.get('q') || '';
      const cat = url.searchParams.get('category') || 'all';
      const maxP = parseFloat(url.searchParams.get('maxPrice') || '0.05');
      const data = await handleDiscoverGlobalAgents({ query: q, category: cat, maxPriceUsdt: maxP });
      return new Response(JSON.stringify(data), {
        status: 200,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }"""
    new = """    if (url.pathname === '/api/agents/marketplace') {
      const cors = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, HEAD',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization, x-api-key, mcp-session-id, last-event-id, accept, x-haichain-vault, x-vault'
      };
      if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });
      const q = url.searchParams.get('q') || '';
      const cat = url.searchParams.get('category') || 'all';
      const maxP = parseFloat(url.searchParams.get('maxPrice') || '0.05');
      const data = await handleDiscoverGlobalAgents({ query: q, category: cat, maxPriceUsdt: maxP });
      return new Response(JSON.stringify(data), {
        status: 200,
        headers: { ...cors, 'Content-Type': 'application/json' }
      });
    }"""
    if old in c:
        c = c.replace(old, new)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'Fixed cors in {p}')
