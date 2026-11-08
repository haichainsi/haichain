import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('preset-prompt-btn')
idx_start = text.rfind('<div', 0, idx)
idx_start = text.rfind('<div', 0, idx_start)
idx_end = text.find('</section>', idx)
print("QUICK DEMOS section:")
print(text[idx_start:idx_start+1500])
