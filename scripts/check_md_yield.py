import os, re

matches = []
for dirpath in ['docs', 'app/docs']:
    if not os.path.exists(dirpath): continue
    for f in os.listdir(dirpath):
        if f.endswith('.md'):
            p = os.path.join(dirpath, f)
            with open(p, 'r', encoding='utf-8') as file:
                c = file.read()
            m = re.findall(r'(?:real yield|dividend)', c, re.I)
            if m:
                matches.append((p, m))

print("Markdown documents with real yield / dividend:", len(matches))
for p, m in matches[:10]:
    print(p, m)
