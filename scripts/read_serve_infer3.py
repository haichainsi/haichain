import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('serve.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 50063 + 3200
print(text[pos:pos+3500])
