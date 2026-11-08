const https = require('https');

const emailTo = 'hungtiger1375@gmail.com';
const subject = 'HAICHAIN Angel Allocation: Deposit Confirmation & 3-Day Notice (SAFT-HAI-2026-LMYCV)';

const textContent = `Dear Mr. Nguyen Thanh Hung,

Thank you for your trust in HAICHAIN.

We confirm receipt of your $3,000 USD reservation deposit:

• Contract ID: SAFT-HAI-2026-LMYCV
• Registered Amount: $20,000 USD (2,857,142 $HAISI)
• Deposit Received: $3,000 USD
• Remaining Balance: $17,000 USD
• Treasury Vault: 5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3
• Beneficiary Wallet: i9yYo2zDquEvbkD2QyX5DkGPyNEZTRK1PA8Gy1QHccF

Due to limited angel slots and waitlist demand, this allocation is reserved for 3 days. 

Please transfer the remaining $17,000 USD to the Treasury Vault above within 3 days. After this deadline, we will fully refund your $3,000 deposit and offer the slot to waitlist investors.

We deeply appreciate your belief in HAICHAIN.

Sincerely,
HAICHAIN Foundation
https://haichain.si`;

const htmlContent = `
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 32px 24px; background-color: #0c0c0e; color: #ffffff; border-radius: 16px; border: 1px solid #27272a; line-height: 1.6;">
  <div style="border-bottom: 1px solid #27272a; padding-bottom: 20px; margin-bottom: 24px;">
    <h2 style="margin: 0; font-size: 20px; font-weight: 700; color: #ffffff;">HAICHAIN PROTOCOL</h2>
    <p style="margin: 6px 0 0 0; font-size: 13px; color: #a1a1aa;">Angel Strategic Allocation &bull; Deposit Confirmation</p>
  </div>
  
  <p style="font-size: 14px; color: #e4e4e7; margin: 0 0 16px 0;">Dear Mr. Nguyen Thanh Hung,</p>
  <p style="font-size: 14px; color: #d4d4d8; margin: 0 0 20px 0;">Thank you for your trust in HAICHAIN.</p>
  
  <p style="font-size: 14px; color: #d4d4d8; margin: 0 0 12px 0;">We confirm receipt of your <strong>$3,000 USD</strong> reservation deposit:</p>
  
  <table style="width: 100%; border-collapse: collapse; font-size: 13px; margin: 16px 0 24px 0; background-color: #141417; border: 1px solid #27272a; border-radius: 12px;">
    <tr><td style="padding: 10px 16px; color: #a1a1aa; width: 38%; border-bottom: 1px solid #27272a;">Contract ID:</td><td style="padding: 10px 16px; font-weight: bold; font-family: monospace; color: #ffffff; border-bottom: 1px solid #27272a;">SAFT-HAI-2026-LMYCV</td></tr>
    <tr><td style="padding: 10px 16px; color: #a1a1aa; border-bottom: 1px solid #27272a;">Registered Amount:</td><td style="padding: 10px 16px; font-weight: bold; color: #ffffff; border-bottom: 1px solid #27272a;">$20,000 USD (2,857,142 $HAISI)</td></tr>
    <tr><td style="padding: 10px 16px; color: #a1a1aa; border-bottom: 1px solid #27272a;">Deposit Received:</td><td style="padding: 10px 16px; font-weight: bold; color: #4ade80; border-bottom: 1px solid #27272a;">+$3,000 USD</td></tr>
    <tr><td style="padding: 10px 16px; color: #a1a1aa; border-bottom: 1px solid #27272a;">Remaining Balance:</td><td style="padding: 10px 16px; font-weight: bold; color: #f59e0b; border-bottom: 1px solid #27272a; font-size: 14px;">$17,000 USD</td></tr>
    <tr><td style="padding: 10px 16px; color: #a1a1aa; border-bottom: 1px solid #27272a;">Treasury Vault:</td><td style="padding: 10px 16px; font-family: monospace; font-size: 11px; color: #ffffff; word-break: break-all; border-bottom: 1px solid #27272a;">5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3</td></tr>
    <tr><td style="padding: 10px 16px; color: #a1a1aa;">Beneficiary Wallet:</td><td style="padding: 10px 16px; font-family: monospace; font-size: 11px; color: #ffffff; word-break: break-all;">i9yYo2zDquEvbkD2QyX5DkGPyNEZTRK1PA8Gy1QHccF</td></tr>
  </table>

  <p style="font-size: 13px; color: #d4d4d8; line-height: 1.6; margin: 0 0 14px 0;">
    Due to limited angel slots and waitlist demand, this allocation is reserved for <strong>3 days</strong>.
  </p>

  <p style="font-size: 13px; color: #d4d4d8; line-height: 1.6; margin: 0 0 16px 0;">
    Please transfer the remaining <strong>$17,000 USD</strong> to the Treasury Vault above within 3 days. After this deadline, we will fully refund your $3,000 deposit and offer the slot to waitlist investors.
  </p>

  <p style="font-size: 13px; color: #d4d4d8; margin: 0 0 24px 0;">
    We deeply appreciate your belief in HAICHAIN.
  </p>

  <div style="border-top: 1px solid #27272a; padding-top: 18px; font-size: 12px; color: #a1a1aa;">
    <p style="margin: 0; color: #ffffff; font-weight: 600;">Sincerely,</p>
    <p style="margin: 4px 0 0 0; color: #ffffff; font-weight: bold;">HAICHAIN Foundation</p>
    <p style="margin: 2px 0 0 0;"><a href="https://haichain.si" style="color: #38bdf8; text-decoration: none;">https://haichain.si</a></p>
  </div>
</div>`;

const postData = JSON.stringify({
  from: 'Haichain <no-reply@mail.haichain.si>',
  to: [emailTo],
  subject: subject,
  text: textContent,
  html: htmlContent
});

const resendKey = process.env.RESEND_API_KEY || '';
if (!resendKey) {
  console.error('ERROR: RESEND_API_KEY environment variable is required.');
  process.exit(1);
}

const req = https.request({
  hostname: 'api.resend.com',
  path: '/emails',
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${resendKey}`,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(postData)
  }
}, (res) => {
  let body = '';
  res.on('data', chunk => body += chunk);
  res.on('end', () => {
    console.log('HTTP Status:', res.statusCode);
    console.log('Response Body:', body);
  });
});

req.on('error', (e) => console.error('Error:', e));
req.write(postData);
req.end();
