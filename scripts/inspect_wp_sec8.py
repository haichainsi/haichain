import glob, re, sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('HAICHAIN_WHITEPAPER_V1.0_*.md')):
    if f.endswith('_EN.md') or f.endswith('_VI.md'):
        continue
    with open(f, 'r', encoding='utf-8') as fl:
        text = fl.read()
    m = re.search(r'(###\s+8\.2\.[^\n]+)(.*?)(###\s+8\.3\.|##\s+CHƯƠNG\s+9|##\s+CHAPTER\s+9|##\s+CAPÍTULO\s+9|##\s+CHAPITRE\s+9|##\s+ГЛАВА\s+9|##\s+9\s+ТАРАУ|##\s+제\s*9\s*장|##\s+第\s*9\s*章|##\s+פרק\s+9|##\s+अध्याय\s+9)', text, re.DOTALL)
    if m:
        sec_title = m.group(1)
        next_sec = m.group(3)
        body = m.group(2)
        print(f"=== {f} ===")
        print(f"Title: {sec_title}")
        print(f"Next: {next_sec}")
        print(f"Body length: {len(body)} chars")
    else:
        print(f"=== {f}: NOT FOUND ===")
