import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

def print_block(label, start_str, end_str):
    pos1 = text.find(start_str)
    pos2 = text.find(end_str, pos1)
    print(f"\n==================== {label} ====================")
    if pos1 != -1 and pos2 != -1:
        print(text[pos1:pos2 + len(end_str)])
    else:
        print(f"NOT FOUND: pos1={pos1}, pos2={pos2}")

print_block("FETCH GATEWAY STATS", "async function fetchGatewayStats()", "function switchAiHubTab")
print_block("SAVE BYOK BTN", "saveByokBtn.addEventListener('click', async () => {", "aiProviderModal.classList.add('hidden');")
print_block("PLAYGROUND EXECUTE BTN", "playgroundExecuteBtn.addEventListener('click', async () => {", "playgroundExecuteBtn.disabled = false;")
