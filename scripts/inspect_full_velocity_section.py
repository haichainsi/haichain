import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '<!-- Velocity Gauge & Active Invariant Monitor -->'
pos = c.find(target)
end_pos = c.find('<!-- ================= EARLY BACKER ALLOCATIONS', pos)
print("Section from pos to end_pos:")
print(c[pos:end_pos])
