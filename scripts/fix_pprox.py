import os, re

for base_dir in ['', 'app']:
    for lang in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
        path = os.path.join(base_dir, f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md') if base_dir else f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

        new_text = re.sub(r'(\s+)pprox\b', r'\1\\approx', text)
        new_text = re.sub(r'(?<!\\)pprox\b', r'\\approx', new_text)

        if new_text != text:
            print(f"Fixed pprox in {path}")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_text)
