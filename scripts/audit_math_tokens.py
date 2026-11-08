import re, sys, glob

sys.stdout.reconfigure(encoding='utf-8')

for fn in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()

    display_math = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
    inline_math = re.findall(r'(?<!\\)\$([^\$\n]+)\$', text)

    print(f"=== {fn} ===")
    print(f"  Display math ($$...$$): {len(display_math)}")
    print(f"  Inline math ($...$): {len(inline_math)}")
    # Sample inline math
    samples = [f"${m}$" for m in inline_math[:5]]
    print(f"  Samples: {', '.join(samples)}")
