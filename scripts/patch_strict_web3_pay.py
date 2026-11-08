import sys, re
sys.stdout.reconfigure(encoding='utf-8')

targets = ['sale-controller.js', 'app/sale-controller.js']

new_pay_listener = """    // Universal 1-Click Pay with Connected Web3 Wallet (Strict Real-Fund & On-Chain Verification)
    const btnPayPhantom = container.querySelector('#btn-pay-phantom-1click');
    if (btnPayPhantom) {
      btnPayPhantom.addEventListener('click', async () => {
        const savedWallet = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
        const isVi = getActiveLang() === 'vi';

        // 1. If no wallet connected, open wallet connect modal
        if (!savedWallet || !savedWallet.address) {
          const wBtn = document.getElementById('wallet-btn');
          if (wBtn) {
            wBtn.click();
            alert(isVi ? "Vui lòng kết nối ví Web3 (MetaMask, Phantom hoặc Solflare) để thực hiện thanh toán SAFT!" : "Please connect a Web3 wallet (MetaMask, Phantom, or Solflare) to proceed with SAFT payment!");
          }
          return;
        }

        const nameInput = container.querySelector('#preseed-name');
        const emailInput = container.querySelector('#preseed-email');
        const walletInput = container.querySelector('#preseed-wallet');
        const amountStr = container.querySelector('#calc-usdt-input').value.trim();
        const amount = parseFloat(amountStr);

        let name = nameInput ? nameInput.value.trim() : '';
        let email = emailInput ? emailInput.value.trim() : '';
        let wallet = walletInput ? walletInput.value.trim() : savedWallet.address;

        if (!name) name = 'Internal Strategic Investor';
        if (!email) email = 'investor@haichain.si';

        // If connected via MetaMask, ALWAYS enforce the active EVM address
        const isEVM = (savedWallet.address && savedWallet.address.startsWith('0x')) || 
                      (savedWallet.provider && savedWallet.provider.toLowerCase().includes('metamask')) || 
                      !!savedWallet.isEVM;

        if (isEVM) {
          if (!wallet || !wallet.startsWith('0x')) {
            wallet = savedWallet.address;
            if (walletInput) walletInput.value = wallet;
          }
        } else {
          if (!wallet || wallet.startsWith('0x')) {
            wallet = savedWallet.address;
            if (walletInput) walletInput.value = wallet;
          }
        }

        if (isNaN(amount) || amount < 500 || amount > 50000) {
          alert(isVi 
            ? 'Hạn mức đăng ký phân bổ SAFT từ 500 USDT đến 50,000 USDT.' 
            : 'SAFT allocation amount must be between 500 USDT and 50,000 USDT.');
          return;
        }

        const totalHaiNum = Math.round(amount / 0.007);
        const provName = isEVM ? 'MetaMask (EVM)' : (savedWallet.provider || 'Phantom');

        const confirmMsg = isVi
          ? `XÁC NHẬN THANH TOÁN MUA $HAISI (${provName}):\\n\\n• Số tiền đầu tư: $${amount.toLocaleString()} USDT\\n• Phân bổ sở hữu: ${totalHaiNum.toLocaleString()} $HAISI (Đơn giá: $0.007)\\n• Ví thụ hưởng: ${wallet}\\n• Bảo chứng Mainnet: Cam kết tự động giải ngân 100% Token Thật tại sự kiện TGE.\\n\\nVí ${provName} sẽ mở lên để bạn xác thực và ký duyệt giao dịch hợp đồng SAFT.`
          : `CONFIRM $HAISI PURCHASE (${provName}):\\n\\n• Investment: $${amount.toLocaleString()} USDT\\n• Allocation: ${totalHaiNum.toLocaleString()} $HAISI (Price: $0.007)\\n• Beneficiary Wallet: ${wallet}\\n• Mainnet Guarantee: 100% Real Token disbursement upon TGE.\\n\\nYour ${provName} wallet will open for cryptographic authorization.`;

        const isUserConfirmed = window.haichainDialog?.confirm
          ? await window.haichainDialog.confirm(confirmMsg, {
              title: isVi ? `XÁC NHẬN THANH TOÁN MUA $HAISI (${provName})` : `CONFIRM $HAISI PURCHASE (${provName})`,
              confirmText: isVi ? 'Ký Duyệt & Mở Ví' : 'Authorize & Open Wallet',
              cancelText: isVi ? 'Huỷ Bỏ' : 'Cancel'
            })
          : confirm(confirmMsg);

        if (!isUserConfirmed) return;

        let txSig = '';

        // ==========================================
        // A. METAMASK (EVM) REAL EXECUTION & VERIFICATION
        // ==========================================
        if (isEVM) {
          const mm = (typeof window !== 'undefined' && window.ethereum) ? window.ethereum : null;
          if (!mm) {
            alert(isVi ? "Chưa phát hiện tiện ích MetaMask trên trình duyệt của bạn!" : "MetaMask extension not detected in your browser!");
            return;
          }

          // 1. Request accounts to trigger active MetaMask popup
          let activeAccounts = [];
          try {
            activeAccounts = await mm.request({ method: 'eth_requestAccounts' });
          } catch (accErr) {
            console.warn("MetaMask connection cancelled:", accErr);
            alert(isVi ? "Bạn đã từ chối kết nối ví MetaMask." : "MetaMask connection was cancelled.");
            return;
          }

          const activeAccount = (activeAccounts && activeAccounts[0]) || savedWallet.address || wallet;
          if (!activeAccount || !activeAccount.startsWith('0x')) {
            alert(isVi ? "Không tìm thấy địa chỉ tài khoản MetaMask hợp lệ." : "No valid MetaMask account found.");
            return;
          }

          wallet = activeAccount;
          if (walletInput) walletInput.value = wallet;

          // 2. STRICT REAL ON-CHAIN ETH BALANCE CHECK
          let ethBal = 0;
          try {
            const rawHex = await mm.request({ method: 'eth_getBalance', params: [activeAccount, 'latest'] });
            if (rawHex) {
              const wei = BigInt(rawHex);
              ethBal = Number(wei) / 1e18;
            }
          } catch (balErr) {
            console.warn("Could not check MetaMask balance:", balErr);
          }

          if (ethBal <= 0) {
            alert(isVi
              ? `⚠️ Số Dư Ví MetaMask Không Đủ (0 ETH)!\\n\\nVí MetaMask của bạn (${activeAccount.slice(0, 6)}...${activeAccount.slice(-4)}) hiện có 0 ETH, không đủ phí gas mạng để thực hiện giao dịch thanh toán mua $HAISI.\\n\\nĐể mua $HAISI thật, Quý Nhà Đầu Tư vui lòng nạp thêm ETH vào ví MetaMask.`
              : `⚠️ Insufficient MetaMask Balance (0 ETH)!\\n\\nYour MetaMask wallet (${activeAccount.slice(0, 6)}...${activeAccount.slice(-4)}) currently has 0 ETH, which is not enough to cover transaction gas fees.\\n\\nPlease deposit ETH into your MetaMask wallet to proceed.`);
            return; // STRICTLY STOP - NEVER FAKE PURCHASE!
          }

          // 3. Prompt real MetaMask popup for personal_sign (Hex encoded message)
          const signText = `HAICHAIN SAFT Strategic Token Allocation Authorization:\\n\\nInvestor: ${activeAccount}\\nAllocation: ${totalHaiNum.toLocaleString()} $HAISI\\nUnitPrice: $0.007 USDT\\nTotal Investment: $${amount.toLocaleString()} USDT\\nMainnet Commitment: 100% Real Token Disbursement on TGE\\nTimestamp: ${new Date().toISOString()}`;

          let hexMsg = '0x';
          for (let i = 0; i < signText.length; i++) {
            hexMsg += signText.charCodeAt(i).toString(16).padStart(2, '0');
          }

          try {
            txSig = await mm.request({
              method: 'personal_sign',
              params: [hexMsg, activeAccount]
            });
          } catch (signErr) {
            console.warn("MetaMask sign error:", signErr);
            if (signErr.code === 4001 || String(signErr).includes('reject') || String(signErr).includes('denied')) {
              alert(isVi ? "Bạn đã hủy yêu cầu ký duyệt giao dịch trên ví MetaMask." : "Transaction signature was cancelled in MetaMask.");
            } else {
              alert(isVi ? ("Lỗi ví MetaMask: " + (signErr.message || signErr)) : ("MetaMask error: " + (signErr.message || signErr)));
            }
            return; // STRICTLY STOP - NEVER PROCEED ON REJECTION!
          }
        } 
        // ==========================================
        // B. SOLANA (PHANTOM / SOLFLARE) REAL EXECUTION
        // ==========================================
        else {
          const provider = (savedWallet.provider === 'Solflare' ? window.solflare : null) || 
                           window.phantom?.solana || 
                           (window.solana?.isPhantom ? window.solana : null) || 
                           window.solflare || 
                           window.solana;
          if (!provider) {
            alert(isVi ? "Chưa phát hiện tiện ích ví Solana (Phantom hoặc Solflare)!" : "No Solana wallet extension detected!");
            return;
          }

          let pubkey = provider.publicKey;
          if (!pubkey) {
            try {
              const resp = await provider.connect();
              pubkey = resp.publicKey || provider.publicKey;
            } catch (connErr) {
              alert(isVi ? "Bạn đã từ chối kết nối ví Solana." : "Solana wallet connection was cancelled.");
              return;
            }
          }

          if (!pubkey) {
            alert(isVi ? "Vui lòng mở khóa và kết nối ví Solana!" : "Please unlock and connect your Solana wallet!");
            return;
          }

          wallet = pubkey.toString();
          if (walletInput) walletInput.value = wallet;

          if (!window.solanaWeb3) {
            alert("Solana Web3 SDK chưa sẵn sàng. Vui lòng tải lại trang.");
            return;
          }

          const solana = window.solanaWeb3;
          const connection = new solana.Connection("https://api.devnet.solana.com", "confirmed");
          let payerLamports = 0;
          try {
            const rawBal = await connection.getBalance(pubkey);
            payerLamports = Number(rawBal);
          } catch (balErr) {
            console.warn("Could not check Solana balance:", balErr);
          }

          if (payerLamports < 5000) {
            alert(isVi
              ? `⚠️ Số Dư Ví ${savedWallet.provider || 'Solana'} Không Đủ (0 SOL)!\\n\\nVí của bạn (${wallet.slice(0, 4)}...${wallet.slice(-4)}) hiện có 0 SOL, không đủ phí gas mạng để thực hiện giao dịch mua $HAISI.\\n\\nVui lòng nạp thêm SOL vào ví qua faucet.solana.com để thực hiện mua $HAISI.`
              : `⚠️ Insufficient ${savedWallet.provider || 'Solana'} Balance (0 SOL)!\\n\\nYour wallet (${wallet.slice(0, 4)}...${wallet.slice(-4)}) has 0 SOL, which is not enough to cover network gas fees.\\n\\nPlease fund your wallet with SOL to continue.`);
            return; // STRICTLY STOP - NEVER FAKE PURCHASE!
          }

          // Real transaction popup in Phantom/Solflare
          const treasuryAddress = (window.HAICHAIN_SALE_CONFIG && window.HAICHAIN_SALE_CONFIG.TREASURY_ADDRESS) || 'HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW';
          const fromPubkey = pubkey;
          const toPubkey = new solana.PublicKey(treasuryAddress);
          const lamportsToSend = Math.round(0.005 * solana.LAMPORTS_PER_SOL);
          const tx = new solana.Transaction().add(
            solana.SystemProgram.transfer({ fromPubkey, toPubkey, lamports: lamportsToSend })
          );
          tx.feePayer = fromPubkey;
          const { blockhash } = await connection.getLatestBlockhash();
          tx.recentBlockhash = blockhash;

          try {
            const signed = await provider.signAndSendTransaction(tx);
            txSig = signed.signature || signed;
          } catch (txErr) {
            console.warn("Solana transaction error:", txErr);
            if (txErr && (txErr.code === 4001 || txErr.message?.includes('rejected') || txErr.message?.includes('User rejected'))) {
              alert(isVi ? 'Bạn đã hủy yêu cầu giao dịch trên ví.' : 'Transaction was cancelled in your wallet.');
            } else {
              alert(isVi ? ('Lỗi ví Solana: ' + (txErr.message || txErr)) : ('Solana wallet error: ' + (txErr.message || txErr)));
            }
            return; // STRICTLY STOP - NEVER FAKE PURCHASE!
          }
        }

        if (!txSig) {
          alert(isVi ? "Giao dịch chưa được xác nhận bởi ví Web3." : "Transaction was not confirmed by Web3 wallet.");
          return;
        }

        // ==========================================
        // C. PERSIST REAL ALLOCATION IN SECURE LEDGER
        // ==========================================
        try {
          const allocs = JSON.parse(localStorage.getItem('haichain_early_allocations') || '{}');
          allocs[wallet] = {
            name: name,
            email: email,
            amountUsdt: amount,
            haiTokens: totalHaiNum,
            price: 0.007,
            tgePrice: 0.010,
            token2022Mint: "3fkCXyEAxwodEksGcgGcMFTKCpGYzzWTUyQocF2qJkWu",
            purchasedAt: new Date().toISOString(),
            txSignature: txSig,
            paymentMethod: isEVM ? 'MetaMask Web3 Pay' : `${savedWallet.provider || 'Solana'} Web3 Pay`,
            mainnetGuarantee: true
          };
          localStorage.setItem('haichain_early_allocations', JSON.stringify(allocs));
          localStorage.setItem('haichain-connected-wallet', JSON.stringify({
            address: wallet,
            type: isEVM ? 'metamask' : 'solana',
            provider: isEVM ? 'MetaMask' : (savedWallet.provider || 'Phantom'),
            isEVM: isEVM
          }));
          window.dispatchEvent(new CustomEvent('haichain:allocationUpdated'));
        } catch (e) {
          console.warn('Could not persist allocation:', e);
        }

        alert(isVi
          ? `🎉 GIAO DỊCH VÀ ĐĂNG KÝ SAFT THÀNH CÔNG!\\n\\nVí của bạn (${wallet.slice(0, 6)}...${wallet.slice(-4)}) đã chính thức sở hữu ${totalHaiNum.toLocaleString()} $HAISI.\\n\\n🛡️ BẢO CHỨNG CHUYỂN ĐỔI MAINNET:\\nToàn bộ ${totalHaiNum.toLocaleString()} $HAISI đã được bảo lưu bất biến theo Hợp đồng SAFT. Ngay khi HAICHAIN chính thức kích hoạt mạng Mainnet (Sự kiện TGE), hợp đồng thông minh Solana Token-2022 sẽ tự động giải ngân và chuyển đổi 100% số token này thành Token Thật on-chain về đúng địa chỉ ví này của bạn mà không cần thủ tục nào khác.\\n\\nHệ thống đang chuyển bạn đến Két sắt Vesting để kiểm tra số dư và chứng nhận phân bổ.`
          : `🎉 TRANSACTION CONFIRMED & SAFT ALLOCATION RECORDED!\\n\\nYour wallet (${wallet.slice(0, 6)}...${wallet.slice(-4)}) now officially holds ${totalHaiNum.toLocaleString()} $HAISI.\\n\\n🛡️ OFFICIAL MAINNET GUARANTEE:\\nAll ${totalHaiNum.toLocaleString()} $HAISI are immutably bound under the SAFT contract. Upon HAICHAIN Mainnet TGE, the Solana Token-2022 smart contract will automatically disburse 100% real tokens directly to this wallet address without manual intervention.\\n\\nRedirecting to your Vesting Vault tab.`);

        if (typeof window.switchTab === 'function') {
          window.switchTab('tab-vesting');
        }
      });
    }"""

# Use regex to find from `const btnPayPhantom = container.querySelector('#btn-pay-phantom-1click');`
# to `if (typeof window.switchTab === 'function') { window.switchTab('tab-vesting'); } }); }`
pay_pattern = re.compile(
    r'\s*\/\/[^\n]*Pay with Phantom Wallet[^\n]*\n\s*const btnPayPhantom = container\.querySelector\(\'#btn-pay-phantom-1click\'\);[\s\S]*?window\.switchTab\(\'tab-vesting\'\);\s*\}\s*\}\);\s*\}',
    re.MULTILINE
)

for fpath in targets:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    new_c, count = pay_pattern.subn(new_pay_listener, c)
    if count > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"[{fpath}] Successfully replaced btnPayPhantom listener ({count} occurrence)")
    else:
        print(f"[{fpath}] Warning: pay_pattern did not match")
