import re

# 1. New keys for i18n.js
i18n_keys = {
    'en': {
        'aiHub.close': 'Close',
        'account.syncBrowser': 'Sync to Chrome Browser'
    },
    'vi': {
        'aiHub.close': 'Đóng',
        'account.syncBrowser': 'Đồng bộ sang trình duyệt Chrome'
    },
    'zh': {
        'aiHub.close': '关闭',
        'account.syncBrowser': '同步至 Chrome 浏览器'
    },
    'ko': {
        'aiHub.close': '닫기',
        'account.syncBrowser': 'Chrome 브라우저로 동기화'
    },
    'fr': {
        'aiHub.close': 'Fermer',
        'account.syncBrowser': 'Synchroniser vers Chrome'
    },
    'es': {
        'aiHub.close': 'Cerrar',
        'account.syncBrowser': 'Sincronizar con navegador Chrome'
    },
    'ru': {
        'aiHub.close': 'Закрыть',
        'account.syncBrowser': 'Синхронизировать с браузером Chrome'
    },
    'kk': {
        'aiHub.close': 'Жабу',
        'account.syncBrowser': 'Chrome браузеріне синхрондау'
    },
    'hi': {
        'aiHub.close': 'बंद करें',
        'account.syncBrowser': 'Chrome ब्राउज़र में सिंक करें'
    },
    'he': {
        'aiHub.close': 'סגור',
        'account.syncBrowser': 'סנכרן לדפדפן Chrome'
    }
}

# 2. guaranteeVestingBreakdown for VESTING_VAULT_I18N
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

# 3. New keys for DASH_NOTICES_I18N
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
        'biometricDecryptError': 'Could not decrypt existing biometric vault. The system refused to overwrite your key to protect existing vault funds. Please re-authenticate on the original device.'
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
        'biometricDecryptError': 'Không thể giải mã Vault sinh trắc học hiện tại. Hệ thống từ chối tạo khóa mới để bảo vệ an toàn số dư đang có trong Vault của bạn. Vui lòng quét lại FaceID trên đúng thiết bị ban đầu.'
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
        'biometricDecryptError': '无法解密现有的生物识别 Vault。系统已拒绝覆盖您的密钥以保护金库中的现有资金。请在原始设备上重新进行身份验证。'
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
        'biometricDecryptError': '기존 생체 인식 Vault를 복호화할 수 없습니다. 금고의 기존 자금을 보호하기 위해 키 덮어쓰기가 거부되었습니다. 원래 기기에서 다시 인증해 주세요.'
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
        'biometricDecryptError': 'Impossible de déchiffrer le coffre biométrique existant. Le système a refusé d\'écraser votre clé pour protéger les fonds existants. Veuillez vous réauthentifier sur l\'appareil d\'origine.'
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
        'biometricDecryptError': 'No se pudo descifrar la bóveda biométrica existente. El sistema rechazó sobrescribir su clave para proteger los fondos existentes. Vuelva a autenticarse en el dispositivo original.'
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
        'biometricDecryptError': 'Не удалось расшифровать существующее биометрическое хранилище. Система отказалась перезаписывать ваш ключ для защиты средств в хранилище. Повторите аутентификацию на исходном устройстве.'
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
        'biometricDecryptError': 'Бар биометриялық сейфтің шифрын ашу мүмкін болмады. Жүйе сейфтегі қаражатты қорғау үшін кілтіңізді қайта жазудан бас тартты. Бастапқы құрылғыда қайта растаңыз.'
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
        'biometricDecryptError': 'मौजूदा बायोमेट्रिक वॉल्ट को डिक्रिप्ट नहीं किया जा सका। सिस्टम ने वॉल्ट फंड की सुरक्षा के लिए कुंजी को ओवरराइट करने से मना कर दिया। कृपया मूल डिवाइस पर पुनः प्रमाणीकरण करें।'
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
        'biometricDecryptError': 'לא ניתן לפענח את הכספת הביומטרית הקיימת. המערכת סירבה לדרוס את המפתח שלך כדי להגן על הכספים הקיימים. אנא בצע אימות מחדש במכשיר המקורי.'
    }
}

print("Loaded all dictionaries successfully.")
