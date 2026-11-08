import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    text = f.read()

terms = [
    'Pay with Phantom',
    'ALLOCATION & RETURN CALCULATOR',
    'View SAFT',
    'Token-2022',
    'Solana L1',
    'Sub-Agent Capability Tree'
]

for t in terms:
    idx = text.find(t)
    print(f"Term '{t}': found={idx != -1}")
    if idx != -1:
        print(text[idx-50:idx+250])
        print("="*40)
