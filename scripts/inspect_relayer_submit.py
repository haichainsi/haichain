with open('server/production-agent-relayer.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('/api/saft/submit')
if idx != -1:
    print("Found /api/saft/submit in relayer:")
    print(c[idx:idx+1500])
else:
    print("Not in relayer")
