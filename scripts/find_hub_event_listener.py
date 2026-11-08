import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.rfind('aiHubBtn.addEventListener')
if idx == -1:
    idx = text.rfind('ai-hub-btn')
print(text[idx-100:idx+1500])
