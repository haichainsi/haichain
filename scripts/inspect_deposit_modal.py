import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_idx = text.find('id="dashboard-deposit-modal"')
print(text[s_idx:s_idx+2000])
