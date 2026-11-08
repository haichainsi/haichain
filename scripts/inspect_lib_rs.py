with open('programs/haichain-core/src/lib.rs', 'r', encoding='utf-8') as f:
    rust_code = f.read()

print("Length of programs/haichain-core/src/lib.rs:", len(rust_code))
lines = rust_code.splitlines()
print("Total lines:", len(lines))
for i in range(min(100, len(lines))):
    print(f"L{i+1}: {lines[i]}")
