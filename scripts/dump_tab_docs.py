import sys

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where tab-docs or devhub starts and ends
start = 2850
end = 3500

with open('scripts/tab_docs_slice.txt', 'w', encoding='utf-8') as out:
    for i in range(start, min(end, len(lines))):
        out.write(f"{i+1}: {lines[i]}")

print("Wrote scripts/tab_docs_slice.txt successfully")
