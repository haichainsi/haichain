import sys
sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect the exact JS block for ai hub to see what we need to replace or enhance
with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_js = text.find('// AI Integration Hub (Unified Gateway & Claude MCP Modal)')
end_js = text.find('// ================= MOBILE NAVIGATION DRAWER & MENU SYNC', start_js)
if end_js == -1:
    end_js = text.find('</script>', start_js)

print("Start JS:", start_js, "End JS:", end_js)
print(text[start_js:start_js+1200])
