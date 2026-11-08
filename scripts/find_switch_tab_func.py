import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.rfind('function switchAiHubTab')
print(text[idx-50:idx+1200])
