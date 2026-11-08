import sys
sys.stdout.reconfigure(encoding='utf-8')

for path in ['sale-controller.js', 'app/sale-controller.js']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update EVM provider check in sale-controller.js
    old_evm_check = """        if (isEVM) {
          const mm = (typeof window !== 'undefined' && window.ethereum) ? window.ethereum : null;
          if (!mm) {
            alert(isVi ? "Chưa phát hiện tiện ích MetaMask trên trình duyệt của bạn!" : "MetaMask extension not detected in your browser!");
            return;
          }"""

    new_evm_check = """        if (isEVM) {
          const mm = (typeof window !== 'undefined' && (window.ethereum || (typeof getMetaMaskProvider === 'function' && getMetaMaskProvider()))) ? (window.ethereum || getMetaMaskProvider()) : null;
          if (!mm) {
            const isMobile = (typeof isMobileDevice === 'function' && isMobileDevice()) || /Android|iPhone|iPad|iPod/i.test(navigator.userAgent || '');
            if (isMobile) {
              const appOrigin = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') ? 'https://haichain.pages.dev' : window.location.origin;
              const targetUrl = appOrigin + window.location.pathname + '?auto_pay_saft=1&amount=' + amount + '&wallet=' + encodeURIComponent(wallet) + '&auto_connect=metamask&return_url=' + encodeURIComponent(window.location.href);
              alert(isVi 
                ? "Đang mở ứng dụng MetaMask để bạn xác nhận giao dịch thanh toán bằng tiền thật trong ví..." 
                : "Opening MetaMask App to confirm transaction with real funds...");
              window.location.href = 'https://metamask.app.link/dapp/' + targetUrl.replace(/^https?:\\/\\//, '');
              return;
            }
            alert(isVi ? "Chưa phát hiện tiện ích MetaMask trên trình duyệt của bạn!" : "MetaMask extension not detected in your browser!");
            return;
          }"""

    if old_evm_check in text:
        text = text.replace(old_evm_check, new_evm_check)
        print(f"Patched EVM check in {path}")
    else:
        print(f"WARNING: old_evm_check not found in {path}")

    # 2. Update Solana provider check in sale-controller.js
    old_sol_check = """          if (!provider) {
            alert(isVi ? "Chưa phát hiện tiện ích ví Solana (Phantom hoặc Solflare)!" : "No Solana wallet extension detected!");
            return;
          }"""

    new_sol_check = """          if (!provider) {
            const isMobile = (typeof isMobileDevice === 'function' && isMobileDevice()) || /Android|iPhone|iPad|iPod/i.test(navigator.userAgent || '');
            if (isMobile) {
              const currentUrl = new URL(window.location.href);
              currentUrl.searchParams.set('autoConnect', 'phantom');
              currentUrl.searchParams.set('auto_pay_saft', '1');
              currentUrl.searchParams.set('amount', amount);
              alert(isVi 
                ? "Đang mở ứng dụng Phantom để bạn xác nhận giao dịch thanh toán bằng tiền thật trong ví..." 
                : "Opening Phantom App to confirm transaction with real funds...");
              window.location.href = 'https://phantom.com/ul/browse/' + encodeURIComponent(currentUrl.toString()) + '?ref=' + encodeURIComponent(window.location.origin);
              return;
            }
            alert(isVi ? "Chưa phát hiện tiện ích ví Solana (Phantom hoặc Solflare)!" : "No Solana wallet extension detected!");
            return;
          }"""

    if old_sol_check in text:
        text = text.replace(old_sol_check, new_sol_check)
        print(f"Patched Solana check in {path}")
    else:
        print(f"WARNING: old_sol_check not found in {path}")

    # 3. Handle auto_pay_saft on page load
    saft_auto_listener = """    // Auto-Pay SAFT Handshake for Mobile Wallets (MetaMask / Phantom deep-link return)
    try {
      const saftParams = new URLSearchParams(window.location.search);
      if (saftParams.get('auto_pay_saft') === '1') {
        const payAmount = saftParams.get('amount');
        const payWallet = saftParams.get('wallet');
        
        // Clean URL params
        const cleanUrl = new URL(window.location.href);
        cleanUrl.searchParams.delete('auto_pay_saft');
        cleanUrl.searchParams.delete('amount');
        cleanUrl.searchParams.delete('wallet');
        window.history.replaceState({}, document.title, cleanUrl.toString());

        setTimeout(() => {
          const calcInput = document.getElementById('calc-usdt-input');
          const walletInput = document.getElementById('preseed-wallet');
          const payBtn = document.getElementById('btn-pay-phantom-1click');
          if (calcInput && payAmount) {
            calcInput.value = payAmount;
            calcInput.dispatchEvent(new Event('input'));
          }
          if (walletInput && payWallet) {
            walletInput.value = payWallet;
          }
          const term = document.getElementById('saft-reservation-terminal');
          if (term) term.scrollIntoView({ behavior: 'smooth' });

          setTimeout(() => {
            if (payBtn) payBtn.click();
          }, 600);
        }, 800);
      }
    } catch (_) {}
"""
    # Insert before the closing IIFE or end of file
    idx_end = text.rfind('})();')
    if idx_end != -1:
        text = text[:idx_end] + saft_auto_listener + text[idx_end:]
        print(f"Injected auto_pay_saft handler in {path}")
    else:
        print(f"WARNING: could not find end of IIFE in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

print("Finished updating sale-controller.js files.")
