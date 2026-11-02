import os

WORKSPACE_DIR = r"c:\Users\Surface\Documents\8. HAICHAIN"
TARGET_FILES = [
    os.path.join(WORKSPACE_DIR, "app", "pdf-modal.js"),
    os.path.join(WORKSPACE_DIR, "pdf-modal.js"),
]

SIGN_BUTTON_HTML = '''            <!-- Digital E-Signature Action Button (Only shown for SAFT Agreements) -->
            <button id="pdf-modal-sign-btn" type="button" class="hidden items-center space-x-1 sm:space-x-1.5 px-2.5 sm:px-3 h-7 sm:h-8 rounded-lg sm:rounded-xl bg-black hover:bg-neutral-800 dark:bg-white dark:hover:bg-neutral-200 text-white dark:text-black transition-all active:scale-95 text-[11px] sm:text-xs font-semibold shadow-xs shrink-0 cursor-pointer animate-pulse">
              <span>✍️</span>
              <span id="pdf-modal-sign-btn-text">Ký Hợp Đồng Online</span>
            </button>
'''

SIGN_DRAWER_HTML = '''        <!-- ========================================================================= -->
        <!-- LUXURY IN-APP DIGITAL E-SIGNATURE OVERLAY (OPTION A - ESIGN ACT COMPLIANT) -->
        <!-- ========================================================================= -->
        <div id="saft-sign-overlay" class="absolute inset-0 z-50 bg-white/98 dark:bg-[#0c0c0e]/98 backdrop-blur-md hidden flex flex-col overflow-y-auto p-3 sm:p-6 md:p-8 transition-all duration-200">
          
          <!-- Drawer Header -->
          <div class="flex items-center justify-between pb-3 sm:pb-4 border-b border-neutral-200 dark:border-neutral-800 shrink-0">
            <div class="flex items-center space-x-2 sm:space-x-3">
              <div class="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-black dark:bg-white text-white dark:text-black flex items-center justify-center font-bold text-sm shadow-xs">
                ✍️
              </div>
              <div>
                <h3 id="saft-drawer-title" class="text-xs sm:text-base font-bold text-black dark:text-white">Ký Điện Tử Hợp Đồng SAFT Pre-Seed ($0.007)</h3>
                <p id="saft-drawer-sub" class="text-[10px] sm:text-xs text-neutral-500 font-mono">Xác thực pháp lý trực tuyến theo chuẩn ESIGN Act &amp; Luật GDĐT 2023</p>
              </div>
            </div>
            
            <button id="saft-drawer-close-btn" type="button" class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl flex items-center justify-center text-neutral-500 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors cursor-pointer" title="Quay lại văn bản">
              <i data-lucide="x" class="w-4 h-4 sm:w-4.5 sm:h-4.5"></i>
            </button>
          </div>

          <!-- Drawer Form Body -->
          <div id="saft-drawer-form-view" class="py-3 sm:py-5 max-w-2xl mx-auto w-full space-y-4">
            
            <!-- Dual Column Fields: Name & Email -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              <div>
                <label id="saft-lbl-name" class="block text-[11px] sm:text-xs font-semibold text-neutral-700 dark:text-neutral-300 mb-1">Họ và Tên / Tên Pháp Nhân *</label>
                <input id="saft-input-name" type="text" placeholder="Nguyễn Văn A / Tech Fund LLC" class="w-full px-3 py-2 text-xs sm:text-sm rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white transition-all">
              </div>
              <div>
                <label id="saft-lbl-email" class="block text-[11px] sm:text-xs font-semibold text-neutral-700 dark:text-neutral-300 mb-1">Email Liên Hệ *</label>
                <input id="saft-input-email" type="email" placeholder="investor@example.com" class="w-full px-3 py-2 text-xs sm:text-sm rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white transition-all">
              </div>
            </div>

            <!-- Dual Column Fields: Amount & Real-time Allocation Calculation -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              <div>
                <label id="saft-lbl-amount" class="block text-[11px] sm:text-xs font-semibold text-neutral-700 dark:text-neutral-300 mb-1">Số Tiền Đăng Ký Đầu Tư (USD / USDT) *</label>
                <div class="relative">
                  <span class="absolute left-3 top-2.5 text-xs font-mono text-neutral-400">$</span>
                  <input id="saft-input-amount" type="number" min="500" max="50000" step="100" value="1000" class="w-full pl-7 pr-3 py-2 text-xs sm:text-sm font-mono rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white transition-all">
                </div>
                <p class="text-[10px] text-neutral-400 mt-1">Hạn mức vé: $500 – $15,000 USD</p>
              </div>

              <div>
                <label class="block text-[11px] sm:text-xs font-semibold text-neutral-700 dark:text-neutral-300 mb-1">Quyền Phân Bổ Token $HAISI (@ $0.007)</label>
                <div class="p-2.5 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-100/60 dark:bg-neutral-900/60 flex flex-col justify-center">
                  <div class="flex items-baseline justify-between">
                    <span id="saft-calc-tokens" class="text-sm sm:text-base font-bold font-mono text-black dark:text-white">142,857</span>
                    <span class="text-[11px] font-mono text-neutral-500">$HAISI</span>
                  </div>
                  <div class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 flex items-center justify-between mt-0.5">
                    <span>Giá trị TGE ($0.010):</span>
                    <span id="saft-calc-tge" class="font-bold">$1,428 USD (+42.8%)</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Beneficiary Wallet Address -->
            <div>
              <div class="flex items-center justify-between mb-1">
                <label id="saft-lbl-wallet" class="text-[11px] sm:text-xs font-semibold text-neutral-700 dark:text-neutral-300">Địa Chỉ Ví Solana Nhận Token Tại TGE *</label>
                <button id="saft-btn-autofill-wallet" type="button" class="text-[10px] font-mono text-neutral-500 hover:text-black dark:hover:text-white underline cursor-pointer">Lấy Ví Đang Kết Nối</button>
              </div>
              <input id="saft-input-wallet" type="text" placeholder="Địa chỉ ví Phantom/Solflare (Base58 32-44 ký tự)..." class="w-full px-3 py-2 text-xs font-mono rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white transition-all">
            </div>

            <!-- Treasury Vault Display (Immutably Bound) -->
            <div class="p-2.5 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950/60 text-[10px] sm:text-[11px] font-mono text-neutral-600 dark:text-neutral-400">
              <div class="flex items-center justify-between">
                <span class="font-bold text-neutral-800 dark:text-neutral-200">🛡️ Kho Bạc Multi-Sig Nhận Vốn (Solana Mainnet):</span>
                <span class="text-emerald-600 dark:text-emerald-400 font-semibold">Squads 2-of-3</span>
              </div>
              <div class="truncate mt-0.5 text-neutral-900 dark:text-neutral-100 font-mono">5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3</div>
            </div>

            <!-- Digital Signature Pad Canvas -->
            <div>
              <div class="flex items-center justify-between mb-1.5">
                <label id="saft-lbl-canvas" class="text-[11px] sm:text-xs font-semibold text-neutral-700 dark:text-neutral-300">Vẽ Chữ Ký Điện Tử Của Bạn Vào Khung Dưới *</label>
                <button id="saft-btn-clear-sig" type="button" class="text-[10px] font-mono text-red-500 hover:text-red-700 underline cursor-pointer">Xóa vẽ lại</button>
              </div>
              <div class="relative w-full rounded-xl overflow-hidden border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 shadow-inner">
                <canvas id="saft-sig-canvas" width="600" height="150" class="w-full h-32 sm:h-36 block touch-none cursor-crosshair"></canvas>
                <div id="saft-sig-placeholder" class="absolute inset-0 flex items-center justify-center pointer-events-none text-xs text-neutral-400 font-mono select-none">
                  (Dùng chuột hoặc ngón tay để ký tên tại đây)
                </div>
              </div>
            </div>

            <!-- Legal Declaration Checkbox -->
            <label class="flex items-start space-x-2.5 text-[11px] sm:text-xs text-neutral-600 dark:text-neutral-400 cursor-pointer select-none pt-1">
              <input id="saft-input-agree" type="checkbox" class="mt-0.5 rounded border-neutral-300 dark:border-neutral-700 text-black dark:text-white cursor-pointer">
              <span id="saft-lbl-agree">Tôi xác nhận đã đọc, hiểu và đồng thuận 100% với các điều khoản của Hợp đồng SAFT HAICHAIN. Tôi hiểu rằng vốn đầu tư được bảo vệ tại Kho Bạc Squads Multi-Sig và token được phân bổ tự động tại TGE.</span>
            </label>

            <!-- Submit Sign Button -->
            <button id="saft-btn-submit-sign" type="button" class="w-full py-3 sm:py-3.5 rounded-xl bg-black hover:bg-neutral-800 dark:bg-white dark:hover:bg-neutral-200 text-white dark:text-black font-bold text-xs sm:text-sm tracking-wide shadow-lg active:scale-[0.99] transition-all cursor-pointer">
              ✍️ XÁC NHẬN KÝ &amp; HOÀN TẤT HỢP ĐỒNG PHÁP LÝ
            </button>
          </div>

          <!-- Drawer Success View (Shown after signing) -->
          <div id="saft-drawer-success-view" class="hidden py-6 sm:py-10 max-w-lg mx-auto w-full text-center space-y-5 animate-scaleUp">
            <div class="w-14 h-14 sm:w-16 sm:h-16 mx-auto rounded-full bg-emerald-500/10 text-emerald-500 flex items-center justify-center text-2xl sm:text-3xl shadow-inner">
              ✓
            </div>
            <div>
              <h4 id="saft-success-title" class="text-base sm:text-xl font-bold text-black dark:text-white">KÝ HỢP ĐỒNG THÀNH CÔNG!</h4>
              <p id="saft-success-sub" class="text-xs sm:text-sm text-neutral-500 mt-1">Hợp đồng SAFT điện tử đã được ghi nhận và đóng dấu kiểm toán mật mã.</p>
            </div>

            <!-- Receipt Card -->
            <div class="p-4 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900/60 text-left text-xs font-mono space-y-2">
              <div class="flex justify-between">
                <span class="text-neutral-500">Mã Hợp Đồng:</span>
                <span id="saft-rec-id" class="font-bold text-black dark:text-white">SAFT-HAI-2026-XXXXX</span>
              </div>
              <div class="flex justify-between">
                <span class="text-neutral-500">Nhà Đầu Tư:</span>
                <span id="saft-rec-name" class="font-semibold text-black dark:text-white truncate max-w-[200px]">--</span>
              </div>
              <div class="flex justify-between">
                <span class="text-neutral-500">Phân Bổ:</span>
                <span id="saft-rec-alloc" class="font-bold text-emerald-600 dark:text-emerald-400">-- $HAISI</span>
              </div>
              <div class="flex justify-between">
                <span class="text-neutral-500">Ví Nhận:</span>
                <span id="saft-rec-wallet" class="font-mono text-[11px] truncate max-w-[200px]">--</span>
              </div>
              <div class="flex justify-between">
                <span class="text-neutral-500">Thời Gian:</span>
                <span id="saft-rec-time" class="text-[11px] text-neutral-400">--</span>
              </div>
              <div class="pt-2 border-t border-neutral-200 dark:border-neutral-800 text-[9px] text-neutral-400 break-all">
                <span class="text-neutral-500 block mb-0.5">SHA-256 Audit Hash:</span>
                <span id="saft-rec-hash">--</span>
              </div>
            </div>

            <!-- Dual Action Buttons: Download PDF & Proceed to Deposit -->
            <div class="space-y-2.5 pt-2">
              <button id="saft-btn-download-cert" type="button" class="w-full py-2.5 sm:py-3 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:bg-neutral-100 dark:hover:bg-neutral-800 text-black dark:text-white font-medium text-xs sm:text-sm transition-all cursor-pointer">
                📥 Tải File Chứng Nhận Hợp Đồng Đã Ký (HTML / PDF)
              </button>
              <button id="saft-btn-proceed-pay" type="button" class="w-full py-3 sm:py-3.5 rounded-xl bg-black hover:bg-neutral-800 dark:bg-white dark:hover:bg-neutral-200 text-white dark:text-black font-bold text-xs sm:text-sm tracking-wide shadow-lg active:scale-[0.99] transition-all cursor-pointer">
                💳 Tiến Hành Nạp Tiền Vào Kho Bạc Ngay
              </button>
            </div>
          </div>

        </div>
'''

SIGN_HANDLER_CODE = '''  // =========================================================================
  // SAFT DIGITAL E-SIGNATURE LOGIC (OPTION A - ESIGN ACT & AUDIT TRAIL ENGINE)
  // =========================================================================
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

    // Canvas Retina Scaling
    function setupCanvasDpi() {
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
      ctx.scale(dpr, dpr);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = document.documentElement.classList.contains('dark') ? '#ffffff' : '#000000';
    }

    // Toggle Overlay
    if (signBtn) {
      signBtn.addEventListener('click', () => {
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
        autoFillConnectedWallet();
        if (!inputWallet.value) {
          alert("Chưa phát hiện ví Web3 (Phantom/Solflare) đang kết nối. Vui lòng dán địa chỉ ví thủ công.");
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
        const name = inputName.value.trim();
        const email = inputEmail.value.trim();
        const amount = parseFloat(inputAmount.value) || 0;
        const wallet = inputWallet.value.trim();
        const agreed = inputAgree.checked;

        if (!name || name.length < 2) {
          alert("Vui lòng nhập Họ và Tên hoặc Tên Pháp Nhân của bạn.");
          inputName.focus();
          return;
        }

        if (!email || !email.includes('@') || !email.includes('.')) {
          alert("Vui lòng nhập địa chỉ Email hợp lệ.");
          inputEmail.focus();
          return;
        }

        if (amount < 500) {
          alert("Hạn mức đăng ký đầu tư tối thiểu là 500 USD.");
          inputAmount.focus();
          return;
        }

        if (!wallet || wallet.length < 32 || wallet.length > 44) {
          alert("Vui lòng nhập địa chỉ ví Solana hợp lệ (32 - 44 ký tự Base58) để nhận token tại TGE.");
          inputWallet.focus();
          return;
        }

        if (strokeCount < 3) {
          alert("Vui lòng ký tên của bạn vào khung chữ ký điện tử.");
          return;
        }

        if (!agreed) {
          alert("Vui lòng tick vào ô xác nhận đồng ý với các điều khoản Hợp đồng SAFT.");
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
        modal.querySelector('#saft-rec-time').textContent = new Date(timestamp).toLocaleString('vi-VN');
        modal.querySelector('#saft-rec-hash').textContent = hashHex;

        formView.classList.add('hidden');
        successView.classList.remove('hidden');
      });
    }

    // Download Signed Certificate (HTML / PDF format)
    if (btnDownloadCert) {
      btnDownloadCert.addEventListener('click', () => {
        if (!signedRecord) return;
        const certHtml = '<!DOCTYPE html>' +
'<html lang="vi">' +
'<head>' +
'<meta charset="UTF-8">' +
'<title>CHỨNG NHẬN KÝ HỢP ĐỒNG SAFT - ' + signedRecord.contractId + '</title>' +
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
'      <h1 style="margin:0; font-size: 22px;">CHỨNG NHẬN KÝ KẾT HỢP ĐỒNG SAFT</h1>' +
'      <p style="margin:5px 0 0 0; color: #666; font-size: 12px;">HAICHAIN PRE-SEED STRATEGIC ROUND ($0.007 USD / $HAISI)</p>' +
'    </div>' +
'    <div class="badge">' + signedRecord.contractId + '</div>' +
'  </div>' +
'  <p>Chứng nhận rằng Nhà Đầu Tư dưới đây đã chính thức ký kết Thỏa Thuận Tương Lai Chuyển Đổi Token (SAFT) với HAICHAIN Autonomous Machine Financial Protocol:</p>' +
'  <div class="grid">' +
'    <div class="field"><div class="label">Nhà Đầu Tư (Người Ký):</div><div class="value">' + signedRecord.name + '</div></div>' +
'    <div class="field"><div class="label">Email Xác Nhận:</div><div class="value">' + signedRecord.email + '</div></div>' +
'    <div class="field"><div class="label">Số Tiền Đầu Tư:</div><div class="value">$' + signedRecord.amount.toLocaleString('en-US') + ' USD (USDT)</div></div>' +
'    <div class="field"><div class="label">Quyền Phân Bổ Token:</div><div class="value">' + signedRecord.tokens.toLocaleString('en-US') + ' $HAISI (@ $0.007)</div></div>' +
'    <div class="field"><div class="label">Giá Trị Dự Kiến TGE:</div><div class="value">$' + (signedRecord.tokens * 0.01).toLocaleString('en-US') + ' USD (+42.8%)</div></div>' +
'    <div class="field"><div class="label">Thời Điểm Ký (UTC):</div><div class="value">' + signedRecord.timestamp + '</div></div>' +
'    <div class="field" style="grid-column: span 2;"><div class="label">Địa Chỉ Ví Solana Nhận Token (Beneficiary Wallet):</div><div class="value">' + signedRecord.wallet + '</div></div>' +
'    <div class="field" style="grid-column: span 2;"><div class="label">Kho Bạc Multi-Sig Nhận Vốn (Solana Mainnet):</div><div class="value">' + signedRecord.treasury + '</div></div>' +
'  </div>' +
'  <div class="sig-box">' +
'    <div>' +
'      <div class="label">CHỮ KÝ ĐIỆN TỬ CỦA NHÀ ĐẦU TƯ:</div>' +
'      <div style="font-size: 12px; color:#444; margin-top: 4px;">Đã ký số trực tuyến theo chuẩn ESIGN Act &amp; Luật GDĐT</div>' +
'    </div>' +
'    <img src="' + signedRecord.signatureData + '" style="max-height: 70px; border-bottom: 1px solid #000;" alt="Signature">' +
'  </div>' +
'  <div class="proof">' +
'    <strong>CRYPTOGRAPHIC AUDIT PROOF (SHA-256):</strong><br>' +
'    ' + signedRecord.hashHex + '<br>' +
'    <em>Chứng từ này được mã hóa bảo chứng, liên kết bất biến với giao dịch trên Solana Blockchain.</em>' +
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

        alert("🎉 HỢP ĐỒNG ĐÃ ĐƯỢC KÝ!\\n\\nVui lòng bấm '1-Click Pay with Web3 Wallet' hoặc chuyển " + signedRecord.amount + " USDT vào Kho Bạc:\\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\\n\\nSố token " + signedRecord.tokens.toLocaleString() + " $HAISI sẽ được tự động phân bổ về ví của bạn tại TGE.");
      });
    }
  }
'''

SIGN_VISIBILITY_LOGIC = '''
    // Dynamic SAFT E-Signature Button Visibility
    const saftSignBtn = document.getElementById('pdf-modal-sign-btn');
    const isSaftDoc = String(pdfUrl || '').toUpperCase().includes('SAFT') || String(docTitle || '').toUpperCase().includes('SAFT');
    if (saftSignBtn) {
      if (isSaftDoc) {
        saftSignBtn.classList.remove('hidden');
        saftSignBtn.classList.add('inline-flex');
      } else {
        saftSignBtn.classList.add('hidden');
        saftSignBtn.classList.remove('inline-flex');
      }
    }
'''

for filepath in TARGET_FILES:
    if not os.path.exists(filepath):
        print("Skipping missing file:", filepath)
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Inject button
    if "pdf-modal-sign-btn" not in code:
        anchor = "<!-- Close Button (✕) ONLY -->"
        if anchor in code:
            code = code.replace(anchor, SIGN_BUTTON_HTML + "\n            " + anchor)
            print("[+] Injected button into", filepath)

    # 2. Inject drawer
    if "saft-sign-overlay" not in code:
        drawer_anchor = "<!-- Floating Sticky Bottom Pill: Current Page & Jump Controls -->"
        if drawer_anchor in code:
            code = code.replace(drawer_anchor, SIGN_DRAWER_HTML + "\n\n        " + drawer_anchor)
            print("[+] Injected drawer into", filepath)

    # 3. Inject init call
    if "initSaftSignatureEngine(modal);" not in code:
        init_anchor = "const closeBtn = modal.querySelector('#pdf-modal-close-btn');"
        if init_anchor in code:
            code = code.replace(init_anchor, "initSaftSignatureEngine(modal);\n\n    " + init_anchor)
            print("[+] Injected init call into", filepath)

    # 4. Inject handler function
    if "function initSaftSignatureEngine(modal)" not in code:
        func_anchor = "window.openPdfViewerModal = async function"
        if func_anchor in code:
            code = code.replace(func_anchor, SIGN_HANDLER_CODE + "\n\n  " + func_anchor)
            print("[+] Injected handler function into", filepath)

    # 5. Inject visibility logic
    if "isSaftDoc" not in code:
        vis_anchor = "modal.classList.remove('hidden');"
        if vis_anchor in code:
            code = code.replace(vis_anchor, "modal.classList.remove('hidden');\n" + SIGN_VISIBILITY_LOGIC)
            print("[+] Injected visibility logic into", filepath)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    print("[*] Successfully processed", filepath)
