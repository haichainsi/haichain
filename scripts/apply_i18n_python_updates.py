import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

card1_updates = {
    "en": {
        "dev.card1Badge": "HTTP 402 Paywall • Python & Node.js",
        "dev.card1Desc": "Turn any AI model or API into a monetized autonomous agent using Python (FastAPI/MCP) or Node.js.",
        "dev.sec1Desc": "Install official Haichain SDK for Python (FastAPI / Anthropic MCP) or Node.js to activate Replay Attack protection and on-chain settlements:"
    },
    "vi": {
        "dev.card1Badge": "HTTP 402 Paywall • Python & Node.js",
        "dev.card1Desc": "Biến bất kỳ mô hình AI hoặc API nào thành Agent có thu phí bằng Python (FastAPI/MCP) hoặc Node.js.",
        "dev.sec1Desc": "Cài đặt bộ thư viện SDK chính thức cho Python (FastAPI / Anthropic MCP) hoặc Node.js để kích hoạt bảo vệ chống Replay Attack và quyết toán on-chain:"
    },
    "zh": {
        "dev.card1Badge": "HTTP 402 支付网关 • Python & Node.js",
        "dev.card1Desc": "使用 Python (FastAPI/MCP) 或 Node.js 将任何 AI 模型或 API 封装为付费智能体。",
        "dev.sec1Desc": "安装适用于 Python (FastAPI / Anthropic MCP) 或 Node.js 的官方 SDK 以激活重放攻击防御与链上结算："
    },
    "ko": {
        "dev.card1Badge": "HTTP 402 Paywall • Python & Node.js",
        "dev.card1Desc": "Python (FastAPI/MCP) 또는 Node.js를 사용하여 모든 AI 모델을 유료 에이전트로 전환하세요.",
        "dev.sec1Desc": "Python (FastAPI / Anthropic MCP) 또는 Node.js용 공식 SDK를 설치하여 재전송 공격 방어 및 온체인 정산을 활성화하세요:"
    },
    "es": {
        "dev.card1Badge": "HTTP 402 Paywall • Python & Node.js",
        "dev.card1Desc": "Monetice cualquier modelo IA o API con Python (FastAPI/MCP) o Node.js.",
        "dev.sec1Desc": "Instale el SDK oficial de Haichain para Python (FastAPI / Anthropic MCP) o Node.js para activar la protección contra ataques de repetición y liquidaciones en cadena:"
    },
    "fr": {
        "dev.card1Badge": "HTTP 402 Paywall • Python & Node.js",
        "dev.card1Desc": "Monétisez n'importe quel modèle IA ou API avec Python (FastAPI/MCP) ou Node.js.",
        "dev.sec1Desc": "Installez le SDK officiel pour Python (FastAPI / Anthropic MCP) ou Node.js afin d'activer la protection anti-rejeu et le règlement on-chain :"
    },
    "ru": {
        "dev.card1Badge": "HTTP 402 Paywall • Python & Node.js",
        "dev.card1Desc": "Превратите любую модель ИИ в платного агента с помощью Python (FastAPI/MCP) или Node.js.",
        "dev.sec1Desc": "Установите официальный SDK для Python (FastAPI / Anthropic MCP) или Node.js для защиты от атак повторного воспроизведения и ончейн-расчетов:"
    },
    "kk": {
        "dev.card1Badge": "HTTP 402 Paywall • Python & Node.js",
        "dev.card1Desc": "Python (FastAPI/MCP) немесе Node.js арқылы кез келген AI моделін ақылы агентке айналдырыңыз.",
        "dev.sec1Desc": "Қайталау шабуылдарынан қорғау және ончейн есеп айырысуларды белсендіру үшін Python (FastAPI / Anthropic MCP) немесе Node.js ресми SDK орнатыңыз:"
    },
    "hi": {
        "dev.card1Badge": "HTTP 402 Paywall • Python & Node.js",
        "dev.card1Desc": "Python (FastAPI/MCP) या Node.js के साथ किसी भी AI मॉडल को मोनेटाइज्ड एजेंट में बदलें।",
        "dev.sec1Desc": "रीप्ले अटैक सुरक्षा और ऑन-चेन निपटान को सक्रिय करने के लिए Python (FastAPI / Anthropic MCP) या Node.js आधिकारिक SDK स्थापित करें:"
    },
    "he": {
        "dev.card1Badge": "HTTP 402 Paywall • Python & Node.js",
        "dev.card1Desc": "הפוך כל מודל AI לסוכן בתשלום באמצעות Python (FastAPI/MCP) או Node.js.",
        "dev.sec1Desc": "התקן את ה-SDK הרשמי של Haichain עבור Python (FastAPI / Anthropic MCP) או Node.js כדי להפעיל הגנת Replay Attack וסילוקים ברשת:"
    }
}

for file_path in ['i18n.js', 'app/i18n.js']:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the positions of each language block
    lang_positions = {}
    for lang in card1_updates.keys():
        pos = text.find(f'"{lang}": {{')
        if pos != -1:
            lang_positions[lang] = pos

    sorted_langs = sorted(lang_positions.items(), key=lambda x: x[1])
    for i, (lang, pos) in enumerate(sorted_langs):
        next_pos = sorted_langs[i+1][1] if i + 1 < len(sorted_langs) else len(text)
        block = text[pos:next_pos]

        # Apply updates inside this block
        updates = card1_updates[lang]
        for key, val in updates.items():
            pattern = re.compile(rf'"{re.escape(key)}":\s*"[^"]*"')
            repl = f'"{key}": "{val}"'
            block = pattern.sub(repl, block)

        text = text[:pos] + block + text[next_pos:]
        # Recalculate positions for subsequent iterations
        for l in sorted_langs[i+1:]:
            lang_positions[l[0]] = text.find(f'"{l[0]}": {{')
        sorted_langs = sorted(lang_positions.items(), key=lambda x: x[1])

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Updated translations in {file_path}")
