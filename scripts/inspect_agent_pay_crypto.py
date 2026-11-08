with open('packages/agent-pay/src/index.ts', 'r', encoding='utf-8') as f:
    code = f.read()

import re
lines = code.splitlines()
for i, l in enumerate(lines):
    if 'nacl.sign.detached.verify' in l or 'crypto.createHash' in l:
        print(f"L{i+1}: {l}")
