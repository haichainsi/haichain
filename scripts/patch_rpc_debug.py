import os

files = ['_worker.js', 'app/_worker.js', 'server/haichain-mcp-worker.js', 'functions/api/mcp.js', 'functions/api/mcp/[[path]].js']

new_rpc_block = """let lastRpcDebug = 'INIT';

async function querySolanaRpc(method, params = []) {
  try {
    const res = await fetch(SOLANA_DEVNET_RPC, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      },
      body: JSON.stringify({
        jsonrpc: '2.0',
        id: 'haichain-mcp-' + Date.now(),
        method: method,
        params: params
      })
    });
    if (!res.ok) {
      lastRpcDebug = 'HTTP_' + res.status;
      return null;
    }
    const json = await res.json();
    if (json && json.result) {
      lastRpcDebug = 'OK_val_' + (typeof json.result.value !== 'undefined' ? json.result.value : JSON.stringify(json.result));
      return json.result;
    }
    lastRpcDebug = 'NO_RESULT_' + JSON.stringify(json);
    return null;
  } catch (err) {
    lastRpcDebug = 'ERR_' + (err.message || String(err));
    return null;
  }
}"""

for fp in files:
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    start_str = "async function querySolanaRpc(method, params = []) {"
    end_str = "// Tool Implementation: get_spending_pot_balance"
    
    if start_str in content and end_str in content:
        start_idx = content.index(start_str)
        end_idx = content.index(end_str)
        content = content[:start_idx] + new_rpc_block + "\n\n" + content[end_idx:]
        
        if '"verificationProof": "Confirmed on Solana L1 Kernel via Cryptographic Merkle Root"' in content and '"rpcDebug"' not in content:
            content = content.replace(
                '"verificationProof": "Confirmed on Solana L1 Kernel via Cryptographic Merkle Root"',
                '"rpcDebug": lastRpcDebug,\n  "verificationProof": "Confirmed on Solana L1 Kernel via Cryptographic Merkle Root"'
            )
            
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated:", fp)
    else:
        print("Markers not found in:", fp)
