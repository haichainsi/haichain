import os

def main():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert Faucet Success Modal HTML right after insufficient-vault-modal
    faucet_modal_html = """  <!-- ======================== FAUCET CLAIMED SUCCESS POPUP MODAL ======================== -->
  <div id="faucet-success-modal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-md hidden flex items-end sm:items-center justify-center p-0 sm:p-4 transition-all duration-300" role="dialog" aria-modal="true" aria-labelledby="faucet-success-modal-title">
    <div class="w-full sm:max-w-md rounded-t-[32px] sm:rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#0c0c0c] p-5 sm:p-6 shadow-2xl relative max-h-[92vh] overflow-y-auto transform transition-transform duration-300 animate-fadeIn">
      
      <!-- Mobile Drag Handle Bar -->
      <div class="sm:hidden w-12 h-1.5 bg-neutral-300 dark:bg-neutral-700 rounded-full mx-auto mb-3.5"></div>

      <!-- Modal Header -->
      <div class="flex justify-between items-center pb-3.5 border-b border-neutral-100 dark:border-neutral-900">
        <div class="flex items-center space-x-3 min-w-0">
          <div class="w-10 h-10 rounded-2xl bg-emerald-500/10 dark:bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 flex items-center justify-center shrink-0 shadow-sm">
            <i data-lucide="check-circle-2" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <div class="flex items-center space-x-2">
              <h3 id="faucet-success-modal-title" class="font-bold text-sm sm:text-base text-black dark:text-white truncate">
                Testnet Faucet Claimed
              </h3>
              <span class="text-[9px] font-mono uppercase px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 font-bold border border-emerald-500/20 shrink-0">Confirmed</span>
            </div>
            <p id="faucet-success-modal-subtitle" class="text-[11px] text-neutral-500 font-mono truncate">
              Solana Devnet Instant Airdrop
            </p>
          </div>
        </div>
        <button id="close-faucet-success-modal-btn" class="p-2 rounded-full bg-neutral-100 hover:bg-neutral-200 dark:bg-neutral-800 dark:hover:bg-neutral-700 text-neutral-500 hover:text-black dark:hover:text-white transition-colors shrink-0 ml-2 cursor-pointer" aria-label="Close">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <!-- Modal Body -->
      <div class="my-4 space-y-3 font-mono text-xs">
        <!-- Hero Claim Amount Card -->
        <div class="p-4 rounded-2xl bg-emerald-500/5 dark:bg-emerald-500/10 border border-emerald-500/20 text-center space-y-1 relative overflow-hidden">
          <div class="text-[11px] text-emerald-700 dark:text-emerald-300 font-sans font-medium" id="faucet-success-modal-hero-label">
            Funds Dispatched to Master Vault
          </div>
          <div id="faucet-success-modal-amount" class="text-2xl sm:text-3xl font-extrabold text-black dark:text-white tracking-tight font-mono">
            +25.00 USDT
          </div>
          <div class="inline-flex items-center space-x-1.5 text-[11px] text-neutral-500 font-mono pt-0.5">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>Solana Devnet Program</span>
            <span>•</span>
            <span class="text-emerald-600 dark:text-emerald-400 font-semibold">0% Gas Fee</span>
          </div>
        </div>

        <!-- Details Grid -->
        <div class="p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2.5 font-mono text-[11px]">
          <div class="flex items-center justify-between">
            <span class="text-neutral-400" id="faucet-success-modal-lbl-vault">Master Vault Balance:</span>
            <span id="faucet-success-modal-vault-bal" class="font-bold text-black dark:text-white">$25.0000 USDT</span>
          </div>
          <div class="flex items-center justify-between pt-2 border-t border-neutral-200/60 dark:border-neutral-800/80">
            <span class="text-neutral-400" id="faucet-success-modal-lbl-status">Status:</span>
            <span class="text-emerald-600 dark:text-emerald-400 font-semibold flex items-center space-x-1">
              <i data-lucide="check" class="w-3.5 h-3.5"></i>
              <span>Settled On-Chain</span>
            </span>
          </div>
          <div id="faucet-success-modal-tx-row" class="flex items-center justify-between pt-2 border-t border-neutral-200/60 dark:border-neutral-800/80">
            <span class="text-neutral-400">Tx Proof:</span>
            <a id="faucet-success-modal-explorer-link" href="#" target="_blank" class="text-neutral-700 dark:text-neutral-300 hover:text-black dark:hover:text-white underline font-mono flex items-center space-x-1 truncate max-w-[180px]">
              <span id="faucet-success-modal-tx-sig">5KtP9...USDT</span>
              <i data-lucide="external-link" class="w-3 h-3 shrink-0"></i>
            </a>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="space-y-2 pt-1">
        <button type="button" id="faucet-success-modal-done-btn" class="w-full py-3.5 px-4 rounded-2xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-bold text-xs flex items-center justify-center space-x-2 shadow-md active:scale-98 transition-all cursor-pointer">
          <i data-lucide="sparkles" class="w-4 h-4 text-emerald-400"></i>
          <span id="faucet-success-modal-done-text">OK • Start AI Inference</span>
        </button>
      </div>

    </div>
  </div>"""

    target_after_insufficient = """  </div>







  <!-- ======================== JAVASCRIPT CONTROLLER ======================== -->"""

    replacement_after_insufficient = """  </div>







""" + faucet_modal_html + """







  <!-- ======================== JAVASCRIPT CONTROLLER ======================== -->"""

    if target_after_insufficient not in content:
        print("ERROR: target_after_insufficient not found")
        return False
    content = content.replace(target_after_insufficient, replacement_after_insufficient, 1)

    # 2. Insert Faucet Success Modal JS Controller
    faucet_js_code = """    // ======================== FAUCET CLAIMED SUCCESS MODAL CONTROLLER ========================
    const faucetSuccessModal = document.getElementById('faucet-success-modal');
    const closeFaucetSuccessModalBtn = document.getElementById('close-faucet-success-modal-btn');
    const faucetSuccessModalDoneBtn = document.getElementById('faucet-success-modal-done-btn');
    const faucetSuccessModalTitle = document.getElementById('faucet-success-modal-title');
    const faucetSuccessModalSubtitle = document.getElementById('faucet-success-modal-subtitle');
    const faucetSuccessModalHeroLabel = document.getElementById('faucet-success-modal-hero-label');
    const faucetSuccessModalAmount = document.getElementById('faucet-success-modal-amount');
    const faucetSuccessModalVaultBal = document.getElementById('faucet-success-modal-vault-bal');
    const faucetSuccessModalLblVault = document.getElementById('faucet-success-modal-lbl-vault');
    const faucetSuccessModalLblStatus = document.getElementById('faucet-success-modal-lbl-status');
    const faucetSuccessModalTxSig = document.getElementById('faucet-success-modal-tx-sig');
    const faucetSuccessModalExplorerLink = document.getElementById('faucet-success-modal-explorer-link');
    const faucetSuccessModalDoneText = document.getElementById('faucet-success-modal-done-text');

    function hideFaucetSuccessModal() {
      if (faucetSuccessModal) {
        faucetSuccessModal.classList.add('hidden');
      }
    }

    function showFaucetSuccessModal(amount, txSig, explorerUrl) {
      if (!faucetSuccessModal) return;
      const lang = (window.haichainI18n && typeof window.haichainI18n.current === 'function')
        ? window.haichainI18n.current()
        : (localStorage.getItem('haichain-lang') || 'en');
      const isVi = lang === 'vi';

      const title = getDashNotice('faucetClaimed') || (isVi ? 'Nhận Testnet Faucet Thành Công' : 'Testnet Faucet Claimed');
      if (faucetSuccessModalTitle) faucetSuccessModalTitle.textContent = title;
      if (faucetSuccessModalSubtitle) faucetSuccessModalSubtitle.textContent = isVi ? 'Airdrop tức thì trên Solana Devnet' : 'Solana Devnet Instant Airdrop';
      if (faucetSuccessModalHeroLabel) faucetSuccessModalHeroLabel.textContent = isVi ? 'Tiền đã nạp vào Master Vault thành công' : 'Funds Dispatched to Master Vault';

      const numAdded = typeof amount === 'number' ? amount : (parseFloat(amount) || 25.0);
      if (faucetSuccessModalAmount) faucetSuccessModalAmount.textContent = `+${numAdded.toFixed(2)} USDT`;

      const currBal = typeof balance === 'number' ? balance : numAdded;
      if (faucetSuccessModalVaultBal) faucetSuccessModalVaultBal.textContent = `$${currBal.toFixed(4)} USDT`;

      if (faucetSuccessModalLblVault) faucetSuccessModalLblVault.textContent = isVi ? 'Số dư Master Vault:' : 'Master Vault Balance:';
      if (faucetSuccessModalLblStatus) faucetSuccessModalLblStatus.textContent = isVi ? 'Trạng thái:' : 'Status:';
      if (faucetSuccessModalDoneText) faucetSuccessModalDoneText.textContent = isVi ? 'Hoàn tất • Trải nghiệm AI ngay' : 'OK • Start AI Inference';

      if (txSig) {
        const shortSig = txSig.length > 16 ? `${txSig.slice(0, 6)}...${txSig.slice(-6)}` : txSig;
        if (faucetSuccessModalTxSig) faucetSuccessModalTxSig.textContent = shortSig;
        if (faucetSuccessModalExplorerLink) {
          faucetSuccessModalExplorerLink.href = explorerUrl || `https://explorer.solana.com/tx/${txSig}?cluster=devnet`;
        }
      }

      faucetSuccessModal.classList.remove('hidden');
      if (typeof safeCreateIcons === 'function') {
        safeCreateIcons();
      } else if (window.lucide && typeof window.lucide.createIcons === 'function') {
        window.lucide.createIcons();
      }
    }

    if (closeFaucetSuccessModalBtn) {
      closeFaucetSuccessModalBtn.addEventListener('click', hideFaucetSuccessModal);
    }
    if (faucetSuccessModalDoneBtn) {
      faucetSuccessModalDoneBtn.addEventListener('click', hideFaucetSuccessModal);
    }
    if (faucetSuccessModal) {
      faucetSuccessModal.addEventListener('click', (e) => {
        if (e.target === faucetSuccessModal) {
          hideFaucetSuccessModal();
        }
      });
    }
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && faucetSuccessModal && !faucetSuccessModal.classList.contains('hidden')) {
        hideFaucetSuccessModal();
      }
    });"""

    target_js_insert = """    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && insufficientVaultModal && !insufficientVaultModal.classList.contains('hidden')) {
        hideInsufficientVaultModal();
      }
    });"""

    replacement_js_insert = target_js_insert + """







""" + faucet_js_code

    if target_js_insert not in content:
        print("ERROR: target_js_insert not found")
        return False
    content = content.replace(target_js_insert, replacement_js_insert, 1)

    # 3. Replace alert calls in faucet handler
    target_alert1 = """          alert(getDashNotice('faucetClaimed') + '\\n\\n+' + added.toFixed(2) + ' USDT (Solana Devnet)');"""
    repl_alert1 = """          showFaucetSuccessModal(added, txSig, explorerUrl);"""

    if target_alert1 not in content:
        print("ERROR: target_alert1 not found")
        return False
    content = content.replace(target_alert1, repl_alert1, 1)

    target_alert2 = """          alert(getDashNotice('faucetCredited'));"""
    repl_alert2 = """          showFaucetSuccessModal(added);"""

    if target_alert2 not in content:
        print("ERROR: target_alert2 not found")
        return False
    content = content.replace(target_alert2, repl_alert2, 1)

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)

    with open('app/dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: Faucet success modal applied to dashboard.html and app/dashboard.html!")
    return True

if __name__ == '__main__':
    main()
