// Node test to simulate Cloudflare Worker endpoints
import worker from '../_worker.js';

async function runTest() {
  console.log('Testing Worker referral telemetry endpoints...');

  // 1. Post click 1 (Twitter Mobile)
  const req1 = new Request('https://haichain.si/api/referral/click', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'cf-ipcountry': 'VN' },
    body: JSON.stringify({
      ref: 'CsFDqYvXWhaichainTestRefWallet123456789',
      source: 'X (Twitter)',
      device: 'Mobile',
      isUnique: true,
      timestamp: Date.now()
    })
  });

  const res1 = await worker.fetch(req1, {}, {});
  console.log('Res1 status:', res1.status);
  const data1 = await res1.json();
  console.log('Data1:', data1);

  // 2. Post click 2 (Telegram Desktop)
  const req2 = new Request('https://haichain.si/api/referral/click', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'cf-ipcountry': 'US' },
    body: JSON.stringify({
      ref: 'CsFDqYvXWhaichainTestRefWallet123456789',
      source: 'Telegram',
      device: 'Desktop',
      isUnique: true,
      timestamp: Date.now()
    })
  });

  const res2 = await worker.fetch(req2, {}, {});
  console.log('Res2 status:', res2.status);
  const data2 = await res2.json();
  console.log('Data2:', data2);

  // 3. Get stats
  const reqStats = new Request('https://haichain.si/api/referral/stats?ref=CsFDqYvXWhaichainTestRefWallet123456789', {
    method: 'GET'
  });

  const resStats = await worker.fetch(reqStats, {}, {});
  console.log('ResStats status:', resStats.status);
  const statsData = await resStats.json();
  console.log('StatsData:', JSON.stringify(statsData, null, 2));

  if (statsData.totalClicks === 2 && statsData.sources['X (Twitter)'] === 1 && statsData.sources['Telegram'] === 1) {
    console.log('>>> WORKER REFERRAL TELEMETRY TEST PASSED WITH 100% SUCCESS! <<<');
  } else {
    throw new Error('Test failed: unexpected stats data');
  }
}

runTest().catch(err => {
  console.error(err);
  process.exit(1);
});
