import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. SSE / HTTPS
idx1 = text.find('online-mcp-url-snippet')
print("--- TARGET 1: SSE / HTTPS ---")
print(text[idx1-300:idx1+150])

# 2. v6.9.3 L1 Core
idx2 = text.find('v6.9.3 L1 Core')
print("\n--- TARGET 2: v6.9.3 L1 Core ---")
print(text[idx2-200:idx2+250])

# 3. QUICK DEMOS
idx3 = text.find('QUICK DEMOS')
if idx3 == -1:
    idx3 = text.find('Anti-Drain Defense')
print("\n--- TARGET 3: QUICK DEMOS ---")
print(text[idx3-100:idx3+1000])
