import re

mm_keys = {
    'en': {
        'metaMaskConnectedBanner': 'MetaMask Wallet Connected',
        'returnToBrowser': 'Return to Safari / Chrome',
        'metaMaskRealConnectedTitle': '✓ MetaMask Real Wallet Connected!',
        'metaMaskMobileTitle': 'MetaMask Mobile',
        'launchingMetaMaskApp': 'Launching MetaMask App...',
        'redirectMetaMaskRealTx': 'Redirecting to MetaMask app to confirm transaction with real funds...'
    },
    'vi': {
        'metaMaskConnectedBanner': 'Đã kết nối ví MetaMask',
        'returnToBrowser': 'Quay về Safari / Chrome',
        'metaMaskRealConnectedTitle': '✓ MetaMask Đã Kết Nối Thực Tế!',
        'metaMaskMobileTitle': 'Ví MetaMask Mobile',
        'launchingMetaMaskApp': 'Đang kết nối tới ứng dụng MetaMask...',
        'redirectMetaMaskRealTx': 'Đang chuyển sang ứng dụng MetaMask để bạn xác nhận giao dịch bằng tiền thật...'
    },
    'zh': {
        'metaMaskConnectedBanner': '已连接 MetaMask 钱包',
        'returnToBrowser': '返回 Safari / Chrome',
        'metaMaskRealConnectedTitle': '✓ MetaMask 真实钱包已连接！',
        'metaMaskMobileTitle': 'MetaMask 移动端',
        'launchingMetaMaskApp': '正在启动 MetaMask 应用程序...',
        'redirectMetaMaskRealTx': '正在跳转至 MetaMask 应用程序以使用真实资金确认交易...'
    },
    'ko': {
        'metaMaskConnectedBanner': 'MetaMask 지갑 연결됨',
        'returnToBrowser': 'Safari / Chrome으로 돌아가기',
        'metaMaskRealConnectedTitle': '✓ MetaMask 실제 지갑 연결됨!',
        'metaMaskMobileTitle': 'MetaMask 모바일',
        'launchingMetaMaskApp': 'MetaMask 앱을 실행하는 중...',
        'redirectMetaMaskRealTx': '실제 자금으로 거래를 확인하기 위해 MetaMask 앱으로 이동하는 중...'
    },
    'fr': {
        'metaMaskConnectedBanner': 'Portefeuille MetaMask Connecté',
        'returnToBrowser': 'Retourner à Safari / Chrome',
        'metaMaskRealConnectedTitle': '✓ Vrai Portefeuille MetaMask Connecté !',
        'metaMaskMobileTitle': 'MetaMask Mobile',
        'launchingMetaMaskApp': 'Lancement de l\'application MetaMask...',
        'redirectMetaMaskRealTx': 'Redirection vers l\'application MetaMask pour confirmer la transaction...'
    },
    'es': {
        'metaMaskConnectedBanner': 'Billetera MetaMask Conectada',
        'returnToBrowser': 'Volver a Safari / Chrome',
        'metaMaskRealConnectedTitle': '✓ ¡Billetera Real MetaMask Conectada!',
        'metaMaskMobileTitle': 'MetaMask Móvil',
        'launchingMetaMaskApp': 'Iniciando la aplicación MetaMask...',
        'redirectMetaMaskRealTx': 'Redirigiendo a la aplicación MetaMask para confirmar la transacción con fondos reales...'
    },
    'ru': {
        'metaMaskConnectedBanner': 'Кошелек MetaMask Подключен',
        'returnToBrowser': 'Вернуться в Safari / Chrome',
        'metaMaskRealConnectedTitle': '✓ Реальный Кошелек MetaMask Подключен!',
        'metaMaskMobileTitle': 'MetaMask Мобильный',
        'launchingMetaMaskApp': 'Запуск приложения MetaMask...',
        'redirectMetaMaskRealTx': 'Перенаправление в приложение MetaMask для подтверждения транзакции реальными средствами...'
    },
    'kk': {
        'metaMaskConnectedBanner': 'MetaMask әмияны қосылды',
        'returnToBrowser': 'Safari / Chrome браузеріне оралу',
        'metaMaskRealConnectedTitle': '✓ Нақты MetaMask әмияны қосылды!',
        'metaMaskMobileTitle': 'MetaMask Мобильді',
        'launchingMetaMaskApp': 'MetaMask қолданбасын іске қосу...',
        'redirectMetaMaskRealTx': 'Нақты қаражатпен транзакцияны растау үшін MetaMask қолданбасына бағытталуда...'
    },
    'hi': {
        'metaMaskConnectedBanner': 'मेटामास्क वॉलेट कनेक्ट हो गया',
        'returnToBrowser': 'Safari / Chrome पर लौटें',
        'metaMaskRealConnectedTitle': '✓ मेटामास्क असली वॉलेट कनेक्ट हो गया!',
        'metaMaskMobileTitle': 'मेटामास्क मोबाइल',
        'launchingMetaMaskApp': 'मेटामास्क ऐप लॉन्च किया जा रहा है...',
        'redirectMetaMaskRealTx': 'वास्तविक फंड के साथ लेनदेन की पुष्टि करने के लिए मेटामास्क ऐप पर पुनर्निर्देशित किया जा रहा है...'
    },
    'he': {
        'metaMaskConnectedBanner': 'ארנק MetaMask מחובר',
        'returnToBrowser': 'חזור ל-Safari / Chrome',
        'metaMaskRealConnectedTitle': '✓ ארנק אמיתי של MetaMask מחובר!',
        'metaMaskMobileTitle': 'MetaMask מובייל',
        'launchingMetaMaskApp': 'מפעיל את אפליקציית MetaMask...',
        'redirectMetaMaskRealTx': 'מפנה לאפליקציית MetaMask כדי לאשר את העסקה עם כספים אמיתיים...'
    }
}

def patch_mm_dashboard(file_path):
    print(f"Patching MM in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # Add keys to DASH_NOTICES_I18N
    d_start = content.find('const DASH_NOTICES_I18N = {')
    d_end = content.find('function getDashNotice(key) {')
    if d_start != -1 and d_end != -1:
        dash_block = content[d_start:d_end]
        for lang, keys in mm_keys.items():
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
        content = content[:d_start] + dash_block + content[d_end:]
        print("  Added MM keys to DASH_NOTICES_I18N")

    # Replace the 7 isVi ? lines
    content = content.replace(
        "${isVi ? 'Đã kết nối ví MetaMask' : 'MetaMask Wallet Connected'}",
        "${getDashNotice('metaMaskConnectedBanner')}"
    )
    content = content.replace(
        "<span>${isVi ? 'Quay về Safari / Chrome' : 'Return to Safari / Chrome'}</span>",
        "<span>${getDashNotice('returnToBrowser')}</span>"
    )
    content = content.replace(
        "title: isVi ? '✓ MetaMask Đã Kết Nối Thực Tế!' : '✓ MetaMask Real Wallet Connected!',",
        "title: getDashNotice('metaMaskRealConnectedTitle'),"
    )
    content = content.replace(
        "walletBtnText.textContent = getDashNotice('connectingMetaMask') || (isVi ? 'Đang mở MetaMask...' : 'Launching MetaMask...');",
        "walletBtnText.textContent = getDashNotice('connectingMetaMask');"
    )
    content = content.replace(
        "title: isVi ? 'Ví MetaMask Mobile' : 'MetaMask Mobile',",
        "title: getDashNotice('metaMaskMobileTitle'),"
    )
    content = content.replace(
        "message: isVi ? 'Đang kết nối tới ứng dụng MetaMask...' : 'Launching MetaMask App...',",
        "message: getDashNotice('launchingMetaMaskApp'),"
    )
    content = content.replace(
        'alert(isVi ? "Đang chuyển sang ứng dụng MetaMask để bạn xác nhận giao dịch bằng tiền thật..." : "Redirecting to MetaMask app to confirm real transaction...");',
        "alert(getDashNotice('redirectMetaMaskRealTx'));"
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

patch_mm_dashboard('dashboard.html')
patch_mm_dashboard('app/dashboard.html')
print("MM Dashboard patched!")
