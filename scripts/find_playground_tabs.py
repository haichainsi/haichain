import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('tab-playground')
print("Occurrences of tab-playground:")
while idx != -1:
    print(text[idx-40:idx+80])
    idx = text.find('tab-playground', idx+1)
