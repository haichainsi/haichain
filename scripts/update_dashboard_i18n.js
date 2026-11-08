const fs = require('fs');

// VESTING_VAULT_I18N dictionary for all 10 languages
const VESTING_VAULT_I18N = {
  kk: {
    vaultTitle: "Token-2022 Вестинг Сейфі және Бөліністер",
    vaultSubtitle: "On-chain $HAISI бөлініс тізілімі және криптографиялық Transfer-Hook вестингтік смарт-келісімшарттары.",
    authRequired: "Solana Әмиянын Растау Қажет",
    authDesc: "Жеке вестинг бөлінісіңізді ашу және Ed25519 ашық кілтін растау үшін Phantom, Solflare, биометриялық Passkey қосыңыз немесе Solana мекенжайыңызды енгізіңіз.",
    connectWalletBtn: "Phantom / Solana Әмиянын Қосу",
    subscribeSaftBtn: "Private SAFT Раундына Жазылу",
    authAddress: "Расталған Әмиян:",
    noAllocTitle: "Бұл Әмиян Мекенжайына Бөлініс Табылмады",
    noAllocDesc: "Бұл әмиян мекенжайы қазынашылық жүйесіндегі белсенді SAFT келісіміне немесе бастапқы токен бөлінісіне әлі байланыстырылмаған. Егер қаражат аударған болсаңыз, желінің растауын күтіңіз.",
    subscribeDiscountBtn: "Private SAFT Раундына Жазылу (30% Жеңілдік)",
    switchWalletBtn: "Басқа Әмиянға Ауысу",
    portfolioTitle: "Инвестор Портфелі және Вестинг Сейфі",
    trancheBadge: "Құпия Стратегиялық Бөлініс",
    transferHookStatus: "Token-2022 Transfer-Hook Бұғатталған",
    addToPhantomBtn: "$HAISI-ді Phantom-ға Қосу",
    resetSimTitle: "Үлгі деректерін қалпына келтіру",
    kpiTotalBalance: "Бөлінген Жалпы $HAISI",
    kpiTokenStandard: "Solana Token-2022 Кеңейтімі",
    kpiCommittedCapital: "Бөлінген Инвестициялық Капитал",
    kpiTreasuryVault: "Multi-Sig L1 Қазынашылығы",
    kpiTgeBenchmark: "Ашық TGE Негізгі Бағасы",
    kpiBenchmarkSubtitle: "Бастапқы Баға $10M FDV",
    kpiTgeValuation: "TGE-дегі Күтілетін Құн",
    kpiNotionalSurplus: "Атаулы Артықшылық",
    transferHookTitle: "Transfer-Hook Криптографиялық Инварианты",
    transferHookDesc: "Барлық ерте кезеңдегі $HAISI токендері клифф және сызықты вестинг шарттары Solana валидаторларымен расталмайынша тасымалдауды математикалық түрде бұғаттайтын ончейн Transfer-Hook кеңейтімімен жасалған.",
    step1Title: "1. TGE Бұғатты Ашу (20%)",
    step1Desc: "Жария 런치падта листинг болған кезде бірден қолжетімді.",
    step2Title: "2. Клифф Кезеңі (1 және 2 айлар)",
    step2Desc: "0% аудару мүмкіндігі. Нарықтық сатылымнан қорғау үшін толық бұғаттау.",
    step3Title: "3. Сызықты Стриминг (3-8 айлар)",
    step3Desc: "180 күн бойы күн сайын біркелкі үлестірілетін үздіксіз микро-стриминг.",
    dailyRate: "$HAISI / күн",
    copyMintPrompt: "TOKEN-2022 MINT МЕКЕНЖАЙЫ КӨШІРІЛДІ ($HAISI):",
    copyMintGuide: "Phantom-ға қосу үшін:\n1. Phantom ашыңыз -> 'Manage token list' басыңыз.\n2. Mint мекенжайын іздеу жолағына қойыңыз.\n3. $HAISI (Haichain SI) балансы мен таңбасын қосыңыз."
  },
  en: {
    vaultTitle: "Token-2022 Vesting Vault & Allocations",
    vaultSubtitle: "On-chain $HAISI (Haichain SI) allocation ledger and cryptographic Transfer-Hook vesting smart contracts.",
    authRequired: "Solana Wallet Authentication Required",
    authDesc: "Connect Phantom, Solflare, Biometric Passkey, or enter your personal Solana address to verify your Ed25519 public key and unlock your personal vesting allocation vault.",
    connectWalletBtn: "Connect Phantom / Solana Wallet",
    subscribeSaftBtn: "Subscribe to Private SAFT",
    authAddress: "Authenticated Address:",
    noAllocTitle: "No Allocation Found for this Address",
    noAllocDesc: "This wallet address is not currently bound to any active SAFT agreement or early token tranche in the treasury vault. If you have recently sent funds, please allow network block finalization.",
    subscribeDiscountBtn: "Subscribe to Private SAFT (30% Discount)",
    switchWalletBtn: "Switch Wallet",
    portfolioTitle: "Investor Portfolio & Vesting Vault",
    trancheBadge: "Confidential Strategic Tranche",
    transferHookStatus: "Token-2022 Transfer-Hook Locked",
    addToPhantomBtn: "Add $HAISI to Phantom",
    resetSimTitle: "Reset simulation",
    kpiTotalBalance: "Total $HAISI Balance",
    kpiTokenStandard: "Solana Token-2022 Extension",
    kpiCommittedCapital: "Committed Capital",
    kpiTreasuryVault: "Multi-Sig Treasury Vault",
    kpiTgeBenchmark: "Public TGE Benchmark",
    kpiBenchmarkSubtitle: "Floor Launchpad Benchmark",
    kpiTgeValuation: "TGE Notional Valuation",
    kpiNotionalSurplus: "Notional Surplus",
    transferHookTitle: "Transfer-Hook Cryptographic Invariant",
    transferHookDesc: "All early $HAISI tokens are minted with on-chain Transfer-Hook extensions that mathematically block transfers until cliff and linear vesting conditions are verified by Solana runtime validators.",
    step1Title: "1. TGE Unlock (20%)",
    step1Desc: "Available immediately at public launchpad listing.",
    step2Title: "2. Cliff Period (Months 1 & 2)",
    step2Desc: "0% transferability. Complete lock to prevent market dumping.",
    step3Title: "3. Linear Stream (Months 3 to 8)",
    step3Desc: "Daily continuous micro-streaming unlocking evenly over 180 days.",
    dailyRate: "$HAISI / day",
    copyMintPrompt: "TOKEN-2022 MINT COPIED ($HAISI):",
    copyMintGuide: "To view in Phantom:\n1. Open Phantom -> Click 'Manage token list'.\n2. Paste the Mint Address into search.\n3. Toggle ON to view your official $HAISI (Haichain SI) balance."
  },
  zh: {
    vaultTitle: "Token-2022 锁仓金库与分配份额",
    vaultSubtitle: "链上 $HAISI (Haichain SI) 认购分配账本与密码学 Transfer-Hook 锁仓智能合约。",
    authRequired: "需要验证 Solana 钱包",
    authDesc: "连接 Phantom、Solflare、生物识别 Passkey 或输入您的 Solana 地址以验证 Ed25519 公钥并解锁您的专属锁仓金库。",
    connectWalletBtn: "连接 Phantom / Solana 钱包",
    subscribeSaftBtn: "认购私募 SAFT 份额",
    authAddress: "已验证钱包地址：",
    noAllocTitle: "未找到此地址的认购分配份额",
    noAllocDesc: "此钱包地址目前未绑定金库系统中的任何有效 SAFT 协议或早期代币分配。如果您刚刚完成转账，请等待链上区块确认。",
    subscribeDiscountBtn: "认购私募 SAFT 份额 (享 30% 优惠折扣)",
    switchWalletBtn: "切换其他钱包",
    portfolioTitle: "投资者投资组合与锁仓金库",
    trancheBadge: "机密战略早期轮次",
    transferHookStatus: "Token-2022 Transfer-Hook 密码学锁定",
    addToPhantomBtn: "将 $HAISI 添加至 Phantom",
    resetSimTitle: "重置模拟数据",
    kpiTotalBalance: "总 $HAISI 分配余额",
    kpiTokenStandard: "Solana Token-2022 扩展规范",
    kpiCommittedCapital: "承诺投资本金",
    kpiTreasuryVault: "L1 多签国库金库",
    kpiTgeBenchmark: "公开 TGE 基准发售盘",
    kpiBenchmarkSubtitle: "初始启动估值 $10M FDV",
    kpiTgeValuation: "TGE 预期票面市值",
    kpiNotionalSurplus: "名义未实现溢价",
    transferHookTitle: "Transfer-Hook 密码学不变性约束",
    transferHookDesc: "所有早期 $HAISI 代币均通过链上 Transfer-Hook 扩展发行，在满足锁仓和线性释放条件并通过 Solana 验证之前，任何转账均在数学底层被严格拦截。",
    step1Title: "1. TGE 首发解锁 (20%)",
    step1Desc: "在公开 Launchpad 上线时立即可用。",
    step2Title: "2. 锁仓期 (第1与第2个月)",
    step2Desc: "0% 转让率。完全冻结以防止二级市场恶意抛售。",
    step3Title: "3. 线性流式释放 (第3至第8个月)",
    step3Desc: "在 180 天内每日平滑持续微支付式释放。",
    dailyRate: "$HAISI / 天",
    copyMintPrompt: "TOKEN-2022 MINT 地址已复制 ($HAISI)：",
    copyMintGuide: "添加至 Phantom 方法：\n1. 打开 Phantom -> 点击 'Manage token list'。\n2. 将 Mint 地址粘贴至搜索框。\n3. 开启 $HAISI (Haichain SI) 显示开关即可查看到账余额与图标。"
  },
  vi: {
    vaultTitle: "Két Vesting Token-2022 & Danh Mục Phân Bổ",
    vaultSubtitle: "Sổ cái phân bổ token $HAISI (Haichain SI) và hợp đồng Vesting on-chain được bảo vệ bằng Transfer-Hook mật mã.",
    authRequired: "Yêu Cầu Kết Nối Ví Solana",
    authDesc: "Hãy kết nối ví Phantom, Solflare, Passkey sinh trắc học hoặc nhập địa chỉ ví Solana cá nhân để xác thực và mở khóa két phân bổ vesting của bạn.",
    connectWalletBtn: "Kết Nối Ví Phantom / Solana",
    subscribeSaftBtn: "Đăng Ký Vòng Private SAFT",
    authAddress: "Ví đang xác thực:",
    noAllocTitle: "Chưa Ghi Nhận Phân Bổ Nào Cho Địa Chỉ Ví Này",
    noAllocDesc: "Địa chỉ ví này hiện chưa có hợp đồng SAFT hoặc phân bổ token sớm nào trong hệ thống kho bạc. Nếu bạn đã chuyển USDT/SOL, giao dịch sẽ được ghi nhận ngay khi khối on-chain hoàn tất xác thực.",
    subscribeDiscountBtn: "Đăng Ký Vòng Private SAFT (Chiết Khấu 30%)",
    switchWalletBtn: "Đổi Địa Chỉ Ví Khác",
    portfolioTitle: "Két Vesting & Danh Mục Đầu Tư",
    trancheBadge: "Khối Đầu Tư Thiên Thần Bảo Mật",
    transferHookStatus: "Token-2022 Transfer-Hook Đang Khóa",
    addToPhantomBtn: "Thêm $HAISI vào Phantom",
    resetSimTitle: "Đặt lại dữ liệu mẫu",
    kpiTotalBalance: "Tổng $HAISI Đã Phân Bổ",
    kpiTokenStandard: "Chuẩn Solana Token-2022",
    kpiCommittedCapital: "Vốn Đầu Tư Cam Kết",
    kpiTreasuryVault: "Kho Bạc Multi-Sig L1",
    kpiTgeBenchmark: "Mốc Niêm Yết Tham Chiếu",
    kpiBenchmarkSubtitle: "Định Giá Khởi Điểm $10M",
    kpiTgeValuation: "Giá Trị Dự Kiến Tại TGE",
    kpiNotionalSurplus: "Tỷ Suất Danh Nghĩa",
    transferHookTitle: "Transfer-Hook Mật Mã Bất Biến",
    transferHookDesc: "Mọi token $HAISI sớm đều được đúc kèm tiện ích mở rộng Transfer-Hook on-chain, ngăn chặn việc chuyển nhượng cho đến khi điều kiện cliff và vesting được xác thực bởi runtime Solana.",
    step1Title: "1. Mở Khóa TGE (20%)",
    step1Desc: "Khả dụng ngay khi niêm yết trên launchpad công khai.",
    step2Title: "2. Giai Đoạn Cliff (Tháng 1 & 2)",
    step2Desc: "0% chuyển nhượng. Đóng băng hoàn toàn để ngăn chặn áp lực xả thị trường.",
    step3Title: "3. Mở Khóa Tuyến Tính (Tháng 3 đến 8)",
    step3Desc: "Mở khóa vi dòng tiền liên tục mỗi ngày, chia đều trong 180 ngày.",
    dailyRate: "$HAISI / ngày",
    copyMintPrompt: "ĐÃ SAO CHÉP ĐỊA CHỈ MINT TOKEN-2022 ($HAISI):",
    copyMintGuide: "Cách thêm vào ví Phantom:\n1. Mở ví Phantom -> Bấm nút 'Manage token list'.\n2. Dán địa chỉ Mint trên vào ô tìm kiếm.\n3. Bật hiển thị token $HAISI (Haichain SI) để xem số dư và biểu tượng của bạn."
  },
  ko: {
    vaultTitle: "Token-2022 베스팅 볼트 및 토큰 배분",
    vaultSubtitle: "온체인 $HAISI (Haichain SI) 배분 원장 및 암호학적 Transfer-Hook 베스팅 스마트 컨트랙트.",
    authRequired: "Solana 지갑 인증 필요",
    authDesc: "Phantom, Solflare, 생체 인식 Passkey를 연결하거나 Solana 주소를 입력하여 Ed25519 공개 키를 확인하고 전용 베스팅 볼트를 잠금 해제하세요.",
    connectWalletBtn: "Phantom / Solana 지갑 연결",
    subscribeSaftBtn: "프라이빗 SAFT 청약 신청",
    authAddress: "인증된 지갑 주소:",
    noAllocTitle: "해당 지갑 주소에 대한 배분 내역이 없습니다",
    noAllocDesc: "이 지갑 주소는 현재 국고 금고의 활성 SAFT 계약이나 초기 토큰 트랜치에 연결되어 있지 않습니다. 최근 자금을 전송하셨다면 네트워크 확인을 기다려 주세요.",
    subscribeDiscountBtn: "프라이빗 SAFT 청약 (30% 할인)",
    switchWalletBtn: "다른 지갑으로 전환",
    portfolioTitle: "투자자 포트폴리오 및 베스팅 볼트",
    trancheBadge: "기밀 전략 트랜치",
    transferHookStatus: "Token-2022 Transfer-Hook 잠금 활성",
    addToPhantomBtn: "Phantom 지갑에 $HAISI 추가",
    resetSimTitle: "시뮬레이션 데이터 초기화",
    kpiTotalBalance: "총 $HAISI 배분 잔액",
    kpiTokenStandard: "Solana Token-2022 확장 표준",
    kpiCommittedCapital: "약정 투자 자본",
    kpiTreasuryVault: "Multi-Sig 국고 금고",
    kpiTgeBenchmark: "공개 TGE 벤치마크",
    kpiBenchmarkSubtitle: "초기 런치패드 $10M FDV",
    kpiTgeValuation: "TGE 예상 평가 가치",
    kpiNotionalSurplus: "명목 미실현 프리미엄",
    transferHookTitle: "Transfer-Hook 암호학적 불변성",
    transferHookDesc: "모든 초기 $HAISI 토큰은 Solana 런타임 검증자에 의해 클리프 및 선형 베스팅 조건이 충족될 때까지 전송을 수학적으로 차단하는 온체인 Transfer-Hook 확장으로 발행됩니다.",
    step1Title: "1. TGE 잠금 해제 (20%)",
    step1Desc: "공개 런치패드 상장 즉시 수령 가능.",
    step2Title: "2. 클리프 기간 (1~2개월차)",
    step2Desc: "전송 불가능 (0%). 시장 덤핑을 방지하기 위한 완전 동결.",
    step3Title: "3. 선형 스트리밍 (3~8개월차)",
    step3Desc: "180일 동안 매일 균등하게 잠금 해제되는 연속 마이크로 스트리밍.",
    dailyRate: "$HAISI / 일",
    copyMintPrompt: "TOKEN-2022 MINT 주소가 복사되었습니다 ($HAISI):",
    copyMintGuide: "Phantom 지갑에 추가하는 방법:\n1. Phantom 열기 -> 'Manage token list' 클릭.\n2. 검색창에 Mint 주소 붙여넣기.\n3. $HAISI (Haichain SI) 토큰 활성화."
  },
  fr: {
    vaultTitle: "Coffre de Vesting Token-2022 & Allocations",
    vaultSubtitle: "Registre d'allocation $HAISI (Haichain SI) on-chain et contrats intelligents de vesting sécurisés par Transfer-Hook.",
    authRequired: "Authentification de Portefeuille Solana Requise",
    authDesc: "Connectez Phantom, Solflare, Passkey biométrique ou entrez votre adresse Solana pour vérifier votre clé publique Ed25519 et déverrouiller votre coffre de vesting.",
    connectWalletBtn: "Connecter Portefeuille Phantom / Solana",
    subscribeSaftBtn: "Souscrire au SAFT Privé",
    authAddress: "Adresse Authentifiée :",
    noAllocTitle: "Aucune Allocation Trouvée pour cette Adresse",
    noAllocDesc: "Cette adresse de portefeuille n'est actuellement liée à aucun accord SAFT actif dans la trésorerie. Si vous avez récemment envoyé des fonds, veuillez patienter pendant la finalisation du bloc.",
    subscribeDiscountBtn: "Souscrire au SAFT Privé (-30% de Réduction)",
    switchWalletBtn: "Changer de Portefeuille",
    portfolioTitle: "Portefeuille Investisseur & Coffre de Vesting",
    trancheBadge: "Tranche Stratégique Confidentielle",
    transferHookStatus: "Verrouillage Token-2022 Transfer-Hook Actif",
    addToPhantomBtn: "Ajouter $HAISI à Phantom",
    resetSimTitle: "Réinitialiser la simulation",
    kpiTotalBalance: "Solde Total $HAISI Alloué",
    kpiTokenStandard: "Extension Solana Token-2022",
    kpiCommittedCapital: "Capital Investi Engagé",
    kpiTreasuryVault: "Coffre Trésorerie Multi-Sig L1",
    kpiTgeBenchmark: "Référence TGE Publique",
    kpiBenchmarkSubtitle: "Valorisation de Départ $10M",
    kpiTgeValuation: "Valorisation Notionnelle TGE",
    kpiNotionalSurplus: "Surplus Notionnel",
    transferHookTitle: "Invariant Cryptographique Transfer-Hook",
    transferHookDesc: "Tous les tokens $HAISI initiaux intègrent l'extension on-chain Transfer-Hook, bloquant mathématiquement tout transfert jusqu'à ce que les conditions de vesting soient vérifiées par les validateurs Solana.",
    step1Title: "1. Déblocage TGE (20%)",
    step1Desc: "Disponible immédiatement dès la cotation publique sur le launchpad.",
    step2Title: "2. Période de Cliff (Mois 1 & 2)",
    step2Desc: "0% transférable. Gel complet pour protéger le marché contre le dumping.",
    step3Title: "3. Flux Linéaire (Mois 3 à 8)",
    step3Desc: "Micro-flux continu quotidien débloqué uniformément sur 180 jours.",
    dailyRate: "$HAISI / jour",
    copyMintPrompt: "ADRESSE MINT TOKEN-2022 COPIÉE ($HAISI) :",
    copyMintGuide: "Pour afficher dans Phantom :\n1. Ouvrez Phantom -> Cliquez sur 'Manage token list'.\n2. Collez l'adresse Mint dans la recherche.\n3. Activez $HAISI (Haichain SI)."
  },
  es: {
    vaultTitle: "Bóveda de Vesting Token-2022 y Asignaciones",
    vaultSubtitle: "Libro mayor de asignaciones $HAISI (Haichain SI) en cadena y contratos inteligentes de vesting con Transfer-Hook criptográfico.",
    authRequired: "Autenticación de Billetera Solana Requerida",
    authDesc: "Conecte Phantom, Solflare, Passkey biométrica o ingrese su dirección de Solana para verificar su clave pública Ed25519 y desbloquear su bóveda de vesting.",
    connectWalletBtn: "Conectar Billetera Phantom / Solana",
    subscribeSaftBtn: "Suscribirse al SAFT Privado",
    authAddress: "Dirección Autenticada:",
    noAllocTitle: "No se Encontró Ninguna Asignación para esta Dirección",
    noAllocDesc: "Esta dirección de billetera no está vinculada actualmente a ningún acuerdo SAFT activo en la tesorería. Si ha enviado fondos recientemente, espere la confirmación del bloque.",
    subscribeDiscountBtn: "Suscribirse al SAFT Privado (30% de Descuento)",
    switchWalletBtn: "Cambiar de Billetera",
    portfolioTitle: "Portafolio del Inversor y Bóveda de Vesting",
    trancheBadge: "Tramo Estratégico Confidencial",
    transferHookStatus: "Bloqueo Token-2022 Transfer-Hook Activo",
    addToPhantomBtn: "Agregar $HAISI a Phantom",
    resetSimTitle: "Restablecer simulación",
    kpiTotalBalance: "Saldo Total de $HAISI Asignado",
    kpiTokenStandard: "Extensión Solana Token-2022",
    kpiCommittedCapital: "Capital Invertido Comprometido",
    kpiTreasuryVault: "Bóveda de Tesorería Multi-Sig L1",
    kpiTgeBenchmark: "Referencia TGE Pública",
    kpiBenchmarkSubtitle: "Valoración Inicial de $10M",
    kpiTgeValuation: "Valoración Nocional en TGE",
    kpiNotionalSurplus: "Excedente Nocional",
    transferHookTitle: "Invariante Criptográfico Transfer-Hook",
    transferHookDesc: "Todos los tokens $HAISI tempranos se emiten con la extensión en cadena Transfer-Hook, bloqueando matemáticamente las transferencias hasta que los validadores de Solana verifiquen las condiciones de vesting.",
    step1Title: "1. Desbloqueo TGE (20%)",
    step1Desc: "Disponible de inmediato en la cotización pública del launchpad.",
    step2Title: "2. Periodo de Cliff (Meses 1 y 2)",
    step2Desc: "0% transferible. Bloqueo total para prevenir ventas masivas en el mercado.",
    step3Title: "3. Transmisión Lineal (Meses 3 a 8)",
    step3Desc: "Micro-transmisión continua diaria desbloqueada uniformemente durante 180 días.",
    dailyRate: "$HAISI / día",
    copyMintPrompt: "DIRECCIÓN MINT TOKEN-2022 COPIADA ($HAISI):",
    copyMintGuide: "Para ver en Phantom:\n1. Abra Phantom -> Haga clic en 'Manage token list'.\n2. Pegue la dirección Mint en la búsqueda.\n3. Active $HAISI (Haichain SI)."
  },
  ru: {
    vaultTitle: "Сейф Вестинга Token-2022 и Аллокации",
    vaultSubtitle: "Ончейн реестр аллокаций $HAISI (Haichain SI) и криптографические смарт-контракты вестинга Transfer-Hook.",
    authRequired: "Требуется Аутентификация Solana Кошелька",
    authDesc: "Подключите Phantom, Solflare, биометрический Passkey или введите адрес Solana для верификации публичного ключа Ed25519 и доступа к сейфу вестинга.",
    connectWalletBtn: "Подключить Phantom / Solana Кошелек",
    subscribeSaftBtn: "Подписаться на Приватный SAFT",
    authAddress: "Аутентифицированный адрес:",
    noAllocTitle: "Аллокаций для этого адреса не найдено",
    noAllocDesc: "Этот адрес кошелька не привязан к действующему соглашению SAFT или траншу в казначействе. Если вы недавно перевели средства, дождитесь финализации блока в сети.",
    subscribeDiscountBtn: "Подписаться на Приватный SAFT (Скидка 30%)",
    switchWalletBtn: "Сменить Кошелек",
    portfolioTitle: "Портфель Инвестора и Сейф Вестинга",
    trancheBadge: "Конфиденциальный Стратегический Транш",
    transferHookStatus: "Блокировка Token-2022 Transfer-Hook Активна",
    addToPhantomBtn: "Добавить $HAISI в Phantom",
    resetSimTitle: "Сбросить демо-данные",
    kpiTotalBalance: "Всего Аллоцировано $HAISI",
    kpiTokenStandard: "Стандарт Solana Token-2022",
    kpiCommittedCapital: "Инвестированный Капитал",
    kpiTreasuryVault: "Мультисиг Казначейство L1",
    kpiTgeBenchmark: "Ориентир Публичного TGE",
    kpiBenchmarkSubtitle: "Стартовая оценка $10M FDV",
    kpiTgeValuation: "Ожидаемая Стоимость при TGE",
    kpiNotionalSurplus: "Номинальная Премия",
    transferHookTitle: "Криптографический Инвариант Transfer-Hook",
    transferHookDesc: "Все токены $HAISI раннего раунда выпускаются с ончейн расширением Transfer-Hook, математически блокирующим переводы до подтверждения условий клиффа и вестинга валидаторами Solana.",
    step1Title: "1. Разблокировка TGE (20%)",
    step1Desc: "Доступно немедленно при публичном листинге на launchpad.",
    step2Title: "2. Период Клиффа (1 и 2 месяцы)",
    step2Desc: "0% переводимости. Полная заморозка для защиты рынка от демпинга.",
    step3Title: "3. Линейный Стриминг (3-8 месяцы)",
    step3Desc: "Ежедневный непрерывный микро-стриминг, равномерно разблокируемый в течение 180 дней.",
    dailyRate: "$HAISI / день",
    copyMintPrompt: "АДРЕС MINT TOKEN-2022 СКОПИРОВАН ($HAISI):",
    copyMintGuide: "Для добавления в Phantom:\n1. Откройте Phantom -> Нажмите 'Manage token list'.\n2. Вставьте адрес Mint в поиск.\n3. Включите токен $HAISI (Haichain SI)."
  },
  hi: {
    vaultTitle: "Token-2022 वेस्टिंग वॉल्ट और आवंटन",
    vaultSubtitle: "ऑन-चेन $HAISI आवंटन लेजर और क्रिप्टोग्राफ़िक Transfer-Hook वेस्टिंग स्मार्ट अनुबंध।",
    authRequired: "Solana वॉलेट प्रमाणीकरण आवश्यक है",
    authDesc: "अपनी एड25519 सार्वजनिक कुंजी सत्यापित करने और अपने वेस्टिंग वॉल्ट को अनलॉक करने के लिए Phantom, Solflare, पासकी कनेक्ट करें या Solana पता दर्ज करें।",
    connectWalletBtn: "Phantom / Solana वॉलेट कनेक्ट करें",
    subscribeSaftBtn: "प्राइवेट SAFT के लिए सदस्यता लें",
    authAddress: "प्रमाणित पता:",
    noAllocTitle: "इस पते के लिए कोई आवंटन नहीं मिला",
    noAllocDesc: "यह वॉलेट पता वर्तमान में ट्रेजरी वॉल्ट में किसी भी सक्रिय SAFT समझौते से जुड़ा नहीं है। यदि आपने हाल ही में धन भेजा है, तो कृपया नेटवर्क ब्लॉक पुष्टिकरण की प्रतीक्षा करें।",
    subscribeDiscountBtn: "प्राइवेट SAFT के लिए सदस्यता लें (30% छूट)",
    switchWalletBtn: "वॉलेट बदलें",
    portfolioTitle: "निवेशक पोर्टफोलियो और वेस्टिंग वॉल्ट",
    trancheBadge: "गोपनीय रणनीतिक ट्रांच",
    transferHookStatus: "Token-2022 Transfer-Hook लॉक सक्रिय",
    addToPhantomBtn: "Phantom में $HAISI जोड़ें",
    resetSimTitle: "सिमुलेशन रीसेट करें",
    kpiTotalBalance: "कुल $HAISI शेष",
    kpiTokenStandard: "Solana Token-2022 एक्सटेंशन",
    kpiCommittedCapital: "प्रतिबद्ध पूंजी",
    kpiTreasuryVault: "मल्टी-सिग ट्रेजरी वॉल्ट",
    kpiTgeBenchmark: "सार्वजनिक TGE बेंचमार्क",
    kpiBenchmarkSubtitle: "प्रारंभिक मूल्यांकन $10M",
    kpiTgeValuation: "TGE अनुमानित मूल्यांकन",
    kpiNotionalSurplus: "अवास्तविक लाभ",
    transferHookTitle: "Transfer-Hook क्रिप्टोग्राफ़िक इनवेरिएंट",
    transferHookDesc: "सभी शुरुआती $HAISI टोकन ऑन-चेन Transfer-Hook एक्सटेंशन के साथ बनाए गए हैं, जो तब तक ट्रांसफर को गणितीय रूप से ब्लॉक करते हैं जब तक कि वेस्टिंग शर्तों को सत्यापित नहीं किया जाता।",
    step1Title: "1. TGE अनलॉक (20%)",
    step1Desc: "सार्वजनिक लॉन्चपैड लिस्टिंग पर तुरंत उपलब्ध।",
    step2Title: "2. क्लिफ अवधि (महीने 1 और 2)",
    step2Desc: "0% स्थानांतरणीयता। बाजार में डंपिंग रोकने के लिए पूर्ण लॉक।",
    step3Title: "3. लीनियर स्ट्रीम (महीने 3 से 8)",
    step3Desc: "180 दिनों में समान रूप से दैनिक निरंतर माइक्रो-स्ट्रीमिंग अनलॉक।",
    dailyRate: "$HAISI / दिन",
    copyMintPrompt: "TOKEN-2022 MINT पता कॉपी किया गया ($HAISI):",
    copyMintGuide: "Phantom में देखने के लिए:\n1. Phantom खोलें -> 'Manage token list' पर क्लिक करें।\n2. खोज में Mint पता चिपकाएँ।\n3. $HAISI (Haichain SI) टॉगल चालू करें।"
  },
  he: {
    vaultTitle: "כספת ווסטינג Token-2022 והקצאות",
    vaultSubtitle: "ספר הקצאות $HAISI ברשת וחוזי ווסטינג חכמים המוגנים באמצעות Transfer-Hook קריפטוגרפי.",
    authRequired: "נדרש אימות ארנק Solana",
    authDesc: "חבר את Phantom, Solflare, Passkey ביומטרי או הזן את כתובת ה-Solana שלך כדי לאמת את המפתח הציבורי ולפתוח את כספת הווסטינג שלך.",
    connectWalletBtn: "חבר ארנק Phantom / Solana",
    subscribeSaftBtn: "הרשמה ל-SAFT פרטי",
    authAddress: "כתובת מאומתת:",
    noAllocTitle: "לא נמצאה הקצאה עבור כתובת זו",
    noAllocDesc: "כתובת ארנק זו אינה קשורה כעת להסכם SAFT פעיל בקופת האוצר. אם העברת כספים לאחרונה, המתן לאישור הבלוק ברשת.",
    subscribeDiscountBtn: "הרשמה ל-SAFT פרטי (30% הנחה)",
    switchWalletBtn: "החלף ארנק",
    portfolioTitle: "תיק משקיע וכספת ווסטינג",
    trancheBadge: "הקצאה אסטרטגית חסויה",
    transferHookStatus: "נעילת Token-2022 Transfer-Hook פעילה",
    addToPhantomBtn: "הוסף $HAISI ל-Phantom",
    resetSimTitle: "אפס הדמיה",
    kpiTotalBalance: "סך יתרת $HAISI שהוקצתה",
    kpiTokenStandard: "תקן Solana Token-2022",
    kpiCommittedCapital: "הון מושקע",
    kpiTreasuryVault: "קופת אוצר מרובת חתימות",
    kpiTgeBenchmark: "מדד TGE ציבורי",
    kpiBenchmarkSubtitle: "שווי פתיחה של 10 מיליון דולר",
    kpiTgeValuation: "שווי משוער בהשקה (TGE)",
    kpiNotionalSurplus: "פרמיה נומינלית",
    transferHookTitle: "Transfer-Hook קריפטוגרפי קבוע",
    transferHookDesc: "כל אסימוני $HAISI המוקדמים מונפקים עם הרחבת Transfer-Hook ברשת, החוסמת העברות באופן מתמטי עד לאימות תנאי הווסטינג על ידי מאמתי Solana.",
    step1Title: "1. שחרור ב-TGE (20%)",
    step1Desc: "זמין מיד עם הרישום ב-Launchpad הציבורי.",
    step2Title: "2. תקופת נעילה (חודשים 1 ו-2)",
    step2Desc: "0% העברות. נעילה מוחלטת להגנה מפני לחץ מכירות.",
    step3Title: "3. שחרור ליניארי (חודשים 3 עד 8)",
    step3Desc: "הזרמה רציפה יומית המשתחררת באופן שווה על פני 180 יום.",
    dailyRate: "$HAISI / יום",
    copyMintPrompt: "כתובת MINT של TOKEN-2022 הועתקה ($HAISI):",
    copyMintGuide: "לצפייה ב-Phantom:\n1. פתח את Phantom -> לחץ על 'Manage token list'.\n2. הדבק את כתובת ה-Mint בחיפוש.\n3. הפעל את $HAISI (Haichain SI)."
  }
};

function patchDashboard(filePath) {
  let html = fs.readFileSync(filePath, 'utf8');

  // 1. Update #ai-hub-btn in header
  html = html.replace(/<button id="ai-hub-btn" type="button" class="([^"]*)" title="([^"]*)">/g,
    `<button id="ai-hub-btn" type="button" class="$1" title="Connect AI" data-i18n-title="nav.aiConnectTitle">`);
  html = html.replace(/<span class="hidden md:inline font-mono text-xs font-semibold">Connect AI<\/span>/g,
    `<span class="hidden md:inline font-mono text-xs font-semibold" data-i18n="nav.aiConnect">Connect AI</span>`);

  // 2. Update Overview Banner button
  html = html.replace(/<span>K[^<]*t N[^<]*i AI Ngay<\/span>/g,
    `<span data-i18n="overview.connectAiNow">Connect AI Now</span>`);

  // 3. Update #tab-playground:
  // a) Prompt input default value and placeholder
  html = html.replace(/<input type="text" id="playground-prompt" value="Explain how HAICHAIN protects AI agents from prompt injection wallet drain" class="([^"]*)">/g,
    `<input type="text" id="playground-prompt" value="Explain how HAICHAIN protects AI agents from prompt injection wallet drain" data-i18n-value="playground.defaultPrompt" data-i18n-placeholder="playground.promptPlaceholder" class="$1">`);

  // b) Quick Demos label
  html = html.replace(/<span class="text-neutral-400 dark:text-neutral-500 text-\[10px\] uppercase tracking-wider font-sans font-semibold">Quick Demos:<\/span>/g,
    `<span class="text-neutral-400 dark:text-neutral-500 text-[10px] uppercase tracking-wider font-sans font-semibold" data-i18n="playground.quickDemos">Quick Demos:</span>`);

  // c) 4 preset prompt buttons
  html = html.replace(/<button type="button" class="preset-prompt-btn ([^"]*)" data-prompt="Explain how HAICHAIN protects AI agents from prompt injection wallet drain" data-model="Claude 3\.5 Sonnet">\s*([^<]*)\s*<\/button>/g,
    `<button type="button" class="preset-prompt-btn $1" data-prompt="Explain how HAICHAIN protects AI agents from prompt injection wallet drain" data-model="Claude 3.5 Sonnet"><span data-i18n="playground.demoAntiDrain">🛡️ Anti-Drain Defense</span></button>`);

  html = html.replace(/<button type="button" class="preset-prompt-btn ([^"]*)" data-prompt="Calculate sub-second micro-escrow netting for autonomous agent swarm on Solana L1" data-model="DeepSeek R1">\s*([^<]*)\s*<\/button>/g,
    `<button type="button" class="preset-prompt-btn $1" data-prompt="Calculate sub-second micro-escrow netting for autonomous agent swarm on Solana L1" data-model="DeepSeek R1"><span data-i18n="playground.demoMicroEscrow">⚡ Micro-Escrow Math</span></button>`);

  html = html.replace(/<button type="button" class="preset-prompt-btn ([^"]*)" data-prompt="Compute joint torques and collision envelope for Optimus kinematic actuator tick" data-model="Optimus Kinematics">\s*([^<]*)\s*<\/button>/g,
    `<button type="button" class="preset-prompt-btn $1" data-prompt="Compute joint torques and collision envelope for Optimus kinematic actuator tick" data-model="Optimus Kinematics"><span data-i18n="playground.demoOptimus">🤖 Optimus Kinematics</span></button>`);

  html = html.replace(/<button type="button" class="preset-prompt-btn ([^"]*)" data-prompt="Generate Solana Anchor instruction for non-custodial capability nullifier" data-model="Claude 3\.5 Sonnet">\s*([^<]*)\s*<\/button>/g,
    `<button type="button" class="preset-prompt-btn $1" data-prompt="Generate Solana Anchor instruction for non-custodial capability nullifier" data-model="Claude 3.5 Sonnet"><span data-i18n="playground.demoAnchor">📜 Smart Contract Anchor</span></button>`);

  // d) Terminal ready line
  html = html.replace(/<span>\[Ready\] Choose an AI engine or task template and click "Execute & Settle On-Chain" to broadcast live micro-escrow\.<\/span>/g,
    `<span id="playground-terminal-ready" data-i18n="playground.terminalReady">[Ready] Choose an AI engine or task template and click "Execute & Settle On-Chain" to broadcast live micro-escrow.</span>`);

  // 4. Update #ai-hub-modal contents with data-i18n
  // Modal Header
  html = html.replace(/<h3 class="font-bold text-sm sm:text-base text-black dark:text-white tracking-tight truncate">[^<]*<\/h3>\s*<span class="px-2 py-0\.5 text-\[9px\] font-mono rounded-full bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-300 border border-neutral-300 dark:border-neutral-800 shrink-0 font-semibold uppercase tracking-wider">3 L[^<]*<\/span>/g,
    `<h3 class="font-bold text-sm sm:text-base text-black dark:text-white tracking-tight truncate" data-i18n="aiHub.modalTitle">HAICHAIN AI Hub</h3>\n              <span class="px-2 py-0.5 text-[9px] font-mono rounded-full bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-300 border border-neutral-300 dark:border-neutral-800 shrink-0 font-semibold uppercase tracking-wider" data-i18n="aiHub.modalBadge">3 Options</span>`);
  
  html = html.replace(/<p class="text-\[10\.5px\] sm:text-\[11\.5px\] text-neutral-500 truncate">Ch[^<]*<\/p>/g,
    `<p class="text-[10.5px] sm:text-[11.5px] text-neutral-500 truncate" data-i18n="aiHub.modalSubtitle">Choose the best connection mode for your experience</p>`);

  // 3 Tabs
  html = html.replace(/<span class="truncate">1\. Desktop App<\/span>/g, `<span class="truncate" data-i18n="aiHub.tabDesktop">1. Desktop App</span>`);
  html = html.replace(/<span class="truncate">2\. Claude Online<\/span>/g, `<span class="truncate" data-i18n="aiHub.tabOnline">2. Claude Online</span>`);
  html = html.replace(/<span class="truncate">3\. Web Direct<\/span>/g, `<span class="truncate" data-i18n="aiHub.tabWeb">3. Web Direct</span>`);

  // Tab 1 Desktop
  html = html.replace(/<span>C[^<]*t 1-Click T[^<]*ng \(Khuy[^<]*ng\)<\/span>/g, `<span data-i18n="aiHub.desktopTitle">1-Click Auto Install (Recommended)</span>`);
  html = html.replace(/<span class="text-\[9\.5px\] px-2 py-0\.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-black dark:text-white font-mono uppercase tracking-wider font-semibold">T[^<]*ng 100%<\/span>/g,
    `<span class="text-[9.5px] px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-black dark:text-white font-mono uppercase tracking-wider font-semibold" data-i18n="aiHub.desktopBadge">100% Automated</span>`);
  
  html = html.replace(/<p class="text-\[11px\] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">\s*D[^<]*Claude Desktop[^<]*<\/p>/g,
    `<p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.desktopDesc">For computers with Claude Desktop or Cursor IDE installed. Automatically configures MCP server and binds to on-chain spending vault.</p>`);

  html = html.replace(/<span>Ch[^<]*y trong Terminal \/ PowerShell \/ Command Prompt:<\/span>/g,
    `<span data-i18n="aiHub.desktopCmdLabel">Run in Terminal / PowerShell / Command Prompt:</span>`);

  html = html.replace(/<span id="copy-desktop-install-text">[^<]*<\/span>/g,
    `<span id="copy-desktop-install-text" data-i18n="aiHub.desktopCopyBtn">Copy 1-Click Install Command</span>`);

  html = html.replace(/<span>3 b[^<]*c k[^<]*t:<\/span>/g,
    `<span data-i18n="aiHub.desktopStepsTitle">3 Activation Steps:</span>`);

  html = html.replace(/<span>Sao ch[^<]*p l[^<]*nh tr[^<]*n v[^<]*d[^<]*n v[^<]*o <strong>Terminal \/ PowerShell \/ Command Prompt<\/strong> r[^<]*i nh[^<]*n Enter\.<\/span>/g,
    `<span data-i18n="aiHub.desktopStep1">Copy the command above, paste into Terminal / PowerShell / Command Prompt, and press Enter.</span>`);

  html = html.replace(/<span>Kh[^<]*i [^<]*ng l[^<]*i [^<]*ng d[^<]*ng <strong>Claude Desktop<\/strong>\.<\/span>/g,
    `<span data-i18n="aiHub.desktopStep2">Restart the Claude Desktop application.</span>`);

  html = html.replace(/<span>Bi[^<]*u t[^<]*ng [^<]* Tools s[^<]* xu[^<]*t hi[^<]*n [^<]* khung chat! B[^<]*n ch[^<]* c[^<]*n g[^<]*: <em>"Ki[^<]*m tra s[^<]* d[^<]* k[^<]*t chi ti[^<]*u HAICHAIN"<\/em>\.<\/span>/g,
    `<span data-i18n="aiHub.desktopStep3">The 🔌 Tools icon will appear in the chat bar! Simply type: "Check HAICHAIN spending vault balance".</span>`);

  html = html.replace(/<span>C[^<]*u h[^<]*nh th[^<]* c[^<]*ng qua file JSON\?<\/span>/g,
    `<span data-i18n="aiHub.desktopManualText">Configure manually via JSON file?</span>`);

  html = html.replace(/<span>T[^<]*i file \.json<\/span>/g,
    `<span data-i18n="aiHub.desktopDownloadJson">Download .json file</span>`);

  // Tab 2 Online
  html = html.replace(/<span>Remote MCP Server \(SSE qua HTTPS\)<\/span>/g,
    `<span data-i18n="aiHub.onlineTitle">Remote MCP Server (SSE over HTTPS)</span>`);

  html = html.replace(/<span class="text-\[9\.5px\] px-2 py-0\.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-black dark:text-white font-mono uppercase tracking-wider font-semibold">[^<]*m M[^<]*y<\/span>/g,
    `<span class="text-[9.5px] px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-black dark:text-white font-mono uppercase tracking-wider font-semibold" data-i18n="aiHub.onlineBadge">Cloud</span>`);

  html = html.replace(/<p class="text-\[11px\] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">\s*D[^<]*claude\.ai[^<]*<\/p>/g,
    `<p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.onlineDesc">For users chatting on claude.ai in browser (Chrome, Safari, Brave, Edge). Connects directly via cloud protocol.</p>`);

  html = html.replace(/<span>[^<]*ng d[^<]*n Remote MCP Connector URL:<\/span>/g,
    `<span data-i18n="aiHub.onlineUrlLabel">Remote MCP Connector URL:</span>`);

  html = html.replace(/<span id="copy-online-mcp-text">[^<]*<\/span>/g,
    `<span id="copy-online-mcp-text" data-i18n="aiHub.onlineCopyBtn">Copy Remote MCP URL</span>`);

  html = html.replace(/<span>C[^<]*ch thi[^<]*t l[^<]*p tr[^<]*n claude\.ai:<\/span>/g,
    `<span data-i18n="aiHub.onlineStepsTitle">How to set up on claude.ai:</span>`);

  html = html.replace(/<span>Truy c[^<]*p <strong>claude\.ai<\/strong> v[^<]* [^<]*ng nh[^<]*p v[^<]*o t[^<]*i kho[^<]*n c[^<]*a b[^<]*n\.<\/span>/g,
    `<span data-i18n="aiHub.onlineStep1">Go to claude.ai and log into your account.</span>`);

  html = html.replace(/<span>B[^<]*m v[^<]*o Avatar \(g[^<]*c d[^<]*i b[^<]*n tr[^<]*i\) [^<]* Ch[^<]*n <strong>Settings<\/strong> [^<]* <strong>Developer \/ Connectors<\/strong>\.<\/span>/g,
    `<span data-i18n="aiHub.onlineStep2">Click your Avatar (bottom-left) -> Settings -> Developer / Connectors.</span>`);

  html = html.replace(/<span>D[^<]*n [^<]*ng link <code class="font-bold text-black dark:text-white">https:\/\/mcp\.haichain\.si\/sse<\/code> v[^<]*o [^<]* Server URL r[^<]*i b[^<]*m <strong>Connect<\/strong>\.<\/span>/g,
    `<span data-i18n="aiHub.onlineStep3">Paste https://mcp.haichain.si/sse into Server URL and click Connect.</span>`);

  // Tab 3 Web Direct
  html = html.replace(/<span>Tr[^<]*i nghi[^<]*m Tr[^<]*c ti[^<]*p tr[^<]*n Web<\/span>/g,
    `<span data-i18n="aiHub.webTitle">Instant Web Experience</span>`);

  html = html.replace(/<p class="text-\[11px\] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">\s*D[^<]*Web3 mu[^<]*n g[^<]*i AI[^<]*<\/p>/g,
    `<p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed" data-i18n="aiHub.webDesc">For Web3 users who want to run AI inference directly in browser without installing Claude or using command lines.</p>`);

  html = html.replace(/<span class="block text-\[11px\] font-bold text-black dark:text-white">[^<]*a M[^<]* H[^<]*nh AI<\/span>/g,
    `<span class="block text-[11px] font-bold text-black dark:text-white" data-i18n="aiHub.webFeature1Title">Multi-AI Model</span>`);

  html = html.replace(/<span class="block text-\[11px\] font-bold text-black dark:text-white">K[^<]*t Chi Ti[^<]*u B[^<]*o V[^<]*<\/span>/g,
    `<span class="block text-[11px] font-bold text-black dark:text-white" data-i18n="aiHub.webFeature2Title">Protected Spending Vault</span>`);

  html = html.replace(/<span class="text-\[10px\] text-neutral-500">Kh[^<]*ng ch[^<]* ng[^<]*n s[^<]*ch, an to[^<]*n v[^<]*n 100%<\/span>/g,
    `<span class="text-[10px] text-neutral-500" data-i18n="aiHub.webFeature2Desc">Hard budget limits, 100% capital safety</span>`);

  html = html.replace(/<span class="block text-\[11px\] font-bold text-black dark:text-white">N[^<]*t Kh[^<]*n C[^<]*p Panic<\/span>/g,
    `<span class="block text-[11px] font-bold text-black dark:text-white" data-i18n="aiHub.webFeature3Title">Panic Circuit Breaker</span>`);

  html = html.replace(/<span class="text-\[10px\] text-neutral-500">Thu h[^<]*i to[^<]*n b[^<]* ti[^<]*n v[^<]* v[^<]* trong 380ms<\/span>/g,
    `<span class="text-[10px] text-neutral-500" data-i18n="aiHub.webFeature3Desc">Reclaim 100% funds to wallet in 380ms</span>`);

  html = html.replace(/<span>M[^<]* AI Playground Ngay B[^<]*y Gi[^<]* &rarr;<\/span>/g,
    `<span data-i18n="aiHub.webLaunchBtn">Open AI Playground Now →</span>`);

  html = html.replace(/<p class="text-center text-\[10\.5px\] text-neutral-500 font-sans">\s*Ch[^<]*c[^<]*n k[^<]*t n[^<]*i v[^<]* Phantom[^<]*<\/p>/g,
    `<p class="text-center text-[10.5px] text-neutral-500 font-sans" data-i18n="aiHub.webFooter">Just connect Phantom / Solflare wallet or enter your own API key (BYOK).</p>`);

  // 5. Inject VESTING_VAULT_I18N and getVestingText()
  const serializedVestingI18n = `\n    // 10-Language Official Vesting Vault Internationalization Matrix\n    const VESTING_VAULT_I18N = ${JSON.stringify(VESTING_VAULT_I18N, null, 2)};\n\n    function getVestingText(key, lang) {\n      const l = lang || (window.haichainI18n ? window.haichainI18n.current() : 'en');\n      const dict = VESTING_VAULT_I18N[l] || VESTING_VAULT_I18N['en'];\n      return dict[key] || VESTING_VAULT_I18N['en'][key] || '';\n    }\n`;

  if (!html.includes('const VESTING_VAULT_I18N =')) {
    const fnStart = `function renderVestingVaultPage() {`;
    html = html.replace(fnStart, `${serializedVestingI18n}\n    function renderVestingVaultPage() {`);
  }

  // 6. Rewrite renderVestingVaultPage() to use getVestingText()
  // Replace the renderVestingVaultPage function with full clean implementation
  const oldVestingFnRegex = /function renderVestingVaultPage\(\) \{[\s\S]*?\/\/ STATE 1: Wallet not connected[\s\S]*?safeCreateIcons\(\);\s*return;\s*\}\s*\/\/ STATE 3: Active Allocation Found![\s\S]*?safeCreateIcons\(\);\s*\}/;

  const newVestingFn = `function renderVestingVaultPage() {
      const container = document.getElementById('vesting-vault-page-container');
      if (!container) return;

      const lang = window.haichainI18n ? window.haichainI18n.current() : 'en';
      const allocations = getStoredAllocations();
      let currentAddress = userWallet ? userWallet.address : null;
      if (!currentAddress) {
        try {
          const savedW = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
          if (savedW && savedW.address) {
            currentAddress = savedW.address;
            userWallet = savedW;
          }
        } catch (_) {}
      }
      const alloc = currentAddress ? allocations[currentAddress] : null;

      // Update sidebar indicator badge
      const sidebarBadge = document.getElementById('vesting-sidebar-badge');
      if (sidebarBadge) {
        if (alloc) sidebarBadge.classList.remove('hidden');
        else sidebarBadge.classList.add('hidden');
      }

      // STATE 1: Wallet not connected
      if (!currentAddress) {
        container.innerHTML = \`
          <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-black shadow-sm space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4">
              <div>
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-xl bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
                  </div>
                  <div>
                    <div class="flex items-center space-x-2">
                      <h2 class="font-bold text-lg sm:text-xl text-black dark:text-white">
                        \${getVestingText('vaultTitle', lang)}
                      </h2>
                      <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800">
                        Solana L1
                      </span>
                    </div>
                  </div>
                </div>
                <p class="text-xs text-neutral-500 mt-1">
                  \${getVestingText('vaultSubtitle', lang)}
                </p>
              </div>
              <div class="flex items-center space-x-2 shrink-0"></div>
            </div>

            <!-- Lock Box Prompt -->
            <div class="p-8 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-center max-w-xl mx-auto space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-neutral-200 dark:bg-neutral-800 flex items-center justify-center mx-auto text-black dark:text-white">
                <i data-lucide="shield-alert" class="w-6 h-6"></i>
              </div>
              <div>
                <h3 class="font-bold text-base text-black dark:text-white">
                  \${getVestingText('authRequired', lang)}
                </h3>
                <p class="text-xs text-neutral-500 mt-1.5 leading-relaxed">
                  \${getVestingText('authDesc', lang)}
                </p>
              </div>
              <div class="pt-2 flex flex-col sm:flex-row items-center justify-center gap-3">
                <button onclick="document.getElementById('wallet-btn').click()" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-xs transition-all shadow-sm">
                  \${getVestingText('connectWalletBtn', lang)}
                </button>
                <button onclick="window.switchTab('tab-preseed')" class="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white font-mono text-xs text-neutral-700 dark:text-neutral-300 transition-all">
                  \${getVestingText('subscribeSaftBtn', lang)}
                </button>
              </div>
            </div>
          </div>
        \`;
        safeCreateIcons();
        return;
      }

      // STATE 2: Wallet connected but no allocation found
      if (!alloc) {
        const shortAddr = \`\${currentAddress.slice(0, 4)}...\${currentAddress.slice(-4)}\`;
        container.innerHTML = \`
          <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-black shadow-sm space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4">
              <div>
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-xl bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
                  </div>
                  <div>
                    <div class="flex items-center space-x-2">
                      <h2 class="font-bold text-lg sm:text-xl text-black dark:text-white">
                        \${getVestingText('vaultTitle', lang)}
                      </h2>
                      <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800">
                        \${shortAddr}
                      </span>
                    </div>
                  </div>
                </div>
                <p class="text-xs text-neutral-500 mt-1">
                  \${getVestingText('authAddress', lang)} <span class="font-mono text-black dark:text-white font-bold">\${currentAddress}</span>
                </p>
              </div>
              <div class="flex items-center space-x-2 shrink-0"></div>
            </div>

            <div class="p-8 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-center max-w-xl mx-auto space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-neutral-200 dark:bg-neutral-800 flex items-center justify-center mx-auto text-neutral-500">
                <i data-lucide="inbox" class="w-6 h-6"></i>
              </div>
              <div>
                <h3 class="font-bold text-base text-black dark:text-white">
                  \${getVestingText('noAllocTitle', lang)}
                </h3>
                <p class="text-xs text-neutral-500 mt-1.5 leading-relaxed">
                  \${getVestingText('noAllocDesc', lang)}
                </p>
              </div>
              <div class="pt-2 flex flex-col sm:flex-row items-center justify-center gap-3">
                <button onclick="window.switchTab('tab-preseed')" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-xs transition-all shadow-sm">
                  \${getVestingText('subscribeDiscountBtn', lang)}
                </button>
                <button onclick="document.getElementById('wallet-btn').click()" class="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white font-mono text-xs text-neutral-700 dark:text-neutral-300 transition-all">
                  \${getVestingText('switchWalletBtn', lang)}
                </button>
              </div>
            </div>
          </div>
        \`;
        safeCreateIcons();
        return;
      }

      // STATE 3: Active Allocation Found!
      const haiTotal = alloc.haiTokens || Math.round((alloc.amountUsdt || 1000) / 0.007);
      const paidUsdt = alloc.amountUsdt || 1000;
      const tgeVal = haiTotal * 0.010;
      const unvestedYield = ((tgeVal - paidUsdt) / paidUsdt * 100).toFixed(1);
      const tgeClaimHai = Math.round(haiTotal * 0.2);
      const linearHai = haiTotal - tgeClaimHai;
      const monthlyStream = Math.round(linearHai / 6);
      const shortAddr = \`\${currentAddress.slice(0, 4)}...\${currentAddress.slice(-4)}\`;

      container.innerHTML = \`
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-black shadow-sm space-y-6">
          
          <!-- Section Header -->
          <div class="flex flex-col lg:flex-row lg:items-center justify-between pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4">
            <div class="flex items-center space-x-3.5 min-w-0">
              <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-2xl bg-black border border-neutral-800 flex items-center justify-center shadow-sm shrink-0 overflow-hidden p-1.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
              </div>
              <div class="min-w-0 space-y-1">
                <div class="flex flex-wrap items-center gap-2">
                  <h2 class="font-bold text-lg sm:text-xl text-black dark:text-white whitespace-nowrap">
                    \${getVestingText('portfolioTitle', lang)}
                  </h2>
                  <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-200 dark:border-neutral-800 font-semibold">
                    \${getVestingText('trancheBadge', lang)}
                  </span>
                  <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-black dark:text-white border border-neutral-300 dark:border-neutral-700 flex items-center space-x-1.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>
                    <span>\${getVestingText('transferHookStatus', lang)}</span>
                  </span>
                </div>
                <div class="flex items-center space-x-2 text-xs text-neutral-500 font-mono">
                  <span>\${getVestingText('authAddress', lang)}</span>
                  <span class="text-black dark:text-white font-bold">\${shortAddr}</span>
                </div>
              </div>
            </div>

            <!-- Header Actions -->
            <div class="flex items-center space-x-2 shrink-0">
              <button onclick="window.copyToken2022Mint()" class="px-4 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-xs transition-all shadow-sm flex items-center space-x-2">
                <div class="w-5 h-5 rounded-lg bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden p-0.5"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
                </div>
                <span>\${getVestingText('addToPhantomBtn', lang)}</span>
              </button>
              <button onclick="window.clearUserAllocation()" class="p-2.5 rounded-xl border border-neutral-200 dark:border-neutral-800 text-neutral-400 hover:text-black dark:hover:text-white transition-colors" title="\${getVestingText('resetSimTitle', lang)}">
                <i data-lucide="refresh-cw" class="w-4 h-4"></i>
              </button>
            </div>
          </div>

          <!-- 4 Executive KPI Cards -->
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 font-mono">
            <div class="p-4 sm:p-5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2">
              <span class="text-[10px] uppercase text-neutral-400 font-sans font-semibold block">\${getVestingText('kpiTotalBalance', lang)}</span>
              <div class="flex items-center space-x-2.5">
                <div class="w-7 h-7 rounded-lg bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden shadow-xs p-1"><img src="/assets/haisi-icon.png?v=haisi_symbol_2026" alt="HAISI" class="w-full h-full object-contain" onerror="if(!this.dataset.retry){this.dataset.retry=1;this.src='/app/assets/haisi-icon.png';}">
                </div>
                <div class="text-xl sm:text-2xl font-black text-black dark:text-white tabular-nums">\${haiTotal.toLocaleString()} <span class="text-xs font-bold text-neutral-400">HAISI</span></div>
              </div>
              <span class="text-[10px] text-neutral-500 font-sans block">\${getVestingText('kpiTokenStandard', lang)}</span>
            </div>

            <div class="p-4 sm:p-5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-1">
              <span class="text-[10px] uppercase text-neutral-400 font-sans font-semibold block">\${getVestingText('kpiCommittedCapital', lang)}</span>
              <div class="text-xl sm:text-2xl font-black text-black dark:text-white tabular-nums">$\${paidUsdt.toLocaleString()}</div>
              <span class="text-[10px] text-neutral-500 font-sans block">\${getVestingText('kpiTreasuryVault', lang)}</span>
            </div>

            <div class="p-4 sm:p-5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-1">
              <span class="text-[10px] uppercase text-neutral-400 font-sans font-semibold block">\${getVestingText('kpiTgeBenchmark', lang)}</span>
              <div class="text-xl sm:text-2xl font-black text-black dark:text-white tabular-nums">$0.010</div>
              <span class="text-[10px] text-neutral-500 font-sans block">\${getVestingText('kpiBenchmarkSubtitle', lang)}</span>
            </div>

            <div class="p-4 sm:p-5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-1">
              <span class="text-[10px] uppercase text-neutral-400 font-sans font-semibold block">\${getVestingText('kpiTgeValuation', lang)}</span>
              <div class="text-xl sm:text-2xl font-black text-black dark:text-white tabular-nums">$\${tgeVal.toLocaleString()}</div>
              <span class="text-[10px] text-neutral-600 dark:text-neutral-400 font-bold block">+\${unvestedYield}% \${getVestingText('kpiNotionalSurplus', lang)}</span>
            </div>
          </div>

          <!-- Deep Architecture Token-2022 Transfer-Hook Explainer -->
          <div class="p-5 sm:p-6 rounded-2xl bg-neutral-950 border border-neutral-800 text-neutral-300 font-mono text-xs space-y-3.5">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-neutral-800 gap-2">
              <div class="flex items-center space-x-2 text-white font-bold">
                <span class="px-2 py-0.5 rounded-md bg-white text-black text-[10px]">SOLANA TOKEN-2022</span>
                <span>\${getVestingText('transferHookTitle', lang)}</span>
              </div>
              <a href="https://explorer.solana.com/address/\${TOKEN_2022_MINT}?cluster=devnet" target="_blank" class="text-white hover:underline text-[11px] flex items-center space-x-1">
                <span>Mint: \${TOKEN_2022_MINT.slice(0, 8)}...\${TOKEN_2022_MINT.slice(-6)}</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>

            <p class="text-neutral-400 text-xs font-sans leading-relaxed">
              \${getVestingText('transferHookDesc', lang)}
            </p>

            <!-- 3-Phase Vesting Visual Timeline -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2 font-mono">
              <div class="p-3.5 rounded-xl bg-neutral-900 border border-neutral-800 space-y-1.5">
                <div class="flex items-center justify-between">
                  <span class="text-white font-bold text-xs">\${getVestingText('step1Title', lang)}</span>
                  <span class="px-1.5 py-0.5 rounded text-[9px] bg-white text-black font-bold">20%</span>
                </div>
                <div class="text-white font-bold text-sm">\${tgeClaimHai.toLocaleString()} HAISI</div>
                <p class="text-[10px] text-neutral-400 font-sans">\${getVestingText('step1Desc', lang)}</p>
              </div>

              <div class="p-3.5 rounded-xl bg-neutral-900 border border-neutral-800 space-y-1.5">
                <div class="flex items-center justify-between">
                  <span class="text-white font-bold text-xs">\${getVestingText('step2Title', lang)}</span>
                  <span class="px-1.5 py-0.5 rounded text-[9px] bg-neutral-800 text-neutral-400 font-bold">0%</span>
                </div>
                <div class="text-neutral-400 font-bold text-sm">0 HAISI</div>
                <p class="text-[10px] text-neutral-400 font-sans">\${getVestingText('step2Desc', lang)}</p>
              </div>

              <div class="p-3.5 rounded-xl bg-neutral-900 border border-neutral-800 space-y-1.5">
                <div class="flex items-center justify-between">
                  <span class="text-white font-bold text-xs">\${getVestingText('step3Title', lang)}</span>
                  <span class="px-1.5 py-0.5 rounded text-[9px] bg-white text-black font-bold">80%</span>
                </div>
                <div class="text-white font-bold text-sm">\${linearHai.toLocaleString()} HAISI</div>
                <p class="text-[10px] text-neutral-400 font-sans">\${getVestingText('step3Desc', lang)} (~\${monthlyStream.toLocaleString()} HAISI / mo)</p>
              </div>
            </div>
          </div>

        </div>
      \`;

      safeCreateIcons();
    }`;

  html = html.replace(oldVestingFnRegex, newVestingFn);

  // 7. Update copyToken2022Mint to use localized alert
  const oldCopyMintRegex = /window\.copyToken2022Mint = async function\(\) \{[\s\S]*?alert\(isVi[\s\S]*?\);\s*\} catch \(err\) \{/;
  const newCopyMint = `window.copyToken2022Mint = async function() {
      const lang = window.haichainI18n ? window.haichainI18n.current() : 'en';
      try {
        await navigator.clipboard.writeText(TOKEN_2022_MINT);
        alert(\`\${getVestingText('copyMintPrompt', lang)}\\n\\n\${TOKEN_2022_MINT}\\n\\n\${getVestingText('copyMintGuide', lang)}\`);
      } catch (err) {`;
  html = html.replace(oldCopyMintRegex, newCopyMint);

  // 8. Re-render vesting vault whenever language changes
  const langChangeTarget = `window.addEventListener('haichain:languageChanged', (e) => {`;
  const langChangeInject = `window.addEventListener('haichain:languageChanged', (e) => {
        const newLang = e.detail && (e.detail.lang || e.detail.language);
        if (typeof renderVestingVaultPage === 'function') {
          renderVestingVaultPage();
        }`;
  if (!html.includes('renderVestingVaultPage();\n        }')) {
    html = html.replace(langChangeTarget, langChangeInject);
  }

  // 9. When preset prompt buttons are clicked, update the prompt
  const presetBtnScript = `// Preset Prompt Buttons click listener
      document.querySelectorAll('.preset-prompt-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const promptInput = document.getElementById('playground-prompt');
          if (promptInput) {
            promptInput.value = btn.getAttribute('data-prompt') || '';
            promptInput.dataset.userEdited = 'true';
            promptInput.focus();
          }
        });
      });`;
  if (!html.includes('promptInput.dataset.userEdited')) {
    html = html.replace(`document.querySelectorAll('.preset-prompt-btn').forEach`, `// Track manual editing
      const playPromptInput = document.getElementById('playground-prompt');
      if (playPromptInput) {
        playPromptInput.addEventListener('input', () => { playPromptInput.dataset.userEdited = 'true'; });
      }
      document.querySelectorAll('.preset-prompt-btn').forEach`);
  }

  fs.writeFileSync(filePath, html, 'utf8');
  console.log('Successfully updated:', filePath);
}

patchDashboard('dashboard.html');
patchDashboard('app/dashboard.html');
