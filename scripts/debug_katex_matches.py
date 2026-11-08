import sys, re, markdown
sys.stdout.reconfigure(encoding='utf-8')

for lang in ['EN', 'VI']:
    print(f"=== ANALYZING {lang} ===")
    with open(f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md', 'r', encoding='utf-8') as f:
        md_text = f.read()

    conv = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
    html = conv.convert(md_text)

    # Protect pre blocks
    parts = re.split(r'(<pre[\s\S]*?</pre>)', html, flags=re.IGNORECASE)

    for idx in range(0, len(parts), 2):
        t = parts[idx]
        # Currency protect
        t = re.sub(r'(?<!\\)\$(\d[\d,.]*(?:\s*(?:million|billion|trillion|[kKmMbB]))?(?:\+)?)', r'&#36;\1', t)
        t = re.sub(r'(?<!\\)\$(HAISI|SOL|USDT|BTC|ETH)\b', r'&#36;\1', t)
        
        # Display math
        t = re.sub(r'\$\$([\s\S]*?)\$\$', '', t)
        
        # Check inline math
        inline_matches = re.finditer(r'(?<!\\)\$([^\$\n\r<]+?)\$', t)
        for m in inline_matches:
            val = m.group(1).strip()
            # If it has spaces and no math symbols:
            math_symbols = ['\\', '_', '^', '=', '+', '-', '<', '>', '{', '}']
            has_math_symbol = any(s in val for s in math_symbols)
            if not has_math_symbol and len(val.split()) > 1:
                print(f"  [FALSE INLINE MATH] '{val}'")
            elif any(tag in val for tag in ['<', '>', 'li', 'p', 'div']):
                print(f"  [HTML LEAK] '{val}'")
