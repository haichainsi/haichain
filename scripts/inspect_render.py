with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(2440, 2520):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
