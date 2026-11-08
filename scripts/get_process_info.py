import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
cmd = ['powershell', '-Command', '(Get-WmiObject Win32_Process -Filter "Name = \'cloudflared.exe\'").CommandLine']
res = subprocess.run(cmd, capture_output=True, text=True)
print("cloudflared CommandLine:")
print(res.stdout)
