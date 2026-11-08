import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('serve.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('/api/infer')
print("Position:", pos)
if pos != -1:
    print(text[pos:pos+3500])
