with open('packages/agent-pay-python/haichain_pay/paywall.py', 'r', encoding='utf-8') as f:
    code = f.read()

print("Length of paywall.py:", len(code))
lines = code.splitlines()
print("Total lines:", len(lines))
for i in range(min(120, len(lines))):
    print(f"L{i+1}: {lines[i]}")
