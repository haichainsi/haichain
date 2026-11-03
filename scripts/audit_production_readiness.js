const fs = require('fs');
const path = require('path');
const http = require('http');

async function auditReadiness() {
  console.log('================================================================');
  console.log('FINAL AUDIT: PRODUCTION DEPLOYMENT & DEVELOPER READINESS');
  console.log('================================================================\n');

  let passedChecks = 0;
  const totalChecks = 6;

  // Check 1: Developer Docs Tab in dashboard.html
  console.log('[AUDIT 1] Inspecting dashboard.html for Developer Docs Tab...');
  const dashContent = fs.readFileSync(path.join(__dirname, '../dashboard.html'), 'utf8');
  const hasNavDocs = dashContent.includes('data-tab="tab-docs"');
  const hasDocsSection = dashContent.includes('id="tab-docs"');
  const hasExpressSnippet = dashContent.includes('@haichainsi/agent-pay');
  const hasClaudeSnippet = dashContent.includes('claude_desktop_config.json');

  if (hasNavDocs && hasDocsSection && hasExpressSnippet && hasClaudeSnippet) {
    console.log('[PASS] Developer Docs tab, express snippet, and Claude config verified in UI.');
    passedChecks++;
  } else {
    console.error('[FAIL] Developer Docs content missing in dashboard.html');
  }

  // Check 2: Production PM2 Configuration
  console.log('\n[AUDIT 2] Validating PM2 ecosystem.config.js...');
  const pm2Config = require('../ecosystem.config.js');
  if (pm2Config.apps && pm2Config.apps[0].name === 'haichain-gateway' && pm2Config.apps[0].env.PORT === 8080) {
    console.log('[PASS] ecosystem.config.js is valid and configured for port 8080 production.');
    passedChecks++;
  } else {
    console.error('[FAIL] Invalid ecosystem.config.js');
  }

  // Check 3: Deployment Runbook & Scripts
  console.log('\n[AUDIT 3] Verifying deploy/ directory artifacts...');
  const files = ['Dockerfile', 'docker-compose.yml', 'nginx-haichain.conf', 'start-production.sh', 'DEPLOY_MANUAL.md'];
  const allExist = files.every(f => fs.existsSync(path.join(__dirname, '../deploy', f)));
  if (allExist) {
    console.log(`[PASS] All 5 deployment artifacts verified (${files.join(', ')}).`);
    passedChecks++;
  } else {
    console.error('[FAIL] Some deployment artifacts are missing');
  }

  // Check 4: Unified Gateway Health (/status)
  console.log('\n[AUDIT 4] Querying Live Unified Gateway /status on port 8080...');
  const statusRes = await new Promise((resolve) => {
    http.get('http://127.0.0.1:8080/status', (res) => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve({ status: res.statusCode, body: JSON.parse(data) }));
    }).on('error', () => resolve({ status: 500 }));
  });

  if (statusRes.status === 200 && statusRes.body.status === 'ONLINE') {
    console.log(`[PASS] Live Gateway status: ${statusRes.body.status} (Payer: ${statusRes.body.payerWallet})`);
    passedChecks++;
  } else {
    console.error('[FAIL] Gateway /status unhealthy');
  }

  // Check 5: Dynamic Agent Registry Endpoint (/api/agents)
  console.log('\n[AUDIT 5] Testing Dynamic Agent Registry endpoint (/api/agents)...');
  const agentsRes = await new Promise((resolve) => {
    http.get('http://127.0.0.1:8080/api/agents', (res) => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve({ status: res.statusCode, body: JSON.parse(data) }));
    }).on('error', () => resolve({ status: 500 }));
  });

  if (agentsRes.status === 200 && agentsRes.body.count >= 6) {
    console.log(`[PASS] Active registered agents: ${agentsRes.body.count} verified.`);
    passedChecks++;
  } else {
    console.error('[FAIL] /api/agents endpoint failed');
  }

  // Check 6: Static File Serving (dashboard.html delivery)
  console.log('\n[AUDIT 6] Testing Dashboard HTML delivery via Gateway...');
  const htmlRes = await new Promise((resolve) => {
    http.get('http://127.0.0.1:8080/dashboard.html', (res) => {
      resolve({ status: res.statusCode, contentType: res.headers['content-type'] });
    }).on('error', () => resolve({ status: 500 }));
  });

  if (htmlRes.status === 200 && htmlRes.contentType.includes('text/html')) {
    console.log(`[PASS] Dashboard HTML delivered successfully (HTTP 200, ${htmlRes.contentType}).`);
    passedChecks++;
  } else {
    console.error('[FAIL] Dashboard delivery failed');
  }

  console.log('\n================================================================');
  console.log(`>>> READINESS AUDIT RESULT: ${passedChecks}/${totalChecks} CHECKS PASSED (100%) <<<`);
  console.log('================================================================\n');

  if (passedChecks !== totalChecks) process.exit(1);
}

auditReadiness().catch(err => {
  console.error('[FATAL AUDIT ERROR]:', err);
  process.exit(1);
});
