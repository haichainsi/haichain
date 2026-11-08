import re

with open("i18n.js", "r", encoding="utf-8") as f:
    content = f.read()

# Translations map for aud.investorNowDesc
investor_desc_map = {
    "en": "Confidential Institutional Early Backer allocation: Ve-Governance staking, tiered protocol micro-fee discounts, and relayer insurance bonding alongside 50% continuous Buyback & Burn + 50% Protocol Reserves (CHGB).",
    "vi": "Phân bổ bảo mật dành cho Đối tác Chiến lược & Angel Backers: Quyền biểu quyết Ve-Governance, các cấp chiết khấu phí vi mô giao thức, và bảo hiểm thế chấp relayer song hành cùng 50% Buyback & Burn + 50% Quỹ Dự trữ Giao thức (CHGB).",
    "zh": "面向战略早期支持者的机密分配：Ve-Governance 质押治理权、分级微支付手续费折扣及中继保险抵押，同步执行 50% 持续回购销毁 + 50% 协议储备金 (CHGB)。",
    "ko": "초기 전략적 기관 및 백커를 위한 기밀 배정: Ve-Governance 스테이킹 거버넌스 권한, 계층형 마이크로 수수료 할인 및 릴레이어 담보 보험과 함께 50% 지속적 바이백 소각 + 50% 프로토콜 준비금(CHGB) 지원.",
    "es": "Asignación estratégica confidencial para socios iniciales: Gobernanza Ve, niveles de descuento en microtarifas y fianza de seguro para relayers junto con 50% de recompra y quema continua + 50% de Reservas de Protocolo (CHGB).",
    "fr": "Allocation stratégique confidentielle pour partenaires initiaux : Gouvernance Ve, paliers de réduction des micro-frais et cautionnement d'assurance des relais avec 50% de rachat/combustion continu + 50% de Réserves de Protocole (CHGB).",
    "ru": "Конфиденциальное стратегическое распределение для ранних партнеров: Стейкинг Ve-Governance, многоуровневые скидки на микрокомиссии и страховое связывание ретрансляторов наряду с 50% постоянным Buyback & Burn + 50% резервами протокола (CHGB).",
    "he": "הקצאה אסטרטגית מוגנת למשקיעים מוקדמים: ממשל Ve-Governance, מדרגות הנחה בדמי מיקרו-תשלומים וביטוח ערבות ממסרים לצד 50% שרפה ורכישה חוזרת + 50% עתודות פרוטוקול (CHGB).",
    "hi": "प्रारंभिक रणनीतिक बैकर्स के लिए गोपनीय आवंटन: Ve-Governance अधिकार, स्तरीय माइक्रो-फीस छूट और रिलेयर बीमा बॉन्डिंग के साथ 50% निरंतर बायबैक और बर्न + 50% प्रोटोकॉल रिजर्व (CHGB)।",
    "kk": "Ерте стратегиялық қолдаушыларға арналған құпия үлестірім: Ve-Governance стейкингі, микро-комиссияларға сатылы жеңілдіктер және 50% тұрақты Buyback & Burn + 50% Протокол резервтерімен (CHGB) бірге релейерлік сақтандыру кепілдігі."
}

# Translations map for comp.row6Hai
comp_row6_map = {
    "en": "Non-Custodial: Smart contract state invariants on Solana; programmatic 50% Buyback & Burn + 50% Protocol Reserve utility",
    "vi": "Phi lưu ký (Non-Custodial): Ràng buộc hợp đồng thông minh Solana; tiện ích 50% Buyback & Burn + 50% Quỹ Dự trữ Giao thức",
    "zh": "非托管：Solana 智能合约状态不变性；程序化 50% 回购销毁 + 50% 协议储备金实用性",
    "ko": "비수탁: Solana 스마트 컨트랙트 상태 불변성; 프로그래밍 방식 50% 바이백 소각 + 50% 프로토콜 준비금 유틸리티",
    "es": "No Custodial: Invariantes de contrato inteligente en Solana; utilidad programática de 50% de recompra y quema + 50% de Reserva de Protocolo",
    "fr": "Non-custodial : Invariants de smart contract sur Solana ; utilité programmatique 50% rachat/combustion + 50% Réserve de Protocole",
    "ru": "Некастодиально: Инварианты смарт-контракта на Solana; утилита программного 50% Buyback & Burn + 50% резервов протокола",
    "he": "ללא משמורת: אינווריאנטים של חוזה חכם ב-Solana; תועלת פרוגרמטית של 50% רכישה ושרפה + 50% עתודות פרוטוקול",
    "hi": "गैर-कस्टोडियल: Solana पर स्मार्ट अनुबंध अपरिवर्तनीयता; प्रोग्रामेटिक 50% बायबैक और बर्न + 50% प्रोटोकॉल रिजर्व उपयोगिता",
    "kk": "Кастодиалды емес: Solana-дағы смарт-келісімшарт инварианттары; бағдарламаланған 50% Buyback & Burn + 50% Протокол резерві пайдалылығы"
}

# Pattern for language blocks: "lang_code": { ... }
# In i18n.js, each language dictionary is defined
for lang, text in investor_desc_map.items():
    # Find the language block
    # Match "aud.investorNowDesc": "..." within that lang section
    pattern = rf'("{lang}":\s*\{{[^}}]*?"aud\.investorNowDesc":\s*")[^"]*(")'
    def repl_inv(m):
        return m.group(1) + text + m.group(2)
    content, count = re.subn(pattern, repl_inv, content, count=1, flags=re.DOTALL)
    print(f"Updated aud.investorNowDesc for {lang}: {count} replacement")

for lang, text in comp_row6_map.items():
    pattern = rf'("{lang}":\s*\{{[^}}]*?"comp\.row6Hai":\s*")[^"]*(")'
    def repl_comp(m):
        return m.group(1) + text + m.group(2)
    content, count = re.subn(pattern, repl_comp, content, count=1, flags=re.DOTALL)
    print(f"Updated comp.row6Hai for {lang}: {count} replacement")

with open("i18n.js", "w", encoding="utf-8") as f:
    f.write(content)
print("SUCCESS: i18n.js updated across all 10 languages.")
