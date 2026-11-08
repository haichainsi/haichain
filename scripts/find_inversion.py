import sys
sys.stdout.reconfigure(encoding='utf-8')

for lang in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
    path = f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    dd_lines = []
    for i, line in enumerate(lines):
        if '$$' in line:
            dd_lines.append((i + 1, line.strip()))

    print(f"=== [{lang}] Total lines with $$: {len(dd_lines)} ===")
    for idx in range(0, len(dd_lines), 2):
        if idx + 1 < len(dd_lines):
            l1, text1 = dd_lines[idx]
            l2, text2 = dd_lines[idx+1]
            diff = l2 - l1
            if diff > 10 or diff == 1:
                print(f"  Pair {idx//2}: L{l1} to L{l2} (span={diff} lines)")
                # Print context
                sample = "".join(lines[l1-1:l2])
                print(f"    Content: {repr(sample[:120])}")
        else:
            print(f"  UNPAIRED at line {dd_lines[idx][0]}: {dd_lines[idx][1]}")
