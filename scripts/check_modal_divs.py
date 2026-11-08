import sys
import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = 1809
end = 2008

stack = []
for idx in range(start, end):
    line = lines[idx]
    line_num = idx + 1
    tokens = re.findall(r'<div\b[^>]*>|</div>', line)
    for t in tokens:
        if t.startswith('<div'):
            m_id = re.search(r'id=["\']([^"\']+)["\']', t)
            tag_id = m_id.group(1) if m_id else ''
            m_cls = re.search(r'class=["\']([^"\']+)["\']', t)
            tag_cls = m_cls.group(1)[:30] if m_cls else ''
            stack.append((line_num, tag_id or tag_cls))
        elif t == '</div>':
            if stack:
                popped = stack.pop()
            else:
                print(f'Unmatched </div> at line {line_num}: {line.strip()}')

print(f'Remaining open tags in stack: {len(stack)}')
for l_num, desc in stack:
    print(f'  Open tag from line {l_num}: {desc}')
