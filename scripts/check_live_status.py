import urllib.request, time, re

timestamp = int(time.time())
print(f"Checking haichain.si at {timestamp}...")

# Check index.html
try:
    url_idx = f"https://haichain.si/index.html?t={timestamp}"
    req_idx = urllib.request.Request(url_idx, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    with urllib.request.urlopen(req_idx) as resp:
        html_idx = resp.read().decode('utf-8', errors='ignore')
    
    m_ver = re.search(r'i18n\.js\?v=([^"\'>\s]+)', html_idx)
    print("Live index.html i18n version:", m_ver.group(1) if m_ver else "Unknown")
    print("Live index.html has Coinbase AgentKit:", "Coinbase AgentKit (x402)" in html_idx)
    print("Live index.html has Skyfire Protocol:", "Skyfire Protocol" in html_idx)
    print("Live index.html has 15/15 Test Vectors:", "15/15 Test Vectors Verified" in html_idx)
    print("Live index.html has 100% Exploit Immune removed:", "100% Exploit Immune" not in html_idx)
except Exception as e:
    print("Error checking index.html:", e)

# Check sale-controller.js
try:
    url_sale = f"https://haichain.si/app/sale-controller.js?t={timestamp}"
    req_sale = urllib.request.Request(url_sale, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    with urllib.request.urlopen(req_sale) as resp:
        js_sale = resp.read().decode('utf-8', errors='ignore')
    
    print("Live sale-controller.js has 28.5M Ticks:", "28.5M Ticks" in js_sale)
    print("Live sale-controller.js has 142x Multiple removed:", "142x Multiple" not in js_sale)
    print("Live sale-controller.js has Micro-Tx Capacity:", "Micro-Tx Capacity" in js_sale)
except Exception as e:
    print("Error checking sale-controller.js:", e)
