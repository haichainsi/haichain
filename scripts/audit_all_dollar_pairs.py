import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for lang in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
    path = f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find all occurrences of $$
    indices = [m.start() for m in re.finditer(r'\$\$', text)]
    print(f"\n==========================================")
    print(f"[{lang}] Total '$$' tokens: {len(indices)} (is even? {len(indices) % 2 == 0})")
    
    if len(indices) % 2 != 0:
        print(f"  WARNING: ODD NUMBER OF '$$' TOKENS!")

    for i in range(0, len(indices) - 1, 2):
        start = indices[i]
        end = indices[i+1]
        content = text[start+2:end]
        lines = content.strip().splitlines()
        if len(lines) > 5 or any(kw in content for kw in ['###', '##', 'Theorem', 'Định lý', 'Bất biến', 'Invariant', 'Proof', 'Chứng minh']):
            start_line = text[:start].count('\n') + 1
            end_line = text[:end].count('\n') + 1
            print(f"  [CORRUPTED DISPLAY MATH] Lines {start_line} to {end_line} ({len(lines)} lines):")
            print(f"    Preview: {repr(content.strip()[:100])}")
