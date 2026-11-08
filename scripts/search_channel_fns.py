with open('programs/haichain-core/src/lib.rs', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['fn open_channel', 'fn close_channel', 'fn settle', 'fn extend_channel_reserve', 'fn dispute', 'fn defend']):
        print(f"L{i+1}: {line.strip()}")
