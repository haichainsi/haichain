import sys
import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<div id="wallet-connect-modal"[^>]*>(.*?)</div>\s*<!--\s*5\.\s*CONNECTED', text, re.DOTALL)
content = m.group(1)

# Search for Custom Solana Public Key inside content
idx = content.find('Custom Solana Public Key')
print('Index of Custom Solana Public Key:', idx)
if idx != -1:
    snippet = content[max(0, idx - 400):min(len(content), idx + 400)]
    print(snippet)
