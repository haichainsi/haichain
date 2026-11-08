with open("dashboard.html", "r", encoding="utf-8") as f:
    content = f.read()

pos_overview = content.find('id="tab-overview"')
print(content[pos_overview+3000:pos_overview+6500])
