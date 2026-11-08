import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

translations_metamask = {
    "vi": {
        "modal.walletMetamask": "Ví MetaMask",
        "modal.walletMetamaskDesc": "Đa chuỗi EVM & Solana Snap (Ethereum, BSC, Arbitrum, Polygon)"
    },
    "en": {
        "modal.walletMetamask": "MetaMask Wallet",
        "modal.walletMetamaskDesc": "EVM Multi-Chain & Solana Snap (Ethereum, BSC, Arbitrum, Polygon)"
    },
    "zh": {
        "modal.walletMetamask": "MetaMask 小狐狸钱包",
        "modal.walletMetamaskDesc": "EVM 多链与 Solana Snap 支持 (Ethereum, BSC, Arbitrum, Polygon)"
    },
    "fr": {
        "modal.walletMetamask": "Portefeuille MetaMask",
        "modal.walletMetamaskDesc": "Multi-chaîne EVM & Solana Snap (Ethereum, BSC, Arbitrum, Polygon)"
    },
    "ko": {
        "modal.walletMetamask": "메타마스크 (MetaMask)",
        "modal.walletMetamaskDesc": "EVM 멀티체인 및 Solana Snap 지원 (Ethereum, BSC, Arbitrum, Polygon)"
    },
    "es": {
        "modal.walletMetamask": "Billetera MetaMask",
        "modal.walletMetamaskDesc": "Multicadena EVM y Solana Snap (Ethereum, BSC, Arbitrum, Polygon)"
    },
    "ru": {
        "modal.walletMetamask": "Кошелёк MetaMask",
        "modal.walletMetamaskDesc": "Мультичейн EVM и Solana Snap (Ethereum, BSC, Arbitrum, Polygon)"
    },
    "kk": {
        "modal.walletMetamask": "MetaMask әмияны",
        "modal.walletMetamaskDesc": "EVM мульти-желі және Solana Snap (Ethereum, BSC, Arbitrum, Polygon)"
    },
    "hi": {
        "modal.walletMetamask": "मेटामास्क वॉलेट (MetaMask)",
        "modal.walletMetamaskDesc": "EVM मल्टी-चेन और Solana Snap (Ethereum, BSC, Arbitrum, Polygon)"
    },
    "he": {
        "modal.walletMetamask": "ארנק MetaMask",
        "modal.walletMetamaskDesc": "ריבוי-רשתות EVM ו-Solana Snap (Ethereum, BSC, Arbitrum, Polygon)"
    }
}

def apply_i18n_patch(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = content
    for lang, dict_keys in translations_metamask.items():
        # Look for "modal.walletSolflareDesc": "..." in this lang block
        # We find the lang block
        pattern = r'(\"' + lang + r'\":\s*\{[\s\S]*?\"modal\.walletSolflareDesc\":\s*\"[^\"]+\",)'
        match = re.search(pattern, modified)
        if match:
            # Check if modal.walletMetamask already exists in this block
            if f'"{lang}":' in match.group(1) and '"modal.walletMetamask"' in match.group(1):
                print(f"[{filepath}] {lang} already contains modal.walletMetamask")
                continue

            insert_lines = (
                f'\n    "modal.walletMetamask": "{dict_keys["modal.walletMetamask"]}",'
                f'\n    "modal.walletMetamaskDesc": "{dict_keys["modal.walletMetamaskDesc"]}",'
            )
            repl = match.group(1) + insert_lines
            modified = modified[:match.start()] + repl + modified[match.end():]
            print(f"[{filepath}] Added MetaMask keys to {lang}")
        else:
            print(f"[{filepath}] WARNING: could not find modal.walletSolflareDesc in {lang}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(modified)
    print(f"[{filepath}] Saved successfully.")

apply_i18n_patch('i18n.js')
apply_i18n_patch('app/i18n.js')
