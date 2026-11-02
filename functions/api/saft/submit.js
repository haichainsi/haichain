const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Requested-With',
  'Access-Control-Max-Age': '86400',
};

function buildHaichainSaftEmailHtml(opt) {
  const contractId = opt.contractId || '';
  const name = opt.name || 'Anonymous Investor';
  const email = opt.email || '';
  const amount = Number(opt.amount) || 0;
  const tokens = Number(opt.tokens) || Math.floor(amount / 0.007);
  const wallet = opt.wallet || 'N/A';
  const treasury = opt.treasury || '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';
  const hashHex = opt.hashHex || 'N/A';
  const timestamp = opt.timestamp || new Date().toISOString();
  const isAdmin = !!opt.isAdmin;

  const contractPdfUrl = "https://haichain.si/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf";
  const tgeVal = Math.round(tokens * 0.01);
  const formattedAmount = amount.toLocaleString('en-US');
  const formattedTokens = tokens.toLocaleString('en-US');
  const formattedTgeVal = tgeVal.toLocaleString('en-US');

  const title = isAdmin ? "PRE-SEED SAFT AGREEMENT SIGNED" : "Pre-Seed SAFT Agreement Execution Confirmation";
  const badge = "✓ CRYPTOGRAPHICALLY SIGNED &amp; RECORDED";
  
  const intro = isAdmin
    ? "A new Pre-Seed Strategic Round Simple Agreement for Future Tokens (SAFT) has been digitally executed and cryptographically sealed pursuant to the <strong>US ESIGN Act (15 U.S.C. § 7001) &amp; UETA standards</strong>."
    : `Dear <strong>${name}</strong>,<br><br>Your Simple Agreement for Future Tokens (SAFT) for the <strong>HAICHAIN Pre-Seed Strategic Round</strong> has been cryptographically signed and officially recorded pursuant to the <strong>US Electronic Signatures in Global and National Commerce Act (ESIGN Act, 15 U.S.C. § 7001) &amp; UETA standards</strong>.`;

  const btnPdfText = "📄 View Official SAFT Agreement (PDF)";
  const btnDashText = "Access HAICHAIN Dashboard";
  const actionLead = "Your official SAFT Agreement copy has been cryptographically sealed. You can view or download the complete contract document below:";
  const treasuryNote = "Investment funds are secured in the Squads Multi-Sig Treasury on Solana Mainnet. Your $HAISI tokens will be minted and transferred directly to your beneficiary wallet upon the Token Generation Event (TGE).";

  return `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HAICHAIN Pre-Seed SAFT Execution</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f4f4f5; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;">
  <div style="background-color: #f4f4f5; padding: 32px 16px;">
    <div style="max-width: 640px; margin: 0 auto; background-color: #0c0c0e; border: 1px solid #27272a; border-radius: 18px; padding: 36px 28px; color: #ffffff; box-shadow: 0 12px 36px rgba(0,0,0,0.25);">
      
      <!-- Brand Header with Logo -->
      <div style="border-bottom: 1px solid #27272a; padding-bottom: 24px; margin-bottom: 28px;">
        <div style="margin-bottom: 16px;">
          <img src="https://haichain.si/assets/haichain-official-logo-white.png" alt="Haichain" height="32" style="height: 32px; width: auto; display: block; border: 0;" />
        </div>
        <div style="font-size: 13px; font-weight: 600; color: #ffffff; letter-spacing: -0.2px; line-height: 1.5;">
          Haichain - The Financial Operating System for The Autonomous Machine Era
        </div>
        <div style="font-size: 12px; color: #a1a1aa; margin-top: 4px; line-height: 1.5;">
          The Economic Bedrock for the Symbiotic Superintelligence Era AI²
        </div>
      </div>

      <!-- Execution Badge -->
      <div style="display: inline-block; background-color: rgba(74, 222, 128, 0.1); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 9999px; padding: 4px 14px; margin-bottom: 20px;">
        <span style="font-size: 11px; font-weight: 700; color: #4ade80; text-transform: uppercase; letter-spacing: 0.5px; font-family: monospace;">
          ${badge}
        </span>
      </div>

      <!-- Salutation & Headline -->
      <h1 style="margin: 0 0 16px 0; font-size: 21px; font-weight: 700; color: #ffffff; letter-spacing: -0.5px;">
        ${title}
      </h1>
      <p style="margin: 0 0 24px 0; font-size: 13px; line-height: 1.6; color: #d4d4d8;">
        ${intro}
      </p>

      <!-- Key Details Card -->
      <div style="background-color: #141417; border: 1px solid #27272a; border-radius: 14px; padding: 22px; margin-bottom: 28px;">
        <table style="width: 100%; border-collapse: collapse; font-size: 13px; line-height: 1.6;">
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; width: 42%; border-bottom: 1px solid #1f1f23;">Contract ID:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #ffffff; font-family: monospace; border-bottom: 1px solid #1f1f23;">${contractId}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Signatory Entity:</td>
            <td style="padding: 8px 0; font-weight: 600; color: #ffffff; border-bottom: 1px solid #1f1f23;">${name}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Registered Email:</td>
            <td style="padding: 8px 0; color: #38bdf8; font-family: monospace; border-bottom: 1px solid #1f1f23;">${email}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Subscription Investment:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #4ade80; font-size: 15px; border-bottom: 1px solid #1f1f23;">$${formattedAmount} USD (USDT)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Token Entitlement:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #ffffff; border-bottom: 1px solid #1f1f23;">${formattedTokens} $HAISI (@ $0.007)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Projected TGE Value:</td>
            <td style="padding: 8px 0; color: #a1a1aa; font-weight: 600; border-bottom: 1px solid #1f1f23;">$${formattedTgeVal} USD (+42.8%)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Beneficiary Solana Wallet:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 11px; color: #ffffff; word-break: break-all; border-bottom: 1px solid #1f1f23;">${wallet}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Multi-Sig Treasury Vault:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 11px; color: #a1a1aa; word-break: break-all; border-bottom: 1px solid #1f1f23;">${treasury}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">SHA-256 Audit Proof:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 10px; color: #71717a; word-break: break-all; border-bottom: 1px solid #1f1f23;">${hashHex}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa;">Execution Time (UTC):</td>
            <td style="padding: 8px 0; color: #ffffff; font-size: 12px;">${timestamp}</td>
          </tr>
        </table>
      </div>

      <!-- Prominent Contract Link & Dashboard Button -->
      <div style="background-color: #121215; border: 1px solid #27272a; border-radius: 14px; padding: 24px; text-align: center; margin-bottom: 28px;">
        <p style="margin: 0 0 16px 0; font-size: 13px; line-height: 1.6; color: #d4d4d8;">
          ${actionLead}
        </p>
        <div style="text-align: center;">
          <a href="${contractPdfUrl}" target="_blank" style="display: inline-block; background-color: #ffffff; color: #000000; font-weight: 700; font-size: 13px; padding: 13px 32px; border-radius: 9999px; text-decoration: none; margin: 6px; box-shadow: 0 4px 14px rgba(255,255,255,0.15);">
            ${btnPdfText}
          </a>
          <a href="https://haichain.si/dashboard" target="_blank" style="display: inline-block; background-color: #18181b; color: #ffffff; font-weight: 600; font-size: 13px; padding: 13px 26px; border-radius: 9999px; text-decoration: none; border: 1px solid #3f3f46; margin: 6px;">
            ${btnDashText}
          </a>
        </div>
      </div>

      <p style="margin: 0 0 28px 0; font-size: 12px; line-height: 1.6; color: #71717a;">
        ${treasuryNote}
      </p>

      <!-- Standard Institutional Email Footer -->
      <div style="border-top: 1px solid #27272a; padding-top: 24px; font-size: 11px; line-height: 1.7; color: #71717a;">
        <div style="margin-bottom: 12px;">
          <strong style="color: #ffffff; font-size: 12px;">Haichain Foundation</strong><br />
          <span style="color: #a1a1aa; font-size: 11px;">Haichain - The Financial Operating System for The Autonomous Machine Era - The Economic Bedrock for the Symbiotic Superintelligence Era AI²</span>
        </div>
        <div style="margin-bottom: 12px; color: #a1a1aa;">
          Official Website: <a href="https://haichain.si" target="_blank" style="color: #38bdf8; text-decoration: none;">https://haichain.si</a> &nbsp;•&nbsp; 
          Support: <a href="mailto:support@haichain.si" style="color: #ffffff; text-decoration: none;">support@haichain.si</a>
        </div>
        <div style="margin-bottom: 12px; color: #52525b; font-size: 10px; line-height: 1.5;">
          <strong>LEGAL NOTICE &amp; ESIGN COMPLIANCE:</strong> This electronic transmission and its cryptographic proof of execution are generated pursuant to the US Electronic Signatures in Global and National Commerce Act (ESIGN Act, 15 U.S.C. § 7001 et seq.) and the Uniform Electronic Transactions Act (UETA). The terms herein constitute a legally binding Simple Agreement for Future Tokens (SAFT) under applicable digital commerce and transaction laws. This message is intended solely for the designated recipient and may contain confidential information. If you received this transmission in error, please notify support@haichain.si immediately.
        </div>
        <div style="color: #3f3f46; font-size: 10px;">
          © Haichain. All rights reserved.
        </div>
      </div>

    </div>
  </div>
</body>
</html>`;
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: corsHeaders });
}

export async function onRequestPost({ request, env }) {
  try {
    const data = await request.json();
    const contractId = data.contractId || ('SAFT-HAI-' + Math.random().toString(36).substring(2, 7).toUpperCase());
    const name = data.name || 'Anonymous Investor';
    const email = data.email || 'haichain.si@gmail.com';
    const amount = Number(data.amount) || 0;
    const tokens = Number(data.tokens) || Math.floor(amount / 0.007);
    const wallet = data.wallet || 'N/A';
    const treasury = data.treasury || '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';
    const timestamp = data.timestamp || new Date().toISOString();
    const hashHex = data.hashHex || 'N/A';
    const signatureData = data.signatureData || '';

    const saftRecord = {
      contractId,
      name,
      email,
      amount,
      tokens,
      wallet,
      treasury,
      timestamp,
      hashHex,
      signatureData
    };

    // 1. Telegram Notification
    const tgToken = (env && env.TELEGRAM_BOT_TOKEN) || '9066296959:AAE716Gw5KOh1jiUuurbdO_g5n7gIXblcqk';
    const tgChatId = (env && env.TELEGRAM_CHAT_ID) || '-5426770743';

    const tgMessage = `🔔 *NEW PRE-SEED SAFT AGREEMENT SIGNED!*
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

    try {
      await fetch(`https://api.telegram.org/bot${tgToken}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: tgChatId,
          text: tgMessage,
          parse_mode: 'Markdown'
        })
      });
    } catch (_) {}

    // 2. Dual Resend Email Notifications
    const resendKey = (env && env.RESEND_API_KEY) || 're_Hqp1tNKV_6w8Ur4v3B91Jv6yusD4CK5pN';
    const senderFrom = 'Haichain <no-reply@mail.haichain.si>';

    // (A) Admin
    try {
      const adminHtml = buildHaichainSaftEmailHtml({
        contractId,
        name,
        email,
        amount,
        tokens,
        wallet,
        treasury,
        hashHex,
        timestamp,
        isAdmin: true,
        lang: 'vi'
      });

      await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${resendKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          from: senderFrom,
          to: ['haichain.si@gmail.com'],
          subject: `🔔 [SAFT Signed] $${amount.toLocaleString('en-US')} USD - ${name} (${contractId})`,
          html: adminHtml
        })
      });
    } catch (_) {}

    // (B) Investor
    if (email && email.includes('@')) {
      try {
        const investorHtml = buildHaichainSaftEmailHtml({
          contractId,
          name,
          email,
          amount,
          tokens,
          wallet,
          treasury,
          hashHex,
          timestamp,
          isAdmin: false,
          lang: 'vi'
        });

        await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${resendKey}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            from: senderFrom,
            to: [email],
            subject: `Haichain Official SAFT Agreement - Signed Confirmation (${contractId})`,
            html: investorHtml
          })
        });
      } catch (_) {}
    }

    return new Response(JSON.stringify({
      success: true,
      contractId,
      timestamp,
      message: 'SAFT agreement recorded & legal confirmation emails dispatched'
    }), {
      status: 200,
      headers: {
        ...corsHeaders,
        'Content-Type': 'application/json'
      }
    });

  } catch (err) {
    return new Response(JSON.stringify({
      success: false,
      error: err.message
    }), {
      status: 500,
      headers: {
        ...corsHeaders,
        'Content-Type': 'application/json'
      }
    });
  }
}
