with open('server/tee-cosigner.ts', 'r', encoding='utf-8') as f:
    code = f.read()

print("Length of server/tee-cosigner.ts:", len(code))
print("First 80 lines:")
print('\n'.join(code.splitlines()[:80]))
