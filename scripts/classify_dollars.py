import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'r', encoding='utf-8') as f:
    text = f.read()

# First find all $$ ... $$ blocks
display_blocks = []
def repl_display(m):
    display_blocks.append(m.group(0))
    return f"__DISPLAY_MATH_{len(display_blocks)-1}__"

text_no_display = re.sub(r'\$\$[\s\S]*?\$\$', repl_display, text)

# Now inspect lines with '$'
lines = text_no_display.splitlines()
currencies = []
inline_maths = []
unclassified = []

for line_no, line in enumerate(lines):
    # Find all $ in line
    if '$' not in line:
        continue
    # Check tokens
    # Find paired $...$ where content doesn't look like plain currency
    # Currency pattern: \$(\d[\d,.]*|\d+B|\d+M|HAISI|SOL)\b(?!\$)
    # Inline math: \$([^\$\s](?:[^\$]*?[^\$\s])?)\$
    matches = re.finditer(r'\$([^\$\n]+?)\$', line)
    pos = 0
    line_has_pair = False
    for m in matches:
        content = m.group(1).strip()
        # Is this content a math formula?
        is_math = False
        if any(c in content for c in ['\\', '^', '_', '=', '<', '>', '{', '}']):
            is_math = True
        elif content in ['B', 'K', 'n', 't', 'p', 'd', 'l', 'r']:
            is_math = True
        elif 'AI^2' in content:
            is_math = True
        
        if is_math:
            inline_maths.append((line_no+1, m.group(0)))
            line_has_pair = True
        else:
            unclassified.append((line_no+1, m.group(0)))

    # Also find single $
    single_dollars = re.findall(r'\$(?:[\d,.]+[BMKbmk\+]?|HAISI|SOL)\b', line)
    for s in single_dollars:
        currencies.append((line_no+1, s))

print(f"Total Display Math: {len(display_blocks)}")
print(f"Total Verified Inline Math: {len(inline_maths)}")
print(f"Total Currency ($10, $HAISI, etc): {len(currencies)}")
print(f"Total Unclassified: {len(unclassified)}")

if unclassified:
    print("\n--- Unclassified Samples ---")
    for lno, text_match in unclassified[:15]:
        print(f"Line {lno}: {text_match}")
