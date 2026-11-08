import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('/api/gateway/stats')
print(text[pos-100:pos+800])
