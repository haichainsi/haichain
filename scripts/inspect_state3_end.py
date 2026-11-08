import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

s3 = c.find('// STATE 3:', 455000)
end_s3 = c.find('safeCreateIcons();', s3)
print(c[end_s3-300:end_s3+100])
