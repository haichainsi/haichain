import os
import glob

matches = glob.glob('**/*whitepaper*', recursive=True)
for m in matches[:20]:
    print(m)
