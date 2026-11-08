with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = 3500
end = 3700

with open('scripts/tab_docs_slice2.txt', 'w', encoding='utf-8') as out:
    for i in range(start, min(end, len(lines))):
        out.write(f"{i+1}: {lines[i]}")

print("Wrote scripts/tab_docs_slice2.txt")
