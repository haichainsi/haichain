with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = 2860
end = 3200
for i in range(start, min(end, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')
