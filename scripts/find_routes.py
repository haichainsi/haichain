import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('server/production-agent-relayer.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'url.pathname ===' in line:
        print(f"Line {i+1}: {line.strip()}")
