/**
 * HAICHAIN Cloudflare Pages Advanced Edge Worker v6.9.3
 * Serves:
 *   1. Cloud MCP Gateway (/api/mcp, /mcp, /sse) for Claude Mobile & Web
 *   2. Static Assets (Dashboard, Whitepaper, HTML, JS, CSS) via env.ASSETS
 */

import { handleMcpRequest } from './functions/_mcp_handler.js';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Route MCP endpoints directly to Cloud MCP Handler
    if (
      url.pathname === '/api/mcp' ||
      url.pathname === '/mcp' ||
      url.pathname === '/sse' ||
      url.pathname === '/api/sse' ||
      url.pathname.startsWith('/api/mcp/')
    ) {
      return await handleMcpRequest(request);
    }

    // Pass all other requests to static assets
    if (env.ASSETS && typeof env.ASSETS.fetch === 'function') {
      return await env.ASSETS.fetch(request);
    }

    return new Response('Asset Fetcher Unavailable', { status: 500 });
  }
};
