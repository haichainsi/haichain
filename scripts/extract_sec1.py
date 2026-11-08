with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = 3070
end = 3310
with open('scripts/current_sec1_block.html', 'w', encoding='utf-8') as out:
    for i in range(start, end):
        out.write(f"{i+1}: {lines[i]}")

print("Wrote scripts/current_sec1_block.html")
