import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_idx = text.find('id="wallet-connect-modal"')
e_idx = text.find('id="wallet-account-modal"')
print(f"Modal range: {s_idx} to {e_idx}")
if s_idx != -1 and e_idx != -1:
    print(text[s_idx:e_idx])
