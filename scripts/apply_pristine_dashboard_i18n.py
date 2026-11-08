import re

# Dictionaries
i18n_keys = {
    'en': {'aiHub.close': 'Close', 'account.syncBrowser': 'Sync to Chrome Browser'},
    'vi': {'aiHub.close': 'Đóng', 'account.syncBrowser': 'Đồng bộ sang trình duyệt Chrome'},
    'zh': {'aiHub.close': '关闭', 'account.syncBrowser': '同步至 Chrome 浏览器'},
    'ko': {'aiHub.close': '닫기', 'account.syncBrowser': 'Chrome 브라우저로 동기화'},
    'fr': {'aiHub.close': 'Fermer', 'account.syncBrowser': 'Synchroniser vers Chrome'},
    'es': {'aiHub.close': 'Cerrar', 'account.syncBrowser': 'Sincronizar con navegador Chrome'},
    'ru': {'aiHub.close': 'Закрыть', 'account.syncBrowser': 'Синхронизировать с браузером Chrome'},
    'kk': {'aiHub.close': 'Жабу', 'account.syncBrowser': 'Chrome браузеріне синхрондау'},
    'hi': {'aiHub.close': 'बंद करें', 'account.syncBrowser': 'Chrome ब्राउज़र में सिंक करें'},
    'he': {'aiHub.close': 'סגור', 'account.syncBrowser': 'סנכרן לדפדפן Chrome'}
}

vesting_breakdown = {
    'en': '20% TGE + 80% Linear 6M',
    'vi': '20% TGE + 80% Tuyến Tính 6T',
    'zh': '20% TGE + 80% 6个月线性释放',
    'ko': '20% TGE + 80% 6개월 선형 분배',
    'fr': '20% TGE + 80% Linéaire 6 Mois',
    'es': '20% TGE + 80% Lineal 6 Meses',
    'ru': '20% TGE + 80% Линейный 6 Мес',
    'kk': '20% TGE + 80% Сызықтық 6 Ай',
    'hi': '20% TGE + 80% रैखिक 6 माह',
    'he': '20% TGE + 80% לינארי 6 חודשים'
}

dash_new_keys = {
    'en': {
        'cmdCopied': '✓ Command copied!',
        'cmdCopyBtn': 'Copy 1-Click Install Command',
        'cmdCopyToastMsg': 'Paste into Terminal/PowerShell to install automatically',
        'linkCopied': '✓ Link copied!',
        'linkCopyBtn': 'Copy Remote MCP URL',
        'linkCopyToastMsg': 'Paste into Settings -> Connectors on claude.ai',
        'aiPlaygroundToast': 'Direct AI inference via Web3 smart contract',
        'copiedToastTitle': 'Copied!',
        'installCmdToastTitle': 'Install Command:',
        'connectWalletFailed': 'Could not connect wallet',
        'signedAuthPrefix': 'Signed Auth:',
        'walletDisconnectedTitle': 'Wallet Disconnected',
        'sessionTerminatedMsg': 'Session terminated successfully',
        'customWalletConnectedTitle': 'Custom Wallet Connected',
        'biometricDecryptError': 'Could not decrypt existing biometric vault. The system refused to overwrite your key to protect existing vault funds. Please re-authenticate on the original device.',
        'confirmResetBtn': 'Reset',
        'cancelBtn': 'Cancel'
    },
    'vi': {
        'cmdCopied': '✓ Đã sao chép lệnh!',
        'cmdCopyBtn': 'Sao chép lệnh cài đặt 1-Click',
        'cmdCopyToastMsg': 'Dán vào Terminal/PowerShell để cài đặt tự động',
        'linkCopied': '✓ Đã sao chép link!',
        'linkCopyBtn': 'Sao chép đường dẫn Remote MCP',
        'linkCopyToastMsg': 'Dán vào Settings -> Connectors trên claude.ai',
        'aiPlaygroundToast': 'Trải nghiệm suy luận AI trực tiếp qua Web3',
        'copiedToastTitle': 'Đã sao chép!',
        'installCmdToastTitle': 'Lệnh cài đặt:',
        'connectWalletFailed': 'Không thể kết nối ví',
        'signedAuthPrefix': 'Ký xác thực:',
        'walletDisconnectedTitle': 'Đã Ngắt Kết Nối',
        'sessionTerminatedMsg': 'Đã thoát phiên làm việc an toàn',
        'customWalletConnectedTitle': 'Đã Kết Nối Ví Custom',
        'biometricDecryptError': 'Không thể giải mã Vault sinh trắc học hiện tại. Hệ thống từ chối tạo khóa mới để bảo vệ an toàn số dư đang có trong Vault của bạn. Vui lòng quét lại FaceID trên đúng thiết bị ban đầu.',
        'confirmResetBtn': 'Đặt lại',
        'cancelBtn': 'Huỷ'
    },
    'zh': {
        'cmdCopied': '✓ 命令已复制！',
        'cmdCopyBtn': '复制 1-Click 安装命令',
        'cmdCopyToastMsg': '粘贴到 Terminal/PowerShell 即可自动安装',
        'linkCopied': '✓ 链接已复制！',
        'linkCopyBtn': '复制 Remote MCP 链接',
        'linkCopyToastMsg': '粘贴到 claude.ai 的 Settings -> Connectors',
        'aiPlaygroundToast': '通过 Web3 直接体验 AI 推理',
        'copiedToastTitle': '已复制！',
        'installCmdToastTitle': '安装命令：',
        'connectWalletFailed': '无法连接钱包',
        'signedAuthPrefix': '签名验证：',
        'walletDisconnectedTitle': '钱包已断开',
        'sessionTerminatedMsg': '会话已安全退出',
        'customWalletConnectedTitle': '自定义钱包已连接',
        'biometricDecryptError': '无法解密现有的生物识别 Vault。系统已拒绝覆盖您的密钥以保护金库中的现有资金。请在原始设备上重新进行身份验证。',
        'confirmResetBtn': '重置',
        'cancelBtn': '取消'
    },
    'ko': {
        'cmdCopied': '✓ 명령어가 복사되었습니다!',
        'cmdCopyBtn': '1-Click 설치 명령어 복사',
        'cmdCopyToastMsg': '터미널/PowerShell에 붙여넣어 자동 설치하세요',
        'linkCopied': '✓ 링크가 복사되었습니다!',
        'linkCopyBtn': 'Remote MCP URL 복사',
        'linkCopyToastMsg': 'claude.ai의 Settings -> Connectors에 붙여넣으세요',
        'aiPlaygroundToast': 'Web3를 통한 실시간 AI 추론 경험',
        'copiedToastTitle': '복사 완료!',
        'installCmdToastTitle': '설치 명령어:',
        'connectWalletFailed': '지갑을 연결할 수 없습니다',
        'signedAuthPrefix': '서명 인증:',
        'walletDisconnectedTitle': '지갑 연결 해제됨',
        'sessionTerminatedMsg': '세션이 안전하게 종료되었습니다',
        'customWalletConnectedTitle': '커스텀 지갑 연결됨',
        'biometricDecryptError': '기존 생체 인식 Vault를 복호화할 수 없습니다. 금고의 기존 자금을 보호하기 위해 키 덮어쓰기가 거부되었습니다. 원래 기기에서 다시 인증해 주세요.',
        'confirmResetBtn': '재설정',
        'cancelBtn': '취소'
    },
    'fr': {
        'cmdCopied': '✓ Commande copiée !',
        'cmdCopyBtn': 'Copier la commande d\'installation 1-Click',
        'cmdCopyToastMsg': 'Collez dans le Terminal/PowerShell pour installer automatiquement',
        'linkCopied': '✓ Lien copié !',
        'linkCopyBtn': 'Copier l\'URL Remote MCP',
        'linkCopyToastMsg': 'Collez dans Paramètres -> Connecteurs sur claude.ai',
        'aiPlaygroundToast': 'Inférence IA directe via Web3',
        'copiedToastTitle': 'Copié !',
        'installCmdToastTitle': 'Commande d\'installation :',
        'connectWalletFailed': 'Impossible de connecter le portefeuille',
        'signedAuthPrefix': 'Auth signée :',
        'walletDisconnectedTitle': 'Portefeuille Déconnecté',
        'sessionTerminatedMsg': 'Session terminée avec succès',
        'customWalletConnectedTitle': 'Portefeuille Personnalisé Connecté',
        'biometricDecryptError': 'Impossible de déchiffrer le coffre biométrique existant. Le système a refusé d\'écraser votre clé pour protéger les fonds existants. Veuillez vous réauthentifier sur l\'appareil d\'origine.',
        'confirmResetBtn': 'Réinitialiser',
        'cancelBtn': 'Annuler'
    },
    'es': {
        'cmdCopied': '✓ ¡Comando copiado!',
        'cmdCopyBtn': 'Copiar comando de instalación 1-Click',
        'cmdCopyToastMsg': 'Pegue en Terminal/PowerShell para instalar automáticamente',
        'linkCopied': '✓ ¡Enlace copiado!',
        'linkCopyBtn': 'Copiar URL de Remote MCP',
        'linkCopyToastMsg': 'Pegue en Configuración -> Conectores en claude.ai',
        'aiPlaygroundToast': 'Inferencia de IA directa a través de Web3',
        'copiedToastTitle': '¡Copiado!',
        'installCmdToastTitle': 'Comando de instalación:',
        'connectWalletFailed': 'No se pudo conectar la billetera',
        'signedAuthPrefix': 'Autenticación firmada:',
        'walletDisconnectedTitle': 'Billetera Desconectada',
        'sessionTerminatedMsg': 'Sesión finalizada de forma segura',
        'customWalletConnectedTitle': 'Billetera Personalizada Conectada',
        'biometricDecryptError': 'No se pudo descifrar la bóveda biométrica existente. El sistema rechazó sobrescribir su clave para proteger los fondos existentes. Vuelva a autenticarse en el dispositivo original.',
        'confirmResetBtn': 'Restablecer',
        'cancelBtn': 'Cancelar'
    },
    'ru': {
        'cmdCopied': '✓ Команда скопирована!',
        'cmdCopyBtn': 'Скопировать команду установки 1-Click',
        'cmdCopyToastMsg': 'Вставьте в Terminal/PowerShell для автоматической установки',
        'linkCopied': '✓ Ссылка скопирована!',
        'linkCopyBtn': 'Скопировать URL Remote MCP',
        'linkCopyToastMsg': 'Вставьте в Настройки -> Коннекторы на claude.ai',
        'aiPlaygroundToast': 'Прямой вывод ИИ через Web3',
        'copiedToastTitle': 'Скопировано!',
        'installCmdToastTitle': 'Команда установки:',
        'connectWalletFailed': 'Не удалось подключить кошелек',
        'signedAuthPrefix': 'Подписанная аутентификация:',
        'walletDisconnectedTitle': 'Кошелек Отключен',
        'sessionTerminatedMsg': 'Сессия успешно завершена',
        'customWalletConnectedTitle': 'Пользовательский Кошелек Подключен',
        'biometricDecryptError': 'Не удалось расшифровать существующее биометрическое хранилище. Система отказалась перезаписывать ваш ключ для защиты средств в хранилище. Повторите аутентификацию на исходном устройстве.',
        'confirmResetBtn': 'Сброс',
        'cancelBtn': 'Отмена'
    },
    'kk': {
        'cmdCopied': '✓ Пәрмен көшірілді!',
        'cmdCopyBtn': '1-Click Орнату Пәрменін Көшіру',
        'cmdCopyToastMsg': 'Автоматты орнату үшін Terminal/PowerShell-ге қойыңыз',
        'linkCopied': '✓ Сілтеме көшірілді!',
        'linkCopyBtn': 'Қашықтағы MCP URL Көшіру',
        'linkCopyToastMsg': 'claude.ai сайтындағы Параметрлер -> Қосқыштар бөліміне қойыңыз',
        'aiPlaygroundToast': 'Web3 арқылы тікелей AI қорытындысы',
        'copiedToastTitle': 'Көшірілді!',
        'installCmdToastTitle': 'Орнату пәрмені:',
        'connectWalletFailed': 'Әмиянды қосу мүмкін болмады',
        'signedAuthPrefix': 'Қол қойылған аутентификация:',
        'walletDisconnectedTitle': 'Әмиян ажыратылды',
        'sessionTerminatedMsg': 'Сессия сәтті аяқталды',
        'customWalletConnectedTitle': 'Арнайы әмиян қосылды',
        'biometricDecryptError': 'Бар биометриялық сейфтің шифрын ашу мүмкін болмады. Жүйе сейфтегі қаражатты қорғау үшін кілтіңізді қайта жазудан бас тартты. Бастапқы құрылғыда қайта растаңыз.',
        'confirmResetBtn': 'Қалпына келтіру',
        'cancelBtn': 'Бас тарту'
    },
    'hi': {
        'cmdCopied': '✓ कमांड कॉपी हो गई!',
        'cmdCopyBtn': '1-Click इंस्टॉल कमांड कॉपी करें',
        'cmdCopyToastMsg': 'स्वचालित रूप से इंस्टॉल करने के लिए Terminal/PowerShell में पेस्ट करें',
        'linkCopied': '✓ लिंक कॉपी हो गया!',
        'linkCopyBtn': 'रिमोट MCP URL कॉपी करें',
        'linkCopyToastMsg': 'claude.ai पर सेटिंग्स -> कनेक्टर्स में पेस्ट करें',
        'aiPlaygroundToast': 'Web3 के माध्यम से प्रत्यक्ष AI अनुमान',
        'copiedToastTitle': 'कॉपी हो गया!',
        'installCmdToastTitle': 'इंस्टॉल कमांड:',
        'connectWalletFailed': 'वॉलेट कनेक्ट नहीं हो सका',
        'signedAuthPrefix': 'हस्ताक्षरित प्रमाणीकरण:',
        'walletDisconnectedTitle': 'वॉलेट डिस्कनेक्ट हो गया',
        'sessionTerminatedMsg': 'सत्र सफलतापूर्वक समाप्त हुआ',
        'customWalletConnectedTitle': 'कस्टम वॉलेट कनेक्ट हो गया',
        'biometricDecryptError': 'मौजूदा बायोमेट्रिक वॉल्ट को डिक्रिप्ट नहीं किया जा सका। सिस्टम ने वॉल्ट फंड की सुरक्षा के लिए कुंजी को ओवरराइट करने से मना कर दिया। कृपया मूल डिवाइस पर पुनः प्रमाणीकरण करें।',
        'confirmResetBtn': 'रीसेट करें',
        'cancelBtn': 'रद्द करें'
    },
    'he': {
        'cmdCopied': '✓ הפקודה הועתקה!',
        'cmdCopyBtn': 'העתק פקודת התקנה בלחיצה אחת',
        'cmdCopyToastMsg': 'הדבק ב-Terminal/PowerShell להתקנה אוטומטית',
        'linkCopied': '✓ הקישור הועתק!',
        'linkCopyBtn': 'העתק כתובת Remote MCP',
        'linkCopyToastMsg': 'הדבק בהגדרות -> מחברים ב-claude.ai',
        'aiPlaygroundToast': 'הסקת בינה מלאכותית ישירה דרך Web3',
        'copiedToastTitle': 'הועתק!',
        'installCmdToastTitle': 'פקודת התקנה:',
        'connectWalletFailed': 'לא ניתן לחבר את הארנק',
        'signedAuthPrefix': 'אימות חתום:',
        'walletDisconnectedTitle': 'הארנק נותק',
        'sessionTerminatedMsg': 'ההפעלה הסתיימה בהצלחה',
        'customWalletConnectedTitle': 'ארנק מותאם אישית מחובר',
        'biometricDecryptError': 'לא ניתן לפענח את הכספת הביומטרית הקיימת. המערכת סירבה לדרוס את המפתח שלך כדי להגן על הכספים הקיימים. אנא בצע אימות מחדש במכשיר המקורי.',
        'confirmResetBtn': 'איפוס',
        'cancelBtn': 'ביטול'
    }
}

def patch_i18n(file_path):
    print(f"\n--- Patching {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for lang in ['kk', 'en', 'zh', 'fr', 'ko', 'es', 'ru', 'vi', 'hi', 'he']:
        keys = i18n_keys.get(lang, {})
        m = re.search(rf'"{lang}":\s*\{{\s*\n', content)
        if not m:
            print(f"ERROR: Lang {lang} not found in {file_path}")
            continue
        
        pos = m.end()
        injection = ""
        for k, v in keys.items():
            if f'"{k}"' not in content:
                v_esc = v.replace('\\', '\\\\').replace('"', '\\"')
                injection += f'    "{k}": "{v_esc}",\n'
        
        if injection:
            content = content[:pos] + injection + content[pos:]
            print(f"  Inserted keys into '{lang}'")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

def patch_dashboard(file_path):
    print(f"\n--- Patching {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # 1. Patch VESTING_VAULT_I18N
    v_start = content.find('const VESTING_VAULT_I18N = {')
    v_end = content.find('const DASH_NOTICES_I18N = {')
    if v_start == -1 or v_end == -1:
        print("ERROR: VESTING_VAULT_I18N boundaries not found")
        return
    
    vesting_block = content[v_start:v_end]
    for lang in ['en', 'vi', 'zh', 'ko', 'fr', 'es', 'ru', 'kk', 'hi', 'he']:
        val = vesting_breakdown.get(lang, '')
        val_esc = val.replace('\\', '\\\\').replace('"', '\\"')
        m = re.search(rf'"{lang}":\s*\{{\s*\n', vesting_block)
        if m and '"guaranteeVestingBreakdown"' not in vesting_block[m.start():m.start()+200]:
            pos = m.end()
            line = f'    "guaranteeVestingBreakdown": "{val_esc}",\n'
            vesting_block = vesting_block[:pos] + line + vesting_block[pos:]
            print(f"  Added guaranteeVestingBreakdown to VESTING_VAULT_I18N['{lang}']")

    content = content[:v_start] + vesting_block + content[v_end:]

    # 2. Patch DASH_NOTICES_I18N
    d_start = content.find('const DASH_NOTICES_I18N = {')
    d_end = content.find('function getDashNotice(key) {')
    if d_start == -1 or d_end == -1:
        print("ERROR: DASH_NOTICES_I18N boundaries not found")
        return

    dash_block = content[d_start:d_end]
    for lang in ['kk', 'en', 'zh', 'vi', 'ko', 'fr', 'es', 'ru', 'hi', 'he']:
        keys = dash_new_keys.get(lang, {})
        m = re.search(rf'"{lang}":\s*\{{\s*\n', dash_block)
        if m:
            pos = m.end()
            injection = ""
            for k, v in keys.items():
                if f'"{k}"' not in dash_block[m.start():m.start()+2500]:
                    v_esc = v.replace('\\', '\\\\').replace('"', '\\"')
                    injection += f'    "{k}": "{v_esc}",\n'
            if injection:
                dash_block = dash_block[:pos] + injection + dash_block[pos:]
                print(f"  Added {len(keys)} keys to DASH_NOTICES_I18N['{lang}']")

    content = content[:d_start] + dash_block + content[d_end:]

    # 3. Patch DOM Markup
    # Close button title
    content = content.replace(
        '<button id="close-ai-hub-modal" type="button" class="w-9 h-9 rounded-full flex items-center justify-center text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-colors cursor-pointer shrink-0" title="Đóng">',
        '<button id="close-ai-hub-modal" type="button" class="w-9 h-9 rounded-full flex items-center justify-center text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-colors cursor-pointer shrink-0" title="Close" data-i18n-title="aiHub.close">'
    )

    # Desktop desc
    content = content.replace(
        """          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">
            Dành cho máy tính đã cài <strong>Claude Desktop</strong> hoặc <strong>Cursor IDE</strong>. Tự động cấu hình MCP server và kết nối két chi tiêu on-chain.
          </p>""",
        """          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.desktopDesc">
            For computers with Claude Desktop or Cursor IDE installed. Automatically configures MCP server and binds to on-chain spending vault.
          </p>"""
    )

    # Desktop cmd label
    content = content.replace(
        '<span>Mở Terminal / PowerShell và chạy:</span>',
        '<span data-i18n="aiHub.desktopCmdLabel">Run in Terminal / PowerShell / Command Prompt:</span>'
    )

    # Online desc
    content = content.replace(
        """          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">
            Dành cho người dùng chat trên web <strong>claude.ai</strong> trên trình duyệt (Chrome, Safari, Brave, Edge). Kết nối trực tiếp qua giao thức đám mây.
          </p>""",
        """          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.onlineDesc">
            For users chatting on claude.ai in browser (Chrome, Safari, Brave, Edge). Connects directly via cloud protocol.
          </p>"""
    )

    # Account sync
    content = content.replace(
        '<span id="account-sync-browser-text">Đồng bộ sang trình duyệt Chrome</span>',
        '<span id="account-sync-browser-text" data-i18n="account.syncBrowser">Sync to Chrome Browser</span>'
    )

    # Guarantee breakdown in certificate
    content = content.replace(
        '<div class="text-[10px] text-neutral-400 font-sans">20% TGE + 80% Tuyến Tính 6T</div>',
        '<div class="text-[10px] text-neutral-400 font-sans">${getVestingText(\'guaranteeVestingBreakdown\', lang)}</div>'
    )

    # 4. Patch JS Strings & Notifications
    # MetaMask toast
    content = content.replace(
        'message: `+$${added.toFixed(2)} USDT • Ký xác thực: ${signature.slice(0, 6)}...`,',
        'message: `+$${added.toFixed(2)} USDT • ${getDashNotice(\'signedAuthPrefix\')} ${signature.slice(0, 6)}...`,'
    )

    # Biometric decrypt error
    content = content.replace(
        """          throw new Error(window.haichainI18n?.currentLang === 'vi'
            ? "Không thể giải mã Vault sinh trắc học hiện tại. Hệ thống từ chối tạo khóa mới để bảo vệ an toàn số dư đang có trong Vault của bạn. Vui lòng quét lại FaceID trên đúng thiết bị ban đầu."
            : "Could not decrypt existing biometric vault. The system refused to overwrite your key to protect existing vault funds. Please re-authenticate on the original device.");""",
        "          throw new Error(getDashNotice('biometricDecryptError'));"
    )

    # Mobile wallet err
    content = content.replace(
        "message: err || 'Không thể kết nối ví',",
        "message: err || getDashNotice('connectWalletFailed'),"
    )

    # Disconnect toast
    content = content.replace(
        """      showToast({
        title: window.haichainI18n?.currentLang === 'vi' ? 'Đã Ngắt Kết Nối' : 'Wallet Disconnected',
        message: window.haichainI18n?.currentLang === 'vi' ? 'Đã thoát phiên làm việc an toàn' : 'Session terminated successfully',
        icon: 'log-out'
      });""",
        """      showToast({
        title: getDashNotice('walletDisconnectedTitle'),
        message: getDashNotice('sessionTerminatedMsg'),
        icon: 'log-out'
      });"""
    )

    # Custom wallet toast
    content = content.replace(
        "title: window.haichainI18n?.currentLang === 'vi' ? 'Đã Kết Nối Ví Custom' : 'Custom Wallet Connected',",
        "title: getDashNotice('customWalletConnectedTitle'),"
    )

    # Copy buttons in AI Hub
    content = content.replace(
        'if (copyDesktopInstallText) copyDesktopInstallText.textContent = "✓ Đã sao chép lệnh!";\n          showToast({ title: "Đã sao chép!", message: "Dán vào Terminal/PowerShell để cài đặt tự động", icon: "check" });',
        "if (copyDesktopInstallText) copyDesktopInstallText.textContent = getDashNotice('cmdCopied');\n          showToast({ title: getDashNotice('copiedToastTitle'), message: getDashNotice('cmdCopyToastMsg'), icon: 'check' });"
    )
    content = content.replace(
        'if (copyDesktopInstallText) copyDesktopInstallText.textContent = "Sao chép lệnh cài đặt 1-Click";',
        "if (copyDesktopInstallText) copyDesktopInstallText.textContent = getDashNotice('cmdCopyBtn');"
    )
    content = content.replace(
        'showToast({ title: "Lệnh cài đặt:", message: cmd, icon: "terminal" });',
        "showToast({ title: getDashNotice('installCmdToastTitle'), message: cmd, icon: 'terminal' });"
    )
    content = content.replace(
        'if (copyOnlineMcpText) copyOnlineMcpText.textContent = "✓ Đã sao chép link!";\n          showToast({ title: "Đã sao chép!", message: "Dán vào Settings -> Connectors trên claude.ai", icon: "check" });',
        "if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopied');\n          showToast({ title: getDashNotice('copiedToastTitle'), message: getDashNotice('linkCopyToastMsg'), icon: 'check' });"
    )
    content = content.replace(
        'if (copyOnlineMcpText) copyOnlineMcpText.textContent = "Sao chép đường dẫn Remote MCP";',
        "if (copyOnlineMcpText) copyOnlineMcpText.textContent = getDashNotice('linkCopyBtn');"
    )

    # Clear user allocation reset/cancel
    content = content.replace(
        """            confirmText: isVi ? 'Đặt lại' : 'Reset',
            cancelText: isVi ? 'Huỷ' : 'Cancel'""",
        """            confirmText: getDashNotice('confirmResetBtn'),
            cancelText: getDashNotice('cancelBtn')"""
    )

    # AI Playground toast
    content = content.replace(
        'showToast({ title: "AI Playground", message: "Trải nghiệm suy luận AI trực tiếp qua Web3", icon: "zap" });',
        "showToast({ title: 'AI Playground', message: getDashNotice('aiPlaygroundToast'), icon: 'zap' });"
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

patch_i18n('i18n.js')
patch_i18n('app/i18n.js')
patch_dashboard('dashboard.html')
patch_dashboard('app/dashboard.html')

print("\nSUCCESS: All files cleanly patched!")
