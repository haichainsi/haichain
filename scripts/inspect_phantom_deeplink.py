import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('assets/phantom-deeplink.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("phantom-deeplink.js overview:")
print(text[:2500])
