import json
import os
import subprocess

SAFT_I18N_10LANG = {
    "vi": {
        "btnOpenSign": "Ký Hợp Đồng Online",
        "title": "Ký Điện Tử Hợp Đồng SAFT Pre-Seed ($0.007)",
        "subtitle": "Xác thực pháp lý trực tuyến theo chuẩn ESIGN Act & Luật GDĐT 2023",
        "nameLabel": "Họ và Tên / Tên Pháp Nhân *",
        "namePlaceholder": "Nguyễn Văn A / Tech Fund LLC",
        "emailLabel": "Email Liên Hệ *",
        "emailPlaceholder": "investor@example.com",
        "amountLabel": "Số Tiền Đăng Ký Đầu Tư (USD / USDT) *",
        "amountNote": "Hạn mức vé: $500 – $15,000 USD",
        "allocLabel": "Quyền Phân Bổ Token $HAISI (@ $0.007)",
        "tgeValLabel": "Giá trị TGE ($0.010):",
        "walletLabel": "Địa Chỉ Ví Solana Nhận Token Tại TGE *",
        "walletPlaceholder": "Địa chỉ ví Phantom/Solflare (Base58 32-44 ký tự)...",
        "autofillBtn": "Lấy Ví Đang Kết Nối",
        "treasuryLabel": "Kho Bạc Multi-Sig Nhận Vốn (Solana Mainnet):",
        "canvasLabel": "Chữ Ký Điện Tử Của Bạn *",
        "canvasPlaceholder": "(Dùng chuột hoặc ngón tay để ký tên tại đây)",
        "clearBtn": "Xóa ký lại",
        "agreeLabel": "Tôi xác nhận đã đọc, hiểu và đồng thuận 100% với các điều khoản của Hợp đồng SAFT HAICHAIN. Tôi hiểu rằng vốn đầu tư được bảo vệ tại Kho Bạc Squads Multi-Sig và token được phân bổ tự động tại TGE.",
        "submitBtn": "XÁC NHẬN KÝ & HOÀN TẤT HỢP ĐỒNG PHÁP LÝ",
        "successTitle": "KÝ HỢP ĐỒNG THÀNH CÔNG",
        "successSubtitle": "Hợp đồng SAFT điện tử đã được ghi nhận và đóng dấu kiểm toán mật mã.",
        "recId": "Mã Hợp Đồng:",
        "recInvestor": "Nhà Đầu Tư:",
        "recAlloc": "Phân Bổ:",
        "recWallet": "Ví Nhận:",
        "recTime": "Thời Gian:",
        "recHash": "SHA-256 Audit Hash:",
        "downloadBtn": "Tải File Chứng Nhận Hợp Đồng (HTML / PDF)",
        "proceedBtn": "Tiến Hành Nạp Tiền Vào Kho Bạc",
        "errName": "Vui lòng nhập Họ và Tên hoặc Tên Pháp Nhân của bạn.",
        "errEmail": "Vui lòng nhập địa chỉ Email hợp lệ.",
        "errAmount": "Hạn mức đăng ký đầu tư tối thiểu là 500 USD.",
        "errWallet": "Vui lòng nhập địa chỉ ví Solana hợp lệ (32 - 44 ký tự Base58) để nhận token tại TGE.",
        "errSig": "Vui lòng ký tên của bạn vào khung chữ ký điện tử.",
        "errAgree": "Vui lòng tick vào ô xác nhận đồng ý với các điều khoản Hợp đồng SAFT.",
        "alertProceed": "HỢP ĐỒNG ĐÃ ĐƯỢC KÝ!\n\nVui lòng chuyển {amount} USDT vào Kho Bạc:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nSố token {tokens} $HAISI sẽ được tự động phân bổ về ví của bạn tại TGE.",
        "noWalletDetected": "Chưa phát hiện ví Web3 (Phantom/Solflare) đang kết nối. Vui lòng dán địa chỉ ví thủ công."
    },
    "en": {
        "btnOpenSign": "Sign Agreement Online",
        "title": "Pre-Seed SAFT Digital E-Signature ($0.007)",
        "subtitle": "Online legal verification compliant with US ESIGN Act & UETA standards",
        "nameLabel": "Full Legal Name / Entity *",
        "namePlaceholder": "John Doe / Apex Capital LLC",
        "emailLabel": "Contact Email *",
        "emailPlaceholder": "investor@example.com",
        "amountLabel": "Subscription Investment Amount (USD / USDT) *",
        "amountNote": "Ticket limit: $500 – $15,000 USD",
        "allocLabel": "Token Entitlement $HAISI (@ $0.007)",
        "tgeValLabel": "TGE Value ($0.010):",
        "walletLabel": "Beneficiary Solana Wallet Address for TGE *",
        "walletPlaceholder": "Solana wallet address (Base58 32-44 characters)...",
        "autofillBtn": "Use Connected Wallet",
        "treasuryLabel": "Multi-Sig Treasury Vault (Solana Mainnet):",
        "canvasLabel": "Your Digital Signature *",
        "canvasPlaceholder": "(Use mouse or touch screen to sign here)",
        "clearBtn": "Clear Signature",
        "agreeLabel": "I confirm that I have read, understood, and agreed to all terms of the HAICHAIN Pre-Seed SAFT Agreement. I understand that investment funds are secured in the Squads Multi-Sig Treasury and tokens are distributed at TGE.",
        "submitBtn": "SIGN & FINALIZE LEGAL AGREEMENT",
        "successTitle": "AGREEMENT SIGNED SUCCESSFULLY",
        "successSubtitle": "Digital SAFT agreement recorded with cryptographic audit trail.",
        "recId": "Contract ID:",
        "recInvestor": "Investor:",
        "recAlloc": "Allocation:",
        "recWallet": "Receiving Wallet:",
        "recTime": "Timestamp:",
        "recHash": "SHA-256 Audit Hash:",
        "downloadBtn": "Download Signed Agreement Certificate (HTML / PDF)",
        "proceedBtn": "Proceed to Deposit to Treasury",
        "errName": "Please enter your Full Legal Name or Entity Name.",
        "errEmail": "Please enter a valid Email address.",
        "errAmount": "Minimum subscription amount is 500 USD.",
        "errWallet": "Please enter a valid Solana wallet address (32 - 44 characters Base58).",
        "errSig": "Please draw your signature in the signature box.",
        "errAgree": "Please agree to the SAFT Agreement terms to proceed.",
        "alertProceed": "AGREEMENT SIGNED!\n\nPlease transfer {amount} USDT to Treasury:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nYour {tokens} $HAISI allocation will be automatically disbursed at TGE.",
        "noWalletDetected": "No Web3 wallet (Phantom/Solflare) detected. Please paste your address manually."
    },
    "zh": {
        "btnOpenSign": "在线签署协议",
        "title": "Pre-Seed SAFT 电子法律签署 ($0.007)",
        "subtitle": "符合美国 ESIGN 法案与 UETA 标准的在线法律合规认证",
        "nameLabel": "法定全名 / 投资机构名称 *",
        "namePlaceholder": "张伟 / 某某资本合伙企业 (LLC)",
        "emailLabel": "联系电子邮箱 *",
        "emailPlaceholder": "investor@example.com",
        "amountLabel": "认购投资金额 (USD / USDT) *",
        "amountNote": "单张认购限额: $500 – $15,000 USD",
        "allocLabel": "$HAISI 代币认购分配权益 (@ $0.007)",
        "tgeValLabel": "TGE 上市预估价值 ($0.010):",
        "walletLabel": "TGE 代币接收 Solana 钱包地址 *",
        "walletPlaceholder": "Solana 钱包地址 (Base58 编码 32-44 位字符)...",
        "autofillBtn": "使用已连接钱包",
        "treasuryLabel": "多签金库收款地址 (Solana 主网):",
        "canvasLabel": "您的电子签名 *",
        "canvasPlaceholder": "(请使用鼠标或触屏在此处签署姓名)",
        "clearBtn": "清除重签",
        "agreeLabel": "本人确认已充分阅读、完全理解并同意 HAICHAIN Pre-Seed SAFT 协议的所有法律条款。本人知悉认购资金受 Squads 2-of-3 多签金库托管，代币将在 TGE 阶段自动分发。",
        "submitBtn": "确认签署并完成法律协议",
        "successTitle": "协议签署成功",
        "successSubtitle": "SAFT 电子法律协议已完成加密存证与防篡改审计哈希记录。",
        "recId": "合同编号:",
        "recInvestor": "投资者 / 机构:",
        "recAlloc": "代币分配额度:",
        "recWallet": "接收钱包:",
        "recTime": "签署时间:",
        "recHash": "SHA-256 审计哈希:",
        "downloadBtn": "下载已签署协议证书 (HTML / PDF)",
        "proceedBtn": "前往多签金库完成认购付款",
        "errName": "请输入您的法定全名或机构名称。",
        "errEmail": "请输入有效的电子邮箱地址。",
        "errAmount": "单笔最低认购投资金额为 500 USD。",
        "errWallet": "请输入有效的 Solana 钱包地址（32 - 44 位 Base58 格式）。",
        "errSig": "请在签名区域内绘制您的电子签名。",
        "errAgree": "请勾选同意 SAFT 协议法律条款以继续。",
        "alertProceed": "协议已成功签署！\n\n请向以下多签金库转账 {amount} USDT:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\n您的 {tokens} $HAISI 代币分配将在 TGE 阶段自动结算至您的钱包。",
        "noWalletDetected": "未检测到已连接的 Web3 钱包 (Phantom/Solflare)，请手动粘贴地址。"
    },
    "ko": {
        "btnOpenSign": "온라인 계약 서명",
        "title": "Pre-Seed SAFT 디지털 전자 서명 ($0.007)",
        "subtitle": "미국 ESIGN 법 및 UETA 표준 준수 온라인 법적 인증",
        "nameLabel": "법적 성명 / 법인명 *",
        "namePlaceholder": "홍길동 / 에이펙스 캐피탈",
        "emailLabel": "담당자 이메일 *",
        "emailPlaceholder": "investor@example.com",
        "amountLabel": "투자 청약 금액 (USD / USDT) *",
        "amountNote": "투자 한도: $500 – $15,000 USD",
        "allocLabel": "$HAISI 토큰 배정 권리 (@ $0.007)",
        "tgeValLabel": "TGE 상장 가치 ($0.010):",
        "walletLabel": "TGE 수령용 솔라나(Solana) 지갑 주소 *",
        "walletPlaceholder": "솔라나 지갑 주소 (Base58 32-44자)...",
        "autofillBtn": "연결된 지갑 주소 불러오기",
        "treasuryLabel": "멀티시그 금고 주소 (Solana 메인넷):",
        "canvasLabel": "전자 서명란 *",
        "canvasPlaceholder": "(마우스 또는 터치스크린으로 서명해 주세요)",
        "clearBtn": "서명 다시 하기",
        "agreeLabel": "본인은 HAICHAIN Pre-Seed SAFT 계약서의 모든 약관을 읽고 완전히 이해하였으며 이에 동의합니다. 투자 자금은 Squads 2-of-3 멀티시그 금고에 안전하게 보관되며 TGE 시점에 토큰이 자동 배정됨을 확인합니다.",
        "submitBtn": "서명 확인 및 법적 계약 체결",
        "successTitle": "계약 서명 완료",
        "successSubtitle": "디지털 SAFT 계약이 암호학적 감사 로그와 함께 안전하게 기록되었습니다.",
        "recId": "계약 번호:",
        "recInvestor": "투자자:",
        "recAlloc": "토큰 배정량:",
        "recWallet": "수령 지갑:",
        "recTime": "서명 일시:",
        "recHash": "SHA-256 감사 해시:",
        "downloadBtn": "서명된 계약 인증서 다운로드 (HTML / PDF)",
        "proceedBtn": "금고 입금 및 투자 절차 진행",
        "errName": "법적 성명 또는 법인명을 입력해 주세요.",
        "errEmail": "올바른 이메일 주소를 입력해 주세요.",
        "errAmount": "최소 투자 청약 금액은 500 USD입니다.",
        "errWallet": "유효한 솔라나 지갑 주소(Base58 32-44자)를 입력해 주세요.",
        "errSig": "서명란에 전자 서명을 입력해 주세요.",
        "errAgree": "진행하시려면 SAFT 계약 약관에 동의해 주세요.",
        "alertProceed": "계약 서명이 완료되었습니다!\n\n아래 멀티시그 금고로 {amount} USDT를 전송해 주세요:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\n배정된 {tokens} $HAISI 토큰은 TGE 시점에 등록된 지갑으로 자동 지급됩니다.",
        "noWalletDetected": "연결된 Web3 지갑(Phantom/Solflare)을 찾을 수 없습니다. 지갑 주소를 직접 입력해 주세요."
    },
    "es": {
        "btnOpenSign": "Firmar Acuerdo Online",
        "title": "Firma Digital de Acuerdo SAFT Pre-Seed ($0.007)",
        "subtitle": "Verificación legal en línea conforme a las normas US ESIGN Act y UETA",
        "nameLabel": "Nombre Legal Completo / Entidad *",
        "namePlaceholder": "Juan Pérez / Apex Capital LLC",
        "emailLabel": "Correo Electrónico de Contacto *",
        "emailPlaceholder": "inversor@ejemplo.com",
        "amountLabel": "Monto de Suscripción de Inversión (USD / USDT) *",
        "amountNote": "Límite por ticket: $500 – $15,000 USD",
        "allocLabel": "Asignación de Tokens $HAISI (@ $0.007)",
        "tgeValLabel": "Valor en TGE ($0.010):",
        "walletLabel": "Dirección de Billetera Solana para TGE *",
        "walletPlaceholder": "Dirección Solana (Base58 de 32 a 44 caracteres)...",
        "autofillBtn": "Usar Billetera Conectada",
        "treasuryLabel": "Bóveda de Tesorería Multi-Firma (Solana Mainnet):",
        "canvasLabel": "Su Firma Digital *",
        "canvasPlaceholder": "(Use el ratón o pantalla táctil para firmar aquí)",
        "clearBtn": "Borrar y repetir firma",
        "agreeLabel": "Confirmo que he leído, comprendido y aceptado el 100% de los términos del Acuerdo SAFT HAICHAIN. Entiendo que los fondos de inversión están custodiados en la Tesorería Multi-Sig Squads y los tokens se distribuirán automáticamente en el TGE.",
        "submitBtn": "FIRMAR Y FORMALIZAR ACUERDO LEGAL",
        "successTitle": "ACUERDO FIRMADO CON ÉXITO",
        "successSubtitle": "Acuerdo legal SAFT registrado con pista de auditoría criptográfica.",
        "recId": "ID de Contrato:",
        "recInvestor": "Inversionista:",
        "recAlloc": "Asignación:",
        "recWallet": "Billetera de Recepción:",
        "recTime": "Fecha y Hora:",
        "recHash": "Hash de Auditoría SHA-256:",
        "downloadBtn": "Descargar Certificado de Firma (HTML / PDF)",
        "proceedBtn": "Proceder al Depósito en la Tesorería",
        "errName": "Por favor ingrese su Nombre Legal Completo o de la Entidad.",
        "errEmail": "Por favor ingrese un Correo Electrónico válido.",
        "errAmount": "El monto mínimo de suscripción es de 500 USD.",
        "errWallet": "Por favor ingrese una dirección válida de billetera Solana (32-44 caracteres Base58).",
        "errSig": "Por favor dibuje su firma en el recuadro correspondiente.",
        "errAgree": "Debe aceptar los términos del Acuerdo SAFT para continuar.",
        "alertProceed": "¡ACUERDO FIRMADO CON ÉXITO!\n\nPor favor transfiera {amount} USDT a la Tesorería Multi-Firma:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nSu asignación de {tokens} $HAISI será distribuida automáticamente en el TGE.",
        "noWalletDetected": "No se detectó billetera Web3 (Phantom/Solflare). Por favor pegue la dirección manualmente."
    },
    "fr": {
        "btnOpenSign": "Signer l’Accord en Ligne",
        "title": "Signature Électronique SAFT Pre-Seed ($0.007)",
        "subtitle": "Vérification juridique conforme aux normes US ESIGN Act et UETA",
        "nameLabel": "Nom Légal Complet / Entité *",
        "namePlaceholder": "Jean Dupont / Apex Capital LLC",
        "emailLabel": "Email de Contact *",
        "emailPlaceholder": "investisseur@exemple.com",
        "amountLabel": "Montant d’Investissement (USD / USDT) *",
        "amountNote": "Limite de souscription: $500 – $15,000 USD",
        "allocLabel": "Attribution de Jetons $HAISI (@ $0.007)",
        "tgeValLabel": "Valeur au TGE ($0.010):",
        "walletLabel": "Adresse de Portefeuille Solana pour le TGE *",
        "walletPlaceholder": "Adresse Solana (Base58 de 32 à 44 caractères)...",
        "autofillBtn": "Utiliser le Portefeuille Connecté",
        "treasuryLabel": "Trésorerie Multi-Sig (Solana Mainnet):",
        "canvasLabel": "Votre Signature Électronique *",
        "canvasPlaceholder": "(Utilisez la souris ou l’écran tactile pour signer ici)",
        "clearBtn": "Effacer la signature",
        "agreeLabel": "Je confirme avoir lu, compris et accepté l’ensemble des conditions du contrat SAFT HAICHAIN. Je comprends que les fonds sont sécurisés dans la trésorerie multi-sig Squads et que les jetons seront distribués lors du TGE.",
        "submitBtn": "SIGNER ET FINALISER LE CONTRAT",
        "successTitle": "ACCORD SIGNÉ AVEC SUCCÈS",
        "successSubtitle": "Contrat SAFT numérique enregistré avec horodatage et audit cryptographique.",
        "recId": "ID du Contrat:",
        "recInvestor": "Investisseur:",
        "recAlloc": "Attribution:",
        "recWallet": "Portefeuille Récepteur:",
        "recTime": "Horodatage:",
        "recHash": "Hash d’Audit SHA-256:",
        "downloadBtn": "Télécharger le Certificat de Signature (HTML / PDF)",
        "proceedBtn": "Procéder au Dépôt vers la Trésorerie",
        "errName": "Veuillez saisir votre nom complet ou le nom de votre entité.",
        "errEmail": "Veuillez saisir une adresse email valide.",
        "errAmount": "Le montant minimum de souscription est de 500 USD.",
        "errWallet": "Veuillez saisir une adresse de portefeuille Solana valide (32-44 caractères Base58).",
        "errSig": "Veuillez apposer votre signature dans la zone prévue à cet effet.",
        "errAgree": "Veuillez accepter les termes de l’accord SAFT pour continuer.",
        "alertProceed": "ACCORD SIGNÉ !\n\nVeuillez transférer {amount} USDT vers la Trésorerie:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nVotre allocation de {tokens} $HAISI sera automatiquement distribuée au TGE.",
        "noWalletDetected": "Aucun portefeuille Web3 (Phantom/Solflare) détecté. Veuillez coller l’adresse manuellement."
    },
    "ru": {
        "btnOpenSign": "Подписать договор онлайн",
        "title": "Электронная подпись договора SAFT Pre-Seed ($0.007)",
        "subtitle": "Юридическая верификация онлайн в соответствии с US ESIGN Act и UETA",
        "nameLabel": "Полное юридическое имя / Название компании *",
        "namePlaceholder": "Иван Иванов / Apex Capital LLC",
        "emailLabel": "Контактный Email *",
        "emailPlaceholder": "investor@example.com",
        "amountLabel": "Сумма инвестиционной подписки (USD / USDT) *",
        "amountNote": "Лимит подписки: $500 – $15,000 USD",
        "allocLabel": "Право на распределение токенов $HAISI (@ $0.007)",
        "tgeValLabel": "Стоимость при TGE ($0.010):",
        "walletLabel": "Адрес кошелька Solana для получения токенов при TGE *",
        "walletPlaceholder": "Адрес Solana (Base58, 32-44 символа)...",
        "autofillBtn": "Использовать подключенный кошелек",
        "treasuryLabel": "Мультисиг казначейство (Solana Mainnet):",
        "canvasLabel": "Ваша электронная подпись *",
        "canvasPlaceholder": "(Используйте мышь или сенсорный экран для подписи)",
        "clearBtn": "Очистить подпись",
        "agreeLabel": "Я подтверждаю, что прочитал, понял и полностью согласен со всеми условиями соглашения HAICHAIN Pre-Seed SAFT. Я понимаю, что средства хранятся в мультисиг казначействе Squads, а токены распределяются при TGE.",
        "submitBtn": "ПОДПИСАТЬ И УТВЕРДИТЬ СОГЛАШЕНИЕ",
        "successTitle": "СОГЛАШЕНИЕ УСПЕШНО ПОДПИСАНО",
        "successSubtitle": "Электронный договор SAFT зарегистрирован с криптографическим аудитом.",
        "recId": "ID контракта:",
        "recInvestor": "Инвестор:",
        "recAlloc": "Аллокация:",
        "recWallet": "Кошелек получения:",
        "recTime": "Время:",
        "recHash": "Аудит-хеш SHA-256:",
        "downloadBtn": "Скачать сертификат соглашения (HTML / PDF)",
        "proceedBtn": "Перейти к переводу средств в казначейство",
        "errName": "Пожалуйста, укажите ваше полное имя или название организации.",
        "errEmail": "Пожалуйста, укажите корректный адрес электронной почты.",
        "errAmount": "Минимальная сумма подписки составляет 500 USD.",
        "errWallet": "Пожалуйста, укажите действительный адрес кошелька Solana (32-44 символа Base58).",
        "errSig": "Пожалуйста, поставьте подпись в поле для подписи.",
        "errAgree": "Пожалуйста, подтвердите согласие с условиями договора SAFT.",
        "alertProceed": "ДОГОВОР ПОДПИСАН!\n\nПожалуйста, переведите {amount} USDT в Казначейство:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nВаша аллокация в размере {tokens} $HAISI будет автоматически перечислена при TGE.",
        "noWalletDetected": "Web3 кошелек (Phantom/Solflare) не обнаружен. Пожалуйста, вставьте адрес вручную."
    },
    "kk": {
        "btnOpenSign": "Келісімге онлайн қол қою",
        "title": "Pre-Seed SAFT келісіміне цифрлық қол қою ($0.007)",
        "subtitle": "US ESIGN Act және UETA стандарттарына сәйкес онлайн заңды верификация",
        "nameLabel": "Толық заңды аты-жөні / Заңды тұлға *",
        "namePlaceholder": "Асқар Серік / Apex Capital LLC",
        "emailLabel": "Байланыс электрондық поштасы *",
        "emailPlaceholder": "investor@example.com",
        "amountLabel": "Инвестициялық жазылу сомасы (USD / USDT) *",
        "amountNote": "Лимит: $500 – $15,000 USD",
        "allocLabel": "$HAISI токендерін алу құқығы (@ $0.007)",
        "tgeValLabel": "TGE кезіндегі бағасы ($0.010):",
        "walletLabel": "TGE кезінде токен алатын Solana әмиян мекенжайы *",
        "walletPlaceholder": "Solana әмиян мекенжайы (Base58 32-44 таңба)...",
        "autofillBtn": "Қосылған әмиянды алу",
        "treasuryLabel": "Multi-Sig қазынашылық қоймасы (Solana Mainnet):",
        "canvasLabel": "Сіздің цифрлық қолтаңбаңыз *",
        "canvasPlaceholder": "(Қол қою үшін тінтуірді немесе сенсорлық экранды пайдаланыңыз)",
        "clearBtn": "Қайта қол қою",
        "agreeLabel": "Мен HAICHAIN Pre-Seed SAFT келісімінің барлық талаптарын оқып шыққанымды, толық түсінгенімді және келісетінімді растаймын. Қаражат Squads 2-of-3 қазынашылығында сақталатынын және токендер TGE кезінде берілетінін түсінемін.",
        "submitBtn": "ҚОЛ ҚОЮ ЖӘНЕ КЕЛІСІМДІ БЕКІТУ",
        "successTitle": "КЕЛІСІМГЕ СӘТТІ ҚОЛ ҚОЙЫЛДЫ",
        "successSubtitle": "Сандық SAFT шарты криптографиялық аудит белгісімен тіркелді.",
        "recId": "Келісімшарт ID:",
        "recInvestor": "Инвестор:",
        "recAlloc": "Бөлініс:",
        "recWallet": "Қабылдаушы әмиян:",
        "recTime": "Уақыты:",
        "recHash": "SHA-256 аудит хэші:",
        "downloadBtn": "Қол қойылған сертификатты жүктеу (HTML / PDF)",
        "proceedBtn": "Қазынашылыққа депозит жасау",
        "errName": "Толық заңды атыңызды немесе компания атауын енгізіңіз.",
        "errEmail": "Жарамды электрондық пошта мекенжайын енгізіңіз.",
        "errAmount": "Ең төменгі инвестиция сомасы - 500 USD.",
        "errWallet": "Жарамды Solana әмиян мекенжайын енгізіңіз (Base58 32-44 таңба).",
        "errSig": "Қолтаңба өрісіне қол қойыңыз.",
        "errAgree": "Жалғастыру үшін SAFT шарттарымен келісуіңіз керек.",
        "alertProceed": "КЕЛІСІМГЕ ҚОЛ ҚОЙЫЛДЫ!\n\nҚазынашылыққа {amount} USDT аударыңыз:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nСізге бөлінген {tokens} $HAISI токендері TGE кезінде автоматты түрде аударылады.",
        "noWalletDetected": "Қосылған Web3 әмиян табылмады. Мекенжайды қолмен енгізіңіз."
    },
    "hi": {
        "btnOpenSign": "ऑनलाइन अनुबंध पर हस्ताक्षर करें",
        "title": "प्री-सीड SAFT डिजिटल ई-हस्ताक्षर ($0.007)",
        "subtitle": "अमेरिकी ESIGN अधिनियम और UETA मानकों के अनुरूप ऑनलाइन कानूनी सत्यापन",
        "nameLabel": "पूर्ण कानूनी नाम / संस्था का नाम *",
        "namePlaceholder": "राजेश शर्मा / एपेक्स कैपिटल",
        "emailLabel": "संपर्क ईमेल *",
        "emailPlaceholder": "investor@example.com",
        "amountLabel": "निवेश सदस्यता राशि (USD / USDT) *",
        "amountNote": "टिकट सीमा: $500 – $15,000 USD",
        "allocLabel": "$HAISI टोकन आवंटन अधिकार (@ $0.007)",
        "tgeValLabel": "TGE मूल्य ($0.010):",
        "walletLabel": "TGE पर टोकन प्राप्त करने के लिए सोलाना वॉलेट पता *",
        "walletPlaceholder": "सोलाना वॉलेट पता (Base58 32-44 वर्ण)...",
        "autofillBtn": "कनेक्टेड वॉलेट का उपयोग करें",
        "treasuryLabel": "मल्टी-सिग ट्रेजरी वॉल्ट (सोलाना मेननेट):",
        "canvasLabel": "आपका डिजिटल हस्ताक्षर *",
        "canvasPlaceholder": "(हस्ताक्षर करने के लिए माउस या टच स्क्रीन का उपयोग करें)",
        "clearBtn": "हस्ताक्षर साफ़ करें",
        "agreeLabel": "मैं पुष्टि करता हूँ कि मैंने HAICHAIN प्री-सीड SAFT अनुबंध की सभी शर्तों को पढ़, समझ और सहमति दे दी है। मैं समझता हूँ कि निवेश निधि स्क्वॉड मल्टी-सिग ट्रेजरी में सुरक्षित है और टोकन TGE पर वितरित किए जाएंगे।",
        "submitBtn": "हस्ताक्षर करें और कानूनी अनुबंध को अंतिम रूप दें",
        "successTitle": "अनुबंध सफलतापूर्वक हस्ताक्षरित",
        "successSubtitle": "क्रिप्टोग्राफ़िक ऑडिट ट्रेल के साथ डिजिटल SAFT अनुबंध दर्ज किया गया।",
        "recId": "अनुबंध आईडी:",
        "recInvestor": "निवेशक:",
        "recAlloc": "आवंटन:",
        "recWallet": "प्राप्तकर्ता वॉलेट:",
        "recTime": "समय:",
        "recHash": "SHA-256 ऑडिट हैश:",
        "downloadBtn": "हस्ताक्षरित प्रमाणपत्र डाउनलोड करें (HTML / PDF)",
        "proceedBtn": "ट्रेजरी में जमा करने के लिए आगे बढ़ें",
        "errName": "कृपया अपना पूर्ण कानूनी नाम या संस्था का नाम दर्ज करें।",
        "errEmail": "कृपया एक मान्य ईमेल पता दर्ज करें।",
        "errAmount": "न्यूनतम सदस्यता राशि 500 USD है।",
        "errWallet": "कृपया एक मान्य सोलाना वॉलेट पता (32-44 वर्ण Base58) दर्ज करें।",
        "errSig": "कृपया हस्ताक्षर बॉक्स में अपना हस्ताक्षर बनाएं।",
        "errAgree": "आगे बढ़ने के लिए कृपया SAFT अनुबंध की शर्तों से सहमत हों।",
        "alertProceed": "अनुबंध हस्ताक्षरित!\n\nकृपया ट्रेजरी में {amount} USDT ट्रांसफर करें:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nआपका {tokens} $HAISI आवंटन TGE पर स्वचालित रूप से वितरित किया जाएगा।",
        "noWalletDetected": "कोई Web3 वॉलेट नहीं मिला। कृपया अपना पता मैन्युअल रूप से पेस्ट करें।"
    },
    "he": {
        "btnOpenSign": "חתימה על ההסכם אונליין",
        "title": "חתימה אלקטרונית על הסכם SAFT Pre-Seed ($0.007)",
        "subtitle": "אימות משפטי מקוון בהתאם לחוקי ESIGN ו-UETA בארה\"ב",
        "nameLabel": "שם משפטי מלא / שם תאגיד *",
        "namePlaceholder": "ישראל ישראלי / Apex Capital LLC",
        "emailLabel": "דוא\"ל ליצירת קשר *",
        "emailPlaceholder": "investor@example.com",
        "amountLabel": "סכום השקעה (USD / USDT) *",
        "amountNote": "מגבלת השקעה: $500 – $15,000 USD",
        "allocLabel": "זכאות להקצאת אסימוני $HAISI (@ $0.007)",
        "tgeValLabel": "שווי ב-TGE ($0.010):",
        "walletLabel": "כתובת ארנק Solana לקבלת אסימונים ב-TGE *",
        "walletPlaceholder": "כתובת ארנק Solana (Base58 32-44 תווים)...",
        "autofillBtn": "השתמש בארנק מחובר",
        "treasuryLabel": "כספת האוצר מרובת-חתימות (Solana Mainnet):",
        "canvasLabel": "החתימה הדיגיטלית שלך *",
        "canvasPlaceholder": "(השתמש בעכבר או במסך מגע לחתימה כאן)",
        "clearBtn": "נקה חתימה",
        "agreeLabel": "אני מאשר כי קראתי, הבנתי והסכמתי לכל תנאי הסכם HAICHAIN Pre-Seed SAFT. אני מבין כי כספי ההשקעה מאובטחים באוצר Multi-Sig של Squads והאסימונים יחולקו ב-TGE.",
        "submitBtn": "חתום ואשר את ההסכם המשפטי",
        "successTitle": "ההסכם נחתם בהצלחה",
        "successSubtitle": "הסכם ה-SAFT הדיגיטלי נרשם עם חותמת ביקורת קריפטוגרפית.",
        "recId": "מזהה חוזה:",
        "recInvestor": "משקיע:",
        "recAlloc": "הקצאה:",
        "recWallet": "ארנק מקבל:",
        "recTime": "חותמת זמן:",
        "recHash": "גיבוב ביקורת SHA-256:",
        "downloadBtn": "הורד תעודת הסכם חתומה (HTML / PDF)",
        "proceedBtn": "המשך להפקדה באוצר",
        "errName": "נא להזין שם משפטי מלא או שם חברה.",
        "errEmail": "נא להזין כתובת דוא\"ל תקינה.",
        "errAmount": "סכום ההשקעה המינימלי הוא 500 USD.",
        "errWallet": "נא להזין כתובת ארנק Solana תקינה (32-44 תווים Base58).",
        "errSig": "נא לחתום בתיבת החתימה.",
        "errAgree": "יש לאשר את תנאי הסכם ה-SAFT כדי להמשיך.",
        "alertProceed": "ההסכם נחתם בהצלחה!\n\nנא להעביר {amount} USDT לחשבון האוצר:\n5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3\n\nהקצאת ה-{tokens} $HAISI שלך תחולק אוטומטית ב-TGE.",
        "noWalletDetected": "לא זוהה ארנק Web3 מחובר. נא להדביק את הכתובת ידנית."
    }
}

NEW_GET_CURRENT_LANG = '''  function getCurrentLang() {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const urlLang = urlParams.get('lang');
      if (urlLang) return urlLang.toLowerCase();
    } catch (_) {}
    if (window.haichainI18n && typeof window.haichainI18n.current === 'function') {
      const l = window.haichainI18n.current();
      if (l) return l.toLowerCase();
    }
    if (window.haichainI18n && typeof window.haichainI18n.getLanguage === 'function') {
      const l = window.haichainI18n.getLanguage();
      if (l) return l.toLowerCase();
    }
    try {
      const saved = localStorage.getItem('haichain-lang') || localStorage.getItem('haichain_lang');
      if (saved) return saved.toLowerCase();
    } catch (_) {}
    return (document.documentElement.getAttribute('lang') || 'en').toLowerCase();
  }'''

GLOBAL_HELPERS_AND_LISTENERS = '''
  // =========================================================================
  // GLOBAL MULTI-LANGUAGE SAFT & MEMO RESOLVERS (10 LANGUAGES)
  // =========================================================================
  window.getSaftPdfForLang = function(lang) {
    const l = (lang || getCurrentLang()).toLowerCase();
    const titles = {
      vi: 'Hợp Đồng SAFT Pre-Seed HAICHAIN (Chính Thức)',
      en: 'HAICHAIN Official SAFT Agreement (Mainnet Guaranteed)',
      zh: 'HAICHAIN 官方 SAFT 认购协议 (主网保障)',
      ko: 'HAICHAIN 공식 SAFT 투자 계약서 (메인넷 보장)',
      es: 'Acuerdo SAFT Oficial de HAICHAIN (Garantizado en Mainnet)',
      fr: 'Contrat SAFT Officiel HAICHAIN (Garanti sur le Mainnet)',
      ru: 'Официальное соглашение SAFT HAICHAIN (Гарантия Mainnet)',
      kk: 'HAICHAIN ресми SAFT келісімі (Mainnet кепілдігі)',
      hi: 'HAICHAIN आधिकारिक SAFT अनुबंध (मेननेट गारंटीकृत)',
      he: 'הסכם SAFT רשמי של HAICHAIN (מובטח במיין-נט)'
    };
    const title = titles[l] || titles['en'];
    const validLangs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he'];
    const chosenLang = validLangs.includes(l) ? l.toUpperCase() : 'EN';
    return {
      url: `/HAICHAIN_PRESEED_SAFT_AGREEMENT_${chosenLang}.pdf`,
      title: title
    };
  };

  window.openSaftPdfModal = function(lang) {
    const doc = window.getSaftPdfForLang(lang);
    window.openPdfViewerModal(doc.url, doc.title);
  };

  window.getPreseedMemoPdfForLang = function(lang) {
    const l = (lang || getCurrentLang()).toLowerCase();
    const titles = {
      vi: 'Bản Ghi Nhớ Đầu Tư Chiến Lược Pre-Seed HAICHAIN (1-Pager)',
      en: 'HAICHAIN Pre-Seed Strategic Investment Memo (1-Pager)',
      zh: 'HAICHAIN Pre-Seed 战略投资备忘录 (单页)',
      ko: 'HAICHAIN Pre-Seed 전략 투자 메모 (1-페이저)',
      es: 'Memorando de Inversión Estratégica Pre-Seed de HAICHAIN (1-Página)',
      fr: 'Mémo d’Investissement Stratégique Pre-Seed HAICHAIN (1-Page)',
      ru: 'Инвестиционный меморандум Pre-Seed HAICHAIN (1-Pager)',
      kk: 'HAICHAIN Pre-Seed стратегиялық инвестициялық меморандумы (1-Бет)',
      hi: 'HAICHAIN प्री-सीड रणनीतिक निवेश मेमो (1-पेजर)',
      he: 'תזכיר השקעה אסטרטגי Pre-Seed של HAICHAIN (עמוד אחד)'
    };
    const title = titles[l] || titles['en'];
    const validLangs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he'];
    const chosenLang = validLangs.includes(l) ? l.toUpperCase() : 'EN';
    return {
      url: `/HAICHAIN_PRESEED_ONE_PAGER_MEMO_${chosenLang}.pdf`,
      title: title
    };
  };

  window.openPreseedMemoModal = function(lang) {
    const doc = window.getPreseedMemoPdfForLang(lang);
    window.openPdfViewerModal(doc.url, doc.title);
  };

  // Global Language Synchronization Listener
  window.addEventListener('haichain:languageChanged', (e) => {
    const lang = (e && e.detail && (e.detail.lang || e.detail.language)) || getCurrentLang();
    if (typeof window.refreshSaftDrawerI18n === 'function') {
      window.refreshSaftDrawerI18n(lang);
    }
    const modal = document.getElementById('pdf-modal');
    if (modal && !modal.classList.contains('hidden')) {
      const meta = getI18nMeta(lang);
      const signBtnText = document.getElementById('pdf-modal-sign-btn-text');
      const t = (typeof SAFT_DRAWER_I18N !== 'undefined' && SAFT_DRAWER_I18N[lang]) || (typeof SAFT_DRAWER_I18N !== 'undefined' && SAFT_DRAWER_I18N['en']);
      if (signBtnText && t) signBtnText.textContent = t.btnOpenSign;
      const indicator = document.getElementById('pdf-modal-page-indicator');
      if (indicator && meta.pagePrefix) {
        indicator.textContent = `${meta.pagePrefix} ${currentPageIndex} / ${renderedPages.size || '--'}`;
      }
      // If a multi-language PDF is currently loaded, switch it cleanly!
      if (currentPdfUrl) {
        const u = currentPdfUrl.toUpperCase();
        if (u.includes('WHITEPAPER')) {
          const newUrl = getWhitepaperUrlForLang(lang);
          if (newUrl !== currentPdfUrl) window.openPdfViewerModal(newUrl, meta.title);
        } else if (u.includes('SAFT')) {
          const doc = typeof window.getSaftPdfForLang === 'function' ? window.getSaftPdfForLang(lang) : null;
          if (doc && doc.url !== currentPdfUrl) window.openPdfViewerModal(doc.url, doc.title);
        } else if (u.includes('MEMO')) {
          const doc = typeof window.getPreseedMemoPdfForLang === 'function' ? window.getPreseedMemoPdfForLang(lang) : null;
          if (doc && doc.url !== currentPdfUrl) window.openPdfViewerModal(doc.url, doc.title);
        }
      }
    }
  });

  window.addEventListener('storage', (e) => {
    if (e.key === 'haichain-lang' || e.key === 'haichain_lang') {
      const lang = e.newValue || getCurrentLang();
      if (typeof window.refreshSaftDrawerI18n === 'function') {
        window.refreshSaftDrawerI18n(lang);
      }
    }
  });
'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace getCurrentLang
    old_get_lang = '''  function getCurrentLang() {
    if (window.haichainI18n && typeof window.haichainI18n.getLanguage === 'function') {
      return window.haichainI18n.getLanguage();
    }
    return localStorage.getItem('haichain_lang') || document.documentElement.getAttribute('lang') || 'en';
  }'''
    if old_get_lang not in content:
        print(f"ERROR: old_get_lang not found in {filepath}")
        return False
    content = content.replace(old_get_lang, NEW_GET_CURRENT_LANG)

    # 2. Replace SAFT_DRAWER_I18N
    dict_str = "  const SAFT_DRAWER_I18N = " + json.dumps(SAFT_I18N_10LANG, ensure_ascii=False, indent=2) + ";\n"
    # Find start of SAFT_DRAWER_I18N
    start_tag = "  const SAFT_DRAWER_I18N = {"
    end_tag = "  };\n\n  function initSaftSignatureEngine(modal) {"
    idx_start = content.find(start_tag)
    idx_end = content.find(end_tag)
    if idx_start == -1 or idx_end == -1:
        print(f"ERROR: SAFT_DRAWER_I18N tags not found in {filepath} (start={idx_start}, end={idx_end})")
        return False
    content = content[:idx_start] + dict_str + content[idx_end + len("  };\n"):]

    # 3. Update applyDrawerI18n(overrideLang)
    old_apply = '''    function applyDrawerI18n() {
      const lang = getCurrentLang();
      const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];'''
    new_apply = '''    function applyDrawerI18n(overrideLang) {
      const lang = overrideLang || getCurrentLang();
      const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];'''
    if old_apply not in content:
        print(f"ERROR: old_apply not found in {filepath}")
        return False
    content = content.replace(old_apply, new_apply)

    # 4. In initSaftSignatureEngine, call applyDrawerI18n() immediately
    old_expose = "    window.refreshSaftDrawerI18n = applyDrawerI18n;"
    new_expose = "    applyDrawerI18n();\n    window.refreshSaftDrawerI18n = applyDrawerI18n;"
    if old_expose not in content:
        print(f"ERROR: old_expose not found in {filepath}")
        return False
    content = content.replace(old_expose, new_expose)

    # 5. In openPdfViewerModal, update signBtnText and refresh call
    old_btn_text = '''        const signBtnText = document.getElementById('pdf-modal-sign-btn-text');
        if (signBtnText) {
          signBtnText.textContent = (lang === 'vi') ? 'Ký Hợp Đồng Online' : 'Sign Agreement Online';
        }'''
    new_btn_text = '''        const signBtnText = document.getElementById('pdf-modal-sign-btn-text');
        const t = SAFT_DRAWER_I18N[lang] || SAFT_DRAWER_I18N['en'];
        if (signBtnText && t) {
          signBtnText.textContent = t.btnOpenSign;
        }'''
    if old_btn_text not in content:
        print(f"ERROR: old_btn_text not found in {filepath}")
        return False
    content = content.replace(old_btn_text, new_btn_text)

    # Update isSaftDoc to cover both SAFT and MEMO
    old_is_saft = "const isSaftDoc = String(pdfUrl || '').toUpperCase().includes('SAFT') || String(docTitle || '').toUpperCase().includes('SAFT');"
    new_is_saft = "const uDoc = String(pdfUrl || '').toUpperCase() + ' ' + String(docTitle || '').toUpperCase();\n    const isSaftDoc = uDoc.includes('SAFT') || uDoc.includes('MEMO');"
    if old_is_saft not in content:
        print(f"ERROR: old_is_saft not found in {filepath}")
        return False
    content = content.replace(old_is_saft, new_is_saft)

    content = content.replace(
        "if (typeof window.refreshSaftDrawerI18n === 'function') {\n      window.refreshSaftDrawerI18n();\n    }",
        "if (typeof window.refreshSaftDrawerI18n === 'function') {\n      window.refreshSaftDrawerI18n(lang);\n    }"
    )

    # 6. Append GLOBAL_HELPERS_AND_LISTENERS at the end
    content = content.rstrip() + "\n" + GLOBAL_HELPERS_AND_LISTENERS + "\n"

    # Write out
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully patched {filepath}")
    return True

res1 = update_file('app/pdf-modal.js')
res2 = update_file('pdf-modal.js')

if not (res1 and res2):
    print("FATAL: Patch failed")
    exit(1)

# Validate syntax with node
res = subprocess.run(['node', '-c', 'app/pdf-modal.js'], capture_output=True, text=True)
if res.returncode != 0:
    print("NODE SYNTAX ERROR in app/pdf-modal.js:", res.stderr)
    exit(1)

res = subprocess.run(['node', '-c', 'pdf-modal.js'], capture_output=True, text=True)
if res.returncode != 0:
    print("NODE SYNTAX ERROR in pdf-modal.js:", res.stderr)
    exit(1)

print("ALL FILES PASSED NODE SYNTAX VALIDATION!")
