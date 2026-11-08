import re

with open('_worker.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Define top-level corsHeaders
top_cors = """// Universal CORS Headers
const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, HEAD',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization, x-api-key, mcp-session-id, last-event-id, accept',
  'Access-Control-Max-Age': '86400'
};

// Global in-memory Edge cache for referral click telemetry
const globalReferralTelemetry = new Map();
"""

# Replace first occurrence of async function handleMcpRequest
if "const corsHeaders = {" in code:
    # Remove the local declaration or let it be shadowed/reassigned
    code = code.replace("async function handleMcpRequest(request) {", top_cors + "\nasync function handleMcpRequest(request) {", 1)

# Referral Handlers
referral_handlers = """
// ==============================================================================
// HAICHAIN REFERRAL CLICK TRACKING & TRAFFIC ANALYTICS EDGE ENGINE
// ==============================================================================
async function handleReferralClick(request, env, ctx) {
  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders });
  }
  if (request.method !== 'POST') {
    return new Response('Method Not Allowed', { status: 405, headers: corsHeaders });
  }

  try {
    const payload = await request.json();
    const rawRef = (payload.ref || payload.referrer || payload.inviter || '').trim();
    if (!rawRef || rawRef.length < 4 || rawRef.length > 64) {
      return new Response(JSON.stringify({ error: 'Invalid referral wallet' }), {
        status: 400,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }

    const cleanRef = rawRef.toLowerCase();
    const source = (payload.source || 'Direct / Private Chat').slice(0, 50);
    const device = (payload.device || 'Desktop').slice(0, 20);
    const medium = (payload.medium || '').slice(0, 30);
    const campaign = (payload.campaign || '').slice(0, 30);
    const country = request.headers.get('cf-ipcountry') || 'Global';
    const isUnique = Boolean(payload.isUnique);
    const timestamp = Number(payload.timestamp) || Date.now();

    // 1. Fetch or initialize edge telemetry
    let stats = globalReferralTelemetry.get(cleanRef);
    if (!stats) {
      stats = {
        ref: rawRef,
        totalClicks: 0,
        uniqueClicks: 0,
        sources: {},
        devices: { Mobile: 0, Desktop: 0 },
        countries: {},
        recentClicks: []
      };
    }

    stats.totalClicks = (stats.totalClicks || 0) + 1;
    if (isUnique) {
      stats.uniqueClicks = (stats.uniqueClicks || 0) + 1;
    } else if (!stats.uniqueClicks) {
      stats.uniqueClicks = 1;
    }

    stats.sources[source] = (stats.sources[source] || 0) + 1;
    stats.devices[device] = (stats.devices[device] || 0) + 1;
    if (country) {
      stats.countries[country] = (stats.countries[country] || 0) + 1;
    }

    stats.recentClicks.unshift({
      timestamp,
      source,
      device,
      medium,
      campaign,
      country
    });
    if (stats.recentClicks.length > 25) {
      stats.recentClicks.pop();
    }

    globalReferralTelemetry.set(cleanRef, stats);

    // 2. Cache API persistence across Edge instances
    if (typeof caches !== 'undefined' && caches.default) {
      try {
        const cache = caches.default;
        const cacheUrl = `https://haichain.si/api/referral/cache/${encodeURIComponent(cleanRef)}`;
        const cacheKey = new Request(cacheUrl);
        const cacheRes = new Response(JSON.stringify(stats), {
          headers: {
            'Content-Type': 'application/json',
            'Cache-Control': 'public, max-age=2592000'
          }
        });
        if (ctx && ctx.waitUntil) {
          ctx.waitUntil(cache.put(cacheKey, cacheRes));
        } else {
          await cache.put(cacheKey, cacheRes);
        }
      } catch (cacheErr) {
        console.warn('[Referral Edge] Cache put error:', cacheErr);
      }
    }

    // 3. KV binding persistence if configured
    if (env && env.REFERRAL_KV) {
      try {
        if (ctx && ctx.waitUntil) {
          ctx.waitUntil(env.REFERRAL_KV.put('ref:' + cleanRef, JSON.stringify(stats)));
        } else {
          await env.REFERRAL_KV.put('ref:' + cleanRef, JSON.stringify(stats));
        }
      } catch (kvErr) {
        console.warn('[Referral Edge] KV put error:', kvErr);
      }
    }

    return new Response(JSON.stringify({
      success: true,
      ref: rawRef,
      totalClicks: stats.totalClicks,
      uniqueClicks: stats.uniqueClicks,
      sources: stats.sources
    }), {
      status: 200,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message || 'Internal Server Error' }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }
}

async function handleReferralStats(request, env, ctx) {
  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders });
  }

  const url = new URL(request.url);
  const rawRef = (url.searchParams.get('ref') || url.searchParams.get('wallet') || '').trim();

  if (!rawRef || rawRef.length < 4) {
    return new Response(JSON.stringify({ error: 'Missing or invalid ref parameter' }), {
      status: 400,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  const cleanRef = rawRef.toLowerCase();
  let stats = globalReferralTelemetry.get(cleanRef);

  // Check Cache API if not in memory
  if (!stats && typeof caches !== 'undefined' && caches.default) {
    try {
      const cache = caches.default;
      const cacheUrl = `https://haichain.si/api/referral/cache/${encodeURIComponent(cleanRef)}`;
      const match = await cache.match(new Request(cacheUrl));
      if (match) {
        stats = await match.json();
        globalReferralTelemetry.set(cleanRef, stats);
      }
    } catch (_) {}
  }

  // Check KV binding if available
  if (!stats && env && env.REFERRAL_KV) {
    try {
      const kvVal = await env.REFERRAL_KV.get('ref:' + cleanRef, 'json');
      if (kvVal) {
        stats = kvVal;
        globalReferralTelemetry.set(cleanRef, stats);
      }
    } catch (_) {}
  }

  if (!stats) {
    stats = {
      ref: rawRef,
      totalClicks: 0,
      uniqueClicks: 0,
      sources: {},
      devices: { Mobile: 0, Desktop: 0 },
      countries: {},
      recentClicks: []
    };
  }

  return new Response(JSON.stringify(stats), {
    status: 200,
    headers: {
      ...corsHeaders,
      'Content-Type': 'application/json',
      'Cache-Control': 'public, max-age=5, s-maxage=5'
    }
  });
}
"""

# Insert referral handlers before `export default {`
target = "export default {"
replacement = referral_handlers + "\nexport default {"
code = code.replace(target, replacement, 1)

# In export default fetch:
fetch_router_target = """    // Only handle MCP API and SSE protocol endpoints
    if (url.pathname === '/api/mcp' || url.pathname.startsWith('/api/mcp/') || url.pathname === '/sse') {
      return await handleMcpRequest(request);
    }"""

fetch_router_replacement = """    // Referral Click Telemetry & Analytics API
    if (url.pathname === '/api/referral/click') {
      return await handleReferralClick(request, env, ctx);
    }
    if (url.pathname === '/api/referral/stats') {
      return await handleReferralStats(request, env, ctx);
    }

    // Only handle MCP API and SSE protocol endpoints
    if (url.pathname === '/api/mcp' || url.pathname.startsWith('/api/mcp/') || url.pathname === '/sse') {
      return await handleMcpRequest(request);
    }"""

code = code.replace(fetch_router_target, fetch_router_replacement, 1)

# Write to both _worker.js and app/_worker.js
with open('_worker.js', 'w', encoding='utf-8') as f:
    f.write(code)

with open('app/_worker.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully patched _worker.js and app/_worker.js!")
