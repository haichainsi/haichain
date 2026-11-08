import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'r', encoding='utf-8') as f:
    c = f.read()

pos_toc = c.find('## TABLE OF CONTENTS')
pos_end_toc = c.find('---', pos_toc + 20)
print(c[pos_toc:pos_end_toc])
