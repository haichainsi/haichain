import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const aiHubBtn = document.getElementById(\'ai-hub-btn\');')
print("idx:", idx)
print(text[idx-200:idx+600])
