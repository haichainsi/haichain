const net = require('net');
const dns = require('dns').promises;

const blockList = new net.BlockList();
// Loopback IPv4 & IPv6
blockList.addSubnet('127.0.0.0', 8, 'ipv4');
blockList.addAddress('::1', 'ipv6');
blockList.addAddress('::', 'ipv6');
blockList.addSubnet('::ffff:127.0.0.0', 104, 'ipv6');

// RFC 1918 Private networks
blockList.addSubnet('10.0.0.0', 8, 'ipv4');
blockList.addSubnet('172.16.0.0', 12, 'ipv4');
blockList.addSubnet('192.168.0.0', 16, 'ipv4');

// Link-local / Cloud metadata
blockList.addSubnet('169.254.0.0', 16, 'ipv4');
blockList.addSubnet('fe80::', 10, 'ipv6');

// CGNAT / Benchmark
blockList.addSubnet('100.64.0.0', 10, 'ipv4');
blockList.addSubnet('198.18.0.0', 15, 'ipv4');

// IPv6 Unique Local
blockList.addSubnet('fc00::', 7, 'ipv6');
// IPv4 broadcast / documentation / unspecified
blockList.addSubnet('0.0.0.0', 8, 'ipv4');
blockList.addSubnet('240.0.0.0', 4, 'ipv4');

async function validateSsrfSafeUrl(targetUrl) {
  let parsed;
  try {
    parsed = new URL(targetUrl);
  } catch (e) {
    throw new Error(`Invalid URL: ${e.message}`);
  }

  const hostname = parsed.hostname.toLowerCase().replace(/\.$/, '').replace(/^\[|\]$/g, '');

  if (hostname === 'localhost' || hostname.endsWith('.localhost') || hostname.endsWith('.local') || hostname.endsWith('.internal')) {
    throw new Error('SSRF Blocked: Local host alias is forbidden');
  }

  // Direct IP check if hostname is already IP
  if (net.isIP(hostname)) {
    const type = net.isIPv6(hostname) ? 'ipv6' : 'ipv4';
    if (blockList.check(hostname, type)) {
      throw new Error(`SSRF Blocked: IP ${hostname} is in prohibited subnet/private range`);
    }
    if (type === 'ipv6' && hostname.toLowerCase().startsWith('::ffff:')) {
      const v4Part = hostname.slice(7);
      if (net.isIPv4(v4Part) && blockList.check(v4Part, 'ipv4')) {
        throw new Error(`SSRF Blocked: IPv4-mapped IPv6 ${hostname} targets private range`);
      }
    }
  } else {
    // DNS resolution
    try {
      const addresses = await dns.lookup(hostname, { all: true });
      if (!addresses || addresses.length === 0) {
        throw new Error('SSRF Blocked: DNS resolution yielded no addresses');
      }
      for (const record of addresses) {
        const ip = record.address;
        const type = record.family === 6 ? 'ipv6' : 'ipv4';
        if (blockList.check(ip, type)) {
          throw new Error(`SSRF Blocked: Resolved IP ${ip} for ${hostname} is prohibited`);
        }
        if (type === 'ipv6' && ip.toLowerCase().startsWith('::ffff:')) {
          const v4Part = ip.slice(7);
          if (net.isIPv4(v4Part) && blockList.check(v4Part, 'ipv4')) {
            throw new Error(`SSRF Blocked: Resolved IPv4-mapped IPv6 ${ip} for ${hostname} is prohibited`);
          }
        }
      }
    } catch (dnsErr) {
      if (dnsErr.message.includes('SSRF Blocked')) throw dnsErr;
      throw new Error(`SSRF Blocked: DNS resolution failed: ${dnsErr.message}`);
    }
  }

  return parsed.toString();
}

async function runTest() {
  const testInputs = [
    'https://localhost/api',
    'https://localhost./api',
    'https://127.0.0.1/api',
    'https://0.0.0.0/api',
    'https://[::1]/api',
    'https://[::]/api',
    'https://[::ffff:127.0.0.1]/api',
    'https://[fd00::1]/api',
    'https://[fe80::1]/api',
    'https://169.254.169.254/latest/meta-data',
    'https://10.0.0.1/api',
    'https://172.16.0.1/api',
    'https://192.168.1.1/api',
    'https://100.64.0.1/api',
    'https://198.18.0.1/api',
    'https://localtest.me/api'
  ];

  console.log('Testing 16 SSRF attack vectors:');
  let blockedCount = 0;
  for (const url of testInputs) {
    try {
      await validateSsrfSafeUrl(url);
      console.log(`❌ FAILED TO BLOCK: ${url}`);
    } catch (err) {
      blockedCount++;
      console.log(`✅ BLOCKED: ${url} -> ${err.message}`);
    }
  }
  console.log(`\nResult: ${blockedCount}/16 attack vectors blocked.`);
}

runTest();
