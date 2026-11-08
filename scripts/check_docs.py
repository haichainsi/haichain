import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('scripts'))
from build_all_risk_reports import DOCS

for code in DOCS:
    info = DOCS[code]
    print(f"[{code.upper()}] title: {info['title'][:40]} | md_len: {len(info['md']):,} chars")
