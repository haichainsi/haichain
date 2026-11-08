import re

sale_keys = {
    'en': {
        'openingMetaMaskSaft': 'Opening MetaMask App to confirm transaction with real funds...',
        'openingPhantomSaft': 'Opening Phantom App to confirm transaction with real funds...',
        'noMetaMaskDetected': 'MetaMask extension not detected in your browser!',
        'noSolanaDetected': 'No Solana wallet extension detected (Phantom or Solflare)!'
    },
    'vi': {
        'openingMetaMaskSaft': 'Đang mở ứng dụng MetaMask để bạn xác nhận giao dịch thanh toán bằng tiền thật trong ví...',
        'openingPhantomSaft': 'Đang mở ứng dụng Phantom để bạn xác nhận giao dịch thanh toán bằng tiền thật trong ví...',
        'noMetaMaskDetected': 'Chưa phát hiện tiện ích MetaMask trên trình duyệt của bạn!',
        'noSolanaDetected': 'Chưa phát hiện tiện ích ví Solana (Phantom hoặc Solflare)!'
    },
    'zh': {
        'openingMetaMaskSaft': '正在打开 MetaMask 应用程序以使用真实资金确认交易...',
        'openingPhantomSaft': '正在打开 Phantom 应用程序以使用真实资金确认交易...',
        'noMetaMaskDetected': '您的浏览器未检测到 MetaMask 插件！',
        'noSolanaDetected': '未检测到 Solana 钱包插件（Phantom 或 Solflare）！'
    },
    'ko': {
        'openingMetaMaskSaft': '실제 자금으로 거래를 확인하기 위해 MetaMask 앱을 여는 중...',
        'openingPhantomSaft': '실제 자금으로 거래를 확인하기 위해 Phantom 앱을 여는 중...',
        'noMetaMaskDetected': '브라우저에서 MetaMask 확장 프로그램이 감지되지 않았습니다!',
        'noSolanaDetected': 'Solana 지갑 확장 프로그램(Phantom 또는 Solflare)이 감지되지 않았습니다!'
    },
    'fr': {
        'openingMetaMaskSaft': "Ouverture de l'application MetaMask pour confirmer la transaction...",
        'openingPhantomSaft': "Ouverture de l'application Phantom pour confirmer la transaction...",
        'noMetaMaskDetected': 'Extension MetaMask non détectée dans votre navigateur !',
        'noSolanaDetected': 'Aucune extension de portefeuille Solana détectée (Phantom ou Solflare) !'
    },
    'es': {
        'openingMetaMaskSaft': 'Abriendo la aplicación MetaMask para confirmar la transacción con fondos reales...',
        'openingPhantomSaft': 'Abriendo la aplicación Phantom para confirmar la transacción con fondos reales...',
        'noMetaMaskDetected': '¡No se detectó la extensión de MetaMask en su navegador!',
        'noSolanaDetected': '¡No se detectó la extensión de billetera Solana (Phantom o Solflare)!'
    },
    'ru': {
        'openingMetaMaskSaft': 'Открытие приложения MetaMask для подтверждения транзакции реальными средствами...',
        'openingPhantomSaft': 'Открытие приложения Phantom для подтверждения транзакции реальными средствами...',
        'noMetaMaskDetected': 'Расширение MetaMask не обнаружено в вашем браузере!',
        'noSolanaDetected': 'Расширение кошелька Solana (Phantom или Solflare) не обнаружено!'
    },
    'kk': {
        'openingMetaMaskSaft': 'Нақты қаражатпен транзакцияны растау үшін MetaMask қолданбасын ашу...',
        'openingPhantomSaft': 'Нақты қаражатпен транзакцияны растау үшін Phantom қолданбасын ашу...',
        'noMetaMaskDetected': 'Браузеріңізде MetaMask кеңейтімі анықталмады!',
        'noSolanaDetected': 'Solana әмиян кеңейтімі (Phantom немесе Solflare) анықталмады!'
    },
    'hi': {
        'openingMetaMaskSaft': 'वास्तविक फंड के साथ लेनदेन की पुष्टि करने के लिए मेटामास्क ऐप खोला जा रहा है...',
        'openingPhantomSaft': 'वास्तविक फंड के साथ लेनदेन की पुष्टि करने के लिए फैंटम ऐप खोला जा रहा है...',
        'noMetaMaskDetected': 'आपके ब्राउज़र में मेटामास्क एक्सटेंशन का पता नहीं चला!',
        'noSolanaDetected': 'कोई सोलाना वॉलेट एक्सटेंशन (फैंटम या सोलफ्लेयर) नहीं मिला!'
    },
    'he': {
        'openingMetaMaskSaft': 'פותח את אפליקציית MetaMask כדי לאשר את העסקה עם כספים אמיתיים...',
        'openingPhantomSaft': 'פותח את אפליקציית Phantom כדי לאשר את העסקה עם כספים אמיתיים...',
        'noMetaMaskDetected': 'תוסף MetaMask לא זוהה בדפדפן שלך!',
        'noSolanaDetected': 'לא זוהה תוסף ארנק Solana (Phantom או Solflare)!'
    }
}

def patch_sale_controller(file_path):
    print(f"Patching {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # Add keys to SALE_I18N
    for lang, keys in sale_keys.items():
        pattern = rf'({lang}:\s*\{{\s*\n)'
        m = re.search(pattern, content)
        if m and '"openingMetaMaskSaft"' not in content[m.start():m.start()+2500]:
            pos = m.end()
            injection = ""
            for k, v in keys.items():
                v_esc = v.replace('\\', '\\\\').replace("'", "\\'")
                injection += f"      {k}: '{v_esc}',\n"
            content = content[:pos] + injection + content[pos:]
            print(f"  Added keys to SALE_I18N['{lang}']")

    # Replace binary alerts in sale-controller.js
    # 1. openingMetaMaskSaft
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Đang mở ứng dụng MetaMask để bạn xác nhận giao dịch thanh toán bằng tiền thật trong ví\.\.\."\s*:\s*"Opening MetaMask App to confirm transaction with real funds\.\.\."\);',
        "alert(getI18nText('openingMetaMaskSaft'));",
        content
    )

    # 2. noMetaMaskDetected
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Chưa phát hiện tiện ích MetaMask trên trình duyệt của bạn!"\s*:\s*"MetaMask extension not detected in your browser!"\);',
        "alert(getI18nText('noMetaMaskDetected'));",
        content
    )

    # 3. openingPhantomSaft
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Đang mở ứng dụng Phantom để bạn xác nhận giao dịch thanh toán bằng tiền thật trong ví\.\.\."\s*:\s*"Opening Phantom App to confirm transaction with real funds\.\.\."\);',
        "alert(getI18nText('openingPhantomSaft'));",
        content
    )

    # 4. noSolanaDetected
    content = re.sub(
        r'alert\(isVi\s*\?\s*"Chưa phát hiện tiện ích ví Solana \(Phantom hoặc Solflare\)!"\s*:\s*"No Solana wallet extension detected!"\);',
        "alert(getI18nText('noSolanaDetected'));",
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

patch_sale_controller('sale-controller.js')
patch_sale_controller('app/sale-controller.js')
