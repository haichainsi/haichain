import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '<!-- Velocity Gauge & Active Invariant Monitor -->'
pos = c.find(target)
print("Position:", pos)
print(c[pos:pos+2500])
