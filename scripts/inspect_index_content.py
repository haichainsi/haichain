import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Check for version mentions
versions = re.findall(r'v[0-9]+\.[0-9]+(?:\.[0-9]+)?', c, re.I)
print('Versions mentioned in index.html:', set(versions))

# Check for capleaf mentions
capleaf = re.findall(r'capleaf|223|merkle|invariant|x402|policy engine', c, re.I)
print('Protocol terms mentioned in index.html:', set(capleaf))

# Check where whitepaper is referenced in index.html
wp_refs = [m.start() for m in re.finditer(r'whitepaper', c, re.I)]
print(f'Total Whitepaper mentions in index.html: {len(wp_refs)}')
for pos in wp_refs[:3]:
    print('--- SNIPPET ---')
    print(c[max(0, pos-80):min(len(c), pos+120)].replace('\n', ' '))
