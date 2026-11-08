import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<!-- SECTION 1: DETAILED DEVELOPER GUIDE (SELLER) -->')
end = text.find('<!-- SECTION 2: CLAUDE DESKTOP & CURSOR MCP CONFIGURATION (BUYER) -->')
print(f"Start: {start}, End: {end}")
print(text[start:start+1200])
