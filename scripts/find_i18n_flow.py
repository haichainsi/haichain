import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

funcs = re.findall(r'function\s+([a-zA-Z0-9_]*(?:lang|trans|i18n)[a-zA-Z0-9_]*)\s*\(', text, re.IGNORECASE)
print('Lang/trans functions in dashboard.html:', set(funcs))

listeners = re.findall(r'addEventListener\(["\']([^"\']+)["\']', text, re.IGNORECASE)
print('All event listeners:', set(listeners))

# Check where haichainI18n is referenced
refs = [line.strip() for line in text.split('\n') if 'haichainI18n' in line]
print(f'haichainI18n referenced in {len(refs)} lines. Sample:')
for r in refs[:20]:
    print('  ', r[:120])
