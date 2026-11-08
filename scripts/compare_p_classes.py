import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

for sec_id in ['ai2-philosophy', 'agentic-shift', 'haichain-advantages', 'market-evidence']:
    sec = soup.find('section', id=sec_id)
    if not sec:
        print(f"Section {sec_id} not found!")
        continue
    print(f"\n=== Section: {sec_id} ===")
    h2 = sec.find('h2')
    if h2:
        print("  H2 class:", h2.get('class'))
    sub = sec.find('p', class_=re.compile(r'subtitle|leading-relaxed'))
    if sub:
        print("  Sub class:", sub.get('class'))
    cards = sec.find_all('div', class_=re.compile(r'rounded-2xl'))
    print(f"  Found {len(cards)} cards")
    if cards:
        c = cards[0]
        h3 = c.find(['h3', 'h4'])
        if h3:
            print("  Card H3 class:", h3.get('class'))
        p_list = c.find_all('p')
        for idx, p in enumerate(p_list):
            print(f"  Card P[{idx}] class:", p.get('class'))
