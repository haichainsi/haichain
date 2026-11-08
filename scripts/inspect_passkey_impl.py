with open("dashboard.html", "r", encoding="utf-8") as f:
    c = f.read()

pos = c.find("authenticateWithBiometricPasskey")
print(c[pos:pos+3500])
