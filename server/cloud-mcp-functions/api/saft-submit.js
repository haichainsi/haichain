// Cloudflare Pages Function: /api/saft/submit
// Executes dual instant email notifications (Admin + Investor) via Resend API and Telegram backup

const RESEND_API_KEY = 're_Hqp1tNKV_6w8Ur4v3B91Jv6yusD4CK5pN';
const RESEND_SENDER = 'Haichain <no-reply@mail.haichain.si>';
const ADMIN_EMAIL = 'haichain.si@gmail.com';
const TELEGRAM_BOT_TOKEN = '9066296959:AAE716Gw5KOh1jiUuurbdO_g5n7gIXblcqk';
const TELEGRAM_CHAT_ID = '-5426770743';

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  'Content-Type': 'application/json'
};

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: corsHeaders });
}

export async function onRequestPost(context) {
  const { request, env } = context;

  try {
    const data = await request.json();
    const contractId = data.contractId || ('SAFT-HAI-' + Math.random().toString(36).substring(2, 7).toUpperCase());
    const name = data.name || 'Anonymous Investor';
    const email = data.email || '';
    const amount = Number(data.amount) || 0;
    const tokens = Number(data.tokens) || Math.floor(amount / 0.007);
    const wallet = data.wallet || 'N/A';
    const treasury = data.treasury || '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';
    const timestamp = data.timestamp || new Date().toISOString();
    const hashHex = data.hashHex || 'N/A';
    const lang = data.lang || 'vi';

    const isVi = lang === 'vi';

    // 1. Build Admin HTML Email
    const adminHtml = data.adminHtml || `
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 620px; margin: 0 auto; padding: 32px 24px; background-color: #0c0c0e; color: #ffffff; border-radius: 16px; border: 1px solid #27272a;">
  <div style="border-bottom: 1px solid #27272a; padding-bottom: 20px; margin-bottom: 24px;">
    <h2 style="margin: 0; font-size: 20px; font-weight: 700; color: #ffffff;">🔔 NEW PRE-SEED SAFT AGREEMENT SIGNED</h2>
    <p style="margin: 6px 0 0 0; font-size: 13px; color: #a1a1aa;">HAICHAIN Autonomous Machine Financial Protocol</p>
  </div>
  <table style="width: 100%; border-collapse: collapse; font-size: 13px; line-height: 1.6;">
    <tr><td style="padding: 10px 0; color: #a1a1aa; width: 40%;">Contract ID:</td><td style="padding: 10px 0; font-weight: bold; font-family: monospace; color: #ffffff;">${contractId}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Signatory:</td><td style="padding: 10px 0; font-weight: bold; color: #ffffff;">${name}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Email:</td><td style="padding: 10px 0; color: #ffffff; font-weight: bold;">${email}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Amount:</td><td style="padding: 10px 0; font-weight: bold; color: #ffffff; font-size: 15px;">$${amount.toLocaleString('en-US')} USD (USDT)</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Token Allocation:</td><td style="padding: 10px 0; font-weight: bold; color: #ffffff;">${tokens.toLocaleString('en-US')} $HAISI (@ $0.007)</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Beneficiary Wallet:</td><td style="padding: 10px 0; font-family: monospace; font-size: 11px; color: #ffffff; word-break: break-all;">${wallet}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Treasury Vault:</td><td style="padding: 10px 0; font-family: monospace; font-size: 11px; color: #a1a1aa; word-break: break-all;">${treasury}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">SHA-256 Audit Hash:</td><td style="padding: 10px 0; font-family: monospace; font-size: 10px; color: #71717a; word-break: break-all;">${hashHex}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Timestamp (UTC):</td><td style="padding: 10px 0; color: #ffffff;">${timestamp}</td></tr>
  </table>
  <div style="margin-top: 24px; padding-top: 18px; border-top: 1px solid #27272a; text-align: center;">
    <a href="https://haichain.si/dashboard" style="display: inline-block; background-color: #ffffff; color: #000000; font-weight: bold; font-size: 13px; padding: 10px 24px; border-radius: 9999px; text-decoration: none;">View Dashboard</a>
  </div>
</div>`;

    // 2. Build Investor HTML Email
    const investorHtml = data.investorHtml || `
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 620px; margin: 0 auto; padding: 32px 24px; background-color: #0c0c0e; color: #ffffff; border-radius: 16px; border: 1px solid #27272a;">
  <div style="border-bottom: 1px solid #27272a; padding-bottom: 20px; margin-bottom: 24px;">
    <h2 style="margin: 0; font-size: 20px; font-weight: 700; color: #ffffff;">${isVi ? 'XÁC NHẬN KÝ KẾT HỢP ĐỒNG SAFT THÀNH CÔNG' : 'SAFT AGREEMENT EXECUTION CONFIRMATION'}</h2>
    <p style="margin: 6px 0 0 0; font-size: 13px; color: #a1a1aa;">HAICHAIN Autonomous Machine Financial Protocol</p>
  </div>
  <p style="font-size: 14px; line-height: 1.6; color: #d4d4d8;">
    ${isVi 
      ? `Kính gửi <strong>${name}</strong>,<br><br>Hợp đồng SAFT (Simple Agreement for Future Tokens) Pre-Seed của bạn đã được ký kết và ghi nhận thành công vào sổ cái mật mã của HAICHAIN.`
      : `Dear <strong>${name}</strong>,<br><br>Your Pre-Seed SAFT Agreement has been legally executed and recorded on the HAICHAIN cryptographic ledger.`}
  </p>
  <table style="width: 100%; border-collapse: collapse; font-size: 13px; line-height: 1.6; margin: 20px 0;">
    <tr><td style="padding: 10px 0; color: #a1a1aa; width: 40%;">${isVi ? 'Mã Hợp Đồng:' : 'Contract ID:'}</td><td style="padding: 10px 0; font-weight: bold; font-family: monospace; color: #ffffff;">${contractId}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">${isVi ? 'Số Tiền Đầu Tư:' : 'Investment Amount:'}</td><td style="padding: 10px 0; font-weight: bold; color: #ffffff; font-size: 15px;">$${amount.toLocaleString('en-US')} USD (USDT)</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">${isVi ? 'Số Lượng Token Phân Bổ:' : 'Token Allocation:'}</td><td style="padding: 10px 0; font-weight: bold; color: #ffffff;">${tokens.toLocaleString('en-US')} $HAISI (@ $0.007)</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">${isVi ? 'Ví Nhận Token (Solana):' : 'Beneficiary Wallet:'}</td><td style="padding: 10px 0; font-family: monospace; font-size: 11px; color: #ffffff; word-break: break-all;">${wallet}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">${isVi ? 'Ví Đa Ký Quỹ Haichain:' : 'Haichain Treasury Vault:'}</td><td style="padding: 10px 0; font-family: monospace; font-size: 11px; color: #a1a1aa; word-break: break-all;">${treasury}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">${isVi ? 'Mã Băm Kiểm Toán SHA-256:' : 'Audit Hash SHA-256:'}</td><td style="padding: 10px 0; font-family: monospace; font-size: 10px; color: #71717a; word-break: break-all;">${hashHex}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">${isVi ? 'Thời Gian Ký (UTC):' : 'Execution Time (UTC):'}</td><td style="padding: 10px 0; color: #ffffff;">${timestamp}</td></tr>
  </table>
  <div style="margin-top: 24px; padding-top: 18px; border-top: 1px solid #27272a; text-align: center;">
    <a href="https://haichain.si/dashboard" style="display: inline-block; background-color: #ffffff; color: #000000; font-weight: bold; font-size: 13px; padding: 10px 24px; border-radius: 9999px; text-decoration: none;">
      ${isVi ? 'Kiểm Tra Kho Vesting Của Bạn' : 'Check Your Vesting Vault'}
    </a>
  </div>
</div>`;

    const resendKey = (env && env.RESEND_API_KEY) || RESEND_API_KEY;
    const adminSubject = `🔔 [SAFT Signed] $${amount.toLocaleString('en-US')} USD - ${name} (${contractId})`;
    const investorSubject = isVi 
      ? `Xác Nhận Ký Hợp Đồng SAFT Pre-Seed - Haichain Protocol (${contractId})`
      : `Haichain Official SAFT Agreement - Signed Confirmation (${contractId})`;

    let adminEmailResult = null;
    let investorEmailResult = null;
    let adminEmailError = null;
    let investorEmailError = null;

    // Send Admin Email via Resend
    try {
      const resAdmin = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${resendKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          from: RESEND_SENDER,
          to: [ADMIN_EMAIL],
          subject: adminSubject,
          html: adminHtml
        })
      });
      if (resAdmin.ok) {
        adminEmailResult = await resAdmin.json();
      } else {
        adminEmailError = await resAdmin.text();
      }
    } catch (e) {
      adminEmailError = e.message;
    }

    // Send Investor Email via Resend
    if (email && email.includes('@')) {
      try {
        const resInv = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${resendKey}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            from: RESEND_SENDER,
            to: [email],
            subject: investorSubject,
            html: investorHtml
          })
        });
        if (resInv.ok) {
          investorEmailResult = await resInv.json();
        } else {
          investorEmailError = await resInv.text();
        }
      } catch (e) {
        investorEmailError = e.message;
      }
    }

    // Send Telegram Notification
    let telegramSent = false;
    try {
      const tgMsg = `🔔 *NEW PRE-SEED SAFT AGREEMENT SIGNED!*
━━━━━━━━━━━━━━━━━━━━
📋 *Contract ID:* \`${contractId}\`
👤 *Investor:* *${name}*
📧 *Email:* \`${email}\`
💰 *Investment:* *$${amount.toLocaleString('en-US')} USD (USDT)*
🪙 *Allocation:* *${tokens.toLocaleString('en-US')} $HAISI* (@ $0.007)
📈 *TGE Upside:* *$${Math.round(tokens * 0.01).toLocaleString('en-US')} USD (+42.8%)*
💼 *Beneficiary Solana Wallet:*
\`${wallet}\`
🏛️ *Multi-Sig Treasury Vault:*
\`${treasury}\`
🔐 *SHA-256 Audit Proof:*
\`${hashHex}\`
⏰ *Signed Time (UTC):* \`${timestamp}\`
━━━━━━━━━━━━━━━━━━━━
✅ *Legally Executed under US ESIGN Act & UETA*`;

      const tgRes = await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: TELEGRAM_CHAT_ID,
          text: tgMsg,
          parse_mode: 'Markdown'
        })
      });
      telegramSent = tgRes.ok;
    } catch (_) {}

    return new Response(JSON.stringify({
      success: true,
      contractId,
      adminEmailSent: !!adminEmailResult,
      adminEmailId: adminEmailResult ? adminEmailResult.id : null,
      adminEmailError,
      investorEmailSent: !!investorEmailResult,
      investorEmailId: investorEmailResult ? investorEmailResult.id : null,
      investorEmailError,
      telegramSent
    }), {
      status: 200,
      headers: corsHeaders
    });

  } catch (err) {
    return new Response(JSON.stringify({ error: err.message || 'Internal Server Error' }), {
      status: 500,
      headers: corsHeaders
    });
  }
}
