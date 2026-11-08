#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_all_whitepapers.py - Phase 2
Completes updates for all 10 HAICHAIN whitepaper markdown files:
1. Voucher formula replacement by matching line with 'CumulativeAmount'
2. Refined invariant introductions across EN, ES, FR, HE, HI, KK, RU
3. HE Section 6.6 insertion
"""

import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

FORMULA_REPLACEMENTS = {
    'VI': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   Trong đó:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: Chuỗi định danh phân tách miền chuẩn giao thức (`\"haichain-v1-channel-settlement\"`).\n"
        "   * $\\text{ClusterID}$: Định danh cụm mạng (Devnet, Testnet, Mainnet-Beta), triệt tiêu 100% rủi ro tấn công phát lại chữ ký xuyên môi trường (Cross-Cluster Replay Attack).\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Ràng buộc chính xác địa chỉ hợp đồng lõi và Kho quỹ PDA của Agent, ngăn chặn tái sử dụng chữ ký trên các hợp đồng fork hoặc hũ tiền khác.\n"
        "   * $\\text{ProviderPubkey}$: Địa chỉ ví công khai của Nhà cung cấp dịch vụ được ủy quyền trong phiên, vô hiệu hóa việc chuyển nhượng vé trái phép cho bên thứ ba.\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Khóa phiên duy nhất, số thứ tự đơn điệu tăng dần ($k$) và số tiền tích lũy lũy tiến, đảm bảo quyết toán gom một vé duy nhất an toàn tuyệt đối.\n"
    ),
    'EN': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   Where:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: Protocol-level cryptographic domain tag (`\"haichain-v1-channel-settlement\"`).\n"
        "   * $\\text{ClusterID}$: Solana cluster identifier (Devnet, Testnet, Mainnet-Beta), mathematically eliminating cross-network signature replay vulnerabilities.\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Cryptographically anchors the voucher to the specific deployed program and the agent's isolated vault account.\n"
        "   * $\\text{ProviderPubkey}$: Public key of the whitelisted service provider for the active session, preventing unauthorized secondary transfer of payment vouchers.\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Monotonically increasing tick counter ($k$) and cumulative spend under a unique session ID, enabling single-voucher settlement with sub-5ms latency and zero reasoning stalls.\n"
    ),
    'ES': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   Donde:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: Etiqueta criptográfica de separación de dominio del protocolo (`\"haichain-v1-channel-settlement\"`).\n"
        "   * $\\text{ClusterID}$: Identificador del clúster de Solana (Devnet, Testnet, Mainnet-Beta), eliminando repeticiones entre redes.\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Vincula la firma al programa exacto y a la bóveda aislada del agente.\n"
        "   * $\\text{ProviderPubkey}$: Clave pública del proveedor autorizado para la sesión activa, impidiendo transferencias no autorizadas.\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Contador monótono ($k$) y gasto acumulado con liquidación única en menos de 5ms.\n"
    ),
    'FR': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   Où:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: Balise cryptographique de séparation de domaine du protocole (`\"haichain-v1-channel-settlement\"`).\n"
        "   * $\\text{ClusterID}$: Identifiant de cluster Solana (Devnet, Testnet, Mainnet-Beta), éliminant tout rejeu trans-réseau.\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Lie le bon au programme précis et au coffre PDA isolé de l'agent.\n"
        "   * $\\text{ProviderPubkey}$: Clé publique du prestataire autorisé pour la session, empêchant tout transfert illicite du bon.\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Compteur monotone ($k$) et montant cumulé assurant un règlement unique sous 5ms.\n"
    ),
    'KO': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   매개변수 정의:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: 프로토콜 레벨 암호학적 도메인 분리 태그 (`\"haichain-v1-channel-settlement\"`).\n"
        "   * $\\text{ClusterID}$: Solana 클러스터 식별자 (Devnet, Testnet, Mainnet-Beta), 환경 간 서명 재전송(Replay) 공격 완전 차단.\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: 배포된 프로그램 및 에이전트의 격리된 볼트 PDA 계정에 바인딩.\n"
        "   * $\\text{ProviderPubkey}$: 활성 세션의 인가된 공급자 공개키, 바우처 제3자 무단 양도 방지.\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: 단조 증가 틱 번호($k$) 및 누적 지출액 기반 5ms 미만 단일 바우처 최종 정산.\n"
    ),
    'ZH': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   参数说明:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: 协议级密码学域分离标识 (`\"haichain-v1-channel-settlement\"`)。\n"
        "   * $\\text{ClusterID}$: Solana 集群标识符 (Devnet, Testnet, Mainnet-Beta)，杜绝跨网络签名重放攻击。\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: 锚定部署的程序和智能体隔离的金库 PDA 账户。\n"
        "   * $\\text{ProviderPubkey}$: 当前会话指定合法服务商公钥，严禁凭单非法向第三方转让。\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: 严格单调递增序号($k$)与累计消费额，支持 < 5ms 单张终局清算。\n"
    ),
    'RU': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   Где:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: Протокольный криптографический тег разделения доменов (`\"haichain-v1-channel-settlement\"`).\n"
        "   * $\\text{ClusterID}$: Идентификатор кластера Solana (Devnet, Testnet, Mainnet-Beta), исключающий повторное использование подписей.\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Привязка чека к смарт-контракту и изолированному PDA-хранилищу агента.\n"
        "   * $\\text{ProviderPubkey}$: Публичный ключ авторизованного поставщика в сессии, предотвращающий передачу чека третьим лицам.\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Монотонный счетчик ($k$) и сумма для итогового расчета быстрее 5 мс.\n"
    ),
    'HE': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   הגדרת פרמטרים:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: תג הצפנה ברמת הפרוטוקול להפרדת תחומים (`\"haichain-v1-channel-settlement\"`).\n"
        "   * $\\text{ClusterID}$: מזהה אשכול Solana (Devnet, Testnet, Mainnet-Beta), מונע התקפות שידור חוזר.\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: מעגן את השובר לתוכנית ולחשבון כספת ה-PDA של הסוכן.\n"
        "   * $\\text{ProviderPubkey}$: מפתח ציבורי של הספק המורשה בהפעלה, מונע העברה בלתי-מורשית לצד שלישי.\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: מונה מונוטוני ($k$) וסכום מצטבר לסילוק סופי בפחות מ-5ms.\n"
    ),
    'HI': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   जहाँ:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: प्रोटोकॉल-स्तरीय क्रिप्टोग्राफिक डोमेन सेपरेशन टैग (`\"haichain-v1-channel-settlement\"`)।\n"
        "   * $\\text{ClusterID}$: सोलाना क्लस्टर पहचानकर्ता (Devnet, Testnet, Mainnet-Beta), जो क्रॉस-नेटवर्क रीप्ले जोखिम को समाप्त करता है।\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: विशिष्ट प्रोग्राम और एजेंट के अलग वॉल्ट पीडीए खाते से बांधता है।\n"
        "   * $\\text{ProviderPubkey}$: सक्रिय सत्र के अधिकृत सेवा प्रदाता की सार्वजनिक कुंजी, जो अनधिकृत हस्तांतरण को रोकती है।\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: 5ms से कम समय में अंतिम निपटान सुनिश्चित करने वाला मोनोटोनिक काउंटर ($k$)।\n"
    ),
    'KK': (
        "   $$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
        "   Мұнда:\n"
        "   * $\\text{DOMAIN\\_SEPARATOR}$: Хаттама деңгейіндегі доменді бөлу криптографиялық тегі (`\"haichain-v1-channel-settlement\"`).\n"
        "   * $\\text{ClusterID}$: Solana кластер идентификаторы (Devnet, Testnet, Mainnet-Beta), желіаралық қайталау қаупін жояды.\n"
        "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Чекті бағдарламаға және агенттің оқшауланған PDA қоймасына байлайды.\n"
        "   * $\\text{ProviderPubkey}$: Сессияның өкілетті провайдерінің ашық кілті, чектің заңсыз берілуіне жол бермейді.\n"
        "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: 5 мс-ден аз уақытта түпкілікті есеп айырысуды қамтамасыз ететін есептегіш ($k$).\n"
    )
}

INVARIANT_EXACT_REPLACEMENTS = {
    'EN': (
        'The smart contract kernel (`haichain-core v6.9.3`) is formally verified and hardened against historic exploits exceeding \\$800,000,000 across decentralized finance:\n',
        'The smart contract kernel (`haichain-core v6.9.3`) implements a **Deterministic Multi-Layer Defense-in-Depth** architecture, enforcing 6 mathematical runtime invariants designed to neutralize critical state vulnerabilities and historic exploit vectors totaling over \\$821 million in losses. Combined with scheduled independent third-party security audits from premier Web3 auditing firms, this deterministic boundary guarantees zero unvetted contract execution:\n'
    ),
    'ES': (
        'El núcleo de contratos inteligentes (`haichain-core v6.9.3`) está verificado formalmente y blindado contra exploits históricos que superan los \\$800.000.000 en finanzas descentralizadas:\n',
        'El núcleo de contratos inteligentes (`haichain-core v6.9.3`) implementa una arquitectura de **Defensa en Profundidad Determinista Multicapa (Deterministic Multi-Layer Defense-in-Depth)**, aplicando 6 invariantes matemáticas en tiempo de ejecución para neutralizar vulnerabilidades de estado y vectores de ataque históricos por más de \\$821 millones. Combinado con auditorías de seguridad independientes programadas de primer nivel, elimina cualquier brecha de ejecución:\n'
    ),
    'FR': (
        'Le noyau de contrats intelligents (`haichain-core v6.9.3`) est formellement vérifié et immunisé contre les attaques historiques ayant coûté plus de \\$800.000.000 dans la finance décentralisée:\n',
        'Le noyau de contrats intelligents (`haichain-core v6.9.3`) met en œuvre une architecture de **Défense en Profondeur Déterministe Multicouche (Deterministic Multi-Layer Defense-in-Depth)**, appliquant 6 invariants mathématiques d\'exécution pour neutraliser les vulnérabilités d\'état et les exploits historiques totalisant plus de \\$821 millions. Associée à un programme d\'audits de sécurité indépendants tiers réguliers, elle garantit l\'intégrité absolue des flux:\n'
    ),
    'HE': (
        'ליבת החוזים החכמים (`haichain-core v6.9.3`) עברה אימות פורמלי והוקשחה נגד מתקפות עבר היסטוריות שהיקפן המצטבר עלה על 800,000,000 דולר ברחבי עולם הפיננסים המבוזרים (DeFi):\n',
        'ליבת החוזים החכמים (`haichain-core v6.9.3`) מיישמת ארכיטקטורת **הגנה לעומק דטרמיניסטית רב-שכבתית (Deterministic Multi-Layer Defense-in-Depth)**, האוכפת 6 אינווריאנטים מתמטיים בזמן ריצה כדי לנטרל מחלקות פגיעות עבר בהיקף של למעלה מ-821 מיליון דולר. בשילוב ביקורות אבטחה חיצוניות בלתי תלויות קבועות, המערכת מבטלת לחלוטין כשלי היגיון בחוזים:\n'
    ),
    'RU': (
        'Ядро смарт-контрактов (`haichain-core v6.9.3`) формально верифицировано и защищено от исторических уязвимостей, стоивших индустрии децентрализованных финансов более \\$800 000 000:\n',
        'Ядро смарт-контрактов (`haichain-core v6.9.3`) реализует архитектуру **Детерминированной многоуровневой глубокой защиты (Deterministic Multi-Layer Defense-in-Depth)**, обеспечивая исполнение 6 математических инвариантов во время выполнения для предотвращения классов уязвимостей и исторических эксплойтов на сумму более \\$821 млн. В сочетании с регулярными независимыми сторонними аудитами безопасности это устраняет любые логические дефекты:\n'
    ),
    'HI': (
        'Ядро смарт-контрактов (`haichain-core v6.9.3`) формально верифицировано и защищено от исторических уязвимостей, стоивших индустрии децентрализованных финансов более \\$800 000 000:\n',
        'स्मार्ट अनुबंध कर्नेल (`haichain-core v6.9.3`) **नियत बहुस्तरीय गहन सुरक्षा (Deterministic Multi-Layer Defense-in-Depth)** वास्तुकला को लागू करता है, जो $821 मिलियन से अधिक के ऐतिहासिक शोषण को बेअसर करने के लिए 6 गणितीय इनवेरिएंट्स को लागू करता है। अनुसूचित तृतीय-पक्ष सुरक्षा ऑडिट के साथ मिलकर यह अनुबंध तर्क दोषों को समाप्त करता है:\n'
    ),
    'KK': (
        'Ядро смарт-келісімшартов (`haichain-core v6.9.3`) формально верифицировано и защищено от исторических уязвимостей, стоивших индустрии децентрализованных финансов более \\$800 000 000:\n',
        'Смарт-келісімшарт ядросы (`haichain-core v6.9.3`) **Детерминирленген көпдеңгейлі терең қорғаныс (Deterministic Multi-Layer Defense-in-Depth)** архитектурасын қолданады, бұл $821 миллионнан астам тарихи шабуылдарды залалсыздандыру үшін 6 математикалық инвариантты орындайды. Тұрақты тәуелсіз үшінші тарап қауіпсіздік аудитімен бірге бұл келісімшарт логикалық кемшіліктерін жояды:\n'
    )
}

HE_SECTION_6_6 = (
    "\n### 6.6. מיצוב אסטרטגי: HAICHAIN כשכבת מדיניות ומפסקי זרם עבור HTTP x402 ו-Solana Pay.sh\n\n"
    "בנוף תשתיות הסוכנים האוטונומיים, פרוטוקולי תשלום פתוחים זכו לאימוץ מוסדי מהיר, בעיקר **HTTP x402** (ביוזמת Coinbase, הועבר לקרן Linux בהשתתפות Visa ו-Mastercard) ו-**Pay.sh** (הושק במשותף על ידי קרן Solana ו-Google Cloud במאי 2026).\n\n"
    "```\n"
    "         ערימת התשתית הפיננסית העולמית לסוכנים אוטונומיים\n"
    "         \n"
    "    [ סוכנים ונחילי בינה ]       : Claude Desktop, Cursor, ElizaOS, CrewAI\n"
    "                                   │\n"
    "                                   ▼\n"
    "    [ תקשורת וחיובים ]           : מפרט HTTP x402 ופרוקסי Pay.sh\n"
    "    (מחזיר 402 Payment Required ומעביר אתגרי תשלום מוצפנים)\n"
    "                                   │\n"
    "                                   ▼\n"
    "    [ מדיניות וניהול סיכונים ]   : ★ HAICHAIN AGENT POLICY VAULT ★\n"
    "    (עצי יכולות Merkle, תקרות MaxSpend קשיחות, מפסק פאניקה < 1s)\n"
    "                                   │\n"
    "                                   ▼\n"
    "    [ מסילות סילוק בשרשרת ]      : פנקס Solana L1 (סילוק USDC / USDT SPL)\n"
    "```\n\n"
    "1. **חלוקת תפקידים ברורה (סינרגיה משלימה):**\n"
    "   * **x402 ו-Pay.sh משמשים כ'צינורות תקשורת':** מגדירים כיצד ממשקי API מחזירים `402 Payment Required` וכיצד מועברות הרשאות (`X-402-Authorization`).\n"
    "   * **HAICHAIN משמש כ'בנק סיכונים וכספת מדיניות':** פותר את השאלות הקריטיות: *מאיפה הסוכן משיג כסף? מי מגביל הוצאות? כיצד עוצרים מודל שהותקף מריקון החשבון?*\n"
    "2. **נטרול פגיעויות מעשיות של x402:**\n"
    "   HAICHAIN פותרת את היעדר תקרות ברירת המחדל באמצעות **עלה יכולות Merkle בן 4 רכיבים** (`Pubkey || MaxSpend || ExpirySlot || Nonce`) ומשפט ההפסד החסום.\n"
    "3. **אינטגרציה חלקה עם SDK:**\n"
    "   חבילת `@haichain/sdk` כוללת מטפלים מובנים לפתרון מאובטח של אתגרי x402.\n\n"
    "---\n"
)

def process_file(filepath):
    filename = os.path.basename(filepath)
    m = re.search(r'V1\.0_([A-Z]{2})\.md', filename)
    if not m:
        return
    lang = m.group(1)

    with open(filepath, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()

    modified = False
    new_lines = []

    for line in lines:
        if 'CumulativeAmount' in line and ('Voucher' in line or 'Sign' in line):
            if 'DOMAIN_SEPARATOR' not in line:
                new_lines.append(FORMULA_REPLACEMENTS[lang])
                modified = True
                print(f"[{lang}] Successfully replaced Voucher formula line")
                continue
        new_lines.append(line)

    content = "".join(new_lines)

    # Invariants replacement
    if lang in INVARIANT_EXACT_REPLACEMENTS:
        old_str, new_str = INVARIANT_EXACT_REPLACEMENTS[lang]
        if old_str in content:
            content = content.replace(old_str, new_str)
            modified = True
            print(f"[{lang}] Successfully replaced Invariant introduction")
        else:
            print(f"[{lang}] Invariant string not found or already replaced")

    # HE Section 6.6 insertion
    if lang == 'HE' and '### 6.6.' not in content:
        he_anchor = "## 7. קיזוז סימטרי"
        pos = content.find(he_anchor)
        if pos != -1:
            # find previous '---'
            dash_pos = content.rfind('---', 0, pos)
            if dash_pos != -1:
                content = content[:dash_pos] + HE_SECTION_6_6 + content[dash_pos + 3:]
                modified = True
                print(f"[{lang}] Successfully inserted Section 6.6 in Hebrew")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as fp:
            fp.write(content)
        print(f"[{lang}] Saved {filename}")
    else:
        print(f"[{lang}] No additional changes")

def main():
    import glob
    files = sorted(glob.glob('HAICHAIN_WHITEPAPER*.md'))
    for f in files:
        process_file(f)

if __name__ == '__main__':
    main()
