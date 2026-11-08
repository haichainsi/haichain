with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(2830, 2860):
    print(f"{i+1}: {lines[i]}", end='')
