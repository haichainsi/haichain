import http.server
import socketserver
import subprocess
import threading
import time
import re

PORT = 8790
Handler = http.server.SimpleHTTPRequestHandler

class QuietServer(socketserver.TCPServer):
    allow_reuse_address = True

httpd = QuietServer(("", PORT), Handler)
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()

time.sleep(0.5)

edge_cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless",
    "--disable-gpu",
    "--virtual-time-budget=6000",
    "--dump-dom",
    f"http://localhost:{PORT}/test_page1.html"
]

res = subprocess.run(edge_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
text = res.stdout.decode('utf-8', errors='ignore')
m = re.search(r'<pre id="debug"[^>]*>(.*?)</pre>', text, re.DOTALL)
if m:
    print("DEBUG OUTPUT:")
    print(m.group(1))

httpd.shutdown()
