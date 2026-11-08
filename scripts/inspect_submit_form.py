import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('sale-controller.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'submit-preseed-form' in line or 'submitBtn.addEventListener' in line:
        print(f"Found at line {i+1}")
        print(''.join(lines[i:i+60]))
        break
