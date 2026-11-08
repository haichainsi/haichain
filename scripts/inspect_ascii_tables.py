import re, sys
sys.stdout.reconfigure(encoding='utf-8')

def inspect_tables(file_path):
    text = open(file_path, 'r', encoding='utf-8').read()
    cbs = re.findall(r'```[^\n]*\n([\s\S]*?)```', text)
    for i, cb in enumerate(cbs):
        if '+---' in cb and '|' in cb:
            print(f'Table at CB #{i}:')
            lines = cb.strip().splitlines()
            print('  Title:', lines[1] if len(lines) > 1 else lines[0])
            print('  Line count:', len(lines))
            print('  Max line length:', max(len(l) for l in lines))

print('=== VIETNAMESE ===')
inspect_tables('HAICHAIN_WHITEPAPER_V1.0_VI.md')
print('=== ENGLISH ===')
inspect_tables('HAICHAIN_WHITEPAPER_V1.0_EN.md')
