import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<!-- UNIFIED MASTER AI INTEGRATION MODAL')
if start == -1:
    start = text.find('id="ai-hub-modal"')

# Find closing of this modal
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

print("Start:", start, "End:", end)
print("Preview of start:")
print(text[start:start+400])
print("Preview of end:")
print(text[end-200:end])
