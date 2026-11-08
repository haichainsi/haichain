import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

s3 = c.find('// STATE 3:', 455000)
print(c[s3:s3+2000])
