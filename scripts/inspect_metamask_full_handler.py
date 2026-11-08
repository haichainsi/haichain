import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("// METAMASK WALLET (EVM & Solana Snap Support)")
print(text[idx:idx+2500])
