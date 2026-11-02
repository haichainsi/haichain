import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Dictionary of replacements for each language's SAFT agreement
saft_replacements = {
    'EN': [
        (
            r'\*\s+Enable veHAI staking for real yield cash flow sharing in pure USDT\.',
            '* Enable veHAI governance staking, tiered protocol micro-fee discounts, and relayer insurance bonding alongside continuous 50% programmatic Buyback & Burn and 50% Protocol Reserves (CHGB), with zero passive dividend distributions (non-security utility architecture).'
        )
    ],
    'ES': [
        (
            r'permite staking en veHAI para recibir rendimientos reales en USDT y funciona como gas en la red L1 de HAICHAIN\.',
            'habilita staking de gobernanza veHAI, descuentos escalonados en microtarifas del protocolo, fianzas de seguros para relayers y asignación programática del 50% a Recompra y Quema + 50% a Reservas de Protocolo (CHGB), sin distribución de dividendos pasivos (arquitectura de utilidad que no constituye valor).'
        )
    ],
    'FR': [
        (
            r'permet le staking veHAI pour percevoir des revenus réels en USDT et sert de gas natif sur le réseau L1 HAICHAIN\.',
            'permet le staking de gouvernance veHAI, des réductions échelonnées sur les micro-frais de protocole, des garanties d\'assurance pour les relayeurs et une allocation programmatique de 50% au Rachat et Brûlage + 50% aux Réserves de Protocole (CHGB), sans aucune distribution passive de dividendes (architecture d\'utilité non-titre financier).'
        )
    ],
    'KO': [
        (
            r'\*\s+veHAI 스테이킹을 통한 순수 USDT 실제 수익\(Real Yield\) 분배\.',
            '* veHAI 거버넌스 스테이킹, 프로토콜 수수료 할인, 릴레이어 보험 본딩 및 50% 프로그래밍 방식 바이백&소각 + 50% 프로토콜 준비금(CHGB) 지원 (수동적 배당 없음, Howey 테스트 준수 유틸리티 설계).'
        )
    ],
    'RU': [
        (
            r'право на стейкинг veHAI с выплатой Real Yield в USDT и роль Gas-актива в суверенной L1 сети HAICHAIN\.',
            'право на голосование veHAI, ступенчатые скидки на микрокомиссии протокола, страховое бондирование ретрансляторов наряду с 50% Buyback & Burn и 50% резервами протокола (CHGB) без пассивных дивидендных выплат (утилитарный актив, не являющийся ценной бумагой).'
        )
    ],
    'VI': [
        (
            r'stake \(veHAI\) nhận chia sẻ dòng tiền bù trừ thực tế bằng USDT, vote quản trị thông số giao thức',
            'stake quản trị veHAI nhận ưu đãi giảm phí và bảo hiểm rủi ro relayer, vote thông số giao thức (100% không chia cổ tức thụ động)'
        ),
        (
            r'real yield settlement distribution \(USDT streaming via veHAI staking\), and sovereign L1 gas consensus\.',
            'veHAI governance staking, relayer insurance bonding, programmatic Buyback & Burn, and sovereign L1 gas consensus. Zero passive cash dividends are distributed.'
        )
    ],
    'VI_EN': [
        (
            r'stake \(veHAI\) nhận chia sẻ dòng tiền bù trừ thực tế bằng USDT, vote quản trị thông số giao thức',
            'stake quản trị veHAI nhận ưu đãi giảm phí và bảo hiểm rủi ro relayer, vote thông số giao thức (100% không chia cổ tức thụ động)'
        ),
        (
            r'real yield settlement distribution \(USDT streaming via veHAI staking\), and sovereign L1 gas consensus\.',
            'veHAI governance staking, relayer insurance bonding, programmatic Buyback & Burn, and sovereign L1 gas consensus. Zero passive cash dividends are distributed.'
        )
    ],
    'ZH': [
        (
            r'\*\s+支持 veHAI 质押并以纯正 USDT 稳定币分享协议现金流真实收益 \(Real Yield\)\。',
            '* 支持 veHAI 治理质押、协议微费率阶梯折扣、中继器保险保证金机制，以及程序化 50% 回购销毁与 50% 协议储备金 (CHGB)，不分配任何被动股息 (符合 Howey 测试的纯功能型实用架构)。'
        )
    ]
}

def update_saft(file_path):
    filename = os.path.basename(file_path)
    lang_match = re.search(r'HAICHAIN_PRESEED_SAFT_AGREEMENT_([A-Z_]+)\.md', filename)
    if not lang_match:
        return False
    lang = lang_match.group(1)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    if lang in saft_replacements:
        for pattern, replacement in saft_replacements[lang]:
            content = re.sub(pattern, replacement, content)
            
    # Also check if any generic "real yield" or "dividend" remains in the file outside disclaimers
    # Make sure line "Zero passive dividend distributions (non-security utility architecture)" is present
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
        return True
    else:
        print(f"No changes needed for {file_path}")
        return False

# Run on root and app/
for path in glob.glob('HAICHAIN_PRESEED_SAFT_AGREEMENT_*.md') + glob.glob('app/HAICHAIN_PRESEED_SAFT_AGREEMENT_*.md'):
    update_saft(path)

print("SAFT update completed.")
