import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('sale-controller.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'Validate Solana Address format' in line or 'wallet.startsWith(\'0x\')' in line:
        print(f"Line {i+1}:")
        print(''.join(lines[i-2:i+10]))
        break
