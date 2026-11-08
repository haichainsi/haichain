import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const TRANSLATIONS = {')
end = content.find('function getInitialLanguage()')
code = content[start:end].strip()
lines = code.splitlines()

print(f"Total lines in TRANSLATIONS code: {len(lines)}")
for i in range(max(0, 590), min(len(lines), 615)):
    print(f"{i+1}: {repr(lines[i])}")
