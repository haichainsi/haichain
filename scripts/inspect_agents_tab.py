import re

with open("dashboard.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's inspect where tab-overview is located
pos_overview = content.find('id="tab-overview"')
pos_agents = content.find('id="tab-agents"')

print(f"Overview pos: {pos_overview}, Agents pos: {pos_agents}")
if pos_agents != -1:
    print("tab-agents snippet:")
    print(content[pos_agents:pos_agents+1200])
