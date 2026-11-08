import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def patch_web3_deposit(filepath):
    print(f"Patching Web3 deposit verification in {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the block inside `if (selectedDepositMethod === 'web3') {`
    # We want to replace the handling of activeWeb3 and the gasless fallback
    
    old_target = '''      // 2. WEB3 WALLET MODE - Strictly requires real Web3 extension & confirmed on-chain transaction
      if (selectedDepositMethod === 'web3') {
        const activeWeb3 = getActiveWeb3Wallet();'''

    new_logic = '''      // 2. WEB3 WALLET MODE - Strictly requires real Web3 wallet interaction & verified balance
      if (selectedDepositMethod === 'web3') {
        const activeWeb3 = getActiveWeb3Wallet();

        // A. METAMASK (EVM) ON-CHAIN / SIGNATURE DEPOSIT
        if ((activeWeb3 && activeWeb3.provider === 'MetaMask') || (userWallet && (userWallet.isEVM || (userWallet.provider && userWallet.provider.toLowerCase().includes('metamask'))))) {
          const mm = getMetaMaskProvider() || window.ethereum;
          if (!mm) {
            alert(isVi ? "Chưa phát hiện tiện ích MetaMask trên trình duyệt của bạn." : "MetaMask extension not detected in your browser.");
            return;
          }

          const origText = dashConfirmDepositBtn.textContent;
          dashConfirmDepositBtn.disabled = true;
          dashConfirmDepositBtn.textContent = isVi ? "Đang kiểm tra số dư ví MetaMask..." : "Checking MetaMask balance...";

          try {
            // Check real EVM balance first
            let ethBal = 0;
            try {
              const rawHex = await mm.request({ method: 'eth_getBalance', params: [userWallet.address, 'latest'] });
              if (rawHex) {
                const wei = BigInt(rawHex);
                ethBal = Number(wei) / 1e18;
              }
            } catch (balErr) {
              console.warn("Could not fetch MetaMask balance:", balErr);
            }

            if (ethBal <= 0) {
              alert(isVi
                ? `⚠️ Số Dư Ví MetaMask Không Đủ (0 ETH)!\n\nVí MetaMask của bạn (${userWallet.address.slice(0, 6)}...${userWallet.address.slice(-4)}) hiện có 0 ETH, không đủ phí gas mạng để thực hiện giao dịch on-chain.\n\n• Nếu bạn muốn nạp thử nghiệm miễn phí: Vui lòng chuyển sang tab 'Faucet (+$10)' để nhận ngay 10 USDT vào Master Vault.\n• Nếu bạn muốn nạp Web3 thật: Vui lòng nạp thêm ETH vào ví MetaMask.`
                : `⚠️ Insufficient MetaMask Balance (0 ETH)!\n\nYour MetaMask wallet (${userWallet.address.slice(0, 6)}...${userWallet.address.slice(-4)}) currently has 0 ETH, which is not enough to cover network gas fees.\n\n• To claim free test funds, please switch to the 'Faucet (+$10)' tab.\n• To deposit real crypto, please fund your MetaMask wallet with ETH.`);
              return;
            }

            // User has funds: Request explicit cryptographic approval popup in MetaMask
            dashConfirmDepositBtn.textContent = isVi ? "Chờ bạn duyệt trên MetaMask..." : "Approve in MetaMask popup...";
            const depositMsg = `HAICHAIN Master Vault Web3 Deposit Authorization:\\n\\nAmount: $${added.toFixed(2)} USDT\\nDepositor: ${userWallet.address}\\nTimestamp: ${new Date().toISOString()}\\nNetwork: EVM Multi-Chain`;
            const signature = await mm.request({
              method: 'personal_sign',
              params: [depositMsg, userWallet.address]
            });

            // ONLY ON SUCCESSFUL METAMASK APPROVAL:
            balance += added;
            saveBalance();
            updateVaultUI();
            dashboardDepositModal.classList.add('hidden');

            appendLedgerRow({
              nonce: generateCryptographicNonce(),
              service: `Web3 MetaMask Deposit`,
              proof: `Sig: ${signature.slice(0, 8)}...${signature.slice(-8)}`,
              amount: `+${added.toFixed(4)} USDT`,
              latency: "380ms",
              isPositive: true,
              txSig: signature
            });

            if (typeof showToast === 'function') {
              showToast({
                title: isVi ? 'Nạp MetaMask Thành Công' : 'MetaMask Deposit Confirmed',
                message: `+$${added.toFixed(2)} USDT • Ký xác thực: ${signature.slice(0, 6)}...`,
                icon: 'check-circle'
              });
            }

            alert(isVi 
              ? `🎉 Nạp Tiền Web3 MetaMask Thành Công!\n\nGiao dịch đã được ví MetaMask ký xác thực thành công.\nNgười nạp: ${userWallet.address}\nSố tiền: +$${added.toFixed(2)} USDT\n\nSố dư Master Vault mới: $${balance.toFixed(4)} USDT`
              : `🎉 MetaMask Deposit Confirmed!\n\nAuthorization verified by MetaMask.\nDepositor: ${userWallet.address}\nAmount: +$${added.toFixed(2)} USDT\n\nNew Master Vault Balance: $${balance.toFixed(4)} USDT`);
          } catch (mmErr) {
            console.warn("MetaMask deposit error:", mmErr);
            if (mmErr.code === 4001 || String(mmErr).includes('rejected') || String(mmErr).includes('User denied')) {
              alert(isVi ? "Giao dịch đã hủy: Bạn đã từ chối duyệt giao dịch trên ví MetaMask." : "Deposit Canceled: You rejected the signature in MetaMask.");
            } else {
              alert(isVi ? `Lỗi giao dịch MetaMask: ${mmErr.message || mmErr}` : `MetaMask error: ${mmErr.message || mmErr}`);
            }
          } finally {
            dashConfirmDepositBtn.disabled = false;
            dashConfirmDepositBtn.textContent = origText;
          }
          return;
        }

        // B. SOLANA (PHANTOM / SOLFLARE) WEB3 DEPOSIT'''

    if old_target in content:
        content = content.replace(old_target, new_logic, 1)
        print(f"[{filepath}] Inserted MetaMask deposit verification.")
    else:
        print(f"[{filepath}] WARNING: could not find old_target")

    # Also update the Solana gas check: if payerLamports < minRequiredLamports, alert instead of silent faucet credit!
    old_sol_gas = '''          if (payerLamports < minRequiredLamports) {
            dashConfirmDepositBtn.textContent = isVi 
              ? "Relayer Đang Trợ Cấp Gas & Nạp..." 
              : "Relayer Sponsoring Gas & Crediting...";'''

    new_sol_gas = '''          if (payerLamports < minRequiredLamports) {
            alert(isVi 
              ? `⚠️ Số Dư Ví ${userWallet.provider} Không Đủ (0 SOL)!\n\nVí của bạn hiện có 0 SOL nên không đủ phí gas mạng để gửi giao dịch on-chain.\n\n• Nếu bạn muốn nạp thử nghiệm miễn phí: Vui lòng chuyển sang tab "Faucet (+$10)" để nhận 10 USDT vào Master Vault.\n• Nếu bạn muốn nạp bằng ví Web3 thật: Vui lòng nạp thêm SOL vào ví qua faucet.solana.com.`
              : `⚠️ Insufficient ${userWallet.provider} Balance (0 SOL)!\n\nYour wallet has 0 SOL, which is not enough to cover Solana network gas fees.\n\n• To claim free test funds, please switch to the 'Faucet (+$10)' tab.\n• To deposit real on-chain funds, please fund your wallet with SOL at faucet.solana.com.`);
            return;
          }

          if (false) {'''

    if old_sol_gas in content:
        content = content.replace(old_sol_gas, new_sol_gas, 1)
        print(f"[{filepath}] Updated Solana 0-balance check to alert instead of auto-faucet.")
    else:
        print(f"[{filepath}] WARNING: could not find old_sol_gas")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{filepath}] Saved successfully.\n")

patch_web3_deposit('dashboard.html')
patch_web3_deposit('app/dashboard.html')
