import re

def patch(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Quick Demos label
    content = content.replace('<span>Quick Demos:</span>', '<span data-i18n="playground.quickDemos">Quick Demos:</span>')

    # 2. Vesting overview banner
    content = re.sub(
        r'\$\{isVi\s*\?\s*`Ví <strong class="text-black dark:text-white">\$\{shortAddr\}</strong> đang sở hữu.*?`\s*:\s*`Investor <strong class="text-black dark:text-white">\$\{shortAddr\}</strong> holds.*?`\}',
        r'${shortAddr}: ${haiTotal.toLocaleString()} $HAISI (Token-2022 Transfer-Hook Locked)',
        content,
        flags=re.DOTALL
    )

    # 3. dashConfirmDepositBtn.textContent
    content = re.sub(
        r'dashConfirmDepositBtn\.textContent = isVi\s*\?\s*"Kết Nối Ví Phantom Để Nạp"\s*:\s*"Connect Phantom to Deposit";',
        r"dashConfirmDepositBtn.textContent = getDashNotice('connectPhantomToDeposit');",
        content,
        flags=re.DOTALL
    )

    # 4. Faucet toast & alert
    content = re.sub(
        r'message: isVi\s*\?\s*`\+\$\{added\.toFixed\(2\)\} USDT thử nghiệm đã nạp vào ví.*?`\s*:\s*`\+\$\{added\.toFixed\(2\)\} USDT testnet funds credited.*?`,',
        r"message: `+${added.toFixed(2)} USDT ${getDashNotice('faucetCredited')}`,",
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'alert\(isVi\s*\?\s*`🎉 Nhận USDT Thử Nghiệm Devnet Thành Công!.*?`\s*:\s*`🎉 Devnet Testnet USDT Claimed!.*?`\);',
        r"alert(getDashNotice('faucetCredited'));",
        content,
        flags=re.DOTALL
    )

    # 5. MetaMask insufficient & deposit
    content = re.sub(
        r'alert\(isVi\s*\?\s*`⚠️ Số Dư Ví MetaMask Không Đủ \(0 ETH\)!.*?`\s*:\s*`⚠️ MetaMask Balance Insufficient \(0 ETH\)!.*?`\);',
        r"alert(getDashNotice('metaMaskInsufficientEth'));",
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 MetaMask Thành Công!.*?`\s*:\s*`🎉 Web3 MetaMask Deposit Confirmed!.*?`\);',
        r"alert(getDashNotice('metaMaskDepositSuccess'));",
        content,
        flags=re.DOTALL
    )

    # 6. Web3 connected prompt
    content = re.sub(
        r'alert\(isVi\s*\?\s*`Đã kết nối ví \$\{userWallet\.provider\} thành công!.*?`\s*:\s*`Connected \$\{userWallet\.provider\} wallet successfully!.*?`\);',
        r"alert(getDashNotice('web3ConnectedConfirmPrompt'));",
        content,
        flags=re.DOTALL
    )

    # 7. No web3 wallet
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Chưa phát hiện tiện ích ví Web3 \(Phantom hoặc Solflare\).*?"\s*:\s*"Web3 wallet \(Phantom or Solflare\) not detected.*?"\);',
        r"alert(getDashNotice('noWeb3DetectedFaucetGuide'));",
        content,
        flags=re.DOTALL
    )

    # 8. 0 SOL
    content = re.sub(
        r'alert\(isVi\s*\?\s*`⚠️ Số Dư Ví \$\{userWallet\.provider\} Không Đủ \(0 SOL\)!.*?`\s*:\s*`⚠️ Insufficient SOL in \$\{userWallet\.provider\} \(0 SOL\)!.*?`\);',
        r"alert(getDashNotice('insufficientSolGaslessGuide'));",
        content,
        flags=re.DOTALL
    )

    # 9. Gasless subsidized toast
    content = re.sub(
        r'message: isVi\s*\?\s*`\+\$\{added\.toFixed\(2\)\} USDT đã vào Master Vault & Trợ cấp 0\.02 SOL vào ví`\s*:\s*`\+\$\{added\.toFixed\(2\)\} USDT credited & 0\.02 SOL gas subsidized`,',
        r"message: `+${added.toFixed(2)} USDT (${getDashNotice('gaslessDepositSuccess')})`,",
        content,
        flags=re.DOTALL
    )

    # 10. Web3 success
    content = re.sub(
        r'alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 Thành Công!\s*\\n\\nGiao dịch đã được xác nhận bất biến trên mạng Solana Devnet\..*?`\s*:\s*`🎉 Web3 Deposit Confirmed!.*?`\);',
        r"alert(getDashNotice('web3DepositConfirmedDevnet'));",
        content,
        flags=re.DOTALL
    )

    # 11. Fiat sandbox
    content = re.sub(
        r'alert\(isVi\s*\?\s*`Thông Báo Cổng Thanh Toán Fiat \(\$\{methodName\}\):.*?`\s*:\s*`Fiat Gateway Notice \(\$\{methodName\}\):.*?`\);',
        r"alert(getDashNotice('fiatSandboxNotice'));",
        content,
        flags=re.DOTALL
    )

    # 12. Zero balance withdrawal
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Số dư trong Master Vault của bạn hiện tại là \$0\.0000 USDT.*?"\s*:\s*"Your Master Vault balance is \$0\.0000 USDT.*?"\);',
        r"alert(getDashNotice('zeroBalanceCannotWithdraw'));",
        content,
        flags=re.DOTALL
    )

    # 13. Insufficient withdrawal balance
    content = re.sub(
        r'alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault hiện tại của bạn là \$.*?`\s*:\s*`Insufficient balance!.*?`\);',
        r"alert(getDashNotice('insufficientWithdrawBalance'));",
        content,
        flags=re.DOTALL
    )

    # 14. Invalid Solana address
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Địa chỉ ví đích không hợp lệ!.*?"\s*:\s*"Invalid destination address!.*?"\);',
        r"alert(getDashNotice('invalidSolanaAddress'));",
        content,
        flags=re.DOTALL
    )

    # 15. Task balance insufficient toast & alert
    content = re.sub(
        r'message: isVi\s*\?\s*`Số dư Master Vault \(\$.*?`\s*:\s*`Master Vault balance \(\$.*?`,',
        r"message: getDashNotice('vaultBalanceInsufficientForTask'),",
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault của bạn hiện tại là \$.*?để tiếp tục\.`\s*:\s*`Insufficient balance!.*?to continue\.`\);',
        r"alert(getDashNotice('vaultBalanceInsufficientForTask'));",
        content,
        flags=re.DOTALL
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully patched: {filename}')

patch('dashboard.html')
patch('app/dashboard.html')
