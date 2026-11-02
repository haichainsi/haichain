import os

files = ['server/haichain-mcp-worker.js', '_worker.js', 'app/_worker.js']

for fp in files:
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Update handleGetSpendingPotBalance signature & fallback
    old_get_bal = """async function handleGetSpendingPotBalance(args = {}) {
  const rawAddr = (args.vaultAddress || args.vault_address || args.walletAddress || args.wallet_address || args.address || args.account || '').trim();
  const isMasterVault = !rawAddr || rawAddr === MASTER_VAULT_PDA;
  const targetAddress = isMasterVault ? MASTER_VAULT_PDA : rawAddr;"""

    new_get_bal = """async function handleGetSpendingPotBalance(args = {}, boundVault = '') {
  const rawAddr = (args.vaultAddress || args.vault_address || args.walletAddress || args.wallet_address || args.address || args.account || (boundVault || '')).trim();
  const isMasterVault = (!rawAddr && !boundVault) || rawAddr === MASTER_VAULT_PDA;
  const targetAddress = isMasterVault ? MASTER_VAULT_PDA : (rawAddr || boundVault);"""

    if old_get_bal in code:
        code = code.replace(old_get_bal, new_get_bal)

    # 2. Update handleExecuteMicroPayment signature & sender
    old_exec_pay = """async function handleExecuteMicroPayment(args = {}) {
  const rawAmount = typeof args.amountUsdt === 'number' ? args.amountUsdt"""

    new_exec_pay = """async function handleExecuteMicroPayment(args = {}, boundVault = '') {
  const rawAmount = typeof args.amountUsdt === 'number' ? args.amountUsdt"""

    if old_exec_pay in code:
        code = code.replace(old_exec_pay, new_exec_pay)

    # In handleExecuteMicroPayment return:
    old_sender = "senderVault: MASTER_VAULT_PDA,"
    new_sender = "senderVault: (boundVault || MASTER_VAULT_PDA),"
    if old_sender in code:
        code = code.replace(old_sender, new_sender)

    # 3. Update handleTriggerEmergencyPanic signature & affectedVaults
    old_panic = """async function handleTriggerEmergencyPanic(args = {}) {"""
    new_panic = """async function handleTriggerEmergencyPanic(args = {}, boundVault = '') {"""
    if old_panic in code:
        code = code.replace(old_panic, new_panic)

    old_affected = """affectedVaults: [
      MASTER_VAULT_PDA
    ],"""
    new_affected = """affectedVaults: [
      boundVault || MASTER_VAULT_PDA
    ],"""
    if old_affected in code:
        code = code.replace(old_affected, new_affected)

    # 4. Update handleJsonRpc signature and tool dispatch
    old_jsonrpc = """async function handleJsonRpc(req) {"""
    new_jsonrpc = """async function handleJsonRpc(req, boundVault = '') {"""
    if old_jsonrpc in code:
        code = code.replace(old_jsonrpc, new_jsonrpc)

    # Inside handleJsonRpc initialize:
    old_init = """serverInfo: {
          name: 'HAICHAIN Autonomous Kernel MCP Gateway',
          version: '6.9.3'
        },
        instructions: 'HAICHAIN is the universal autonomous machine financial operating system on Solana. Use these tools to inspect agent spending pots, execute sub-cent micro-payments on Solana Devnet, and trigger the emergency panic circuit breaker.'"""

    new_init = """serverInfo: {
          name: 'HAICHAIN Autonomous Kernel MCP Gateway',
          version: '7.0.0 (Personalized 1-Click Vault)'
        },
        instructions: boundVault 
          ? `HAICHAIN Autonomous Machine Financial OS. DEDICATED PERSONALIZED SESSION bound to user vault: ${boundVault}. All balance inspections, micro-payments, and panic triggers automatically execute on this vault by default without needing to specify an address.`
          : 'HAICHAIN is the universal autonomous machine financial operating system on Solana. Use these tools to inspect agent spending pots, execute sub-cent micro-payments on Solana Devnet, and trigger the emergency panic circuit breaker.'"""

    if old_init in code:
        code = code.replace(old_init, new_init)

    # Tool calls inside handleJsonRpc:
    code = code.replace("handleGetSpendingPotBalance(toolArgs)", "handleGetSpendingPotBalance(toolArgs, boundVault)")
    code = code.replace("handleExecuteMicroPayment(toolArgs)", "handleExecuteMicroPayment(toolArgs, boundVault)")
    code = code.replace("handleTriggerEmergencyPanic(toolArgs)", "handleTriggerEmergencyPanic(toolArgs, boundVault)")

    # 5. In handleMcpRequest: extract boundVault and pass it
    old_mcp_req = """async function handleMcpRequest(request) {
  const url = new URL(request.url);"""

    new_mcp_req = """async function handleMcpRequest(request) {
  const url = new URL(request.url);
  const boundVault = (url.searchParams.get('vault') || 
                      url.searchParams.get('user') || 
                      url.searchParams.get('wallet') || 
                      url.searchParams.get('v') || '').trim();"""

    if old_mcp_req in code:
        code = code.replace(old_mcp_req, new_mcp_req)

    # Status payload in GET /api/mcp:
    old_status = """    const statusPayload = {
      status: 'ONLINE',
      gateway: 'HAICHAIN Cloud MCP Gateway',
      version: '6.9.5',"""

    new_status = """    const statusPayload = {
      status: 'ONLINE',
      gateway: 'HAICHAIN Cloud MCP Gateway',
      version: '7.0.0 (Personalized 1-Click Vault)',
      boundVault: boundVault || MASTER_VAULT_PDA,
      isPersonalized: !!boundVault,
      sessionType: boundVault ? 'PERSONALIZED_DEDICATED_VAULT' : 'PROTOCOL_MASTER_VAULT',
      ownerNotice: boundVault ? `This 1-click endpoint is dedicated to vault: ${boundVault}` : 'Protocol shared devnet gateway.',"""

    if old_status in code:
        code = code.replace(old_status, new_status)

    # POST dispatch: pass boundVault to handleJsonRpc
    code = code.replace("const res = await handleJsonRpc(item);", "const res = await handleJsonRpc(item, boundVault);")
    code = code.replace("const responsePayload = await handleJsonRpc(parsed);", "const responsePayload = await handleJsonRpc(parsed, boundVault);")

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Successfully patched:", fp)
