import sys
sys.stdout.reconfigure(encoding='utf-8')

replacements = {
    'ZH': ('按照 0.1% 的费率进行清算抽成', '按照 0.05% 的费率进行清算抽成'),
    'KO': ('0.1%의 청산 마진을', '0.05%의 청산 마진을'),
    'ES': ('Comisión del 0.1% capturada', 'Comisión del 0.05% capturada'),
    'FR': ('Prélèvement de 0.1% capturé', 'Prélèvement de 0.05% capturé'),
    'RU': ('Сбор 0.1% удерживается', 'Сбор 0.05% удерживается'),
    'KK': ('Сбор 0.1% удерживается', 'Сбор 0.05% удерживается'),
    'HI': ('Сбор 0.1% удерживается', 'Сбор 0.05% удерживается'),
}

for lang, (old_str, new_str) in replacements.items():
    f_path = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md"
    with open(f_path, 'r', encoding='utf-8') as f:
        txt = f.read()
    if old_str in txt:
        txt = txt.replace(old_str, new_str)
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(txt)
        print(f"[OK] Replaced in {lang}: {old_str} -> {new_str}")
    else:
        print(f"[WARN] Target not found in {lang}")

print("\nAudit again:")
for lang in ['ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI']:
    f_path = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md"
    with open(f_path, 'r', encoding='utf-8') as f:
        txt = f.read()
    print(f"{lang}: has '0.1%' = {'0.1%' in txt}, has '0.05%' = {'0.05%' in txt}")
