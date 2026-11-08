import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# We can find the code block that starts with ``` and contains (60% and ends with ```
for p in glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md') + glob.glob('app/HAICHAIN_WHITEPAPER_V1.0_*.md'):
    filename = os.path.basename(p)
    m = re.search(r'HAICHAIN_WHITEPAPER_V1.0_([A-Z_]+)\.md', filename)
    if not m:
        continue
    lang = m.group(1)
    if lang in ['EN', 'VI']:
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Match the code block containing 60%
    block_match = re.search(r'```[^\n]*\n[^\n]*\n[^\n]*\n.*?60%.*?```', text, re.DOTALL)
    if block_match:
        old_block = block_match.group(0)
        # Check if it has 60% and 40%
        if '60%' in old_block and '40%' in old_block:
            print(f"Found 60/40 diagram in {p}: length {len(old_block)}")
            # Let's inspect
