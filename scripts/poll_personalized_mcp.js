async function pollDeploy() {
  const targetScript = 'v39_personalized_vault_mcp_1793648000000';
  for (let i = 0; i < 20; i++) {
    try {
      const res = await fetch('https://haichain.si/dashboard?t=' + Date.now(), {
        headers: { 'User-Agent': 'Mozilla/5.0' }
      });
      const html = await res.text();
      if (html.includes(targetScript)) {
        console.log(`[SUCCESS] Cloudflare Pages deployed commit with script ${targetScript} at attempt ${i + 1}`);
        const snippetMatch = html.match(/id="online-mcp-connected-box"/);
        console.log("Found online-mcp-connected-box:", !!snippetMatch);
        return true;
      }
    } catch (e) {
      console.log('Fetch error:', e.message);
    }
    await new Promise(r => setTimeout(r, 4000));
  }
  console.log('[TIMEOUT] Deployment still in progress on CDN edges.');
  return false;
}
pollDeploy();
