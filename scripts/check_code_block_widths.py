import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'r', encoding='utf-8') as f:
    c = f.read()

code_blocks = re.findall(r'```(?:[a-zA-Z0-9_-]*)\n(.*?)\n```', c, re.DOTALL)
print(f"Total code blocks: {len(code_blocks)}")
for i, block in enumerate(code_blocks):
    lines = block.splitlines()
    max_len = max(len(l) for l in lines) if lines else 0
    first_line = lines[0] if lines else ""
    print(f"Block {i+1}: max line length = {max_len} chars")
