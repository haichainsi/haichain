const fs = require('fs');

const NOTICES_DICT = {
  kk: {
    tabStrategic: "Стратегиялық VIP Бөлініс",
    passkeyTitle: "Биометриялық Passkey Әмияны",
    passkeySubtitle: "WebAuthn аппараттық растауы • Абсолютті қауіпсіздік",
    syncChrome: "Chrome браузеріне синхрондау",
    openingPhantom: "Phantom ашылуда...",
    openingPhantomTitle: "Phantom Қосымшасы Ашылуда...",
    approvePhantomMsg: "Chrome-ға оралу үшін Phantom-да рұқсат беріңіз",
    openingSolflare: "Solflare ашылуда...",
    openingSolflareTitle: "Solflare Қосымшасы Ашылуда...",
    approveSolflareMsg: "Chrome-ға оралу үшін Solflare-де рұқсат беріңіз",
    scanningBio: "Биометрия тексерілуде...",
    passkeyConnected: "Passkey Сәтті Қосылды",
    bioError: "Биометриялық Қате",
    connectingPhantom: "Phantom-ға қосылуда...",
    connectingMetaMask: "MetaMask-қа қосылуда...",
    connectingSolflare: "Solflare-ге қосылуда...",
    connectionRejected: "Пайдаланушы байланысты тоқтатты",
    resetSimulationConfirm: "Бұл әмиян үшін үлгі бөлініс деректерін қалпына келтіру керек пе?",
    activeVestingVault: "Белсенді Token-2022 Вестинг Сейфі",
    angelTranche: "Періштелер Траншы",
    openMyVestingVault: "Менің Вестинг Сейфіме Өту →",
    connectedCheck: "Қосылды ✓",
    passkeyActiveDeposit: "Passkey Қосулы • Толықтыру үшін Phantom/Solflare-ді қосыңыз",
    connectPhantomBtn: "Phantom-ды Қосу",
    connectingBtn: "Қосылуда...",
    walletNotConnected: "Әмиян Қосылмаған",
    connectWalletBeforeDeposit: "Қаражат салмас бұрын Passkey немесе Phantom әмиянын қосыңыз.",
    enterValidDeposit: "Жарамды салым сомасын енгізіңіз (> 0).",
    broadcastingFaucet: "Solana Devnet Faucet транзакциясы жіберілуде...",
    faucetClaimed: "Сынақ Faucet Қабылданды",
    faucetCredited: "Devnet Master Vault-қа қаражат сәтті қосылды!",
    connectingPhantomWallet: "Phantom әмиянына қосылуда...",
    web3Rejected: "Web3 әмиян қосылымынан бас тартылды.",
    web3Disconnected: "Web3 әмияны ажыратылды. Phantom-ды қайта қосыңыз.",
    awaitingSignature: "Әмиянда қол қоюды растаңыз...",
    gaslessDepositSuccess: "Комиссиясыз Салым Сәтті Аяқталды (0% Gas)",
    depositCredited: "Master Vault-қа қаражат түсті!",
    approveInPhantomExt: "Phantom кеңейтімінде растаңыз...",
    confirmingSolana: "Solana Devnet-те расталуда...",
    web3DepositSuccess: "Web3 Салымы Сәтті Расталды",
    depositCanceledUser: "Салым тоқтатылды: Әмиянда транзакциядан бас тарттыңыз.",
    solanaTxFailed: "Solana Devnet транзакциясы сәтсіз аяқталды:",
    cannotWithdrawEmergency: "Vault Апаттық Жағдайда (Emergency Stop) болған кезде қаражат шығару мүмкін емес.",
    connectWalletBeforeWithdraw: "Қаражат шығармас бұрын расталған әмиянды қосыңыз.",
    zeroBalance: "Нөлдік Баланс",
    zeroBalanceMsg: "Master Vault балансы $0.0000 USDT. Шығаратын қаражат жоқ.",
    enterValidWithdraw: "Жарамды шығару сомасын енгізіңіз (> 0).",
    withdrawCanceledMetaMask: "Шығару тоқтатылды: MetaMask-та қол қоюдан бас тарттыңыз.",
    withdrawCanceled: "Шығару тоқтатылды: Әмиянда қол қоюдан бас тарттыңыз.",
    withdrawSuccess: "Қаражат Шығару Сәтті Орындалды",
    walletRequiredAi: "AI-ді орындау үшін Passkey немесе Phantom әмиянын қосыңыз.",
    insufficientVaultBalance: "Vault Балансы Жеткіліксіз"
  },
  en: {
    tabStrategic: "Private Strategic Allocation",
    passkeyTitle: "Passkey Biometric Wallet",
    passkeySubtitle: "Hardware-Bound WebAuthn • Zero Key Risk",
    syncChrome: "Sync Wallet to Chrome Browser",
    openingPhantom: "Opening Phantom...",
    openingPhantomTitle: "Opening Phantom App...",
    approvePhantomMsg: "Approve in Phantom to return to Chrome",
    openingSolflare: "Opening Solflare...",
    openingSolflareTitle: "Opening Solflare App...",
    approveSolflareMsg: "Approve in Solflare to return to Chrome",
    scanningBio: "Scanning Biometric...",
    passkeyConnected: "Passkey Connected Successfully",
    bioError: "Biometric Error",
    connectingPhantom: "Connecting Phantom...",
    connectingMetaMask: "Connecting MetaMask...",
    connectingSolflare: "Connecting Solflare...",
    connectionRejected: "Connection rejected by user",
    resetSimulationConfirm: "Reset simulation allocation for this wallet?",
    activeVestingVault: "Active Token-2022 Vesting Vault",
    angelTranche: "Angel Tranche",
    openMyVestingVault: "Open My Vesting Vault →",
    connectedCheck: "Connected ✓",
    passkeyActiveDeposit: "Passkey Active • Connect Phantom/Solflare to Deposit",
    connectPhantomBtn: "Connect Phantom",
    connectingBtn: "Connecting...",
    walletNotConnected: "Wallet Not Connected",
    connectWalletBeforeDeposit: "Please connect a Passkey or Phantom wallet before depositing.",
    enterValidDeposit: "Please enter a valid deposit amount (> 0).",
    broadcastingFaucet: "Broadcasting Solana Devnet Faucet Tx...",
    faucetClaimed: "Testnet Faucet Claimed",
    faucetCredited: "Faucet Credited to Master Vault!",
    connectingPhantomWallet: "Connecting Phantom Wallet...",
    web3Rejected: "Web3 wallet connection was canceled or rejected.",
    web3Disconnected: "Web3 wallet disconnected. Please reconnect Phantom.",
    awaitingSignature: "Awaiting signature in wallet...",
    gaslessDepositSuccess: "Gasless Deposit Confirmed (0% Gas)",
    depositCredited: "Credited to Master Vault!",
    approveInPhantomExt: "Approve in Phantom extension...",
    confirmingSolana: "Confirming on Solana Devnet...",
    web3DepositSuccess: "Web3 Deposit Confirmed",
    depositCanceledUser: "Deposit Canceled: You rejected the transaction in your wallet.",
    solanaTxFailed: "Solana Devnet transaction failed:",
    cannotWithdrawEmergency: "Cannot withdraw while Vault is in Emergency Stop state.",
    connectWalletBeforeWithdraw: "Please connect a verified wallet before withdrawing.",
    zeroBalance: "Zero Balance",
    zeroBalanceMsg: "Your Master Vault balance is $0.0000 USDT. No funds available to withdraw.",
    enterValidWithdraw: "Please enter a valid withdrawal amount (> 0).",
    withdrawCanceledMetaMask: "Withdrawal Canceled: You rejected the MetaMask authorization signature.",
    withdrawCanceled: "Withdrawal Canceled: You rejected the cryptographic authorization signature.",
    withdrawSuccess: "Withdrawal Executed",
    walletRequiredAi: "Connect your sovereign wallet to authorize AI execution.",
    insufficientVaultBalance: "Insufficient Vault Balance"
  },
  zh: {
    tabStrategic: "机密战略分配",
    passkeyTitle: "生物识别 Passkey 钱包",
    passkeySubtitle: "WebAuthn 硬件级加密验证 • 零私钥泄露风险",
    syncChrome: "同步钱包至 Chrome 浏览器",
    openingPhantom: "正在打开 Phantom...",
    openingPhantomTitle: "正在调起 Phantom 客户端...",
    approvePhantomMsg: "请在 Phantom 中完成授权以返回 Chrome",
    openingSolflare: "正在打开 Solflare...",
    openingSolflareTitle: "正在调起 Solflare 客户端...",
    approveSolflareMsg: "请在 Solflare 中完成授权以返回 Chrome",
    scanningBio: "正在扫描生物识别特征...",
    passkeyConnected: "Passkey 验证连接成功",
    bioError: "生物识别验证失败",
    connectingPhantom: "正在连接 Phantom 钱包...",
    connectingMetaMask: "正在连接 MetaMask 钱包...",
    connectingSolflare: "正在连接 Solflare 钱包...",
    connectionRejected: "用户已取消连接",
    resetSimulationConfirm: "确定要重置该钱包的模拟认购分配数据吗？",
    activeVestingVault: "活跃的 Token-2022 锁仓金库",
    angelTranche: "天使轮份额",
    openMyVestingVault: "进入我的锁仓金库 →",
    connectedCheck: "已连接 ✓",
    passkeyActiveDeposit: "Passkey 已启用 • 连接 Phantom/Solflare 进行链上入金",
    connectPhantomBtn: "连接 Phantom",
    connectingBtn: "连接中...",
    walletNotConnected: "未连接钱包",
    connectWalletBeforeDeposit: "充值前请先连接 Passkey 或 Phantom 钱包。",
    enterValidDeposit: "请输入有效的充值金额 (> 0)。",
    broadcastingFaucet: "正在广播 Solana Devnet 水龙头交易...",
    faucetClaimed: "测试网水龙头领取成功",
    faucetCredited: "水龙头代币已成功充入 Master Vault！",
    connectingPhantomWallet: "正在连接 Phantom 钱包...",
    web3Rejected: "Web3 钱包连接已取消或被拒绝。",
    web3Disconnected: "Web3 钱包已断开连接，请重新连接 Phantom。",
    awaitingSignature: "正在等待钱包内确认签名...",
    gaslessDepositSuccess: "零 Gas 充值已确认 (0% 手续费)",
    depositCredited: "资金已入账至 Master Vault！",
    approveInPhantomExt: "请在 Phantom 扩展程序中确认...",
    confirmingSolana: "Solana Devnet 区块链确认中...",
    web3DepositSuccess: "Web3 充值确认成功",
    depositCanceledUser: "充值已取消：您在钱包中拒绝了该笔交易。",
    solanaTxFailed: "Solana Devnet 链上交易失败：",
    cannotWithdrawEmergency: "金库当前处于紧急熔断状态 (Emergency Stop)，禁止提现。",
    connectWalletBeforeWithdraw: "提现前请先连接已验证的钱包地址。",
    zeroBalance: "余额为零",
    zeroBalanceMsg: "您的 Master Vault 余额为 $0.0000 USDT，暂无可提现金额。",
    enterValidWithdraw: "请输入有效的提现金额 (> 0)。",
    withdrawCanceledMetaMask: "提现已取消：您拒绝了 MetaMask 授权签名。",
    withdrawCanceled: "提现已取消：您拒绝了密码学授权签名。",
    withdrawSuccess: "提现执行成功",
    walletRequiredAi: "请连接 Passkey 或 Phantom 钱包以授权 AI 推理执行。",
    insufficientVaultBalance: "金库可用余额不足"
  },
  vi: {
    tabStrategic: "Phân Bổ Chiến Lược VIP",
    passkeyTitle: "Ví Sinh Trắc Học Passkey",
    passkeySubtitle: "Xác thực phần cứng WebAuthn • An toàn tuyệt đối",
    syncChrome: "Đồng bộ sang trình duyệt Chrome",
    openingPhantom: "Đang mở Phantom...",
    openingPhantomTitle: "Đang mở Phantom App...",
    approvePhantomMsg: "Cấp quyền trong Phantom để quay lại Chrome",
    openingSolflare: "Đang mở Solflare...",
    openingSolflareTitle: "Đang mở Solflare App...",
    approveSolflareMsg: "Cấp quyền trong Solflare để quay lại Chrome",
    scanningBio: "Quét sinh trắc học...",
    passkeyConnected: "Xác Thực Passkey Thành Công",
    bioError: "Lỗi xác thực sinh trắc học",
    connectingPhantom: "Đang kết nối Phantom...",
    connectingMetaMask: "Đang kết nối MetaMask...",
    connectingSolflare: "Đang kết nối Solflare...",
    connectionRejected: "Người dùng đã hủy kết nối",
    resetSimulationConfirm: "Bạn có muốn đặt lại dữ liệu phân bổ mẫu cho ví này?",
    activeVestingVault: "Két Vesting Token-2022 Đang Hoạt Động",
    angelTranche: "Khối Thiên Thần",
    openMyVestingVault: "Truy Cập Két Vesting Của Tôi →",
    connectedCheck: "Đã Kết Nối ✓",
    passkeyActiveDeposit: "Passkey Đang Bật • Kết Nối Phantom để Nạp On-Chain",
    connectPhantomBtn: "Kết Nối Phantom",
    connectingBtn: "Đang kết nối...",
    walletNotConnected: "Chưa kết nối ví",
    connectWalletBeforeDeposit: "Vui lòng kết nối ví Passkey hoặc Phantom trước khi nạp tiền.",
    enterValidDeposit: "Vui lòng nhập số tiền nạp hợp lệ (> 0).",
    broadcastingFaucet: "Đang gửi giao dịch Solana Devnet Faucet...",
    faucetClaimed: "Nhận Testnet Faucet Thành Công",
    faucetCredited: "Đã nạp USDT Devnet vào Master Vault!",
    connectingPhantomWallet: "Đang kết nối ví Phantom...",
    web3Rejected: "Bạn đã từ chối kết nối ví Web3.",
    web3Disconnected: "Ví Web3 bị ngắt kết nối. Vui lòng kết nối lại ví Phantom.",
    awaitingSignature: "Vui lòng duyệt giao dịch trên ví...",
    gaslessDepositSuccess: "Nạp Tiền Thành Công (0% Gas)",
    depositCredited: "Đã nạp tiền vào Master Vault!",
    approveInPhantomExt: "Chờ bạn bấm Duyệt trên Phantom...",
    confirmingSolana: "Đang xác thực trên Solana Devnet...",
    web3DepositSuccess: "Nạp Web3 Thành Công",
    depositCanceledUser: "Giao dịch đã hủy: Bạn đã từ chối duyệt giao dịch trên ví.",
    solanaTxFailed: "Giao dịch thất bại trên Solana Devnet:",
    cannotWithdrawEmergency: "Không thể rút tiền khi Vault đang ở trạng thái Khẩn cấp (Emergency Stop).",
    connectWalletBeforeWithdraw: "Vui lòng kết nối ví trước khi thực hiện rút tiền.",
    zeroBalance: "Số dư bằng 0",
    zeroBalanceMsg: "Số dư Master Vault của bạn là $0.0000 USDT. Không có khoản tiền nào để rút.",
    enterValidWithdraw: "Vui lòng nhập số tiền rút hợp lệ (> 0).",
    withdrawCanceledMetaMask: "Rút tiền đã hủy: Bạn đã từ chối ký xác thực giao dịch trên ví MetaMask.",
    withdrawCanceled: "Rút tiền đã hủy: Bạn đã từ chối ký xác thực giao dịch trên ví.",
    withdrawSuccess: "Rút Tiền Thành Công",
    walletRequiredAi: "Vui lòng kết nối ví Passkey hoặc Phantom để cấp quyền thực thi AI.",
    insufficientVaultBalance: "Số dư không đủ"
  },
  ko: {
    tabStrategic: "프라이빗 전략 배분",
    passkeyTitle: "생체 인식 Passkey 지갑",
    passkeySubtitle: "WebAuthn 하드웨어 인증 • 제로 키 리스크",
    syncChrome: "Chrome 브라우저로 지갑 동기화",
    openingPhantom: "Phantom 실행 중...",
    openingPhantomTitle: "Phantom 앱 여는 중...",
    approvePhantomMsg: "Chrome으로 돌아가려면 Phantom에서 승인하세요",
    openingSolflare: "Solflare 실행 중...",
    openingSolflareTitle: "Solflare 앱 여는 중...",
    approveSolflareMsg: "Chrome으로 돌아가려면 Solflare에서 승인하세요",
    scanningBio: "생체 인식 스캔 중...",
    passkeyConnected: "Passkey 인증 연결 성공",
    bioError: "생체 인식 오류",
    connectingPhantom: "Phantom 지갑 연결 중...",
    connectingMetaMask: "MetaMask 지갑 연결 중...",
    connectingSolflare: "Solflare 지갑 연결 중...",
    connectionRejected: "사용자가 연결을 취소했습니다",
    resetSimulationConfirm: "이 지갑의 모의 배분 데이터를 초기화하시겠습니까?",
    activeVestingVault: "활성 Token-2022 베스팅 볼트",
    angelTranche: "엔젤 트랜치",
    openMyVestingVault: "내 베스팅 볼트 열기 →",
    connectedCheck: "연결됨 ✓",
    passkeyActiveDeposit: "Passkey 활성 • 온체인 입금을 위해 Phantom/Solflare 연결",
    connectPhantomBtn: "Phantom 연결",
    connectingBtn: "연결 중...",
    walletNotConnected: "지갑 미연결",
    connectWalletBeforeDeposit: "입금하기 전에 Passkey 또는 Phantom 지갑을 연결하세요.",
    enterValidDeposit: "유효한 입금 금액(> 0)을 입력하세요.",
    broadcastingFaucet: "Solana Devnet Faucet 트랜잭션 전송 중...",
    faucetClaimed: "테스트넷 Faucet 수령 완료",
    faucetCredited: "Master Vault에 Faucet 잔액이 입금되었습니다!",
    connectingPhantomWallet: "Phantom 지갑 연결 중...",
    web3Rejected: "Web3 지갑 연결이 취소되었습니다.",
    web3Disconnected: "Web3 지갑 연결이 끊어졌습니다. Phantom을 다시 연결하세요.",
    awaitingSignature: "지갑에서 서명 승인을 기다리는 중...",
    gaslessDepositSuccess: "무가스 입금 완료 (0% 가스비)",
    depositCredited: "Master Vault에 입금 완료되었습니다!",
    approveInPhantomExt: "Phantom 확장 프로그램에서 승인하세요...",
    confirmingSolana: "Solana Devnet 확인 중...",
    web3DepositSuccess: "Web3 입금 확인 완료",
    depositCanceledUser: "입금 취소: 지갑에서 트랜잭션을 거부했습니다.",
    solanaTxFailed: "Solana Devnet 트랜잭션 실패:",
    cannotWithdrawEmergency: "Vault가 긴급 정지(Emergency Stop) 상태일 때는 출금할 수 없습니다.",
    connectWalletBeforeWithdraw: "출금하기 전에 인증된 지갑을 연결하세요.",
    zeroBalance: "잔액 없음",
    zeroBalanceMsg: "Master Vault 잔액이 $0.0000 USDT입니다. 출금 가능한 자금이 없습니다.",
    enterValidWithdraw: "유효한 출금 금액(> 0)을 입력하세요.",
    withdrawCanceledMetaMask: "출금 취소: MetaMask 서명을 거부했습니다.",
    withdrawCanceled: "출금 취소: 지갑 서명을 거부했습니다.",
    withdrawSuccess: "출금 실행 완료",
    walletRequiredAi: "AI 실행을 승인하려면 Passkey 또는 Phantom 지갑을 연결하세요.",
    insufficientVaultBalance: "Vault 잔액 부족"
  },
  fr: {
    tabStrategic: "Allocation Stratégique Privée",
    passkeyTitle: "Portefeuille Biométrique Passkey",
    passkeySubtitle: "Authentification WebAuthn • Sécurité Matérielle Absolue",
    syncChrome: "Synchroniser avec Chrome",
    openingPhantom: "Ouverture de Phantom...",
    openingPhantomTitle: "Ouverture de l'Application Phantom...",
    approvePhantomMsg: "Approuvez dans Phantom pour revenir à Chrome",
    openingSolflare: "Ouverture de Solflare...",
    openingSolflareTitle: "Ouverture de l'Application Solflare...",
    approveSolflareMsg: "Approuvez dans Solflare pour revenir à Chrome",
    scanningBio: "Numérisation biométrique...",
    passkeyConnected: "Passkey Connecté avec Succès",
    bioError: "Erreur Biométrique",
    connectingPhantom: "Connexion à Phantom...",
    connectingMetaMask: "Connexion à MetaMask...",
    connectingSolflare: "Connexion à Solflare...",
    connectionRejected: "Connexion rejetée par l'utilisateur",
    resetSimulationConfirm: "Réinitialiser les données de simulation pour ce portefeuille ?",
    activeVestingVault: "Coffre de Vesting Token-2022 Actif",
    angelTranche: "Tranche Angel",
    openMyVestingVault: "Ouvrir Mon Coffre de Vesting →",
    connectedCheck: "Connecté ✓",
    passkeyActiveDeposit: "Passkey Actif • Connectez Phantom/Solflare pour déposer",
    connectPhantomBtn: "Connecter Phantom",
    connectingBtn: "Connexion...",
    walletNotConnected: "Portefeuille Non Connecté",
    connectWalletBeforeDeposit: "Veuillez connecter un portefeuille Passkey ou Phantom avant de déposer.",
    enterValidDeposit: "Veuillez entrer un montant valide (> 0).",
    broadcastingFaucet: "Diffusion de la transaction Faucet Solana Devnet...",
    faucetClaimed: "Faucet Testnet Réclamé",
    faucetCredited: "Crédit Faucet ajouté au Master Vault !",
    connectingPhantomWallet: "Connexion au portefeuille Phantom...",
    web3Rejected: "La connexion au portefeuille Web3 a été annulée.",
    web3Disconnected: "Portefeuille Web3 déconnecté. Veuillez reconnecter Phantom.",
    awaitingSignature: "En attente de signature dans le portefeuille...",
    gaslessDepositSuccess: "Dépôt sans Gas Confirmé (0% Gas)",
    depositCredited: "Fonds crédités sur le Master Vault !",
    approveInPhantomExt: "Approuvez dans l'extension Phantom...",
    confirmingSolana: "Confirmation sur Solana Devnet...",
    web3DepositSuccess: "Dépôt Web3 Confirmé",
    depositCanceledUser: "Dépôt annulé : transaction rejetée dans le portefeuille.",
    solanaTxFailed: "Échec de la transaction Solana Devnet :",
    cannotWithdrawEmergency: "Impossible de retirer pendant l'état d'arrêt d'urgence.",
    connectWalletBeforeWithdraw: "Veuillez connecter votre portefeuille avant de retirer.",
    zeroBalance: "Solde Nul",
    zeroBalanceMsg: "Votre solde Master Vault est de $0.0000 USDT. Aucun fonds à retirer.",
    enterValidWithdraw: "Veuillez entrer un montant de retrait valide (> 0).",
    withdrawCanceledMetaMask: "Retrait annulé : signature MetaMask rejetée.",
    withdrawCanceled: "Retrait annulé : signature rejetée dans le portefeuille.",
    withdrawSuccess: "Retrait Exécuté avec Succès",
    walletRequiredAi: "Connectez votre portefeuille pour autoriser l'exécution de l'IA.",
    insufficientVaultBalance: "Solde insuffisant dans le Vault"
  },
  es: {
    tabStrategic: "Asignación Estratégica Privada",
    passkeyTitle: "Billetera Biométrica Passkey",
    passkeySubtitle: "Autenticación WebAuthn por hardware • Cero riesgo de claves",
    syncChrome: "Sincronizar billetera con Chrome",
    openingPhantom: "Abriendo Phantom...",
    openingPhantomTitle: "Abriendo la Aplicación Phantom...",
    approvePhantomMsg: "Aprueba en Phantom para volver a Chrome",
    openingSolflare: "Abriendo Solflare...",
    openingSolflareTitle: "Abriendo la Aplicación Solflare...",
    approveSolflareMsg: "Aprueba en Solflare para volver a Chrome",
    scanningBio: "Escaneando biometría...",
    passkeyConnected: "Passkey Conectada con Éxito",
    bioError: "Error Biométrico",
    connectingPhantom: "Conectando Phantom...",
    connectingMetaMask: "Conectando MetaMask...",
    connectingSolflare: "Conectando Solflare...",
    connectionRejected: "Conexión rechazada por el usuario",
    resetSimulationConfirm: "¿Restablecer datos de simulación para esta billetera?",
    activeVestingVault: "Bóveda de Vesting Token-2022 Activa",
    angelTranche: "Tramo Ángel",
    openMyVestingVault: "Abrir Mi Bóveda de Vesting →",
    connectedCheck: "Conectado ✓",
    passkeyActiveDeposit: "Passkey Activa • Conecte Phantom/Solflare para depositar",
    connectPhantomBtn: "Conectar Phantom",
    connectingBtn: "Conectando...",
    walletNotConnected: "Billetera No Conectada",
    connectWalletBeforeDeposit: "Conecte una billetera Passkey o Phantom antes de depositar.",
    enterValidDeposit: "Ingrese un monto válido de depósito (> 0).",
    broadcastingFaucet: "Transmitiendo transacción de Faucet en Solana Devnet...",
    faucetClaimed: "Faucet de Testnet Reclamado",
    faucetCredited: "¡Fondos del Faucet acreditados en el Master Vault!",
    connectingPhantomWallet: "Conectando Billetera Phantom...",
    web3Rejected: "La conexión de billetera Web3 fue cancelada o rechazada.",
    web3Disconnected: "Billetera Web3 desconectada. Vuelva a conectar Phantom.",
    awaitingSignature: "Esperando firma en la billetera...",
    gaslessDepositSuccess: "Depósito sin Gas Confirmado (0% Gas)",
    depositCredited: "¡Fondos acreditados en Master Vault!",
    approveInPhantomExt: "Apruebe en la extensión de Phantom...",
    confirmingSolana: "Confirmando en Solana Devnet...",
    web3DepositSuccess: "Depósito Web3 Confirmado",
    depositCanceledUser: "Depósito cancelado: Rechazó la transacción en su billetera.",
    solanaTxFailed: "Transacción fallida en Solana Devnet:",
    cannotWithdrawEmergency: "No se puede retirar mientras la Bóveda esté en Parada de Emergencia.",
    connectWalletBeforeWithdraw: "Conecte una billetera verificada antes de retirar fondos.",
    zeroBalance: "Saldo Cero",
    zeroBalanceMsg: "Su saldo en Master Vault es de $0.0000 USDT. No hay fondos para retirar.",
    enterValidWithdraw: "Ingrese un monto de retiro válido (> 0).",
    withdrawCanceledMetaMask: "Retiro cancelado: Rechazó la firma en MetaMask.",
    withdrawCanceled: "Retiro cancelado: Rechazó la firma en la billetera.",
    withdrawSuccess: "Retiro Ejecutado con Éxito",
    walletRequiredAi: "Conecte su billetera para autorizar la ejecución de IA.",
    insufficientVaultBalance: "Saldo insuficiente en la Bóveda"
  },
  ru: {
    tabStrategic: "Приватная Стратегическая Аллокация",
    passkeyTitle: "Биометрический Passkey Кошелек",
    passkeySubtitle: "Аппаратная аутентификация WebAuthn • Абсолютная безопасность",
    syncChrome: "Синхронизировать кошелек с Chrome",
    openingPhantom: "Открытие Phantom...",
    openingPhantomTitle: "Открытие Приложения Phantom...",
    approvePhantomMsg: "Подтвердите в Phantom для возврата в Chrome",
    openingSolflare: "Открытие Solflare...",
    openingSolflareTitle: "Открытие Приложения Solflare...",
    approveSolflareMsg: "Подтвердите в Solflare для возврата в Chrome",
    scanningBio: "Сканирование биометрии...",
    passkeyConnected: "Passkey Успешно Подключен",
    bioError: "Биометрическая Ошибка",
    connectingPhantom: "Подключение к Phantom...",
    connectingMetaMask: "Подключение к MetaMask...",
    connectingSolflare: "Подключение к Solflare...",
    connectionRejected: "Подключение отклонено пользователем",
    resetSimulationConfirm: "Сбросить данные симуляции для этого кошелька?",
    activeVestingVault: "Активный Сейф Вестинга Token-2022",
    angelTranche: "Ангельский Транш",
    openMyVestingVault: "Открыть Мой Сейф Вестинга →",
    connectedCheck: "Подключено ✓",
    passkeyActiveDeposit: "Passkey Активен • Подключите Phantom/Solflare для пополнения",
    connectPhantomBtn: "Подключить Phantom",
    connectingBtn: "Подключение...",
    walletNotConnected: "Кошелек Не Подключен",
    connectWalletBeforeDeposit: "Подключите Passkey или Phantom кошелек перед внесением средств.",
    enterValidDeposit: "Введите корректную сумму пополнения (> 0).",
    broadcastingFaucet: "Отправка транзакции Faucet Solana Devnet...",
    faucetClaimed: "Тестовый Faucet Получен",
    faucetCredited: "Баланс Faucet зачислен в Master Vault!",
    connectingPhantomWallet: "Подключение кошелька Phantom...",
    web3Rejected: "Подключение Web3 кошелька было отменено.",
    web3Disconnected: "Web3 кошелек отключен. Подключите Phantom заново.",
    awaitingSignature: "Ожидание подписи в кошельке...",
    gaslessDepositSuccess: "Пополнение без комиссии (0% Gas)",
    depositCredited: "Средства зачислены в Master Vault!",
    approveInPhantomExt: "Подтвердите в расширении Phantom...",
    confirmingSolana: "Подтверждение в сети Solana Devnet...",
    web3DepositSuccess: "Web3 Пополнение Подтверждено",
    depositCanceledUser: "Пополнение отменено: Вы отклонили транзакцию в кошельке.",
    solanaTxFailed: "Ошибка транзакции в Solana Devnet:",
    cannotWithdrawEmergency: "Вывод невозможен в режиме аварийной остановки (Emergency Stop).",
    connectWalletBeforeWithdraw: "Подключите верифицированный кошелек перед выводом средств.",
    zeroBalance: "Нулевой Баланс",
    zeroBalanceMsg: "Баланс Master Vault составляет $0.0000 USDT. Нет средств для вывода.",
    enterValidWithdraw: "Введите корректную сумму вывода (> 0).",
    withdrawCanceledMetaMask: "Вывод отменен: Вы отклонили подпись в MetaMask.",
    withdrawCanceled: "Вывод отменен: Вы отклонили подпись в кошельке.",
    withdrawSuccess: "Вывод Успешно Выполнен",
    walletRequiredAi: "Подключите кошелек для авторизации выполнения ИИ.",
    insufficientVaultBalance: "Недостаточно средств в Сейфе"
  },
  hi: {
    tabStrategic: "प्राइवेट रणनीतिक आवंटन",
    passkeyTitle: "बायोमेट्रिक पासकी वॉलेट",
    passkeySubtitle: "हार्डवेयर-आधारित WebAuthn • शून्य की-जोखिम",
    syncChrome: "Chrome ब्राउज़र में वॉलेट सिंक करें",
    openingPhantom: "Phantom खोला जा रहा है...",
    openingPhantomTitle: "Phantom ऐप खोला जा रहा है...",
    approvePhantomMsg: "Chrome पर लौटने के लिए Phantom में अनुमति दें",
    openingSolflare: "Solflare खोला जा रहा है...",
    openingSolflareTitle: "Solflare ऐप खोला जा रहा है...",
    approveSolflareMsg: "Chrome पर लौटने के लिए Solflare में अनुमति दें",
    scanningBio: "बायोमेट्रिक स्कैन किया जा रहा है...",
    passkeyConnected: "पासकी सफलतापूर्वक कनेक्ट हो गई",
    bioError: "बायोमेट्रिक त्रुटि",
    connectingPhantom: "Phantom कनेक्ट हो रहा है...",
    connectingMetaMask: "MetaMask कनेक्ट हो रहा है...",
    connectingSolflare: "Solflare कनेक्ट हो रहा है...",
    connectionRejected: "उपयोगकर्ता द्वारा कनेक्शन अस्वीकृत",
    resetSimulationConfirm: "क्या इस वॉलेट के लिए सिमुलेशन डेटा रीसेट करें?",
    activeVestingVault: "सक्रिय Token-2022 वेस्टिंग वॉल्ट",
    angelTranche: "एंजेल ट्रांच",
    openMyVestingVault: "मेरा वेस्टिंग वॉल्ट खोलें →",
    connectedCheck: "कनेक्टेड ✓",
    passkeyActiveDeposit: "पासकी सक्रिय • जमा करने के लिए Phantom/Solflare कनेक्ट करें",
    connectPhantomBtn: "Phantom कनेक्ट करें",
    connectingBtn: "कनेक्ट हो रहा है...",
    walletNotConnected: "वॉलेट कनेक्ट नहीं है",
    connectWalletBeforeDeposit: "जमा करने से पहले कृपया पासकी या Phantom वॉलेट कनेक्ट करें।",
    enterValidDeposit: "कृपया एक वैध जमा राशि दर्ज करें (> 0)।",
    broadcastingFaucet: "Solana Devnet Faucet लेनदेन प्रसारित किया जा रहा है...",
    faucetClaimed: "टेस्टनेट फॉसेट प्राप्त हुआ",
    faucetCredited: "Master Vault में फॉसेट जमा हो गया!",
    connectingPhantomWallet: "Phantom वॉलेट कनेक्ट किया जा रहा है...",
    web3Rejected: "Web3 वॉलेट कनेक्शन रद्द कर दिया गया।",
    web3Disconnected: "Web3 वॉलेट डिस्कनेक्ट हो गया। कृपया Phantom पुनः कनेक्ट करें।",
    awaitingSignature: "वॉलेट में हस्ताक्षर की प्रतीक्षा है...",
    gaslessDepositSuccess: "गैसलेस जमा की पुष्टि (0% Gas)",
    depositCredited: "Master Vault में धनराशि जमा हो गई!",
    approveInPhantomExt: "Phantom एक्सटेंशन में स्वीकृत करें...",
    confirmingSolana: "Solana Devnet पर पुष्टि की जा रही है...",
    web3DepositSuccess: "Web3 जमा की पुष्टि हुई",
    depositCanceledUser: "जमा रद्द: आपने वॉलेट में लेनदेन अस्वीकार कर दिया।",
    solanaTxFailed: "Solana Devnet लेनदेन विफल:",
    cannotWithdrawEmergency: "आपातकालीन स्थिति में निकासी संभव नहीं है।",
    connectWalletBeforeWithdraw: "निकासी से पहले कृपया अपना वॉलेट कनेक्ट करें।",
    zeroBalance: "शून्य शेष",
    zeroBalanceMsg: "आपके Master Vault का शेष $0.0000 USDT है। निकासी के लिए कोई फंड नहीं है।",
    enterValidWithdraw: "कृपया एक वैध निकासी राशि दर्ज करें (> 0)।",
    withdrawCanceledMetaMask: "निकासी रद्द: आपने MetaMask हस्ताक्षर अस्वीकार कर दिया।",
    withdrawCanceled: "निकासी रद्द: आपने वॉलेट हस्ताक्षर अस्वीकार कर दिया।",
    withdrawSuccess: "निकासी सफलतापूर्वक निष्पादित हुई",
    walletRequiredAi: "AI निष्पादन अधिकृत करने के लिए अपना वॉलेट कनेक्ट करें।",
    insufficientVaultBalance: "वॉल्ट में अपर्याप्त शेष"
  },
  he: {
    tabStrategic: "הקצאה אסטרטגית פרטית",
    passkeyTitle: "ארנק ביומטרי Passkey",
    passkeySubtitle: "אימות חומרה WebAuthn • אפס סיכון למפתחות",
    syncChrome: "סנכרן ארנק לדפדפן Chrome",
    openingPhantom: "פותח את Phantom...",
    openingPhantomTitle: "פותח את אפליקציית Phantom...",
    approvePhantomMsg: "אשר ב-Phantom כדי לחזור ל-Chrome",
    openingSolflare: "פותח את Solflare...",
    openingSolflareTitle: "פותח את אפליקציית Solflare...",
    approveSolflareMsg: "אשר ב-Solflare כדי לחזור ל-Chrome",
    scanningBio: "סורק נתונים ביומטריים...",
    passkeyConnected: "Passkey חובר בהצלחה",
    bioError: "שגיאה ביומטרית",
    connectingPhantom: "מתחבר ל-Phantom...",
    connectingMetaMask: "מתחבר ל-MetaMask...",
    connectingSolflare: "מתחבר ל-Solflare...",
    connectionRejected: "החיבור נדחה על ידי המשתמש",
    resetSimulationConfirm: "האם לאפס את נתוני ההדמיה עבור ארנק זה?",
    activeVestingVault: "כספת ווסטינג Token-2022 פעילה",
    angelTranche: "טרנץ' אנג'ל",
    openMyVestingVault: "פתח את כספת הווסטינג שלי →",
    connectedCheck: "מחובר ✓",
    passkeyActiveDeposit: "Passkey פעיל • חבר Phantom/Solflare להפקדה",
    connectPhantomBtn: "חבר את Phantom",
    connectingBtn: "מתחבר...",
    walletNotConnected: "ארנק לא מחובר",
    connectWalletBeforeDeposit: "אנא חבר ארנק Passkey או Phantom לפני ההפקדה.",
    enterValidDeposit: "אנא הזן סכום הפקדה תקין (> 0).",
    broadcastingFaucet: "משדר עסקת Faucet ב-Solana Devnet...",
    faucetClaimed: "ברז רשת הבדיקה נתבע בהצלחה",
    faucetCredited: "הסכום זוכה ל-Master Vault!",
    connectingPhantomWallet: "מתחבר לארנק Phantom...",
    web3Rejected: "חיבור ארנק Web3 בוטל או נדחה.",
    web3Disconnected: "ארנק Web3 מנותק. אנא חבר מחדש את Phantom.",
    awaitingSignature: "ממתין לחתימה בארנק...",
    gaslessDepositSuccess: "הפקדה ללא עמלות גז אושרה (0% Gas)",
    depositCredited: "הכספים זוכו ב-Master Vault!",
    approveInPhantomExt: "אשר בתוסף Phantom...",
    confirmingSolana: "מאמת ב-Solana Devnet...",
    web3DepositSuccess: "הפקדת Web3 אושרה",
    depositCanceledUser: "ההפקדה בוטלה: דחית את העסקה בארנק שלך.",
    solanaTxFailed: "עסקת Solana Devnet נכשלה:",
    cannotWithdrawEmergency: "לא ניתן למשוך כספים כאשר הכספת במצב עצירת חירום.",
    connectWalletBeforeWithdraw: "אנא חבר ארנק מאומת לפני משיכת כספים.",
    zeroBalance: "יתרה אפס",
    zeroBalanceMsg: "יתרת ה-Master Vault שלך היא $0.0000 USDT. אין כספים למשיכה.",
    enterValidWithdraw: "אנא הזן סכום משיכה תקין (> 0).",
    withdrawCanceledMetaMask: "המשיכה בוטלה: דחית את חתימת האימות ב-MetaMask.",
    withdrawCanceled: "המשיכה בוטלה: דחית את חתימת האימות בארנק.",
    withdrawSuccess: "המשיכה בוצעה בהצלחה",
    walletRequiredAi: "חבר את הארנק שלך כדי לאשר ביצוע AI.",
    insufficientVaultBalance: "יתרה לא מספקת בכספת"
  }
};

function patchNotices(filePath) {
  let html = fs.readFileSync(filePath, 'utf8');

  // Insert DASH_NOTICES_I18N helper right after VESTING_VAULT_I18N helper
  const helperDefinition = `
    const DASH_NOTICES_I18N = ${JSON.stringify(NOTICES_DICT, null, 2)};

    function getDashNotice(key) {
      const lang = window.haichainI18n ? window.haichainI18n.current() : 'en';
      const dict = DASH_NOTICES_I18N[lang] || DASH_NOTICES_I18N['en'];
      return dict[key] || DASH_NOTICES_I18N['en'][key] || '';
    }
  `;

  if (!html.includes('const DASH_NOTICES_I18N =')) {
    html = html.replace('function getVestingText', `${helperDefinition}\n    function getVestingText`);
  }

  // Replace remaining isVi expressions with getDashNotice(key)
  html = html.replace(/currentTabTitle\.textContent = isVi \? 'Ph[^']*' : 'Private Strategic Allocation';/g,
    `currentTabTitle.textContent = getDashNotice('tabStrategic');`);
  
  html = html.replace(/titleEl\.textContent = isVi \? 'Ph[^']*' : 'Private Strategic Allocation';/g,
    `titleEl.textContent = getDashNotice('tabStrategic');`);

  html = html.replace(/if \(titleEl\) titleEl\.textContent = isVi \? 'V[^']*' : 'Passkey Biometric Wallet';/g,
    `if (titleEl) titleEl.textContent = getDashNotice('passkeyTitle');`);

  html = html.replace(/if \(subtitleEl\) subtitleEl\.textContent = isVi \? 'X[^']*' : 'Hardware-Bound WebAuthn • Zero Key Risk';/g,
    `if (subtitleEl) subtitleEl.textContent = getDashNotice('passkeySubtitle');`);

  html = html.replace(/syncText\.textContent = isVi \? '[^']*' : 'Sync Wallet to Chrome Browser';/g,
    `syncText.textContent = getDashNotice('syncChrome');`);

  html = html.replace(/walletBtnText\.textContent = isVi \? "Đang mở Phantom\.\.\." : "Opening Phantom\.\.\.";/g,
    `walletBtnText.textContent = getDashNotice('openingPhantom');`);

  html = html.replace(/title: isVi \? 'Đang mở Phantom\.\.\.' : 'Opening Phantom App\.\.\.',/g,
    `title: getDashNotice('openingPhantomTitle'),`);

  html = html.replace(/message: isVi \? 'Cấp quyền trong Phantom để quay lại Chrome' : 'Approve in Phantom to return to Chrome',/g,
    `message: getDashNotice('approvePhantomMsg'),`);

  html = html.replace(/walletBtnText\.textContent = isVi \? "Đang mở Solflare\.\.\." : "Opening Solflare\.\.\.";/g,
    `walletBtnText.textContent = getDashNotice('openingSolflare');`);

  html = html.replace(/title: isVi \? 'Đang mở Solflare\.\.\.' : 'Opening Solflare App\.\.\.',/g,
    `title: getDashNotice('openingSolflareTitle'),`);

  html = html.replace(/message: isVi \? 'Cấp quyền trong Solflare để quay lại Chrome' : 'Approve in Solflare to return to Chrome',/g,
    `message: getDashNotice('approveSolflareMsg'),`);

  html = html.replace(/walletBtnText\.textContent = isVi \? "Quét sinh trắc học\.\.\." : "Scanning Biometric\.\.\.";/g,
    `walletBtnText.textContent = getDashNotice('scanningBio');`);

  html = html.replace(/title: isVi \? 'Xác Thực Passkey Thành Công' : 'Passkey Connected Successfully',/g,
    `title: getDashNotice('passkeyConnected'),`);

  html = html.replace(/'<strong>' \+ \(isVi \? 'Lỗi xác thực sinh trắc học' : 'Biometric Error'\) \+ ':<\/strong> '/g,
    `'<strong>' + getDashNotice('bioError') + ':</strong> '`);

  html = html.replace(/walletBtnText\.textContent = isVi \? "Đang kết nối Phantom\.\.\." : "Connecting Phantom\.\.\.";/g,
    `walletBtnText.textContent = getDashNotice('connectingPhantom');`);

  html = html.replace(/walletBtnText\.textContent = isVi \? "Đang kết nối MetaMask\.\.\." : "Connecting MetaMask\.\.\.";/g,
    `walletBtnText.textContent = getDashNotice('connectingMetaMask');`);

  html = html.replace(/walletBtnText\.textContent = isVi \? "Đang kết nối Solflare\.\.\." : "Connecting Solflare\.\.\.";/g,
    `walletBtnText.textContent = getDashNotice('connectingSolflare');`);

  html = html.replace(/message: isVi \? 'Người dùng đã hủy kết nối' : 'Connection rejected',/g,
    `message: getDashNotice('connectionRejected'),`);

  html = html.replace(/if \(confirm\(isVi \? 'Bạn có muốn đặt lại dữ liệu phân bổ mẫu cho ví này\?' : 'Reset simulation allocation for this wallet\?'\)\) \{/g,
    `if (confirm(getDashNotice('resetSimulationConfirm'))) {`);

  html = html.replace(/\$\{isVi \? 'Két Vesting Token-2022 Đang Hoạt Động' : 'Active Token-2022 Vesting Vault'\}/g,
    `\${getDashNotice('activeVestingVault')}`);

  html = html.replace(/\$\{isVi \? 'Khối Thiên Thần' : 'Angel Tranche'\}/g,
    `\${getDashNotice('angelTranche')}`);

  html = html.replace(/<span>\$\{isVi \? 'Truy Cập Két Vesting Của Tôi →' : 'Open My Vesting Vault →'\}<\/span>/g,
    `<span>\${getDashNotice('openMyVestingVault')}</span>`);

  html = html.replace(/btn\.textContent = isVi \? "Đã Kết Nối ✓" : "Connected ✓";/g,
    `btn.textContent = getDashNotice('connectedCheck');`);

  html = html.replace(/\? \(isVi \? "Passkey Đang Bật • Kết Nối Phantom để Nạp On-Chain" : "Passkey Active • Connect Phantom\/Solflare to Deposit"\)/g,
    `? getDashNotice('passkeyActiveDeposit')`);

  html = html.replace(/btn\.textContent = isVi \? "Kết Nối Phantom" : "Connect Phantom";/g,
    `btn.textContent = getDashNotice('connectPhantomBtn');`);

  html = html.replace(/depositConnectBtn\.textContent = isVi \? "Đang kết nối\.\.\." : "Connecting\.\.\.";/g,
    `depositConnectBtn.textContent = getDashNotice('connectingBtn');`);

  html = html.replace(/title: isVi \? 'Chưa kết nối ví' : 'Wallet Not Connected',/g,
    `title: getDashNotice('walletNotConnected'),`);

  html = html.replace(/message: isVi \? 'Vui lòng kết nối ví Passkey hoặc Phantom trước khi nạp tiền\.' : 'Please connect a Passkey or Solana wallet before depositing\.',/g,
    `message: getDashNotice('connectWalletBeforeDeposit'),`);

  html = html.replace(/alert\(isVi \? 'Vui lòng kết nối ví Passkey hoặc Phantom trước khi nạp tiền\.' : 'Please connect a wallet before depositing\.'\);/g,
    `alert(getDashNotice('connectWalletBeforeDeposit'));`);

  html = html.replace(/alert\(isVi \? "Vui lòng nhập số tiền nạp hợp lệ \(> 0\)\." : "Please enter a valid deposit amount\."\);/g,
    `alert(getDashNotice('enterValidDeposit'));`);

  html = html.replace(/dashConfirmDepositBtn\.textContent = isVi \? "Đang gửi giao dịch Solana Devnet Faucet\.\.\." : "Broadcasting Solana Devnet Faucet Tx\.\.\.";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('broadcastingFaucet');`);

  html = html.replace(/title: isVi \? 'Nhận Testnet Faucet Thành Công' : 'Testnet Faucet Claimed',/g,
    `title: getDashNotice('faucetClaimed'),`);

  html = html.replace(/alert\(isVi \? `Đã nạp \+\${added\.toFixed\(2\)} USDT Devnet vào Master Vault!` : `Faucet Credited \+\${added\.toFixed\(2\)} USDT to Master Vault!`\);/g,
    `alert(getDashNotice('faucetCredited'));`);

  html = html.replace(/dashConfirmDepositBtn\.textContent = isVi \? "Đang kết nối ví Phantom\.\.\." : "Connecting Phantom Wallet\.\.\.";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('connectingPhantomWallet');`);

  html = html.replace(/alert\(isVi \? "Bạn đã từ chối kết nối ví Web3\." : "Web3 wallet connection was canceled or rejected\."\);/g,
    `alert(getDashNotice('web3Rejected'));`);

  html = html.replace(/alert\(isVi \? "Ví Web3 bị ngắt kết nối\. Vui lòng kết nối lại ví Phantom\." : "Web3 wallet disconnected\. Please reconnect Phantom\."\);/g,
    `alert(getDashNotice('web3Disconnected'));`);

  html = html.replace(/dashConfirmDepositBtn\.textContent = isVi \? "Vui lòng duyệt giao dịch trên ví\.\.\." : "Awaiting signature in wallet\.\.\.";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('awaitingSignature');`);

  html = html.replace(/title: isVi \? 'Nạp Tiền Thành Công \(0% Gas\)' : 'Gasless Deposit Confirmed',/g,
    `title: getDashNotice('gaslessDepositSuccess'),`);

  html = html.replace(/alert\(isVi \? `Đã nạp \+\$\${added\.toFixed\(2\)} USDT vào Master Vault!` : `Credited \+\$\${added\.toFixed\(2\)} USDT to Master Vault!`\);/g,
    `alert(getDashNotice('depositCredited'));`);

  html = html.replace(/dashConfirmDepositBtn\.textContent = isVi \? "Chờ bạn bấm Duyệt trên Phantom\.\.\." : "Approve in Phantom extension\.\.\.";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('approveInPhantomExt');`);

  html = html.replace(/dashConfirmDepositBtn\.textContent = isVi \? "Đang xác thực trên Solana Devnet\.\.\." : "Confirming on Solana Devnet\.\.\.";/g,
    `dashConfirmDepositBtn.textContent = getDashNotice('confirmingSolana');`);

  html = html.replace(/title: isVi \? 'Nạp Web3 Thành Công' : 'Web3 Deposit Confirmed',/g,
    `title: getDashNotice('web3DepositSuccess'),`);

  html = html.replace(/alert\(isVi \? "Giao dịch đã hủy: Bạn đã từ chối duyệt giao dịch trên ví\." : "Deposit Canceled: You rejected the transaction in your wallet\."\);/g,
    `alert(getDashNotice('depositCanceledUser'));`);

  html = html.replace(/alert\(isVi \? `Giao dịch thất bại trên Solana Devnet: \$\{errMsg\}` : `Solana Devnet transaction failed: \$\{errMsg\}`\);/g,
    `alert(getDashNotice('solanaTxFailed') + ' ' + errMsg);`);

  html = html.replace(/alert\(isVi \? "Không thể rút tiền khi Vault đang ở trạng thái Khẩn cấp \(Emergency Stop\)\." : "Cannot withdraw while Vault is in Emergency Stop state\."\);/g,
    `alert(getDashNotice('cannotWithdrawEmergency'));`);

  html = html.replace(/message: isVi \? 'Vui lòng kết nối ví trước khi thực hiện rút tiền\.' : 'Please connect a wallet before withdrawing funds\.',/g,
    `message: getDashNotice('connectWalletBeforeWithdraw'),`);

  html = html.replace(/alert\(isVi \? 'Vui lòng kết nối ví trước khi rút tiền\.' : 'Please connect your wallet first\.'\);/g,
    `alert(getDashNotice('connectWalletBeforeWithdraw'));`);

  html = html.replace(/title: isVi \? 'Số dư bằng 0' : 'Zero Balance',/g,
    `title: getDashNotice('zeroBalance'),`);

  html = html.replace(/message: isVi \? 'Số dư Master Vault của bạn là \$0\.0000 USDT\. Không có khoản tiền nào để rút\.' : 'Your Master Vault balance is \$0\.0000 USDT\. No funds available to withdraw\.',/g,
    `message: getDashNotice('zeroBalanceMsg'),`);

  html = html.replace(/message: isVi \? 'Vui lòng kết nối ví trước khi thực hiện rút tiền\.' : 'Please connect your verified wallet before withdrawing\.',/g,
    `message: getDashNotice('connectWalletBeforeWithdraw'),`);

  html = html.replace(/alert\(isVi \? "Vui lòng nhập số tiền rút hợp lệ \(> 0\)\." : "Please enter a valid withdrawal amount\."\);/g,
    `alert(getDashNotice('enterValidWithdraw'));`);

  html = html.replace(/alert\(isVi \? "Rút tiền đã hủy: Bạn đã từ chối ký xác thực giao dịch trên ví MetaMask\." : "Withdrawal Canceled: You rejected the MetaMask authorization signature\."\);/g,
    `alert(getDashNotice('withdrawCanceledMetaMask'));`);

  html = html.replace(/alert\(isVi \? "Rút tiền đã hủy: Bạn đã từ chối ký xác thực giao dịch trên ví\." : "Withdrawal Canceled: You rejected the cryptographic authorization signature\."\);/g,
    `alert(getDashNotice('withdrawCanceled'));`);

  html = html.replace(/title: isVi \? 'Rút Tiền Thành Công' : 'Withdrawal Executed',/g,
    `title: getDashNotice('withdrawSuccess'),`);

  html = html.replace(/message: isVi \? 'Vui lòng kết nối ví Passkey hoặc Phantom để cấp quyền thực thi AI\.' : 'Connect your sovereign wallet to authorize AI execution\.',/g,
    `message: getDashNotice('walletRequiredAi'),`);

  html = html.replace(/title: isVi \? 'Số dư không đủ' : 'Insufficient Vault Balance',/g,
    `title: getDashNotice('insufficientVaultBalance'),`);

  fs.writeFileSync(filePath, html, 'utf8');
  console.log('Successfully patched notices in:', filePath);
}

patchNotices('dashboard.html');
patchNotices('app/dashboard.html');
