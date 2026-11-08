import re

def fix_workers():
    # 1. Fix server/haichain-mcp-worker.js and server/cloud-mcp-functions/_mcp_handler.js
    for fpath in ['server/haichain-mcp-worker.js', 'server/cloud-mcp-functions/_mcp_handler.js']:
        print(f"Patching {fpath}...")
        with open(fpath, 'r', encoding='utf-8') as f:
            code = f.read()

        # Update fetch handler in standalone worker to route /api/vault/sync and /api/vault/balance
        old_fetch = '''    // Only handle MCP API and SSE protocol endpoints
    if (url.pathname === '/api/mcp' || url.pathname.startsWith('/api/mcp/') || url.pathname === '/sse') {
      return await handleMcpRequest(request);
    }'''
        new_fetch = '''    // Handle MCP API, SSE, and real-time Vault Balance Sync endpoints
    if (url.pathname === '/api/mcp' || url.pathname.startsWith('/api/mcp/') || url.pathname === '/sse' || url.pathname === '/api/vault/sync' || url.pathname === '/api/vault/balance') {
      return await handleMcpRequest(request, env, ctx);
    }'''
        if old_fetch in code:
            code = code.replace(old_fetch, new_fetch)
            print(f"Updated fetch route in {fpath}.")

        # Update handleMcpRequest signature to accept (request, env, ctx)
        code = code.replace('export async function handleMcpRequest(request) {', 'export async function handleMcpRequest(request, env = null, ctx = null) {')

        # Update /api/vault/sync in handleMcpRequest to also persist in KV if available
        old_sync_block = '''    if (v) {
      vaultBalanceRegistry.set(v, b);
      return new Response(JSON.stringify({ status: 'SYNCHRONIZED', vault: v, balance: b, timestamp: Date.now() }), {
        status: 200,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }'''
        new_sync_block = '''    if (v) {
      vaultBalanceRegistry.set(v, b);
      const kv = (env && (env.REFERRAL_KV || env.SAFT_KV || env.VAULT_KV));
      if (kv) {
        try {
          if (ctx && ctx.waitUntil) {
            ctx.waitUntil(kv.put('vault_bal:' + v, String(b)));
          } else {
            await kv.put('vault_bal:' + v, String(b));
          }
        } catch (_) {}
      }
      return new Response(JSON.stringify({ status: 'SYNCHRONIZED', vault: v, balance: b, timestamp: Date.now() }), {
        status: 200,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }'''
        if old_sync_block in code:
            code = code.replace(old_sync_block, new_sync_block)
            print(f"Updated sync block with KV support in {fpath}.")

        # Update handleGetSpendingPotBalance call to pass env
        code = code.replace(
            'return await handleGetSpendingPotBalance(args, boundVault, allocatedBal);',
            'return await handleGetSpendingPotBalance(args, boundVault, allocatedBal, env);'
        )

        # Update handleGetSpendingPotBalance signature and KV read
        code = code.replace(
            'async function handleGetSpendingPotBalance(args = {}, boundVault = \'\', allocatedBal = 0) {',
            'async function handleGetSpendingPotBalance(args = {}, boundVault = \'\', allocatedBal = 0, env = null) {'
        )

        old_reg_check = '''  // Check live synced balance from dashboard first
  let registryBal = null;
  if (targetAddress && vaultBalanceRegistry.has(targetAddress)) {
    registryBal = vaultBalanceRegistry.get(targetAddress);
  }'''
        new_reg_check = '''  // Check live synced balance from dashboard (memory cache + global KV)
  let registryBal = null;
  if (targetAddress) {
    if (vaultBalanceRegistry.has(targetAddress)) {
      registryBal = vaultBalanceRegistry.get(targetAddress);
    } else {
      const kv = (env && (env.REFERRAL_KV || env.SAFT_KV || env.VAULT_KV));
      if (kv) {
        try {
          const val = await kv.get('vault_bal:' + targetAddress);
          if (val !== null && !isNaN(parseFloat(val))) {
            registryBal = parseFloat(val);
            vaultBalanceRegistry.set(targetAddress, registryBal);
          }
        } catch (_) {}
      }
    }
  }'''
        if old_reg_check in code:
            code = code.replace(old_reg_check, new_reg_check)
            print(f"Updated registry check with KV read in {fpath}.")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"Done {fpath}.")

    # 2. Fix _worker.js and app/_worker.js
    for wpath in ['_worker.js', 'app/_worker.js']:
        print(f"Patching {wpath}...")
        with open(wpath, 'r', encoding='utf-8') as f:
            wcode = f.read()

        # Remove duplicate export default at lines 633-649
        duplicate_export = '''export default {
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

    return await fetch(request);
  }
};'''
        if duplicate_export in wcode:
            wcode = wcode.replace(duplicate_export, '// End of MCP Gateway module')
            print(f"Removed duplicate export default in {wpath}.")

        # Update main export default to route /api/vault/sync and /api/vault/balance
        old_main_mcp_route = '''    // Only handle MCP API and SSE protocol endpoints
    if (url.pathname === '/api/mcp' || url.pathname.startsWith('/api/mcp/') || url.pathname === '/sse') {
      return await handleMcpRequest(request);
    }'''
        new_main_mcp_route = '''    // Handle MCP API, SSE, and real-time Vault Balance Sync endpoints
    if (url.pathname === '/api/mcp' || url.pathname.startsWith('/api/mcp/') || url.pathname === '/sse' || url.pathname === '/api/vault/sync' || url.pathname === '/api/vault/balance') {
      return await handleMcpRequest(request, env, ctx);
    }'''
        if old_main_mcp_route in wcode:
            wcode = wcode.replace(old_main_mcp_route, new_main_mcp_route)
            print(f"Updated main export default routing in {wpath}.")

        # Update handleMcpRequest signature in _worker.js
        wcode = wcode.replace('export async function handleMcpRequest(request) {', 'export async function handleMcpRequest(request, env = null, ctx = null) {')

        # Update sync block in _worker.js
        old_sync_block = '''    if (v) {
      vaultBalanceRegistry.set(v, b);
      return new Response(JSON.stringify({ status: 'SYNCHRONIZED', vault: v, balance: b, timestamp: Date.now() }), {
        status: 200,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }'''
        new_sync_block = '''    if (v) {
      vaultBalanceRegistry.set(v, b);
      const kv = (env && (env.REFERRAL_KV || env.SAFT_KV || env.VAULT_KV));
      if (kv) {
        try {
          if (ctx && ctx.waitUntil) {
            ctx.waitUntil(kv.put('vault_bal:' + v, String(b)));
          } else {
            await kv.put('vault_bal:' + v, String(b));
          }
        } catch (_) {}
      }
      return new Response(JSON.stringify({ status: 'SYNCHRONIZED', vault: v, balance: b, timestamp: Date.now() }), {
        status: 200,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }'''
        if old_sync_block in wcode:
            wcode = wcode.replace(old_sync_block, new_sync_block)
            print(f"Updated sync block with KV in {wpath}.")

        # Update handleGetSpendingPotBalance call to pass env
        wcode = wcode.replace(
            'return await handleGetSpendingPotBalance(args, boundVault, allocatedBal);',
            'return await handleGetSpendingPotBalance(args, boundVault, allocatedBal, env);'
        )

        # Update handleGetSpendingPotBalance signature and KV read
        wcode = wcode.replace(
            'async function handleGetSpendingPotBalance(args = {}, boundVault = \'\', allocatedBal = 0) {',
            'async function handleGetSpendingPotBalance(args = {}, boundVault = \'\', allocatedBal = 0, env = null) {'
        )

        old_reg_check = '''  // Check live synced balance from dashboard first
  let registryBal = null;
  if (targetAddress && vaultBalanceRegistry.has(targetAddress)) {
    registryBal = vaultBalanceRegistry.get(targetAddress);
  }'''
        new_reg_check = '''  // Check live synced balance from dashboard (memory cache + global KV)
  let registryBal = null;
  if (targetAddress) {
    if (vaultBalanceRegistry.has(targetAddress)) {
      registryBal = vaultBalanceRegistry.get(targetAddress);
    } else {
      const kv = (env && (env.REFERRAL_KV || env.SAFT_KV || env.VAULT_KV));
      if (kv) {
        try {
          const val = await kv.get('vault_bal:' + targetAddress);
          if (val !== null && !isNaN(parseFloat(val))) {
            registryBal = parseFloat(val);
            vaultBalanceRegistry.set(targetAddress, registryBal);
          }
        } catch (_) {}
      }
    }
  }'''
        if old_reg_check in wcode:
            wcode = wcode.replace(old_reg_check, new_reg_check)
            print(f"Updated registry check in {wpath}.")

        with open(wpath, 'w', encoding='utf-8') as f:
            f.write(wcode)
        print(f"Done {wpath}.")

fix_workers()
