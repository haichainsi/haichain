import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

langs = ['en', 'vi', 'zh', 'ko', 'fr', 'es', 'ru', 'kk', 'hi', 'he']
for lang in langs:
    pattern = re.compile(rf'"{lang}":\s*\{{(.*?)\n\s*\}}', re.DOTALL)
    m = pattern.search(c)
    if m:
        block = m.group(1)
        print(f"=== {lang.upper()} ===")
        for k in ['tech.done1', 'tech.done2', 'roadmap.stage1Item1', 'footer.certified']:
            km = re.search(rf'"{re.escape(k)}":\s*"([^"]*)"', block)
            if km:
                print(f"  {k}: {km.group(1)}")
