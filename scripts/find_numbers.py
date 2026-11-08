import os, re

for root, dirs, files in os.walk('.'):
    if any(x in root for x in ['.git', 'node_modules', '.gemini']):
        continue
    for f in files:
        if f.endswith(('.html', '.js', '.py')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8') as fp:
                    content = fp.read()
                    if '1. Desktop' in content or '2. Claude' in content or '3. Web' in content:
                        print(f"MATCH in {p}:")
                        for idx, line in enumerate(content.splitlines()):
                            if any(k in line for k in ['1. Desktop', '2. Claude', '3. Web']):
                                print(f"  L{idx+1}: {line.strip()}")
            except Exception as e:
                pass
