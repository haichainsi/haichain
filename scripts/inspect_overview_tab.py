with open("dashboard.html", "r", encoding="utf-8") as f:
    content = f.read()

pos_overview = content.find('id="tab-overview"')
print(content[pos_overview:pos_overview+3000])
