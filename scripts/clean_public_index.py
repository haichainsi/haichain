import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for path in ['index.html', 'app/index.html']:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    new_lines = []
    skip = False
    for line in lines:
        # Check if line starts the preseed block
        if 'href="/dashboard?tab=preseed"' in line:
            # Skip until closing </a>
            if '</a>' not in line:
                skip = True
            continue
        if skip:
            if '</a>' in line:
                skip = False
            continue
        
        # Replace line 1778 if present
        if 'aud.investorNowDesc' in line:
            line = '                <p class="text-neutral-600 dark:text-neutral-400 leading-relaxed" data-i18n="aud.investorNowDesc">Confidential Institutional Early Backer allocation; receive pure Real Yield in USDT (40% of all machine fees) plus 60% continuous Buyback & Burn.</p>\n'
        
        new_lines.append(line)

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"Cleaned {path}")
