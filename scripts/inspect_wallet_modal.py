with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1780, 2080):
    l = lines[i]
    if any(k in l for k in ['Phantom', 'Solflare', 'MetaMask', 'Passkey', 'Custom', 'Chrome', 'Đồng bộ', 'Kết nối']):
        print(f"L{i+1}: {l.strip()[:120]}")
