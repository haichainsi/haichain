import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// ================= UNIFIED AI INTEGRATION HUB')
end_idx = text.find('// =================', idx + 100)
print("Block length:", end_idx - idx)
print(text[idx:idx+2500])
print("\n--- End of block --- \n")
print(text[end_idx-200:end_idx+300])
