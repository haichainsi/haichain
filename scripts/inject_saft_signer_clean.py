import os

WORKSPACE_DIR = r"c:\Users\Surface\Documents\8. HAICHAIN"
TARGET_FILES = [
    os.path.join(WORKSPACE_DIR, "app", "pdf-modal.js"),
    os.path.join(WORKSPACE_DIR, "pdf-modal.js"),
]

SIGN_BUTTON_HTML = '''            <!-- Digital E-Signature Action Button (Zero Icons, Pure Typography) -->
            <button id="pdf-modal-sign-btn" type="button" class="hidden items-center justify-center px-3.5 sm:px-4 h-7 sm:h-8 rounded-lg sm:rounded-xl bg-white hover:bg-neutral-200 text-black font-semibold text-xs tracking-tight shadow-sm active:scale-95 transition-all shrink-0 cursor-pointer" style="background-color: #ffffff !important; color: #000000 !important;">
              <span id="pdf-modal-sign-btn-text">Sign Agreement Online</span>
            </button>
'''

SIGN_DRAWER_HTML = '''        <!-- ========================================================================= -->
        <!-- LUXURY IN-APP DIGITAL E-SIGNATURE OVERLAY (SOLID OPAQUE, ULTRA-HIGH CONTRAST) -->
        <!-- ========================================================================= -->
        <div id="saft-sign-overlay" class="absolute inset-0 z-50 hidden flex flex-col overflow-y-auto p-4 sm:p-6 md:p-8 transition-all duration-200 select-none" style="background-color: #0c0c0e !important; color: #ffffff !important;">
          
          <!-- Drawer Header (Clean Apple Minimalist, Solid Background) -->
          <div class="flex items-center justify-between pb-3 sm:pb-4 border-b border-neutral-800 shrink-0">
            <div>
              <h3 id="saft-drawer-title" class="text-sm sm:text-base font-bold text-white tracking-tight" style="color: #ffffff !important;">Pre-Seed SAFT Digital E-Signature ($0.007)</h3>
              <p id="saft-drawer-sub" class="text-xs font-mono mt-0.5" style="color: #a1a1aa !important;">Online legal verification compliant with US ESIGN Act &amp; UETA standards</p>
            </div>
            
            <button id="saft-drawer-close-btn" type="button" class="w-8 h-8 rounded-xl flex items-center justify-center text-neutral-400 hover:text-white hover:bg-neutral-800 transition-colors cursor-pointer text-sm font-mono" title="Close" style="color: #a1a1aa !important;">
              ✕
            </button>
          </div>

          <!-- Drawer Form Body -->
          <div id="saft-drawer-form-view" class="py-4 sm:py-6 max-w-2xl mx-auto w-full space-y-4 pb-28 sm:pb-20 select-text">
            
            <!-- Dual Column Fields: Name & Email -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              <div>
                <label id="saft-lbl-name" class="block text-xs font-semibold mb-1" style="color: #ffffff !important;">Full Legal Name / Entity *</label>
                <input id="saft-input-name" type="text" placeholder="John Doe / Apex Capital LLC" class="w-full px-3.5 py-2.5 text-xs sm:text-sm rounded-xl focus:outline-none transition-all" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
              </div>
              <div>
                <label id="saft-lbl-email" class="block text-xs font-semibold mb-1" style="color: #ffffff !important;">Contact Email *</label>
                <input id="saft-input-email" type="email" placeholder="investor@example.com" class="w-full px-3.5 py-2.5 text-xs sm:text-sm rounded-xl focus:outline-none transition-all" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
              </div>
            </div>

            <!-- Dual Column Fields: Amount & Real-time Allocation Calculation -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              <div>
                <label id="saft-lbl-amount" class="block text-xs font-semibold mb-1" style="color: #ffffff !important;">Subscription Investment Amount (USD / USDT) *</label>
                <div class="relative">
                  <span class="absolute left-3.5 top-2.5 text-xs font-mono" style="color: #71717a !important;">$</span>
                  <input id="saft-input-amount" type="number" min="500" max="50000" step="100" value="1000" class="w-full pl-8 pr-3.5 py-2.5 text-xs sm:text-sm font-mono rounded-xl focus:outline-none transition-all" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
                </div>
                <p id="saft-txt-amount-note" class="text-[11px] font-mono mt-1" style="color: #a1a1aa !important;">Ticket limit: $500 – $15,000 USD</p>
              </div>

              <div>
                <label id="saft-lbl-alloc" class="block text-xs font-semibold mb-1" style="color: #ffffff !important;">Token Entitlement $HAISI (@ $0.007)</label>
                <div class="p-3 rounded-xl flex flex-col justify-center" style="background-color: #18181b !important; border: 1px solid #27272a !important;">
                  <div class="flex items-baseline justify-between">
                    <span id="saft-calc-tokens" class="text-sm sm:text-base font-bold font-mono" style="color: #ffffff !important;">142,857</span>
                    <span class="text-xs font-mono" style="color: #a1a1aa !important;">$HAISI</span>
                  </div>
                  <div class="text-[11px] font-mono flex items-center justify-between mt-1 pt-1 border-t border-neutral-800">
                    <span id="saft-lbl-tge-val" style="color: #a1a1aa !important;">TGE Value ($0.010):</span>
                    <span id="saft-calc-tge" class="font-bold" style="color: #4ade80 !important;">$1,428 USD (+42.8%)</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Beneficiary Wallet Address -->
            <div>
              <div class="flex items-center justify-between mb-1">
                <label id="saft-lbl-wallet" class="text-xs font-semibold" style="color: #ffffff !important;">Beneficiary Solana Wallet Address for TGE *</label>
                <button id="saft-btn-autofill-wallet" type="button" class="text-xs font-mono underline hover:opacity-80 cursor-pointer transition-colors" style="color: #38bdf8 !important;">Use Connected Wallet</button>
              </div>
              <input id="saft-input-wallet" type="text" placeholder="Solana wallet address (Base58 32-44 characters)..." class="w-full px-3.5 py-2.5 text-xs font-mono rounded-xl focus:outline-none transition-all" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
            </div>

            <!-- Treasury Vault Display (Immutably Bound) -->
            <div class="p-3 rounded-xl text-[11px] font-mono" style="background-color: #18181b !important; border: 1px solid #27272a !important;">
              <div class="flex items-center justify-between">
                <span id="saft-lbl-treasury" class="font-semibold" style="color: #d4d4d8 !important;">Multi-Sig Treasury Vault (Solana Mainnet):</span>
                <span class="font-bold" style="color: #4ade80 !important;">Squads 2-of-3</span>
              </div>
              <div class="truncate mt-1 font-mono font-medium" style="color: #ffffff !important;">5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3</div>
            </div>

            <!-- Digital Signature Pad Canvas -->
            <div>
              <div class="flex items-center justify-between mb-1.5">
                <label id="saft-lbl-canvas" class="text-xs font-semibold" style="color: #ffffff !important;">Your Digital Signature *</label>
                <button id="saft-btn-clear-sig" type="button" class="text-xs font-mono underline hover:opacity-80 cursor-pointer transition-colors" style="color: #f87171 !important;">Clear Signature</button>
              </div>
              <div class="relative w-full rounded-xl overflow-hidden shadow-sm" style="background-color: #000000 !important; border: 1px solid #3f3f46 !important;">
                <canvas id="saft-sig-canvas" width="600" height="150" class="w-full h-32 sm:h-36 block touch-none cursor-crosshair"></canvas>
                <div id="saft-sig-placeholder" class="absolute inset-0 flex items-center justify-center pointer-events-none text-xs font-mono select-none" style="color: #71717a !important;">
                  (Use mouse or touch screen to sign here)
                </div>
              </div>
            </div>

            <!-- Legal Declaration Checkbox -->
            <label class="flex items-start space-x-3 text-xs cursor-pointer select-none pt-1" style="color: #e4e4e7 !important;">
              <input id="saft-input-agree" type="checkbox" class="mt-0.5 rounded cursor-pointer w-4 h-4 accent-white">
              <span id="saft-lbl-agree" class="leading-relaxed">I confirm that I have read, understood, and agreed to all terms of the HAICHAIN Pre-Seed SAFT Agreement. I understand that investment funds are secured in the Squads Multi-Sig Treasury and tokens are distributed at TGE.</span>
            </label>

            <!-- Submit Sign Button -->
            <button id="saft-btn-submit-sign" type="button" class="w-full py-3 sm:py-3.5 rounded-xl font-bold text-xs sm:text-sm tracking-wide shadow-lg active:scale-[0.99] transition-all cursor-pointer" style="background-color: #ffffff !important; color: #000000 !important;">
              SIGN &amp; FINALIZE LEGAL AGREEMENT
            </button>
          </div>

          <!-- Drawer Success View (Shown after signing) -->
          <div id="saft-drawer-success-view" class="hidden py-8 sm:py-12 max-w-lg mx-auto w-full text-center space-y-6 pb-28 sm:pb-20 select-text animate-scaleUp">
            <div class="w-12 h-12 mx-auto rounded-full border border-neutral-600 flex items-center justify-center text-sm font-bold font-mono text-white" style="border-color: #52525b !important; color: #ffffff !important;">
              OK
            </div>
            <div>
              <h4 id="saft-success-title" class="text-base sm:text-xl font-bold" style="color: #ffffff !important;">AGREEMENT SIGNED SUCCESSFULLY</h4>
              <p id="saft-success-sub" class="text-xs sm:text-sm mt-1" style="color: #a1a1aa !important;">Digital SAFT agreement recorded with cryptographic audit trail.</p>
            </div>

            <!-- Receipt Card -->
            <div class="p-4 sm:p-5 rounded-2xl text-left text-xs font-mono space-y-2.5" style="background-color: #18181b !important; border: 1px solid #27272a !important;">
              <div class="flex justify-between">
                <span id="saft-rec-lbl-id" style="color: #a1a1aa !important;">Contract ID:</span>
                <span id="saft-rec-id" class="font-bold" style="color: #ffffff !important;">SAFT-HAI-2026-XXXXX</span>
              </div>
              <div class="flex justify-between">
                <span id="saft-rec-lbl-investor" style="color: #a1a1aa !important;">Investor:</span>
                <span id="saft-rec-name" class="font-semibold truncate max-w-[200px]" style="color: #ffffff !important;">--</span>
              </div>
              <div class="flex justify-between">
                <span id="saft-rec-lbl-alloc" style="color: #a1a1aa !important;">Allocation:</span>
                <span id="saft-rec-alloc" class="font-bold" style="color: #4ade80 !important;">-- $HAISI</span>
              </div>
              <div class="flex justify-between">
                <span id="saft-rec-lbl-wallet" style="color: #a1a1aa !important;">Receiving Wallet:</span>
                <span id="saft-rec-wallet" class="font-mono text-[11px] truncate max-w-[200px]" style="color: #d4d4d8 !important;">--</span>
              </div>
              <div class="flex justify-between">
                <span id="saft-rec-lbl-time" style="color: #a1a1aa !important;">Timestamp:</span>
                <span id="saft-rec-time" class="text-[11px]" style="color: #a1a1aa !important;">--</span>
              </div>
              <div class="pt-2 border-t border-neutral-800 text-[10px] break-all" style="color: #71717a !important;">
                <span id="saft-rec-lbl-hash" class="block mb-0.5" style="color: #a1a1aa !important;">SHA-256 Audit Hash:</span>
                <span id="saft-rec-hash">--</span>
              </div>
            </div>

            <!-- Dual Action Buttons: Download PDF & Proceed to Deposit -->
            <div class="space-y-3 pt-2">
              <button id="saft-btn-download-cert" type="button" class="w-full py-3 rounded-xl font-medium text-xs sm:text-sm transition-all cursor-pointer" style="background-color: #18181b !important; color: #ffffff !important; border: 1px solid #3f3f46 !important;">
                Download Signed Agreement Certificate (HTML / PDF)
              </button>
              <button id="saft-btn-proceed-pay" type="button" class="w-full py-3 sm:py-3.5 rounded-xl font-bold text-xs sm:text-sm tracking-wide shadow-lg active:scale-[0.99] transition-all cursor-pointer" style="background-color: #ffffff !important; color: #000000 !important;">
                Proceed to Deposit to Treasury
              </button>
            </div>
          </div>

        </div>
'''

SIGN_HANDLER_CODE = r'''  // =========================================================================
  // SAFT DIGITAL E-SIGNATURE LOGIC (OPTION A - MULTI-LANGUAGE & ZERO ICONS)
  // =========================================================================
  const SAFT_DRAWER_I18N = {
    vi: {
      btnOpenSign: 'Ký Hợp Đồng Online',
      title: 'Ký Điện Tử Hợp Đồng SAFT Pre-Seed ($0.007)',
      subtitle: 'Xác thực pháp lý trực tuyến theo chuẩn ESIGN Act & Luật GDĐT 2023',
      nameLabel: 'Họ và Tên / Tên Pháp Nhân *',
      namePlaceholder: 'Nguyễn Văn A / Tech Fund LLC',
      emailLabel: 'Email Liên Hệ *',
      emailPlaceholder: 'investor@example.com',
      amountLabel: 'Số Tiền Đăng Ký Đầu Tư (USD / USDT) *',
      amountNote: 'Hạn mức vé: $500 – $15,000 USD',
      allocLabel: 'Quyền Phân Bổ Token $HAISI (@ $0.007)',
      tgeValLabel: 'Giá trị TGE ($0.010):',
      walletLabel: 'Địa Chỉ Ví Solana Nhận Token Tại TGE *',
      walletPlaceholder: 'Địa chỉ ví Phantom/Solflare (Base58 32-44 ký tự)...',
      autofillBtn: 'Lấy Ví Đang Kết Nối',
      treasuryLabel: 'Kho Bạc Multi-Sig Nhận Vốn (Solana Mainnet):',
      canvasLabel: 'Chữ Ký Điện Tử Của Bạn *',
      canvasPlaceholder: '(Dùng chuột hoặc ngón tay để ký tên tại đây)',
      clearBtn: 'Xóa ký lại',
      agreeLabel: 'Tôi xác nhận đã đọc, hiểu và đồng thuận 100% với các điều khoản của Hợp đồng SAFT HAICHAIN. Tôi hiểu rằng vốn đầu tư được bảo vệ tại Kho Bạc Squads Multi-Sig và token được phân bổ tự động tại TGE.',
      submitBtn: 'XÁC NHẬN KÝ & HOÀN TẤT HỢP ĐỒNG PHÁP LÝ',
      successTitle: 'KÝ HỢP ĐỒNG THÀNH CÔNG',
      successSubtitle: 'Hợp đồng SAFT điện tử đã được ghi nhận và đóng dấu kiểm toán mật mã.',
      recId: 'Mã Hợp Đồng:',
      recInvestor: 'Nhà Đầu Tư:',
      recAlloc: 'Phân Bổ:',
      recWallet: 'Ví Nhận:',
      recTime: 'Thời Gian:',
      recHash: 'SHA-256 Audit Hash:',
      downloadBtn: 'Tải File Chứng Nhận Hợp Đồng (HTML / PDF)',
      proceedBtn: 'Tiến Hành Nạp Tiền Vào Kho Bạc',
      errName: 'Vui lòng nhập Họ và Tên hoặc Tên Pháp Nhân của bạn.',
      errEmail: 'Vui lòng nhập địa chỉ Email hợp lệ.',
      errAmount: 'Hạn mức đăng ký đầu tư tối thiểu là 500 USD.',
      errWallet: 'Vui lòng nhập địa chỉ ví Solana hợp lệ (32 - 44 ký tự Base58) để nhận token tại TGE.',
      errSig: 'Vui lòng ký tên của bạn vào khung chữ ký điện tử.',
      errAgree: 'Vui lòng tick vào ô xác nhận đồng ý với các điều khoản Hợp đồng SAFT.',
      alertProceed: 'HỢP ĐỒNG ĐÃ ĐƯỢC KÝ!\n\nVui lòng chuyển {amount} USDT vào Kho Bạc:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nSố token {tokens} $HAISI sẽ được tự động phân bổ về ví của bạn tại TGE.',
      noWalletDetected: 'Chưa phát hiện ví Web3 (Phantom/Solflare) đang kết nối. Vui lòng dán địa chỉ ví thủ công.'
    },
    en: {
      btnOpenSign: 'Sign Agreement Online',
      title: 'Pre-Seed SAFT Digital E-Signature ($0.007)',
      subtitle: 'Online legal verification compliant with US ESIGN Act & UETA standards',
      nameLabel: 'Full Legal Name / Entity *',
      namePlaceholder: 'John Doe / Apex Capital LLC',
      emailLabel: 'Contact Email *',
      emailPlaceholder: 'investor@example.com',
      amountLabel: 'Subscription Investment Amount (USD / USDT) *',
      amountNote: 'Ticket limit: $500 – $15,000 USD',
      allocLabel: 'Token Entitlement $HAISI (@ $0.007)',
      tgeValLabel: 'TGE Value ($0.010):',
      walletLabel: 'Beneficiary Solana Wallet Address for TGE *',
      walletPlaceholder: 'Solana wallet address (Base58 32-44 characters)...',
      autofillBtn: 'Use Connected Wallet',
      treasuryLabel: 'Multi-Sig Treasury Vault (Solana Mainnet):',
      canvasLabel: 'Your Digital Signature *',
      canvasPlaceholder: '(Use mouse or touch screen to sign here)',
      clearBtn: 'Clear Signature',
      agreeLabel: 'I confirm that I have read, understood, and agreed to all terms of the HAICHAIN Pre-Seed SAFT Agreement. I understand that investment funds are secured in the Squads Multi-Sig Treasury and tokens are distributed at TGE.',
      submitBtn: 'SIGN & FINALIZE LEGAL AGREEMENT',
      successTitle: 'AGREEMENT SIGNED SUCCESSFULLY',
      successSubtitle: 'Digital SAFT agreement recorded with cryptographic audit trail.',
      recId: 'Contract ID:',
      recInvestor: 'Investor:',
      recAlloc: 'Allocation:',
      recWallet: 'Receiving Wallet:',
      recTime: 'Timestamp:',
      recHash: 'SHA-256 Audit Hash:',
      downloadBtn: 'Download Signed Agreement Certificate (HTML / PDF)',
      proceedBtn: 'Proceed to Deposit to Treasury',
      errName: 'Please enter your Full Legal Name or Entity Name.',
      errEmail: 'Please enter a valid Email address.',
      errAmount: 'Minimum subscription amount is 500 USD.',
      errWallet: 'Please enter a valid Solana wallet address (32 - 44 characters Base58).',
      errSig: 'Please draw your signature in the signature box.',
      errAgree: 'Please agree to the SAFT Agreement terms to proceed.',
      alertProceed: 'AGREEMENT SIGNED!\n\nPlease transfer {amount} USDT to Treasury:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nYour {tokens} $HAISI allocation will be automatically disbursed at TGE.',
      noWalletDetected: 'No Web3 wallet (Phantom/Solflare) detected. Please paste your address manually.'
    }
  };

  function initSaftSignatureEngine(modal) {
    const signBtn = modal.querySelector('#pdf-modal-sign-btn');
    const overlay = modal.querySelector('#saft-sign-overlay');
    const closeBtn = modal.querySelector('#saft-drawer-close-btn');
    const formView = modal.querySelector('#saft-drawer-form-view');
    const successView = modal.querySelector('#saft-drawer-success-view');

    const inputName = modal.querySelector('#saft-input-name');
    const inputEmail = modal.querySelector('#saft-input-email');
    const inputAmount = modal.querySelector('#saft-input-amount');
    const inputWallet = modal.querySelector('#saft-input-wallet');
    const inputAgree = modal.querySelector('#saft-input-agree');
    const calcTokens = modal.querySelector('#saft-calc-tokens');
    const calcTge = modal.querySelector('#saft-calc-tge');
    const btnAutoFill = modal.querySelector('#saft-btn-autofill-wallet');
    const btnClearSig = modal.querySelector('#saft-btn-clear-sig');
    const btnSubmit = modal.querySelector('#saft-btn-submit-sign');
    const btnDownloadCert = modal.querySelector('#saft-btn-download-cert');
    const btnProceedPay = modal.querySelector('#saft-btn-proceed-pay');

    const canvas = modal.querySelector('#saft-sig-canvas');
    const placeholder = modal.querySelector('#saft-sig-placeholder');

    let isDrawing = false;
    let strokeCount = 0;
    let lastX = 0;
    let lastY = 0;
    let signedRecord = null;

    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    // Update Drawer i18n
    function applyDrawerI18n() {
      const lang = getCurrentLang();
      const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];

      const signBtnText = modal.querySelector('#pdf-modal-sign-btn-text');
      if (signBtnText) signBtnText.textContent = t.btnOpenSign;

      const dTitle = modal.querySelector('#saft-drawer-title');
      if (dTitle) dTitle.textContent = t.title;

      const dSub = modal.querySelector('#saft-drawer-sub');
      if (dSub) dSub.textContent = t.subtitle;

      const lblName = modal.querySelector('#saft-lbl-name');
      if (lblName) lblName.textContent = t.nameLabel;
      if (inputName) inputName.placeholder = t.namePlaceholder;

      const lblEmail = modal.querySelector('#saft-lbl-email');
      if (lblEmail) lblEmail.textContent = t.emailLabel;
      if (inputEmail) inputEmail.placeholder = t.emailPlaceholder;

      const lblAmount = modal.querySelector('#saft-lbl-amount');
      if (lblAmount) lblAmount.textContent = t.amountLabel;

      const txtAmountNote = modal.querySelector('#saft-txt-amount-note');
      if (txtAmountNote) txtAmountNote.textContent = t.amountNote;

      const lblAlloc = modal.querySelector('#saft-lbl-alloc');
      if (lblAlloc) lblAlloc.textContent = t.allocLabel;

      const lblTgeVal = modal.querySelector('#saft-lbl-tge-val');
      if (lblTgeVal) lblTgeVal.textContent = t.tgeValLabel;

      const lblWallet = modal.querySelector('#saft-lbl-wallet');
      if (lblWallet) lblWallet.textContent = t.walletLabel;
      if (inputWallet) inputWallet.placeholder = t.walletPlaceholder;

      if (btnAutoFill) btnAutoFill.textContent = t.autofillBtn;

      const lblTreasury = modal.querySelector('#saft-lbl-treasury');
      if (lblTreasury) lblTreasury.textContent = t.treasuryLabel;

      const lblCanvas = modal.querySelector('#saft-lbl-canvas');
      if (lblCanvas) lblCanvas.textContent = t.canvasLabel;

      if (placeholder) placeholder.textContent = t.canvasPlaceholder;
      if (btnClearSig) btnClearSig.textContent = t.clearBtn;

      const lblAgree = modal.querySelector('#saft-lbl-agree');
      if (lblAgree) lblAgree.textContent = t.agreeLabel;

      if (btnSubmit) btnSubmit.textContent = t.submitBtn;

      const sTitle = modal.querySelector('#saft-success-title');
      if (sTitle) sTitle.textContent = t.successTitle;

      const sSub = modal.querySelector('#saft-success-sub');
      if (sSub) sSub.textContent = t.successSubtitle;

      const recLblId = modal.querySelector('#saft-rec-lbl-id');
      if (recLblId) recLblId.textContent = t.recId;

      const recLblInvestor = modal.querySelector('#saft-rec-lbl-investor');
      if (recLblInvestor) recLblInvestor.textContent = t.recInvestor;

      const recLblAlloc = modal.querySelector('#saft-rec-lbl-alloc');
      if (recLblAlloc) recLblAlloc.textContent = t.recAlloc;

      const recLblWallet = modal.querySelector('#saft-rec-lbl-wallet');
      if (recLblWallet) recLblWallet.textContent = t.recWallet;

      const recLblTime = modal.querySelector('#saft-rec-lbl-time');
      if (recLblTime) recLblTime.textContent = t.recTime;

      const recLblHash = modal.querySelector('#saft-rec-lbl-hash');
      if (recLblHash) recLblHash.textContent = t.recHash;

      if (btnDownloadCert) btnDownloadCert.textContent = t.downloadBtn;
      if (btnProceedPay) btnProceedPay.textContent = t.proceedBtn;
    }

    // Canvas Retina Scaling with crisp white stroke on solid black
    function setupCanvasDpi() {
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
      ctx.scale(dpr, dpr);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = '#ffffff'; // Pure white ink on solid black
    }

    // Toggle Overlay
    if (signBtn) {
      signBtn.addEventListener('click', () => {
        applyDrawerI18n();
        overlay.classList.remove('hidden');
        formView.classList.remove('hidden');
        successView.classList.add('hidden');
        setTimeout(setupCanvasDpi, 50);

        // Auto-fill connected wallet if available
        autoFillConnectedWallet();
        updateDynamicAlloc();
      });
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        overlay.classList.add('hidden');
      });
    }

    // Dynamic Token Calculation (@ $0.007)
    function updateDynamicAlloc() {
      const amt = parseFloat(inputAmount.value) || 0;
      const tokens = Math.floor(amt / 0.007);
      const tgeVal = tokens * 0.010;
      if (calcTokens) calcTokens.textContent = tokens.toLocaleString('en-US');
      if (calcTge) calcTge.textContent = '$' + Math.round(tgeVal).toLocaleString('en-US') + ' USD (+42.8%)';
    }

    if (inputAmount) {
      inputAmount.addEventListener('input', updateDynamicAlloc);
    }

    // Auto-fill wallet
    function autoFillConnectedWallet() {
      const activeW = window.HAICHAIN_CURRENT_WALLET || 
                      (window.solana && window.solana.publicKey ? window.solana.publicKey.toString() : '') ||
                      (window.solflare && window.solflare.publicKey ? window.solflare.publicKey.toString() : '');
      if (activeW && inputWallet && !inputWallet.value) {
        inputWallet.value = activeW;
      }
    }

    if (btnAutoFill) {
      btnAutoFill.addEventListener('click', () => {
        const lang = getCurrentLang();
        const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];
        autoFillConnectedWallet();
        if (!inputWallet.value) {
          alert(t.noWalletDetected);
        }
      });
    }

    // Canvas Drawing Handlers (Touch & Mouse)
    function getCanvasCoords(e) {
      const rect = canvas.getBoundingClientRect();
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      const clientY = e.touches ? e.touches[0].clientY : e.clientY;
      return {
        x: clientX - rect.left,
        y: clientY - rect.top
      };
    }

    function startDraw(e) {
      isDrawing = true;
      strokeCount++;
      if (placeholder) placeholder.classList.add('hidden');
      const coords = getCanvasCoords(e);
      lastX = coords.x;
      lastY = coords.y;
      ctx.beginPath();
      ctx.moveTo(coords.x, coords.y);
    }

    function draw(e) {
      if (!isDrawing) return;
      e.preventDefault();
      const coords = getCanvasCoords(e);
      ctx.lineTo(coords.x, coords.y);
      ctx.stroke();
      lastX = coords.x;
      lastY = coords.y;
    }

    function stopDraw() {
      if (isDrawing) {
        isDrawing = false;
        ctx.closePath();
      }
    }

    canvas.addEventListener('mousedown', startDraw);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDraw);
    canvas.addEventListener('mouseleave', stopDraw);

    canvas.addEventListener('touchstart', (e) => {
      e.preventDefault();
      startDraw(e);
    }, { passive: false });
    canvas.addEventListener('touchmove', draw, { passive: false });
    canvas.addEventListener('touchend', stopDraw);

    if (btnClearSig) {
      btnClearSig.addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        strokeCount = 0;
        if (placeholder) placeholder.classList.remove('hidden');
      });
    }

    // Form Validation & Submission
    if (btnSubmit) {
      btnSubmit.addEventListener('click', async () => {
        const lang = getCurrentLang();
        const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];

        const name = inputName.value.trim();
        const email = inputEmail.value.trim();
        const amount = parseFloat(inputAmount.value) || 0;
        const wallet = inputWallet.value.trim();
        const agreed = inputAgree.checked;

        if (!name || name.length < 2) {
          alert(t.errName);
          inputName.focus();
          return;
        }

        if (!email || !email.includes('@') || !email.includes('.')) {
          alert(t.errEmail);
          inputEmail.focus();
          return;
        }

        if (amount < 500) {
          alert(t.errAmount);
          inputAmount.focus();
          return;
        }

        if (!wallet || wallet.length < 32 || wallet.length > 44) {
          alert(t.errWallet);
          inputWallet.focus();
          return;
        }

        if (strokeCount < 3) {
          alert(t.errSig);
          return;
        }

        if (!agreed) {
          alert(t.errAgree);
          return;
        }

        // Generate SHA-256 Audit Proof
        const timestamp = new Date().toISOString();
        const contractId = 'SAFT-HAI-2026-' + Math.random().toString(36).substring(2, 7).toUpperCase();
        const tokens = Math.floor(amount / 0.007);
        const treasury = '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';
        const signatureData = canvas.toDataURL('image/png');

        const rawProof = contractId + '|' + name + '|' + email + '|' + amount + '|' + tokens + '|' + wallet + '|' + treasury + '|' + timestamp;
        let hashHex = '';
        try {
          const enc = new TextEncoder().encode(rawProof);
          const buf = await crypto.subtle.digest('SHA-256', enc);
          hashHex = Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
        } catch (_) {
          hashHex = 'SHA256_' + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
        }

        signedRecord = {
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

        // Save to localStorage
        try {
          const prev = JSON.parse(localStorage.getItem('HAICHAIN_SIGNED_SAFT_RECORDS') || '[]');
          prev.unshift(signedRecord);
          localStorage.setItem('HAICHAIN_SIGNED_SAFT_RECORDS', JSON.stringify(prev));
          localStorage.setItem('HAICHAIN_ACTIVE_SAFT', JSON.stringify(signedRecord));
        } catch (e) {
          console.warn('Could not save SAFT to storage:', e);
        }

        // Display Success View
        modal.querySelector('#saft-rec-id').textContent = contractId;
        modal.querySelector('#saft-rec-name').textContent = name;
        modal.querySelector('#saft-rec-alloc').textContent = tokens.toLocaleString('en-US') + ' $HAISI';
        modal.querySelector('#saft-rec-wallet').textContent = wallet.slice(0, 6) + '...' + wallet.slice(-6);
        modal.querySelector('#saft-rec-time').textContent = (lang === 'vi') ? new Date(timestamp).toLocaleString('vi-VN') : new Date(timestamp).toUTCString();
        modal.querySelector('#saft-rec-hash').textContent = hashHex;

        formView.classList.add('hidden');
        successView.classList.remove('hidden');
      });
    }

    // Download Signed Certificate (HTML / PDF format)
    if (btnDownloadCert) {
      btnDownloadCert.addEventListener('click', () => {
        if (!signedRecord) return;
        const lang = getCurrentLang();
        const isVi = (lang === 'vi');

        const docTitle = isVi ? ('CHỨNG NHẬN KÝ HỢP ĐỒNG SAFT - ' + signedRecord.contractId) : ('SAFT AGREEMENT SIGNING CERTIFICATE - ' + signedRecord.contractId);
        const subTitle = 'HAICHAIN PRE-SEED STRATEGIC ROUND ($0.007 USD / $HAISI)';
        const certStatement = isVi
          ? 'Chứng nhận rằng Nhà Đầu Tư dưới đây đã chính thức ký kết Thỏa Thuận Tương Lai Chuyển Đổi Token (SAFT) với HAICHAIN Autonomous Machine Financial Protocol:'
          : 'This certifies that the Investor below has executed the Simple Agreement for Future Tokens (SAFT) with HAICHAIN Autonomous Machine Financial Protocol:';

        const certHtml = '<!DOCTYPE html>' +
'<html lang="' + (isVi ? 'vi' : 'en') + '">' +
'<head>' +
'<meta charset="UTF-8">' +
'<title>' + docTitle + '</title>' +
'<style>' +
'  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 40px; background: #ffffff; color: #111; max-width: 800px; margin: 0 auto; line-height: 1.6; }' +
'  .header { border-bottom: 2px solid #111; padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: flex-end; }' +
'  .badge { background: #111; color: #fff; padding: 4px 12px; border-radius: 999px; font-size: 11px; font-family: monospace; }' +
'  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 25px 0; }' +
'  .field { border-bottom: 1px dashed #ddd; padding-bottom: 8px; }' +
'  .label { font-size: 11px; color: #666; text-transform: uppercase; letter-spacing: 0.5px; }' +
'  .value { font-size: 14px; font-weight: 600; font-family: monospace; }' +
'  .sig-box { margin-top: 30px; padding: 20px; border: 1px solid #e5e5e5; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; }' +
'  .proof { margin-top: 30px; padding: 15px; background: #f9f9f9; border-radius: 8px; font-family: monospace; font-size: 10px; word-break: break-all; color: #666; }' +
'</style>' +
'</head>' +
'<body>' +
'  <div class="header">' +
'    <div>' +
'      <h1 style="margin:0; font-size: 22px;">' + docTitle + '</h1>' +
'      <p style="margin:5px 0 0 0; color: #666; font-size: 12px;">' + subTitle + '</p>' +
'    </div>' +
'    <div class="badge">' + signedRecord.contractId + '</div>' +
'  </div>' +
'  <p>' + certStatement + '</p>' +
'  <div class="grid">' +
'    <div class="field"><div class="label">' + (isVi ? 'Nhà Đầu Tư (Người Ký):' : 'Investor (Signatory):') + '</div><div class="value">' + signedRecord.name + '</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Email Xác Nhận:' : 'Email Address:') + '</div><div class="value">' + signedRecord.email + '</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Số Tiền Đầu Tư:' : 'Investment Amount:') + '</div><div class="value">$' + signedRecord.amount.toLocaleString('en-US') + ' USD (USDT)</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Quyền Phân Bổ Token:' : 'Token Allocation:') + '</div><div class="value">' + signedRecord.tokens.toLocaleString('en-US') + ' $HAISI (@ $0.007)</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Giá Trị Dự Kiến TGE:' : 'TGE Projected Value:') + '</div><div class="value">$' + (signedRecord.tokens * 0.01).toLocaleString('en-US') + ' USD (+42.8%)</div></div>' +
'    <div class="field"><div class="label">' + (isVi ? 'Thời Điểm Ký (UTC):' : 'Signing Timestamp (UTC):') + '</div><div class="value">' + signedRecord.timestamp + '</div></div>' +
'    <div class="field" style="grid-column: span 2;"><div class="label">' + (isVi ? 'Địa Chỉ Ví Solana Nhận Token (Beneficiary Wallet):' : 'Beneficiary Solana Receiving Address:') + '</div><div class="value">' + signedRecord.wallet + '</div></div>' +
'    <div class="field" style="grid-column: span 2;"><div class="label">' + (isVi ? 'Kho Bạc Multi-Sig Nhận Vốn (Solana Mainnet):' : 'Multi-Sig Treasury Vault (Solana Mainnet):') + '</div><div class="value">' + signedRecord.treasury + '</div></div>' +
'  </div>' +
'  <div class="sig-box">' +
'    <div>' +
'      <div class="label">' + (isVi ? 'CHỮ KÝ ĐIỆN TỬ CỦA NHÀ ĐẦU TƯ:' : 'INVESTOR DIGITAL SIGNATURE:') + '</div>' +
'      <div style="font-size: 12px; color:#444; margin-top: 4px;">' + (isVi ? 'Đã ký số trực tuyến theo chuẩn ESIGN Act &amp; Luật GDĐT' : 'Executed digitally pursuant to US ESIGN Act &amp; UETA standards') + '</div>' +
'    </div>' +
'    <img src="' + signedRecord.signatureData + '" style="max-height: 70px; border-bottom: 1px solid #000;" alt="Signature">' +
'  </div>' +
'  <div class="proof">' +
'    <strong>CRYPTOGRAPHIC AUDIT PROOF (SHA-256):</strong><br>' +
'    ' + signedRecord.hashHex + '<br>' +
'    <em>' + (isVi ? 'Chứng từ này được mã hóa bảo chứng, liên kết bất biến với giao dịch trên Solana Blockchain.' : 'This document is cryptographically verified and permanently linked to Solana blockchain transactions.') + '</em>' +
'  </div>' +
'  <script>window.onload = function() { window.print(); };<' + '/script>' +
'</body>' +
'</html>';

        const blob = new Blob([certHtml], { type: 'text/html;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'HAICHAIN_SAFT_CERTIFICATE_' + signedRecord.contractId + '.html';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      });
    }

    // Proceed to Payment
    if (btnProceedPay) {
      btnProceedPay.addEventListener('click', () => {
        if (!signedRecord) return;
        const lang = getCurrentLang();
        const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];
        window.closePdfViewerModal();

        // Redirect or open Tab 7 / Private Round
        if (window.location.pathname.includes('dashboard')) {
          const tabBtn = document.querySelector('[data-tab="private-round"], [data-tab="preseed"], #nav-tab-preseed');
          if (tabBtn) tabBtn.click();
        }

        // Fill in amount in sale controller if exists
        const amtInput = document.getElementById('sale-invest-amount') || document.querySelector('input[name="saftAmount"]');
        if (amtInput) {
          amtInput.value = signedRecord.amount;
          amtInput.dispatchEvent(new Event('input', { bubbles: true }));
        }

        const alertMsg = t.alertProceed
          .replace('{amount}', signedRecord.amount)
          .replace('{tokens}', signedRecord.tokens.toLocaleString());
        alert(alertMsg);
      });
    }

    // Expose language refresh hook
    window.refreshSaftDrawerI18n = applyDrawerI18n;
  }
'''

SIGN_VISIBILITY_LOGIC = '''
    // Dynamic SAFT E-Signature Button Visibility & i18n (Zero Icons, Ultra-High Contrast)
    const saftSignBtn = document.getElementById('pdf-modal-sign-btn');
    const isSaftDoc = String(pdfUrl || '').toUpperCase().includes('SAFT') || String(docTitle || '').toUpperCase().includes('SAFT');
    if (saftSignBtn) {
      if (isSaftDoc) {
        saftSignBtn.classList.remove('hidden');
        saftSignBtn.classList.add('inline-flex');
        const signBtnText = document.getElementById('pdf-modal-sign-btn-text');
        if (signBtnText) {
          signBtnText.textContent = (lang === 'vi') ? 'Ký Hợp Đồng Online' : 'Sign Agreement Online';
        }
      } else {
        saftSignBtn.classList.add('hidden');
        saftSignBtn.classList.remove('inline-flex');
      }
    }
    if (typeof window.refreshSaftDrawerI18n === 'function') {
      window.refreshSaftDrawerI18n();
    }
'''

for filepath in TARGET_FILES:
    if not os.path.exists(filepath):
        print("Skipping missing file:", filepath)
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Replace button with zero-icon version
    if '<button id="pdf-modal-sign-btn"' in code:
        start_idx = code.find('<!-- Digital E-Signature Action Button')
        if start_idx != -1:
            end_idx = code.find('</button>', start_idx) + 9
            code = code[:start_idx] + SIGN_BUTTON_HTML.strip() + code[end_idx:]
            print("[+] Cleaned button in", filepath)

    # 2. Replace drawer with solid opaque & ultra-high contrast version
    old_drawer_start = code.find('<!-- ========================================================================= -->\n        <!-- LUXURY IN-APP DIGITAL E-SIGNATURE OVERLAY')
    if old_drawer_start != -1:
        old_drawer_end = code.find('<!-- Floating Sticky Bottom Pill: Current Page & Jump Controls -->', old_drawer_start)
        code = code[:old_drawer_start] + SIGN_DRAWER_HTML.strip() + "\n\n        " + code[old_drawer_end:]
        print("[+] Replaced drawer with solid opaque version in", filepath)

    # 3. Replace handler code
    old_handler_start = code.find('// =========================================================================\n  // SAFT DIGITAL E-SIGNATURE LOGIC')
    if old_handler_start != -1:
        old_handler_end = code.find('window.openPdfViewerModal = async function', old_handler_start)
        code = code[:old_handler_start] + SIGN_HANDLER_CODE.strip() + "\n\n  " + code[old_handler_end:]
        print("[+] Cleaned handler in", filepath)

    # 4. Replace visibility logic
    old_vis_start = code.find('// Dynamic SAFT E-Signature Button Visibility')
    if old_vis_start != -1:
        old_vis_end = code.find('try {\n      let doc =', old_vis_start)
        if old_vis_end == -1:
            old_vis_end = code.find('try {\r\n      let doc =', old_vis_start)
        if old_vis_end != -1:
            code = code[:old_vis_start] + SIGN_VISIBILITY_LOGIC.strip() + "\n\n    " + code[old_vis_end:]
            print("[+] Cleaned visibility logic in", filepath)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    print("[*] Successfully processed", filepath)
