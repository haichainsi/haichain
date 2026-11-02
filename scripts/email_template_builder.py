def build_email_template(is_admin, contract_id, name, email, amount, tokens, wallet, treasury, hash_hex, timestamp, lang='vi'):
    contract_pdf_url = "https://haichain.si/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI_EN.pdf"
    is_vi = (lang == 'vi')
    
    tge_val = int(tokens * 0.01)
    
    title = "THÔNG BÁO HỢP ĐỒNG SAFT PRE-SEED ĐÃ ĐƯỢC KÝ" if is_admin else ("Xác Nhận Ký Kết Hợp Đồng SAFT Pre-Seed" if is_vi else "Pre-Seed SAFT Agreement Execution Confirmation")
    badge = "✓ CRYPTOGRAPHICALLY SIGNED &amp; RECORDED"
    
    intro = f"""Kính gửi <strong>{name}</strong>,<br><br>
Hợp đồng Tương lai Chuyển đổi Token (SAFT - Simple Agreement for Future Tokens) của bạn cho Vòng Chiến Lược Pre-Seed đã được ký kết điện tử và niêm phong mật mã học thành công theo chuẩn <strong>US ESIGN Act &amp; Luật Giao Dịch Điện Tử 2023</strong>.""" if is_vi else f"""Dear <strong>{name}</strong>,<br><br>
Your Simple Agreement for Future Tokens (SAFT) for the <strong>HAICHAIN Pre-Seed Strategic Round</strong> has been cryptographically signed and officially recorded pursuant to the <strong>US Electronic Signatures in Global and National Commerce Act (ESIGN Act) &amp; UETA standards</strong>."""

    if is_admin:
        intro = f"""Hệ thống vừa ghi nhận một Hợp đồng SAFT Vòng Chiến Lược Pre-Seed mới được ký kết điện tử trực tuyến và xác thực mật mã học thành công."""

    btn_pdf_text = "📄 Xem File Hợp Đồng SAFT (PDF)" if is_vi else "📄 View Official SAFT Agreement (PDF)"
    btn_dash_text = "Truy Cập Dashboard" if is_vi else "Access HAICHAIN Dashboard"
    action_lead = "Bản sao Hợp đồng SAFT chính thức đã được xuất bản và bảo vệ an toàn. Bạn có thể mở xem trực tiếp hoặc tải về máy toàn văn hợp đồng tại đây:" if is_vi else "Your official SAFT Agreement has been published and cryptographically sealed. You can view or download the complete contract document below:"
    
    treasury_note = "Nguồn vốn đầu tư được bảo vệ tại Kho Bạc Squads Multi-Sig trên Solana Mainnet. Token $HAISI sẽ được phân phối tự động tới ví thụ hưởng của bạn ngay khi giao thức chính thức tiến hành TGE." if is_vi else "Investment funds are secured in the Squads Multi-Sig Treasury on Solana Mainnet. Your $HAISI tokens will be minted and transferred directly to your beneficiary wallet upon Token Generation Event (TGE)."

    return f"""<!DOCTYPE html>
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
          {badge}
        </span>
      </div>

      <!-- Main Headline & Intro -->
      <h1 style="margin: 0 0 16px 0; font-size: 21px; font-weight: 700; color: #ffffff; letter-spacing: -0.5px;">
        {title}
      </h1>
      <p style="margin: 0 0 24px 0; font-size: 13px; line-height: 1.6; color: #d4d4d8;">
        {intro}
      </p>

      <!-- Contract Key Values Matrix -->
      <div style="background-color: #141417; border: 1px solid #27272a; border-radius: 14px; padding: 22px; margin-bottom: 28px;">
        <table style="width: 100%; border-collapse: collapse; font-size: 13px; line-height: 1.6;">
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; width: 40%; border-bottom: 1px solid #1f1f23;">Mã Hợp Đồng (Contract ID):</td>
            <td style="padding: 8px 0; font-weight: 700; color: #ffffff; font-family: monospace; border-bottom: 1px solid #1f1f23;">{contract_id}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Nhà Đầu Tư (Signatory):</td>
            <td style="padding: 8px 0; font-weight: 600; color: #ffffff; border-bottom: 1px solid #1f1f23;">{name}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Email Đăng Ký:</td>
            <td style="padding: 8px 0; color: #38bdf8; font-family: monospace; border-bottom: 1px solid #1f1f23;">{email}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Số Tiền Đầu Tư:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #4ade80; font-size: 15px; border-bottom: 1px solid #1f1f23;">${amount:,} USD (USDT)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Quyền Phân Bổ Token:</td>
            <td style="padding: 8px 0; font-weight: 700; color: #ffffff; border-bottom: 1px solid #1f1f23;">{tokens:,} $HAISI (@ $0.007)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Giá Trị Dự Kiến Tại TGE:</td>
            <td style="padding: 8px 0; color: #a1a1aa; font-weight: 600; border-bottom: 1px solid #1f1f23;">${tge_val:,} USD (+42.8%)</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Ví Solana Nhận Token:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 11px; color: #ffffff; word-break: break-all; border-bottom: 1px solid #1f1f23;">{wallet}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Kho Bạc Multi-Sig Nhận Vốn:</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 11px; color: #a1a1aa; word-break: break-all; border-bottom: 1px solid #1f1f23;">{treasury}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa; border-bottom: 1px solid #1f1f23;">Mã Băm Bảo Chứng (SHA-256):</td>
            <td style="padding: 8px 0; font-family: monospace; font-size: 10px; color: #71717a; word-break: break-all; border-bottom: 1px solid #1f1f23;">{hash_hex}</td>
          </tr>
          <tr>
            <td style="padding: 8px 0; color: #a1a1aa;">Thời Gian Ký (UTC):</td>
            <td style="padding: 8px 0; color: #ffffff; font-size: 12px;">{timestamp}</td>
          </tr>
        </table>
      </div>

      <!-- Prominent Contract File Attachment & Dashboard Link -->
      <div style="background-color: #121215; border: 1px solid #27272a; border-radius: 14px; padding: 24px; text-align: center; margin-bottom: 28px;">
        <p style="margin: 0 0 16px 0; font-size: 13px; line-height: 1.6; color: #d4d4d8;">
          {action_lead}
        </p>
        <div style="text-align: center;">
          <a href="{contract_pdf_url}" target="_blank" style="display: inline-block; background-color: #ffffff; color: #000000; font-weight: 700; font-size: 13px; padding: 13px 32px; border-radius: 9999px; text-decoration: none; margin: 6px; box-shadow: 0 4px 14px rgba(255,255,255,0.15);">
            {btn_pdf_text}
          </a>
          <a href="https://haichain.si/dashboard" target="_blank" style="display: inline-block; background-color: #18181b; color: #ffffff; font-weight: 600; font-size: 13px; padding: 13px 26px; border-radius: 9999px; text-decoration: none; border: 1px solid #3f3f46; margin: 6px;">
            {btn_dash_text}
          </a>
        </div>
      </div>

      <p style="margin: 0 0 28px 0; font-size: 12px; line-height: 1.6; color: #71717a;">
        {treasury_note}
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
</html>"""
