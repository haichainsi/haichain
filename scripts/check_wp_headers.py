import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

langs = ['EN', 'VI', 'ZH', 'KO', 'FR', 'ES', 'RU', 'KK', 'HI', 'HE']
for lang in langs:
    fname = f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            lines = [f.readline() for _ in range(8)]
        print(f"=== {lang} ===")
        print("".join(lines))
