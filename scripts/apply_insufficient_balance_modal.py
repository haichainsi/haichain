import os

def main():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert modal HTML
    modal_html = """  <!-- ======================== INSUFFICIENT VAULT BALANCE POPUP MODAL ======================== -->
  <div id="insufficient-vault-modal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-md hidden flex items-end sm:items-center justify-center p-0 sm:p-4 transition-all duration-300" role="dialog" aria-modal="true" aria-labelledby="insufficient-modal-title">
    <div class="w-full sm:max-w-md rounded-t-[32px] sm:rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#0c0c0c] p-5 sm:p-6 shadow-2xl relative max-h-[92vh] overflow-y-auto transform transition-transform duration-300 animate-fadeIn">
      
      <!-- Mobile Drag Handle Bar -->
      <div class="sm:hidden w-12 h-1.5 bg-neutral-300 dark:bg-neutral-700 rounded-full mx-auto mb-3.5"></div>

      <!-- Modal Header -->
      <div class="flex justify-between items-center pb-3.5 border-b border-neutral-100 dark:border-neutral-900">
        <div class="flex items-center space-x-3 min-w-0">
          <div class="w-10 h-10 rounded-2xl bg-amber-500/10 dark:bg-amber-500/15 text-amber-600 dark:text-amber-400 border border-amber-500/20 flex items-center justify-center shrink-0 shadow-sm">
            <i data-lucide="alert-triangle" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <div class="flex items-center space-x-2">
              <h3 id="insufficient-modal-title" class="font-bold text-sm sm:text-base text-black dark:text-white truncate">
                Insufficient Vault Balance
              </h3>
              <span class="text-[9px] font-mono uppercase px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 font-bold border border-amber-500/20 shrink-0">Devnet Faucet</span>
            </div>
            <p id="insufficient-modal-subtitle" class="text-[11px] text-neutral-500 font-mono truncate">
              Master Vault Escrow Protection
            </p>
          </div>
        </div>
        <button id="close-insufficient-modal-btn" class="p-2 rounded-full bg-neutral-100 hover:bg-neutral-200 dark:bg-neutral-800 dark:hover:bg-neutral-700 text-neutral-500 hover:text-black dark:hover:text-white transition-colors shrink-0 ml-2 cursor-pointer" aria-label="Close">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <!-- Modal Body -->
      <div class="my-4 space-y-3 font-mono text-xs">
        <!-- Message Card -->
        <div class="p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-3">
          <div class="flex items-start space-x-2.5">
            <i data-lucide="info" class="w-4 h-4 text-amber-500 shrink-0 mt-0.5"></i>
            <p id="insufficient-modal-message" class="text-xs text-neutral-700 dark:text-neutral-300 leading-relaxed font-sans font-medium">
              Master Vault balance is insufficient for this AI task. Please top up via Faucet.
            </p>
          </div>

          <!-- Balance vs Cost Metrics Grid -->
          <div class="grid grid-cols-2 gap-2 pt-2 border-t border-neutral-200/60 dark:border-neutral-800/80 font-mono text-[11px]">
            <div class="p-2.5 rounded-xl bg-white dark:bg-black/50 border border-neutral-200 dark:border-neutral-800">
              <span id="insufficient-modal-lbl-balance" class="text-neutral-400 text-[10px] block">Current Balance:</span>
              <span id="insufficient-modal-current-bal" class="font-bold text-black dark:text-white">$0.0000 USDT</span>
            </div>
            <div class="p-2.5 rounded-xl bg-white dark:bg-black/50 border border-neutral-200 dark:border-neutral-800">
              <span id="insufficient-modal-lbl-cost" class="text-neutral-400 text-[10px] block">Task Fee:</span>
              <span id="insufficient-modal-required-cost" class="font-bold text-amber-600 dark:text-amber-400">$0.0020 USDT</span>
            </div>
          </div>
        </div>

        <!-- Devnet Faucet Callout Badge -->
        <div class="p-3 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-between text-xs">
          <div class="flex items-center space-x-2 min-w-0">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
            <span id="insufficient-modal-faucet-notice" class="text-[11px] text-emerald-800 dark:text-emerald-300 font-sans font-medium truncate">
              Instant Free Devnet Faucet: +$10.00 USDT
            </span>
          </div>
          <span class="text-[10px] font-mono px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 font-bold shrink-0 ml-2">0% Gas</span>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="space-y-2 pt-1">
        <button type="button" id="insufficient-modal-topup-btn" class="w-full py-3.5 px-4 rounded-2xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-bold text-xs flex items-center justify-center space-x-2 shadow-md active:scale-98 transition-all cursor-pointer">
          <i data-lucide="droplet" class="w-4 h-4 text-emerald-500"></i>
          <span id="insufficient-modal-topup-text">Top up via Faucet (+$10 USDT)</span>
        </button>
        <button type="button" id="insufficient-modal-dismiss-btn" class="w-full py-2.5 px-4 rounded-xl border border-neutral-200 dark:border-neutral-800 hover:bg-neutral-100 dark:hover:bg-neutral-900 text-neutral-600 dark:text-neutral-400 font-semibold text-xs transition-colors cursor-pointer">
          <span id="insufficient-modal-dismiss-text">Dismiss</span>
        </button>
      </div>

    </div>
  </div>"""

    target_modal_place = """        </div>



      </div>



    </div>



  </div>







  <!-- ======================== JAVASCRIPT CONTROLLER ======================== -->"""

    replacement_modal_place = """        </div>



      </div>



    </div>



  </div>







""" + modal_html + """







  <!-- ======================== JAVASCRIPT CONTROLLER ======================== -->"""

    if target_modal_place not in content:
        print("ERROR: target_modal_place not found")
        return False
    content = content.replace(target_modal_place, replacement_modal_place, 1)

    # 2. Insert JS controller
    js_code = """    // ======================== INSUFFICIENT VAULT BALANCE MODAL CONTROLLER ========================
    const insufficientVaultModal = document.getElementById('insufficient-vault-modal');
    const closeInsufficientModalBtn = document.getElementById('close-insufficient-modal-btn');
    const insufficientModalDismissBtn = document.getElementById('insufficient-modal-dismiss-btn');
    const insufficientModalTopupBtn = document.getElementById('insufficient-modal-topup-btn');
    const insufficientModalTitle = document.getElementById('insufficient-modal-title');
    const insufficientModalSubtitle = document.getElementById('insufficient-modal-subtitle');
    const insufficientModalMessage = document.getElementById('insufficient-modal-message');
    const insufficientModalCurrentBal = document.getElementById('insufficient-modal-current-bal');
    const insufficientModalRequiredCost = document.getElementById('insufficient-modal-required-cost');
    const insufficientModalLblBalance = document.getElementById('insufficient-modal-lbl-balance');
    const insufficientModalLblCost = document.getElementById('insufficient-modal-lbl-cost');
    const insufficientModalFaucetNotice = document.getElementById('insufficient-modal-faucet-notice');
    const insufficientModalTopupText = document.getElementById('insufficient-modal-topup-text');
    const insufficientModalDismissText = document.getElementById('insufficient-modal-dismiss-text');

    function hideInsufficientVaultModal() {
      if (insufficientVaultModal) {
        insufficientVaultModal.classList.add('hidden');
      }
    }

    function showInsufficientVaultModal(currBalance, cost, customMsg) {
      if (!insufficientVaultModal) return;
      const lang = (window.haichainI18n && typeof window.haichainI18n.current === 'function')
        ? window.haichainI18n.current()
        : (localStorage.getItem('haichain-lang') || 'en');
      const isVi = lang === 'vi';

      const title = getDashNotice('insufficientVaultBalance') || (isVi ? 'Số dư Vault không đủ' : 'Insufficient Vault Balance');
      const msg = customMsg || getDashNotice('vaultBalanceInsufficientForTask') || (isVi ? 'Số dư Master Vault không đủ cho tác vụ AI này. Vui lòng nạp thêm qua Faucet Devnet.' : 'Master Vault balance is insufficient for this AI task. Please top up via Faucet.');

      if (insufficientModalTitle) insufficientModalTitle.textContent = title;
      if (insufficientModalSubtitle) insufficientModalSubtitle.textContent = isVi ? 'Bảo vệ quỹ ký quỹ Solana Micro-Escrow' : 'Master Vault Escrow Protection';
      if (insufficientModalMessage) insufficientModalMessage.textContent = msg;

      const numBal = typeof currBalance === 'number' ? currBalance : (typeof balance === 'number' ? balance : 0);
      const numCost = typeof cost === 'number' ? cost : (typeof selectedCost === 'number' ? selectedCost : 0.0020);

      if (insufficientModalCurrentBal) insufficientModalCurrentBal.textContent = `$${numBal.toFixed(4)} USDT`;
      if (insufficientModalRequiredCost) insufficientModalRequiredCost.textContent = `$${numCost.toFixed(4)} USDT`;

      if (insufficientModalLblBalance) insufficientModalLblBalance.textContent = isVi ? 'Số dư hiện tại:' : 'Current Balance:';
      if (insufficientModalLblCost) insufficientModalLblCost.textContent = isVi ? 'Phí tác vụ AI:' : 'Task Fee:';
      if (insufficientModalFaucetNotice) insufficientModalFaucetNotice.textContent = isVi ? 'Faucet Devnet miễn phí: +$10.00 USDT' : 'Instant Free Devnet Faucet: +$10.00 USDT';
      if (insufficientModalTopupText) insufficientModalTopupText.textContent = isVi ? 'Nạp tiền qua Faucet (+$10 USDT)' : 'Top up via Faucet (+$10 USDT)';
      if (insufficientModalDismissText) insufficientModalDismissText.textContent = isVi ? 'Đóng' : 'Dismiss';

      insufficientVaultModal.classList.remove('hidden');
      if (typeof safeCreateIcons === 'function') {
        safeCreateIcons();
      } else if (window.lucide && typeof window.lucide.createIcons === 'function') {
        window.lucide.createIcons();
      }
    }

    if (closeInsufficientModalBtn) {
      closeInsufficientModalBtn.addEventListener('click', hideInsufficientVaultModal);
    }
    if (insufficientModalDismissBtn) {
      insufficientModalDismissBtn.addEventListener('click', hideInsufficientVaultModal);
    }
    if (insufficientVaultModal) {
      insufficientVaultModal.addEventListener('click', (e) => {
        if (e.target === insufficientVaultModal) {
          hideInsufficientVaultModal();
        }
      });
    }
    if (insufficientModalTopupBtn) {
      insufficientModalTopupBtn.addEventListener('click', () => {
        hideInsufficientVaultModal();
        if (dashboardDepositModal) {
          dashboardDepositModal.classList.remove('hidden');
          if (typeof selectDepositTab === 'function') {
            selectDepositTab('faucet');
          }
        }
      });
    }
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && insufficientVaultModal && !insufficientVaultModal.classList.contains('hidden')) {
        hideInsufficientVaultModal();
      }
    });"""

    target_js_place = """    closeWalletModalBtn.addEventListener('click', () => walletConnectModal.classList.add('hidden'));



    closeAccountModalBtn.addEventListener('click', () => walletAccountModal.classList.add('hidden'));"""

    replacement_js_place = """    closeWalletModalBtn.addEventListener('click', () => walletConnectModal.classList.add('hidden'));



    closeAccountModalBtn.addEventListener('click', () => walletAccountModal.classList.add('hidden'));







""" + js_code

    if target_js_place not in content:
        print("ERROR: target_js_place not found")
        return False
    content = content.replace(target_js_place, replacement_js_place, 1)

    # 3. Replace playgroundExecuteBtn alert
    target_balance_guard = """      // 2. Strict Real Vault Balance Guard



      if (balance < selectedCost) {



        dashboardDepositModal.classList.remove('hidden');



        if (typeof showToast === 'function') {



          showToast({



            title: getDashNotice('insufficientVaultBalance'),



            message: getDashNotice('vaultBalanceInsufficientForTask'),



            icon: 'alert-circle'



          });



        }



        alert(getDashNotice('vaultBalanceInsufficientForTask'));



        return;



      }"""

    replacement_balance_guard = """      // 2. Strict Real Vault Balance Guard



      if (balance < selectedCost) {



        if (typeof showToast === 'function') {



          showToast({



            title: getDashNotice('insufficientVaultBalance'),



            message: getDashNotice('vaultBalanceInsufficientForTask'),



            icon: 'alert-circle'



          });



        }



        showInsufficientVaultModal(balance, selectedCost);



        return;



      }"""

    if target_balance_guard not in content:
        print("ERROR: target_balance_guard not found")
        return False
    content = content.replace(target_balance_guard, replacement_balance_guard, 1)

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)

    with open('app/dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: Both dashboard.html and app/dashboard.html updated successfully!")
    return True

if __name__ == '__main__':
    main()
