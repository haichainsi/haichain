import re

for filename in ['index.html', 'app/index.html', 'dashboard.html', 'app/dashboard.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        if 'external-link' in line and any(w in line or (idx > 0 and any(w in lines[idx-1] for w in ['whitepaper', 'Whitepaper'])) or (idx < len(lines)-1 and any(w in lines[idx+1] for w in ['whitepaper', 'Whitepaper'])) for w in ['whitepaper', 'Whitepaper', 'saft', 'SAFT', 'memo', 'Memo']):
            print(f"{filename}:{idx+1}: {line.strip()}")
