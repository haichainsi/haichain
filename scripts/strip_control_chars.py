import os, re

for base_dir in ['', 'app']:
    for lang in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
        path = os.path.join(base_dir, f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md') if base_dir else f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Strip any ascii control chars except \t and \n
        new_text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)

        if new_text != text:
            print(f"Stripped invisible control chars in {path}")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_text)
