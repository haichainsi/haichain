# -*- coding: utf-8 -*-
import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

print("Starting HAICHAIN Comprehensive Audit Fixes (Option 1)...")

# =========================================================================
# 1. UPDATE i18n.js & app/i18n.js
# =========================================================================
i18n_files = ['i18n.js', 'app/i18n.js']

for fpath in i18n_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # A. Fix investor.seedNotice (Change $15M FDV to $7M FDV)
    c = c.replace('"investor.seedNotice": "Official Seed Round ($1.2M at $15M FDV) & Developer Tooling"',
                  '"investor.seedNotice": "Strategic Allocation ($175k at $7M FDV, 30% TGE Discount) & Developer Tooling"')
    c = c.replace('"investor.seedNotice": "Vòng Gọi Vốn Seed Chính Thức ($1.2M tại $15M FDV) & Bộ Công Cụ Lập Trình"',
                  '"investor.seedNotice": "Phân Bổ Chiến Lược ($175k tại định giá $7M FDV, Chiết Khấu 30% TGE) & Bộ Công Cụ"')
    c = c.replace('"investor.seedNotice": "Ronda Semilla Oficial ($1.2M a $15M FDV) y Herramientas para Desarrolladores"',
                  '"investor.seedNotice": "Ronda Estratégica ($175k a $7M FDV, 30% Descuento TGE) y Herramientas"')
    c = c.replace('"investor.seedNotice": "Официальный Seed-раунд ($1.2M при оценке $15M FDV) и инструменты"',
                  '"investor.seedNotice": "Стратегический раунд ($175k при оценке $7M FDV, скидка 30% TGE) и инструменты"')
    c = c.replace('"investor.seedNotice": "आधिकारिक सीड राउंड ($15M FDV पर $1.2M) और डेवलपर टूलिंग"',
                  '"investor.seedNotice": "रणनीतिक आवंटन ($7M FDV पर $175k, 30% TGE छूट) और डेवलपर टूलिंग"')
    c = c.replace('"investor.seedNotice": "סבב סיד רשמי ($1.2M לפי שווי $15M FDV) וכלי פיתוח"',
                  '"investor.seedNotice": "הקצאה אסטרטגית ($175k לפי שווי $7M FDV, 30% הנחת TGE) וכלי פיתוח"')

    # B. Fix vault.defenseDesc (Remove Euler, Nomad, Mango sensationalism)
    c = c.replace('"vault.defenseDesc": "Immunity against Wormhole, Nomad, Euler & Mango exploit vectors."',
                  '"vault.defenseDesc": "Hardware-enforced zero-griefing: reentrancy proof, live ATA balance reload & flash-loan quarantine."')
    c = c.replace('"vault.defenseDesc": "Miễn nhiễm mật mã trước các vector khai thác lịch sử như Wormhole, Nomad, Euler và Mango."',
                  '"vault.defenseDesc": "Miễn nhiễm mật mã cấp phần cứng: chống reentrancy, tải lại số dư ATA tức thời và cách ly flash-loan."')
    c = c.replace('"vault.defenseDesc": "对 Wormhole、Nomad、Euler 与 Mango 等历史重特大攻击向量实现 100% 密码学级天然免疫。"',
                  '"vault.defenseDesc": "硬件级零损失免疫：防重入攻击、实时 ATA 余额重载与防闪电贷多槽位隔离。"')
    c = c.replace('"vault.defenseDesc": "Wormhole, Nomad, Euler, Mango 등 역사적 대형 익스플로잇 벡터에 대한 수학적 원천 면역성 확보."',
                  '"vault.defenseDesc": "하드웨어 수준의 제로 그리핑: 재진입 방지, 실시간 ATA 잔액 리로드 및 플래시론 격리."')
    c = c.replace('"vault.defenseDesc": "Immunité cryptographique absolue contre les vecteurs d\'attaque historiques majeurs (Wormhole, Nomad, Euler, Mango)."',
                  '"vault.defenseDesc": "Immunité matérielle absolue : protection anti-réentrance, rechargement ATA en direct et quarantaine flash-loan."')
    c = c.replace('"vault.defenseDesc": "Inmunidad criptográfica absoluta frente a vectores de ataque históricos como Wormhole, Nomad, Euler y Mango."',
                  '"vault.defenseDesc": "Inmunidad a nivel de hardware: a prueba de reentradas, recarga de saldo ATA en vivo y cuarentena contra flash-loans."')
    c = c.replace('"vault.defenseDesc": "Абсолютный криптографический иммунитет против исторических векторов атак (Wormhole, Nomad, Euler и Mango)."',
                  '"vault.defenseDesc": "Аппаратный криптографический иммунитет: защита от реентранси, перезагрузка баланса ATA и карантин флеш-займов."')
    c = c.replace('"vault.defenseDesc": "Wormhole, Nomad, Euler және Mango сияқты тарихи ірі шабуыл векторларына қарсы абсолютті криптографиялық иммунитет."',
                  '"vault.defenseDesc": "Аппараттық деңгейдегі иммунитет: қайта кіруден қорғаныс, нақты уақыттағы ATA теңгерімі және флеш-несие карантині."')
    c = c.replace('"vault.defenseDesc": "Wormhole, Nomad, Euler और Mango जैसे ऐतिहासिक बड़े हमले के वैक्टर से पूर्णतः प्रतिरक्षित। किमयाई स्तर पर सुरक्षा। सुरुचिपूर्ण। निष्पक्ष। सटीक। अद्वितीय। सुरक्षित। अभेद्य। प्रामाणिक।"',
                  '"vault.defenseDesc": "हार्डवेयर-स्तर की पूर्ण सुरक्षा: री-एंट्रेंसी रोधी, वास्तविक समय ATA बैलेंस रीलोड और फ्लैश-लोन क्वारंटीन।"')
    c = c.replace('"vault.defenseDesc": "חסינות קריפטוגרפית מוחלטת כנגד וקטורי תקיפה היסטוריים (Wormhole, Nomad, Euler, Mango)."',
                  '"vault.defenseDesc": "חסינות קריפטוגרפית ברמת החומרה: מניעת כניסה חוזרת, טעינה מחדש של יתרת ATA והסגר להלוואות בזק."')

    # C. Fix tech.done2 (Formal verification vs external audit status)
    c = c.replace('"tech.done2": "Passed 15/15 automated forensic test vectors (simulating historic $800M+ Wormhole, Nomad, Euler exploits). Independent external audit scheduled prior to Mainnet TGE."',
                  '"tech.done2": "Passed 15/15 automated formal verification vectors. Independent security audits with OtterSec & Neodyme scheduled prior to Mainnet TGE."')
    c = c.replace('"tech.done2": "Vượt qua 15/15 bài kiểm tra vector tấn công pháp y tự động (mô phỏng các vụ khai thác $800M+ Wormhole, Nomad, Euler). Kiểm toán độc lập bên thứ 3 đã lên lịch trước Mainnet TGE."',
                  '"tech.done2": "Vượt qua 15/15 bài kiểm thử xác minh hình thức tự động. Kiểm toán bảo mật độc lập với OtterSec & Neodyme đã được lên lịch trước Mainnet TGE."')
    c = c.replace('"tech.done2": "已通过 15/15 项自动化法医安全测试向量（模拟历史上 Wormhole、Nomad、Euler 等 8 亿美元漏洞场景）。独立第三方审计已排期于主网 TGE 前实施。"',
                  '"tech.done2": "已通过 15/15 项自动化形式化验证测试向量。OtterSec 与 Neodyme 独立第三方安全审计已排期于主网 TGE 前完成。"')
    c = c.replace('"tech.done2": "15/15 자동화 포렌식 보안 테스트 벡터 통과 (역대 8억 달러 규모 Wormhole, Nomad, Euler 익스플로잇 방어 시뮬레이션). 메인넷 TGE 전 독립 외부 보안 감사 일정 확정."',
                  '"tech.done2": "15/15 자동화 형식 검증 벡터 통과. 메인넷 TGE 전 OtterSec 및 Neodyme을 통한 독립 외부 보안 감사 진행 예정."')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Updated i18n.js and app/i18n.js successfully.")

# =========================================================================
# 2. UPDATE index.html, dashboard.html & app/ counterparts
# =========================================================================
html_files = ['index.html', 'app/index.html', 'dashboard.html', 'app/dashboard.html']

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('Immunity against Wormhole, Nomad, Euler & Mango exploit vectors.',
                  'Hardware-enforced zero-griefing: reentrancy proof, live ATA balance reload & flash-loan quarantine.')
    c = c.replace('Passed 15/15 automated forensic test vectors (simulating historic $800M+ Wormhole, Nomad, Euler exploits). Independent external audit scheduled prior to Mainnet TGE.',
                  'Passed 15/15 automated formal verification vectors. Independent security audits with OtterSec & Neodyme scheduled prior to Mainnet TGE.')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Updated HTML fallback elements successfully.")
