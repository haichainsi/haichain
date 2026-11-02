# -*- coding: utf-8 -*-
import os, sys, shutil

# 1. Fix server/haichain-mcp-worker.js
worker_path = 'server/haichain-mcp-worker.js'
with open(worker_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """export default {
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

new_block = """export default {
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

if old_block in content:
    content = content.replace(old_block, new_block)
    with open(worker_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed routing in {worker_path}')
else:
    print(f'Warning: old_block not found in {worker_path}')

# 2. Move root wrangler.toml to server/wrangler.toml
if os.path.exists('wrangler.toml'):
    server_wrangler = """name = "haichain-mcp"
main = "haichain-mcp-worker.js"
compatibility_date = "2024-09-01"

[observability]
enabled = true
"""
    with open('server/wrangler.toml', 'w', encoding='utf-8') as f:
        f.write(server_wrangler)
    os.remove('wrangler.toml')
    print('Moved wrangler.toml to server/wrangler.toml')

# 3. Ensure _routes.json exists in root and app/
routes_json = """{
  "version": 1,
  "include": [
    "/api/*",
    "/sse"
  ],
  "exclude": []
}
"""
for p in ['_routes.json', 'app/_routes.json']:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(routes_json)
    print(f'Ensured {p}')

print('All routing fixes applied successfully.')
