import json
import re

print("Adding marketplace i18n keys to i18n.js and app/i18n.js...")

TRANSLATIONS = {
    'vi': {
        'marketplace.title': 'Sàn Việc Làm Agent Quốc Tế',
        'marketplace.subtitle': 'Mạng lưới liên kết trực tiếp Smithery MCP, Fetch.ai Almanac & Glama. Cho phép AI của bạn tự động tìm kiếm, đàm phán và thuê Agent phụ qua vi thanh toán on-chain.'
    },
    'en': {
        'marketplace.title': 'Global Agent Labor Marketplace',
        'marketplace.subtitle': 'Universal federated mesh connecting Smithery MCP, Fetch.ai Almanac, and Glama. Your AI can autonomously search, negotiate, and hire specialized sub-agents with micro-payments.'
    },
    'zh': {
        'marketplace.title': '全球智能体劳动力市场',
        'marketplace.subtitle': '直连 Smithery MCP、Fetch.ai Almanac 及 Glama 全球网络。允许您的 AI 自主搜索、协商并通过链上微支付雇佣专业子智能体。'
    },
    'es': {
        'marketplace.title': 'Mercado Global de Agentes AI',
        'marketplace.subtitle': 'Malla federada universal conectada a Smithery MCP, Fetch.ai Almanac y Glama. Su IA puede buscar, negociar y contratar subagentes especializados mediante micropagos on-chain.'
    },
    'fr': {
        'marketplace.title': 'Marché Mondial des Agents IA',
        'marketplace.subtitle': 'Réseau fédéré universel reliant Smithery MCP, Fetch.ai Almanac et Glama. Votre IA peut rechercher, négocier et embaucher des sous-agents spécialisés via des micro-paiements on-chain.'
    },
    'ko': {
        'marketplace.title': '글로벌 AI 에이전트 노동 마켓플레이스',
        'marketplace.subtitle': 'Smithery MCP, Fetch.ai Almanac 및 Glama와 직접 연결된 글로벌 네트워크. AI가 온체인 마이크로 결제를 통해 전문 하위 에이전트를 자율적으로 검색하고 고용합니다.'
    },
    'ru': {
        'marketplace.title': 'Глобальный рынок труда ИИ-агентов',
        'marketplace.subtitle': 'Универсальная сеть, объединяющая Smithery MCP, Fetch.ai Almanac и Glama. Ваш ИИ может автономно находить и нанимать специализированных субагентов через микроплатежи on-chain.'
    },
    'hi': {
        'marketplace.title': 'ग्लोबल एआई एजेंट लेबर मार्केटप्लेस',
        'marketplace.subtitle': 'Smithery MCP, Fetch.ai Almanac और Glama से सीधे जुड़ा फेडरेटेड नेटवर्क। आपका AI ऑन-चेन माइक्रो-पेमेंट के जरिए स्पेशलाइज्ड सब-एजेंट्स को हायर कर सकता है।'
    },
    'kk': {
        'marketplace.title': 'Жаһандық AI агенттер еңбек нарығы',
        'marketplace.subtitle': 'Smithery MCP, Fetch.ai Almanac және Glama жүйелерімен байланысқан желі. AI мамандандырылған қосалқы агенттерді ончейн микротөлемдер арқылы тауып, жалдай алады.'
    },
    'he': {
        'marketplace.title': 'שוק העבודה העולמי של סוכני AI',
        'marketplace.subtitle': 'רשת פדרטיבית המחברת את Smithery MCP, Fetch.ai Almanac ו-Glama. ה-AI שלך יכול לחפש ולשכור תת-סוכנים מומחים באמצעות מיקרו-תשלומים ברשת.'
    }
}

for filepath in ['i18n.js', 'app/i18n.js']:
    print(f"Updating {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # In i18n.js, each language block is like:
    #   vi: {
    #     ...
    #   },
    for lang, kvs in TRANSLATIONS.items():
        pattern = rf'({lang}\s*:\s*\{{[\s\S]*?)(}})'
        # Let's see if we can find a good anchor in each language object, like "connectors.gatewayReady"
        anchor = f'"connectors.gatewayReady"'
        # Let's check how connectors.gatewayReady is formatted in this lang
        injection = f'    "marketplace.title": "{kvs["marketplace.title"]}",\n    "marketplace.subtitle": "{kvs["marketplace.subtitle"]}",\n'
        
        # We can find the lang block by searching for lang: {
        lang_start = content.find(f'{lang}:')
        if lang_start == -1:
            lang_start = content.find(f"'{lang}':")
        if lang_start == -1:
            lang_start = content.find(f'"{lang}":')

        if lang_start != -1:
            # Find the next "swarm.title":
            swarm_pos = content.find('"swarm.title":', lang_start)
            if swarm_pos != -1:
                # Insert right before "swarm.title":
                content = content[:swarm_pos] + injection + content[swarm_pos:]
                print(f"  Inserted keys for [{lang}] before swarm.title")
            else:
                print(f"  Could not find swarm.title for [{lang}]")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {filepath}")

print("=== i18n Updates Complete ===")
