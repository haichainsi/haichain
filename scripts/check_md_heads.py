import sys
sys.stdout.reconfigure(encoding='utf-8')

languages = ['VI', 'EN', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']

for lang in languages:
    fn = f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
    with open(fn, 'r', encoding='utf-8') as f:
        head = [f.readline().strip() for _ in range(12)]
    print(f"=== {lang} ({fn}) ===")
    for l in head[:6]:
        if l:
            print("  " + l)
