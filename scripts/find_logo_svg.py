import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Look for haichain logo SVG in index.html
svgs = re.findall(r'<svg[^>]*>.*?</svg>', c[:8000], re.DOTALL)
print(f"SVGs in top of index.html: {len(svgs)}")
for s in svgs[:3]:
    print("--- SVG ---")
    print(s[:500])
