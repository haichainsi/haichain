import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

res = subprocess.run(['git', 'show', 'HEAD:sale-controller.js'], capture_output=True, text=True, encoding='utf-8')
lines = res.stdout.splitlines()
print(f'Total lines in HEAD: {len(lines)}')
print('\n'.join(lines[1460:1480]))
print("...")
print('\n'.join(lines[2010:2026]))
