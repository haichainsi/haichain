import sys, re, markdown
sys.stdout.reconfigure(encoding='utf-8')

for lang in ['EN', 'VI']:
    print(f"=== CHECKING KATEX INPUT FOR {lang} ===")
    with open(f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md', 'r', encoding='utf-8') as f:
        md_text = f.read()

    conv = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
    html = conv.convert(md_text)

    # Split by <pre>
    parts = re.split(r'(<pre[\s\S]*?</pre>)', html, flags=re.IGNORECASE)

    # Let's inspect display math
    for idx in range(0, len(parts), 2):
        t = parts[idx]
        for m in re.finditer(r'<p>\s*\$\$([\s\S]*?)\$\$\s*</p>', t):
            f = m.group(1)
            if any(kw in f for kw in ['<ol>', '<li>', '<p>', 'Reveal', 'Invariant']):
                print(f"  [BAD DISPLAY MATH P]: {repr(f[:120])}")
        for m in re.finditer(r'\$\$([\s\S]*?)\$\$', t):
            f = m.group(1)
            if any(kw in f for kw in ['<ol>', '<li>', '<p>', 'Reveal', 'Invariant']):
                print(f"  [BAD DISPLAY MATH RAW]: {repr(f[:120])}")

        # Check inline math
        for m in re.finditer(r'(?<!\\)\$([^\$\n\r]+?)\$', t):
            f = m.group(1)
            if any(kw in f for kw in ['<ol>', '<li>', '<p>', 'Reveal', 'Invariant', 'Soulbound']):
                print(f"  [BAD INLINE MATH]: {repr(f[:120])}")
