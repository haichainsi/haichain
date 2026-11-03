/**
 * Example: An autonomous Web Scraper Agent on Smithery/Glama monetized with HAICHAIN Paywall.
 * 
 * If a caller sends a request without payment, this server returns HTTP 402 Payment Required.
 * If a caller settles the micro-payment ($0.003 USDT) via HAICHAIN, the agent returns the scraped data.
 */

const http = require('http');
const { HaichainPaywall } = require('../dist/index.js');

const paywall = new HaichainPaywall({
  recipient: 'Sm1thScrap3rPo1nt782VbX4nNmK9q1zEwR2Ty7LpA', // Agent Creator's Solana Address
  priceUsdt: 0.003,                                       // $0.003 USDT / micro-task
  serviceName: 'Smithery Web Extraction Sentinel Node #01',
  cluster: 'devnet',
  requireConfirmation: false
});

const server = http.createServer(async (req, res) => {
  // Check payment using Haichain Paywall
  const authHeader = req.headers['authorization'] || req.headers['x-payment-signature'];
  const check = await paywall.verifyPayment(authHeader);

  if (!check.valid) {
    // 402 Payment Required
    const challenge = paywall.generate402Challenge(req.url);
    res.writeHead(challenge.status, challenge.headers);
    return res.end(JSON.stringify(challenge.body));
  }

  // Payment Verified! Execute and return valuable agent output
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    status: 'SUCCESS_PAID',
    agent: 'Smithery Web Extraction Sentinel Node #01',
    paymentSettled: '$0.0030 USDT',
    recipient: 'Sm1thScrap3rPo1nt782VbX4nNmK9q1zEwR2Ty7LpA',
    extractedData: {
      source: 'Autonomous Target',
      crawledRecords: 42,
      entities: ['SOL-USDT', 'Raydium Liquidity Pool', 'Zero Captcha Delay']
    }
  }));
});

const PORT = 3800;
server.listen(PORT, () => {
  console.log(`[Monetized Agent] Running on http://127.0.0.1:${PORT}`);
});
