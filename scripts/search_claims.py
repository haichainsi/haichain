import os

patterns = ['Claude Theorem', 'OtterSec', 'Neodyme', 'Nuclear Immunity Fortress', 'military-hardened', 'Claude Audit', 'Claude audit']

for root, dirs, files in os.walk('.'):
    if any(p in root for p in ['.git', 'node_modules', '.cargo', 'target', '.gemini', 'artifacts']):
        continue
    for f in files:
        if f.endswith(('.html', '.md', '.ts', '.js', '.json', '.rs', '.py')):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
                    text = fh.read()
                    for p in patterns:
                        if p.lower() in text.lower():
                            print(f'Found "{p}" in {path}')
            except Exception:
                pass
