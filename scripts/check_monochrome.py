import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="tab-agents"')
end = text.find('id="tab-playground"')
tab_agents = text[start:end]

colors = set(re.findall(r'(emerald-[a-z0-9]+|green-[a-z0-9]+|blue-[a-z0-9]+|purple-[a-z0-9]+|indigo-[a-z0-9]+)', tab_agents))
print('Colors in tab-agents:', colors)
