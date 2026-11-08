import sys, json
sys.stdout.reconfigure(encoding='utf-8')

with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's inspect kk and vi to see the marketplace keys
kk_idx = c.find('"marketplace.title"')
print('marketplace keys snippet:')
print(c[kk_idx:kk_idx+300])

translations = {
    "en": {
        "marketplace.title": "Global Agent Labor Marketplace",
        "marketplace.subtitle": "Universal federated mesh connecting Smithery MCP, Fetch.ai Almanac, and Glama. Direct autonomous discovery, negotiation, and settlement for specialized sub-agents with micro-payments."
    },
    "zh": {
        "marketplace.title": "全球智能体劳动力市场",
        "marketplace.subtitle": "直连 Smithery MCP、Fetch.ai Almanac 及 Glama 全球网络。允许您的 AI 自主搜索、协商并通过链上微支付雇佣专业子智能体。"
    },
    "fr": {
        "marketplace.title": "Marché Mondial des Agents IA",
        "marketplace.subtitle": "Réseau fédéré universel reliant Smithery MCP, Fetch.ai Almanac et Glama. Permet à votre IA de découvrir, négocier et rémunérer des sous-agents spécialisés via des micro-paiements on-chain."
    },
    "ko": {
        "marketplace.title": "글로벌 AI 에이전트 노동 마켓플레이스",
        "marketplace.subtitle": "Smithery MCP, Fetch.ai Almanac 및 Glama와 직접 연동되는 범용 연합 메시. AI가 온체인 마이크로 결제를 통해 전문 하위 에이전트를 자율적으로 검색하고 고용합니다."
    },
    "es": {
        "marketplace.title": "Mercado Global de Agentes AI",
        "marketplace.subtitle": "Malla federada universal conectada a Smithery MCP, Fetch.ai Almanac y Glama. Permite a su IA descubrir, negociar y contratar subagentes especializados mediante micropagos on-chain."
    },
    "ru": {
        "marketplace.title": "Глобальный рынок труда ИИ-агентов",
        "marketplace.subtitle": "Универсальная сеть, объединяющая Smithery MCP, Fetch.ai Almanac и Glama. Автономный поиск, согласование и найм специализированных субагентов через микроплатежи on-chain."
    },
    "he": {
        "marketplace.title": "שוק העבודה העולמי של סוכני AI",
        "marketplace.subtitle": "רשת פדרטיבית המחברת את Smithery MCP, Fetch.ai Almanac ו-Glama. גילוי עצמאי, משא ומתן והעסקת תת-סוכנים מומחים באמצעות מיקרו-תשלומים."
    }
}

# Update both i18n.js and app/i18n.js
for path in ['i18n.js', 'app/i18n.js']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    for lang, kv in translations.items():
        # find "lang": {
        lang_target = f'"{lang}": {{\n'
        if lang_target in content:
            # check if marketplace.title already inside this block
            # find next closing brace or start of next lang
            l_idx = content.find(lang_target)
            next_l_idx = content.find('  },', l_idx)
            block = content[l_idx:next_l_idx]
            if '"marketplace.title"' not in block:
                to_insert = f'    "marketplace.title": "{kv["marketplace.title"]}",\n    "marketplace.subtitle": "{kv["marketplace.subtitle"]}",\n'
                content = content[:l_idx + len(lang_target)] + to_insert + content[l_idx + len(lang_target):]
                print(f'Added marketplace keys to [{lang}] in {path}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done!')
