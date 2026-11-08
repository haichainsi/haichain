import re

all_sale_keys = {
    'en': {
        'btnConnectWeb3ToBuy': 'Connect Web3 Wallet to Buy $HAISI',
        'btnPayMetaMask': '🦊 Pay for $HAISI with MetaMask',
        'btnPaySolflare': '🔥 Pay for $HAISI with Solflare',
        'btnPayPhantom': '👻 Pay with Phantom (1-Click)',
        'connectWeb3Required': 'Please connect your Web3 wallet (MetaMask, Phantom, or Solflare) to proceed with SAFT payment.',
        'confirmPurchaseTitle': 'CONFIRM $HAISI PURCHASE ({provider})',
        'authorizeOpenWallet': 'Authorize & Open Wallet',
        'metaMaskConnCancelled': 'MetaMask connection was cancelled.',
        'metaMaskNoAccount': 'No valid MetaMask account found.',
        'metaMaskTxCancelled': 'Transaction signature was cancelled in MetaMask.',
        'metaMaskErrorPrefix': 'MetaMask error:',
        'solanaConnCancelled': 'Solana wallet connection was cancelled.',
        'solanaUnlockPrompt': 'Please unlock and connect your Solana wallet!',
        'solanaTxCancelled': 'Transaction was cancelled in your wallet.',
        'solanaErrorPrefix': 'Solana wallet error:',
        'txNotConfirmed': 'Transaction was not confirmed by Web3 wallet.'
    },
    'vi': {
        'btnConnectWeb3ToBuy': 'Kết Nối Ví Web3 Để Mua $HAISI',
        'btnPayMetaMask': '🦊 Thanh Toán $HAISI Bằng MetaMask (EVM)',
        'btnPaySolflare': '🔥 Thanh Toán $HAISI Bằng Solflare',
        'btnPayPhantom': '👻 Thanh Toán 1-Click Ví Phantom',
        'connectWeb3Required': 'Vui lòng kết nối ví Web3 (MetaMask, Phantom hoặc Solflare) để thực hiện thanh toán SAFT.',
        'confirmPurchaseTitle': 'XÁC NHẬN THANH TOÁN MUA $HAISI ({provider})',
        'authorizeOpenWallet': 'Ký Duyệt & Mở Ví',
        'metaMaskConnCancelled': 'Bạn đã từ chối kết nối ví MetaMask.',
        'metaMaskNoAccount': 'Không tìm thấy địa chỉ tài khoản MetaMask hợp lệ.',
        'metaMaskTxCancelled': 'Bạn đã hủy yêu cầu ký duyệt giao dịch trên ví MetaMask.',
        'metaMaskErrorPrefix': 'Lỗi ví MetaMask:',
        'solanaConnCancelled': 'Bạn đã từ chối kết nối ví Solana.',
        'solanaUnlockPrompt': 'Vui lòng mở khóa và kết nối ví Solana!',
        'solanaTxCancelled': 'Bạn đã hủy yêu cầu giao dịch trên ví.',
        'solanaErrorPrefix': 'Lỗi ví Solana:',
        'txNotConfirmed': 'Giao dịch chưa được xác nhận bởi ví Web3.'
    },
    'zh': {
        'btnConnectWeb3ToBuy': '连接 Web3 钱包以认购 $HAISI',
        'btnPayMetaMask': '🦊 使用 MetaMask 支付 $HAISI (EVM)',
        'btnPaySolflare': '🔥 使用 Solflare 支付 $HAISI',
        'btnPayPhantom': '👻 使用 Phantom 1-Click 快捷支付',
        'connectWeb3Required': '请连接您的 Web3 钱包（MetaMask、Phantom 或 Solflare）以完成 SAFT 认购支付。',
        'confirmPurchaseTitle': '确认认购 $HAISI 代币 ({provider})',
        'authorizeOpenWallet': '授权并打开钱包',
        'metaMaskConnCancelled': '您已取消 MetaMask 钱包连接。',
        'metaMaskNoAccount': '未找到有效的 MetaMask 账户地址。',
        'metaMaskTxCancelled': 'MetaMask 中的交易签名已取消。',
        'metaMaskErrorPrefix': 'MetaMask 错误：',
        'solanaConnCancelled': '您已取消 Solana 钱包连接。',
        'solanaUnlockPrompt': '请解锁并连接您的 Solana 钱包！',
        'solanaTxCancelled': '钱包中的交易已取消。',
        'solanaErrorPrefix': 'Solana 钱包错误：',
        'txNotConfirmed': 'Web3 钱包未确认此交易。'
    },
    'ko': {
        'btnConnectWeb3ToBuy': '$HAISI 구매를 위해 Web3 지갑 연결',
        'btnPayMetaMask': '🦊 MetaMask로 $HAISI 결제 (EVM)',
        'btnPaySolflare': '🔥 Solflare로 $HAISI 결제',
        'btnPayPhantom': '👻 Phantom 1-Click 결제',
        'connectWeb3Required': 'SAFT 결제를 진행하려면 Web3 지갑(MetaMask, Phantom 또는 Solflare)을 연결하세요.',
        'confirmPurchaseTitle': '$HAISI 구매 승인 및 결제 확인 ({provider})',
        'authorizeOpenWallet': '승인 및 지갑 열기',
        'metaMaskConnCancelled': 'MetaMask 지갑 연결이 취소되었습니다.',
        'metaMaskNoAccount': '유효한 MetaMask 계정을 찾을 수 없습니다.',
        'metaMaskTxCancelled': 'MetaMask에서 거래 서명이 취소되었습니다.',
        'metaMaskErrorPrefix': 'MetaMask 오류:',
        'solanaConnCancelled': 'Solana 지갑 연결이 취소되었습니다.',
        'solanaUnlockPrompt': 'Solana 지갑을 잠금 해제하고 연결하세요!',
        'solanaTxCancelled': '지갑에서 거래가 취소되었습니다.',
        'solanaErrorPrefix': 'Solana 지갑 오류:',
        'txNotConfirmed': 'Web3 지갑에서 거래가 확인되지 않았습니다.'
    },
    'fr': {
        'btnConnectWeb3ToBuy': 'Connecter le portefeuille Web3 pour acheter $HAISI',
        'btnPayMetaMask': '🦊 Payer $HAISI avec MetaMask (EVM)',
        'btnPaySolflare': '🔥 Payer $HAISI avec Solflare',
        'btnPayPhantom': '👻 Payer en 1 Clic avec Phantom',
        'connectWeb3Required': 'Veuillez connecter votre portefeuille Web3 (MetaMask, Phantom ou Solflare) pour procéder au paiement SAFT.',
        'confirmPurchaseTitle': 'CONFIRMER L\'ACHAT DE $HAISI ({provider})',
        'authorizeOpenWallet': 'Autoriser et ouvrir le portefeuille',
        'metaMaskConnCancelled': 'La connexion à MetaMask a été annulée.',
        'metaMaskNoAccount': 'Aucun compte MetaMask valide trouvé.',
        'metaMaskTxCancelled': 'La signature de la transaction a été annulée dans MetaMask.',
        'metaMaskErrorPrefix': 'Erreur MetaMask :',
        'solanaConnCancelled': 'La connexion au portefeuille Solana a été annulée.',
        'solanaUnlockPrompt': 'Veuillez déverrouiller et connecter votre portefeuille Solana !',
        'solanaTxCancelled': 'La transaction a été annulée dans votre portefeuille.',
        'solanaErrorPrefix': 'Erreur portefeuille Solana :',
        'txNotConfirmed': 'La transaction n\'a pas été confirmée par le portefeuille Web3.'
    },
    'es': {
        'btnConnectWeb3ToBuy': 'Conectar billetera Web3 para comprar $HAISI',
        'btnPayMetaMask': '🦊 Pagar $HAISI con MetaMask (EVM)',
        'btnPaySolflare': '🔥 Pagar $HAISI con Solflare',
        'btnPayPhantom': '👻 Pagar en 1 Clic con Phantom',
        'connectWeb3Required': 'Conecte su billetera Web3 (MetaMask, Phantom o Solflare) para proceder con el pago SAFT.',
        'confirmPurchaseTitle': 'CONFIRMAR COMPRA DE $HAISI ({provider})',
        'authorizeOpenWallet': 'Autorizar y abrir billetera',
        'metaMaskConnCancelled': 'Se canceló la conexión con MetaMask.',
        'metaMaskNoAccount': 'No se encontró una cuenta válida de MetaMask.',
        'metaMaskTxCancelled': 'Se canceló la firma de la transacción en MetaMask.',
        'metaMaskErrorPrefix': 'Error de MetaMask:',
        'solanaConnCancelled': 'Se canceló la conexión con la billetera Solana.',
        'solanaUnlockPrompt': '¡Desbloquee y conecte su billetera Solana!',
        'solanaTxCancelled': 'Se canceló la transacción en su billetera.',
        'solanaErrorPrefix': 'Error de billetera Solana:',
        'txNotConfirmed': 'La transacción no fue confirmada por la billetera Web3.'
    },
    'ru': {
        'btnConnectWeb3ToBuy': 'Подключить Web3-кошелек для покупки $HAISI',
        'btnPayMetaMask': '🦊 Оплатить $HAISI через MetaMask (EVM)',
        'btnPaySolflare': '🔥 Оплатить $HAISI через Solflare',
        'btnPayPhantom': '👻 Оплатить в 1 Клик через Phantom',
        'connectWeb3Required': 'Пожалуйста, подключите Web3-кошелек (MetaMask, Phantom или Solflare) для оплаты SAFT.',
        'confirmPurchaseTitle': 'ПОДТВЕРЖДЕНИЕ ПОКУПКИ $HAISI ({provider})',
        'authorizeOpenWallet': 'Авторизовать и открыть кошелек',
        'metaMaskConnCancelled': 'Подключение MetaMask было отменено.',
        'metaMaskNoAccount': 'Действительный аккаунт MetaMask не найден.',
        'metaMaskTxCancelled': 'Подпись транзакции в MetaMask была отменена.',
        'metaMaskErrorPrefix': 'Ошибка MetaMask:',
        'solanaConnCancelled': 'Подключение кошелька Solana было отменено.',
        'solanaUnlockPrompt': 'Пожалуйста, разблокируйте и подключите кошелек Solana!',
        'solanaTxCancelled': 'Транзакция была отменена в вашем кошельке.',
        'solanaErrorPrefix': 'Ошибка кошелька Solana:',
        'txNotConfirmed': 'Транзакция не была подтверждена Web3-кошельком.'
    },
    'kk': {
        'btnConnectWeb3ToBuy': '$HAISI сатып алу үшін Web3 әмиянын қосыңыз',
        'btnPayMetaMask': '🦊 MetaMask арқылы $HAISI төлеу (EVM)',
        'btnPaySolflare': '🔥 Solflare арқылы $HAISI төлеу',
        'btnPayPhantom': '👻 Phantom арқылы 1-Click төлеу',
        'connectWeb3Required': 'SAFT төлемін жалғастыру үшін Web3 әмияныңызды (MetaMask, Phantom немесе Solflare) қосыңыз.',
        'confirmPurchaseTitle': '$HAISI САТЫП АЛУДЫ РАСТАУ ({provider})',
        'authorizeOpenWallet': 'Растау және әмиянды ашу',
        'metaMaskConnCancelled': 'MetaMask әмиянын қосу тоқтатылды.',
        'metaMaskNoAccount': 'Жарамды MetaMask тіркелгісі табылмады.',
        'metaMaskTxCancelled': 'MetaMask әмиянында транзакцияға қол қою тоқтатылды.',
        'metaMaskErrorPrefix': 'MetaMask қатесі:',
        'solanaConnCancelled': 'Solana әмиянын қосу тоқтатылды.',
        'solanaUnlockPrompt': 'Solana әмияныңызды ашып, қосыңыз!',
        'solanaTxCancelled': 'Әмияныңызда транзакция тоқтатылды.',
        'solanaErrorPrefix': 'Solana әмиян қатесі:',
        'txNotConfirmed': 'Транзакция Web3 әмиянымен расталмады.'
    },
    'hi': {
        'btnConnectWeb3ToBuy': '$HAISI खरीदने के लिए Web3 वॉलेट कनेक्ट करें',
        'btnPayMetaMask': '🦊 मेटामास्क के साथ $HAISI भुगतान करें',
        'btnPaySolflare': '🔥 सोलफ्लेयर के साथ $HAISI भुगतान करें',
        'btnPayPhantom': '👻 फैंटम के साथ 1-क्लिक भुगतान',
        'connectWeb3Required': 'SAFT भुगतान जारी रखने के लिए कृपया अपना Web3 वॉलेट (मेटामास्क, फैंटम या सोलफ्लेयर) कनेक्ट करें।',
        'confirmPurchaseTitle': '$HAISI खरीद की पुष्टि करें ({provider})',
        'authorizeOpenWallet': 'अधिकृत करें और वॉलेट खोलें',
        'metaMaskConnCancelled': 'मेटामास्क कनेक्शन रद्द कर दिया गया था।',
        'metaMaskNoAccount': 'कोई मान्य मेटामास्क खाता नहीं मिला।',
        'metaMaskTxCancelled': 'मेटामास्क में लेनदेन हस्ताक्षर रद्द कर दिया गया था।',
        'metaMaskErrorPrefix': 'मेटामास्क त्रुटि:',
        'solanaConnCancelled': 'सोलाना वॉलेट कनेक्शन रद्द कर दिया गया था।',
        'solanaUnlockPrompt': 'कृपया अपना सोलाना वॉलेट अनलॉक करें और कनेक्ट करें!',
        'solanaTxCancelled': 'आपके वॉलेट में लेनदेन रद्द कर दिया गया था।',
        'solanaErrorPrefix': 'सोलाना वॉलेट त्रुटि:',
        'txNotConfirmed': 'Web3 वॉलेट द्वारा लेनदेन की पुष्टि नहीं की गई थी।'
    },
    'he': {
        'btnConnectWeb3ToBuy': 'חבר ארנק Web3 כדי לרכוש את $HAISI',
        'btnPayMetaMask': '🦊 שלם עבור $HAISI עם MetaMask',
        'btnPaySolflare': '🔥 שלם עבור $HAISI עם Solflare',
        'btnPayPhantom': '👻 שלם בלחיצה אחת עם Phantom',
        'connectWeb3Required': 'אנא חבר את ארנק ה-Web3 שלך (MetaMask, Phantom או Solflare) כדי להמשיך בתשלום ה-SAFT.',
        'confirmPurchaseTitle': 'אישור רכישת $HAISI ({provider})',
        'authorizeOpenWallet': 'אשר ופתח את הארנק',
        'metaMaskConnCancelled': 'החיבור ל-MetaMask בוטל.',
        'metaMaskNoAccount': 'לא נמצא חשבון MetaMask חוקי.',
        'metaMaskTxCancelled': 'חתימת העסקה בוטלה ב-MetaMask.',
        'metaMaskErrorPrefix': 'שגיאת MetaMask:',
        'solanaConnCancelled': 'חיבור ארנק Solana בוטל.',
        'solanaUnlockPrompt': 'אנא בטל את נעילת ארנק Solana וחבר אותו!',
        'solanaTxCancelled': 'העסקה בוטלה בארנק שלך.',
        'solanaErrorPrefix': 'שגיאת ארנק Solana:',
        'txNotConfirmed': 'העסקה לא אושרה על ידי ארנק Web3.'
    }
}

def patch_universal_sale(file_path):
    print(f"Universal i18n patch for {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # Add keys to SALE_I18N
    for lang, keys in all_sale_keys.items():
        pattern = rf'({lang}:\s*\{{\s*\n)'
        m = re.search(pattern, content)
        if m:
            pos = m.end()
            injection = ""
            for k, v in keys.items():
                if f"{k}:" not in content[m.start():m.start()+3500]:
                    v_esc = v.replace('\\', '\\\\').replace("'", "\\'")
                    injection += f"      {k}: '{v_esc}',\n"
            if injection:
                content = content[:pos] + injection + content[pos:]
                print(f"  Added {len(keys)} keys to SALE_I18N['{lang}']")

    # Replace button texts:
    content = content.replace(
        "if (!saved.address) return isVi ? 'Kết Nối Ví Web3 Để Mua $HAISI' : 'Connect Web3 Wallet to Buy $HAISI';",
        "if (!saved.address) return getI18nText('btnConnectWeb3ToBuy');"
    )
    content = content.replace(
        "return isVi ? '🦊 Thanh Toán $HAISI Bằng MetaMask (EVM)' : '🦊 Pay for $HAISI with MetaMask';",
        "return getI18nText('btnPayMetaMask');"
    )
    content = content.replace(
        "return isVi ? '🔥 Thanh Toán $HAISI Bằng Solflare' : '🔥 Pay for $HAISI with Solflare';",
        "return getI18nText('btnPaySolflare');"
    )
    content = content.replace(
        "return isVi ? '👻 Thanh Toán 1-Click Ví Phantom' : '👻 Pay with Phantom (1-Click)';",
        "return getI18nText('btnPayPhantom');"
    )

    # Replace connectWeb3Required alert:
    content = content.replace(
        'alert(isVi ? "Vui lòng kết nối ví Web3 (MetaMask, Phantom hoặc Solflare) để thực hiện thanh toán SAFT." : "Please connect your Web3 wallet (MetaMask, Phantom, or Solflare) to proceed with SAFT payment.");',
        "alert(getI18nText('connectWeb3Required'));"
    )

    # Replace confirm dialog:
    content = content.replace(
        "title: isVi ? `XÁC NHẬN THANH TOÁN MUA $HAISI (${provName})` : `CONFIRM $HAISI PURCHASE (${provName})`,",
        "title: getI18nText('confirmPurchaseTitle').replace('{provider}', provName),"
    )
    content = content.replace(
        "confirmText: isVi ? 'Ký Duyệt & Mở Ví' : 'Authorize & Open Wallet',",
        "confirmText: getI18nText('authorizeOpenWallet'),"
    )

    # Replace MetaMask alerts:
    content = content.replace(
        'alert(isVi ? "Bạn đã từ chối kết nối ví MetaMask." : "MetaMask connection was cancelled.");',
        "alert(getI18nText('metaMaskConnCancelled'));"
    )
    content = content.replace(
        'alert(isVi ? "Không tìm thấy địa chỉ tài khoản MetaMask hợp lệ." : "No valid MetaMask account found.");',
        "alert(getI18nText('metaMaskNoAccount'));"
    )
    content = content.replace(
        'alert(isVi ? "Bạn đã hủy yêu cầu ký duyệt giao dịch trên ví MetaMask." : "Transaction signature was cancelled in MetaMask.");',
        "alert(getI18nText('metaMaskTxCancelled'));"
    )
    content = content.replace(
        'alert(isVi ? ("Lỗi ví MetaMask: " + (signErr.message || signErr)) : ("MetaMask error: " + (signErr.message || signErr)));',
        "alert(getI18nText('metaMaskErrorPrefix') + ' ' + (signErr.message || signErr));"
    )

    # Replace Solana alerts:
    content = content.replace(
        'alert(isVi ? "Bạn đã từ chối kết nối ví Solana." : "Solana wallet connection was cancelled.");',
        "alert(getI18nText('solanaConnCancelled'));"
    )
    content = content.replace(
        'alert(isVi ? "Vui lòng mở khóa và kết nối ví Solana!" : "Please unlock and connect your Solana wallet!");',
        "alert(getI18nText('solanaUnlockPrompt'));"
    )
    content = content.replace(
        "alert(isVi ? 'Bạn đã hủy yêu cầu giao dịch trên ví.' : 'Transaction was cancelled in your wallet.');",
        "alert(getI18nText('solanaTxCancelled'));"
    )
    content = content.replace(
        "alert(isVi ? ('Lỗi ví Solana: ' + (txErr.message || txErr)) : ('Solana wallet error: ' + (txErr.message || txErr)));",
        "alert(getI18nText('solanaErrorPrefix') + ' ' + (txErr.message || txErr));"
    )
    content = content.replace(
        'alert(isVi ? "Giao dịch chưa được xác nhận bởi ví Web3." : "Transaction was not confirmed by Web3 wallet.");',
        "alert(getI18nText('txNotConfirmed'));"
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

patch_universal_sale('sale-controller.js')
patch_universal_sale('app/sale-controller.js')
print("Sale controllers universally translated!")
