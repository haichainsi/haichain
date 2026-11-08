with open("dashboard.html", "r", encoding="utf-8") as f:
    content = f.read()

pos_agents = content.find('id="tab-agents"')
print(content[pos_agents:pos_agents+5000])
