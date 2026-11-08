import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

for p in glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md'):
    filename = os.path.basename(p)
    m = re.search(r'HAICHAIN_WHITEPAPER_V1.0_([A-Z_]+)\.md', filename)
    if not m:
        continue
    lang = m.group(1)
    if lang in ['EN', 'VI']:
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    
    block_match = re.search(r'```[^`]*?60%[^`]*?```', text, re.DOTALL)
    if block_match:
        old_block = block_match.group(0)
        print(f"File {p}: block length = {len(old_block)}")
        print(repr(old_block[:100]))
