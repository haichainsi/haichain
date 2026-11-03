import os

files_to_update = [
    'dashboard.html',
    os.path.join('app', 'dashboard.html'),
    'i18n.js',
    os.path.join('app', 'i18n.js')
]

for fpath in files_to_update:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    count_before = content.count('HAIChain')
    if count_before > 0:
        content = content.replace('HAIChain', 'Haichain')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SUCCESS: Replaced {count_before} occurrences of 'HAIChain' with 'Haichain' in {fpath}")
    else:
        print(f"NOTICE: No occurrences of 'HAIChain' in {fpath}")

# Verification check
print("\n--- VERIFICATION ---")
for fpath in files_to_update:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        rem = c.count('HAIChain')
        print(f"{fpath}: remaining 'HAIChain' = {rem}")
