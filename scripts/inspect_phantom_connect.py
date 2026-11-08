import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/phantom-deeplink.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('connect: function')
print(text[idx:idx+2500])
