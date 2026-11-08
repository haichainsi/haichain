import json
import re

# Translation data for all 10 languages
translations = {
    "vi": {
        "aiHub.onlineStep2": "Đặt tên: 'HAICHAIN' và dán Server URL (đã sao chép ở trên) vào ô URL.",
        "aiHub.badgeDedicated": "🔒 ĐÃ GẮN VÍ RIÊNG",
        "aiHub.badgeGeneric": "⚡ URL CHUNG (CHƯA GẮN VÍ)",
        "aiHub.connectedTitle": "URL Cá Nhân Hóa Dành Riêng Cho Ví:",
        "aiHub.connectedDesc": "AI Claude Mobile sẽ tự động liên kết thẳng vào két chi tiêu của ví này mà không cần nhập thủ công địa chỉ trong khung chat.",
        "aiHub.unconnectedTitle": "Bạn muốn AI cá nhân hóa theo ví riêng?",
        "aiHub.unconnectedDesc": "Kết nối ví ngay để hệ thống tự động sinh Server URL độc quyền gắn mã két của bạn.",
        "aiHub.btnConnectForLink": "⚡ Kết nối ví để nhận link riêng",
        "aiHub.copiedPersonalizedToastMsg": "Đã sao chép Server URL MCP cá nhân hóa! Claude Mobile sẽ tự động nhận diện ví của bạn.",
        "aiHub.copiedGenericToastMsg": "Đã sao chép Server URL MCP chung. (Mẹo: Kết nối ví để nhận link cá nhân hóa riêng)"
    },
    "en": {
        "aiHub.onlineStep2": "Set Name to 'HAICHAIN' and paste the copied Server URL from above into the URL field.",
        "aiHub.badgeDedicated": "🔒 DEDICATED VAULT BOUND",
        "aiHub.badgeGeneric": "⚡ GENERIC URL (UNBOUND)",
        "aiHub.connectedTitle": "Personalized URL for Wallet:",
        "aiHub.connectedDesc": "Claude Mobile AI will automatically bind directly to this wallet's spending pot without requiring manual address entry in chat.",
        "aiHub.unconnectedTitle": "Want AI personalized to your own wallet?",
        "aiHub.unconnectedDesc": "Connect wallet now to automatically generate a dedicated Server URL bound to your vault.",
        "aiHub.btnConnectForLink": "⚡ Connect Wallet for Dedicated Link",
        "aiHub.copiedPersonalizedToastMsg": "Dedicated personalized MCP URL copied! Claude Mobile will automatically bind to your vault.",
        "aiHub.copiedGenericToastMsg": "Generic MCP URL copied. (Tip: Connect wallet to get your dedicated URL)"
    },
    "zh": {
        "aiHub.onlineStep2": "设置名称为 'HAICHAIN' 并将上方复制的 Server URL 粘贴到 URL 输入框中。",
        "aiHub.badgeDedicated": "🔒 已绑定专属金库",
        "aiHub.badgeGeneric": "⚡ 通用 URL（未绑定钱包）",
        "aiHub.connectedTitle": "专属个性化钱包 URL：",
        "aiHub.connectedDesc": "Claude 手机端 AI 将自动直连该钱包的支出金库，无需在聊天中手动输入地址。",
        "aiHub.unconnectedTitle": "想要 AI 针对您的专属钱包进行个性化？",
        "aiHub.unconnectedDesc": "立即连接钱包，系统将自动生成绑定您金库的专属 Server URL。",
        "aiHub.btnConnectForLink": "⚡ 连接钱包获取专属链接",
        "aiHub.copiedPersonalizedToastMsg": "已复制专属个性化 MCP URL！Claude 手机端将自动绑定您的金库。",
        "aiHub.copiedGenericToastMsg": "已复制通用 MCP URL。（提示：连接钱包即可获取专属链接）"
    },
    "kk": {
        "aiHub.onlineStep2": "Атауын 'HAICHAIN' деп қойып, жоғарыда көшірілген Server URL мекенжайын енгізіңіз.",
        "aiHub.badgeDedicated": "🔒 ЖЕКЕ СЕЙФ БАЙЛАНҒАН",
        "aiHub.badgeGeneric": "⚡ ЖАЛПЫ URL (ӘМИЯНСЫЗ)",
        "aiHub.connectedTitle": "Әмиянға арналған жеке URL:",
        "aiHub.connectedDesc": "Claude Mobile AI осы әмиянның шығыс сейфіне тікелей қосылады, чатта мекенжайды қолмен енгізу қажет емес.",
        "aiHub.unconnectedTitle": "AI-ды жеке әмияныңызға бейімдегіңіз келе ме?",
        "aiHub.unconnectedDesc": "Сейфіңіз байланысқан эксклюзивті Server URL алу үшін әмиянды қазір қосыңыз.",
        "aiHub.btnConnectForLink": "⚡ Жеке сілтеме алу үшін әмиянды қосу",
        "aiHub.copiedPersonalizedToastMsg": "Жеке MCP URL көшірілді! Claude Mobile автоматты түрде сейфіңізге байланады.",
        "aiHub.copiedGenericToastMsg": "Жалпы MCP URL көшірілді. (Кеңес: Жеке сілтеме алу үшін әмиянды қосыңыз)"
    },
    "ko": {
        "aiHub.onlineStep2": "이름을 'HAICHAIN'으로 설정하고 위에서 복사한 Server URL을 URL 입력란에 붙여넣습니다.",
        "aiHub.badgeDedicated": "🔒 전용 금고 연결됨",
        "aiHub.badgeGeneric": "⚡ 공용 URL (지갑 미연결)",
        "aiHub.connectedTitle": "지갑 전용 맞춤 URL:",
        "aiHub.connectedDesc": "Claude 모바일 AI가 채팅창에 주소를 수동 입력할 필요 없이 이 지갑의 지출 금고에 자동 직결됩니다.",
        "aiHub.unconnectedTitle": "AI가 내 전용 지갑에 맞춤화되길 원하시나요?",
        "aiHub.unconnectedDesc": "지금 지갑을 연결하면 금고에 연동된 전용 Server URL이 자동 생성됩니다.",
        "aiHub.btnConnectForLink": "⚡ 전용 링크 발급받기 위해 지갑 연결",
        "aiHub.copiedPersonalizedToastMsg": "전용 맞춤 MCP URL이 복사되었습니다! Claude 모바일이 금고에 자동 연결됩니다.",
        "aiHub.copiedGenericToastMsg": "공용 MCP URL이 복사되었습니다. (팁: 전용 링크를 받으려면 지갑을 연결하세요)"
    },
    "fr": {
        "aiHub.onlineStep2": "Nommez-le 'HAICHAIN' et collez l'URL du serveur copiée ci-dessus dans le champ URL.",
        "aiHub.badgeDedicated": "🔒 COFFRE DÉDIÉ LIÉ",
        "aiHub.badgeGeneric": "⚡ URL GÉNÉRIQUE (NON LIÉ)",
        "aiHub.connectedTitle": "URL personnalisée pour le portefeuille :",
        "aiHub.connectedDesc": "L'IA Claude Mobile se connectera automatiquement au coffre de ce portefeuille sans saisie manuelle dans le chat.",
        "aiHub.unconnectedTitle": "Vous souhaitez une IA personnalisée pour votre portefeuille ?",
        "aiHub.unconnectedDesc": "Connectez votre portefeuille pour générer une URL de serveur dédiée liée à votre coffre.",
        "aiHub.btnConnectForLink": "⚡ Connecter le portefeuille pour le lien dédié",
        "aiHub.copiedPersonalizedToastMsg": "URL MCP personnalisée copiée ! Claude Mobile se liera automatiquement à votre coffre.",
        "aiHub.copiedGenericToastMsg": "URL MCP générique copiée. (Astuce : Connectez votre portefeuille pour un lien dédié)"
    },
    "es": {
        "aiHub.onlineStep2": "Nómbrelo 'HAICHAIN' y pegue la URL del servidor copiada arriba en el campo URL.",
        "aiHub.badgeDedicated": "🔒 BÓVEDA DEDICADA VINCULADA",
        "aiHub.badgeGeneric": "⚡ URL GENÉRICA (SIN VINCULAR)",
        "aiHub.connectedTitle": "URL personalizada para la billetera:",
        "aiHub.connectedDesc": "La IA de Claude Móvil se vinculará directamente a la bóveda de gasto de esta billetera sin necesidad de escribir la dirección en el chat.",
        "aiHub.unconnectedTitle": "¿Desea que la IA se personalice para su billetera?",
        "aiHub.unconnectedDesc": "Conecte su billetera ahora para generar una URL de servidor dedicada vinculada a su bóveda.",
        "aiHub.btnConnectForLink": "⚡ Conectar billetera para enlace dedicado",
        "aiHub.copiedPersonalizedToastMsg": "¡URL MCP personalizada copiada! Claude Móvil se vinculará automáticamente a su bóveda.",
        "aiHub.copiedGenericToastMsg": "URL MCP genérica copiada. (Consejo: Conecte su billetera para obtener un enlace dedicado)"
    },
    "ru": {
        "aiHub.onlineStep2": "Укажите имя 'HAICHAIN' и вставьте скопированный выше Server URL в поле URL.",
        "aiHub.badgeDedicated": "🔒 ПРИВЯЗАНО К СЕЙФУ",
        "aiHub.badgeGeneric": "⚡ ОБЩИЙ URL (НЕТ ПРИВЯЗКИ)",
        "aiHub.connectedTitle": "Персональный URL для кошелька:",
        "aiHub.connectedDesc": "Claude Mobile AI автоматически подключится к сейфу этого кошелька без ручного ввода адреса в чате.",
        "aiHub.unconnectedTitle": "Хотите персонализировать AI под ваш кошелек?",
        "aiHub.unconnectedDesc": "Подключите кошелек сейчас, чтобы сгенерировать персональный Server URL для вашего сейфа.",
        "aiHub.btnConnectForLink": "⚡ Подключить кошелек для личной ссылки",
        "aiHub.copiedPersonalizedToastMsg": "Персональный MCP URL скопирован! Claude Mobile автоматически привяжется к вашему сейфу.",
        "aiHub.copiedGenericToastMsg": "Общий MCP URL скопирован. (Совет: Подключите кошелек для персональной ссылки)"
    },
    "hi": {
        "aiHub.onlineStep2": "नाम 'HAICHAIN' सेट करें और ऊपर कॉपी किया गया Server URL पेस्ट करें।",
        "aiHub.badgeDedicated": "🔒 समर्पित वॉल्ट लिंक किया गया",
        "aiHub.badgeGeneric": "⚡ सामान्य URL (अलिंक)",
        "aiHub.connectedTitle": "वॉलेट के लिए वैयक्तिकृत URL:",
        "aiHub.connectedDesc": "Claude मोबाइल AI बिना चैट में पता दर्ज किए सीधे इस वॉलेट के खर्च वॉल्ट से जुड़ जाएगा।",
        "aiHub.unconnectedTitle": "क्या आप अपने व्यक्तिगत वॉलेट के लिए AI चाहते हैं?",
        "aiHub.unconnectedDesc": "अपने वॉल्ट से बंधा एक समर्पित Server URL उत्पन्न करने के लिए अभी वॉलेट कनेक्ट करें।",
        "aiHub.btnConnectForLink": "⚡ समर्पित लिंक के लिए वॉलेट कनेक्ट करें",
        "aiHub.copiedPersonalizedToastMsg": "वैयक्तिकृत MCP URL कॉपी किया गया! Claude मोबाइल आपके वॉल्ट से जुड़ जाएगा।",
        "aiHub.copiedGenericToastMsg": "सामान्य MCP URL कॉपी किया गया। (सुझाव: समर्पित लिंक के लिए वॉलेट कनेक्ट करें)"
    },
    "he": {
        "aiHub.onlineStep2": "הגדר שם: 'HAICHAIN' והדבק את כתובת ה-Server URL שהועתקה למעלה בשדה ה-URL.",
        "aiHub.badgeDedicated": "🔒 כספת ייעודית מקושרת",
        "aiHub.badgeGeneric": "⚡ URL כללי (ללא ארנק)",
        "aiHub.connectedTitle": "כתובת URL מותאמת אישית לארנק:",
        "aiHub.connectedDesc": "ה-AI של Claude Mobile יתחבר ישירות לכספת ההוצאות של ארנק זה ללא צורך בהזנת כתובת בצ'אט.",
        "aiHub.unconnectedTitle": "רוצה שה-AI יותאם אישית לארנק שלך?",
        "aiHub.unconnectedDesc": "חבר ארנק כעת כדי ליצור כתובת Server URL ייעודית המקושרת לכספת שלך.",
        "aiHub.btnConnectForLink": "⚡ חבר ארנק לקבלת קישור ייעודי",
        "aiHub.copiedPersonalizedToastMsg": "כתובת MCP מותאמת אישית הועתקה! Claude Mobile יקושר אוטומטית לכספת שלך.",
        "aiHub.copiedGenericToastMsg": "כתובת MCP כללית הועתקה. (טיפ: חבר ארנק לקבלת קישור ייעודי)"
    }
}

def update_file(filepath):
    print(f"Updating {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for lang, keys in translations.items():
        # Find where lang is defined: "lang": {
        # We need to insert keys into that block if not already there, and update onlineStep2
        lang_pattern = f'"{lang}":\\s*\\{{'
        lang_match = re.search(lang_pattern, content)
        if not lang_match:
            print(f"Lang {lang} not found in {filepath}!")
            continue

        # In this language block, update aiHub.onlineStep2
        step2_val = keys["aiHub.onlineStep2"]
        # Replace existing onlineStep2 in this lang
        # First locate next lang or end of object
        start_pos = lang_match.end()
        # Find the next language key or end of translations
        # To be safe, look for '"aiHub.onlineStep2":' after start_pos
        step2_regex = re.compile(r'("aiHub\.onlineStep2":\s*")[^"]*(")')
        # Search only within this language section
        sub_content = content[start_pos:]
        m_step2 = step2_regex.search(sub_content)
        if m_step2:
            abs_start = start_pos + m_step2.start()
            abs_end = start_pos + m_step2.end()
            new_step2_str = f'"aiHub.onlineStep2": "{step2_val}"'
            content = content[:abs_start] + new_step2_str + content[abs_end:]

        # Now check which new keys need to be added to this language block
        new_entries = []
        for k, v in keys.items():
            if k == "aiHub.onlineStep2":
                continue
            if f'"{k}":' not in content[start_pos:start_pos + 40000]: # rough block size
                escaped_v = v.replace('"', '\\"')
                new_entries.append(f'    "{k}": "{escaped_v}",')

        if new_entries:
            # Insert right after '"aiHub.onlineStep2": ...'
            insert_marker = f'"aiHub.onlineStep2": "{step2_val}",'
            if insert_marker not in content:
                insert_marker = f'"aiHub.onlineStep2": "{step2_val}"'
            
            idx = content.find(insert_marker, start_pos)
            if idx != -1:
                replacement = insert_marker + "\n" + "\n".join(new_entries)
                content = content[:idx] + replacement + content[idx + len(insert_marker):]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Finished {filepath}.")

update_file('i18n.js')
update_file('app/i18n.js')
