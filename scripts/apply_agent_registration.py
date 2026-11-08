import os

relayer_path = 'server/production-agent-relayer.js'

with open(relayer_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Normalize
code = code.replace('\r\n', '\n')

# Add dynamic agents loader in constructor
old_ctor = """    // Load Real Funded Solana Devnet Keypair
    this.payerKeypair = this.loadPayerKeypair();
  }"""

new_ctor = """    // Load Real Funded Solana Devnet Keypair
    this.payerKeypair = this.loadPayerKeypair();
    this.dynamicAgentsFile = path.join(__dirname, 'dynamic-agents.json');
    this.allAgents = this.loadAllAgents();
  }

  loadAllAgents() {
    let custom = [];
    try {
      if (fs.existsSync(this.dynamicAgentsFile)) {
        custom = JSON.parse(fs.readFileSync(this.dynamicAgentsFile, 'utf8'));
      }
    } catch (e) {
      console.warn('[Relayer] Error reading dynamic-agents.json:', e.message);
    }
    return [...GLOBAL_AGENT_REGISTRY, ...custom];
  }

  registerCommunityAgent(agentData) {
    const { name, category, description, pricingUsdt, recipientAddress, endpointUrl, capabilities } = agentData;
    if (!name || name.trim().length < 3) throw new Error('Agent name must be at least 3 characters');
    if (!recipientAddress) throw new Error('Recipient Solana address is required');
    
    // Validate Base58
    try {
      new PublicKey(recipientAddress);
    } catch (e) {
      throw new Error('Invalid Solana Base58 recipient address: ' + recipientAddress);
    }

    const price = Math.max(0.001, parseFloat(pricingUsdt || '0.003'));
    const newAgent = {
      agentId: `agent-community-${Date.now().toString(36)}-${Math.floor(Math.random()*900+100)}`,
      name: name.trim(),
      provider: 'Community Decentralized Agent Node',
      category: category || 'custom',
      pricingUsdt: price,
      slaUptime: '99.5%',
      description: description ? description.trim() : 'External community autonomous service node',
      recipientAddress: recipientAddress.trim(),
      endpointUrl: endpointUrl ? endpointUrl.trim() : null,
      capabilities: Array.isArray(capabilities) ? capabilities : ['Autonomous API Task', 'HTTP 402 Settlement'],
      registeredAt: new Date().toISOString(),
      isCommunityVerified: true
    };

    let existing = [];
    try {
      if (fs.existsSync(this.dynamicAgentsFile)) {
        existing = JSON.parse(fs.readFileSync(this.dynamicAgentsFile, 'utf8'));
      }
    } catch (_) {}

    existing.push(newAgent);
    fs.writeFileSync(this.dynamicAgentsFile, JSON.stringify(existing, null, 2), 'utf8');
    this.allAgents = [...GLOBAL_AGENT_REGISTRY, ...existing];
    return newAgent;
  }"""

if old_ctor in code:
    code = code.replace(old_ctor, new_ctor)
    print("SUCCESS: Added dynamic agent loader and registerCommunityAgent method")
else:
    print("WARNING: old_ctor not matched")

# Update discover_global_agents to use this.allAgents
code = code.replace("const enriched = GLOBAL_AGENT_REGISTRY.map(a => ({", "const enriched = (this.allAgents || GLOBAL_AGENT_REGISTRY).map(a => ({")

# Add HTTP routes for /api/agents and /api/agents/register
route_hook = """      // API: Direct Agent Dispatch & Settlement
      if (url.pathname === '/api/relayer/dispatch' && req.method === 'POST') {"""

new_routes = """      // API: Community Agent Discovery & Registration
      if (url.pathname === '/api/agents' && req.method === 'GET') {
        res.writeHead(200, { ...cors, 'Content-Type': 'application/json' });
        return res.end(JSON.stringify({
          agents: this.allAgents || GLOBAL_AGENT_REGISTRY,
          count: (this.allAgents || GLOBAL_AGENT_REGISTRY).length,
          timestamp: new Date().toISOString()
        }));
      }

      if (url.pathname === '/api/agents/register' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', () => {
          try {
            const parsed = JSON.parse(body || '{}');
            const registered = this.registerCommunityAgent(parsed);
            res.writeHead(201, { ...cors, 'Content-Type': 'application/json' });
            res.end(JSON.stringify({
              success: true,
              message: 'Community agent registered successfully and active in HAIChain Registry',
              agent: registered,
              totalAgentsActive: this.allAgents.length
            }));
          } catch (err) {
            res.writeHead(400, { ...cors, 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: false, error: err.message }));
          }
        });
        return;
      }

      // API: Direct Agent Dispatch & Settlement
      if (url.pathname === '/api/relayer/dispatch' && req.method === 'POST') {"""

if route_hook in code:
    code = code.replace(route_hook, new_routes)
    print("SUCCESS: Added /api/agents and /api/agents/register endpoints")
else:
    print("WARNING: route_hook not matched")

with open(relayer_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Agent registration implementation completed.")
