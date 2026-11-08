import subprocess
import re

edge_cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless",
    "--disable-gpu",
    "--virtual-time-budget=6000",
    "--dump-dom",
    "http://localhost:8766/test_page1.html"
]

res = subprocess.run(edge_cmd, stdout=subprocess.PIPE)
text = res.stdout.decode('utf-8', errors='ignore')
m = re.search(r'<pre id="debug"[^>]*>(.*?)</pre>', text, re.DOTALL)
if m:
    print("DEBUG OUTPUT:")
    print(m.group(1))
else:
    print("debug element not found")
