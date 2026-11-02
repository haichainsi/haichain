import sys

sys.stdout.reconfigure(encoding='utf-8')

for p in ['index.html', 'dashboard.html', 'app/index.html', 'app/dashboard.html']:
    with open(p, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print('=== ' + p + ' METADATA ===')
    for i in range(min(60, len(lines))):
        line = lines[i].strip()
        l_low = line.lower()
        if '<title>' in l_low or 'name="description"' in l_low or 'og:description' in l_low or 'twitter:description' in l_low or 'og:title' in l_low:
            print(f'Line {i+1}: {line}')
