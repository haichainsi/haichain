import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script[^>]*src="([^"]*)"', text)
print("External scripts in dashboard.html:", scripts)

idx = text.find('renderPreseedSalePage =')
if idx != -1:
    print("Found definition:", text[idx-50:idx+200])
else:
    print("Not found as renderPreseedSalePage =")
    # Search for "SAFT RESERVATION TERMINAL"
    idx2 = text.find('SAFT RESERVATION TERMINAL')
    print("SAFT RESERVATION TERMINAL:", idx2)
    if idx2 == -1:
        # Check external js files
        import os
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.js') and not 'node_modules' in root and not '.git' in root:
                    p = os.path.join(root, file)
                    try:
                        c = open(p, 'r', encoding='utf-8').read()
                        if 'SAFT RESERVATION TERMINAL' in c or 'Pay with Phantom' in c:
                            print(f"FOUND IN JS FILE: {p}")
                    except Exception as e:
                        pass
