import sys
sys.stdout.reconfigure(encoding='utf-8')

for lang in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
    with open(f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md', 'r', encoding='utf-8') as f:
        text = f.read()
    c = text.count('$$')
    print(f'[{lang}] $$ count: {c} (even: {c % 2 == 0})')
