import re

extended_keys = {
    'en': {
        'confirmMsgInvestment': 'CONFIRM $HAISI PURCHASE ({provider}):\n\n• Investment Amount: ${amount} USDT\n• Token Allocation: {tokens} $HAISI (Price: $0.007)\n• Beneficiary Wallet: {wallet}\n• Mainnet Guarantee: 100% real on-chain conversion disbursed at TGE.\n\nYour {provider} wallet will open for cryptographic authorization.',
        'saftSuccessAlert': '🎉 SAFT SUBSCRIPTION & ALLOCATION CONFIRMED!\n\nYour wallet ({shortWallet}) now officially holds {tokens} $HAISI.\n\n🛡️ MAINNET CONVERSION GUARANTEE:\nAll {tokens} $HAISI are immutably secured under the SAFT Agreement. Upon HAICHAIN Mainnet launch (TGE), the Solana Token-2022 smart contract will automatically disburse 100% real on-chain tokens directly to this wallet.\n\nRedirecting to your Vesting Vault to inspect allocation...',
        'saftLimitsError': 'SAFT allocation amount must be between 500 USDT and 50,000 USDT.',
        'web3WalletNotFound': 'Web3 wallet extension not found. Please connect your wallet in the header or paste address manually.'
    },
    'vi': {
        'confirmMsgInvestment': 'XÁC NHẬN THANH TOÁN MUA $HAISI ({provider}):\n\n• Số tiền đầu tư: ${amount} USDT\n• Phân bổ sở hữu: {tokens} $HAISI (Đơn giá: $0.007)\n• Ví thụ hưởng: {wallet}\n• Bảo chứng Mainnet: Cam kết tự động giải ngân 100% Token Thật tại sự kiện TGE.\n\nVí {provider} của bạn sẽ mở ra để xác thực mật mã.',
        'saftSuccessAlert': '🎉 ĐÃ GHI NHẬN ĐĂNG KÝ VÀ BẢO CHỨNG PHÂN BỔ SAFT!\n\nVí của bạn ({shortWallet}) đã chính thức sở hữu {tokens} $HAISI.\n\n🛡️ BẢO CHỨNG CHUYỂN ĐỔI MAINNET:\nToàn bộ {tokens} $HAISI đã được bảo lưu bất biến theo Hợp đồng SAFT. Ngay khi HAICHAIN chính thức kích hoạt mạng Mainnet (Sự kiện TGE), hợp đồng thông minh Solana Token-2022 sẽ tự động giải ngân và chuyển đổi 100% số token này thành Token Thật on-chain về đúng địa chỉ ví này của bạn mà không cần thủ tục nào khác.\n\nHệ thống đang chuyển bạn đến Két sắt Vesting để kiểm tra số dư và chứng nhận phân bổ.',
        'saftLimitsError': 'Hạn mức đăng ký phân bổ SAFT từ 500 USDT đến 50.000 USDT.',
        'web3WalletNotFound': 'Không tìm thấy tiện ích ví Web3. Vui lòng kết nối ví ở góc trên hoặc dán địa chỉ ví thủ công.'
    },
    'zh': {
        'confirmMsgInvestment': '确认认购 $HAISI 代币 ({provider})：\n\n• 投资金额：${amount} USDT\n• 代币额度：{tokens} $HAISI（单价：$0.007）\n• 受益人钱包：{wallet}\n• 主网保函：在 TGE 时自动 100% 兑换链上代币。\n\n您的 {provider} 钱包将打开进行密码学授权。',
        'saftSuccessAlert': '🎉 SAFT 认购与额度保函已确认！\n\n您的钱包 ({shortWallet}) 已正式持有 {tokens} $HAISI。\n\n🛡️ 主网兑换官方保函：\n所有 {tokens} $HAISI 均受到 SAFT 协议的不可变法律保护。HAICHAIN 主网启动 (TGE) 时，Solana Token-2022 智能合约将自动将 100% 真实链上代币划转至该钱包。\n\n正在跳转至您的 Vesting 金库查看额度...',
        'saftLimitsError': 'SAFT 认购金额必须在 500 USDT 至 50,000 USDT 之间。',
        'web3WalletNotFound': '未检测到 Web3 钱包插件。请在顶部连接钱包或手动粘贴地址。'
    },
    'ko': {
        'confirmMsgInvestment': '$HAISI 구매 승인 및 결제 확인 ({provider}):\n\n• 투자 금액: ${amount} USDT\n• 토큰 배분: {tokens} $HAISI (단가: $0.007)\n• 수령 지갑: {wallet}\n• 메인넷 보증: TGE 시 100% 온체인 실제 토큰 자동 지급.\n\n암호학적 서명을 위해 {provider} 지갑이 열립니다.',
        'saftSuccessAlert': '🎉 SAFT 청약 및 토큰 할당이 승인되었습니다!\n\n귀하의 지갑({shortWallet})이 이제 공식적으로 {tokens} $HAISI를 보유합니다.\n\n🛡️ 메인넷 전환 보증:\n모든 {tokens} $HAISI는 SAFT 계약에 따라 불변으로 보호됩니다. HAICHAIN 메인넷 출시(TGE) 시 Solana Token-2022 스마트 계약이 100% 온체인 실제 토큰을 이 지갑으로 자동 지급합니다.\n\n배분 증명서 확인을 위해 Vesting 금고로 이동합니다...',
        'saftLimitsError': 'SAFT 할당 금액은 500 USDT에서 50,000 USDT 사이여야 합니다.',
        'web3WalletNotFound': 'Web3 지갑 확장 프로그램을 찾을 수 없습니다. 헤더에서 지갑을 연결하거나 주소를 수동으로 입력하세요.'
    },
    'fr': {
        'confirmMsgInvestment': 'CONFIRMER L\'ACHAT DE $HAISI ({provider}) :\n\n• Montant d\'investissement : ${amount} USDT\n• Allocation : {tokens} $HAISI (Prix : $0.007)\n• Portefeuille bénéficiaire : {wallet}\n• Garantie Mainnet : Conversion 100% on-chain déboursée au TGE.\n\nVotre portefeuille {provider} va s\'ouvrir pour l\'autorisation.',
        'saftSuccessAlert': '🎉 SOUSCRIPTION SAFT & ALLOCATION CONFIRMÉES !\n\nVotre portefeuille ({shortWallet}) détient désormais {tokens} $HAISI.\n\n🛡️ GARANTIE DE CONVERSION MAINNET :\nTous les {tokens} $HAISI sont légalement garantis sous l\'Accord SAFT. Dès le lancement du Mainnet HAICHAIN (TGE), le contrat intelligent Solana Token-2022 déboursera automatiquement 100% des tokens réels sur ce portefeuille.\n\nRedirection vers votre coffre de Vesting...',
        'saftLimitsError': 'Le montant de l\'allocation SAFT doit être compris entre 500 USDT et 50 000 USDT.',
        'web3WalletNotFound': 'Extension de portefeuille Web3 non trouvée. Veuillez connecter votre portefeuille ou coller l\'adresse manuellement.'
    },
    'es': {
        'confirmMsgInvestment': 'CONFIRMAR COMPRA DE $HAISI ({provider}):\n\n• Monto de inversión: ${amount} USDT\n• Asignación: {tokens} $HAISI (Precio: $0.007)\n• Billetera beneficiaria: {wallet}\n• Garantía Mainnet: Conversión 100% on-chain desembolsada en TGE.\n\nSu billetera {provider} se abrirá para la autorización.',
        'saftSuccessAlert': '🎉 ¡SUSCRIPCIÓN SAFT Y ASIGNACIÓN CONFIRMADAS!\n\nSu billetera ({shortWallet}) ahora posee oficialmente {tokens} $HAISI.\n\n🛡️ GARANTÍA DE CONVERSIÓN MAINNET:\nTodos los {tokens} $HAISI están legalmente respaldados bajo el Acuerdo SAFT. En el lanzamiento de la Mainnet de HAICHAIN (TGE), el contrato inteligente Solana Token-2022 desembolsará automáticamente el 100% de los tokens reales a esta billetera.\n\nRedirigiendo a su Bóveda de Vesting...',
        'saftLimitsError': 'El monto de la asignación SAFT debe estar entre 500 USDT y 50.000 USDT.',
        'web3WalletNotFound': 'No se encontró la extensión de billetera Web3. Conecte su billetera arriba o pegue la dirección manualmente.'
    },
    'ru': {
        'confirmMsgInvestment': 'ПОДТВЕРЖДЕНИЕ ПОКУПКИ $HAISI ({provider}):\n\n• Сумма инвестиций: ${amount} USDT\n• Выделение токенов: {tokens} $HAISI (Цена: $0.007)\n• Кошелек получателя: {wallet}\n• Гарантия Mainnet: 100% ончейн-конвертация при TGE.\n\nВаш кошелек {provider} откроется для подписи.',
        'saftSuccessAlert': '🎉 ПОДПИСКА SAFT И ВЫДЕЛЕНИЕ ТОКЕНОВ ПОДТВЕРЖДЕНЫ!\n\nВаш кошелек ({shortWallet}) теперь официально владеет {tokens} $HAISI.\n\n🛡️ ГАРАНТИЯ КОНВЕРТАЦИИ В MAINNET:\nВсе {tokens} $HAISI юридически защищены соглашением SAFT. При запуске Mainnet HAICHAIN (TGE) смарт-контракт Solana Token-2022 автоматически переведет 100% реальных ончейн-токенов на этот кошелек.\n\nПеренаправление в Сейф Вестинга...',
        'saftLimitsError': 'Сумма выделения SAFT должна составлять от 500 USDT до 50 000 USDT.',
        'web3WalletNotFound': 'Расширение Web3-кошелька не найдено. Подключите кошелек в шапке или вставьте адрес вручную.'
    },
    'kk': {
        'confirmMsgInvestment': '$HAISI САТЫП АЛУДЫ РАСТАУ ({provider}):\n\n• Инвестиция көлемі: ${amount} USDT\n• Бөлінген үлес: {tokens} $HAISI (Бағасы: $0.007)\n• Алушы әмиян: {wallet}\n• Mainnet кепілдігі: TGE кезінде 100% нақты ончейн токендер автоматты түрде беріледі.\n\nКриптографиялық растау үшін {provider} әмияныңыз ашылады.',
        'saftSuccessAlert': '🎉 SAFT ЖАЗЫЛУЫ МЕН БӨЛІНГЕН ҮЛЕС РАСТАЛДЫ!\n\nСіздің әмияныңыз ({shortWallet}) енді ресми түрде {tokens} $HAISI иеленеді.\n\n🛡️ MAINNET РЕСМИ КЕПІЛДІГІ:\nБарлық {tokens} $HAISI SAFT келісімшартымен өзгермейтін түрде қорғалған. HAICHAIN Mainnet іске қосылғанда (TGE), Solana Token-2022 смарт-келісімшарты 100% нақты ончейн токендерді осы әмиянға автоматты түрде аударады.\n\nVesting сейфіне бағытталуда...',
        'saftLimitsError': 'SAFT бөлінген үлес сомасы 500 USDT мен 50 000 USDT арасында болуы керек.',
        'web3WalletNotFound': 'Web3 әмиян кеңейтімі табылмады. Жоғарғы жағындағы әмиянды қосыңыз немесе мекенжайды қолмен қойыңыз.'
    },
    'hi': {
        'confirmMsgInvestment': '$HAISI खरीद की पुष्टि करें ({provider}):\n\n• निवेश राशि: ${amount} USDT\n• टोकन आवंटन: {tokens} $HAISI (मूल्य: $0.007)\n• लाभार्थी वॉलेट: {wallet}\n• मेननेट गारंटी: TGE पर 100% वास्तविक ऑन-चेन रूपांतरण।\n\nहस्ताक्षर के लिए आपका {provider} वॉलेट खुलेगा।',
        'saftSuccessAlert': '🎉 SAFT सदस्यता और आवंटन की पुष्टि हो गई!\n\nआपका वॉलेट ({shortWallet}) अब आधिकारिक तौर पर {tokens} $HAISI रखता है।\n\n🛡️ मेननेट रूपांतरण गारंटी:\nसभी {tokens} $HAISI SAFT समझौते के तहत सुरक्षित हैं। मेननेट लॉन्च (TGE) पर, सोलाना टोकन-2022 स्मार्ट अनुबंध स्वचालित रूप से इस वॉलेट में 100% वास्तविक टोकन वितरित करेगा।\n\nआवंटन देखने के लिए वेस्टिंग वॉल्ट पर पुनर्निर्देशित किया जा रहा है...',
        'saftLimitsError': 'SAFT आवंटन राशि 500 USDT और 50,000 USDT के बीच होनी चाहिए।',
        'web3WalletNotFound': 'Web3 वॉलेट एक्सटेंशन नहीं मिला। कृपया शीर्ष पर वॉलेट कनेक्ट करें या मैन्युअल रूप से पता पेस्ट करें।'
    },
    'he': {
        'confirmMsgInvestment': 'אישור רכישת $HAISI ({provider}):\n\n• סכום השקעה: ${amount} USDT\n• הקצאת אסימונים: {tokens} $HAISI (מחיר: $0.007)\n• ארנק מוטב: {wallet}\n• ערבות רשת ראשית: 100% המרה אמיתית ב-TGE.\n\nארנק ה-{provider} שלך ייפתח לאישור חתימה.',
        'saftSuccessAlert': '🎉 מנוי והקצאת SAFT אושרו!\n\nהארנק שלך ({shortWallet}) מחזיק כעת באופן רשמי ב-{tokens} $HAISI.\n\n🛡️ ערבות המרה לרשת הראשית:\nכל {tokens} $HAISI מאובטחים ללא שינוי תחת הסכם SAFT. עם השקת רשת Mainnet של HAICHAIN (אירוע TGE), החוזה החכם Solana Token-2022 ישחרר אוטומטית 100% אסימוני רשת אמיתיים לארנק זה.\n\nמעביר אותך לכספת הווסטינג...',
        'saftLimitsError': 'סכום הקצאת ה-SAFT חייב להיות בין 500 USDT ל-50,000 USDT.',
        'web3WalletNotFound': 'תוסף ארנק Web3 לא נמצא. אנא חבר את הארנק בחלק העליון או הדבק את הכתובת ידנית.'
    }
}

def inject_extended_sale(file_path):
    print(f"Injecting extended keys into {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # Add keys to SALE_I18N
    for lang, keys in extended_keys.items():
        pattern = rf'({lang}:\s*\{{\s*\n)'
        m = re.search(pattern, content)
        if m:
            pos = m.end()
            injection = ""
            for k, v in keys.items():
                if f"{k}:" not in content[m.start():m.start()+4500]:
                    v_esc = v.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
                    injection += f"      {k}: '{v_esc}',\n"
            if injection:
                content = content[:pos] + injection + content[pos:]
                print(f"  Added extended keys to SALE_I18N['{lang}']")

    # 1. Replace web3 wallet not found alert
    s_w3 = """          } else {
            alert(isVi 
              ? 'Không tìm thấy tiện ích ví Web3. Vui lòng kết nối ví ở góc trên hoặc dán địa chỉ ví thủ công.' 
              : 'Web3 wallet extension not found. Please connect your wallet in the header or paste address manually.');
          }"""
    r_w3 = """          } else {
            alert(getI18nText('web3WalletNotFound'));
          }"""
    if s_w3 in content:
        content = content.replace(s_w3, r_w3)
        print("  Replaced web3WalletNotFound")

    # 2. Replace limits error alert
    s_lim = """        if (isNaN(amount) || amount < 500 || amount > 50000) {
          alert(isVi 
            ? 'Hạn mức đăng ký phân bổ SAFT từ 500 USDT đến 50,000 USDT.' 
            : 'SAFT allocation amount must be between 500 USDT and 50,000 USDT.');
          return;
        }"""
    r_lim = """        if (isNaN(amount) || amount < 500 || amount > 50000) {
          alert(getI18nText('saftLimitsError'));
          return;
        }"""
    if s_lim in content:
        content = content.replace(s_lim, r_lim)
        print("  Replaced saftLimitsError")

    # 3. Replace confirmMsg
    s_cmsg = """        const confirmMsg = isVi
          ? `XÁC NHẬN THANH TOÁN MUA $HAISI (${provName}):

• Số tiền đầu tư: $${amount.toLocaleString()} USDT
• Phân bổ sở hữu: ${totalHaiNum.toLocaleString()} $HAISI (Đơn giá: $0.007)
• Ví thụ hưởng: ${wallet}
• Bảo chứng Mainnet: Cam kết tự động giải ngân 100% Token Thật tại sự kiện TGE.

Ví ${provName} của bạn sẽ mở ra để xác thực mật mã.`
          : `CONFIRM $HAISI PURCHASE (${provName}):

• Investment Amount: $${amount.toLocaleString()} USDT
• Token Allocation: ${totalHaiNum.toLocaleString()} $HAISI (@ $0.007)
• Beneficiary Wallet: ${wallet}
• Mainnet Guarantee: 100% real on-chain conversion disbursed at TGE.

Your ${provName} wallet will open for cryptographic authorization.`;"""
    r_cmsg = """        const confirmMsg = getI18nText('confirmMsgInvestment')
          .replace('{provider}', provName)
          .replace('{amount}', amount.toLocaleString())
          .replace('{tokens}', totalHaiNum.toLocaleString())
          .replace('{wallet}', wallet);"""
    if s_cmsg in content:
        content = content.replace(s_cmsg, r_cmsg)
        print("  Replaced confirmMsg")

    # 4. Replace success alert
    s_succ = """Ví của bạn (${wallet.slice(0, 6)}...${wallet.slice(-4)}) đã chính thức sở hữu ${totalHaiNum.toLocaleString()} $HAISI.

🛡️ BẢO CHỨNG CHUYỂN ĐỔI MAINNET:
Toàn bộ ${totalHaiNum.toLocaleString()} $HAISI đã được bảo lưu bất biến theo Hợp đồng SAFT. Ngay khi HAICHAIN chính thức kích hoạt mạng Mainnet (Sự kiện TGE), hợp đồng thông minh Solana Token-2022 sẽ tự động giải ngân và chuyển đổi 100% số token này thành Token Thật on-chain về đúng địa chỉ ví này của bạn mà không cần thủ tục nào khác.

Hệ thống đang chuyển bạn đến Két sắt Vesting để kiểm tra số dư và chứng nhận phân bổ.`
            : `🎉 SAFT SUBSCRIPTION & ALLOCATION CONFIRMED!

Your wallet (${wallet.slice(0, 6)}...${wallet.slice(-4)}) now officially holds ${totalHaiNum.toLocaleString()} $HAISI.

🛡️ MAINNET CONVERSION GUARANTEE:
All ${totalHaiNum.toLocaleString()} $HAISI are immutably secured under the SAFT Agreement. Upon HAICHAIN Mainnet launch (TGE), the Solana Token-2022 smart contract will automatically disburse 100% real on-chain tokens directly to this wallet with zero additional actions required.

Redirecting to your Vesting Vault tab.`);"""
    
    # Check if s_succ pattern is in content
    pattern_succ = r'alert\(isVi\s*\?\s*`🎉 ĐÃ GHI NHẬN ĐĂNG KÝ VÀ BẢO CHỨNG PHÂN BỔ SAFT![\s\S]*?Redirecting to your Vesting Vault tab\.`\);'
    r_succ = """alert(getI18nText('saftSuccessAlert')
              .replace('{shortWallet}', `${wallet.slice(0, 6)}...${wallet.slice(-4)}`)
              .replace(/{tokens}/g, totalHaiNum.toLocaleString()));"""
    
    if re.search(pattern_succ, content):
        content = re.sub(pattern_succ, r_succ, content)
        print("  Replaced saftSuccessAlert")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

inject_extended_sale('sale-controller.js')
inject_extended_sale('app/sale-controller.js')
print("Extended sale i18n injected!")
