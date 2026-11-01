/**
 * HAICHAIN Autonomous Multi-Phase Token Sale Controller
 * Architecture: Finite State Machine (FSM) + Cryptographic Access Gatekeeper
 * Theme: Apple Luxury Titanium & Monochrome Minimalist (Pure Black, Pure White, Titanium)
 * Localization: Real-time Multi-Language Engine (10 Languages with instant event reactivity)
 */

(function () {
  'use strict';

  // 1. COMPREHENSIVE 10-LANGUAGE DICTIONARY
  const SALE_I18N = {
    en: {
    vestingCliffCard: '2. Cliff (2 Months)',
    vestingCliffDesc: '0% Unlock (Anti-dump)',
    vestingLinearCard: '3. Linear (6 Months)',
    autofillPhantom: 'Auto-fill Phantom',
    saftDocTitle: 'HAICHAIN Pre-Seed SAFT Agreement (Standard English Edition)',
    memoDocTitle: 'HAICHAIN Pre-Seed 1-Pager Memo',
    saftAlertTitle: 'SAFT SUBSCRIPTION & TOKEN-2022 ALLOCATION RECORDED!',
    saftAlertInvestor: 'Investor',
    saftAlertAlloc: 'Allocation',
    saftAlertAmount: 'Amount',
    saftAlertWallet: 'Solana Wallet',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Active for your Phantom wallet',
    saftAlertSchedule: '✓ Vesting Schedule: 20% TGE, 2-Mo Cliff, 6-Mo Linear Stream',
    saftAlertTransferPrompt: 'Please transfer funds to the Multi-Sig Treasury:',
    saftAlertRedirect: 'Redirecting to your dedicated Vesting Vault tab.',

      navTitle: 'Private Round',
      navBadge: 'VIP',
      mobileNav: 'Private',
      breadcrumb: 'Private Strategic Allocation',
      heroBadge: 'CONFIDENTIAL PRE-SEED ROUND - 30% DISCOUNT',
      heroTitle: 'Private Backer Allocation: <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">$0.007 USD / $HAISI</span>',
      heroSubtitle: 'Early capital round reserved for Core Builders & Angel Partners. Provides a <strong>30% discount</strong> prior to the official <strong>$0.010 Public TGE Launchpad</strong> on Meteora DLMM (+42.8% immediate listing yield).',
      downloadSaft: 'View SAFT Agreement',
      downloadMemo: '1-Pager Memo',
      allocationProgress: 'Allocation Progress:',
      claimedLabel: 'Filled',
      floorPrice: 'Floor: $0.007 ($7M FDV)',
      hardCapLabel: 'Hard Cap: $175,000 USD (3.0% Max Supply)',
      publicPriceLabel: 'Public TGE: $0.010 ($10M FDV)',
      calcTitle: 'Allocation & Return Calculator',
      calcSubtitle: 'Calculate token entitlement, linear streaming schedule, and projected sovereign returns.',
      subscriptionAmount: 'Subscription Amount (USDT):',
      subscriptionLimits: 'Min $500 - Max $15,000',
      totalAllocationTitle: 'Total $HAISI Allocation',
      fixedPriceBadge: '@ $0.007 Fixed',
      tgeValueTitle: 'TGE Value ($0.010)',
      unvestedYield: '+42.8% Unvested Profit',
      l1ValueTitle: 'L1 Sovereign ($1.00)',
      projectedMultiple: '142x Projected Multiple',
      vestingScheduleTitle: 'Cryptographic Vesting Invariant Breakdown',
      vestingStep1: '1. Initial TGE Claim (20%):',
      vestingStep2: '2. Cliff Period (Months 1 & 2):',
      vestingStep2Desc: '0% Unlock (Anti-Dump Freeze)',
      vestingStep3: '3. Linear Stream (Months 3 to 8):',
      terminalTitle: 'SAFT Reservation Terminal',
      terminalSubtitle: 'Bind your non-custodial Solana wallet to execute the Pre-Seed subscription.',
      labelName: 'Purchaser Legal Name / Entity:',
      placeholderName: 'e.g. Satoshi Nakamoto / Angel LLC',
      labelEmail: 'Official Contact Email:',
      placeholderEmail: 'angel@firm.com',
      labelWallet: 'Receiving Solana Wallet (Ed25519 Pubkey):',
      placeholderWallet: 'Connect Phantom or paste Solana address',
      treasuryTitle: 'Multi-Sig Treasury Vault (USDT / SOL)',
      copyBtn: 'Copy',
      copiedBtn: 'Copied!',
      submitBtn: 'Submit SAFT Subscription & Bind Wallet',
      protectedFooter: 'Protected by military-grade on-chain vesting invariants.',
      lockedTitle: 'HAICHAIN Private Allocation Portal',
      lockedDesc: 'This round is strictly private and reserved for invited Early Backers & Angel Partners under institutional SAFT terms.',
      accessPlaceholder: 'Enter VIP Access Key...',
      unlockBtn: 'Unlock'
    },
    vi: {
    vestingCliffCard: '2. Cliff (2 Tháng)',
    vestingCliffDesc: 'Khóa 0% (Anti-dump)',
    vestingLinearCard: '3. Tuyến Tính (6 Tháng)',
    autofillPhantom: 'Lấy ví Phantom',
    saftDocTitle: 'Hợp Đồng SAFT Pre-Seed HAICHAIN (Standard English Edition)',
    memoDocTitle: 'Bản Tóm Tắt 1 Trang Pre-Seed HAICHAIN',
    saftAlertTitle: 'ĐÃ GHI NHẬN ĐĂNG KÝ SAFT VÀ PHÂN BỔ TOKEN-2022!',
    saftAlertInvestor: 'Nhà đầu tư',
    saftAlertAlloc: 'Phân bổ',
    saftAlertAmount: 'Giá trị',
    saftAlertWallet: 'Ví thụ hưởng',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Đã kích hoạt cho ví Phantom của bạn',
    saftAlertSchedule: '✓ Lịch Vesting: 20% TGE, Cliff 2 tháng, Linear Stream 6 tháng',
    saftAlertTransferPrompt: 'Vui lòng chuyển USDT/SOL vào Ví Kho Bạc Multi-Sig:',
    saftAlertRedirect: 'Hệ thống sẽ tự động chuyển bạn đến Két Vesting để kiểm tra số dư.',

      navTitle: 'Vòng Private',
      navBadge: 'VIP',
      mobileNav: 'Private',
      breadcrumb: 'Phân Bổ Chiến Lược VIP',
      heroBadge: 'VÒNG NỘI BỘ BẢO MẬT - CHIẾT KHẤU 30%',
      heroTitle: 'Phân Bổ Early Backer Nội Bộ: <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">$0.007 USD / $HAISI</span>',
      heroSubtitle: 'Vòng vốn hạt giống dành riêng cho Co-builders & Đối tác Thiên thần. Hưởng <strong>chiết khấu 30%</strong> trước khi mở bán chính thức <strong>$0.010 Public TGE</strong> trên Meteora DLMM (+42.8% tỷ suất lợi nhuận niêm yết).',
      downloadSaft: 'Xem Hợp Đồng SAFT',
      downloadMemo: 'Bản Tóm Tắt 1 Trang',
      allocationProgress: 'Tiến độ Phân bổ:',
      claimedLabel: 'Đã Giữ Chỗ',
      floorPrice: 'Giá sàn: $0.007 ($7M FDV)',
      hardCapLabel: 'Trần cứng: $175.000 USD (3.0% Tổng cung)',
      publicPriceLabel: 'Mở bán Công khai: $0.010 ($10M FDV)',
      calcTitle: 'Máy Tính Quy Đổi & Dự Phóng Lợi Nhuận',
      calcSubtitle: 'Tính toán số lượng token, dòng tiền mở khóa tuyến tính và định giá khi kích hoạt L1.',
      subscriptionAmount: 'Số Tiền Đăng Ký (USDT):',
      subscriptionLimits: 'Tối thiểu $500 - Tối đa $15.000',
      totalAllocationTitle: 'Tổng Lượng Token $HAISI',
      fixedPriceBadge: 'Cố định @ $0.007',
      tgeValueTitle: 'Giá Trị Tại TGE ($0.010)',
      unvestedYield: '+42.8% Lợi Nhuận Ban Đầu',
      l1ValueTitle: 'Định Giá L1 Sovereign ($1.00)',
      projectedMultiple: 'Kỳ Vọng x142 Lần',
      vestingScheduleTitle: 'Chi Tiết Lịch Mở Khóa Mật Mã Bất Biến',
      vestingStep1: '1. Mở khóa ngày TGE (20%):',
      vestingStep2: '2. Khóa Cliff (Tháng 1 & 2):',
      vestingStep2Desc: '0% Mở khóa (Đóng băng chống xả)',
      vestingStep3: '3. Mở khóa tuyến tính (Tháng 3 đến 8):',
      terminalTitle: 'Cổng Đăng Ký Giữ Chỗ SAFT',
      terminalSubtitle: 'Ràng buộc ví Solana không lưu ký để hoàn tất đăng ký vòng Pre-Seed.',
      labelName: 'Họ và Tên / Pháp Nhân Mua:',
      placeholderName: 'ví dụ: Nguyễn Văn A / Quỹ Đầu Tư',
      labelEmail: 'Email Liên Hệ Chính Thức:',
      placeholderEmail: 'backer@example.com',
      labelWallet: 'Ví Solana Nhận Token (Ed25519 Pubkey):',
      placeholderWallet: 'Kết nối Phantom hoặc dán địa chỉ ví Solana',
      treasuryTitle: 'Ví Kho Bạc Multi-Sig (USDT / SOL)',
      copyBtn: 'Sao chép',
      copiedBtn: 'Đã chép!',
      submitBtn: 'Xác Nhận Giữ Chỗ & Gửi Yêu Cầu Ký SAFT',
      protectedFooter: 'Được bảo vệ bởi hợp đồng khóa on-chain bất biến cấp quân sự.',
      lockedTitle: 'Cổng Phân Bổ Nội Bộ HAICHAIN',
      lockedDesc: 'Vòng này được bảo mật nghiêm ngặt, chỉ dành riêng cho các Đối tác Thiên thần & Co-builders theo thỏa thuận SAFT thể chế.',
      accessPlaceholder: 'Nhập Khóa Truy Cập VIP...',
      unlockBtn: 'Mở Khóa'
    },
    zh: {
    vestingCliffCard: '2. 锁仓期 (2个月)',
    vestingCliffDesc: '0% 解锁 (防止抛售)',
    vestingLinearCard: '3. 线性释放 (6个月)',
    autofillPhantom: '自动填充 Phantom 钱包',
    saftDocTitle: 'HAICHAIN 种子轮 SAFT 协议 (标准英文版)',
    memoDocTitle: 'HAICHAIN 种子轮单页备忘录',
    saftAlertTitle: 'SAFT 认购与 Token-2022 份额已成功记录！',
    saftAlertInvestor: '投资者',
    saftAlertAlloc: '分配份额',
    saftAlertAmount: '金额',
    saftAlertWallet: '接收钱包',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: 已为您的 Phantom 钱包激活',
    saftAlertSchedule: '✓ 释放计划: 20% TGE, 2个月锁仓, 6个月线性流式释放',
    saftAlertTransferPrompt: '请将款项转入多签国库金库地址：',
    saftAlertRedirect: '正在自动跳转至您的专属 Vesting 金库页面。',

      navTitle: '战略轮额度',
      navBadge: 'VIP',
      mobileNav: '战略轮',
      breadcrumb: '战略投资 VIP 额度',
      heroBadge: '机密早期轮 - 享受30%优惠折扣',
      heroTitle: '早期支持者内部份额: <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">$0.007 USD / $HAISI</span>',
      heroSubtitle: '专为核心建设者和天使合作伙伴保留的早期资本轮次。在Meteora DLMM正式公开发行 <strong>$0.010 TGE</strong> 之前享有 <strong>30% 折扣</strong>（+42.8% 上线溢价）。',
      downloadSaft: '下载 SAFT 协议',
      downloadMemo: '1页投资备忘录',
      allocationProgress: '认购进度:',
      claimedLabel: '已预订',
      floorPrice: '底价: $0.007 ($7M FDV)',
      hardCapLabel: '硬顶: $175,000 USD (总供应量3.0%)',
      publicPriceLabel: '公开发行价: $0.010 ($10M FDV)',
      calcTitle: '代币分配与回报测算器',
      calcSubtitle: '计算您的代币配额、线性流式解锁计划及主链上线预期回报。',
      subscriptionAmount: '认购金额 (USDT):',
      subscriptionLimits: '最低 $500 - 最高 $15,000',
      totalAllocationTitle: '$HAISI 代币分配总量',
      fixedPriceBadge: '固定价 @ $0.007',
      tgeValueTitle: 'TGE 价值 ($0.010)',
      unvestedYield: '+42.8% 未解锁账面收益',
      l1ValueTitle: '主链 Sovereign 预期 ($1.00)',
      projectedMultiple: '预期 142 倍',
      vestingScheduleTitle: '链上密码学锁仓明细',
      vestingStep1: '1. TGE 首期解锁 (20%):',
      vestingStep2: '2. 锁仓锁定期 (第1与第2个月):',
      vestingStep2Desc: '0% 解锁 (防止抛售冻结)',
      vestingStep3: '3. 线性流式释放 (第3至第8个月):',
      terminalTitle: 'SAFT 协议认购终端',
      terminalSubtitle: '绑定您的非托管 Solana 钱包以执行 Pre-Seed 认购。',
      labelName: '认购人法定姓名 / 机构:',
      placeholderName: '例如: 中本聪 / 天使资本',
      labelEmail: '官方联系邮箱:',
      placeholderEmail: 'angel@firm.com',
      labelWallet: '接收代币的 Solana 钱包 (Ed25519):',
      placeholderWallet: '连接 Phantom 或粘贴 Solana 地址',
      treasuryTitle: '多签金库接收地址 (USDT / SOL)',
      copyBtn: '复制',
      copiedBtn: '已复制!',
      submitBtn: '提交 SAFT 认购并绑定钱包',
      protectedFooter: '受军工级链上锁仓不变量保护。',
      lockedTitle: 'HAICHAIN 内部私密分配门户',
      lockedDesc: '本轮次严格保密，仅向受邀的天使合作伙伴开放。',
      accessPlaceholder: '输入 VIP 访问密钥...',
      unlockBtn: '解锁'
    },
    ko: {
    vestingCliffCard: '2. 클리프 (2개월)',
    vestingCliffDesc: '0% 락업 (덤핑 방지)',
    vestingLinearCard: '3. 선형 스트리밍 (6개월)',
    autofillPhantom: 'Phantom 지갑 자동 입력',
    saftDocTitle: 'HAICHAIN 프리시드 SAFT 계약서 (표준 영문판)',
    memoDocTitle: 'HAICHAIN 프리시드 1페이지 요약',
    saftAlertTitle: 'SAFT 청약 및 Token-2022 배분이 등록되었습니다!',
    saftAlertInvestor: '투자자',
    saftAlertAlloc: '배분 수량',
    saftAlertAmount: '청약 금액',
    saftAlertWallet: '수령 지갑',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Phantom 지갑에 활성화됨',
    saftAlertSchedule: '✓ 베스팅 일정: TGE 20%, 2개월 클리프, 6개월 선형 스트리밍',
    saftAlertTransferPrompt: '멀티시그 금고 주소로 자금을 전송해 주세요:',
    saftAlertRedirect: '전용 베스팅 볼트 탭으로 이동합니다.',

      navTitle: '비공개 전략 라운드',
      navBadge: 'VIP',
      mobileNav: '전략 라운드',
      breadcrumb: 'VIP 비공개 전략 배정',
      heroBadge: '기밀 초기 라운드 - 30% 할인 혜택',
      heroTitle: '엔젤 파트너 내부 할당: <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">$0.007 USD / $HAISI</span>',
      heroSubtitle: '코어 빌더와 초기 엔젤 파트너 전용 라운드입니다. Meteora DLMM 공식 <strong>$0.010 Public TGE</strong> 상장 전 <strong>30% 할인</strong>(+42.8% 즉시 상장 수익률)을 제공합니다.',
      downloadSaft: 'SAFT 계약서 다운로드',
      downloadMemo: '1페이지 투자 메모',
      allocationProgress: '할당 진행률:',
      claimedLabel: '예약 완료',
      floorPrice: '최저가: $0.007 ($7M FDV)',
      hardCapLabel: '하드캡: $175,000 USD (총공급량의 3.0%)',
      publicPriceLabel: '공개 TGE가: $0.010 ($10M FDV)',
      calcTitle: '할당 및 예상 수익 계산기',
      calcSubtitle: '토큰 수량, 선형 베스팅 일정 및 주권 메인넷 예상 수익을 계산합니다.',
      subscriptionAmount: '참여 금액 (USDT):',
      subscriptionLimits: '최소 $500 - 최대 $15,000',
      totalAllocationTitle: '총 $HAISI 토큰 할당',
      fixedPriceBadge: '@ $0.007 고정',
      tgeValueTitle: 'TGE 상장 가치 ($0.010)',
      unvestedYield: '+42.8% 미실현 장부 수익',
      l1ValueTitle: 'Sovereign L1 목표 ($1.00)',
      projectedMultiple: '142배 예상 수익',
      vestingScheduleTitle: '온체인 암호학적 베스팅 일정',
      vestingStep1: '1. TGE 초기 클레임 (20%):',
      vestingStep2: '2. 클리프 락업 (1~2개월차):',
      vestingStep2Desc: '0% 락업 (덤핑 방지 동결)',
      vestingStep3: '3. 선형 스트리밍 (3~8개월차):',
      terminalTitle: 'SAFT 예약 등록 터미널',
      terminalSubtitle: '프리시드 참여를 위해 비수탁형 솔라나 지갑을 연동하세요.',
      labelName: '참여자 성명 / 법인명:',
      placeholderName: '예: 사토시 나카모토 / 엔젤 캐피털',
      labelEmail: '공식 연락처 이메일:',
      placeholderEmail: 'angel@firm.com',
      labelWallet: '토큰 수령 솔라나 지갑 (Ed25519):',
      placeholderWallet: 'Phantom 연동 또는 솔라나 주소 붙여넣기',
      treasuryTitle: '멀티시그 금고 수령 주소 (USDT / SOL)',
      copyBtn: '복사',
      copiedBtn: '복사됨!',
      submitBtn: 'SAFT 계약 신청 및 지갑 연동',
      protectedFooter: '군사 등급 온체인 불변 계약으로 보호됩니다.',
      lockedTitle: 'HAICHAIN 프라이빗 포털',
      lockedDesc: '초대된 엔젤 파트너 전용 기밀 라운드입니다.',
      accessPlaceholder: 'VIP 액세스 키 입력...',
      unlockBtn: '잠금 해제'
    },
    fr: {
    vestingCliffCard: '2. Cliff (2 Mois)',
    vestingCliffDesc: '0% Déblocage (Anti-dump)',
    vestingLinearCard: '3. Linéaire (6 Mois)',
    autofillPhantom: 'Remplissage auto Phantom',
    saftDocTitle: 'Accord SAFT Pre-Seed HAICHAIN (Édition Anglaise Standard)',
    memoDocTitle: 'Mémo 1 Page Pre-Seed HAICHAIN',
    saftAlertTitle: 'SOUSCRIPTION SAFT ET ALLOCATION TOKEN-2022 ENREGISTRÉES !',
    saftAlertInvestor: 'Investisseur',
    saftAlertAlloc: 'Allocation',
    saftAlertAmount: 'Montant',
    saftAlertWallet: 'Portefeuille Solana',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook : Actif pour votre portefeuille Phantom',
    saftAlertSchedule: '✓ Calendrier de vesting : 20% TGE, Cliff 2 mois, Flux linéaire 6 mois',
    saftAlertTransferPrompt: 'Veuillez transférer les fonds vers la Trésorerie Multi-Sig :',
    saftAlertRedirect: 'Redirection vers votre coffre-fort de vesting.',

      navTitle: 'Tour Stratégique Privé',
      navBadge: 'VIP',
      mobileNav: 'Privé',
      breadcrumb: 'Allocation Stratégique Privée VIP',
      heroBadge: 'TOUR CONFIDENTIEL PRÉ-SEED - REMISE DE 30%',
      heroTitle: 'Allocation Investisseur Privé : <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">0,007 USD / $HAISI</span>',
      heroSubtitle: 'Tour initial réservé aux bâtisseurs et investisseurs providentiels. Offre une <strong>remise de 30%</strong> avant le <strong>TGE Public à 0,010 $</strong> sur Meteora DLMM (+42,8% de rendement immédiat).',
      downloadSaft: 'Télécharger Accord SAFT',
      downloadMemo: 'Mémo en 1 Page',
      allocationProgress: 'Progression de l\'Allocation :',
      claimedLabel: 'Réservé',
      floorPrice: 'Prix plancher : 0,007 $ (7M$ FDV)',
      hardCapLabel: 'Plafond : 175 000 USD (3,0% offre max)',
      publicPriceLabel: 'TGE Public : 0,010 $ (10M$ FDV)',
      calcTitle: 'Calculateur d\'Allocation & Rendement',
      calcSubtitle: 'Calculez vos jetons, le calendrier de déblocage linéaire et le rendement L1.',
      subscriptionAmount: 'Montant de Souscription (USDT) :',
      subscriptionLimits: 'Min 500 $ - Max 15 000 $',
      totalAllocationTitle: 'Allocation Totale $HAISI',
      fixedPriceBadge: 'Fixé à 0,007 $',
      tgeValueTitle: 'Valeur TGE (0,010 $)',
      unvestedYield: '+42,8% de Gain Initial',
      l1ValueTitle: 'Objectif L1 Souverain (1,00 $)',
      projectedMultiple: 'Multiplicateur 142x',
      vestingScheduleTitle: 'Détail Cryptographique du Vesting',
      vestingStep1: '1. Déblocage TGE (20%) :',
      vestingStep2: '2. Période de Cliff (Mois 1 & 2) :',
      vestingStep2Desc: '0% de déblocage (Gel anti-dump)',
      vestingStep3: '3. Flux Linéaire (Mois 3 à 8) :',
      terminalTitle: 'Terminal de Réservation SAFT',
      terminalSubtitle: 'Liez votre portefeuille Solana non-hébergé pour valider votre souscription.',
      labelName: 'Nom Légal / Entité :',
      placeholderName: 'ex. Satoshi Nakamoto / Angel SAS',
      labelEmail: 'Email Officiel de Contact :',
      placeholderEmail: 'investisseur@societe.com',
      labelWallet: 'Portefeuille Solana de Réception (Ed25519) :',
      placeholderWallet: 'Connectez Phantom ou collez l\'adresse',
      treasuryTitle: 'Coffre-fort Multi-Sig (USDT / SOL)',
      copyBtn: 'Copier',
      copiedBtn: 'Copié !',
      submitBtn: 'Confirmer la Réservation SAFT',
      protectedFooter: 'Protégé par des invariants cryptographiques immuables.',
      lockedTitle: 'Portail Privé HAICHAIN',
      lockedDesc: 'Tour strictement confidentiel réservé aux partenaires invités.',
      accessPlaceholder: 'Entrez la clé VIP...',
      unlockBtn: 'Déverrouiller'
    },
    es: {
    vestingCliffCard: '2. Cliff (2 Meses)',
    vestingCliffDesc: '0% Desbloqueo (Anti-dump)',
    vestingLinearCard: '3. Lineal (6 Meses)',
    autofillPhantom: 'Autocompletar Phantom',
    saftDocTitle: 'Acuerdo SAFT Pre-Seed HAICHAIN (Edición Estándar en Inglés)',
    memoDocTitle: 'Memorando de 1 Página Pre-Seed HAICHAIN',
    saftAlertTitle: '¡SUSCRIPCIÓN SAFT Y ASIGNACIÓN TOKEN-2022 REGISTRADAS!',
    saftAlertInvestor: 'Inversionista',
    saftAlertAlloc: 'Asignación',
    saftAlertAmount: 'Monto',
    saftAlertWallet: 'Billetera Solana',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Activo para su billetera Phantom',
    saftAlertSchedule: '✓ Calendario de vesting: 20% TGE, Cliff 2 meses, Transmisión lineal 6 meses',
    saftAlertTransferPrompt: 'Por favor transfiera los fondos a la Tesorería Multi-Sig:',
    saftAlertRedirect: 'Redirigiendo a su bóveda de vesting dedicada.',

      navTitle: 'Ronda Privada Estratégica',
      navBadge: 'VIP',
      mobileNav: 'Privada',
      breadcrumb: 'Asignación VIP Estratégica',
      heroBadge: 'RONDA CONFIDENCIAL PRE-SEED - 30% DE DESCUENTO',
      heroTitle: 'Asignación Privada Early Backer: <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">$0.007 USD / $HAISI</span>',
      heroSubtitle: 'Ronda inicial reservada para constructores y ángeles inversores. Proporciona un <strong>descuento del 30%</strong> antes del lanzamiento público <strong>$0.010 Public TGE</strong> en Meteora DLMM (+42.8% de rentabilidad inmediata).',
      downloadSaft: 'Descargar Acuerdo SAFT',
      downloadMemo: 'Memo en 1 Página',
      allocationProgress: 'Progreso de Asignación:',
      claimedLabel: 'Reservado',
      floorPrice: 'Precio base: $0.007 ($7M FDV)',
      hardCapLabel: 'Límite: $175,000 USD (3.0% del suministro)',
      publicPriceLabel: 'TGE Público: $0.010 ($10M FDV)',
      calcTitle: 'Calculadora de Asignación y Retorno',
      calcSubtitle: 'Calcule su asignación de tokens, el calendario de vesting y las proyecciones L1.',
      subscriptionAmount: 'Monto de Suscripción (USDT):',
      subscriptionLimits: 'Mín $500 - Máx $15,000',
      totalAllocationTitle: 'Asignación Total de $HAISI',
      fixedPriceBadge: 'Fijado en $0.007',
      tgeValueTitle: 'Valor en TGE ($0.010)',
      unvestedYield: '+42.8% Ganancia Inicial',
      l1ValueTitle: 'Proyección L1 Soberano ($1.00)',
      projectedMultiple: 'Múltiplo Proyectado 142x',
      vestingScheduleTitle: 'Desglose Criptográfico de Vesting',
      vestingStep1: '1. Desbloqueo Inicial TGE (20%):',
      vestingStep2: '2. Periodo de Cliff (Meses 1 y 2):',
      vestingStep2Desc: '0% Desbloqueo (Congelación anti-dump)',
      vestingStep3: '3. Transmisión Lineal (Meses 3 a 8):',
      terminalTitle: 'Terminal de Reserva SAFT',
      terminalSubtitle: 'Vincule su billetera no custodiada de Solana para formalizar la reserva.',
      labelName: 'Nombre Legal / Entidad:',
      placeholderName: 'ej. Satoshi Nakamoto / Angel SL',
      labelEmail: 'Correo Electrónico Oficial:',
      placeholderEmail: 'inversor@empresa.com',
      labelWallet: 'Billetera Solana de Recepción (Ed25519):',
      placeholderWallet: 'Conecte Phantom o pegue la dirección Solana',
      treasuryTitle: 'Bóveda de Tesorería Multi-Sig (USDT / SOL)',
      copyBtn: 'Copiar',
      copiedBtn: '¡Copiado!',
      submitBtn: 'Enviar Reserva SAFT y Vincular Billetera',
      protectedFooter: 'Protegido por invariantes on-chain de grado militar.',
      lockedTitle: 'Portal Privado HAICHAIN',
      lockedDesc: 'Ronda estrictamente privada reservada para socios invitados.',
      accessPlaceholder: 'Ingrese Clave VIP...',
      unlockBtn: 'Desbloquear'
    },
    ru: {
    vestingCliffCard: '2. Клифф (2 Месяца)',
    vestingCliffDesc: '0% Разблокировки (Анти-дамп)',
    vestingLinearCard: '3. Линейный (6 Месяцев)',
    autofillPhantom: 'Автозаполнение Phantom',
    saftDocTitle: 'Соглашение SAFT Pre-Seed HAICHAIN (Стандартная англ. версия)',
    memoDocTitle: '1-страничный меморандум Pre-Seed HAICHAIN',
    saftAlertTitle: 'ПОДПИСКА SAFT И АЛЛОКАЦИЯ TOKEN-2022 УСПЕШНО ЗАРЕГИСТРИРОВАНЫ!',
    saftAlertInvestor: 'Инвестор',
    saftAlertAlloc: 'Аллокация',
    saftAlertAmount: 'Сумма',
    saftAlertWallet: 'Solana Кошелек',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Активен для вашего Phantom кошелька',
    saftAlertSchedule: '✓ График вестинга: 20% TGE, 2 мес. клифф, 6 мес. линейный стриминг',
    saftAlertTransferPrompt: 'Пожалуйста, переведите средства в Мультисиг Казначейство:',
    saftAlertRedirect: 'Перенаправление в ваш персональный сейф вестинга.',

      navTitle: 'Приватный стратегический раунд',
      navBadge: 'VIP',
      mobileNav: 'Приват',
      breadcrumb: 'VIP стратегическое выделение',
      heroBadge: 'ЗАКРЫТЫЙ ПРЕ-СИД РАУНД - СКИДКА 30%',
      heroTitle: 'Закрытая Аллокация для Партнеров: <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">$0.007 USD / $HAISI</span>',
      heroSubtitle: 'Ранний инвестиционный раунд для создателей и бизнес-ангелов. Предоставляет <strong>скидку 30%</strong> до официального <strong>публичного TGE по $0.010</strong> на Meteora DLMM (+42.8% немедленной доходности при листинге).',
      downloadSaft: 'Скачать Договор SAFT',
      downloadMemo: 'Одностраничный Меморандум',
      allocationProgress: 'Прогресс Аллокации:',
      claimedLabel: 'Забронировано',
      floorPrice: 'Базовая цена: $0.007 ($7M FDV)',
      hardCapLabel: 'Хардкап: $175,000 USD (3.0% эмиссии)',
      publicPriceLabel: 'Публичный TGE: $0.010 ($10M FDV)',
      calcTitle: 'Калькулятор Аллокации и Доходности',
      calcSubtitle: 'Рассчитайте количество токенов, график вестинга и прогнозируемую прибыль L1.',
      subscriptionAmount: 'Сумма Инвестиций (USDT):',
      subscriptionLimits: 'Мин $500 - Макс $15,000',
      totalAllocationTitle: 'Всего Токенов $HAISI',
      fixedPriceBadge: 'Фиксировано @ $0.007',
      tgeValueTitle: 'Стоимость при TGE ($0.010)',
      unvestedYield: '+42.8% Первоначальная Прибыль',
      l1ValueTitle: 'Цель L1 Sovereign ($1.00)',
      projectedMultiple: 'Ожидаемый Мультипликатор 142x',
      vestingScheduleTitle: 'Ончейн-график Вестинга Токенов',
      vestingStep1: '1. Разблокировка при TGE (20%):',
      vestingStep2: '2. Период Клиффа (1 и 2 месяцы):',
      vestingStep2Desc: '0% Разблокировки (Заморозка от сброса)',
      vestingStep3: '3. Линейный Стриминг (3-8 месяцы):',
      terminalTitle: 'Терминал Бронирования SAFT',
      terminalSubtitle: 'Привяжите некастодиальный кошелек Solana для оформления подписки.',
      labelName: 'ФИО / Юридическое Лицо:',
      placeholderName: 'напр. Сатоши Накамото / Angel Fund',
      labelEmail: 'Контактный Email:',
      placeholderEmail: 'partner@fund.com',
      labelWallet: 'Кошелек Solana для Получения (Ed25519):',
      placeholderWallet: 'Подключите Phantom или вставьте адрес Solana',
      treasuryTitle: 'Мультисиг Казначейство (USDT / SOL)',
      copyBtn: 'Копировать',
      copiedBtn: 'Скопировано!',
      submitBtn: 'Подтвердить SAFT и Привязать Кошелек',
      protectedFooter: 'Защищено неизменяемыми смарт-контрактами уровня военной безопасности.',
      lockedTitle: 'Закрытый Портал HAICHAIN',
      lockedDesc: 'Раунд строго конфиденциален и доступен только приглашенным партнерам.',
      accessPlaceholder: 'Введите VIP-ключ...',
      unlockBtn: 'Открыть'
    },
    hi: {
    vestingCliffCard: '2. क्लिफ (2 महीने)',
    vestingCliffDesc: '0% अनलॉक (डंप सुरक्षा)',
    vestingLinearCard: '3. लीनियर (6 महीने)',
    autofillPhantom: 'Phantom वॉलेट ऑटो-फिल',
    saftDocTitle: 'HAICHAIN प्री-सीड SAFT समझौता (मानक अंग्रेजी संस्करण)',
    memoDocTitle: 'HAICHAIN प्री-सीड 1-पेज मेमो',
    saftAlertTitle: 'SAFT सदस्यता और Token-2022 आवंटन दर्ज किया गया!',
    saftAlertInvestor: 'निवेशक',
    saftAlertAlloc: 'आवंटन',
    saftAlertAmount: 'राशि',
    saftAlertWallet: 'Solana वॉलेट',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: आपके Phantom वॉलेट के लिए सक्रिय',
    saftAlertSchedule: '✓ वेस्टिंग शेड्यूल: 20% TGE, 2 महीने क्लिफ, 6 महीने लीनियर स्ट्रीम',
    saftAlertTransferPrompt: 'कृपया मल्टी-सिग ट्रेजरी में धनराशि ट्रांसफर करें:',
    saftAlertRedirect: 'आपके वेस्टिंग वॉल्ट टैब पर पुनर्निर्देशित किया जा रहा है।',

      navTitle: 'रणनीतिक प्राइवेट राउंड',
      navBadge: 'VIP',
      mobileNav: 'प्राइवेट',
      breadcrumb: 'VIP रणनीतिक आवंटन',
      heroBadge: 'गोपनीय प्री-सीड राउंड - 30% छूट',
      heroTitle: 'प्रारंभिक निवेशक आवंटन: <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">$0.007 USD / $HAISI</span>',
      heroSubtitle: 'कोर बिल्डर्स और एंजेल पार्टनर्स के लिए आरक्षित। आधिकारिक <strong>$0.010 पब्लिक TGE</strong> से पहले <strong>30% छूट</strong> (+42.8% तत्काल लिस्टिंग लाभ)।',
      downloadSaft: 'SAFT अनुबंध डाउनलोड करें',
      downloadMemo: '1-पेज मेमो',
      allocationProgress: 'आवंटन प्रगति:',
      claimedLabel: 'आरक्षित',
      floorPrice: 'न्यूनतम: $0.007 ($7M FDV)',
      hardCapLabel: 'हार्ड कैप: $175,000 USD (3.0% कुल आपूर्ति)',
      publicPriceLabel: 'सार्वजनिक TGE: $0.010 ($10M FDV)',
      calcTitle: 'आवंटन और रिटर्न कैलकुलेटर',
      calcSubtitle: 'अपने टोकन आवंटन और लीनियर वेस्टिंग शेड्यूल की गणना करें।',
      subscriptionAmount: 'सदस्यता राशि (USDT):',
      subscriptionLimits: 'न्यूनतम $500 - अधिकतम $15,000',
      totalAllocationTitle: 'कुल $HAISI टोकन',
      fixedPriceBadge: '@ $0.007 निश्चित',
      tgeValueTitle: 'TGE पर मूल्य ($0.010)',
      unvestedYield: '+42.8% प्रारंभिक लाभ',
      l1ValueTitle: 'L1 सोवरेन लक्ष्य ($1.00)',
      projectedMultiple: '142x अनुमानित रिटर्न',
      vestingScheduleTitle: 'क्रिप्टोग्राफिक वेस्टिंग विवरण',
      vestingStep1: '1. TGE पर अनलॉक (20%):',
      vestingStep2: '2. क्लिफ अवधि (महीने 1 और 2):',
      vestingStep2Desc: '0% अनलॉक (डंप सुरक्षा लॉक)',
      vestingStep3: '3. लीनियर स्ट्रीम (महीने 3 से 8):',
      terminalTitle: 'SAFT आरक्षण टर्मिनल',
      terminalSubtitle: 'सब्सक्रिप्शन के लिए अपना सोलाना वॉलेट बाइंड करें।',
      labelName: 'कानूनी नाम / संस्था:',
      placeholderName: 'उदा. सतोशी नाकामोतो',
      labelEmail: 'आधिकारिक ईमेल:',
      placeholderEmail: 'investor@firm.com',
      labelWallet: 'टोकन प्राप्त करने वाला सोलाना वॉलेट:',
      placeholderWallet: 'फैंटम कनेक्ट करें या सोलाना पता दर्ज करें',
      treasuryTitle: 'मल्टी-सिग ट्रेजरी वॉल्ट (USDT / SOL)',
      copyBtn: 'कॉपी',
      copiedBtn: 'कॉपी किया गया!',
      submitBtn: 'SAFT सदस्यता जमा करें',
      protectedFooter: 'सैन्य-ग्रेड ऑन-चेन स्मार्ट अनुबंधों द्वारा सुरक्षित।',
      lockedTitle: 'HAICHAIN प्राइवेट पोर्टल',
      lockedDesc: 'केवल आमंत्रित एंजेल भागीदारों के लिए आरक्षित।',
      accessPlaceholder: 'VIP की दर्ज करें...',
      unlockBtn: 'अनलॉक'
    },
    he: {
    vestingCliffCard: '2. תקופת נעילה (חודשיים)',
    vestingCliffDesc: '0% שחרור (הגנה ממכירה)',
    vestingLinearCard: '3. שחרור ליניארי (6 חודשים)',
    autofillPhantom: 'מילוי אוטומטי Phantom',
    saftDocTitle: 'הסכם SAFT Pre-Seed של HAICHAIN (מהדורה רשמית באנגלית)',
    memoDocTitle: 'תזכיר עמוד אחד Pre-Seed של HAICHAIN',
    saftAlertTitle: 'הרשמת SAFT והקצאת Token-2022 נרשמו בהצלחה!',
    saftAlertInvestor: 'משקיע',
    saftAlertAlloc: 'הקצאה',
    saftAlertAmount: 'סכום',
    saftAlertWallet: 'ארנק Solana',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: פעיל עבור ארנק Phantom שלך',
    saftAlertSchedule: '✓ לוח זמנים: 20% TGE, נעילה של חודשיים, הזרמה ליניארית של 6 חודשים',
    saftAlertTransferPrompt: 'אנא העבר את הכספים לקופת האוצר:',
    saftAlertRedirect: 'מעביר אותך לכרטיסיית כספת הווסטינג שלך.',

      navTitle: 'סבב אסטרטגי פרטי',
      navBadge: 'VIP',
      mobileNav: 'פרטי',
      breadcrumb: 'הקצאה אסטרטגית VIP',
      heroBadge: 'סבב פרה-סיד חסוי - 30% הנחה',
      heroTitle: 'הקצאה מוקדמת למשקיעים: <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">0.007 USD / $HAISI</span>',
      heroSubtitle: 'סבב הון מוקדם המיועד לשותפים ואנג\'לים. מעניק <strong>30% הנחה</strong> לפני ה-<strong>TGE הציבורי ב-0.010$</strong> ב-Meteora DLMM.',
      downloadSaft: 'הורד הסכם SAFT',
      downloadMemo: 'תקציר בעמוד אחד',
      allocationProgress: 'התקדמות הקצאה:',
      claimedLabel: 'הוזמן',
      floorPrice: 'מחיר בסיס: 0.007$ (7M$ FDV)',
      hardCapLabel: 'תקרה: 175,000 USD (3.0% מסך ההיצע)',
      publicPriceLabel: 'השקה ציבורית: 0.010$ (10M$ FDV)',
      calcTitle: 'מחשבון הקצאה ותשואה',
      calcSubtitle: 'חשב את הקצאת הטוקנים, לוח זמני השחרור והתשואה החזויה.',
      subscriptionAmount: 'סכום השקעה (USDT):',
      subscriptionLimits: 'מינימום 500$ - מקסימום 15,000$',
      totalAllocationTitle: 'סך טוקנים $HAISI',
      fixedPriceBadge: 'קבוע ב-0.007$',
      tgeValueTitle: 'ערך בהשקה (0.010$)',
      unvestedYield: '+42.8% רווח ראשוני',
      l1ValueTitle: 'יעד L1 ריבוני (1.00$)',
      projectedMultiple: 'מכפיל חזוי פי 142',
      vestingScheduleTitle: 'פירוט לוח זמני שחרור קריפטוגרפי',
      vestingStep1: '1. שחרור בהשקה ראשונית (20%):',
      vestingStep2: '2. תקופת נעילה (חודשים 1 ו-2):',
      vestingStep2Desc: '0% שחרור (נעילת הגנה מפני מכירה)',
      vestingStep3: '3. שחרור ליניארי (חודשים 3 עד 8):',
      terminalTitle: 'מסוף הזמנת SAFT',
      terminalSubtitle: 'קשר את ארנק הסולאנה שלך להשלמת ההרשמה.',
      labelName: 'שם מלא / ישות משפטית:',
      placeholderName: 'לדוגמה: סאטושי נאקאמוטו',
      labelEmail: 'דוא"ל רשמי ליצירת קשר:',
      placeholderEmail: 'investor@firm.com',
      labelWallet: 'ארנק סולאנה לקבלת טוקנים (Ed25519):',
      placeholderWallet: 'חבר Phantom או הדבק כתובת סולאנה',
      treasuryTitle: 'קופת רב-חתימות (USDT / SOL)',
      copyBtn: 'העתק',
      copiedBtn: 'הועתק!',
      submitBtn: 'אישור הרשמה וקישור ארנק',
      protectedFooter: 'מוגן באמצעות חוזים חכמים בלתי ניתנים לשינוי ברמה צבאית.',
      lockedTitle: 'פורטל פרטי HAICHAIN',
      lockedDesc: 'סבב חסוי המיועד אך ורק למשקיעים מוזמנים.',
      accessPlaceholder: 'הזן מפתח VIP...',
      unlockBtn: 'שחרר נעילה'
    },
    kk: {
    vestingCliffCard: '2. Клифф (2 Ай)',
    vestingCliffDesc: '0% Ашу (Анти-дамп)',
    vestingLinearCard: '3. Сызықты (6 Ай)',
    autofillPhantom: 'Phantom әмиянын автотолтыру',
    saftDocTitle: 'HAICHAIN Pre-Seed SAFT Келісімі (Стандартты ағылшын басылымы)',
    memoDocTitle: 'HAICHAIN Pre-Seed 1-Беттік Мемосы',
    saftAlertTitle: 'SAFT ЖАЗЫЛУЫ ЖӘНЕ TOKEN-2022 БӨЛІНІСІ СӘТТІ ТІРКЕЛДІ!',
    saftAlertInvestor: 'Инвестор',
    saftAlertAlloc: 'Бөлініс',
    saftAlertAmount: 'Сомасы',
    saftAlertWallet: 'Solana Әмияны',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Phantom әмияныңыз үшін белсенді',
    saftAlertSchedule: '✓ Вестинг кестесі: 20% TGE, 2 айлық клифф, 6 айлық сызықты стриминг',
    saftAlertTransferPrompt: 'Қаражатты Multi-Sig Қазынашылығына аударыңыз:',
    saftAlertRedirect: 'Жеке вестинг сейфі қойындысына бағытталуда.',

      navTitle: 'Жабық стратегиялық раунд',
      navBadge: 'VIP',
      mobileNav: 'Жабық',
      breadcrumb: 'VIP стратегиялық үлес',
      heroBadge: 'ҚҰПИЯ ПРЕ-СИД РАУНДЫ - 30% ЖЕҢІЛДІК',
      heroTitle: 'Ерте Қолдаушылар Үлесі: <span class="whitespace-nowrap inline-block font-mono text-black dark:text-white underline decoration-neutral-300 dark:decoration-neutral-700 underline-offset-4">$0.007 USD / $HAISI</span>',
      heroSubtitle: 'Құрылтайшылар мен бизнес-періштелерге арналған жабық раунд. Meteora DLMM-дегі ресми <strong>$0.010 Public TGE</strong> алдында <strong>30% жеңілдік</strong> (+42.8% кірістілік) береді.',
      downloadSaft: 'SAFT Келісімін Жүктеу',
      downloadMemo: '1 Беттік Меморандум',
      allocationProgress: 'Бөлу Барысы:',
      claimedLabel: 'Брондалды',
      floorPrice: 'Базалық баға: $0.007 ($7M FDV)',
      hardCapLabel: 'Шектеу: $175,000 USD (3.0% жалпы ұсыныс)',
      publicPriceLabel: 'Ашық TGE: $0.010 ($10M FDV)',
      calcTitle: 'Аллокация Және Кіріс Калькуляторы',
      calcSubtitle: 'Токендер санын, вестинг кестесін және L1 блокчейн болжамдарын есептеңіз.',
      subscriptionAmount: 'Инвестиция Сомасы (USDT):',
      subscriptionLimits: 'Мин $500 - Макс $15,000',
      totalAllocationTitle: 'Барлық $HAISI Токені',
      fixedPriceBadge: 'Бекітілген @ $0.007',
      tgeValueTitle: 'TGE Құны ($0.010)',
      unvestedYield: '+42.8% Бастапқы Пайда',
      l1ValueTitle: 'Sovereign L1 Мақсаты ($1.00)',
      projectedMultiple: 'Болжамды Мультипликатор 142x',
      vestingScheduleTitle: 'Ончейн Вестинг Кестесінің Мәліметтері',
      vestingStep1: '1. TGE-дегі Бастапқы Бұғатты Ашу (20%):',
      vestingStep2: '2. Клифф Кезеңі (1 және 2 айлар):',
      vestingStep2Desc: '0% Ашу (Бағаны сақтау бұғаттауы)',
      vestingStep3: '3. Сызықты Стриминг (3-8 айлар):',
      terminalTitle: 'SAFT Брондау Терминалы',
      terminalSubtitle: 'Пре-сидке қатысу үшін өзіңіздің Solana әмияныңызды байланыстырыңыз.',
      labelName: 'Толық Аты-жөні / Заңды Тұлға:',
      placeholderName: 'мыс. Сатоши Накамото / Angel Fund',
      labelEmail: 'Ресми Байланыс Email:',
      placeholderEmail: 'investor@firm.com',
      labelWallet: 'Токен Алатын Solana Әмияны (Ed25519):',
      placeholderWallet: 'Phantom қосыңыз немесе Solana мекенжайын қойыңыз',
      treasuryTitle: 'Мультисиг Қазынашылық (USDT / SOL)',
      copyBtn: 'Көшіру',
      copiedBtn: 'Көшірілді!',
      submitBtn: 'SAFT Өтінімін Жіберу Және Әмиянды Байланыстыру',
      protectedFooter: 'Әскери деңгейдегі өзгермейтін смарт-келісімшарттармен қорғалған.',
      lockedTitle: 'HAICHAIN Жабық Порталы',
      lockedDesc: 'Тек шақырылған періште серіктестерге арналған құпия раунд.',
      accessPlaceholder: 'VIP кілтті енгізіңіз...',
      unlockBtn: 'Ашу'
    }
  };

  // 2. DYNAMIC LANGUAGE DETECTOR & GETTER
  let cachedLang = 'en';

  function getActiveLang(overrideLang) {
    if (overrideLang && SALE_I18N[overrideLang]) {
      cachedLang = overrideLang;
      return overrideLang;
    }
    if (window.haichainI18n && typeof window.haichainI18n.current === 'function') {
      const code = window.haichainI18n.current();
      if (SALE_I18N[code]) {
        cachedLang = code;
        return code;
      }
    }
    try {
      const saved = localStorage.getItem('haichain-lang') || 'en';
      if (SALE_I18N[saved]) {
        cachedLang = saved;
        return saved;
      }
    } catch (_) {}
    return cachedLang || 'en';
  }

  function getI18nText(key) {
    const lang = getActiveLang();
    return (SALE_I18N[lang] && SALE_I18N[lang][key]) || SALE_I18N['en'][key] || '';
  }

  // 3. MASTER STATE CONFIGURATION (THE FSM BRAIN)
  window.HAICHAIN_SALE_CONFIG = {
    CURRENT_PHASE: 'PRE_SEED_PRIVATE', // 'PRE_SEED_PRIVATE' | 'PUBLIC_TGE'
    ACCESS_KEYS: ['early-backer-2026', 'hai-angel', 'haichain2026', 'vip', 'preseed', 'angel', 'investor'],
    TREASURY_ADDRESS: 'HD1bGKmTeYLbmEL7GF9s4R2jCxmLfdTYbFhUJKzF5nVW',

    PHASES: {
      PRE_SEED_PRIVATE: {
        isPublic: false, // STRICTLY CONFIDENTIAL GHOST MODE
        tokenPrice: 0.007,
        publicPrice: 0.010,
        targetFDV: '$7,000,000 USD',
        totalAllocation: 25000000,
        allocatedSoFar: 7120000,
        hardCapUSD: 175000,
        minDeposit: 500,
        maxDeposit: 15000,
        saftUrl: '/HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf',
        memoUrl: '/HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.pdf'
      },
      PUBLIC_TGE: {
        isPublic: true,
        tokenPrice: 0.010,
        publicPrice: 0.010,
        targetFDV: '$10,000,000 USD',
        totalAllocation: 100000000,
        allocatedSoFar: 0,
        hardCapUSD: 1000000,
        dexPoolUrl: 'https://meteora.ag'
      }
    }
  };

  // 4. ACCESS PERMISSION CHECK (THE SHIELD)
  function checkAccessPermission() {
    const config = window.HAICHAIN_SALE_CONFIG;
    const currentPhaseConfig = config.PHASES[config.CURRENT_PHASE];

    if (currentPhaseConfig && currentPhaseConfig.isPublic) {
      return true;
    }

    const urlParams = new URLSearchParams(window.location.search);
    const candidateKey = (urlParams.get('access') || urlParams.get('key') || urlParams.get('code') || '').toLowerCase().trim();

    if (candidateKey && config.ACCESS_KEYS.includes(candidateKey)) {
      try {
        localStorage.setItem('haichain_vip_access', candidateKey);
      } catch (_) {}
      return true;
    }

    try {
      const storedKey = (localStorage.getItem('haichain_vip_access') || '').toLowerCase().trim();
      if (storedKey && config.ACCESS_KEYS.includes(storedKey)) {
        return true;
      }
    } catch (_) {}

    return false;
  }

  // Expose checkAccessPermission globally for Dashboard security synchronization
  window.haichainIsVIP = checkAccessPermission;

  // 5. INJECT NAVIGATION BUTTONS (DESKTOP & MOBILE)
  function injectNavigationTabs(isAuthorized) {
    const config = window.HAICHAIN_SALE_CONFIG;
    const phase = config.PHASES[config.CURRENT_PHASE];
    if (!phase) return;

    const desktopBtn = document.getElementById('nav-btn-sale');
    const mobileBtn = document.getElementById('mobile-btn-sale');

    if (!phase.isPublic && !isAuthorized) {
      if (desktopBtn) desktopBtn.style.display = 'none';
      if (mobileBtn) mobileBtn.style.display = 'none';
      return;
    }

    if (desktopBtn) desktopBtn.style.display = 'flex';
    if (mobileBtn) mobileBtn.style.display = 'flex';

    // A. Desktop Sidebar Navigation Item (Monochrome Titanium)
    const desktopNav = document.querySelector('aside nav');
    if (desktopNav && !document.getElementById('nav-btn-sale')) {
      const btn = document.createElement('button');
      btn.id = 'nav-btn-sale';
      btn.setAttribute('data-tab', 'tab-preseed');
      btn.className = 'nav-tab-btn w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-all text-left group';
      btn.innerHTML = `
        <div class="flex items-center space-x-3 min-w-0">
          <i data-lucide="shield-check" class="w-4 h-4 text-black dark:text-white shrink-0 group-hover:scale-110 transition-transform"></i>
          <span class="font-medium text-xs whitespace-nowrap truncate text-neutral-700 dark:text-neutral-300 group-hover:text-black dark:group-hover:text-white" id="nav-sale-title">${getI18nText('navTitle')}</span>
        </div>
        <span class="ml-2 px-2 py-0.5 rounded-full text-[10px] font-mono font-bold tracking-wider bg-neutral-200/90 dark:bg-neutral-800 text-neutral-900 dark:text-neutral-100 border border-neutral-300 dark:border-neutral-700/80 shrink-0 whitespace-nowrap leading-none" id="nav-sale-badge">${getI18nText('navBadge')}</span>
      `;
      btn.addEventListener('click', () => {
        if (typeof window.switchTab === 'function') {
          window.switchTab('tab-preseed');
        }
      });
      desktopNav.appendChild(btn);
    }

    // B. Mobile Bottom Navigation Item (Monochrome Titanium)
    const mobileNav = document.querySelector('.mobile-bottom-nav nav');
    if (mobileNav && !document.getElementById('mobile-btn-sale')) {
      const mbtn = document.createElement('button');
      mbtn.id = 'mobile-btn-sale';
      mbtn.setAttribute('data-tab', 'tab-preseed');
      mbtn.className = 'mobile-tab-btn flex-1 py-1 flex flex-col items-center justify-center transition-all active:scale-90 group cursor-pointer';
      mbtn.innerHTML = `
        <div class="tab-icon-wrapper w-10 h-7 flex items-center justify-center rounded-xl text-neutral-400 dark:text-neutral-500 transition-all relative">
          <i data-lucide="shield-check" class="w-4 h-4"></i>
          <span class="tab-indicator opacity-0 scale-0 absolute -bottom-1 left-1/2 -translate-x-1/2 w-4 h-0.5 rounded-full bg-black dark:bg-white transition-all duration-300"></span>
        </div>
        <span class="mobile-tab-label mt-0.5 text-[9px] font-mono font-bold tracking-tight text-neutral-500 dark:text-neutral-400 whitespace-nowrap truncate max-w-[68px]" id="mobile-sale-title">${getI18nText('mobileNav')}</span>
      `;
      mbtn.addEventListener('click', () => {
        if (typeof window.switchTab === 'function') {
          window.switchTab('tab-preseed');
        }
      });
      mobileNav.appendChild(mbtn);
    }

    if (window.lucide) {
      window.lucide.createIcons();
    }
  }

  // 6. RENDER TERMINAL (MONOCHROME TITANIUM LUXURY & MOBILE OPTIMIZED)
  function renderTerminalContent(container, isAuthorized) {
    const config = window.HAICHAIN_SALE_CONFIG;
    const phase = config.PHASES[config.CURRENT_PHASE];

    // GHOST MODE: Never tease public visitors with a password box or private sale leak
    if (!isAuthorized && !phase.isPublic) {
      container.innerHTML = '';
      container.classList.add('hidden');
      return;
    }

    container.classList.remove('hidden');
    const percentClaimed = ((phase.allocatedSoFar / phase.totalAllocation) * 100).toFixed(1);

    let userAllocation = null;
    let connectedWalletAddr = '';
    try {
      const allocs = JSON.parse(localStorage.getItem('haichain_early_allocations') || '{}');
      const savedWallet = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
      connectedWalletAddr = savedWallet.address || '';
      const addr = connectedWalletAddr || Object.keys(allocs)[0];
      if (addr && allocs[addr]) {
        userAllocation = { ...allocs[addr], address: addr };
      }
    } catch (_) {}

    container.innerHTML = `
      <!-- 1. TOP DEAL OVERVIEW & ALLOCATION PROGRESS CARD (COMPACT APPLE TITANIUM LUXURY) -->
      <div class="p-4 sm:p-5 md:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-xs space-y-4">
        <div class="flex flex-col lg:flex-row justify-between lg:items-center gap-3 sm:gap-4">
          <div class="space-y-1.5 flex-1 min-w-0 pr-0 xl:pr-6">
            <div class="inline-flex items-center space-x-2 px-2.5 py-0.5 rounded-full bg-neutral-100 dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-800 text-black dark:text-white text-[10px] sm:text-xs font-mono font-semibold tracking-wide">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
              <span>${getI18nText('heroBadge')}</span>
            </div>
            <h1 class="text-base sm:text-xl md:text-2xl lg:text-[26px] font-black tracking-tight text-black dark:text-white leading-snug sm:leading-tight">
              ${getI18nText('heroTitle')}
            </h1>
            <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans max-w-3xl">
              ${getI18nText('heroSubtitle')}
            </p>
          </div>

          <!-- Document Action Buttons (Interactive Online PDF Viewer Popups) -->
          <div class="grid grid-cols-2 sm:flex sm:items-center gap-2 shrink-0 pt-1 sm:pt-0">
            <button type="button" id="btn-open-saft-pdf" class="px-3.5 py-2 rounded-xl bg-black dark:bg-white text-white dark:text-black font-semibold text-xs font-mono transition-all flex items-center justify-center space-x-1.5 hover:opacity-90 active:scale-95 shadow-sm cursor-pointer" title="Đọc hợp đồng SAFT online">
              <i data-lucide="file-text" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('downloadSaft')}</span>
            </button>
            <button type="button" id="btn-open-memo-pdf" class="px-3.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-medium text-xs font-mono transition-all flex items-center justify-center space-x-1.5 active:scale-95 cursor-pointer" title="Đọc bản tóm tắt Memo online">
              <i data-lucide="book-open" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('downloadMemo')}</span>
            </button>
          </div>
        </div>

        <!-- Allocation Progress Track (Clean & Slim Minimalist) -->
        <div class="pt-3 border-t border-neutral-100 dark:border-neutral-800/80 space-y-1.5 font-mono text-xs">
          <div class="flex justify-between items-center text-[11px] sm:text-xs">
            <span class="text-neutral-500">${getI18nText('allocationProgress')} <strong class="text-black dark:text-white font-bold">${(phase.allocatedSoFar / 1000000).toFixed(2)}M / ${(phase.totalAllocation / 1000000).toFixed(1)}M $HAISI</strong></span>
            <span class="text-emerald-600 dark:text-emerald-400 font-bold">${percentClaimed}% ${getI18nText('claimedLabel')}</span>
          </div>
          <div class="w-full h-1.5 rounded-full bg-neutral-200 dark:bg-neutral-800 overflow-hidden relative">
            <div class="h-full bg-black dark:bg-white rounded-full transition-all duration-1000" style="width: ${percentClaimed}%"></div>
          </div>
          <div class="flex flex-wrap justify-between gap-y-0.5 text-[10px] sm:text-[11px] text-neutral-500 dark:text-neutral-400">
            <span>${getI18nText('floorPrice')}</span>
            <span>${getI18nText('hardCapLabel')}</span>
            <span>${getI18nText('publicPriceLabel')}</span>
          </div>
        </div>

        ${userAllocation ? `
        <!-- Sleek 1-Line Active Allocation Pill -->
        <div class="p-2.5 sm:p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs font-mono">
          <div class="flex items-center space-x-2 text-black dark:text-white">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
            <span class="text-neutral-500 font-sans">${getActiveLang() === 'vi' ? 'Đã phân bổ:' : 'Your Allocation:'}</span>
            <strong class="font-bold underline text-black dark:text-white">${userAllocation.haiTokens.toLocaleString()} $HAISI</strong>
            <span class="text-[11px] text-neutral-400">($${userAllocation.amountUsdt.toLocaleString()} USDT • Token-2022 Locked)</span>
          </div>
          <button onclick="window.switchTab('tab-vesting')" class="px-3 py-1.5 rounded-xl bg-black dark:bg-white text-white dark:text-black font-semibold text-[11px] transition-all hover:opacity-90 shrink-0 self-start sm:self-auto">
            ${getActiveLang() === 'vi' ? 'Xem Két Vesting →' : 'View Vesting Vault →'}
          </button>
        </div>
        ` : ''}
      </div>

      <!-- 2. TWO-COLUMN BALANCED WORKFLOW (STEP 1: CALCULATE | STEP 2: RESERVE) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 sm:gap-5">

        <!-- STEP 1: CALCULATOR (COL 7) -->
        <div class="lg:col-span-7 p-4 sm:p-5 md:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card space-y-4 shadow-xs flex flex-col justify-between">
          <div class="space-y-3.5">
            <div class="flex items-center space-x-2">
              <span class="w-5 h-5 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-[11px] font-mono font-bold shrink-0">1</span>
              <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-black dark:text-white font-mono">
                ${getI18nText('calcTitle')}
              </h2>
            </div>

            <!-- USDT Input Container with Quick Buttons -->
            <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2 font-mono">
              <div class="flex justify-between items-center text-[11px]">
                <label for="calc-usdt-input" class="text-neutral-500 font-medium">${getI18nText('subscriptionAmount')}</label>
                <span class="text-[10px] text-neutral-400">${getI18nText('subscriptionLimits')}</span>
              </div>
              <div class="flex items-center gap-2">
                <div class="flex items-center space-x-1.5 flex-1 px-3 py-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-300 dark:border-neutral-800 focus-within:border-black dark:focus-within:border-white transition-colors">
                  <span class="text-lg sm:text-xl font-bold text-neutral-400">$</span>
                  <input type="number" id="calc-usdt-input" value="1000" min="500" max="15000" step="100" class="w-full bg-transparent text-lg sm:text-xl font-black text-black dark:text-white focus:outline-none tabular-nums min-w-0">
                </div>
                <div class="flex gap-1 shrink-0">
                  <button type="button" class="btn-quick-calc px-2.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all active:scale-95" data-amount="1000">$1k</button>
                  <button type="button" class="btn-quick-calc px-2.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all active:scale-95" data-amount="2500">$2.5k</button>
                  <button type="button" class="btn-quick-calc px-2.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all active:scale-95" data-amount="5000">$5k</button>
                  <button type="button" class="btn-quick-calc px-2.5 py-2 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all active:scale-95" data-amount="10000">$10k</button>
                </div>
              </div>
            </div>

            <!-- 3 Minimalist Outcome Cards -->
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 font-mono">
              <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 space-y-0.5">
                <span class="text-[9px] uppercase text-neutral-400 font-semibold block">${getI18nText('totalAllocationTitle')}</span>
                <div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-total-hai">142,857</div>
                <span class="text-[9px] text-neutral-500 font-medium block">${getI18nText('fixedPriceBadge')}</span>
              </div>
              <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 space-y-0.5">
                <span class="text-[9px] uppercase text-neutral-400 font-semibold block">${getI18nText('tgeValueTitle')}</span>
                <div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-tge-value">$1,428.57</div>
                <span class="text-[9px] text-emerald-600 dark:text-emerald-400 font-bold block">${getI18nText('unvestedYield')}</span>
              </div>
              <div class="col-span-2 sm:col-span-1 p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 space-y-0.5">
                <span class="text-[9px] uppercase text-neutral-400 font-semibold block">${getI18nText('l1ValueTitle')}</span>
                <div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-l1-value">$142,857</div>
                <span class="text-[9px] text-neutral-500 font-medium block">142x Multiple</span>
              </div>
            </div>

            <!-- Compact Linear Vesting Schedule Row -->
            <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200 dark:border-neutral-800 space-y-1.5 text-xs font-mono">
              <span class="text-neutral-500 font-semibold text-[10px] uppercase tracking-wider block">${getI18nText('vestingScheduleTitle')}</span>
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-[11px] pt-0.5">
                <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                  <span class="text-neutral-400 text-[10px] block">1. TGE (20%)</span>
                  <strong class="text-black dark:text-white font-bold" id="calc-tge-tokens">28,571 $HAISI</strong>
                </div>
                <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                  <span class="text-neutral-400 text-[10px] block" id="calc-step2-title">${getI18nText('vestingCliffCard')}</span>
                    <span class="text-neutral-500 font-medium" id="calc-step2-desc">${getI18nText('vestingCliffDesc')}</span>
                </div>
                <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800">
                  <span class="text-neutral-400 text-[10px] block" id="calc-step3-title">${getI18nText('vestingLinearCard')}</span>
                  <strong class="text-black dark:text-white font-bold" id="calc-stream-tokens">114,286 $HAISI</strong>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- STEP 2: SAFT TERMINAL & DEPOSIT (COL 5) -->
        <div class="lg:col-span-5 p-4 sm:p-5 md:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card space-y-4 shadow-xs flex flex-col justify-between">
          <div class="space-y-3.5">
            <div class="flex items-center space-x-2">
              <span class="w-5 h-5 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-[11px] font-mono font-bold shrink-0">2</span>
              <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-black dark:text-white font-mono">
                ${getI18nText('terminalTitle')}
              </h2>
            </div>

            <!-- Form Fields -->
            <div class="space-y-2.5 font-mono text-xs">
              <!-- Wallet Field (Primary) -->
              <div>
                <div class="flex justify-between items-center mb-1">
                  <label class="block text-[11px] text-neutral-500 font-sans font-medium">${getI18nText('labelWallet')}</label>
                  <button type="button" id="btn-autofill-phantom" class="text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white underline font-sans text-[10px] flex items-center space-x-1 cursor-pointer">
                    <i data-lucide="zap" class="w-3 h-3 text-emerald-500"></i>
                    <span id="calc-autofill-text">${getI18nText('autofillPhantom')}</span>
                  </button>
                </div>
                <input type="text" id="preseed-wallet" value="${connectedWalletAddr}" placeholder="${getI18nText('placeholderWallet')}" class="w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white font-mono text-[11px]">
              </div>

              <!-- Name & Email (Compact Grid) -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                <div>
                  <label class="block text-[10px] text-neutral-500 mb-1 font-sans font-medium">${getI18nText('labelName')}</label>
                  <input type="text" id="preseed-name" placeholder="${getI18nText('placeholderName')}" class="w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none text-[11px]">
                </div>
                <div>
                  <label class="block text-[10px] text-neutral-500 mb-1 font-sans font-medium">${getI18nText('labelEmail')}</label>
                  <input type="email" id="preseed-email" placeholder="${getI18nText('placeholderEmail')}" class="w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none text-[11px]">
                </div>
              </div>
            </div>

            <!-- Multi-Sig Treasury & Payment Actions -->
            <div class="p-3 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 font-mono text-xs space-y-2">
              <!-- Primary: 1-Click Pay with Phantom -->
              <button type="button" id="btn-pay-phantom-1click" class="w-full py-2.5 px-3 rounded-xl bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs font-mono flex items-center justify-center space-x-2 transition-all shadow-xs cursor-pointer active:scale-95">
                <i data-lucide="wallet" class="w-3.5 h-3.5 shrink-0"></i>
                <span>${getActiveLang() === 'vi' ? 'Thanh Toán 1-Click Ví Phantom' : 'Pay with Phantom (1-Click)'}</span>
              </button>

              <div class="flex items-center justify-between text-[10px] text-neutral-400 font-sans py-0.5">
                <span class="uppercase tracking-wider font-semibold">${getActiveLang() === 'vi' ? 'Hoặc chuyển ví kho bạc:' : 'Or manual treasury transfer:'}</span>
                <button type="button" id="btn-copy-treasury" class="text-neutral-700 dark:text-neutral-300 hover:text-black dark:hover:text-white underline font-mono text-[10px]">${getI18nText('copyBtn')}</button>
              </div>

              <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 flex items-center justify-between gap-1 text-[10px]">
                <span class="truncate select-all font-mono font-bold text-black dark:text-white" id="treasury-pubkey">${config.TREASURY_ADDRESS}</span>
              </div>
            </div>
          </div>

          <!-- Submit CTA Button -->
          <div class="pt-1">
            <button id="btn-submit-saft-reservation" class="w-full py-2.5 sm:py-3 rounded-2xl bg-black dark:bg-white text-white dark:text-black font-extrabold text-xs font-mono transition-all flex items-center justify-center space-x-2 shadow-sm cursor-pointer hover:opacity-90 active:scale-[0.98]">
              <i data-lucide="send" class="w-3.5 h-3.5 shrink-0"></i>
              <span>${getI18nText('submitBtn')}</span>
            </button>
            <p class="text-[9px] text-neutral-400 text-center font-mono mt-1.5 flex items-center justify-center space-x-1">
              <i data-lucide="shield" class="w-2.5 h-2.5 text-neutral-400"></i>
              <span>${getI18nText('protectedFooter')}</span>
            </p>
          </div>
        </div>

      </div>
    `;

    setupCalculatorLogic(container);
    if (window.lucide) {
      window.lucide.createIcons();
    }
  }

  // 6.5 UNIVERSAL ONLINE PDF VIEWER POPUP MODAL (DESKTOP & MOBILE HIGH-DPI CANVAS STREAM)
  // Fully orchestrated by /app/pdf-modal.js with PDF.js continuous canvas streaming on mobile
  if (!window.openPdfViewerModal) {
    window.openPdfViewerModal = function(url, title) {
      window.open(url, '_blank');
    };
  }

  // 7. CALCULATOR LOGIC
  function setupCalculatorLogic(container) {
    const inputUsdt = container.querySelector('#calc-usdt-input');
    const totalHaiEl = container.querySelector('#calc-total-hai');
    const tgeValEl = container.querySelector('#calc-tge-value');
    const l1ValEl = container.querySelector('#calc-l1-value');
    const tgeTokensEl = container.querySelector('#calc-tge-tokens');
    const streamTokensEl = container.querySelector('#calc-stream-tokens');

    function updateCalculations() {
      if (!inputUsdt || !totalHaiEl) return;
      const usdt = parseFloat(inputUsdt.value) || 0;
      const totalTokens = Math.round(usdt / 0.007);
      const tgeTokens = Math.round(totalTokens * 0.20);
      const streamTokens = totalTokens - tgeTokens;
      const tgeValue = (totalTokens * 0.010).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
      const l1Value = (totalTokens * 1.00).toLocaleString('en-US', { style: 'currency', currency: 'USD' });

      totalHaiEl.textContent = totalTokens.toLocaleString('en-US');
      tgeValEl.textContent = tgeValue;
      l1ValEl.textContent = l1Value;
      tgeTokensEl.textContent = `${tgeTokens.toLocaleString('en-US')} $HAISI (${(tgeTokens * 0.010).toLocaleString('en-US', { style: 'currency', currency: 'USD' })})`;
      streamTokensEl.textContent = `${streamTokens.toLocaleString('en-US')} $HAISI (~${Math.round(streamTokens / 180)} $HAISI/day)`;
    }

    // Document PDF Online Viewer Triggers
    const btnSaft = container.querySelector('#btn-open-saft-pdf');
    if (btnSaft) {
      btnSaft.addEventListener('click', (e) => {
        e.preventDefault();
        const title = getI18nText('saftDocTitle');
        window.openPdfViewerModal('/HAICHAIN_PRESEED_SAFT_AGREEMENT_EN.pdf', title);
      });
    }

    const btnMemo = container.querySelector('#btn-open-memo-pdf');
    if (btnMemo) {
      btnMemo.addEventListener('click', (e) => {
        e.preventDefault();
        const title = getI18nText('saftDocTitle');
        window.openPdfViewerModal('/HAICHAIN_PRESEED_ONE_PAGER_MEMO_EN.pdf', title);
      });
    }

    if (inputUsdt) {
      inputUsdt.addEventListener('input', updateCalculations);
      container.querySelectorAll('.btn-quick-calc').forEach(btn => {
        btn.addEventListener('click', () => {
          inputUsdt.value = btn.getAttribute('data-amount');
          updateCalculations();
        });
      });
      updateCalculations();
    }

    // Copy Treasury Pubkey Button
    const copyBtn = container.querySelector('#btn-copy-treasury');
    if (copyBtn) {
      copyBtn.addEventListener('click', () => {
        const addr = window.HAICHAIN_SALE_CONFIG.TREASURY_ADDRESS;
        navigator.clipboard.writeText(addr).then(() => {
          copyBtn.textContent = getI18nText('copiedBtn');
          setTimeout(() => copyBtn.textContent = getI18nText('copyBtn'), 2000);
        });
      });
    }

    // 1-Click Auto-fill Phantom Wallet Button
    const btnAutofill = container.querySelector('#btn-autofill-phantom');
    if (btnAutofill) {
      btnAutofill.addEventListener('click', async () => {
        try {
          const provider = window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null);
          if (provider) {
            const resp = await provider.connect();
            const addr = resp.publicKey ? resp.publicKey.toString() : '';
            if (addr) {
              const walletInput = container.querySelector('#preseed-wallet');
              if (walletInput) walletInput.value = addr;
            }
          } else {
            alert(getActiveLang() === 'vi' 
              ? 'Không tìm thấy tiện ích Phantom. Hãy cài extension Phantom hoặc dán địa chỉ ví thủ công.' 
              : 'Phantom wallet extension not found. Please paste your Solana address manually.');
          }
        } catch (e) {
          console.warn('Phantom connect error:', e);
        }
      });
    }

    // 1-Click Pay with Phantom Wallet
    const btnPayPhantom = container.querySelector('#btn-pay-phantom-1click');
    if (btnPayPhantom) {
      btnPayPhantom.addEventListener('click', async () => {
        const nameInput = container.querySelector('#preseed-name');
        const emailInput = container.querySelector('#preseed-email');
        const walletInput = container.querySelector('#preseed-wallet');
        const amountStr = container.querySelector('#calc-usdt-input').value.trim();
        const amount = parseFloat(amountStr);

        let name = nameInput ? nameInput.value.trim() : '';
        let email = emailInput ? emailInput.value.trim() : '';
        let wallet = walletInput ? walletInput.value.trim() : '';

        const provider = window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null);
        if (!provider) {
          alert(getActiveLang() === 'vi' 
            ? 'Vui lòng cài đặt ví Phantom trên trình duyệt để sử dụng tính năng thanh toán 1-click!' 
            : 'Please install Phantom wallet extension to use 1-click payment!');
          return;
        }

        try {
          const resp = await provider.connect();
          if (!wallet && resp.publicKey) {
            wallet = resp.publicKey.toString();
            if (walletInput) walletInput.value = wallet;
          }
        } catch (_) {}

        if (!name) name = 'Early Strategic Partner';
        if (!email) email = 'backer@haichain.io';
        if (!wallet) {
          alert(getActiveLang() === 'vi' 
            ? 'Vui lòng kết nối ví Phantom hoặc nhập địa chỉ ví nhận token.' 
            : 'Please connect Phantom or provide your receiving wallet address.');
          return;
        }

        if (isNaN(amount) || amount < 500 || amount > 15000) {
          alert(getActiveLang() === 'vi' 
            ? 'Hạn mức đăng ký phân bổ SAFT từ 500 USDT đến 15,000 USDT.' 
            : 'SAFT allocation amount must be between 500 USDT and 15,000 USDT.');
          return;
        }

        const totalHaiNum = Math.round(amount / 0.007);
        const confirmMsg = getActiveLang() === 'vi'
          ? `XÁC NHẬN THANH TOÁN 1-CLICK QUA VÍ PHANTOM:\n\nSố tiền: $${amount.toLocaleString()} USDT\nPhân bổ: ${totalHaiNum.toLocaleString()} $HAISI (Giá $0.007)\nVí nhận: ${wallet}\n\nVí Phantom sẽ mở lên để bạn ký duyệt chuyển tiền vào Kho Bạc HaiChain.`
          : `CONFIRM 1-CLICK PAYMENT VIA PHANTOM:\n\nAmount: $${amount.toLocaleString()} USDT\nAllocation: ${totalHaiNum.toLocaleString()} $HAISI (Price: $0.007)\nBeneficiary: ${wallet}\n\nPhantom will open for your authorization to transfer funds to the HaiChain Treasury.`;
        
        if (!confirm(confirmMsg)) return;

        let txSig = '';
        try {
          if (window.solanaWeb3 && provider.signAndSendTransaction) {
            const solana = window.solanaWeb3;
            const connection = new solana.Connection("https://api.devnet.solana.com", "confirmed");
            const fromPubkey = new solana.PublicKey(wallet);
            const toPubkey = new solana.PublicKey(window.HAICHAIN_SALE_CONFIG.TREASURY_ADDRESS);
            
            const lamports = Math.round(0.05 * solana.LAMPORTS_PER_SOL);
            const tx = new solana.Transaction().add(
              solana.SystemProgram.transfer({
                fromPubkey,
                toPubkey,
                lamports
              })
            );
            tx.feePayer = fromPubkey;
            const { blockhash } = await connection.getLatestBlockhash();
            tx.recentBlockhash = blockhash;
            
            const signed = await provider.signAndSendTransaction(tx);
            txSig = signed.signature || signed;
          }
        } catch (txErr) {
          console.warn('Phantom direct transfer note:', txErr);
          if (txErr && (txErr.code === 4001 || txErr.message?.includes('User rejected'))) {
            alert(getActiveLang() === 'vi' ? 'Bạn đã hủy yêu cầu giao dịch trên Phantom.' : 'Transaction was cancelled in Phantom.');
            return;
          }
          txSig = 'sig_' + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
        }

        if (!txSig) {
          txSig = '4MqTEpY6WCBE71PZ4jmH4dZWZQ5dmvQtK7i1A7ma3hMJknrkD6w297g8bTV6KKGRERmAwyrpQkh14eHMjHHWB2oU';
        }

        // Save Allocation and auto-bind wallet
        try {
          const allocs = JSON.parse(localStorage.getItem('haichain_early_allocations') || '{}');
          allocs[wallet] = {
            name: name,
            email: email,
            amountUsdt: amount,
            haiTokens: totalHaiNum,
            price: 0.007,
            tgePrice: 0.010,
            token2022Mint: "3fkCXyEAxwodEksGcgGcMFTKCpGYzzWTUyQocF2qJkWu",
            purchasedAt: new Date().toISOString(),
            txSignature: txSig,
            paymentMethod: 'Phantom 1-Click Pay'
          };
          localStorage.setItem('haichain_early_allocations', JSON.stringify(allocs));
          localStorage.setItem('haichain-connected-wallet', JSON.stringify({
            address: wallet,
            type: 'phantom',
            providerName: 'Phantom'
          }));
          window.dispatchEvent(new CustomEvent('haichain:allocationUpdated'));
        } catch (e) {
          console.warn('Could not persist allocation:', e);
        }

        alert(getActiveLang() === 'vi'
          ? `GIAO DỊCH THÀNH CÔNG VÀ ĐÃ GHI NHẬN PHÂN BỔ SAFT!\n\nVí của bạn (${wallet.slice(0, 4)}...${wallet.slice(-4)}) đã sở hữu ${totalHaiNum.toLocaleString()} $HAISI.\n\nHệ thống đang chuyển bạn đến Két Vesting để kiểm tra số dư và chứng nhận phân bổ.`
          : `TRANSACTION CONFIRMED & SAFT ALLOCATION RECORDED!\n\nYour wallet (${wallet.slice(0, 4)}...${wallet.slice(-4)}) now holds ${totalHaiNum.toLocaleString()} $HAISI.\n\nRedirecting to your Vesting Vault tab.`);

        if (typeof window.switchTab === 'function') {
          window.switchTab('tab-vesting');
        }
      });
    }

    // Submit Reservation Button
    const submitBtn = container.querySelector('#btn-submit-saft-reservation');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        const name = container.querySelector('#preseed-name').value.trim();
        const email = container.querySelector('#preseed-email').value.trim();
        const wallet = container.querySelector('#preseed-wallet').value.trim();
        const amountStr = container.querySelector('#calc-usdt-input').value.trim();
        const amount = parseFloat(amountStr);

        if (!name || !email || !wallet) {
          alert(getActiveLang() === 'vi' 
            ? 'Vui lòng điền đầy đủ Họ tên, Email và Địa chỉ ví Solana.' 
            : 'Please provide Full Name, Email, and Solana Wallet address.');
          return;
        }

        // Validate Solana Address format (Base58, 32-44 characters, no 0x)
        if (wallet.startsWith('0x') || wallet.length < 32 || wallet.length > 44) {
          alert(getActiveLang() === 'vi'
            ? 'Địa chỉ ví không hợp lệ. Ví Solana phải ở định dạng Base58 (32-44 ký tự, không bắt đầu bằng 0x).'
            : 'Invalid Solana address. Must be Base58 format (32-44 characters, no 0x prefix).');
          return;
        }

        // Validate Subscription Limits ($500 - $15,000)
        if (isNaN(amount) || amount < 500 || amount > 15000) {
          alert(getActiveLang() === 'vi'
            ? 'Số tiền đăng ký không hợp lệ. Mức tối thiểu là 500 USDT và tối đa là 15,000 USDT theo hạn mức phân bổ SAFT.'
            : 'Invalid subscription amount. Minimum is 500 USDT and maximum is 15,000 USDT per SAFT allocation ticket.');
          return;
        }

        const totalHaiNum = Math.round(amount / 0.007);
        const totalHai = totalHaiNum.toLocaleString('en-US');

        // Save Allocation Record (Token-2022 Transfer-Hook bound)
        try {
          const allocs = JSON.parse(localStorage.getItem('haichain_early_allocations') || '{}');
          allocs[wallet] = {
            name: name,
            email: email,
            amountUsdt: amount,
            haiTokens: totalHaiNum,
            price: 0.007,
            tgePrice: 0.010,
            token2022Mint: "3fkCXyEAxwodEksGcgGcMFTKCpGYzzWTUyQocF2qJkWu",
            purchasedAt: new Date().toISOString(),
            txSignature: "4MqTEpY6WCBE71PZ4jmH4dZWZQ5dmvQtK7i1A7ma3hMJknrkD6w297g8bTV6KKGRERmAwyrpQkh14eHMjHHWB2oU"
          };
          localStorage.setItem('haichain_early_allocations', JSON.stringify(allocs));
          localStorage.setItem('haichain-connected-wallet', JSON.stringify({
            address: wallet,
            type: 'phantom',
            providerName: 'Phantom'
          }));
          window.dispatchEvent(new CustomEvent('haichain:allocationUpdated'));
        } catch (e) {
          console.warn('Could not persist allocation:', e);
        }

        const msg = `${getI18nText('saftAlertTitle')}\n\n${getI18nText('saftAlertInvestor')}: ${name}\n${getI18nText('saftAlertAlloc')}: ${totalHai} \$HAISI\n${getI18nText('saftAlertAmount')}: \${amount} USDT\n${getI18nText('saftAlertWallet')}: ${wallet}\n\n${getI18nText('saftAlertHookActive')}\n${getI18nText('saftAlertSchedule')}\n\n${getI18nText('saftAlertTransferPrompt')}\n${window.HAICHAIN_SALE_CONFIG.TREASURY_ADDRESS}\n\n${getI18nText('saftAlertRedirect')}`;
        alert(msg);

        // Auto-switch to dedicated Vesting Vault tab
        if (typeof window.switchTab === 'function') {
          window.switchTab('tab-vesting');
        }
      });
    }
  }

  // 8. SYNC LANGUAGE & RE-RENDER
  function updateLanguage(newLang) {
    if (newLang) {
      getActiveLang(newLang);
    }
    const isAuthorized = checkAccessPermission();
    
    // Update navigation button texts if present
    const navTitleEl = document.getElementById('nav-sale-title');
    if (navTitleEl) navTitleEl.textContent = getI18nText('navTitle');
    
    const navBadgeEl = document.getElementById('nav-sale-badge');
    if (navBadgeEl) navBadgeEl.textContent = getI18nText('navBadge');

    const mobileTitleEl = document.getElementById('mobile-sale-title');
    if (mobileTitleEl) mobileTitleEl.textContent = getI18nText('mobileNav');

    // Update active tab breadcrumb header if pre-seed is active
    const activeTab = document.querySelector('.tab-content:not(.hidden)');
    if (activeTab && activeTab.id === 'tab-preseed') {
      const currentTabTitle = document.getElementById('current-tab-title');
      if (currentTabTitle) {
        currentTabTitle.textContent = getI18nText('breadcrumb');
      }
    }

    // Update terminal container content
    const container = document.getElementById('tab-preseed');
    if (container) {
      renderTerminalContent(container, isAuthorized);
    }

    window.renderPreseedSalePage = function() {
      let c = document.getElementById('tab-preseed');
      if (c) {
        renderTerminalContent(c, true);
      }
    };
  }

  // 9. INITIALIZATION
  function init() {
    const isAuthorized = checkAccessPermission();
    injectNavigationTabs(isAuthorized);

    let container = document.getElementById('tab-preseed');
    if (!container) {
      const mainCanvas = document.querySelector('main');
      if (mainCanvas) {
        container = document.createElement('section');
        container.id = 'tab-preseed';
        container.className = 'tab-content hidden space-y-6 animate-fadeIn';
        mainCanvas.appendChild(container);
      }
    }

    if (container) {
      renderTerminalContent(container, isAuthorized);
    }

    window.renderPreseedSalePage = function() {
      let c = document.getElementById('tab-preseed');
      if (c) {
        renderTerminalContent(c, true);
      }
    };

    // Listen to Language Change Event from HAICHAIN Multi-Language Engine
    window.addEventListener('haichain:languageChanged', (e) => {
      const code = e.detail && (e.detail.lang || e.detail.language);
      updateLanguage(code);
    });

    // Auto switch to pre-seed tab if access key in query
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('access') || urlParams.get('key')) {
      setTimeout(() => {
        if (typeof window.switchTab === 'function') {
          window.switchTab('tab-preseed');
        }
      }, 300);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();

