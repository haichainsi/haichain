import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for path in ['i18n.js', 'app/i18n.js']:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # Regex replace all "aud.investorNowDesc": "..." containing 0.007
    # en
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"Pre-Seed entry at \$0\.007[^"]+"',
        '"aud.investorNowDesc": "Confidential Institutional Early Backer allocation; receive pure Real Yield in USDT (40% of all machine fees) plus 60% continuous Buyback & Burn."',
        text
    )
    # vi
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"Cơ hội tham gia vòng Pre-Seed giá \$0\.007[^"]+"',
        '"aud.investorNowDesc": "Phân bổ chiến lược bảo mật dành cho Angel Partners & Đối tác; hưởng Real Yield bằng USDT (40% phí giao dịch máy móc) cùng 60% Buyback & Burn liên tục."',
        text
    )
    # kk
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"Pre-Seed кезеңіне \$0\.007[^"]+"',
        '"aud.investorNowDesc": "Институционалдық ерте қолдаушылардың жабық үлесі; таза USDT түріндегі Real Yield (барлық машина комиссияларының 40%) және үздіксіз 60% Buyback & Burn алу."',
        text
    )
    # zh
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"Pre-Seed 轮定价 \$0\.007[^"]+"',
        '"aud.investorNowDesc": "机构与早期合伙人保密战略配额；享有 40% 全球协议费用的纯 USDT 真实收益分红与 60% 协议代币持续回购销毁。"',
        text
    )
    # ko
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"사전 시드\(Pre-Seed\) 라운드 \$0\.007[^"]+"',
        '"aud.investorNowDesc": "기관 및 엔젤 파트너 전용 비공개 전략적 배분; 순수 USDT 실제 수익 분배 (글로벌 프로토콜 수수료의 40%) 및 60% 지속적인 바이백 앤 번 혜택."',
        text
    )
    # fr
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"Entr[^"]*Pre-Seed[^"]*0,007[^"]+"',
        '"aud.investorNowDesc": "Allocation stratégique confidentielle pour partenaires et fonds institutionnels ; distribution de Real Yield en USDT pur (40% de tous les frais de machine) et 60% de rachat et combustion continus."',
        text
    )
    # es
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"Entrada en ronda Pre-Seed a \$0\.007[^"]+"',
        '"aud.investorNowDesc": "Asignación estratégica confidencial para socios institucionales; distribución de Real Yield en USDT puro (40% de tarifas de máquina) y 60% de recompra y quema continua."',
        text
    )
    # ru
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"Вход на стадии Pre-Seed по \$0\.007[^"]+"',
        '"aud.investorNowDesc": "Конфиденциальная стратегическая аллокация для институциональных партнеров; получение чистого Real Yield в USDT (40% всех комиссий сети) и 60% непрерывного Buyback & Burn."',
        text
    )
    # hi
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"Pre-Seed राउंड में \$0\.007[^"]+"',
        '"aud.investorNowDesc": "संस्थागत और रणनीतिक भागीदारों के लिए गोपनीय आवंटन; शुद्ध USDT में वास्तविक उपज (सभी मशीन शुल्क का 40%) और निरंतर 60% बायबैक और बर्न प्राप्त करें।"',
        text
    )
    # he
    text = re.sub(
        r'"aud\.investorNowDesc":\s*"כניסה בסבב Pre-Seed במחיר \$0\.007[^"]+"',
        '"aud.investorNowDesc": "הקצאה אסטרטגית סודית למשקיעים ושותפים מוסדיים; קבלת Real Yield טהור ב-USDT (40% מכלל עמלות המכונות) ו-60% רכישה חוזרת ושריפה מתמשכת."',
        text
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Sanitized {path}")
