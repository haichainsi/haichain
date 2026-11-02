// functions/api/wallet-relay.js
// Cloudflare Pages Function for Cross-Browser/Mobile Wallet Handshake Sync
const memorySessions = new Map();

export async function onRequest(context) {
  const { request } = context;
  const url = new URL(request.url);

  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Cache-Control": "no-cache, no-store, must-revalidate"
  };

  if (request.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  // GET /api/wallet-relay?id=...
  if (request.method === "GET") {
    const id = url.searchParams.get("id");
    if (!id) {
      return new Response(JSON.stringify({ error: "Missing session id" }), {
        status: 400,
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }

    const session = memorySessions.get(id);
    if (session) {
      return new Response(JSON.stringify({ success: true, connected: true, data: session }), {
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }

    return new Response(JSON.stringify({ success: true, connected: false }), {
      headers: { ...corsHeaders, "Content-Type": "application/json" }
    });
  }

  // POST /api/wallet-relay
  if (request.method === "POST") {
    try {
      const body = await request.json();
      if (!body.id || !body.address) {
        return new Response(JSON.stringify({ error: "Missing session id or address" }), {
          status: 400,
          headers: { ...corsHeaders, "Content-Type": "application/json" }
        });
      }

      memorySessions.set(body.id, {
        address: body.address,
        provider: body.provider || "MetaMask",
        balance: body.balance || null,
        timestamp: Date.now()
      });

      // Evict old entries
      if (memorySessions.size > 500) {
        const now = Date.now();
        for (const [k, v] of memorySessions.entries()) {
          if (now - v.timestamp > 600000) memorySessions.delete(k);
        }
      }

      return new Response(JSON.stringify({ success: true }), {
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    } catch (e) {
      return new Response(JSON.stringify({ error: e.message }), {
        status: 500,
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }
  }

  return new Response("Method not allowed", { status: 405, headers: corsHeaders });
}
