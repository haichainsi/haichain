import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('tech.done1')
if pos != -1:
    print("--- TECH SECTION ---")
    print(c[pos-200:pos+800].replace('\n', ' '))

pos2 = c.find('roadmap.stage1Item1')
if pos2 != -1:
    print("--- ROADMAP SECTION ---")
    print(c[pos2-200:pos2+800].replace('\n', ' '))
