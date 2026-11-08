import os
import re
import shutil

translations = {
    'ZH': {
        'old_channel': '若服务商突然掉线失联，智能体在物理倒计时结束后 (如 60 秒) 可单方面触发 `close_channel_expired`，100% 完整收回未消费资金，资金安全万无一失。',
        'new_channel': '智能体可发起 `request_channel_close`。通道进入 300 个插槽 (约 120 秒) 争议挑战窗口 (Dispute Challenge Window)，允许服务商提交最新签署凭证结算。若 300 插槽内无争议，100% 剩余未消费资金安全退还智能体；恶意提款将被罚没 (Slashing) 质押金。',
        'replacements': [
            ('$0.000001 (Netting)', '$0.000001 (1,000:1 状态通道压缩 / $0.001 基础费用)'),
            ('极低手续费 ($0.000001', '极低手续费 ($0.000001 压缩净额 / $0.001 基础费'),
            ('极低的手续费 ($0.000001)', '极低手续费 ($0.000001 压缩净额 / $0.001 基础费)'),
            ('欧盟法规 (EU AI Act、GDPR、MiCA、SEPA)', '欧盟法规 (EU AI Act、GDPR、符合 MiCA 的 Circle USDC/EURC、SEPA)')
        ]
    },
    'ES': {
        'old_channel': 'Si un proveedor se desconecta inesperadamente, el Agente invoca `close_channel_expired` al expirar el temporizador (ej. 60 segundos), recuperando el 100% de los fondos no consumidos sin riesgo de pérdida.',
        'new_channel': 'El Agente invoca `request_channel_close`. El canal entra en una Ventana de Desafío de Disputa de 300 slots (~120s) que permite al proveedor presentar el último comprobante firmado para liquidación equitativa. Sin disputa en 300 slots, el 100% del colateral no consumido se desbloquea con cero riesgo de pérdida; fraudes se castigan con Slashing.',
        'replacements': [
            ('$0.000001 (Netting)', '$0.000001 (Compresión 1,000:1 / $0.001 Base)'),
            ('($0.000001 piso de compensación)', '($0.000001 por compresión 1,000:1 / $0.001 base)'),
            ('tarifas de transacción de $0.000001', 'tarifas base de ~$0.001 ($0.000001 por tick con compresión 1,000:1)'),
            ('Sentiment, CAPTCHA, UI validation', 'Sentiment, RLHF, Validación de Firma Humana'),
            ('(EU AI Act, GDPR, MiCA, SEPA)', '(EU AI Act, GDPR, MiCA con Circle USDC & EURC, SEPA)')
        ]
    },
    'FR': {
        'old_channel': 'Si le prestataire s\'interrompt brutalement, l\'Agent appelle `close_channel_expired` après l\'écoulement d\'un délai (ex: 60 secondes), récupérant l\'intégralité de son capital sans la moindre perte.',
        'new_channel': 'L\'Agent appelle `request_channel_close`. Le canal entre dans une Fenêtre de Défi de Litige de 300 slots (~120s) permettant au prestataire de soumettre le dernier bon signé pour un règlement équitable. En l\'absence de litige sous 300 slots, 100% du capital non consommé est débloqué sans risque; toute tentative frauduleuse entraîne un Slashing.',
        'replacements': [
            ('$0.000001 (Netting)', '$0.000001 (Compression 1 000:1 / $0,001 Base)'),
            ('($0.000001 plancher de compensation)', '($0,000001 par compression 1 000:1 / $0,001 base)'),
            ('frais de transaction de $0.000001', 'frais de base de ~$0,001 ($0,000001 par tick via compression 1 000:1)'),
            ('Sentiment, CAPTCHA, UI validation', 'Sentiment, RLHF, Validation de Signature Humaine'),
            ('(EU AI Act, GDPR, MiCA, SEPA)', '(EU AI Act, GDPR, MiCA conforme via Circle USDC & EURC, SEPA)')
        ]
    },
    'KO': {
        'old_channel': '공급자의 연결이 예기치 않게 끊어지면 타이머 만료(예: 60초) 시 에이전트가 `close_channel_expired`를 호출하여 미소비 담보를 100% 회수합니다.',
        'new_channel': '에이전트가 `request_channel_close`를 호출하면 300 슬롯(~120초)의 분쟁 챌린지 윈도우(Dispute Challenge Window)에 진입합니다. 제공자는 서명된 최신 바우처를 제출하여 공정 정산할 수 있습니다. 300 슬롯 내 이의가 없으면 미소비 자금 100%가 안전하게 잠금 해제되며, 부정 조기 인출 시도는 보증금 Slashing 처리됩니다.',
        'replacements': [
            ('$0.000001 (Netting)', '$0.000001 (1,000:1 압축 정산 / $0.001 기본료)'),
            ('($0.000001 정산 바닥)', '($0.000001 1,000:1 압축 / $0.001 기본 수수료)'),
            ('$0.000001의 트랜잭션 수수료로', '~$0.001 기본 수수료(1,000:1 배치 압축 시 틱당 $0.000001)로'),
            ('(EU AI Act, GDPR, MiCA, SEPA)', '(EU AI Act, GDPR, Circle USDC/EURC 기반 MiCA 준수, SEPA)')
        ]
    },
    'RU': {
        'old_channel': 'Если поставщик внезапно обрывает связь, агент вызывает метод `close_channel_expired` по истечении тайм-аута (например, 60 секунд), возвращая весь заблокированный капитал без потерь.',
        'new_channel': 'Агент вызывает `request_channel_close`. Канал переходит в Окно Оспаривания на 300 слотов (~120с), позволяя поставщику предоставить последний подписанный ваучер для справедливого расчета. Без споров в течение 300 слотов 100% неиспользованных средств безопасно возвращаются; мошеннические попытки наказываются слэшингом (Slashing).',
        'replacements': [
            ('(EU AI Act, GDPR, MiCA, SEPA)', '(EU AI Act, GDPR, соответствие MiCA через Circle USDC/EURC, SEPA)')
        ]
    },
    'KK': {
        'old_channel': 'Если поставщик внезапно обрывает связь, агент вызывает метод `close_channel_expired` по истечении тайм-аута (например, 60 секунд), возвращая весь заблокированный капитал без потерь.',
        'new_channel': 'Агент `request_channel_close` шақырады. Арна 300 слоттық (~120с) Дауласу Терезесіне (Dispute Challenge Window) өтеді, бұл жеткізушіге соңғы қол қойылған ваучерді ұсынуға мүмкіндік береді. 300 слот ішінде дау туындамаса, қаражаттың 100%-ы қауіпсіз қайтарылады; алаяқтық әрекеттер Slashing арқылы айыппұлға ұшырайды.',
        'replacements': [
            ('(EU AI Act, GDPR, MiCA, SEPA)', '(EU AI Act, GDPR, Circle USDC/EURC арқылы MiCA талаптарына сәйкес, SEPA)')
        ]
    },
    'HI': {
        'old_channel': 'Если поставщик внезапно обрывает связь, агент вызывает метод `close_channel_expired` по истечении тайм-аута (например, 60 секунд), возвращая весь заблокированный капитал без потерь.',
        'new_channel': 'यदि प्रदाता अप्रत्याशित रूप से डिस्कनेक्ट हो जाता है, तो एजेंट `request_channel_close` लागू करता है। चैनल 300 स्लॉट (~120s) डिस्प्यूट चैलेंज विंडो में प्रवेश करता है, जिससे प्रदाता नवीनतम हस्ताक्षरित वाउचर प्रस्तुत कर सकता है। 300 स्लॉट में कोई विवाद न होने पर 100% अप्रयुक्त पूंजी सुरक्षित रूप से अनलॉक हो जाती है; कपटपूर्ण निकासी पर स्लैशिंग (Slashing) लागू होती है।',
        'replacements': [
            ('(EU AI Act, GDPR, MiCA, SEPA)', '(EU AI Act, GDPR, Circle USDC/EURC के साथ MiCA अनुपालन, SEPA)')
        ]
    },
    'HE': {
        'old_channel': 'הסוכן מפעיל את `close_channel_expired` עם פקיעת טיימר התפוגה (למשל 60 שניות), ומחזיר 100% מהבטוחות שלא נצרכו ללא שום סיכון לאובדן הון.',
        'new_channel': 'הסוכן מפעיל `request_channel_close`. הערוץ נכנס לחלון ערעור ומחלוקת של 300 סלוטים (~120 שניות) המאפשר לספק להגיש את השובר החתום העדכני ביותר להסדר הוגן. בהיעדר מחלוקת תוך 300 סלוטים, 100% מהביטחונות משוחררים בבטחה; ניסיון משיכה זדוני נענש בסלשינג (Slashing).',
        'replacements': [
            ('$0.000001 (Netting)', '$0.000001 (דחיסת 1,000:1 / $0.001 בסיס)'),
            ('($0.000001 רצפת קיזוז)', '($0.000001 בדחיסת 1,000:1 / $0.001 בסיס)'),
            ('דמי עסקה של $0.000001', 'דמי בסיס של כ-$0.001 ($0.000001 לטיק בדחיסת 1,000:1)'),
            ('(EU AI Act, GDPR, MiCA, SEPA)', '(EU AI Act, GDPR, תאימות ל-MiCA באמצעות Circle USDC/EURC, SEPA)')
        ]
    }
}

for lang, data in translations.items():
    fname = f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
    if not os.path.exists(fname):
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Channel update
    if data['old_channel'] in content:
        content = content.replace(data['old_channel'], data['new_channel'])
        print(f"[{lang}] Successfully patched dispute challenge window.")
    else:
        # Regex search for close_channel_expired line
        pattern = re.compile(r'[^\n]*`close_channel_expired`[^\n]*', re.UNICODE)
        if pattern.search(content):
            content = pattern.sub(data['new_channel'], content)
            print(f"[{lang}] Patched dispute challenge window line via regex.")
        else:
            print(f"[{lang}] close_channel_expired line already updated or not found.")

    # Replacements
    for old_r, new_r in data['replacements']:
        if old_r in content:
            content = content.replace(old_r, new_r)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    app_path = os.path.join('app', fname)
    shutil.copyfile(fname, app_path)
    print(f"[{lang}] Synced to {app_path}")

print("All 8 international whitepapers successfully updated and synced!")
