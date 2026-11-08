import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

new_keys_map = {
    "en": {
        "vault.heartbeatSession": "Heartbeat Session (valid_until)",
        "vault.touchPasskey": "Touch Passkey to Refresh (+1h)",
        "vault.timeToControl": "Time-to-Control (τ)",
        "vault.maxTheftCeiling": "Max Theft Ceiling E_theft(τ)",
        "vault.authorityArchitecture": "Authority Decoupling",
        "vault.masterPasskeyBadge": "Master: FIDO2 Passkey (P-256)",
        "vault.subAgentBadge": "Sub-Agents: Ephemeral Ed25519",
        "vault.wireSpecBadge": "CapLeaf v1 (223 Bytes LE)"
    },
    "vi": {
        "vault.heartbeatSession": "Phiên Heartbeat (valid_until)",
        "vault.touchPasskey": "Chạm Passkey để Gia Hạn (+1h)",
        "vault.timeToControl": "Thời Gian Kiểm Soát (τ)",
        "vault.maxTheftCeiling": "Trần Rủi Ro Tối Đa E_theft(τ)",
        "vault.authorityArchitecture": "Tách Biệt Quyền Lực",
        "vault.masterPasskeyBadge": "Chủ Sở Hữu: FIDO2 Passkey (P-256)",
        "vault.subAgentBadge": "Agent Con: Ed25519 Tạm Thời",
        "vault.wireSpecBadge": "Chuẩn Wire CapLeaf v1 (223 Bytes LE)"
    },
    "zh": {
        "vault.heartbeatSession": "心跳会话有效周期 (valid_until)",
        "vault.touchPasskey": "触碰 Passkey 延长 (+1小时)",
        "vault.timeToControl": "控制反应时间 (τ)",
        "vault.maxTheftCeiling": "最大损失数学上限 E_theft(τ)",
        "vault.authorityArchitecture": "权限架构解耦",
        "vault.masterPasskeyBadge": "主权限: FIDO2 Passkey (P-256)",
        "vault.subAgentBadge": "子代理: 临时 Ed25519",
        "vault.wireSpecBadge": "CapLeaf v1 规范 (223 Bytes LE)"
    },
    "ko": {
        "vault.heartbeatSession": "하트비트 세션 유효주기 (valid_until)",
        "vault.touchPasskey": "Passkey 터치로 연장 (+1시간)",
        "vault.timeToControl": "제어 반응 시간 (τ)",
        "vault.maxTheftCeiling": "최대 손실 수학적 상한 E_theft(τ)",
        "vault.authorityArchitecture": "권한 분리 아키텍처",
        "vault.masterPasskeyBadge": "마스터: FIDO2 Passkey (P-256)",
        "vault.subAgentBadge": "하위 에이전트: 임시 Ed25519",
        "vault.wireSpecBadge": "CapLeaf v1 표준 (223 Bytes LE)"
    },
    "fr": {
        "vault.heartbeatSession": "Session Heartbeat (valid_until)",
        "vault.touchPasskey": "Toucher Passkey pour Renouveler (+1h)",
        "vault.timeToControl": "Temps de Contrôle (τ)",
        "vault.maxTheftCeiling": "Plafond de Perte Max E_theft(τ)",
        "vault.authorityArchitecture": "Séparation des Autorités",
        "vault.masterPasskeyBadge": "Maître : Clé Passkey FIDO2 (P-256)",
        "vault.subAgentBadge": "Sous-Agents : Ed25519 Éphémère",
        "vault.wireSpecBadge": "CapLeaf v1 (223 Octets LE)"
    },
    "es": {
        "vault.heartbeatSession": "Sesión Heartbeat (valid_until)",
        "vault.touchPasskey": "Tocar Passkey para Renovar (+1h)",
        "vault.timeToControl": "Tiempo de Control (τ)",
        "vault.maxTheftCeiling": "Techo Máximo de Pérdida E_theft(τ)",
        "vault.authorityArchitecture": "Desacoplamiento de Autoridad",
        "vault.masterPasskeyBadge": "Maestro: Passkey FIDO2 (P-256)",
        "vault.subAgentBadge": "Sub-Agentes: Ed25519 Efímero",
        "vault.wireSpecBadge": "CapLeaf v1 (223 Bytes LE)"
    },
    "ru": {
        "vault.heartbeatSession": "Сессия Heartbeat (valid_until)",
        "vault.touchPasskey": "Коснитесь Passkey для Продления (+1ч)",
        "vault.timeToControl": "Время Реакции Контроля (τ)",
        "vault.maxTheftCeiling": "Предел Максимального Ущерба E_theft(τ)",
        "vault.authorityArchitecture": "Разделение Полномочий",
        "vault.masterPasskeyBadge": "Владелец: FIDO2 Passkey (P-256)",
        "vault.subAgentBadge": "Субагенты: Эфемерный Ed25519",
        "vault.wireSpecBadge": "Стандарт CapLeaf v1 (223 Байта LE)"
    },
    "kk": {
        "vault.heartbeatSession": "Heartbeat сессиясы (valid_until)",
        "vault.touchPasskey": "Ұзарту үшін Passkey басыңыз (+1сағ)",
        "vault.timeToControl": "Бақылау реакция уақыты (τ)",
        "vault.maxTheftCeiling": "Максималды шығын шегі E_theft(τ)",
        "vault.authorityArchitecture": "Өкілеттіктерді ажырату",
        "vault.masterPasskeyBadge": "Бас иесі: FIDO2 Passkey (P-256)",
        "vault.subAgentBadge": "Қосымша агенттер: Уақытша Ed25519",
        "vault.wireSpecBadge": "CapLeaf v1 стандарты (223 Байт LE)"
    },
    "hi": {
        "vault.heartbeatSession": "हार्टबीट सत्र (valid_until)",
        "vault.touchPasskey": "नवीनीकरण के लिए पासकी स्पर्श करें (+1 घंटा)",
        "vault.timeToControl": "नियंत्रण प्रतिक्रिया समय (τ)",
        "vault.maxTheftCeiling": "अधिकतम संभावित क्षति सीमा E_theft(τ)",
        "vault.authorityArchitecture": "प्राधिकरण पृथक्करण",
        "vault.masterPasskeyBadge": "मास्टर: FIDO2 पासकी (P-256)",
        "vault.subAgentBadge": "उप-एजेंट: अल्पकालिक Ed25519",
        "vault.wireSpecBadge": "CapLeaf v1 मानक (223 बाइट्स LE)"
    },
    "he": {
        "vault.heartbeatSession": "סשן פעימות דופק (valid_until)",
        "vault.touchPasskey": "גע ב-Passkey להארכה (+1 שעה)",
        "vault.timeToControl": "זמן תגובת שליטה (τ)",
        "vault.maxTheftCeiling": "תקרת הפסד מקסימלית E_theft(τ)",
        "vault.authorityArchitecture": "הפרדת סמכויות",
        "vault.masterPasskeyBadge": "מאסטר: FIDO2 Passkey (P-256)",
        "vault.subAgentBadge": "תת-סוכנים: Ed25519 זמני",
        "vault.wireSpecBadge": "תקן CapLeaf v1 (223 בתים LE)"
    }
}

for filepath in ['i18n.js', 'app/i18n.js']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # For each language in new_keys_map, locate its block and insert the new keys right after "vault.velocityCap": "..."
    for lang, keys_dict in new_keys_map.items():
        pattern = re.compile(rf'("{re.escape(lang)}":\s*\{{[^}}]*"vault\.velocityCap":\s*"[^"]*",?)', re.MULTILINE)
        m = pattern.search(content)
        if m:
            matched_str = m.group(1)
            # Build injection string
            inj_lines = []
            for k, v in keys_dict.items():
                if f'"{k}":' not in content[m.start():m.start()+2500]:
                    inj_lines.append(f'    "{k}": "{v}",')
            if inj_lines:
                replacement = matched_str + "\n" + "\n".join(inj_lines)
                content = content[:m.start()] + replacement + content[m.end():]
                print(f"Updated {filepath} for {lang}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished updating i18n files.")
