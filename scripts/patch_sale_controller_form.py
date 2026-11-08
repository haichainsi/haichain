import sys
sys.stdout.reconfigure(encoding='utf-8')

files = ['sale-controller.js', 'app/sale-controller.js']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the validation:
    # if (wallet.startsWith('0x') || wallet.length < 32 || wallet.length > 44)
    old_val = """        // Validate Solana Address format (Base58, 32-44 characters, no 0x)
        if (wallet.startsWith('0x') || wallet.length < 32 || wallet.length > 44) {
          alert(getActiveLang() === 'vi' 
            ? 'Địa chỉ ví không hợp lệ. Ví Solana phải ở định dạng Base58 (32-44 ký tự, không bắt đầu bằng 0x).' 
            : 'Invalid Solana address. Must be Base58 format (32-44 characters, no 0x prefix).');
          return;
        }"""

    new_val = """        // Validate Wallet Address format (Supports Solana Base58 32-44 chars or EVM 0x 42 chars)
        const isSolanaAddr = !wallet.startsWith('0x') && wallet.length >= 32 && wallet.length <= 44;
        const isEvmAddr = wallet.startsWith('0x') && wallet.length === 42;
        if (!isSolanaAddr && !isEvmAddr) {
          alert(getActiveLang() === 'vi' 
            ? 'Địa chỉ ví không hợp lệ. Vui lòng cung cấp địa chỉ ví Solana (Base58) hoặc ví EVM MetaMask (0x... 42 ký tự).' 
            : 'Invalid wallet address. Please provide a valid Solana (Base58) or EVM MetaMask (0x...) address.');
          return;
        }"""

    if old_val in content:
        content = content.replace(old_val, new_val)
        print(f"Replaced address validation in {filepath}")
    else:
        print(f"Old validation not found in {filepath}")

    # Ensure mainnetGuarantee: true is in allocs[wallet]
    old_alloc = """          allocs[wallet] = {
            name: name,
            email: email,
            amountUsdt: amount,
            haiTokens: totalHaiNum,
            price: 0.007,
            tgePrice: 0.010,
            token2022Mint: "3fkCXyEAxwodEksGcgGcMFTKCpGYzzWTUyQocF2qJkWu",
            purchasedAt: new Date().toISOString(),
            txSignature: "4MqTEpY6WCBE71PZ4jmH4dZWZQ5dmvQtK7i1A7ma3hMJknrkD6w297g8bTV6KKGRERmAwyrpQkh14eHMjHHWB2oU"
          };"""

    new_alloc = """          allocs[wallet] = {
            name: name,
            email: email,
            amountUsdt: amount,
            haiTokens: totalHaiNum,
            price: 0.007,
            tgePrice: 0.010,
            token2022Mint: "3fkCXyEAxwodEksGcgGcMFTKCpGYzzWTUyQocF2qJkWu",
            purchasedAt: new Date().toISOString(),
            txSignature: "4MqTEpY6WCBE71PZ4jmH4dZWZQ5dmvQtK7i1A7ma3hMJknrkD6w297g8bTV6KKGRERmAwyrpQkh14eHMjHHWB2oU",
            paymentMethod: isEvmAddr ? 'MetaMask Web3 SAFT' : 'Solana Web3 SAFT',
            mainnetGuarantee: true
          };"""

    if old_alloc in content:
        content = content.replace(old_alloc, new_alloc)
        print(f"Replaced alloc structure in {filepath}")
    else:
        print(f"Old alloc not found in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done patching sale controllers.")
