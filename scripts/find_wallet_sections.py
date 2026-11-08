import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

targets = [
    'function updateWalletBtnUI',
    'function normalizeProviderName',
    'function openAccountModal',
    'async function setConnectedWallet',
    'document.querySelectorAll(\'.wallet-provider-btn\')'
]

for t in targets:
    for idx, l in enumerate(lines):
        if t in l:
            print(f"[{t}] at line {idx+1}")
            break
