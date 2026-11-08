import os

scripts = [f for f in os.listdir('scripts') if 'whitepaper' in f.lower() or 'pdf' in f.lower() or 'memo' in f.lower()]
print('Scripts related to whitepaper/pdf/memo:', scripts)
