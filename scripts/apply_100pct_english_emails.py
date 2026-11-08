import re

def update_worker_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update investorSubject to always be English
    old_subj_pattern = r"const investorSubject = isVi\s*\?\s*`[^`]+`\s*:\s*`[^`]+`;"
    new_subj = "const investorSubject = `HAICHAIN Official SAFT Agreement - Signed Confirmation (${contractId})`;"
    content = re.sub(old_subj_pattern, new_subj, content)

    # 2. Update investorHtml fallback to 100% English (eliminate isVi ternaries)
    old_investor_html = r"""    // 2\. Build Investor HTML Email
    const investorHtml = data\.investorHtml \|\| `[\s\S]*?</div>`;"""

    new_investor_html = """    // 2. Build Investor HTML Email (100% English for all recipients)
    const investorHtml = data.investorHtml || `
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 620px; margin: 0 auto; padding: 32px 24px; background-color: #0c0c0e; color: #ffffff; border-radius: 16px; border: 1px solid #27272a;">
  <div style="border-bottom: 1px solid #27272a; padding-bottom: 20px; margin-bottom: 24px;">
    <h2 style="margin: 0; font-size: 20px; font-weight: 700; color: #ffffff;">SAFT AGREEMENT EXECUTION CONFIRMATION</h2>
    <p style="margin: 6px 0 0 0; font-size: 13px; color: #a1a1aa;">HAICHAIN Autonomous Machine Financial Protocol</p>
  </div>
  <p style="font-size: 14px; line-height: 1.6; color: #d4d4d8;">
    Dear <strong>${name}</strong>,<br><br>Your Pre-Seed SAFT Agreement has been legally executed and recorded on the HAICHAIN cryptographic ledger.
  </p>
  <table style="width: 100%; border-collapse: collapse; font-size: 13px; line-height: 1.6; margin: 20px 0;">
    <tr><td style="padding: 10px 0; color: #a1a1aa; width: 40%;">Contract ID:</td><td style="padding: 10px 0; font-weight: bold; font-family: monospace; color: #ffffff;">${contractId}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Investment Amount:</td><td style="padding: 10px 0; font-weight: bold; color: #ffffff; font-size: 15px;">$${amount.toLocaleString('en-US')} USD (USDT)</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Token Allocation:</td><td style="padding: 10px 0; font-weight: bold; color: #ffffff;">${tokens.toLocaleString('en-US')} $HAISI (@ $0.007)</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Beneficiary Wallet:</td><td style="padding: 10px 0; font-family: monospace; font-size: 11px; color: #ffffff; word-break: break-all;">${wallet}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Haichain Treasury Vault:</td><td style="padding: 10px 0; font-family: monospace; font-size: 11px; color: #a1a1aa; word-break: break-all;">${treasury}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Audit Hash SHA-256:</td><td style="padding: 10px 0; font-family: monospace; font-size: 10px; color: #71717a; word-break: break-all;">${hashHex}</td></tr>
    <tr><td style="padding: 10px 0; color: #a1a1aa;">Execution Time (UTC):</td><td style="padding: 10px 0; color: #ffffff;">${timestamp}</td></tr>
  </table>
  <div style="margin-top: 24px; padding-top: 18px; border-top: 1px solid #27272a; text-align: center;">
    <a href="https://haichain.si/dashboard" style="display: inline-block; background-color: #ffffff; color: #000000; font-weight: bold; font-size: 13px; padding: 10px 24px; border-radius: 9999px; text-decoration: none;">
      Check Your Vesting Vault
    </a>
  </div>
</div>`;"""

    content = re.sub(old_investor_html, new_investor_html, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated worker file: {filepath}')


def update_pdf_modal(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # In submission payload, ensure lang is always 'en'
    content = content.replace("isAdmin: true,\n            lang: lang || 'vi'", "isAdmin: true,\n            lang: 'en'")
    content = content.replace("isAdmin: true,\r\n            lang: lang || 'vi'", "isAdmin: true,\r\n            lang: 'en'")

    content = content.replace("isAdmin: false,\n            lang: lang || 'vi'", "isAdmin: false,\n            lang: 'en'")
    content = content.replace("isAdmin: false,\r\n            lang: lang || 'vi'", "isAdmin: false,\r\n            lang: 'en'")

    content = content.replace("investorHtml,\n            lang: lang || 'vi'", "investorHtml,\n            lang: 'en'")
    content = content.replace("investorHtml,\r\n            lang: lang || 'vi'", "investorHtml,\r\n            lang: 'en'")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated pdf modal file: {filepath}')


def update_google_script(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. adminSubject and investorSubject
    content = content.replace(
        'var adminSubject = "🔔 [HAICHAIN SAFT] Nhà đầu tư mới ký hợp đồng: $" + amount.toLocaleString() + " - " + name;',
        'var adminSubject = "🔔 [SAFT Signed] $" + amount.toLocaleString("en-US") + " USD - " + name + " (" + contractId + ")";'
    )
    content = content.replace(
        'var investorSubject = "Xác nhận ký kết Hợp đồng SAFT HAICHAIN (" + contractId + ") - Proof of Execution";',
        'var investorSubject = "HAICHAIN Official SAFT Agreement - Signed Confirmation (" + contractId + ")";'
    )

    # 2. adminHtml
    old_admin_html = """    var adminHtml = 
      "<div style='font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; max-width:600px; margin:0 auto; padding:24px; background:#0c0c0e; color:#ffffff; border-radius:16px;'>" +
        "<h2 style='color:#ffffff; margin-top:0; border-bottom:1px solid #27272a; padding-bottom:12px;'>🔔 HỢP ĐỒNG SAFT PRE-SEED VỪA ĐƯỢC KÝ KẾT</h2>" +
        "<table style='width:100%; border-collapse:collapse; color:#d4d4d8; font-size:14px; margin:20px 0;'>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Mã Hợp Đồng:</td><td style='font-weight:bold; color:#ffffff; font-family:monospace;'>" + contractId + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Nhà Đầu Tư:</td><td style='font-weight:bold; color:#ffffff;'>" + name + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Email Liên Hệ:</td><td>" + email + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Số Tiền Đầu Tư:</td><td style='color:#4ade80; font-weight:bold;'>$" + amount.toLocaleString() + " USD (USDT)</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Quyền Phân Bổ:</td><td style='font-weight:bold; color:#ffffff;'>" + tokens.toLocaleString() + " $HAISI (@ $0.007)</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Ví Solana Nhận:</td><td style='font-family:monospace; font-size:12px; color:#ffffff;'>" + wallet + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Kho Bạc Nhận:</td><td style='font-family:monospace; font-size:12px; color:#ffffff;'>" + treasury + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Mã SHA-256:</td><td style='font-family:monospace; font-size:11px; color:#a1a1aa; word-break:break-all;'>" + hashHex + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Thời Gian (UTC):</td><td>" + timestamp + "</td></tr>" +
        "</table>" +
        "<p style='font-size:12px; color:#71717a; border-top:1px solid #27272a; padding-top:12px; margin-bottom:0;'>HAICHAIN Autonomous Machine Financial Protocol • Universal SAFT Engine</p>" +
      "</div>";"""

    new_admin_html = """    var adminHtml = 
      "<div style='font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; max-width:600px; margin:0 auto; padding:24px; background:#0c0c0e; color:#ffffff; border-radius:16px;'>" +
        "<h2 style='color:#ffffff; margin-top:0; border-bottom:1px solid #27272a; padding-bottom:12px;'>🔔 NEW PRE-SEED SAFT AGREEMENT SIGNED</h2>" +
        "<table style='width:100%; border-collapse:collapse; color:#d4d4d8; font-size:14px; margin:20px 0;'>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Contract ID:</td><td style='font-weight:bold; color:#ffffff; font-family:monospace;'>" + contractId + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Signatory:</td><td style='font-weight:bold; color:#ffffff;'>" + name + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Email:</td><td>" + email + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Investment Amount:</td><td style='color:#4ade80; font-weight:bold;'>$" + amount.toLocaleString('en-US') + " USD (USDT)</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Token Allocation:</td><td style='font-weight:bold; color:#ffffff;'>" + tokens.toLocaleString('en-US') + " $HAISI (@ $0.007)</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Beneficiary Wallet:</td><td style='font-family:monospace; font-size:12px; color:#ffffff;'>" + wallet + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Haichain Treasury Vault:</td><td style='font-family:monospace; font-size:12px; color:#ffffff;'>" + treasury + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>SHA-256 Audit Hash:</td><td style='font-family:monospace; font-size:11px; color:#a1a1aa; word-break:break-all;'>" + hashHex + "</td></tr>" +
          "<tr><td style='padding:8px 0; color:#a1a1aa;'>Timestamp (UTC):</td><td>" + timestamp + "</td></tr>" +
        "</table>" +
        "<p style='font-size:12px; color:#71717a; border-top:1px solid #27272a; padding-top:12px; margin-bottom:0;'>HAICHAIN Autonomous Machine Financial Protocol • Universal SAFT Engine</p>" +
      "</div>";"""

    content = content.replace(old_admin_html, new_admin_html)

    # 3. investorHtml
    old_investor_html = """      var investorHtml = 
        "<div style='font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; max-width:600px; margin:0 auto; padding:24px; background:#0c0c0e; color:#ffffff; border-radius:16px;'>" +
          "<h2 style='color:#ffffff; margin-top:0; border-bottom:1px solid #27272a; padding-bottom:12px;'>XÁC NHẬN KÝ KẾT HỢP ĐỒNG SAFT</h2>" +
          "<p style='color:#e4e4e7; line-height:1.6;'>Kính gửi <strong>" + name + "</strong>,</p>" +
          "<p style='color:#d4d4d8; line-height:1.6;'>Cảm ơn bạn đã tham gia Vòng Chiến Lược Pre-Seed của <strong>HAICHAIN</strong> (Universal Autonomous Machine Financial &amp; Cognitive Operating System). Hợp đồng SAFT trực tuyến của bạn đã được thực thi và chứng thực mật mã học thành công theo chuẩn US ESIGN Act &amp; Luật GDĐT.</p>" +
          "<div style='background:#18181b; border:1px solid #27272a; border-radius:12px; padding:16px; margin:20px 0;'>" +
            "<div style='margin-bottom:8px; font-size:13px; color:#a1a1aa;'>MÃ HỢP ĐỒNG: <span style='color:#ffffff; font-family:monospace; font-weight:bold;'>" + contractId + "</span></div>" +
            "<div style='margin-bottom:8px; font-size:13px; color:#a1a1aa;'>SỐ TIỀN ĐẦU TƯ: <span style='color:#4ade80; font-weight:bold;'>$" + amount.toLocaleString() + " USD (USDT)</span></div>" +
            "<div style='margin-bottom:8px; font-size:13px; color:#a1a1aa;'>PHÂN BỔ TOKEN: <span style='color:#ffffff; font-weight:bold;'>" + tokens.toLocaleString() + " $HAISI (@ $0.007)</span></div>" +
            "<div style='margin-bottom:8px; font-size:13px; color:#a1a1aa;'>VÍ NHẬN TOKEN TẠI TGE: <br><span style='color:#ffffff; font-family:monospace; font-size:11px;'>" + wallet + "</span></div>" +
            "<div style='font-size:13px; color:#a1a1aa;'>MÃ BĂM BẢO CHỨNG (SHA-256): <br><span style='color:#71717a; font-family:monospace; font-size:10px; word-break:break-all;'>" + hashHex + "</span></div>" +
          "</div>" +
          "<p style='color:#a1a1aa; font-size:13px; line-height:1.6;'>Toàn bộ nguồn vốn được bảo vệ tại Kho Bạc Squads Multi-Sig Mainnet: <code>" + treasury + "</code> và token sẽ được phân phối tự động tới ví Solana của bạn tại thời điểm TGE.</p>" +
          "<p style='margin-top:24px; color:#ffffff; font-size:13px;'>Trân trọng,<br><strong>HAICHAIN Autonomous Protocol Foundation</strong><br><a href='https://haichain.si' style='color:#38bdf8; text-decoration:none;'>https://haichain.si</a></p>" +
        "</div>";"""

    new_investor_html = """      var investorHtml = 
        "<div style='font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; max-width:600px; margin:0 auto; padding:24px; background:#0c0c0e; color:#ffffff; border-radius:16px;'>" +
          "<h2 style='color:#ffffff; margin-top:0; border-bottom:1px solid #27272a; padding-bottom:12px;'>SAFT AGREEMENT EXECUTION CONFIRMATION</h2>" +
          "<p style='color:#e4e4e7; line-height:1.6;'>Dear <strong>" + name + "</strong>,</p>" +
          "<p style='color:#d4d4d8; line-height:1.6;'>Thank you for participating in the Pre-Seed Strategic Round of <strong>HAICHAIN</strong> (The Financial Operating System for The Autonomous Machine Era). Your Simple Agreement for Future Tokens (SAFT) has been legally executed and recorded on the HAICHAIN cryptographic ledger pursuant to the US ESIGN Act (15 U.S.C. § 7001) &amp; UETA standards.</p>" +
          "<div style='background:#18181b; border:1px solid #27272a; border-radius:12px; padding:16px; margin:20px 0;'>" +
            "<div style='margin-bottom:8px; font-size:13px; color:#a1a1aa;'>CONTRACT ID: <span style='color:#ffffff; font-family:monospace; font-weight:bold;'>" + contractId + "</span></div>" +
            "<div style='margin-bottom:8px; font-size:13px; color:#a1a1aa;'>INVESTMENT AMOUNT: <span style='color:#4ade80; font-weight:bold;'>$" + amount.toLocaleString('en-US') + " USD (USDT)</span></div>" +
            "<div style='margin-bottom:8px; font-size:13px; color:#a1a1aa;'>TOKEN ALLOCATION: <span style='color:#ffffff; font-weight:bold;'>" + tokens.toLocaleString('en-US') + " $HAISI (@ $0.007)</span></div>" +
            "<div style='margin-bottom:8px; font-size:13px; color:#a1a1aa;'>BENEFICIARY WALLET: <br><span style='color:#ffffff; font-family:monospace; font-size:11px;'>" + wallet + "</span></div>" +
            "<div style='font-size:13px; color:#a1a1aa;'>SHA-256 AUDIT HASH: <br><span style='color:#71717a; font-family:monospace; font-size:10px; word-break:break-all;'>" + hashHex + "</span></div>" +
          "</div>" +
          "<p style='color:#a1a1aa; font-size:13px; line-height:1.6;'>All investment funds are secured in the Squads Multi-Sig Treasury on Solana Mainnet: <code>" + treasury + "</code> and your $HAISI tokens will be minted and transferred directly to your beneficiary wallet upon the Token Generation Event (TGE).</p>" +
          "<p style='margin-top:24px; color:#ffffff; font-size:13px;'>Sincerely,<br><strong>HAICHAIN Autonomous Protocol Foundation</strong><br><a href='https://haichain.si' style='color:#38bdf8; text-decoration:none;'>https://haichain.si</a></p>" +
        "</div>";"""

    content = content.replace(old_investor_html, new_investor_html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated Google script file: {filepath}')


if __name__ == '__main__':
    update_worker_file('_worker.js')
    update_worker_file('app/_worker.js')
    update_worker_file('server/cloud-mcp-functions/api/saft-submit.js')
    update_worker_file('server/haichain-mcp-worker.js')
    update_pdf_modal('pdf-modal.js')
    update_pdf_modal('app/pdf-modal.js')
    update_google_script('scripts/HAICHAIN_SAFT_GOOGLE_SCRIPT.js')
    print('All updates applied successfully!')
