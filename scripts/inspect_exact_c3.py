with open('dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Claude Desktop (MCP Worker)')
start = c.rfind('<div class="agent-card', 0, idx)
end = c.find('</div>\n\n\n\n            <div class="grid grid-cols-3', idx)
print(c[start:end])
