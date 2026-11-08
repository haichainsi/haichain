import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.rfind('</script>')
print(c[pos-2000:pos])
