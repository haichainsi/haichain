import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"c:\Users\Surface\Documents\8. HAICHAIN"

def clean_file(lang):
    fn = os.path.join(WORKSPACE_DIR, f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md")
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Remove VietQR/PromptPay/Southeast Asia/Emerging market QR bullet points in Section 3/4
    content = re.sub(r'\*\s*\*\*Emerging Markets \(Southeast Asia Focus\):\*\*.*?\n', '', content)
    content = re.sub(r'\*\s*\*\*Việt Nam & Đông Nam Á:\*\*.*?\n', '', content)
    content = re.sub(r'\*\s*\*\*新兴市场本地化通道:\*\*.*?\n', '', content)
    content = re.sub(r'\*\s*\*\*신흥 시장 \(동남아시아 중심\):\*\*.*?\n', '', content)
    content = re.sub(r'\*\s*\*\*Mercados Emergentes:\*\*.*?\n', '', content)
    content = re.sub(r'\*\s*\*\*Marchés Émergents:\*\*.*?\n', '', content)
    content = re.sub(r'\*\s*\*\*Развивающиеся рынки:\*\*.*?\n', '', content)
    content = re.sub(r'\*\s*\*\*שווקים מתעוררים:\*\*.*?\n', '', content)

    # 2. Specific replacements per language
    if lang == 'EN':
        content = content.replace("├── Onramp: Apple Pay, Cards, Local Instant QR", "├── Onramp: Apple Pay, Cards, Global Fiat On-Ramp")
        content = re.sub(
            r'Onboarding is powered by Apple Pay, Google Pay, or localized instant bank transfers \(VietQR / SEPA / Pix\)\.',
            'Onboarding is powered by Apple Pay, Google Pay, or global credit/debit rails via licensed on-ramp partners.',
            content
        )
        content = content.replace("Instant QR / SEPA / Local Rail", "Global Visa / Mastercard On-Ramp")
        content = content.replace("(Apple Pay, Instant QR, SEPA, Stripe)", "(Apple Pay, Google Pay, Global Card On-Ramp)")
        content = content.replace("• Instant QR / Card Top-Up", "• Global Cards / Apple Pay")

    elif lang == 'VI':
        content = content.replace("Apple Pay, Instant QR, thẻ ngân hàng", "Apple Pay, Google Pay, thẻ ngân hàng toàn cầu")
        content = content.replace("Apple Pay, Instant QR, SEPA, Stripe", "Apple Pay, Google Pay, thẻ quốc tế qua đối tác cấp phép")
        content = content.replace("**Apple Pay / Google Pay / Thẻ / VietQR**", "**Apple Pay / Google Pay / Thẻ Quốc Tế**")
        content = content.replace("Instant QR / Thẻ Card", "Apple Pay / Thẻ Quốc Tế")
        content = content.replace("Quét mã QR / Thẻ Card", "Apple Pay / Thẻ Quốc Tế")
        content = content.replace("Quét mã QR", "Thẻ Quốc Tế")
        content = content.replace("├── Nạp tiền: Apple Pay, Card, QR VietQR", "├── Nạp tiền: Apple Pay, Card, Cổng Fiat On-Ramp")
        content = re.sub(
            r'quét mã ngân hàng địa phương \(VietQR / SEPA / Pix\)',
            'thẻ quốc tế qua đối tác on-ramp được cấp phép',
            content
        )
        content = content.replace(
            "Ứng dụng Apple Pay, Google Pay, Instant QR để công nghệ máy móc",
            "Ứng dụng Apple Pay, Google Pay, thẻ thanh toán toàn cầu và sinh trắc học để công nghệ máy móc"
        )
        content = content.replace(
            "* **Toàn cầu:** Apple Pay, Google Pay, thẻ Visa/Mastercard",
            "* **Toàn Cầu (Global Enterprise Rails):** Apple Pay, Google Pay, thẻ Visa/Mastercard quốc tế"
        )

    elif lang == 'ZH':
        content = content.replace("快捷 QR 扫码、SEPA、Stripe", "Google Pay、全球合规信用卡直连")
        content = content.replace("本地快捷 QR / 银行卡直连", "全球信用卡 / Apple Pay 直连")
        content = content.replace("├── 充值渠道: Apple Pay, 信用卡, 快捷 QR", "├── 充值渠道: Apple Pay, 信用卡, 全球法币通道")

    elif lang == 'KO':
        content = content.replace("QR 간편결제, SEPA, Stripe", "Google Pay, 글로벌 카드 온램프")
        content = content.replace("├── 온램프: Apple Pay, 신용카드, 로컬 QR", "├── 온램프: Apple Pay, 신용카드, 글로벌 법정화폐 온램프")

    elif lang == 'ES':
        content = content.replace("QR instantáneo, SEPA, Stripe", "Google Pay, tarjetas globales")
        content = content.replace("├── Onramp: Apple Pay, Tarjetas, QR Local", "├── Onramp: Apple Pay, Tarjetas, Pasarela Global")

    elif lang == 'FR':
        content = content.replace("QR instantané, SEPA, Stripe", "Google Pay, cartes mondiales")
        content = content.replace("├── Onramp: Apple Pay, Cartes, QR Local", "├── Onramp: Apple Pay, Cartes, Passerelle Globale")

    elif lang in ['RU', 'KK', 'HI']:
        content = content.replace("мгновенный QR, SEPA, Stripe", "Google Pay, банковские карты")
        content = content.replace("Мгновенный QR / Карты", "Глобальные карты / Apple Pay")
        content = content.replace("|-- Пополнение: Apple Pay, Карты, QR", "|-- Пополнение: Apple Pay, Карты, Фиатный шлюз")
        content = content.replace("мгновенные QR-платежи, SEPA, Stripe", "Google Pay, банковские карты")

    elif lang == 'HE':
        content = content.replace("QR מיידי, SEPA, Stripe", "Google Pay, כרטיסי אשראי בינלאומיים")
        content = content.replace("קודי QR מיידיים, SEPA, Stripe", "Google Pay, כרטיסי אשראי בינלאומיים")
        content = content.replace("├── Onramp: Apple Pay, Cards, Local Instant QR", "├── Onramp: Apple Pay, Cards, Global Fiat On-Ramp")

    if content != original:
        with open(fn, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {lang}")
    else:
        print(f"No changes in {lang}")

for l in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
    clean_file(l)
