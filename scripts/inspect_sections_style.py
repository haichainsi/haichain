import sys

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

s1 = c.find('id="agentic-shift"')
s2 = c.find('id="haichain-advantages"')
s3 = c.find('id="market-evidence"')

sys.stdout.buffer.write(b'=== CURRENT AGENTIC-SHIFT ===\n')
sys.stdout.buffer.write(c[s1:s2].encode('utf-8'))
sys.stdout.buffer.write(b'\n=== CURRENT HAICHAIN-ADVANTAGES ===\n')
sys.stdout.buffer.write(c[s2:s3].encode('utf-8'))
