async function poll() {
  const testVault = '7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU';
  console.log('Polling mcp.haichain.si for version 7.1.0...');

  for (let i = 0; i < 20; i++) {
    try {
      const res = await fetch('https://mcp.haichain.si/api/mcp?vault=' + testVault + '&t=' + Date.now(), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          jsonrpc: '2.0',
          id: 1,
          method: 'tools/call',
          params: {
            name: 'get_spending_pot_balance',
            arguments: {}
          }
        })
      });
      if (res.ok) {
        const json = await res.json();
        const text = json?.result?.content?.[0]?.text;
        if (text && text.includes('isPersonalizedVault')) {
          console.log('[SUCCESS] Live mcp.haichain.si updated with v7.1.0 at attempt', i + 1);
          console.log('Returned payload:');
          console.log(text);
          return true;
        }
      }
    } catch (e) {
      console.log('Err:', e.message);
    }
    await new Promise(r => setTimeout(r, 4000));
  }
  console.log('[TIMEOUT] Still deploying');
  return false;
}
poll();
