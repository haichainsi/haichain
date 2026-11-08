with open('packages/agent-pay/src/index.ts', 'r', encoding='utf-8') as f:
    ts_code = f.read()

print("Length of packages/agent-pay/src/index.ts:", len(ts_code))
print("First 80 lines:")
print('\n'.join(ts_code.splitlines()[:80]))
