// Cloudflare Pages Function: /api/wallet-relay
// In-memory & Cache-based fast session relay for MetaMask mobile cross-browser handoff

export async function onRequest(context) {
  const { request } = context;
  const url = new URL(request.url);

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  const cache = caches.default;

  // POST: MetaMask posts wallet connection
  if (request.method === 'POST') {
    try {
      const data = await request.json();
      const sessId = data.sessId || data.sess_id;
      if (!sessId || !data.address) {
        return new Response(JSON.stringify({ error: 'Missing sessId or address' }), { status: 400, headers: corsHeaders });
      }

      const cacheKey = new Request(`https://haichain-relay.internal/sess/${sessId}`, { method: 'GET' });
      const payload = JSON.stringify({
        address: data.address,
        provider: data.provider || 'MetaMask',
        evmBalance: data.evmBalance || '0.0000',
        timestamp: Date.now()
      });

      const cacheResponse = new Response(payload, {
        headers: {
          'Content-Type': 'application/json',
          'Cache-Control': 'public, max-age=300'
        }
      });

      await cache.put(cacheKey, cacheResponse);
      return new Response(JSON.stringify({ success: true, sessId }), { status: 200, headers: corsHeaders });
    } catch (e) {
      return new Response(JSON.stringify({ error: e.message }), { status: 500, headers: corsHeaders });
    }
  }

  // GET: Chrome polls for wallet connection
  if (request.method === 'GET') {
    const sessId = url.searchParams.get('sess_id') || url.searchParams.get('sessId');
    if (!sessId) {
      return new Response(JSON.stringify({ error: 'Missing sess_id' }), { status: 400, headers: corsHeaders });
    }

    const cacheKey = new Request(`https://haichain-relay.internal/sess/${sessId}`, { method: 'GET' });
    const cached = await cache.match(cacheKey);

    if (cached) {
      const body = await cached.text();
      return new Response(body, { status: 200, headers: corsHeaders });
    } else {
      return new Response(JSON.stringify({ status: 'pending' }), { status: 200, headers: corsHeaders });
    }
  }

  return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405, headers: corsHeaders });
}
