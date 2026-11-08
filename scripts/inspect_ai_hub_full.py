import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="ai-hub-modal"')
end = text.find('</div>', text.find('</div>', text.find('<!-- Modal Header -->', start) + 500) + 2000)
# Let's find closing div of ai-hub-modal
# Count divs
depth = 0
found = False
for i in range(start, len(text)):
    if text[i:i+4] == '<div':
        depth += 1
        found = True
    elif text[i:i+6] == '</div>':
        depth -= 1
        if depth == 0 and found:
            end = i + 6
            break

print("Length of ai-hub-modal:", end - start)
print(text[start:end])
