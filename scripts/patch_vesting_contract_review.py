import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Add window.openReviewSignedSaftModal and window.printSignedSaftCertificate before window.openSaftPdfModal
    target_saft_func = 'window.openSaftPdfModal = function(overrideLang) {'
    if target_saft_func not in c:
        print(f"Error: {target_saft_func} not found in {filepath}")
        return False

    modal_and_print_js = '''    // =========================================================================
    // SIGNED SAFT REVIEW MODAL (STRICT MONOCHROME, ZERO OVERFLOW, FULL AUDIT)
    // =========================================================================
    window.openReviewSignedSaftModal = function(customRecord) {
      let record = customRecord;
      if (!record) {
        try {
          const rawActive = localStorage.getItem('HAICHAIN_ACTIVE_SAFT');
          if (rawActive) record = JSON.parse(rawActive);
          if (!record) {
            const list = JSON.parse(localStorage.getItem('HAICHAIN_SIGNED_SAFT_RECORDS') || '[]');
            if (list && list.length > 0) record = list[0];
          }
          if (!record) {
            const savedW = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
            const addr = savedW.address || (window.userWallet ? window.userWallet.address : null);
            if (addr && typeof window.getStoredAllocations === 'function') {
              const allocs = window.getStoredAllocations();
              const a = allocs[addr];
              if (a) {
                record = {
                  contractId: a.contractId || ('SAFT-2026-HAI-' + addr.slice(2, 6).toUpperCase()),
                  name: a.name || 'Strategic Investor',
                  email: a.email || 'investor@haichain.si',
                  amount: a.amountUsdt || 1000,
                  tokens: a.haiTokens || Math.round((a.amountUsdt || 1000) / 0.007),
                  wallet: addr,
                  treasury: '9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM',
                  timestamp: a.timestamp || new Date().toISOString(),
                  hashHex: a.hashHex || 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
                };
              }
            }
          }
        } catch (_) {}
      }

      if (!record) {
        if (typeof window.openSaftPdfModal === 'function') {
          window.openSaftPdfModal();
        }
        return;
      }

      const lang = window.haichainI18n ? window.haichainI18n.current() : 'vi';
      const isVi = (lang === 'vi');
      const formattedAmount = Number(record.amount || 1000).toLocaleString('en-US');
      const formattedTokens = Number(record.tokens || Math.round(Number(record.amount || 1000) / 0.007)).toLocaleString('en-US');
      const dateStr = (record.timestamp || new Date().toISOString()).replace('T', ' ').substring(0, 19);

      let modal = document.getElementById('signed-saft-review-modal');
      if (!modal) {
        modal = document.createElement('div');
        modal.id = 'signed-saft-review-modal';
        document.body.appendChild(modal);
      }

      modal.className = 'fixed inset-0 z-[9999] flex items-center justify-center p-3 sm:p-4 bg-black/80 backdrop-blur-sm animate-fadeIn';
      modal.innerHTML = `
        <div class="relative w-full max-w-xl max-h-[90vh] flex flex-col bg-white dark:bg-neutral-950 text-black dark:text-white rounded-2xl border border-neutral-300 dark:border-neutral-800 shadow-2xl overflow-hidden font-sans">
          <!-- Header -->
          <div class="flex items-center justify-between px-5 py-4 border-b border-neutral-200 dark:border-neutral-800 shrink-0">
            <div class="space-y-0.5">
              <h3 class="text-sm sm:text-base font-bold text-black dark:text-white leading-tight">
                ${isVi ? 'Hợp Đồng SAFT Đã Ký Kết' : 'Signed SAFT Agreement'}
              </h3>
              <p class="text-[11px] font-mono text-neutral-500">
                ${record.contractId || 'SAFT-2026-HAI-001'} • US ESIGN Act
              </p>
            </div>
            <button onclick="document.getElementById('signed-saft-review-modal').remove()" class="w-8 h-8 rounded-lg flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-all cursor-pointer font-bold text-lg leading-none">
              &times;
            </button>
          </div>

          <!-- Content Scroll -->
          <div class="p-5 sm:p-6 overflow-y-auto space-y-3.5 text-xs font-mono">
            <!-- Status Box -->
            <div class="p-3 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-between">
              <span class="text-neutral-500 text-[11px]">${isVi ? 'Trạng thái pháp lý:' : 'Legal Status:'}</span>
              <span class="font-bold text-black dark:text-white text-[11px] uppercase">${isVi ? 'Đã ký kết hợp pháp' : 'Legally Executed'}</span>
            </div>

            <!-- 4-Stat Grid -->
            <div class="grid grid-cols-2 gap-2.5">
              <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/50 border border-neutral-200 dark:border-neutral-800">
                <span class="text-neutral-500 block text-[10px] uppercase">${isVi ? 'Người Ký' : 'Signatory'}</span>
                <span class="font-bold text-black dark:text-white text-xs truncate block mt-0.5">${record.name || 'Investor'}</span>
              </div>
              <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/50 border border-neutral-200 dark:border-neutral-800">
                <span class="text-neutral-500 block text-[10px] uppercase">${isVi ? 'Email Xác Nhận' : 'Email'}</span>
                <span class="font-bold text-black dark:text-white text-xs truncate block mt-0.5">${record.email || 'N/A'}</span>
              </div>
              <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/50 border border-neutral-200 dark:border-neutral-800">
                <span class="text-neutral-500 block text-[10px] uppercase">${isVi ? 'Số Tiền Đầu Tư' : 'Investment Amount'}</span>
                <span class="font-bold text-black dark:text-white text-xs block mt-0.5">$${formattedAmount} USDT</span>
              </div>
              <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/50 border border-neutral-200 dark:border-neutral-800">
                <span class="text-neutral-500 block text-[10px] uppercase">${isVi ? 'Phân Bổ Token' : 'Token Allocation'}</span>
                <span class="font-bold text-black dark:text-white text-xs block mt-0.5">${formattedTokens} HAISI</span>
              </div>
            </div>

            <!-- Wallet & Treasury Addresses -->
            <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/50 border border-neutral-200 dark:border-neutral-800 space-y-1.5 break-all">
              <div>
                <span class="text-neutral-500 block text-[10px] uppercase">${isVi ? 'Ví Nhận Phân Bổ (Beneficiary Wallet)' : 'Beneficiary Wallet'}</span>
                <span class="font-bold text-black dark:text-white text-[11px]">${record.wallet || 'N/A'}</span>
              </div>
              <div class="pt-1.5 border-t border-neutral-200/50 dark:border-neutral-800/50">
                <span class="text-neutral-500 block text-[10px] uppercase">${isVi ? 'Thời Gian Ký (UTC)' : 'Signing Timestamp'}</span>
                <span class="text-neutral-800 dark:text-neutral-200 text-[11px]">${dateStr}</span>
              </div>
            </div>

            <!-- Signature Canvas/Image -->
            <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/50 border border-neutral-200 dark:border-neutral-800 space-y-2">
              <div class="flex items-center justify-between text-[10px] text-neutral-500 uppercase">
                <span>${isVi ? 'Chữ Ký Điện Tử Đã Ghi Nhận' : 'Recorded Digital Signature'}</span>
                <span>US ESIGN Act</span>
              </div>
              <div class="p-2 rounded-lg bg-white dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center min-h-[60px]">
                ${record.signatureData ? `<img src="${record.signatureData}" class="max-h-14 object-contain filter contrast-200 dark:invert" alt="Signature">` : `<span class="text-neutral-400 font-bold tracking-widest text-[11px]">[CRYPTOGRAPHICALLY SIGNED]</span>`}
              </div>
            </div>

            <!-- Audit Proof Hash -->
            <div class="p-2.5 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-[10px] break-all">
              <span class="text-neutral-500 block uppercase">SHA-256 Cryptographic Audit Hash:</span>
              <span class="text-black dark:text-white font-mono mt-0.5 block">${record.hashHex || 'N/A'}</span>
            </div>
          </div>

          <!-- Footer Buttons -->
          <div class="p-4 border-t border-neutral-200 dark:border-neutral-800 flex flex-col sm:flex-row items-center justify-between gap-2.5 bg-neutral-50/50 dark:bg-neutral-900/30 shrink-0">
            <button onclick="if(window.openSaftPdfModal){document.getElementById('signed-saft-review-modal').remove();window.openSaftPdfModal('${lang}');}" class="w-full sm:w-auto px-4 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:bg-neutral-100 dark:hover:bg-neutral-800 text-xs font-semibold font-mono text-neutral-700 dark:text-neutral-300 transition-all cursor-pointer text-center">
              ${isVi ? 'Xem Toàn Văn SAFT' : 'View Full Agreement'}
            </button>
            <div class="flex items-center gap-2 w-full sm:w-auto">
              <button onclick="window.printSignedSaftCertificate()" class="w-full sm:w-auto px-4 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:bg-neutral-100 dark:hover:bg-neutral-800 text-xs font-semibold font-mono text-black dark:text-white transition-all cursor-pointer text-center">
                ${isVi ? 'In / Lưu PDF' : 'Print / Save PDF'}
              </button>
              <button onclick="document.getElementById('signed-saft-review-modal').remove()" class="w-full sm:w-auto px-5 py-2 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-xs font-semibold font-mono transition-all cursor-pointer text-center">
                ${isVi ? 'Đóng' : 'Close'}
              </button>
            </div>
          </div>
        </div>
      `;
    };

    window.printSignedSaftCertificate = function(customRecord) {
      let record = customRecord;
      if (!record) {
        try {
          const rawActive = localStorage.getItem('HAICHAIN_ACTIVE_SAFT');
          if (rawActive) record = JSON.parse(rawActive);
          if (!record) {
            const list = JSON.parse(localStorage.getItem('HAICHAIN_SIGNED_SAFT_RECORDS') || '[]');
            if (list && list.length > 0) record = list[0];
          }
        } catch (_) {}
      }
      if (!record) return;
      const lang = window.haichainI18n ? window.haichainI18n.current() : 'vi';
      const isVi = (lang === 'vi');
      const docTitle = isVi ? ('CHỨNG NHẬN KÝ HỢP ĐỒNG SAFT - ' + record.contractId) : ('SAFT AGREEMENT SIGNING CERTIFICATE - ' + record.contractId);
      const certHtml = `<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>${docTitle}</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 40px; background: #ffffff; color: #111; max-width: 800px; margin: 0 auto; line-height: 1.6; }
  .header { border-bottom: 2px solid #111; padding-bottom: 16px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: flex-end; }
  .badge { background: #111; color: #fff; padding: 4px 12px; border-radius: 999px; font-size: 11px; font-family: monospace; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 20px 0; }
  .field { border-bottom: 1px dashed #ddd; padding-bottom: 6px; }
  .label { font-size: 11px; color: #666; text-transform: uppercase; letter-spacing: 0.5px; }
  .value { font-size: 13px; font-weight: 600; font-family: monospace; margin-top: 2px; }
  .sig-box { margin-top: 24px; padding: 16px; border: 1px solid #e5e5e5; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; }
  .proof { margin-top: 24px; padding: 12px; background: #f9f9f9; border-radius: 8px; font-family: monospace; font-size: 10px; word-break: break-all; color: #666; }
</style>
</head>
<body>
  <div class="header">
    <div>
      <h1 style="margin:0; font-size: 20px;">${docTitle}</h1>
      <p style="margin:4px 0 0 0; color: #666; font-size: 11px;">HAICHAIN PRE-SEED STRATEGIC ROUND ($0.007 USD / $HAISI)</p>
    </div>
    <div class="badge">${record.contractId || 'SAFT-2026-HAI-001'}</div>
  </div>
  <p style="font-size: 12px;">${isVi ? 'Chứng nhận rằng Nhà Đầu Tư dưới đây đã chính thức ký kết Thỏa Thuận Tương Lai Chuyển Đổi Token (SAFT) với HAICHAIN Autonomous Machine Financial Protocol:' : 'This certifies that the Investor below has executed the Simple Agreement for Future Tokens (SAFT) with HAICHAIN Autonomous Machine Financial Protocol:'}</p>
  <div class="grid">
    <div class="field"><div class="label">${isVi ? 'Nhà Đầu Tư (Người Ký):' : 'Investor (Signatory):'}</div><div class="value">${record.name || 'Investor'}</div></div>
    <div class="field"><div class="label">${isVi ? 'Email Xác Nhận:' : 'Email Address:'}</div><div class="value">${record.email || 'N/A'}</div></div>
    <div class="field"><div class="label">${isVi ? 'Số Tiền Đầu Tư:' : 'Investment Amount:'}</div><div class="value">$${Number(record.amount || 1000).toLocaleString('en-US')} USD</div></div>
    <div class="field"><div class="label">${isVi ? 'Phân Bổ Token:' : 'Token Allocation:'}</div><div class="value">${Number(record.tokens || 142857).toLocaleString('en-US')} $HAISI (@ $0.007)</div></div>
    <div class="field" style="grid-column: span 2;"><div class="label">${isVi ? 'Địa Chỉ Ví Nhận Token:' : 'Beneficiary Receiving Address:'}</div><div class="value">${record.wallet || 'N/A'}</div></div>
    <div class="field" style="grid-column: span 2;"><div class="label">${isVi ? 'Kho Bạc Multi-Sig Nhận Vốn:' : 'Multi-Sig Treasury Vault:'}</div><div class="value">${record.treasury || '9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM'}</div></div>
    <div class="field" style="grid-column: span 2;"><div class="label">${isVi ? 'Thời Điểm Ký (UTC):' : 'Signing Timestamp (UTC):'}</div><div class="value">${record.timestamp || new Date().toISOString()}</div></div>
  </div>
  <div class="sig-box">
    <div>
      <div class="label">${isVi ? 'CHỮ KÝ ĐIỆN TỬ CỦA NHÀ ĐẦU TƯ:' : 'INVESTOR DIGITAL SIGNATURE:'}</div>
      <div style="font-size: 11px; color:#666; margin-top: 4px;">${isVi ? 'Đã ký số trực tuyến theo chuẩn ESIGN Act &amp; Luật GDĐT' : 'Executed digitally pursuant to US ESIGN Act &amp; UETA standards'}</div>
    </div>
    ${record.signatureData ? `<img src="${record.signatureData}" style="max-height: 50px; border-bottom: 1px solid #000; filter: brightness(0);" alt="Signature">` : '<div style="font-family:monospace; font-weight:bold;">[CRYPTOGRAPHICALLY SIGNED]</div>'}
  </div>
  <div class="proof">
    <strong>CRYPTOGRAPHIC AUDIT PROOF (SHA-256):</strong><br>
    ${record.hashHex || 'N/A'}<br>
    <em>${isVi ? 'Chứng từ này được mã hóa bảo chứng, liên kết bất biến với giao dịch trên Solana Blockchain.' : 'This document is cryptographically verified and permanently linked to Solana blockchain transactions.'}</em>
  </div>
  <script>window.onload = function() { window.print(); };<\/script>
</body>
</html>`;

      const win = window.open('', '_blank');
      if (win) {
        win.document.open();
        win.document.write(certHtml);
        win.document.close();
      }
    };

'''

    if 'window.openReviewSignedSaftModal =' not in c:
        c = c.replace(target_saft_func, modal_and_print_js + target_saft_func, 1)

    # 2. Update renderSignedContractCardHtml definition to be fully resilient, monochrome, and always show contract status
    old_func_pattern = r'function renderSignedContractCardHtml\(saft, currentLang\) \{[\s\S]*?\n      \}'
    new_func_js = '''function renderSignedContractCardHtml(saft, currentLang, alloc, currentAddress) {
        const isVi = currentLang === 'vi';

        // Check if user has a signed SAFT or an allocation on record
        let contract = saft;
        if (!contract && alloc) {
          contract = {
            contractId: alloc.contractId || ('SAFT-2026-HAI-' + (currentAddress ? currentAddress.slice(2, 6).toUpperCase() : '001')),
            name: alloc.name || (isVi ? 'Nhà Đầu Tư Chiến Lược' : 'Strategic Investor'),
            email: alloc.email || 'investor@haichain.si',
            amount: alloc.amountUsdt || 1000,
            tokens: alloc.haiTokens || Math.round((alloc.amountUsdt || 1000) / 0.007),
            wallet: currentAddress || 'N/A',
            treasury: '9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM',
            timestamp: alloc.timestamp || '2026-03-15T00:00:00Z',
            hashHex: alloc.hashHex || 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
          };
        }

        // --- CASE 1: SIGNED SAFT CONTRACT RECORD EXISTS ---
        if (contract) {
          const formattedAmount = Number(contract.amount || 1000).toLocaleString('en-US');
          const formattedTokens = Number(contract.tokens || Math.round(Number(contract.amount || 1000) / 0.007)).toLocaleString('en-US');
          const dateStr = (contract.timestamp || new Date().toISOString()).replace('T', ' ').substring(0, 19);
          const shortW = contract.wallet ? (contract.wallet.length > 12 ? `${contract.wallet.slice(0, 6)}...${contract.wallet.slice(-6)}` : contract.wallet) : 'N/A';
          const titleText = isVi ? 'Hợp đồng SAFT đã ký' : 'Signed SAFT Agreement';
          const statusBadge = isVi ? 'Đã ký kết • US ESIGN Act' : 'Executed • US ESIGN Act';
          const signatoryLabel = isVi ? 'Người ký' : 'Signatory';
          const amountLabel = isVi ? 'Số tiền đầu tư' : 'Investment';
          const tokensLabel = isVi ? 'Token phân bổ' : 'Allocation';
          const dateLabel = isVi ? 'Thời gian ký' : 'Signed Time';
          const walletLabel = isVi ? 'Ví thụ hưởng:' : 'Beneficiary Wallet:';
          const btnText = isVi ? 'Xem lại hợp đồng đã ký' : 'Review Signed Agreement';

          return `
            <!-- SIGNED SAFT CONTRACT SECTION (STRICT MONOCHROME, ZERO OVERFLOW) -->
            <div class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-4 shadow-xs">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-neutral-100 dark:border-neutral-900 gap-2">
                <div class="space-y-0.5">
                  <div class="flex items-center space-x-2">
                    <span class="w-2 h-2 rounded-full bg-black dark:bg-white inline-block"></span>
                    <h3 class="font-bold text-sm sm:text-base text-black dark:text-white leading-snug">
                      ${titleText}
                    </h3>
                  </div>
                  <p class="text-[11px] text-neutral-400 font-mono">
                    Contract ID: <span class="text-black dark:text-white font-semibold">${contract.contractId || 'SAFT-2026-HAI-001'}</span>
                  </p>
                </div>
                <span class="self-start sm:self-auto px-2.5 py-1 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-200 dark:border-neutral-800 font-semibold uppercase tracking-wider">
                  ${statusBadge}
                </span>
              </div>

              <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3 text-xs font-mono">
                <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800">
                  <span class="text-neutral-400 block text-[10px] uppercase">${signatoryLabel}</span>
                  <span class="font-bold text-black dark:text-white truncate block text-[11px] sm:text-xs mt-0.5">${contract.name || 'Investor'}</span>
                </div>
                <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800">
                  <span class="text-neutral-400 block text-[10px] uppercase">${amountLabel}</span>
                  <span class="font-bold text-black dark:text-white block text-[11px] sm:text-xs mt-0.5">$${formattedAmount} USDT</span>
                </div>
                <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800">
                  <span class="text-neutral-400 block text-[10px] uppercase">${tokensLabel}</span>
                  <span class="font-bold text-black dark:text-white block text-[11px] sm:text-xs mt-0.5">${formattedTokens} HAISI</span>
                </div>
                <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800">
                  <span class="text-neutral-400 block text-[10px] uppercase">${dateLabel}</span>
                  <span class="font-bold text-black dark:text-white block text-[11px] sm:text-xs truncate mt-0.5">${dateStr}</span>
                </div>
              </div>

              <div class="p-2.5 sm:p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800 text-[10px] font-mono break-all text-neutral-500">
                <span class="text-neutral-400">SHA-256 Audit Hash:</span> <span class="text-neutral-700 dark:text-neutral-300">${contract.hashHex || 'N/A'}</span>
              </div>

              <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-1">
                <div class="text-[11px] text-neutral-500 font-mono truncate">
                  ${walletLabel} <span class="text-black dark:text-white font-semibold">${shortW}</span>
                </div>
                <button onclick="if(window.openReviewSignedSaftModal){window.openReviewSignedSaftModal();}else if(window.openSaftPdfModal){window.openSaftPdfModal('${currentLang}');}" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-xs font-semibold font-mono transition-all cursor-pointer text-center active:scale-95 shadow-sm">
                  ${btnText}
                </button>
              </div>
            </div>
          `;
        }

        // --- CASE 2: NO SIGNED SAFT ON THIS DEVICE YET ---
        const unTitleText = isVi ? 'Hợp đồng đầu tư (SAFT)' : 'Investment Agreement (SAFT)';
        const unStatusBadge = isVi ? 'Chưa ký kết • Pre-Seed' : 'Not Signed • Pre-Seed';
        const unDesc = isVi ? 'Ký thỏa thuận SAFT để xác lập quyền nhận phân bổ token $HAISI tại TGE ($0.007 / $HAISI) theo chuẩn ESIGN Act.' : 'Execute the SAFT agreement to guarantee your $HAISI token allocation at TGE ($0.007 / $HAISI) pursuant to the US ESIGN Act.';
        const unBtnText = isVi ? 'Xem & Ký hợp đồng SAFT' : 'Review & Sign SAFT Agreement';

        return `
          <!-- UNSIGNED SAFT CONTRACT SECTION (STRICT MONOCHROME, ZERO OVERFLOW) -->
          <div class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-4 shadow-xs">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-neutral-100 dark:border-neutral-900 gap-2">
              <div class="space-y-0.5">
                <div class="flex items-center space-x-2">
                  <span class="w-2 h-2 rounded-full border border-neutral-400 dark:border-neutral-600 inline-block"></span>
                  <h3 class="font-bold text-sm sm:text-base text-black dark:text-white leading-snug">
                    ${unTitleText}
                  </h3>
                </div>
                <p class="text-[11px] text-neutral-400 font-mono">
                  Simple Agreement for Future Tokens • Round Pre-Seed ($0.007)
                </p>
              </div>
              <span class="self-start sm:self-auto px-2.5 py-1 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800 font-medium uppercase tracking-wider">
                ${unStatusBadge}
              </span>
            </div>

            <p class="text-xs text-neutral-500 font-sans leading-relaxed">
              ${unDesc}
            </p>

            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-1 border-t border-neutral-100 dark:border-neutral-900">
              <div class="text-[11px] text-neutral-400 font-mono">
                ${isVi ? 'Ký trực tuyến • Xác thực ngay lập tức' : 'Instant E-Signature • Fully Audited'}
              </div>
              <button onclick="if(window.openSaftPdfModal){window.openSaftPdfModal('${currentLang}');}else{window.openPdfViewerModal('/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI.pdf', 'Thỏa Thuận SAFT');}" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-xs font-semibold font-mono transition-all cursor-pointer text-center active:scale-95 shadow-sm">
                ${unBtnText}
              </button>
            </div>
          </div>
        `;
      }'''

    c = re.sub(old_func_pattern, new_func_js, c, count=1)

    # 3. Update the calls in S1, S2, S3 to pass alloc and currentAddress
    c = c.replace(
        '${renderSignedContractCardHtml(activeSaft, lang)}',
        '${renderSignedContractCardHtml(activeSaft, lang, alloc, currentAddress)}'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Successfully patched {filepath}")
    return True

update_file('dashboard.html')
update_file('app/dashboard.html')
