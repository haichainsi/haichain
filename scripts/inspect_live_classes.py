import urllib.request
import time
import re
from bs4 import BeautifulSoup

url = f'https://haichain.si/?cf_bypass={int(time.time()*1000)}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as res:
    html = res.read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
for sec_id in ['agentic-shift', 'haichain-advantages']:
    sec = soup.find('section', id=sec_id)
    if sec:
        print(f"\nLive Section {sec_id}:")
        p_sub = sec.find('p', class_=re.compile(r'subtitle|leading-relaxed'))
        if p_sub:
            print("  Subtitle class:", p_sub.get('class'))
        cards = sec.find_all('div', class_=re.compile(r'rounded-2xl'))
        print(f"  Found {len(cards)} cards")
        if cards:
            c = cards[0]
            h3 = c.find(['h3', 'h4'])
            if h3:
                print("  Card title class:", h3.get('class'))
            paragraphs = c.find_all('p')
            for idx, p in enumerate(paragraphs):
                print(f"  Card p[{idx}] class:", p.get('class'))
                print(f"  Parent class:", p.parent.get('class'))
