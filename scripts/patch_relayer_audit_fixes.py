with open('server/production-agent-relayer.js', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add net and dns imports
old_imports = "const https = require('https');"
new_imports = """const https = require('https');
const net = require('net');
const dns = require('dns').promises;

// ============================================================================
// HARDENED SSRF BLOCKLIST (IPv4 + IPv6 + CGNAT + Benchmark + Loopbacks)
// ============================================================================
const ssrfBlockList = new net.BlockList();
ssrfBlockList.addSubnet('127.0.0.0', 8, 'ipv4');
ssrfBlockList.addAddress('::1', 'ipv6');
ssrfBlockList.addAddress('::', 'ipv6');
ssrfBlockList.addSubnet('::ffff:127.0.0.0', 104, 'ipv6');
ssrfBlockList.addSubnet('10.0.0.0', 8, 'ipv4');
ssrfBlockList.addSubnet('172.16.0.0', 12, 'ipv4');
ssrfBlockList.addSubnet('192.168.0.0', 16, 'ipv4');
ssrfBlockList.addSubnet('169.254.0.0', 16, 'ipv4');
ssrfBlockList.addSubnet('fe80::', 10, 'ipv6');
ssrfBlockList.addSubnet('100.64.0.0', 10, 'ipv4');
ssrfBlockList.addSubnet('198.18.0.0', 15, 'ipv4');
ssrfBlockList.addSubnet('fc00::', 7, 'ipv6');
ssrfBlockList.addSubnet('0.0.0.0', 8, 'ipv4');
ssrfBlockList.addSubnet('240.0.0.0', 4, 'ipv4');

// In-Memory Rate Limiting for SAFT / Email Endpoints (Sliding window: 5 requests / 15 mins)
const saftIpRateMap = new Map();
function checkSaftRateLimit(ip) {
  const now = Date.now();
  const windowMs = 15 * 60 * 1000;
  const maxReqs = 5;
  const history = (saftIpRateMap.get(ip) || []).filter(ts => now - ts < windowMs);
  if (history.length >= maxReqs) return false;
  history.push(now);
  saftIpRateMap.set(ip, history);
  return true;
}

function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str).replace(/[&<>"']/g, m => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  })[m]);
}"""

assert old_imports in c, "Could not find imports in server/production-agent-relayer.js"
c = c.replace(old_imports, new_imports, 1)

# 2. Replace validateOutboundUrl with async hardened version
p_start = c.indexOf('function validateOutboundUrl(targetUrl) {') if hasattr(c, 'indexOf') else c.find('function validateOutboundUrl(targetUrl) {')
p_end = c.find('const GLOBAL_AGENT_REGISTRY = [')
assert p_start != -1 and p_end != -1, "Could not locate validateOutboundUrl block"

old_ssrf_fn = c[p_start:p_end]

new_ssrf_fn = """async function validateOutboundUrl(targetUrl) {
  let parsed;
  try {
    parsed = new URL(targetUrl);
  } catch (e) {
    throw new Error(`Invalid URL: ${e.message}`);
  }

  // Allow https (and http for local test suites only if explicitly allowed)
  if (parsed.protocol !== 'https:' && parsed.protocol !== 'http:') {
    throw new Error(`SSRF Blocked: Invalid protocol ${parsed.protocol}`);
  }

  const rawHost = parsed.hostname.toLowerCase();
  const cleanHost = rawHost.replace(/\\.$/, '').replace(/^\\[|\\]$/g, '');

  if (cleanHost === 'localhost' || cleanHost.endsWith('.localhost') || cleanHost.endsWith('.local') || cleanHost.endsWith('.internal')) {
    throw new Error('SSRF Blocked: Local host alias is forbidden');
  }

  if (net.isIP(cleanHost)) {
    const type = net.isIPv6(cleanHost) ? 'ipv6' : 'ipv4';
    if (ssrfBlockList.check(cleanHost, type)) {
      throw new Error(`SSRF Blocked: IP ${cleanHost} is in prohibited subnet/private range`);
    }
    if (type === 'ipv6' && cleanHost.startsWith('::ffff:')) {
      const v4Part = cleanHost.slice(7);
      if (net.isIPv4(v4Part) && ssrfBlockList.check(v4Part, 'ipv4')) {
        throw new Error(`SSRF Blocked: IPv4-mapped IPv6 ${cleanHost} targets private range`);
      }
    }
  } else {
    try {
      const addresses = await dns.lookup(cleanHost, { all: true });
      if (!addresses || addresses.length === 0) {
        throw new Error('SSRF Blocked: DNS resolution yielded no addresses');
      }
      for (const record of addresses) {
        const ip = record.address;
        const type = record.family === 6 ? 'ipv6' : 'ipv4';
        if (ssrfBlockList.check(ip, type)) {
          throw new Error(`SSRF Blocked: Resolved IP ${ip} for ${cleanHost} is prohibited`);
        }
        if (type === 'ipv6' && ip.toLowerCase().startsWith('::ffff:')) {
          const v4Part = ip.slice(7);
          if (net.isIPv4(v4Part) && ssrfBlockList.check(v4Part, 'ipv4')) {
            throw new Error(`SSRF Blocked: Resolved IPv4-mapped IPv6 ${ip} for ${cleanHost} is prohibited`);
          }
        }
      }
    } catch (dnsErr) {
      if (dnsErr.message.includes('SSRF Blocked')) throw dnsErr;
      throw new Error(`SSRF Blocked: DNS resolution failed for ${cleanHost}: ${dnsErr.message}`);
    }
  }

  return parsed.href;
}

"""

c = c[:p_start] + new_ssrf_fn + c[p_end:]

# 3. Update callAgentTask and dispatchTask to await validateOutboundUrl and use redirect: 'manual'
c = c.replace('validateOutboundUrl(agent.endpointUrl);', 'await validateOutboundUrl(agent.endpointUrl);')
c = c.replace('const fetchUrl = validateOutboundUrl(rawUrl);', 'const fetchUrl = await validateOutboundUrl(rawUrl);')

# 4. Add redirect: 'manual' to fetch options
c = c.replace("let resp = await fetch(agent.endpointUrl, {\n        method: 'POST',", "let resp = await fetch(agent.endpointUrl, {\n        method: 'POST',\n        redirect: 'manual',")
c = c.replace("const retryResp = await fetch(agent.endpointUrl, {\n          method: 'POST',", "const retryResp = await fetch(agent.endpointUrl, {\n          method: 'POST',\n          redirect: 'manual',")
c = c.replace("const response = await fetch(fetchUrl, {\n          signal: controller.signal,", "const response = await fetch(fetchUrl, {\n          signal: controller.signal,\n          redirect: 'manual',")

# 5. Sanitize /api/saft/submit
old_saft_handler = """            const contractId = data.contractId || ('SAFT-HAI-' + Math.random().toString(36).substring(2, 7).toUpperCase());
            const name = data.name || 'Anonymous Investor';
            const email = data.email || '';
            const amount = Number(data.amount) || 0;
            const tokens = Number(data.tokens) || Math.floor(amount / 0.007);
            const wallet = data.wallet || 'N/A';
            const treasury = data.treasury || DEFAULT_TREASURY;
            const timestamp = data.timestamp || new Date().toISOString();
            const hashHex = data.hashHex || 'N/A';"""

new_saft_handler = """            const clientIp = (req.headers['x-forwarded-for'] || req.socket.remoteAddress || '127.0.0.1').split(',')[0].trim();
            if (!checkSaftRateLimit(clientIp)) {
              res.writeHead(429, { 'Content-Type': 'application/json' });
              return res.end(JSON.stringify({ error: 'Too Many Requests: Rate limit exceeded (5 requests per 15 mins)' }));
            }

            const rawEmail = (data.email || '').trim();
            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
            if (!rawEmail || !emailRegex.test(rawEmail) || rawEmail.length > 100 || rawEmail.includes('\\r') || rawEmail.includes('\\n')) {
              res.writeHead(400, { 'Content-Type': 'application/json' });
              return res.end(JSON.stringify({ error: 'Invalid email address provided' }));
            }

            const contractId = escapeHtml(data.contractId || ('SAFT-HAI-' + Math.random().toString(36).substring(2, 7).toUpperCase()));
            const name = escapeHtml(data.name || 'Anonymous Investor').slice(0, 100);
            const email = rawEmail;
            const amount = Math.min(Math.max(Number(data.amount) || 0, 0), 10000000);
            const tokens = Number(data.tokens) || Math.floor(amount / 0.007);
            const wallet = escapeHtml(data.wallet || 'N/A').slice(0, 64);
            const treasury = DEFAULT_TREASURY;
            const timestamp = new Date().toISOString();
            const hashHex = escapeHtml(data.hashHex || 'N/A').slice(0, 64);"""

assert old_saft_handler in c, "Could not find old_saft_handler"
c = c.replace(old_saft_handler, new_saft_handler, 1)

# Prevent caller-supplied arbitrary HTML in /api/saft/submit
c = c.replace("let adminHtml = data.adminHtml;", "let adminHtml = null; // Enforce strict server-side template only")
c = c.replace("let investorHtml = data.investorHtml;", "let investorHtml = null; // Enforce strict server-side template only")

with open('server/production-agent-relayer.js', 'w', encoding='utf-8') as f:
    f.write(c)

print("Successfully applied relayer security audit fixes to server/production-agent-relayer.js")
