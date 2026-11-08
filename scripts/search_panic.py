with open('programs/haichain-core/src/lib.rs', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['panic_stop', 'emergency_stop', 'freeze_pot', 'kill_switch']):
        print(f"L{i+1}: {line.strip()}")
