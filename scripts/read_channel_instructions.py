with open('programs/haichain-core/src/lib.rs', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(735, 850):
    if i < len(lines):
        print(f"L{i+1}: {lines[i]}", end='')
