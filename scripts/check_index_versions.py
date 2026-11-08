import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

for m in re.finditer(r'v6\.9\.3|V1\.0|v1\.0', c):
    pos = m.start()
    print('--- MATCH ---')
    print(c[max(0, pos-100):min(len(c), pos+150)].replace('\n', ' '))
