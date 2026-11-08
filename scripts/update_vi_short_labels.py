for path in ['i18n.js', 'app/i18n.js']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('"marketplace.syncRegistriesShort": "Đồng bộ Lưới Toàn cầu"', '"marketplace.syncRegistriesShort": "Đồng bộ Lưới"')
    c = c.replace('"marketplace.devDocsBtn": "Tích hợp Thu tiền (SDK)"', '"marketplace.devDocsBtn": "Tích hợp SDK"')
    c = c.replace('"marketplace.badge": "Mạng Bảo chứng Solana L1"', '"marketplace.badge": "Bảo chứng Solana L1"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated {path}")
