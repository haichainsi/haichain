with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1850, 1975):
    line = lines[i]
    if '<div' in line or '</div' in line or '<button' in line or '</button' in line:
        print(f"{i+1:4d}: {line.strip()[:100]}")
