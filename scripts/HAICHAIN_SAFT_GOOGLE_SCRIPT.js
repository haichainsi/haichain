/**
 * ==============================================================================
 * HAICHAIN PRE-SEED SAFT AGREEMENT - GOOGLE APPS SCRIPT WEBHOOK ENGINE
 * ==============================================================================
 * Tự động hóa:
 * 1. Ghi thông tin Hợp đồng SAFT vào Google Sheets
 * 2. Gửi Email thông báo có kèm link chứng chỉ cho Admin (haichain.si@gmail.com)
 * 3. Gửi Email xác nhận chính thức cho Nhà Đầu Tư (Investor)
 */

function doPost(e) {
  try {
    var rawData = e.postData.contents;
    var data = JSON.parse(rawData);
    
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Tạo tiêu đề cột tự động nếu là bảng tính mới
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "Thời Gian (UTC)",
        "Mã Hợp Đồng (Contract ID)",
        "Tên Nhà Đầu Tư / Quỹ",
        "Email",
        "Số Tiền Đầu Tư ($ USD)",
        "Quyền Phân Bổ ($HAISI)",
        "Địa Chỉ Ví Nhận Token (Solana)",
        "Kho Bạc Multi-Sig",
        "Mã Băm Bảo Chứng (SHA-256 Hash)"
      ]);
      sheet.getRange(1, 1, 1, 9).setFontWeight("bold").setBackground("#0c0c0e").setFontColor("#ffffff");
      sheet.setFrozenRows(1);
    }
    
    var timestamp = data.timestamp || new Date().toISOString();
    var contractId = data.contractId || "SAFT-HAI-" + new Date().getTime();
    var name = data.name || "N/A";
    var email = data.email || "N/A";
    var amount = Number(data.amount) || 0;
    var tokens = Number(data.tokens) || Math.floor(amount / 0.007);
    var wallet = data.wallet || "N/A";
    var treasury = data.treasury || "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3";
    var hashHex = data.hashHex || "N/A";
    
    // 1. Ghi vào Google Sheets
    sheet.appendRow([
      timestamp,
      contractId,
      name,
      email,
      amount,
      tokens,
      wallet,
      treasury,
      hashHex
    ]);
    
    // 2. Gửi Email Thông Báo Cho Admin (haichain.si@gmail.com)
    var adminEmail = "haichain.si@gmail.com";
    var adminSubject = "🔔 [HAICHAIN SAFT] Nhà đầu tư mới ký hợp đồng: $" + amount.toLocaleString() + " - " + name;
    var adminHtml = 
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
      "</div>";
      
    MailApp.sendEmail({
      to: adminEmail,
      subject: adminSubject,
      htmlBody: adminHtml
    });
    
    // 3. Gửi Email Xác Nhận Chính Thức Cho Nhà Đầu Tư
    if (email && email.indexOf("@") > -1) {
      var investorSubject = "Xác nhận ký kết Hợp đồng SAFT HAICHAIN (" + contractId + ") - Proof of Execution";
      var investorHtml = 
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
        "</div>";
        
      MailApp.sendEmail({
        to: email,
        subject: investorSubject,
        htmlBody: investorHtml
      });
    }
    
    return ContentService.createTextOutput(JSON.stringify({ status: "success", contractId: contractId }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
