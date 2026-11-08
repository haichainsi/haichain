import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('app/pdf-modal.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'(telegram|resend|email|notify|api\/saft|send)', text, re.IGNORECASE)]
print("Total matches in pdf-modal.js:", len(matches))

lines = text.split('\n')
for idx, line in enumerate(lines):
    if any(k in line.lower() for k in ['resend', 'telegram', 'send_email', 'mail', 'saft_signed', 'api/saft', 'api/notify']):
        print(f"Line {idx+1}: {line.strip()[:140]}")
