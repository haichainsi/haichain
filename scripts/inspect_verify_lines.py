with open('packages/agent-pay/src/index.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'verifyVoucher' in line or 'verifyPayment' in line or 'nacl.sign.detached.verify' in line:
        print(f"L{i+1}: {line.strip()}")
