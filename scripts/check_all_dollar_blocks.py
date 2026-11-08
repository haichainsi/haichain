import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for lang in ['EN', 'VI']:
    print(f"=== CHECKING $$ BLOCKS IN {lang} ===")
    with open(f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md', 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Find all $$...$$
    blocks = re.findall(r'\$\$([\s\S]*?)\$\$', text)
    for i, b in enumerate(blocks):
        lines = len(b.strip().splitlines())
        if lines > 5 or any(kw in b for kw in ['###', '##', '<p>', '<ol>', '<li>', 'The ', 'Khi ', 'Để ']):
            print(f"  [SUSPECT $$ BLOCK #{i}] lines={lines}: {repr(b.strip()[:100])}")
