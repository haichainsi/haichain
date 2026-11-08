import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('tab-preseed')
print("Occurrences of tab-preseed:")
while idx != -1:
    print(text[idx-50:idx+200])
    print("=" * 40)
    idx = text.find('tab-preseed', idx+1)
