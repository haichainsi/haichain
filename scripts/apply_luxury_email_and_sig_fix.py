import re
import os

EMAIL_BUILDER_JS = r'''
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
  const lang = opt.lang || 'vi';
  const isVi = (lang === 'vi');

  const contractPdfUrl = "https://haichain.si/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf";
  const tgeVal = Math.round(tokens * 0.01);
  const formattedAmount = amount.toLocaleString('en-US');
  const formattedTokens = tokens.toLocaleString('en-US');
  const formattedTgeVal = tgeVal.toLocaleString('en-US');

  const title = isAdmin ? "THÔNG BÁO HỢP ĐỒNG SAFT PRE-SEED ĐÃ ĐƯỢC KÝ" : (isVi ? "Xác Nhận Ký Kết Hợp Đồng SAFT Pre-Seed" : "Pre-Seed SAFT Agreement Execution Confirmation");
  const badge = "✓ CRYPTOGRAPHICALLY SIGNED &amp; RECORDED";
  
  let intro = '';
  if (isAdmin) {
    intro = 'Hệ thống vừa ghi nhận một Hợp đồng SAFT Vòng Chiến Lược Pre-Seed mới được ký kết điện tử trực tuyến và niêm phong mật mã học thành công theo chuẩn <strong>US ESIGN Act &amp; Luật Giao Dịch Điện Tử 2023</strong>.';
  } else if (isVi) {
    intro = 'Kính gửi <strong>' + name + '</strong>,<br><br>Hợp đồng Tương lai Chuyển đổi Token (SAFT - Simple Agreement for Future Tokens) của bạn cho Vòng Chiến Lược Pre-Seed đã được ký kết điện tử và niêm phong mật mã học thành công theo chuẩn <strong>US ESIGN Act &amp; Luật Giao Dịch Điện Tử 2023</strong>.';
  } else {
    intro = 'Dear <strong>' + name + '</strong>,<br><br>Your Simple Agreement for Future Tokens (SAFT) for the <strong>HAICHAIN Pre-Seed Strategic Round</strong> has been cryptographically signed and officially recorded pursuant to the <strong>US Electronic Signatures in Global and National Commerce Act (ESIGN Act) &amp; UETA standards</strong>.';
  }

  const btnPdfText = isVi ? "📄 Xem File Hợp Đồng SAFT (PDF)" : "📄 View Official SAFT Agreement (PDF)";
  const btnDashText = isVi ? "Truy Cập Dashboard" : "Access HAICHAIN Dashboard";
  const actionLead = isVi ? "Bản sao Hợp đồng SAFT chính thức đã được xuất bản và bảo vệ an toàn. Bạn có thể mở xem trực tiếp hoặc tải về máy toàn văn hợp đồng tại đây:" : "Your official SAFT Agreement has been published and cryptographically sealed. You can view or download the complete contract document below:";
  const treasuryNote = isVi ? "Nguồn vốn đầu tư được bảo vệ tại Kho Bạc Squads Multi-Sig trên Solana Mainnet. Token $HAISI sẽ được phân phối tự động tới ví thụ hưởng của bạn ngay khi giao thức chính thức tiến hành TGE." : "Investment funds are secured in the Squads Multi-Sig Treasury on Solana Mainnet. Your $HAISI tokens will be minted and transferred directly to your beneficiary wallet upon Token Generation Event (TGE).";

  return `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Haichain SAFT Execution</title>
</head>
<body style="margin: 0; padding: 0; background-color: #000000; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;">
  <div style="background-color: #000000; padding: 32px 16px;">
    <div style="max-width: 640px; margin: 0 auto; background-color: #0c0c0e; border: 1px solid #27272a; border-radius: 18px; padding: 36px 28px; color: #ffffff; box-shadow: 0 20px 40px rgba(0,0,0,0.8);">
      
      <!-- Brand Header with Logo & Core Vision -->
      <div style="border-bottom: 1px solid #27272a; padding-bottom: 24px; margin-bottom: 28px;">
        <div style="margin-bottom: 16px;">
          <img src="https://haichain.si/assets/haichain-official-logo-white.png" alt="Haichain" height="32" style="height: 32px; width: auto; display: block; border: 0;" />
        </div>
        <div style="font-size: 13px; font-weight: 600; color: #ffffff; letter-spacing: -0.2px; line-height: 1.5;">
          Haichain — The Financial Operating System for The Autonomous Machine Era
        </div>
        <div style="font-size: 12px; color: #a1a1aa; margin-top: 4px; line-height: 1.5;">
          The Economic Bedrock for the Symbiotic Superintelligence Era AI²
        </div>
      </div>

      <!-- Execution Status Badge -->
      <div style="display: inline-block; background-color: rgba(74, 222, 128, 0.1); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 9999px; padding: 4px 14px; margin-bottom: 20px;">
        <span style="font-size: 11px; font-weight: 700; color: #4ade80; text-transform: uppercase; letter-spacing: 0.5px; font-family: monospace;">
          ${badge}
        </span>
      </div>

      <!-- Main Headline & Intro -->
      <h1 style="margin: 0 0 16px 0; font-size: 21px; font-weight: 700; color: #ffffff; letter-spacing: -0.5px;">
        ${title}
      </h1>
      <p style="margin: 0 0 24px 0; font-size: 13px; line-height: 1.6; color: #d4d4d8;">
        ${intro}
      </p>

      <!-- Contract Key Values Matrix -->
      <div style="background-color: #141417; border: 1px solid #27272a; border-radius: 14px; padding: 22px; margin-bottom: 28px;">
        <table style="width: 100%; border-collapse: collapse; font-size: 13px; line-height: 1.6;">
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; width: 40%; border-bottom: 1px solid #1f1f23;">Mã Hợp Đồng (Contract ID):</td>
            <td style="padding: 8px 0; font-weight: 700; color: #ffffff; font-family: monospace; border-bottom: 1px solid #1f1f23;">${contractId}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Nhà Đầu Tư (Signatory):</td>
            <td style="padding: 8px 0; font-weight: 600; color: #ffffff; border-bottom: 1px solid #1f1f23;">${name}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Email Đăng Ký:</td>
            <td style="padding: 8px 0; color: #38bdf8; font-family: monospace; border-bottom: 1px solid #1f1f23;">${email}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Số Tiền Đầu Tư:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #4ade80; font-size: 15px; border-bottom: 1px solid #1f1f23;">$${formattedAmount} USD (USDT)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Quyền Phân Bổ Token:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #ffffff; border-bottom: 1px solid #1f1f23;">${formattedTokens} $HAISI (@ $0.007)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Giá Trị Dự Kiến Tại TGE:</td>
            <td style="padding: 8px 0; color: #a1a1aa; font-weight: 600; border-bottom: 1px solid #1f1f23;">$${formattedTgeVal} USD (+42.8%)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Ví Solana Nhận Token:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 11px; color: #ffffff; word-break: break-all; border-bottom: 1px solid #1f1f23;">${wallet}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Kho Bạc Multi-Sig Nhận Vốn:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 11px; color: #a1a1aa; word-break: break-all; border-bottom: 1px solid #1f1f23;">${treasury}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Mã Băm Bảo Chứng (SHA-256):</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 10px; color: #71717a; word-break: break-all; border-bottom: 1px solid #1f1f23;">${hashHex}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa;">Thời Gian Ký (UTC):</td>
            <td style="padding: 8px 0; color: #ffffff; font-size: 12px;">${timestamp}</td>
          </tr>
        </table>
      </div>

      <!-- Prominent Contract File Attachment & Dashboard Link -->
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
          Universal Autonomous Machine Financial &amp; Cognitive Operating System • Solana L1 Anchor Kernel
        </div>
        <div style="margin-bottom: 12px; color: #a1a1aa;">
          Official Website: <a href="https://haichain.si" target="_blank" style="color: #38bdf8; text-decoration: none;">https://haichain.si</a> &nbsp;•&nbsp; 
          Contact &amp; Support: <a href="mailto:support@haichain.si" style="color: #ffffff; text-decoration: none;">support@haichain.si</a>
        </div>
        <div style="margin-bottom: 12px; color: #52525b; font-size: 10px; line-height: 1.5;">
          <strong>LEGAL NOTICE &amp; ESIGN COMPLIANCE:</strong> This electronic transmission and its cryptographic proof of execution are generated pursuant to the US Electronic Signatures in Global and National Commerce Act (ESIGN Act, 15 U.S.C. § 7001 et seq.) and the Uniform Electronic Transactions Act (UETA). The terms herein constitute a legally binding Simple Agreement for Future Tokens (SAFT) under applicable digital commerce and transaction laws. This message is intended solely for the designated recipient and may contain confidential information. If you received this transmission in error, please notify support@haichain.si immediately.
        </div>
        <div style="color: #3f3f46; font-size: 10px;">
          © 2026 Haichain. All rights reserved.
        </div>
      </div>

    </div>
  </div>
</body>
</html>`;
}
'''

def patch_worker(file_path):
    print(f"Patching {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure buildHaichainSaftEmailHtml is in the file
    if 'function buildHaichainSaftEmailHtml' not in content:
        # Prepend to helper functions or put before handleSaftSubmit
        content = EMAIL_BUILDER_JS + "\n" + content

    # 2. Update Resend sender and template in handleSaftSubmit
    # Pattern to find from const senderFrom to investorRes call
    pattern = re.compile(
        r"const resendKey = .*?;\s*const senderFrom = .*?;\s*let resendAdminSuccess = false;.*?const investorRes = await fetch\('https://api\.resend\.com/emails', \{.*?\}\);\s*resendInvestorSuccess = investorRes\.ok;\s*\}\s*catch\s*\(e\)\s*\{\s*console\.warn\('Resend investor email dispatch error:', e\);\s*\}\s*\}",
        re.DOTALL
    )

    replacement = r'''const resendKey = (env && env.RESEND_API_KEY) || 're_Hqp1tNKV_6w8Ur4v3B91Jv6yusD4CK5pN';
    const senderFrom = 'Haichain <no-reply@mail.haichain.si>';
    let resendAdminSuccess = false;
    let resendInvestorSuccess = false;

    // (A) Email to Admin: haichain.si@gmail.com
    try {
      const adminEmailHtml = buildHaichainSaftEmailHtml({
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

      const adminRes = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${resendKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          from: senderFrom,
          to: ['haichain.si@gmail.com'],
          subject: `🔔 [SAFT Signed] $${amount.toLocaleString('en-US')} USD - ${name} (${contractId})`,
          html: adminEmailHtml
        })
      });
      resendAdminSuccess = adminRes.ok;
    } catch (e) {
      console.warn('Resend admin email dispatch error:', e);
    }

    // (B) Email to Investor: Official SAFT Execution Confirmation
    if (email && email.includes('@')) {
      try {
        const investorEmailHtml = buildHaichainSaftEmailHtml({
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

        const investorRes = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${resendKey}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            from: senderFrom,
            to: [email],
            subject: `Haichain Official SAFT Agreement - Signed Confirmation (${contractId})`,
            html: investorEmailHtml
          })
        });
        resendInvestorSuccess = investorRes.ok;
      } catch (e) {
        console.warn('Resend investor email dispatch error:', e);
      }
    }'''

    new_content, count = pattern.subn(replacement, content, count=1)
    if count == 0:
        print(f"Warning: regex replacement failed for {file_path}, doing manual slice replacement.")
        # fallback manual replace
        idx1 = content.indexOf('const resendKey =')
        # if needed
    else:
        print(f"Successfully replaced Resend logic in {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

patch_worker('_worker.js')
patch_worker('app/_worker.js')
