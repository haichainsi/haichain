with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(660, 695):
    print(f"{i+1}: {lines[i]}", end='')
