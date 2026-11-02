import re

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

def patch_pdf_modal(file_path):
    print(f"Patching {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add buildHaichainSaftEmailHtml if not present
    if 'function buildHaichainSaftEmailHtml' not in content:
        content = EMAIL_BUILDER_JS + "\n" + content

    # 2. Fix signature drawing startDraw to render a dot immediately
    startdraw_pattern = re.compile(
        r"function startDraw\(e\) \{.*?ctx\.moveTo\(coords\.x, coords\.y\);\s*\}",
        re.DOTALL
    )
    startdraw_replacement = '''function startDraw(e) {
      isDrawing = true;
      strokeCount++;
      pointsDrawn++;
      hasSigned = true;
      if (placeholder) placeholder.classList.add('hidden');

      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#000000';
      ctx.fillStyle = '#000000';

      const coords = getCanvasCoords(e);
      lastX = coords.x;
      lastY = coords.y;
      
      // Render dot immediately so single clicks / taps leave physical ink
      ctx.beginPath();
      ctx.arc(coords.x, coords.y, 1.25, 0, Math.PI * 2);
      ctx.fill();

      ctx.beginPath();
      ctx.moveTo(coords.x, coords.y);
    }'''

    content, c1 = startdraw_pattern.subn(startdraw_replacement, content, count=1)
    print(f"startDraw patched: {c1}")

    # 3. Fix event listeners for canvas to support pointer + touch + mouse flawlessly
    listeners_pattern = re.compile(
        r"if \(window\.PointerEvent\) \{.*?canvas\.addEventListener\('touchcancel', stopDraw\);\s*\}",
        re.DOTALL
    )
    listeners_replacement = '''// Unified Pointer + Touch + Mouse event listeners
    if (window.PointerEvent) {
      canvas.addEventListener('pointerdown', (e) => {
        try { canvas.setPointerCapture(e.pointerId); } catch (_) {}
        startDraw(e);
      });
      canvas.addEventListener('pointermove', draw);
      canvas.addEventListener('pointerup', (e) => {
        try { canvas.releasePointerCapture(e.pointerId); } catch (_) {}
        stopDraw();
      });
      canvas.addEventListener('pointercancel', stopDraw);
      canvas.addEventListener('pointerleave', stopDraw);
    }

    // Always attach touch listeners for rock-solid mobile compatibility
    canvas.addEventListener('touchstart', (e) => {
      if (e.cancelable) e.preventDefault();
      startDraw(e);
    }, { passive: false });
    canvas.addEventListener('touchmove', (e) => {
      if (e.cancelable) e.preventDefault();
      draw(e);
    }, { passive: false });
    canvas.addEventListener('touchend', stopDraw);
    canvas.addEventListener('touchcancel', stopDraw);

    // Fallback mouse listeners
    canvas.addEventListener('mousedown', startDraw);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDraw);
    canvas.addEventListener('mouseleave', stopDraw);'''

    content, c2 = listeners_pattern.subn(listeners_replacement, content, count=1)
    print(f"listeners patched: {c2}")

    # 4. Make isSigValid rock solid
    sig_valid_pattern = re.compile(
        r"// Validate digital signature \(accepts 1 or more strokes with genuine drawn points/pixels\)\s*let isSigValid = false;.*?if \(!isSigValid\) \{",
        re.DOTALL
    )
    sig_valid_replacement = '''// Validate digital signature (accepts drawn strokes, raster pixels, or signature data)
        let isSigValid = false;
        if (hasSigned || strokeCount > 0 || pointsDrawn > 0) {
          isSigValid = true;
        }
        try {
          const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
          const d = imgData.data;
          for (let i = 3; i < d.length; i += 8) {
            if (d[i] > 5) {
              isSigValid = true;
              hasSigned = true;
              break;
            }
          }
        } catch (_) {}
        try {
          const dataUrl = canvas.toDataURL('image/png');
          if (dataUrl && dataUrl.length > 1000) {
            isSigValid = true;
            hasSigned = true;
          }
        } catch (_) {}

        if (!isSigValid) {'''

    content, c3 = sig_valid_pattern.subn(sig_valid_replacement, content, count=1)
    print(f"isSigValid patched: {c3}")

    # 5. Replace Resend client-side dispatch with luxury email builder
    resend_pattern = re.compile(
        r"// 0\. Instant Email Notification via Resend.*?catch\(e => console\.warn\('Resend direct investor non-blocking:', e\)\);\s*\}\s*\}\s*catch\s*\(_\)\s*\{\}",
        re.DOTALL
    )
    resend_replacement = '''// 0. Dual Instant Email Notifications via Resend (Admin + Investor)
        try {
          const resendKey = 're_Hqp1tNKV_6w8Ur4v3B91Jv6yusD4CK5pN';
          const senderFrom = 'Haichain <no-reply@mail.haichain.si>';

          // (A) Send to Admin (haichain.si@gmail.com)
          const adminSubject = '🔔 [SAFT Signed] $' + amount.toLocaleString('en-US') + ' USD - ' + name + ' (' + contractId + ')';
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
            lang: lang || 'vi'
          });

          fetch('https://api.resend.com/emails', {
            method: 'POST',
            headers: {
              'Authorization': 'Bearer ' + resendKey,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              from: senderFrom,
              to: ['haichain.si@gmail.com'],
              subject: adminSubject,
              html: adminHtml
            })
          }).catch(e => console.warn('Resend direct admin non-blocking:', e));

          // (B) Send to Investor (Confirmation & Receipt)
          if (email && email.includes('@')) {
            const investorSubject = 'Haichain Official SAFT Agreement - Signed Confirmation (' + contractId + ')';
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
              lang: lang || 'vi'
            });

            fetch('https://api.resend.com/emails', {
              method: 'POST',
              headers: {
                'Authorization': 'Bearer ' + resendKey,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                from: senderFrom,
                to: [email],
                subject: investorSubject,
                html: investorHtml
              })
            }).catch(e => console.warn('Resend direct investor non-blocking:', e));
          }
        } catch (_) {}'''

    content, c4 = resend_pattern.subn(resend_replacement, content, count=1)
    print(f"resend patched: {c4}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Finished {file_path}\n")

patch_pdf_modal('app/pdf-modal.js')
patch_pdf_modal('pdf-modal.js')
