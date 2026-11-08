import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_VI.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Protect code blocks
code_blocks = []
clean_md = re.sub(r'```[\s\S]*?```', lambda m: f'CODEBLOCKPLACEHOLDER{len(code_blocks)}END' if not code_blocks.append(m.group(0)) else '', text)

items = re.findall(r'\$\$([\s\S]*?)\$\$', clean_md)
print(f"Total $$ blocks: {len(items)}")
for i, item in enumerate(items):
    first_line = item.strip().splitlines()[0] if item.strip() else 'EMPTY'
    print(f"Block #{i} ({len(item.strip().splitlines())} lines): {repr(first_line[:60])}")
