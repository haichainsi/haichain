with open('pdf-modal.js', 'r', encoding='utf-8') as f:
    c = f.read()

lines = c.splitlines()
print("\n".join(lines[2360:2420]))
print("...")
print("\n".join(lines[2715:2745]))
