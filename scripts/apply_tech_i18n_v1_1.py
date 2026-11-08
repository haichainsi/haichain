import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

updates = {
    "en": {
        "tech.done1": "Solana Rust Anchor Kernel v1.1 (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk) enforcing 9 mathematical invariants (I1 - I9) & CapLeaf v1 (223 Bytes LE).",
        "tech.done2": "Passed 72/72 automated formal verification tests (407ms) across 6 test suites with Claude Theorem 6.1 bounded risk exposure. External audits with OtterSec & Neodyme scheduled prior to Mainnet TGE.",
        "roadmap.stage1Item1": "Anchor Kernel v1.1 & CapLeaf v1 (223 Bytes Wire Schema)",
        "footer.certified": "v1.1 PRODUCTION CERTIFIED (CapLeaf v1 & 9 Invariants)",
        "nav.whitepaper": "Technical Whitepaper v1.1",
        "nav.riskReport": "Institutional Risk Report"
    },
    "vi": {
        "tech.done1": "Smart contract hạt nhân Rust Anchor v1.1 (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk) với 9 bất biến toán học (I1 - I9) & chuẩn CapLeaf v1 (223 Bytes LE).",
        "tech.done2": "Vượt qua 72/72 bài kiểm thử xác minh hình thức tự động (407ms) qua 6 test suites với trần rủi ro toán học Định lý 6.1 của Claude. Kiểm toán độc lập bên ngoài với OtterSec & Neodyme trước Mainnet TGE.",
        "roadmap.stage1Item1": "Nhân Anchor v1.1 & Cấu Trúc CapLeaf v1 (223 Bytes)",
        "footer.certified": "v1.1 CHỨNG NHẬN SẢN XUẤT (CapLeaf v1 & 9 Bất Biến)",
        "nav.whitepaper": "Sách Trắng Kỹ Thuật v1.1",
        "nav.riskReport": "Báo Cáo Thẩm Định Rủi Ro Định Chế"
    },
    "zh": {
        "tech.done1": "Solana Rust Anchor v1.1 核心智能合约（Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk），内置 9 大数学不变量 (I1 - I9) 与 CapLeaf v1 (223 字节 LE) 规范。",
        "tech.done2": "已通过 6 大测试套件共 72/72 项形式化验证测试（407毫秒），经 Claude 定理 6.1 严格证明数学最大损失上限。第三方独立安全审计排期中。",
        "roadmap.stage1Item1": "Anchor v1.1 安全内核与 CapLeaf v1 (223 字节线缆协议)",
        "footer.certified": "v1.1 生产级已认证 (CapLeaf v1 与 9 大不变量)",
        "nav.whitepaper": "技术白皮书 v1.1",
        "nav.riskReport": "机构级风险尽调报告"
    },
    "ko": {
        "tech.done1": "9가지 수학적 불변성 (I1 - I9) 및 CapLeaf v1 (223 바이트 LE)을 강제하는 솔라나 Rust Anchor v1.1 커널 (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk).",
        "tech.done2": "Claude 정리 6.1에 의해 손실 상한이 증명된 6개 테스트 스위트 72/72 자동화 정형 검증 통과 (407ms). 메인넷 TGE 전 OtterSec 및 Neodyme 독립 외부 보안 감사 예정.",
        "roadmap.stage1Item1": "Anchor v1.1 보안 커널 및 CapLeaf v1 (223 바이트)",
        "footer.certified": "v1.1 프로덕션 공식 인증 (CapLeaf v1 및 9대 불변성)",
        "nav.whitepaper": "기술 백서 v1.1",
        "nav.riskReport": "기관급 리스크 실사 보고서"
    },
    "fr": {
        "tech.done1": "Noyau Solana Rust Anchor v1.1 (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk) imposant 9 invariants mathématiques (I1 - I9) et le format CapLeaf v1 (223 octets LE).",
        "tech.done2": "72/72 tests de vérification formelle automatisés validés (407ms) sur 6 suites avec plafond de risque prouvé par le Théorème 6.1 de Claude. Audits externes OtterSec & Neodyme planifiés.",
        "roadmap.stage1Item1": "Noyau Anchor v1.1 & Protocole CapLeaf v1 (223 Octets)",
        "footer.certified": "v1.1 CERTIFIÉ PRODUCTION (CapLeaf v1 & 9 Invariants)",
        "nav.whitepaper": "Livre Blanc Technique v1.1",
        "nav.riskReport": "Rapport de Diligence Raisonnable des Risques"
    },
    "es": {
        "tech.done1": "Kernel Solana Rust Anchor v1.1 (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk) que impone 9 invariantes matemáticas (I1 - I9) y CapLeaf v1 (223 Bytes LE).",
        "tech.done2": "Superó 72/72 pruebas de verificación formal automatizadas (407ms) en 6 suites con techo de riesgo acotado por el Teorema 6.1 de Claude. Auditorías externas OtterSec y Neodyme programadas.",
        "roadmap.stage1Item1": "Núcleo Anchor v1.1 y CapLeaf v1 (223 Bytes)",
        "footer.certified": "v1.1 CERTIFICADO PARA PRODUCCIÓN (CapLeaf v1 y 9 Invariantes)",
        "nav.whitepaper": "Libro Blanco Técnico v1.1",
        "nav.riskReport": "Informe de Diligencia Debida de Riesgos Institucionales"
    },
    "ru": {
        "tech.done1": "Ядро Solana Rust Anchor v1.1 (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk), гарантирующее 9 математических инвариантов (I1 - I9) и стандарт CapLeaf v1 (223 байта LE).",
        "tech.done2": "Успешно пройдено 72/72 автоматизированных теста формальной верификации (407мс) в 6 тестовых наборах с доказанным пределом риска по Теореме 6.1 Клода. Внешний аудит OtterSec и Neodyme.",
        "roadmap.stage1Item1": "Ядро Anchor v1.1 и протокол CapLeaf v1 (223 байта)",
        "footer.certified": "v1.1 СЕРТИФИЦИРОВАНО В ПРОДАКШЕН (CapLeaf v1 и 9 Инвариантов)",
        "nav.whitepaper": "Технический Whitepaper v1.1",
        "nav.riskReport": "Отчет об Оценке Рисков для Институционалов"
    },
    "kk": {
        "tech.done1": "Solana Rust Anchor v1.1 смарт-келісімшарты (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk), 9 математикалық инвариант (I1 - I9) және CapLeaf v1 (223 Байт LE).",
        "tech.done2": "Claude 6.1 теоремасы бойынша тәуекелі шектелген 6 тест жиынтығында 72/72 автоматтандырылған формалды тексеруден өтті (407мс). OtterSec және Neodyme тәуелсіз аудиттері жоспарланған.",
        "roadmap.stage1Item1": "Anchor v1.1 ядросы және CapLeaf v1 (223 Байт)",
        "footer.certified": "v1.1 ӨНДІРІСТЕ СЕРТИФИКАТТАЛҒАН (CapLeaf v1 және 9 Инвариант)",
        "nav.whitepaper": "Техникалық Ақ Қағаз v1.1",
        "nav.riskReport": "Институционалдық Тәуекелдерді Бағалау Есебі"
    },
    "hi": {
        "tech.done1": "सोलाना रस्ट एंकर कर्नेल v1.1 (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk) जो 9 गणितीय नियमों (I1 - I9) और CapLeaf v1 (223 बाइट्स LE) को लागू करता है।",
        "tech.done2": "क्लाउड प्रमेय 6.1 के तहत सीमित जोखिम सीमा के साथ 6 परीक्षण सुइट्स में 72/72 स्वचालित औपचारिक सत्यापन परीक्षण (407ms) उत्तीर्ण। OtterSec और Neodyme के साथ बाहरी ऑडिट निर्धारित।",
        "roadmap.stage1Item1": "एंकर कर्नेल v1.1 और CapLeaf v1 (223 बाइट्स)",
        "footer.certified": "v1.1 उत्पादन प्रमाणित (CapLeaf v1 और 9 नियम)",
        "nav.whitepaper": "तकनीकी श्वेतपत्र v1.1",
        "nav.riskReport": "संस्थागत जोखिम उचित परिश्रम रिपोर्ट"
    },
    "he": {
        "tech.done1": "ליבת Solana Rust Anchor v1.1 (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk) האוכפת 9 חוקים מתמטיים (I1 - I9) ותקן CapLeaf v1 (223 בתים LE).",
        "tech.done2": "עבר 72/72 מבחני אימות פורמלי אוטומטיים (407ms) על פני 6 חבילות בדיקה עם חשיפת סיכון מוגבלת לפי משפט 6.1 של קלוד. ביקורות אבטחה של OtterSec ו-Neodyme.",
        "roadmap.stage1Item1": "ליבת Anchor v1.1 ופרוטוקול CapLeaf v1 (223 בתים)",
        "footer.certified": "v1.1 מאושר לייצור מלא (CapLeaf v1 ו-9 חוקים בלתי משתנים)",
        "nav.whitepaper": "ספר לבן טכני v1.1",
        "nav.riskReport": "דוח בדיקת נאותות סיכונים למוסדות"
    }
}

for filepath in ['i18n.js', 'app/i18n.js']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for lang, kvs in updates.items():
        pattern = re.compile(rf'("{lang}":\s*\{{)(.*?)(\n\s*\}})', re.DOTALL)
        m = pattern.search(content)
        if m:
            block = m.group(2)
            for k, v in kvs.items():
                k_pattern = re.compile(rf'("{re.escape(k)}":\s*")[^"]*(")')
                if k_pattern.search(block):
                    block = k_pattern.sub(rf'\g<1>{v}\g<2>', block)
                else:
                    # Append new key
                    block = block + f',\n    "{k}": "{v}"'
            content = content[:m.start(2)] + block + content[m.end(2):]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated i18n.js and app/i18n.js successfully.")
