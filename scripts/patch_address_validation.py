import sys, re
sys.stdout.reconfigure(encoding='utf-8')

pattern = re.compile(
    r'\/\/\s*Validate Solana Address format[^\n]*\n\s*if\s*\(\s*wallet\.startsWith\(\'0x\'\)[^\}]*\}',
    re.MULTILINE
)

replacement = """// Validate Wallet Address format (Supports Solana Base58 32-44 chars or EVM 0x 42 chars)
        const isSolanaAddr = !wallet.startsWith('0x') && wallet.length >= 32 && wallet.length <= 44;
        const isEvmAddr = wallet.startsWith('0x') && wallet.length === 42;
        if (!isSolanaAddr && !isEvmAddr) {
          alert(getActiveLang() === 'vi' 
            ? 'Địa chỉ ví không hợp lệ. Vui lòng cung cấp địa chỉ ví Solana (Base58) hoặc ví EVM MetaMask (0x... 42 ký tự).' 
            : 'Invalid wallet address. Please provide a valid Solana (Base58) or EVM MetaMask (0x...) address.');
          return;
        }"""

for fpath in ['sale-controller.js', 'app/sale-controller.js']:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_c, count = pattern.subn(replacement, c)
    if count > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Replaced address format check in {fpath} ({count} occurrence(s))")
    else:
        print(f"Pattern not found in {fpath}")

