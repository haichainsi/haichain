# -*- coding: utf-8 -*-
import os, sys, json

# 1. Create _routes.json and app/_routes.json
routes_content = json.dumps({
    "version": 1,
    "include": [
        "/api/*",
        "/sse"
    ],
    "exclude": []
}, indent=2) + "\n"

for p in ['_routes.json', 'app/_routes.json']:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(routes_content)
    print(f'Created {p}')

# 2. Fix fetch handler in _worker.js and app/_worker.js
old_fetch = """export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === '/api/mcp' || url.pathname.startsWith('/api/mcp/') || url.pathname === '/') {
      return await handleMcpRequest(request);
    }
    if (env && env.ASSETS) {
      try {
        const res = await env.ASSETS.fetch(request);
        if (res.status !== 404) return res;
      } catch (_) {}
    }
    return await handleMcpRequest(request);
  }
};"""

new_fetch = """export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Only handle MCP API and SSE protocol endpoints
    if (url.pathname === '/api/mcp' || url.pathname.startsWith('/api/mcp/') || url.pathname === '/sse') {
      return await handleMcpRequest(request);
    }

    // Pass all web traffic directly to static assets (index.html, dashboard.html, assets, etc.)
    if (env && env.ASSETS) {
      return await env.ASSETS.fetch(request);
    }

    return new Response('Not Found', { status: 404 });
  }
};"""

for p in ['_worker.js', 'app/_worker.js']:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        if old_fetch in c:
            c = c.replace(old_fetch, new_fetch)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f'Fixed routing in {p}')
        else:
            print(f'Warning: old_fetch not found in {p}')

print('Routing fix applied successfully.')
