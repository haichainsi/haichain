with open('_worker.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Lines 410-435:')
for i in range(410, 435):
    print(f'{i+1}: {lines[i].rstrip()}')

print('\nLines 550-573:')
for i in range(550, len(lines)):
    print(f'{i+1}: {lines[i].rstrip()}')
