with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'wallet-provider-btn' in line or 'data-provider' in line or 'connectPhantom' in line or 'connectSolflare' in line or 'connectMetaMask' in line or 'connectWallet' in line:
        if idx > 1500: # in script section or modals
            print(f"Line {idx+1}: {line.strip()[:100]}")
