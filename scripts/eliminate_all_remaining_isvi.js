const fs = require('fs');

const EXTRA_NOTICES = {
  kk: {
    phantomNotDetected: "Браузеріңізде <strong>Phantom кеңейтімі табылмады</strong>. Әмиянды қосу үшін кеңейтімді орнатыңыз.",
    solflareNotDetected: "Браузеріңізде <strong>Solflare кеңейтімі табылмады</strong>. Әмиянды қосу үшін кеңейтімді орнатыңыз.",
    metaMaskNotDetectedFull: "Браузеріңізде <strong>MetaMask кеңейтімі табылмады</strong>. MetaMask қосымшасын орнатыңыз.",
    confirmOnChainDepositPhantom: "On-Chain Салымды Растау (Phantom қолтаңбасы)",
    connectPhantomToDeposit: "Салым Салу Үшін Phantom-ды Қосу",
    metaMaskInsufficientEth: "⚠️ MetaMask Әмиянында Баланс Жеткіліксіз (0 ETH)!\n\nТранзакция үшін ETH қажет.",
    web3ConnectedConfirmPrompt: "Әмиян сәтті қосылды!\n\nТранзакцияға қол қою үшін 'On-Chain Салымды Растау' түймесін басыңыз.",
    noWeb3DetectedFaucetGuide: "Бұл браузерде Web3 әмияны (Phantom немесе Solflare) табылмады.\n\nPhantom орнатыңыз немесе тегін 10 USDT сынақтан өту үшін 'Faucet (+$10)' қойындысын пайдаланыңыз!",
    insufficientSolGaslessGuide: "⚠️ Әмиянда Баланс Жеткіліксіз (0 SOL)!\n\nHAICHAIN Gasless Relayer салымды комиссиясыз автоматты түрде өңдейді.",
    web3DepositConfirmedDevnet: "🎉 Web3 Салымы Сәтті Орындалды!\n\nТранзакция Solana Devnet желісінде расталды.",
    fiatSandboxNotice: "Fiat Төлем Шлюзі туралы хабарлама:\n\nHAICHAIN желісі Solana Devnet сынақ ортасында жұмыс істеуде. Тегін тестілеу үшін 'Faucet (+$10)' қойындысына өтіңіз!",
    zeroBalanceCannotWithdraw: "Master Vault балансы $0.0000 USDT. Шығаратын қаражат жоқ.",
    insufficientWithdrawBalance: "Баланс жеткіліксіз!\n\nMaster Vault балансы сұралған сомадан аз.",
    invalidSolanaAddress: "Тағайындалған әмиян мекенжайы қате!\n\nSolana Base58 жарамды мекенжайын енгізіңіз (32-44 таңба).",
    withdrawSuccessNotice: "Қаражат шығару сәтті аяқталды!\n\nҚаражат әмиянға жіберілді. Өңдеу жылдамдығы: 380мс.",
    vaultBalanceInsufficientForTask: "Master Vault балансы бұл AI тапсырмасы үшін жеткіліксіз. Faucet арқылы толықтырыңыз.",
    aiSecurityKernelHeader: "[HAICHAIN Security Kernel: Қауіпсіздік Талдауы]",
    aiAnchorCodeHeader: "[Solana Anchor Смарт-Келісімшарт Коды]",
    aiEnterpriseAnalysisHeader: "[Кәсіпорын Деңгейіндегі Автономды Талдау]"
  },
  en: {
    phantomNotDetected: "<strong>Phantom extension not detected</strong> in your browser. Please install the extension to connect.",
    solflareNotDetected: "<strong>Solflare extension not detected</strong> in your browser. Please install the extension to connect.",
    metaMaskNotDetectedFull: "<strong>MetaMask extension not detected</strong> in your browser. Please install MetaMask to connect.",
    confirmOnChainDepositPhantom: "Confirm On-Chain Deposit (Sign Phantom)",
    connectPhantomToDeposit: "Connect Phantom to Deposit",
    metaMaskInsufficientEth: "⚠️ MetaMask Balance Insufficient (0 ETH)!\n\nETH is required for network fees.",
    web3ConnectedConfirmPrompt: "Wallet connected successfully!\n\nPlease click 'Confirm On-Chain Deposit' to sign the transaction.",
    noWeb3DetectedFaucetGuide: "Web3 wallet (Phantom or Solflare) not detected in this browser.\n\nPlease install Phantom or switch to the 'Faucet (+$10)' tab to receive free Devnet USDT!",
    insufficientSolGaslessGuide: "⚠️ Wallet Balance Insufficient (0 SOL)!\n\nHAICHAIN Gasless Relayer will sponsor your transaction with 0% gas fees.",
    web3DepositConfirmedDevnet: "🎉 Web3 Deposit Confirmed!\n\nTransaction finalized on Solana Devnet.",
    fiatSandboxNotice: "Fiat Gateway Notice:\n\nHAICHAIN is currently operating on Solana Devnet. Please use the 'Faucet (+$10)' tab to test for free!",
    zeroBalanceCannotWithdraw: "Master Vault balance is $0.0000 USDT. No funds available to withdraw.",
    insufficientWithdrawBalance: "Insufficient balance!\n\nYour Master Vault balance is less than the requested withdrawal amount.",
    invalidSolanaAddress: "Invalid destination address!\n\nPlease enter a valid Solana address (Base58 string of 32-44 characters).",
    withdrawSuccessNotice: "Withdrawal successful!\n\nFunds dispatched to your wallet. Speed: 380ms.",
    vaultBalanceInsufficientForTask: "Master Vault balance is insufficient for this AI task. Please top up via Faucet.",
    aiSecurityKernelHeader: "[HAICHAIN Security Kernel: Sovereign AI Safety Analysis]",
    aiAnchorCodeHeader: "[Solana Anchor Micro-Escrow Instruction Logic]",
    aiEnterpriseAnalysisHeader: "[Enterprise Sovereign Agent Analysis]"
  },
  zh: {
    phantomNotDetected: "您的浏览器<strong>未检测到 Phantom 插件</strong>。请安装插件后连接钱包。",
    solflareNotDetected: "您的浏览器<strong>未检测到 Solflare 插件</strong>。请安装插件后连接钱包。",
    metaMaskNotDetectedFull: "您的浏览器<strong>未检测到 MetaMask 插件</strong>。请安装插件或使用移动端连接。",
    confirmOnChainDepositPhantom: "确认链上充值 (Phantom 签名)",
    connectPhantomToDeposit: "连接 Phantom 钱包进行充值",
    metaMaskInsufficientEth: "⚠️ MetaMask 余额不足 (0 ETH)！\n\n链上交易需要支付网络 Gas 费用。",
    web3ConnectedConfirmPrompt: "钱包连接成功！\n\n请点击“确认链上充值”在钱包中完成交易签名与广播。",
    noWeb3DetectedFaucetGuide: "未在此浏览器中检测到 Web3 钱包 (Phantom 或 Solflare)。\n\n请安装 Phantom 插件，或切换至“水龙头 (+$10)”标签页立即免费领取 10 USDT 测试代币！",
    insufficientSolGaslessGuide: "⚠️ 钱包 SOL 余额不足 (0 SOL)！\n\nHAICHAIN 免 Gas 中继器将自动全额补贴网络手续费。",
    web3DepositConfirmedDevnet: "🎉 Web3 充值确认成功！\n\n交易已在 Solana Devnet 网络上不可篡改地确认。",
    fiatSandboxNotice: "法币支付通道提示：\n\nHAICHAIN 当前运行在 Solana Devnet 环境。请切换至“水龙头 (+$10)”标签免费体验 AI 智能体任务！",
    zeroBalanceCannotWithdraw: "Master Vault 当前余额为 $0.0000 USDT，无可用提现资金。",
    insufficientWithdrawBalance: "可用余额不足！\n\n您的 Master Vault 余额小于请求的提现金额。",
    invalidSolanaAddress: "目标钱包地址格式错误！\n\n请输入有效的 Solana Base58 地址 (32 - 44 位字符)。",
    withdrawSuccessNotice: "提现执行成功！\n\n资金已全额原路结算至您的钱包。响应耗时：380ms。",
    vaultBalanceInsufficientForTask: "Master Vault 可用余额不足以支付此 AI 任务。请通过水龙头免费充值。",
    aiSecurityKernelHeader: "[HAICHAIN 安全内核：专属 AI 防护架构分析]",
    aiAnchorCodeHeader: "[Solana Anchor 微托管智能合约指令代码]",
    aiEnterpriseAnalysisHeader: "[企业级自主智能体推理报告]"
  },
  vi: {
    phantomNotDetected: "<strong>Chưa phát hiện tiện ích Phantom</strong> trên trình duyệt của bạn. Hãy cài đặt extension để kết nối ví.",
    solflareNotDetected: "<strong>Chưa phát hiện tiện ích Solflare</strong> trên trình duyệt của bạn. Hãy cài đặt extension để kết nối ví.",
    metaMaskNotDetectedFull: "<strong>Chưa phát hiện tiện ích MetaMask</strong> trên trình duyệt của bạn. Hãy cài đặt MetaMask để kết nối.",
    confirmOnChainDepositPhantom: "Xác Nhận Nạp On-Chain (Ký Ví Phantom)",
    connectPhantomToDeposit: "Kết Nối Ví Phantom Để Nạp",
    metaMaskInsufficientEth: "⚠️ Số Dư Ví MetaMask Không Đủ (0 ETH)!\n\nCần ETH để trả phí mạng.",
    web3ConnectedConfirmPrompt: "Đã kết nối ví thành công!\n\nVui lòng bấm 'Xác Nhận Nạp On-Chain' để ký và duyệt giao dịch.",
    noWeb3DetectedFaucetGuide: "Chưa phát hiện tiện ích ví Web3 trên trình duyệt này.\n\nHãy cài đặt Phantom hoặc chuyển qua tab 'Faucet (+$10)' để nhận 10 USDT thử nghiệm miễn phí!",
    insufficientSolGaslessGuide: "⚠️ Số Dư Ví Không Đủ (0 SOL)!\n\nHAICHAIN Gasless Relayer đã tự động trợ cấp 0% phí gas cho bạn.",
    web3DepositConfirmedDevnet: "🎉 Nạp Tiền Web3 Thành Công!\n\nGiao dịch đã được xác nhận bất biến trên mạng Solana Devnet.",
    fiatSandboxNotice: "Thông Báo Cổng Thanh Toán Fiat:\n\nHAICHAIN đang vận hành trên Solana Devnet. Vui lòng chuyển qua tab 'Faucet (+$10)' để trải nghiệm miễn phí!",
    zeroBalanceCannotWithdraw: "Số dư trong Master Vault của bạn hiện tại là $0.0000 USDT. Không có khoản tiền nào để rút.",
    insufficientWithdrawBalance: "Số dư không đủ!\n\nSố dư Master Vault nhỏ hơn số tiền bạn muốn rút.",
    invalidSolanaAddress: "Địa chỉ ví đích không hợp lệ!\n\nVui lòng nhập đúng địa chỉ ví Solana hợp lệ (Base58, 32 - 44 ký tự).",
    withdrawSuccessNotice: "Rút tiền thành công!\n\nĐã giải ngân về địa chỉ ví của bạn. Tốc độ xử lý: 380ms.",
    vaultBalanceInsufficientForTask: "Số dư Master Vault không đủ cho tác vụ AI này. Vui lòng nạp thêm qua Faucet Devnet.",
    aiSecurityKernelHeader: "[HAICHAIN Security Kernel: Phân Tích An Toàn AI Độc Quyền]",
    aiAnchorCodeHeader: "[Mã Lệnh Solana Anchor Xác Thực Hợp Đồng Vi Thanh Toán]",
    aiEnterpriseAnalysisHeader: "[Phân Tích Tự Hành Cấp Độ Doanh Nghiệp]"
  },
  ko: {
    phantomNotDetected: "브라우저에서 <strong>Phantom 확장 프로그램이 감지되지 않았습니다</strong>. 지갑을 연결하려면 확장 프로그램을 설치하세요.",
    solflareNotDetected: "브라우저에서 <strong>Solflare 확장 프로그램이 감지되지 않았습니다</strong>. 지갑을 연결하려면 확장 프로그램을 설치하세요.",
    metaMaskNotDetectedFull: "브라우저에서 <strong>MetaMask 확장 프로그램이 감지되지 않았습니다</strong>. MetaMask를 설치하세요.",
    confirmOnChainDepositPhantom: "온체인 입금 확인 (Phantom 서명)",
    connectPhantomToDeposit: "입금할 Phantom 지갑 연결",
    metaMaskInsufficientEth: "⚠️ MetaMask 잔액 부족 (0 ETH)!\n\n네트워크 수수료를 위한 ETH가 필요합니다.",
    web3ConnectedConfirmPrompt: "지갑이 연결되었습니다!\n\n트랜잭션을 승인하려면 '온체인 입금 확인'을 클릭하세요.",
    noWeb3DetectedFaucetGuide: "이 브라우저에서 Web3 지갑을 감지할 수 없습니다.\n\nPhantom을 설치하거나 'Faucet (+$10)' 탭에서 무료 테스트 USDT를 받으세요!",
    insufficientSolGaslessGuide: "⚠️ SOL 잔액 부족 (0 SOL)!\n\nHAICHAIN 가스리스 릴레이어가 수수료를 0%로 지원합니다.",
    web3DepositConfirmedDevnet: "🎉 Web3 입금 확인 완료!\n\nSolana Devnet에서 트랜잭션이 확정되었습니다.",
    fiatSandboxNotice: "법정화폐 결제 안내:\n\nHAICHAIN은 현재 Solana Devnet에서 운영 중입니다. 무료 체험을 위해 'Faucet (+$10)' 탭을 이용해 주세요!",
    zeroBalanceCannotWithdraw: "Master Vault 잔액이 $0.0000 USDT입니다. 출금 가능한 자금이 없습니다.",
    insufficientWithdrawBalance: "잔액 부족!\n\nMaster Vault 잔액이 출금 요청 금액보다 적습니다.",
    invalidSolanaAddress: "유효하지 않은 지갑 주소입니다!\n\n올바른 Solana Base58 주소(32~44자)를 입력하세요.",
    withdrawSuccessNotice: "출금 실행 완료!\n\n지갑으로 즉시 송금되었습니다. 처리 속도: 380ms.",
    vaultBalanceInsufficientForTask: "Master Vault 잔액이 이 AI 작업에 부족합니다. Faucet을 통해 충전하세요.",
    aiSecurityKernelHeader: "[HAICHAIN 보안 커널: 전용 AI 안전 분석]",
    aiAnchorCodeHeader: "[Solana Anchor 마이크로 에스크로 스마트 컨트랙트 코드]",
    aiEnterpriseAnalysisHeader: "[기업용 자율 에이전트 추론 분석]"
  },
  fr: {
    phantomNotDetected: "<strong>Extension Phantom non détectée</strong> dans votre navigateur. Veuillez l'installer pour vous connecter.",
    solflareNotDetected: "<strong>Extension Solflare non détectée</strong> dans votre navigateur. Veuillez l'installer pour vous connecter.",
    metaMaskNotDetectedFull: "<strong>Extension MetaMask non détectée</strong> dans votre navigateur. Veuillez installer MetaMask.",
    confirmOnChainDepositPhantom: "Confirmer le Dépôt On-Chain (Signer Phantom)",
    connectPhantomToDeposit: "Connecter Phantom pour Déposer",
    metaMaskInsufficientEth: "⚠️ Solde MetaMask Insuffisant (0 ETH)!\n\nDes ETH sont requis pour les frais de réseau.",
    web3ConnectedConfirmPrompt: "Portefeuille connecté avec succès !\n\nCliquez sur 'Confirmer le Dépôt On-Chain' pour signer la transaction.",
    noWeb3DetectedFaucetGuide: "Portefeuille Web3 non détecté dans ce navigateur.\n\nInstallez Phantom ou passez à l'onglet 'Faucet (+$10)' pour obtenir 10 USDT de test gratuits !",
    insufficientSolGaslessGuide: "⚠️ Solde SOL Insuffisant (0 SOL)!\n\nLe Relayer Sans Gas HAICHAIN sponsorise vos frais à 0%.",
    web3DepositConfirmedDevnet: "🎉 Dépôt Web3 Confirmé !\n\nTransaction validée sur Solana Devnet.",
    fiatSandboxNotice: "Avis Passerelle Fiat :\n\nHAICHAIN fonctionne actuellement sur Solana Devnet. Utilisez le Faucet pour tester gratuitement !",
    zeroBalanceCannotWithdraw: "Le solde Master Vault est de $0.0000 USDT. Aucun fonds à retirer.",
    insufficientWithdrawBalance: "Solde insuffisant !\n\nVotre solde Master Vault est inférieur au montant demandé.",
    invalidSolanaAddress: "Adresse de destination invalide !\n\nVeuillez saisir une adresse Solana valide (Base58, 32 à 44 caractères).",
    withdrawSuccessNotice: "Retrait réussi !\n\nFonds envoyés vers votre portefeuille. Délai : 380ms.",
    vaultBalanceInsufficientForTask: "Solde Master Vault insuffisant pour cette tâche IA. Veuillez recharger via le Faucet.",
    aiSecurityKernelHeader: "[Noyau de Sécurité HAICHAIN : Analyse de Sûreté IA]",
    aiAnchorCodeHeader: "[Code d'Instruction Micro-Escrow Solana Anchor]",
    aiEnterpriseAnalysisHeader: "[Rapport d'Analyse Autonome Entreprise]"
  },
  es: {
    phantomNotDetected: "<strong>Extensión Phantom no detectada</strong> en su navegador. Instale la extensión para conectar su billetera.",
    solflareNotDetected: "<strong>Extensión Solflare no detectada</strong> en su navegador. Instale la extensión para conectar su billetera.",
    metaMaskNotDetectedFull: "<strong>Extensión MetaMask no detectada</strong> en su navegador. Instale MetaMask para conectar.",
    confirmOnChainDepositPhantom: "Confirmar Depósito On-Chain (Firmar Phantom)",
    connectPhantomToDeposit: "Conectar Phantom para Depositar",
    metaMaskInsufficientEth: "⚠️ ¡Saldo de MetaMask Insuficiente (0 ETH)!\n\nSe requiere ETH para las tarifas de red.",
    web3ConnectedConfirmPrompt: "¡Billetera conectada con éxito!\n\nHaga clic en 'Confirmar Depósito On-Chain' para firmar la transacción.",
    noWeb3DetectedFaucetGuide: "Billetera Web3 no detectada en este navegador.\n\nInstale Phantom o use la pestaña 'Faucet (+$10)' para recibir 10 USDT de prueba gratis.",
    insufficientSolGaslessGuide: "⚠️ ¡Saldo SOL Insuficiente (0 SOL)!\n\nEl Relayer sin Gas de HAICHAIN cubrirá sus tarifas al 0%.",
    web3DepositConfirmedDevnet: "🎉 ¡Depósito Web3 Confirmado!\n\nTransacción finalizada en Solana Devnet.",
    fiatSandboxNotice: "Aviso de Pasarela Fiat:\n\nHAICHAIN opera actualmente en Solana Devnet. ¡Utilice el Faucet para realizar pruebas gratuitas!",
    zeroBalanceCannotWithdraw: "Su saldo en Master Vault es de $0.0000 USDT. No hay fondos para retirar.",
    insufficientWithdrawBalance: "¡Saldo insuficiente!\n\nSu saldo en Master Vault es menor que el monto solicitado.",
    invalidSolanaAddress: "¡Dirección de destino no válida!\n\nIngrese una dirección válida de Solana (Base58, 32-44 caracteres).",
    withdrawSuccessNotice: "¡Retiro exitoso!\n\nFondos enviados a su billetera. Tiempo de procesamiento: 380 ms.",
    vaultBalanceInsufficientForTask: "Saldo insuficiente en Master Vault para esta tarea de IA. Recargue mediante el Faucet.",
    aiSecurityKernelHeader: "[Núcleo de Seguridad HAICHAIN: Análisis de Seguridad de IA]",
    aiAnchorCodeHeader: "[Lógica de Instrucción Micro-Escrow de Solana Anchor]",
    aiEnterpriseAnalysisHeader: "[Análisis de Agentes Autónomos Empresariales]"
  },
  ru: {
    phantomNotDetected: "В вашем браузере <strong>не обнаружено расширение Phantom</strong>. Установите расширение для подключения.",
    solflareNotDetected: "В вашем браузере <strong>не обнаружено расширение Solflare</strong>. Установите расширение для подключения.",
    metaMaskNotDetectedFull: "В вашем браузере <strong>не обнаружено расширение MetaMask</strong>. Установите расширение MetaMask.",
    confirmOnChainDepositPhantom: "Подтвердить Ончейн-Пополнение (Подпись Phantom)",
    connectPhantomToDeposit: "Подключить Phantom для Пополнения",
    metaMaskInsufficientEth: "⚠️ Недостаточно средств в MetaMask (0 ETH)!\n\nТребуется ETH для оплаты сетевой комиссии.",
    web3ConnectedConfirmPrompt: "Кошелек успешно подключен!\n\nНажмите 'Подтвердить Ончейн-Пополнение' для подписания транзакции.",
    noWeb3DetectedFaucetGuide: "Web3 кошелек не обнаружен в браузере.\n\nУстановите Phantom или перейдите во вкладку 'Faucet (+$10)' для получения бесплатных тестовых USDT!",
    insufficientSolGaslessGuide: "⚠️ Недостаточно SOL на балансе (0 SOL)!\n\nБезгазовый релейер HAICHAIN покроет 100% комиссии сети.",
    web3DepositConfirmedDevnet: "🎉 Web3 Пополнение Подтверждено!\n\nТранзакция финализирована в сети Solana Devnet.",
    fiatSandboxNotice: "Уведомление о Фиатном Шлюзе:\n\nHAICHAIN работает в тестовой сети Solana Devnet. Используйте вкладку 'Faucet (+$10)' для бесплатного тестирования!",
    zeroBalanceCannotWithdraw: "Баланс Master Vault составляет $0.0000 USDT. Нет средств для вывода.",
    insufficientWithdrawBalance: "Недостаточный баланс!\n\nБаланс Master Vault меньше запрашиваемой суммы вывода.",
    invalidSolanaAddress: "Некорректный адрес кошелька!\n\nВведите действительный адрес Solana (Base58, 32-44 символа).",
    withdrawSuccessNotice: "Вывод успешно выполнен!\n\nСредства отправлены на ваш кошелек. Скорость: 380 мс.",
    vaultBalanceInsufficientForTask: "Баланса Master Vault недостаточно для этой задачи ИИ. Пополните через Faucet.",
    aiSecurityKernelHeader: "[Ядро Безопасности HAICHAIN: Анализ Безопасности ИИ]",
    aiAnchorCodeHeader: "[Код Инструкции Микро-Эскроу Solana Anchor]",
    aiEnterpriseAnalysisHeader: "[Корпоративный Автономный Анализ]"
  },
  hi: {
    phantomNotDetected: "आपके ब्राउज़र में <strong>Phantom एक्सटेंशन नहीं मिला</strong>। कनेक्ट करने के लिए एक्सटेंशन इंस्टॉल करें।",
    solflareNotDetected: "आपके ब्राउज़र में <strong>Solflare एक्सटेंशन नहीं मिला</strong>। कनेक्ट करने के लिए एक्सटेंशन इंस्टॉल करें।",
    metaMaskNotDetectedFull: "आपके ब्राउज़र में <strong>MetaMask एक्सटेंशन नहीं मिला</strong>। कनेक्ट करने के लिए MetaMask इंस्टॉल करें।",
    confirmOnChainDepositPhantom: "ऑन-चेन जमा की पुष्टि करें (Phantom हस्ताक्षर)",
    connectPhantomToDeposit: "जमा करने के लिए Phantom कनेक्ट करें",
    metaMaskInsufficientEth: "⚠️ MetaMask में अपर्याप्त शेष (0 ETH)!\n\nनेटवर्क शुल्क के लिए ETH आवश्यक है।",
    web3ConnectedConfirmPrompt: "वॉलेट सफलतापूर्वक कनेक्ट हुआ!\n\nलेनदेन पर हस्ताक्षर करने के लिए 'ऑन-चेन जमा की पुष्टि करें' पर क्लिक करें।",
    noWeb3DetectedFaucetGuide: "इस ब्राउज़र में Web3 वॉलेट नहीं मिला।\n\nकृपया Phantom इंस्टॉल करें या मुफ्त Devnet USDT के लिए 'Faucet (+$10)' टैब पर जाएं!",
    insufficientSolGaslessGuide: "⚠️ वॉलेट में अपर्याप्त SOL (0 SOL)!\n\nHAICHAIN गैसलेस रिलेयर 0% गैस शुल्क के साथ प्रायोजित करेगा।",
    web3DepositConfirmedDevnet: "🎉 Web3 जमा की पुष्टि हुई!\n\nSolana Devnet पर लेनदेन अंतिम रूप से पूरा हुआ।",
    fiatSandboxNotice: "फ़िएट गेटवे सूचना:\n\nHAICHAIN वर्तमान में Solana Devnet पर चल रहा है। मुफ्त परीक्षण के लिए फॉसेट का उपयोग करें!",
    zeroBalanceCannotWithdraw: "Master Vault का शेष $0.0000 USDT है। निकासी के लिए कोई फंड नहीं है।",
    insufficientWithdrawBalance: "अपर्याप्त शेष!\n\nआपका वॉल्ट शेष अनुरोधित निकासी राशि से कम है।",
    invalidSolanaAddress: "अमान्य गंतव्य पता!\n\nकृपया एक वैध Solana पता दर्ज करें (32-44 वर्ण)।",
    withdrawSuccessNotice: "निकासी सफल!\n\nफंड आपके वॉलेट में भेज दिया गया है। गति: 380ms।",
    vaultBalanceInsufficientForTask: "इस AI कार्य के लिए वॉल्ट में अपर्याप्त शेष है। फॉसेट से टॉप अप करें।",
    aiSecurityKernelHeader: "[HAICHAIN सुरक्षा कर्नेल: AI सुरक्षा विश्लेषण]",
    aiAnchorCodeHeader: "[Solana Anchor माइक्रो-एस्क्रो निर्देश कोड]",
    aiEnterpriseAnalysisHeader: "[एंटरप्राइज स्वायत्त एजेंट विश्लेषण]"
  },
  he: {
    phantomNotDetected: "<strong>תוסף Phantom לא זוהה</strong> בדפדפן שלך. אנא התקן את התוסף כדי להתחבר.",
    solflareNotDetected: "<strong>תוסף Solflare לא זוהה</strong> בדפדפן שלך. אנא התקן את התוסף כדי להתחבר.",
    metaMaskNotDetectedFull: "<strong>תוסף MetaMask לא זוהה</strong> בדפדפן שלך. אנא התקן את MetaMask כדי להתחבר.",
    confirmOnChainDepositPhantom: "אשר הפקדה ברשת (חתימת Phantom)",
    connectPhantomToDeposit: "חבר את Phantom להפקדה",
    metaMaskInsufficientEth: "⚠️ יתרת MetaMask אינה מספקת (0 ETH)!\n\nנדרש ETH לתשלום עמלות הרשת.",
    web3ConnectedConfirmPrompt: "הארנק חובר בהצלחה!\n\nאנא לחץ על 'אשר הפקדה ברשת' לחתימה על העסקה.",
    noWeb3DetectedFaucetGuide: "לא זוהה ארנק Web3 בדפדפן זה.\n\nהתקן את Phantom או עבור לכרטיסיית 'Faucet (+$10)' לקבלת USDT חינם ברשת הבדיקה!",
    insufficientSolGaslessGuide: "⚠️ יתרת SOL אינה מספקת (0 SOL)!\n\nממסר ה-Gasless של HAICHAIN יממן את העמלות ב-0%.",
    web3DepositConfirmedDevnet: "🎉 הפקדת Web3 אושרה!\n\nהעסקה אושרה ברשת Solana Devnet.",
    fiatSandboxNotice: "הודעת שער פיאט:\n\nHAICHAIN פועל כעת ברשת Solana Devnet. השתמש בברז לבדיקות חינם!",
    zeroBalanceCannotWithdraw: "יתרת ה-Master Vault היא $0.0000 USDT. אין כספים למשיכה.",
    insufficientWithdrawBalance: "יתרה לא מספקת!\n\nיתרת ה-Master Vault שלך נמוכה מסכום המשיכה המבוקש.",
    invalidSolanaAddress: "כתובת יעד לא תקינה!\n\nאנא הזן כתובת Solana תקינה (Base58, 32-44 תווים).",
    withdrawSuccessNotice: "המשיכה בוצעה בהצלחה!\n\nהכספים נשלחו לארנק שלך. מהירות עיבוד: 380ms.",
    vaultBalanceInsufficientForTask: "יתרת ה-Master Vault אינה מספקת למשימת AI זו. טען מחדש דרך הברז.",
    aiSecurityKernelHeader: "[גרעין האבטחה של HAICHAIN: ניתוח בטיחות AI]",
    aiAnchorCodeHeader: "[קוד הוראות מיקרו-אסקרו של Solana Anchor]",
    aiEnterpriseAnalysisHeader: "[דוח ניתוח סוכנים אוטונומיים]"
  }
};

function patchFile(filePath) {
  let html = fs.readFileSync(filePath, 'utf8');

  // Inject EXTRA_NOTICES into DASH_NOTICES_I18N
  for (const [lang, map] of Object.entries(EXTRA_NOTICES)) {
    const langToken = `"${lang}": {`;
    const idx = html.indexOf(langToken);
    if (idx !== -1) {
      let inject = '\n';
      for (const [k, v] of Object.entries(map)) {
        inject += `      "${k}": ${JSON.stringify(v)},\n`;
      }
      const insertPoint = idx + langToken.length;
      html = html.substring(0, insertPoint) + inject + html.substring(insertPoint);
    }
  }

  // Add data-i18n to Quick Demos & 4 demo buttons
  html = html.replace(/<span>Quick Demos<\/span>/g, `<span data-i18n="playground.quickDemos">Quick Demos</span>`);
  html = html.replace(/<span class="truncate">Anti-Drain<\/span>/g, `<span class="truncate" data-i18n="playground.demoAntiDrain">Anti-Drain</span>`);
  html = html.replace(/<span class="truncate">Micro-Escrow<\/span>/g, `<span class="truncate" data-i18n="playground.demoMicroEscrow">Micro-Escrow</span>`);
  html = html.replace(/<span class="truncate">Optimus AI<\/span>/g, `<span class="truncate" data-i18n="playground.demoOptimus">Optimus AI</span>`);
  html = html.replace(/<span class="truncate">Anchor CPI<\/span>/g, `<span class="truncate" data-i18n="playground.demoAnchor">Anchor CPI</span>`);

  // Replace multiline isVi checks
  html = html.replace(/walletNoticeText\.innerHTML = isVi\s*\?\s*"<strong>Chưa phát hiện tiện ích Phantom<\/strong>[^"]*"\s*:\s*"<strong>Phantom extension not detected<\/strong>[^"]*";/g,
    `walletNoticeText.innerHTML = getDashNotice('phantomNotDetected');`);

  html = html.replace(/walletNoticeText\.innerHTML = isVi\s*\?\s*"<strong>Chưa phát hiện tiện ích MetaMask<\/strong>[^"]*"\s*:\s*"<strong>MetaMask extension not detected<\/strong>[^"]*";/g,
    `walletNoticeText.innerHTML = getDashNotice('metaMaskNotDetectedFull');`);

  html = html.replace(/walletNoticeText\.innerHTML = isVi\s*\?\s*"<strong>Chưa phát hiện tiện ích Solflare<\/strong>[^"]*"\s*:\s*"<strong>Solflare extension not detected<\/strong>[^"]*";/g,
    `walletNoticeText.innerHTML = getDashNotice('solflareNotDetected');`);

  html = html.replace(/dashConfirmDepositBtn\.textContent = isVi\s*\?\s*"Xác Nhận Nạp On-Chain \(Ký Ví Phantom\)"\s*:\s*"Confirm On-Chain Deposit \(Sign Phantom\)";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('confirmOnChainDepositPhantom');`);

  html = html.replace(/dashConfirmDepositBtn\.textContent = isVi\s*\?\s*"Kết Nối Ví Phantom Để Nạp"\s*:\s*"Connect Phantom to Deposit";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('connectPhantomToDeposit');`);

  html = html.replace(/alert\(isVi\s*\?\s*`⚠️ Số Dư Ví MetaMask Không Đủ \(0 ETH\)![\s\S]*?`\s*:\s*`⚠️ MetaMask Balance Insufficient \(0 ETH\)![\s\S]*?`\);/g,
    `alert(getDashNotice('metaMaskInsufficientEth'));`);

  html = html.replace(/alert\(isVi\s*\?\s*`Đã kết nối ví \$\{userWallet\.provider\} thành công![\s\S]*?`\s*:\s*`Connected \$\{userWallet\.provider\} wallet successfully![\s\S]*?`\);/g,
    `alert(getDashNotice('web3ConnectedConfirmPrompt'));`);

  html = html.replace(/alert\(isVi\s*\?\s*"Chưa phát hiện tiện ích ví Web3 \(Phantom hoặc Solflare\)[\s\S]*?"\s*:\s*"Web3 wallet \(Phantom or Solflare\) not detected[\s\S]*?"\);/g,
    `alert(getDashNotice('noWeb3DetectedFaucetGuide'));`);

  html = html.replace(/alert\(isVi\s*\?\s*`⚠️ Số Dư Ví \$\{userWallet\.provider\} Không Đủ \(0 SOL\)![\s\S]*?`\s*:\s*`⚠️ Insufficient SOL in \$\{userWallet\.provider\} \(0 SOL\)![\s\S]*?`\);/g,
    `alert(getDashNotice('insufficientSolGaslessGuide'));`);

  html = html.replace(/alert\(isVi\s*\?\s*`🎉 Nạp Tiền Web3 Thành Công!\s*\\n\\nGiao dịch đã được xác nhận bất biến trên mạng Solana Devnet\.[\s\S]*?`\s*:\s*`🎉 Web3 Deposit Confirmed![\s\S]*?`\);/g,
    `alert(getDashNotice('web3DepositConfirmedDevnet'));`);

  html = html.replace(/alert\(isVi\s*\?\s*`Thông Báo Cổng Thanh Toán Fiat[\s\S]*?`\s*:\s*`Fiat Gateway Notice[\s\S]*?`\);/g,
    `alert(getDashNotice('fiatSandboxNotice'));`);

  html = html.replace(/alert\(isVi\s*\?\s*"Số dư trong Master Vault của bạn hiện tại là \$0\.0000 USDT[\s\S]*?"\s*:\s*"Your Master Vault balance is \$0\.0000 USDT[\s\S]*?"\);/g,
    `alert(getDashNotice('zeroBalanceCannotWithdraw'));`);

  html = html.replace(/alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault hiện tại của bạn là \$[\s\S]*?`\s*:\s*`Insufficient balance![\s\S]*?`\);/g,
    `alert(getDashNotice('insufficientWithdrawBalance'));`);

  html = html.replace(/alert\(isVi\s*\?\s*"Địa chỉ ví đích không hợp lệ![\s\S]*?"\s*:\s*"Invalid destination address![\s\S]*?"\);/g,
    `alert(getDashNotice('invalidSolanaAddress'));`);

  html = html.replace(/alert\(isVi\s*\?\s*`Rút tiền thành công!\\n\\nĐã giải ngân[\s\S]*?`\s*:\s*`Withdrawal successful![\s\S]*?`\);/g,
    `alert(getDashNotice('withdrawSuccessNotice'));`);

  html = html.replace(/alert\(isVi\s*\?\s*`Số dư không đủ!\\n\\nSố dư Master Vault của bạn hiện tại là \$[\s\S]*?để tiếp tục\.`\s*:\s*`Insufficient balance![\s\S]*?to continue\.`\);/g,
    `alert(getDashNotice('vaultBalanceInsufficientForTask'));`);

  html = html.replace(/generatedResponse = isVi\s*\?\s*`\[HAICHAIN Security Kernel: Phân Tích An Toàn AI Độc Quyền\]/g,
    `generatedResponse = \`\${getDashNotice('aiSecurityKernelHeader')}`);

  html = html.replace(/generatedResponse = isVi\s*\?\s*`\[Mã Lệnh Solana Anchor Xác Thực Hợp Đồng Vi Thanh Toán\]/g,
    `generatedResponse = \`\${getDashNotice('aiAnchorCodeHeader')}`);

  html = html.replace(/generatedResponse = isVi\s*\?\s*`\[Phân Tích Tự Hành Cấp Độ Doanh Nghiệp qua \$\{selectedModel\}\]/g,
    `generatedResponse = \`\${getDashNotice('aiEnterpriseAnalysisHeader')}`);

  fs.writeFileSync(filePath, html, 'utf8');
  console.log('Processed:', filePath);
}

patchFile('dashboard.html');
patchFile('app/dashboard.html');
