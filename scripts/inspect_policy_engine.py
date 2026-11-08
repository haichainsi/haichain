with open('sdk/typescript/src/policy-engine.ts', 'r', encoding='utf-8') as f:
    code = f.read()

print("Length of policy-engine.ts:", len(code))
print("First 80 lines:")
print('\n'.join(code.splitlines()[:80]))
