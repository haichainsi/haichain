import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Solana L1')
while idx != -1:
    print(text[idx-100:idx+150])
    print("="*40)
    idx = text.find('Solana L1', idx+1)
