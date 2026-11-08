import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add data-i18n to playground
    content = content.replace('<span>Quick Demos:</span>', '<span data-i18n="playground.quickDemos">Quick Demos:</span>')
    content = content.replace('<span class="truncate">Anti-Drain</span>', '<span class="truncate" data-i18n="playground.demoAntiDrain">Anti-Drain</span>')
    content = content.replace('<span class="truncate">Micro-Escrow</span>', '<span class="truncate" data-i18n="playground.demoMicroEscrow">Micro-Escrow</span>')
    content = content.replace('<span class="truncate">Optimus AI</span>', '<span class="truncate" data-i18n="playground.demoOptimus">Optimus AI</span>')
    content = content.replace('<span class="truncate">Anchor CPI</span>', '<span class="truncate" data-i18n="playground.demoAnchor">Anchor CPI</span>')

    # 2. Replace wallet notices (matches 1, 2, 3)
    content = re.sub(
        r'walletNoticeText\.innerHTML\s*=\s*isVi\s*\?\s*"<strong>Chưa phát hiện tiện ích Phantom</strong>[^"]*"\s*:\s*"<strong>Phantom extension not detected</strong>[^"]*";',
        "walletNoticeText.innerHTML = getVestingText('phantomNotDetected');",
        content
    )
    content = re.sub(
        r'walletNoticeText\.innerHTML\s*=\s*isVi\s*\?\s*"<strong>Chưa phát hiện tiện ích MetaMask</strong>[^"]*"\s*:\s*"<strong>MetaMask extension not detected</strong>[^"]*";',
        "walletNoticeText.innerHTML = getVestingText('metaMaskNotDetectedFull');",
        content
    )
    content = re.sub(
        r'walletNoticeText\.innerHTML\s*=\s*isVi\s*\?\s*"<strong>Chưa phát hiện tiện ích Solflare</strong>[^"]*"\s*:\s*"<strong>Solflare extension not detected</strong>[^"]*";',
        "walletNoticeText.innerHTML = getVestingText('solflareNotDetected');",
        content
    )

    # 3. Match 4: Token-2022 mint copy alert
    content = re.sub(
        r'alert\(isVi\s*\?\s*`ĐÃ SAO CHÉP ĐỊA CHỈ MINT TOKEN-2022[\s\S]*?Transfer-Hook status\.`\);',
        "alert(getVestingText('copiedToken2022Alert') + '\\n\\n' + TOKEN_2022_MINT);",
        content
    )

    # 4. Matches 5 & 6: dashConfirmDepositBtn text
    content = re.sub(
        r'dashConfirmDepositBtn\.textContent\s*=\s*isVi\s*\?\s*"Xác Nhận Nạp On-Chain \(Ký Ví Phantom\)"\s*:\s*"Confirm On-Chain Deposit \(Sign with Phantom\)";',
        "dashConfirmDepositBtn.textContent = getDashNotice('confirmOnChainDepositPhantom');",
        content
    )
    content = re.sub(
        r'dashConfirmDepositBtn\.textContent\s*=\s*isVi\s*\?\s*"Kết Nối Ví Phantom Để Nạp"\s*:\s*"Connect Phantom Wallet to Deposit";',
        "dashConfirmDepositBtn.textContent = getDashNotice('connectPhantomToDeposit');",
        content
    )

    # 5. Match 7: Faucet toast message
    content = re.sub(
        r'message:\s*isVi\s*\?\s*`\+\$\{added\.toFixed\(2\)\} USDT thử nghiệm[^`]*`\s*:\s*`\+\$\{added\.toFixed\(2\)\} Devnet test USDT[^`]*`',
        "message: getDashNotice('faucetClaimed') + ' (+' + added.toFixed(2) + ' USDT)'",
        content
    )

    # 6. Match 8: Faucet alert
    content = re.sub(
        r'alert\(isVi\s*\?\s*`🎉 Nhận USDT Thử Nghiệm Devnet Thành Công![\s\S]*?\?cluster=devnet`\);',
        "alert(getDashNotice('faucetClaimed') + '\\n\\n+' + added.toFixed(2) + ' USDT (Solana Devnet)');",
        content
    )

    # 7. Match 9: MetaMask insufficient ETH
    content = re.sub(
        r'alert\(isVi\s*\?\s*`⚠️ Số Dư Ví MetaMask Không Đủ \(0 ETH\)![\s\S]*?to test on Solana Devnet\.`\);',
        "alert(getDashNotice('metaMaskInsufficientEth'));",
        content
    )

    # 8. Match 10: MetaMask deposit success
    content = re.sub(
        r'alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 MetaMask Thành Công![\s\S]*?Instant Settlement: 380ms\.`\);',
        "alert(getDashNotice('metaMaskDepositSuccess'));",
        content
    )

    # 9. Match 11: Web3 connected confirm prompt
    content = re.sub(
        r'alert\(isVi\s*\?\s*`Đã kết nối ví \$\{userWallet\.provider\} thành công![\s\S]*?on Solana Devnet\.`\);',
        "alert(getDashNotice('web3ConnectedConfirmPrompt'));",
        content
    )

    # 10. Match 12: No web3 detected faucet guide
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Chưa phát hiện tiện ích ví Web3 \(Phantom hoặc Solflare\)[\s\S]*?to receive free testnet funds\."\);',
        "alert(getDashNotice('noWeb3DetectedFaucetGuide'));",
        content
    )

    # 11. Match 13: Insufficient SOL gasless guide
    content = re.sub(
        r'alert\(isVi\s*\?\s*`⚠️ Số Dư Ví \$\{userWallet\.provider\} Không Đủ \(0 SOL\)![\s\S]*?0% Gas Fee Subsidy\.`\);',
        "alert(getDashNotice('insufficientSolGaslessGuide'));",
        content
    )

    # 12. Match 14: Gasless deposit toast message
    content = re.sub(
        r'message:\s*isVi\s*\?\s*`\+\$\{added\.toFixed\(2\)\} USDT đã vào Master Vault[^`]*`\s*:\s*`\+\$\$\{added\.toFixed\(2\)\} USDT credited[^`]*`',
        "message: getDashNotice('gaslessDepositSuccess') + ' (+$' + added.toFixed(2) + ' USDT)'",
        content
    )

    # 13. Match 15: Gasless deposit alert
    content = re.sub(
        r'alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 Thành Công \(Hỗ Trợ 0% Phí Gas\)![\s\S]*?enjoy 0% Gas Fees on Solana Devnet!`\);',
        "alert(getDashNotice('web3DepositConfirmedDevnet'));",
        content
    )

    # 14. Match 16: Web3 deposit confirmed devnet alert
    content = re.sub(
        r'alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 Thành Công![\s\S]*?\?cluster=devnet`\);',
        "alert(getDashNotice('web3DepositConfirmedDevnet'));",
        content
    )

    # 15. Match 17: Fiat sandbox notice
    content = re.sub(
        r'alert\(isVi\s*\?\s*`Thông Báo Cổng Thanh Toán Fiat \(\$\{methodName\}\):[\s\S]*?test for free on Solana Devnet!`\);',
        "alert(getDashNotice('fiatSandboxNotice'));",
        content
    )

    # 16. Match 18: Zero balance cannot withdraw
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Số dư trong Master Vault của bạn hiện tại là \$0\.0000 USDT\.[\s\S]*?Cannot withdraw\."\);',
        "alert(getDashNotice('zeroBalanceCannotWithdraw'));",
        content
    )

    # 17. Match 19: Insufficient withdraw balance
    content = re.sub(
        r'alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault hiện tại của bạn là[\s\S]*?withdraw \$\$\{amount\.toFixed\(4\)\} USDT\.`\);',
        "alert(getDashNotice('insufficientWithdrawBalance'));",
        content
    )

    # 18. Match 20: Invalid Solana destination address
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Địa chỉ ví đích không hợp lệ![\s\S]*?e\.g\., HD1b\.\.\.5nVW\)\."\);',
        "alert(getDashNotice('invalidSolanaAddress'));",
        content
    )

    # 19. Match 21: Withdraw success notice
    content = re.sub(
        r'alert\(isVi\s*\?\s*`Rút tiền thành công!\\n\\nĐã giải ngân[\s\S]*?Instant Sub-Second Retraction\)\.`\);',
        "alert(getDashNotice('withdrawSuccessNotice'));",
        content
    )

    # 20. Matches 22, 23, 24: Generated AI responses
    content = re.sub(
        r'generatedResponse = isVi\s*\?\s*`\[HAICHAIN Security Kernel: Phân Tích An Toàn AI Độc Quyền\][\s\S]*?`\s*:\s*`\[HAICHAIN Security Kernel: Frontier Agent Protection\]',
        "generatedResponse = `[HAICHAIN Security Kernel: Frontier Agent Protection]",
        content
    )

    content = re.sub(
        r'generatedResponse = isVi\s*\?\s*`\[Mã Lệnh Solana Anchor Xác Thực Hợp Đồng Vi Thanh Toán\][\s\S]*?`\s*:\s*`\[Solana Anchor Smart Contract: Escrow Settlement Code\]',
        "generatedResponse = `[Solana Anchor Smart Contract: Escrow Settlement Code]",
        content
    )

    content = re.sub(
        r'generatedResponse = isVi\s*\?\s*`\[Phân Tích Tự Hành Cấp Độ Doanh Nghiệp qua \$\{selectedModel\}\][\s\S]*?`\s*:\s*`\[Autonomous Enterprise Inference via \$\{selectedModel\}\]',
        "generatedResponse = `[Autonomous Enterprise Inference via ${selectedModel}]",
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Done patching: {filepath}')

patch_file('dashboard.html')
patch_file('app/dashboard.html')
