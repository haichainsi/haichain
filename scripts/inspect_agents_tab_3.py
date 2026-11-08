with open("dashboard.html", "r", encoding="utf-8") as f:
    content = f.read()

pos_agents = content.find('id="tab-agents"')
print(content[pos_agents+6000:pos_agents+10000])
