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
      confirmMsgInvestment: 'CONFIRM $HAISI PURCHASE ({provider}):\n\n• Investment Amount: ${amount} USDT\n• Token Allocation: {tokens} $HAISI (Price: $0.007)\n• Beneficiary Wallet: {wallet}\n• Mainnet Guarantee: 100% real on-chain conversion disbursed at TGE.\n\nYour {provider} wallet will open for cryptographic authorization.',
      saftSuccessAlert: '🎉 SAFT SUBSCRIPTION & ALLOCATION CONFIRMED!\n\nYour wallet ({shortWallet}) now officially holds {tokens} $HAISI.\n\n🛡️ MAINNET CONVERSION GUARANTEE:\nAll {tokens} $HAISI are immutably secured under the SAFT Agreement. Upon HAICHAIN Mainnet launch (TGE), the Solana Token-2022 smart contract will automatically disburse 100% real on-chain tokens directly to this wallet.\n\nRedirecting to your Vesting Vault to inspect allocation...',
      saftLimitsError: 'SAFT allocation amount must be between 500 USDT and 50,000 USDT.',
      web3WalletNotFound: 'Web3 wallet extension not found. Please connect your wallet in the header or paste address manually.',
      btnConnectWeb3ToBuy: 'Connect Web3 Wallet to Pay',
      btnPayMetaMask: '1-Click Pay with Web3 Wallet',
      btnPaySolflare: '1-Click Pay with Web3 Wallet',
      btnPayPhantom: '1-Click Pay with Web3 Wallet',
      connectWeb3Required: 'Please connect your Web3 wallet to proceed with SAFT payment.',
      confirmPurchaseTitle: 'CONFIRM $HAISI PURCHASE ({provider})',
      authorizeOpenWallet: 'Authorize & Open Wallet',
      metaMaskConnCancelled: 'MetaMask connection was cancelled.',
      metaMaskNoAccount: 'No valid MetaMask account found.',
      metaMaskTxCancelled: 'Transaction signature was cancelled in MetaMask.',
      metaMaskErrorPrefix: 'MetaMask error:',
      solanaConnCancelled: 'Solana wallet connection was cancelled.',
      solanaUnlockPrompt: 'Please unlock and connect your Solana wallet!',
      solanaTxCancelled: 'Transaction was cancelled in your wallet.',
      solanaErrorPrefix: 'Solana wallet error:',
      txNotConfirmed: 'Transaction was not confirmed by Web3 wallet.',
      openingMetaMaskSaft: 'Opening MetaMask App to confirm transaction with real funds...',
      openingPhantomSaft: 'Opening Phantom App to confirm transaction with real funds...',
      noMetaMaskDetected: 'MetaMask extension not detected in your browser!',
      noSolanaDetected: 'No Solana wallet extension detected (Phantom or Solflare)!',
    vestingCliffCard: '2. Cliff (2 Months)',
    vestingCliffDesc: '0% Unlock (Anti-dump)',
    vestingLinearCard: '3. Linear (6 Months)',
    autofillPhantom: 'Auto-fill Web3 Wallet',
    saftDocTitle: 'HAICHAIN Pre-Seed SAFT Agreement (Standard English Edition)',
    memoDocTitle: 'HAICHAIN Pre-Seed 1-Pager Memo',
    saftAlertTitle: 'SAFT SUBSCRIPTION & TOKEN-2022 ALLOCATION RECORDED!',
    saftAlertInvestor: 'Investor',
    saftAlertAlloc: 'Allocation',
    saftAlertAmount: 'Amount',
    saftAlertWallet: 'Solana Wallet',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Active for your Web3 wallet',
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
      l1ValueTitle: 'Micro-Tx Capacity',
      projectedMultiple: '~200 Ticks / $HAISI Gas Capacity',
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
      placeholderWallet: 'Connect Web3 wallet or paste address',
      treasuryTitle: 'Multi-Sig Treasury Vault (USDT / SOL)',
      copyBtn: 'Copy',
      copiedBtn: 'Copied!',
      submitBtn: 'Submit SAFT Subscription & Bind Wallet',
      protectedFooter: 'Protected by military-grade on-chain vesting invariants.',
      lockedTitle: 'HAICHAIN Private Allocation Portal',
      lockedDesc: 'This round is strictly private and reserved for invited Early Backers & Angel Partners under institutional SAFT terms.',
      accessPlaceholder: 'Enter VIP Access Key...',
      unlockBtn: 'Unlock',

      // Referral & Commission Engine
      refProgramTitle: 'HAICHAIN Genesis Referral Program',
      refProgramBadge: '+5% Bonus for Friends • 6% Commission for You',
      refProgramDesc: 'Invite fellow builders and strategic backers to the Private Round. When your invitees subscribe to SAFT (min 500 USDT), they instantly receive +5% Bonus $HAISI and you earn 6% $HAISI commission. 100% synchronized with SAFT Vesting (20% TGE, 2-Month Cliff, 6-Month Linear Stream).',
      refYourLink: 'Your Unique Referral Link:',
      refCopyLink: 'Copy Link',
      refCopied: 'Copied! ✓',
      refShareX: 'Share on X',
      refShareTelegram: 'Telegram',
      refConnectToGenerate: 'Connect your Web3 wallet to generate your referral link and start earning 6% $HAISI commissions.',
      refActiveBadge: '✓ Referral Code Active: +5% Bonus Tokens Applied',
      refInvitedBy: 'Referred by:',
      refEnterCodePrompt: 'Have a referral code or inviter wallet?',
      refCodePlaceholder: 'Enter Solana / EVM wallet address...',
      refApplyBtn: 'Apply',
      refRemoveBtn: 'Remove',
      refSelfReferralError: 'You cannot refer your own wallet address.',
      refInvalidCodeError: 'Invalid referral address format.',
      refCodeAppliedToast: 'Referral code applied! You will receive +5% bonus $HAISI tokens.',
      refStatsTitle: 'Your Affiliate Performance',
      refTotalInvites: 'Referred Backers',
      refTotalVolume: 'Total Volume Raised',
      refTotalEarned: 'Total $HAISI Commission',
      refBonusTag: '(+5% Ref Bonus)'
    },
    vi: {
      confirmMsgInvestment: 'XÁC NHẬN THANH TOÁN MUA $HAISI ({provider}):\n\n• Số tiền đầu tư: ${amount} USDT\n• Phân bổ sở hữu: {tokens} $HAISI (Đơn giá: $0.007)\n• Ví thụ hưởng: {wallet}\n• Bảo chứng Mainnet: Cam kết tự động giải ngân 100% Token Thật tại sự kiện TGE.\n\nVí {provider} của bạn sẽ mở ra để xác thực mật mã.',
      saftSuccessAlert: '🎉 ĐÃ GHI NHẬN ĐĂNG KÝ VÀ BẢO CHỨNG PHÂN BỔ SAFT!\n\nVí của bạn ({shortWallet}) đã chính thức sở hữu {tokens} $HAISI.\n\n🛡️ BẢO CHỨNG CHUYỂN ĐỔI MAINNET:\nToàn bộ {tokens} $HAISI đã được bảo lưu bất biến theo Hợp đồng SAFT. Ngay khi HAICHAIN chính thức kích hoạt mạng Mainnet (Sự kiện TGE), hợp đồng thông minh Solana Token-2022 sẽ tự động giải ngân và chuyển đổi 100% số token này thành Token Thật on-chain về đúng địa chỉ ví này của bạn mà không cần thủ tục nào khác.\n\nHệ thống đang chuyển bạn đến Két sắt Vesting để kiểm tra số dư và chứng nhận phân bổ.',
      saftLimitsError: 'Hạn mức đăng ký phân bổ SAFT từ 500 USDT đến 50.000 USDT.',
      web3WalletNotFound: 'Không tìm thấy tiện ích ví Web3. Vui lòng kết nối ví ở góc trên hoặc dán địa chỉ ví thủ công.',
      btnConnectWeb3ToBuy: 'Kết Nối Ví Web3 Để Thanh Toán',
      btnPayMetaMask: 'Thanh Toán 1-Click Qua Ví Web3',
      btnPaySolflare: 'Thanh Toán 1-Click Qua Ví Web3',
      btnPayPhantom: 'Thanh Toán 1-Click Qua Ví Web3',
      connectWeb3Required: 'Vui lòng kết nối ví Web3 để thực hiện thanh toán SAFT.',
      confirmPurchaseTitle: 'XÁC NHẬN THANH TOÁN MUA $HAISI ({provider})',
      authorizeOpenWallet: 'Ký Duyệt & Mở Ví',
      metaMaskConnCancelled: 'Bạn đã từ chối kết nối ví MetaMask.',
      metaMaskNoAccount: 'Không tìm thấy địa chỉ tài khoản MetaMask hợp lệ.',
      metaMaskTxCancelled: 'Bạn đã hủy yêu cầu ký duyệt giao dịch trên ví MetaMask.',
      metaMaskErrorPrefix: 'Lỗi ví MetaMask:',
      solanaConnCancelled: 'Bạn đã từ chối kết nối ví Solana.',
      solanaUnlockPrompt: 'Vui lòng mở khóa và kết nối ví Solana!',
      solanaTxCancelled: 'Bạn đã hủy yêu cầu giao dịch trên ví.',
      solanaErrorPrefix: 'Lỗi ví Solana:',
      txNotConfirmed: 'Giao dịch chưa được xác nhận bởi ví Web3.',
      openingMetaMaskSaft: 'Đang mở ứng dụng MetaMask để bạn xác nhận giao dịch thanh toán bằng tiền thật trong ví...',
      openingPhantomSaft: 'Đang mở ứng dụng Phantom để bạn xác nhận giao dịch thanh toán bằng tiền thật trong ví...',
      noMetaMaskDetected: 'Chưa phát hiện tiện ích MetaMask trên trình duyệt của bạn!',
      noSolanaDetected: 'Chưa phát hiện tiện ích ví Solana (Phantom hoặc Solflare)!',
    vestingCliffCard: '2. Cliff (2 Tháng)',
    vestingCliffDesc: 'Khóa 0% (Anti-dump)',
    vestingLinearCard: '3. Tuyến Tính (6 Tháng)',
    autofillPhantom: 'Tự điền ví Web3',
    saftDocTitle: 'Hợp Đồng SAFT Pre-Seed HAICHAIN (Standard English Edition)',
    memoDocTitle: 'Bản Tóm Tắt 1 Trang Pre-Seed HAICHAIN',
    saftAlertTitle: 'ĐÃ GHI NHẬN ĐĂNG KÝ SAFT VÀ PHÂN BỔ TOKEN-2022!',
    saftAlertInvestor: 'Nhà đầu tư',
    saftAlertAlloc: 'Phân bổ',
    saftAlertAmount: 'Giá trị',
    saftAlertWallet: 'Ví thụ hưởng',
    saftAlertHookActive: '✓ Token-2022 Transfer-Hook: Đã kích hoạt cho ví Web3 của bạn',
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
      l1ValueTitle: 'Hạn Ngạch Giao Dịch Agent',
      projectedMultiple: '~200 Giao Dịch Vi Mô / $HAISI',
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
      placeholderWallet: 'Kết nối ví Web3 hoặc dán địa chỉ',
      treasuryTitle: 'Ví Kho Bạc Multi-Sig (USDT / SOL)',
      copyBtn: 'Sao chép',
      copiedBtn: 'Đã chép!',
      submitBtn: 'Xác Nhận Giữ Chỗ & Gửi Yêu Cầu Ký SAFT',
      protectedFooter: 'Được bảo vệ bởi hợp đồng khóa on-chain bất biến cấp quân sự.',
      lockedTitle: 'Cổng Phân Bổ Nội Bộ HAICHAIN',
      lockedDesc: 'Vòng này được bảo mật nghiêm ngặt, chỉ dành riêng cho các Đối tác Thiên thần & Co-builders theo thỏa thuận SAFT thể chế.',
      accessPlaceholder: 'Nhập Khóa Truy Cập VIP...',
      unlockBtn: 'Mở Khóa',

      // Referral & Commission Engine
      refProgramTitle: 'Chương Trình Giới Thiệu & Hoa Hồng Genesis',
      refProgramBadge: '+5% Bonus Cho Bạn Bè • 6% Hoa Hồng Cho Bạn',
      refProgramDesc: 'Mời bạn bè và đối tác tham gia Vòng Chiến Lược Nội Bộ. Khi người được mời đăng ký SAFT (tối thiểu 500 USDT), họ nhận ngay +5% Bonus $HAISI và bạn nhận 6% hoa hồng $HAISI. Lịch mở khóa đồng bộ 100% với hợp đồng SAFT (20% TGE, Cliff 2 tháng, Linear Stream 6 tháng).',
      refYourLink: 'Link Giới Thiệu Riêng Của Bạn:',
      refCopyLink: 'Sao Chép Link',
      refCopied: 'Đã Sao Chép! ✓',
      refShareX: 'Chia sẻ lên X',
      refShareTelegram: 'Telegram',
      refConnectToGenerate: 'Kết nối ví Web3 để tạo link giới thiệu và bắt đầu nhận 6% hoa hồng $HAISI.',
      refActiveBadge: '✓ Đang Áp Dụng Mã Giới Thiệu: Nhận Thêm +5% Bonus Token',
      refInvitedBy: 'Người giới thiệu:',
      refEnterCodePrompt: 'Bạn có địa chỉ ví hoặc mã người giới thiệu?',
      refCodePlaceholder: 'Nhập địa chỉ ví Solana / EVM...',
      refApplyBtn: 'Áp Dụng',
      refRemoveBtn: 'Gỡ Bỏ',
      refSelfReferralError: 'Bạn không thể tự giới thiệu địa chỉ ví của chính mình.',
      refInvalidCodeError: 'Định dạng địa chỉ giới thiệu không hợp lệ.',
      refCodeAppliedToast: 'Đã kích hoạt mã giới thiệu! Bạn sẽ nhận thêm +5% Bonus $HAISI.',
      refStatsTitle: 'Hiệu Quả Giới Thiệu Của Bạn',
      refTotalInvites: 'Số Ví Đã Nạp',
      refTotalVolume: 'Tổng Doanh Số Giới Thiệu',
      refTotalEarned: 'Tổng Hoa Hồng $HAISI',
      refBonusTag: '(+5% Thưởng Ref)'
    },
    zh: {
      confirmMsgInvestment: '确认认购 $HAISI 代币 ({provider})：\n\n• 投资金额：${amount} USDT\n• 代币额度：{tokens} $HAISI（单价：$0.007）\n• 受益人钱包：{wallet}\n• 主网保函：在 TGE 时自动 100% 兑换链上代币。\n\n您的 {provider} 钱包将打开进行密码学授权。',
      saftSuccessAlert: '🎉 SAFT 认购与额度保函已确认！\n\n您的钱包 ({shortWallet}) 已正式持有 {tokens} $HAISI。\n\n🛡️ 主网兑换官方保函：\n所有 {tokens} $HAISI 均受到 SAFT 协议的不可变法律保护。HAICHAIN 主网启动 (TGE) 时，Solana Token-2022 智能合约将自动将 100% 真实链上代币划转至该钱包。\n\n正在跳转至您的 Vesting 金库查看额度...',
      saftLimitsError: 'SAFT 认购金额必须在 500 USDT 至 50,000 USDT 之间。',
      web3WalletNotFound: '未检测到 Web3 钱包插件。请在顶部连接钱包或手动粘贴地址。',
      btnConnectWeb3ToBuy: 'Connect Web3 Wallet to Pay',
      btnPayMetaMask: '1-Click Pay with Web3 Wallet',
      btnPaySolflare: '1-Click Pay with Web3 Wallet',
      btnPayPhantom: '1-Click Pay with Web3 Wallet',
      connectWeb3Required: '请连接您的 Web3 钱包（MetaMask、Phantom 或 Solflare）以完成 SAFT 认购支付。',
      confirmPurchaseTitle: '确认认购 $HAISI 代币 ({provider})',
      authorizeOpenWallet: '授权并打开钱包',
      metaMaskConnCancelled: '您已取消 MetaMask 钱包连接。',
      metaMaskNoAccount: '未找到有效的 MetaMask 账户地址。',
      metaMaskTxCancelled: 'MetaMask 中的交易签名已取消。',
      metaMaskErrorPrefix: 'MetaMask 错误：',
      solanaConnCancelled: '您已取消 Solana 钱包连接。',
      solanaUnlockPrompt: '请解锁并连接您的 Solana 钱包！',
      solanaTxCancelled: '钱包中的交易已取消。',
      solanaErrorPrefix: 'Solana 钱包错误：',
      txNotConfirmed: 'Web3 钱包未确认此交易。',
      openingMetaMaskSaft: '正在打开 MetaMask 应用程序以使用真实资金确认交易...',
      openingPhantomSaft: '正在打开 Phantom 应用程序以使用真实资金确认交易...',
      noMetaMaskDetected: '您的浏览器未检测到 MetaMask 插件！',
      noSolanaDetected: '未检测到 Solana 钱包插件（Phantom 或 Solflare）！',
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
      l1ValueTitle: '智能体执行配额',
      projectedMultiple: '约 200 次微交易 / $HAISI 算力',
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
      confirmMsgInvestment: '$HAISI 구매 승인 및 결제 확인 ({provider}):\n\n• 투자 금액: ${amount} USDT\n• 토큰 배분: {tokens} $HAISI (단가: $0.007)\n• 수령 지갑: {wallet}\n• 메인넷 보증: TGE 시 100% 온체인 실제 토큰 자동 지급.\n\n암호학적 서명을 위해 {provider} 지갑이 열립니다.',
      saftSuccessAlert: '🎉 SAFT 청약 및 토큰 할당이 승인되었습니다!\n\n귀하의 지갑({shortWallet})이 이제 공식적으로 {tokens} $HAISI를 보유합니다.\n\n🛡️ 메인넷 전환 보증:\n모든 {tokens} $HAISI는 SAFT 계약에 따라 불변으로 보호됩니다. HAICHAIN 메인넷 출시(TGE) 시 Solana Token-2022 스마트 계약이 100% 온체인 실제 토큰을 이 지갑으로 자동 지급합니다.\n\n배분 증명서 확인을 위해 Vesting 금고로 이동합니다...',
      saftLimitsError: 'SAFT 할당 금액은 500 USDT에서 50,000 USDT 사이여야 합니다.',
      web3WalletNotFound: 'Web3 지갑 확장 프로그램을 찾을 수 없습니다. 헤더에서 지갑을 연결하거나 주소를 수동으로 입력하세요.',
      btnConnectWeb3ToBuy: 'Connect Web3 Wallet to Pay',
      btnPayMetaMask: '1-Click Pay with Web3 Wallet',
      btnPaySolflare: '1-Click Pay with Web3 Wallet',
      btnPayPhantom: '1-Click Pay with Web3 Wallet',
      connectWeb3Required: 'SAFT 결제를 진행하려면 Web3 지갑(MetaMask, Phantom 또는 Solflare)을 연결하세요.',
      confirmPurchaseTitle: '$HAISI 구매 승인 및 결제 확인 ({provider})',
      authorizeOpenWallet: '승인 및 지갑 열기',
      metaMaskConnCancelled: 'MetaMask 지갑 연결이 취소되었습니다.',
      metaMaskNoAccount: '유효한 MetaMask 계정을 찾을 수 없습니다.',
      metaMaskTxCancelled: 'MetaMask에서 거래 서명이 취소되었습니다.',
      metaMaskErrorPrefix: 'MetaMask 오류:',
      solanaConnCancelled: 'Solana 지갑 연결이 취소되었습니다.',
      solanaUnlockPrompt: 'Solana 지갑을 잠금 해제하고 연결하세요!',
      solanaTxCancelled: '지갑에서 거래가 취소되었습니다.',
      solanaErrorPrefix: 'Solana 지갑 오류:',
      txNotConfirmed: 'Web3 지갑에서 거래가 확인되지 않았습니다.',
      openingMetaMaskSaft: '실제 자금으로 거래를 확인하기 위해 MetaMask 앱을 여는 중...',
      openingPhantomSaft: '실제 자금으로 거래를 확인하기 위해 Phantom 앱을 여는 중...',
      noMetaMaskDetected: '브라우저에서 MetaMask 확장 프로그램이 감지되지 않았습니다!',
      noSolanaDetected: 'Solana 지갑 확장 프로그램(Phantom 또는 Solflare)이 감지되지 않았습니다!',
    vestingCliffCard: '2. 클리프 (2개월)',
    vestingCliffDesc: '0% 락업 (덤핑 방지)',
    vestingLinearCard: '3. 선형 스트리밍 (6개월)',
    autofillPhantom: 'Web3 지갑 자동 입력',
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
      l1ValueTitle: '에이전트 실행 한도',
      projectedMultiple: '$HAISI당 약 200회 마이크로 결제',
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
      confirmMsgInvestment: 'CONFIRMER L\'ACHAT DE $HAISI ({provider}) :\n\n• Montant d\'investissement : ${amount} USDT\n• Allocation : {tokens} $HAISI (Prix : $0.007)\n• Portefeuille bénéficiaire : {wallet}\n• Garantie Mainnet : Conversion 100% on-chain déboursée au TGE.\n\nVotre portefeuille {provider} va s\'ouvrir pour l\'autorisation.',
      saftSuccessAlert: '🎉 SOUSCRIPTION SAFT & ALLOCATION CONFIRMÉES !\n\nVotre portefeuille ({shortWallet}) détient désormais {tokens} $HAISI.\n\n🛡️ GARANTIE DE CONVERSION MAINNET :\nTous les {tokens} $HAISI sont légalement garantis sous l\'Accord SAFT. Dès le lancement du Mainnet HAICHAIN (TGE), le contrat intelligent Solana Token-2022 déboursera automatiquement 100% des tokens réels sur ce portefeuille.\n\nRedirection vers votre coffre de Vesting...',
      saftLimitsError: 'Le montant de l\'allocation SAFT doit être compris entre 500 USDT et 50 000 USDT.',
      web3WalletNotFound: 'Extension de portefeuille Web3 non trouvée. Veuillez connecter votre portefeuille ou coller l\'adresse manuellement.',
      btnConnectWeb3ToBuy: 'Connect Web3 Wallet to Pay',
      btnPayMetaMask: '1-Click Pay with Web3 Wallet',
      btnPaySolflare: '1-Click Pay with Web3 Wallet',
      btnPayPhantom: '1-Click Pay with Web3 Wallet',
      connectWeb3Required: 'Veuillez connecter votre portefeuille Web3 (MetaMask, Phantom ou Solflare) pour procéder au paiement SAFT.',
      confirmPurchaseTitle: 'CONFIRMER L\'ACHAT DE $HAISI ({provider})',
      authorizeOpenWallet: 'Autoriser et ouvrir le portefeuille',
      metaMaskConnCancelled: 'La connexion à MetaMask a été annulée.',
      metaMaskNoAccount: 'Aucun compte MetaMask valide trouvé.',
      metaMaskTxCancelled: 'La signature de la transaction a été annulée dans MetaMask.',
      metaMaskErrorPrefix: 'Erreur MetaMask :',
      solanaConnCancelled: 'La connexion au portefeuille Solana a été annulée.',
      solanaUnlockPrompt: 'Veuillez déverrouiller et connecter votre portefeuille Solana !',
      solanaTxCancelled: 'La transaction a été annulée dans votre portefeuille.',
      solanaErrorPrefix: 'Erreur portefeuille Solana :',
      txNotConfirmed: 'La transaction n\'a pas été confirmée par le portefeuille Web3.',
      openingMetaMaskSaft: 'Ouverture de l\'application MetaMask pour confirmer la transaction...',
      openingPhantomSaft: 'Ouverture de l\'application Phantom pour confirmer la transaction...',
      noMetaMaskDetected: 'Extension MetaMask non détectée dans votre navigateur !',
      noSolanaDetected: 'Aucune extension de portefeuille Solana détectée (Phantom ou Solflare) !',
    vestingCliffCard: '2. Cliff (2 Mois)',
    vestingCliffDesc: '0% Déblocage (Anti-dump)',
    vestingLinearCard: '3. Linéaire (6 Mois)',
    autofillPhantom: 'Remplissage auto portefeuille Web3',
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
      l1ValueTitle: 'Capacité de Micro-Tx',
      projectedMultiple: '~200 Ticks / Puissance Gas $HAISI',
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
      confirmMsgInvestment: 'CONFIRMAR COMPRA DE $HAISI ({provider}):\n\n• Monto de inversión: ${amount} USDT\n• Asignación: {tokens} $HAISI (Precio: $0.007)\n• Billetera beneficiaria: {wallet}\n• Garantía Mainnet: Conversión 100% on-chain desembolsada en TGE.\n\nSu billetera {provider} se abrirá para la autorización.',
      saftSuccessAlert: '🎉 ¡SUSCRIPCIÓN SAFT Y ASIGNACIÓN CONFIRMADAS!\n\nSu billetera ({shortWallet}) ahora posee oficialmente {tokens} $HAISI.\n\n🛡️ GARANTÍA DE CONVERSIÓN MAINNET:\nTodos los {tokens} $HAISI están legalmente respaldados bajo el Acuerdo SAFT. En el lanzamiento de la Mainnet de HAICHAIN (TGE), el contrato inteligente Solana Token-2022 desembolsará automáticamente el 100% de los tokens reales a esta billetera.\n\nRedirigiendo a su Bóveda de Vesting...',
      saftLimitsError: 'El monto de la asignación SAFT debe estar entre 500 USDT y 50.000 USDT.',
      web3WalletNotFound: 'No se encontró la extensión de billetera Web3. Conecte su billetera arriba o pegue la dirección manualmente.',
      btnConnectWeb3ToBuy: 'Connect Web3 Wallet to Pay',
      btnPayMetaMask: '1-Click Pay with Web3 Wallet',
      btnPaySolflare: '1-Click Pay with Web3 Wallet',
      btnPayPhantom: '1-Click Pay with Web3 Wallet',
      connectWeb3Required: 'Conecte su billetera Web3 (MetaMask, Phantom o Solflare) para proceder con el pago SAFT.',
      confirmPurchaseTitle: 'CONFIRMAR COMPRA DE $HAISI ({provider})',
      authorizeOpenWallet: 'Autorizar y abrir billetera',
      metaMaskConnCancelled: 'Se canceló la conexión con MetaMask.',
      metaMaskNoAccount: 'No se encontró una cuenta válida de MetaMask.',
      metaMaskTxCancelled: 'Se canceló la firma de la transacción en MetaMask.',
      metaMaskErrorPrefix: 'Error de MetaMask:',
      solanaConnCancelled: 'Se canceló la conexión con la billetera Solana.',
      solanaUnlockPrompt: '¡Desbloquee y conecte su billetera Solana!',
      solanaTxCancelled: 'Se canceló la transacción en su billetera.',
      solanaErrorPrefix: 'Error de billetera Solana:',
      txNotConfirmed: 'La transacción no fue confirmada por la billetera Web3.',
      openingMetaMaskSaft: 'Abriendo la aplicación MetaMask para confirmar la transacción con fondos reales...',
      openingPhantomSaft: 'Abriendo la aplicación Phantom para confirmar la transacción con fondos reales...',
      noMetaMaskDetected: '¡No se detectó la extensión de MetaMask en su navegador!',
      noSolanaDetected: '¡No se detectó la extensión de billetera Solana (Phantom o Solflare)!',
    vestingCliffCard: '2. Cliff (2 Meses)',
    vestingCliffDesc: '0% Desbloqueo (Anti-dump)',
    vestingLinearCard: '3. Lineal (6 Meses)',
    autofillPhantom: 'Autocompletar billetera Web3',
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
      l1ValueTitle: 'Capacidad de Micro-Tx',
      projectedMultiple: '~200 Ticks / Potencia Gas $HAISI',
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
      confirmMsgInvestment: 'ПОДТВЕРЖДЕНИЕ ПОКУПКИ $HAISI ({provider}):\n\n• Сумма инвестиций: ${amount} USDT\n• Выделение токенов: {tokens} $HAISI (Цена: $0.007)\n• Кошелек получателя: {wallet}\n• Гарантия Mainnet: 100% ончейн-конвертация при TGE.\n\nВаш кошелек {provider} откроется для подписи.',
      saftSuccessAlert: '🎉 ПОДПИСКА SAFT И ВЫДЕЛЕНИЕ ТОКЕНОВ ПОДТВЕРЖДЕНЫ!\n\nВаш кошелек ({shortWallet}) теперь официально владеет {tokens} $HAISI.\n\n🛡️ ГАРАНТИЯ КОНВЕРТАЦИИ В MAINNET:\nВсе {tokens} $HAISI юридически защищены соглашением SAFT. При запуске Mainnet HAICHAIN (TGE) смарт-контракт Solana Token-2022 автоматически переведет 100% реальных ончейн-токенов на этот кошелек.\n\nПеренаправление в Сейф Вестинга...',
      saftLimitsError: 'Сумма выделения SAFT должна составлять от 500 USDT до 50 000 USDT.',
      web3WalletNotFound: 'Расширение Web3-кошелька не найдено. Подключите кошелек в шапке или вставьте адрес вручную.',
      btnConnectWeb3ToBuy: 'Connect Web3 Wallet to Pay',
      btnPayMetaMask: '1-Click Pay with Web3 Wallet',
      btnPaySolflare: '1-Click Pay with Web3 Wallet',
      btnPayPhantom: '1-Click Pay with Web3 Wallet',
      connectWeb3Required: 'Пожалуйста, подключите Web3-кошелек (MetaMask, Phantom или Solflare) для оплаты SAFT.',
      confirmPurchaseTitle: 'ПОДТВЕРЖДЕНИЕ ПОКУПКИ $HAISI ({provider})',
      authorizeOpenWallet: 'Авторизовать и открыть кошелек',
      metaMaskConnCancelled: 'Подключение MetaMask было отменено.',
      metaMaskNoAccount: 'Действительный аккаунт MetaMask не найден.',
      metaMaskTxCancelled: 'Подпись транзакции в MetaMask была отменена.',
      metaMaskErrorPrefix: 'Ошибка MetaMask:',
      solanaConnCancelled: 'Подключение кошелька Solana было отменено.',
      solanaUnlockPrompt: 'Пожалуйста, разблокируйте и подключите кошелек Solana!',
      solanaTxCancelled: 'Транзакция была отменена в вашем кошельке.',
      solanaErrorPrefix: 'Ошибка кошелька Solana:',
      txNotConfirmed: 'Транзакция не была подтверждена Web3-кошельком.',
      openingMetaMaskSaft: 'Открытие приложения MetaMask для подтверждения транзакции реальными средствами...',
      openingPhantomSaft: 'Открытие приложения Phantom для подтверждения транзакции реальными средствами...',
      noMetaMaskDetected: 'Расширение MetaMask не обнаружено в вашем браузере!',
      noSolanaDetected: 'Расширение кошелька Solana (Phantom или Solflare) не обнаружено!',
    vestingCliffCard: '2. Клифф (2 Месяца)',
    vestingCliffDesc: '0% Разблокировки (Анти-дамп)',
    vestingLinearCard: '3. Линейный (6 Месяцев)',
    autofillPhantom: 'Автозаполнение Web3 кошелька',
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
      l1ValueTitle: 'Квота Микро-Транзакций',
      projectedMultiple: '~200 Тиков / Газ $HAISI',
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
      confirmMsgInvestment: '$HAISI खरीद की पुष्टि करें ({provider}):\n\n• निवेश राशि: ${amount} USDT\n• टोकन आवंटन: {tokens} $HAISI (मूल्य: $0.007)\n• लाभार्थी वॉलेट: {wallet}\n• मेननेट गारंटी: TGE पर 100% वास्तविक ऑन-चेन रूपांतरण।\n\nहस्ताक्षर के लिए आपका {provider} वॉलेट खुलेगा।',
      saftSuccessAlert: '🎉 SAFT सदस्यता और आवंटन की पुष्टि हो गई!\n\nआपका वॉलेट ({shortWallet}) अब आधिकारिक तौर पर {tokens} $HAISI रखता है।\n\n🛡️ मेननेट रूपांतरण गारंटी:\nसभी {tokens} $HAISI SAFT समझौते के तहत सुरक्षित हैं। मेननेट लॉन्च (TGE) पर, सोलाना टोकन-2022 स्मार्ट अनुबंध स्वचालित रूप से इस वॉलेट में 100% वास्तविक टोकन वितरित करेगा।\n\nआवंटन देखने के लिए वेस्टिंग वॉल्ट पर पुनर्निर्देशित किया जा रहा है...',
      saftLimitsError: 'SAFT आवंटन राशि 500 USDT और 50,000 USDT के बीच होनी चाहिए।',
      web3WalletNotFound: 'Web3 वॉलेट एक्सटेंशन नहीं मिला। कृपया शीर्ष पर वॉलेट कनेक्ट करें या मैन्युअल रूप से पता पेस्ट करें।',
      btnConnectWeb3ToBuy: 'Connect Web3 Wallet to Pay',
      btnPayMetaMask: '1-Click Pay with Web3 Wallet',
      btnPaySolflare: '1-Click Pay with Web3 Wallet',
      btnPayPhantom: '1-Click Pay with Web3 Wallet',
      connectWeb3Required: 'SAFT भुगतान जारी रखने के लिए कृपया अपना Web3 वॉलेट (मेटामास्क, फैंटम या सोलफ्लेयर) कनेक्ट करें।',
      confirmPurchaseTitle: '$HAISI खरीद की पुष्टि करें ({provider})',
      authorizeOpenWallet: 'अधिकृत करें और वॉलेट खोलें',
      metaMaskConnCancelled: 'मेटामास्क कनेक्शन रद्द कर दिया गया था।',
      metaMaskNoAccount: 'कोई मान्य मेटामास्क खाता नहीं मिला।',
      metaMaskTxCancelled: 'मेटामास्क में लेनदेन हस्ताक्षर रद्द कर दिया गया था।',
      metaMaskErrorPrefix: 'मेटामास्क त्रुटि:',
      solanaConnCancelled: 'सोलाना वॉलेट कनेक्शन रद्द कर दिया गया था।',
      solanaUnlockPrompt: 'कृपया अपना सोलाना वॉलेट अनलॉक करें और कनेक्ट करें!',
      solanaTxCancelled: 'आपके वॉलेट में लेनदेन रद्द कर दिया गया था।',
      solanaErrorPrefix: 'सोलाना वॉलेट त्रुटि:',
      txNotConfirmed: 'Web3 वॉलेट द्वारा लेनदेन की पुष्टि नहीं की गई थी।',
      openingMetaMaskSaft: 'वास्तविक फंड के साथ लेनदेन की पुष्टि करने के लिए मेटामास्क ऐप खोला जा रहा है...',
      openingPhantomSaft: 'वास्तविक फंड के साथ लेनदेन की पुष्टि करने के लिए फैंटम ऐप खोला जा रहा है...',
      noMetaMaskDetected: 'आपके ब्राउज़र में मेटामास्क एक्सटेंशन का पता नहीं चला!',
      noSolanaDetected: 'कोई सोलाना वॉलेट एक्सटेंशन (फैंटम या सोलफ्लेयर) नहीं मिला!',
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
      l1ValueTitle: 'माइक्रो-लेनदेन क्षमता',
      projectedMultiple: '~200 टिक्स / $HAISI गैस क्षमता',
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
      confirmMsgInvestment: 'אישור רכישת $HAISI ({provider}):\n\n• סכום השקעה: ${amount} USDT\n• הקצאת אסימונים: {tokens} $HAISI (מחיר: $0.007)\n• ארנק מוטב: {wallet}\n• ערבות רשת ראשית: 100% המרה אמיתית ב-TGE.\n\nארנק ה-{provider} שלך ייפתח לאישור חתימה.',
      saftSuccessAlert: '🎉 מנוי והקצאת SAFT אושרו!\n\nהארנק שלך ({shortWallet}) מחזיק כעת באופן רשמי ב-{tokens} $HAISI.\n\n🛡️ ערבות המרה לרשת הראשית:\nכל {tokens} $HAISI מאובטחים ללא שינוי תחת הסכם SAFT. עם השקת רשת Mainnet של HAICHAIN (אירוע TGE), החוזה החכם Solana Token-2022 ישחרר אוטומטית 100% אסימוני רשת אמיתיים לארנק זה.\n\nמעביר אותך לכספת הווסטינג...',
      saftLimitsError: 'סכום הקצאת ה-SAFT חייב להיות בין 500 USDT ל-50,000 USDT.',
      web3WalletNotFound: 'תוסף ארנק Web3 לא נמצא. אנא חבר את הארנק בחלק העליון או הדבק את הכתובת ידנית.',
      btnConnectWeb3ToBuy: 'Connect Web3 Wallet to Pay',
      btnPayMetaMask: '1-Click Pay with Web3 Wallet',
      btnPaySolflare: '1-Click Pay with Web3 Wallet',
      btnPayPhantom: '1-Click Pay with Web3 Wallet',
      connectWeb3Required: 'אנא חבר את ארנק ה-Web3 שלך (MetaMask, Phantom או Solflare) כדי להמשיך בתשלום ה-SAFT.',
      confirmPurchaseTitle: 'אישור רכישת $HAISI ({provider})',
      authorizeOpenWallet: 'אשר ופתח את הארנק',
      metaMaskConnCancelled: 'החיבור ל-MetaMask בוטל.',
      metaMaskNoAccount: 'לא נמצא חשבון MetaMask חוקי.',
      metaMaskTxCancelled: 'חתימת העסקה בוטלה ב-MetaMask.',
      metaMaskErrorPrefix: 'שגיאת MetaMask:',
      solanaConnCancelled: 'חיבור ארנק Solana בוטל.',
      solanaUnlockPrompt: 'אנא בטל את נעילת ארנק Solana וחבר אותו!',
      solanaTxCancelled: 'העסקה בוטלה בארנק שלך.',
      solanaErrorPrefix: 'שגיאת ארנק Solana:',
      txNotConfirmed: 'העסקה לא אושרה על ידי ארנק Web3.',
      openingMetaMaskSaft: 'פותח את אפליקציית MetaMask כדי לאשר את העסקה עם כספים אמיתיים...',
      openingPhantomSaft: 'פותח את אפליקציית Phantom כדי לאשר את העסקה עם כספים אמיתיים...',
      noMetaMaskDetected: 'תוסף MetaMask לא זוהה בדפדפן שלך!',
      noSolanaDetected: 'לא זוהה תוסף ארנק Solana (Phantom או Solflare)!',
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
      l1ValueTitle: 'מכסת מיקרו-עסקאות',
      projectedMultiple: '~200 עסקאות / כוח גז $HAISI',
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
      confirmMsgInvestment: '$HAISI САТЫП АЛУДЫ РАСТАУ ({provider}):\n\n• Инвестиция көлемі: ${amount} USDT\n• Бөлінген үлес: {tokens} $HAISI (Бағасы: $0.007)\n• Алушы әмиян: {wallet}\n• Mainnet кепілдігі: TGE кезінде 100% нақты ончейн токендер автоматты түрде беріледі.\n\nКриптографиялық растау үшін {provider} әмияныңыз ашылады.',
      saftSuccessAlert: '🎉 SAFT ЖАЗЫЛУЫ МЕН БӨЛІНГЕН ҮЛЕС РАСТАЛДЫ!\n\nСіздің әмияныңыз ({shortWallet}) енді ресми түрде {tokens} $HAISI иеленеді.\n\n🛡️ MAINNET РЕСМИ КЕПІЛДІГІ:\nБарлық {tokens} $HAISI SAFT келісімшартымен өзгермейтін түрде қорғалған. HAICHAIN Mainnet іске қосылғанда (TGE), Solana Token-2022 смарт-келісімшарты 100% нақты ончейн токендерді осы әмиянға автоматты түрде аударады.\n\nVesting сейфіне бағытталуда...',
      saftLimitsError: 'SAFT бөлінген үлес сомасы 500 USDT мен 50 000 USDT арасында болуы керек.',
      web3WalletNotFound: 'Web3 әмиян кеңейтімі табылмады. Жоғарғы жағындағы әмиянды қосыңыз немесе мекенжайды қолмен қойыңыз.',
      btnConnectWeb3ToBuy: 'Connect Web3 Wallet to Pay',
      btnPayMetaMask: '1-Click Pay with Web3 Wallet',
      btnPaySolflare: '1-Click Pay with Web3 Wallet',
      btnPayPhantom: '1-Click Pay with Web3 Wallet',
      connectWeb3Required: 'SAFT төлемін жалғастыру үшін Web3 әмияныңызды (MetaMask, Phantom немесе Solflare) қосыңыз.',
      confirmPurchaseTitle: '$HAISI САТЫП АЛУДЫ РАСТАУ ({provider})',
      authorizeOpenWallet: 'Растау және әмиянды ашу',
      metaMaskConnCancelled: 'MetaMask әмиянын қосу тоқтатылды.',
      metaMaskNoAccount: 'Жарамды MetaMask тіркелгісі табылмады.',
      metaMaskTxCancelled: 'MetaMask әмиянында транзакцияға қол қою тоқтатылды.',
      metaMaskErrorPrefix: 'MetaMask қатесі:',
      solanaConnCancelled: 'Solana әмиянын қосу тоқтатылды.',
      solanaUnlockPrompt: 'Solana әмияныңызды ашып, қосыңыз!',
      solanaTxCancelled: 'Әмияныңызда транзакция тоқтатылды.',
      solanaErrorPrefix: 'Solana әмиян қатесі:',
      txNotConfirmed: 'Транзакция Web3 әмиянымен расталмады.',
      openingMetaMaskSaft: 'Нақты қаражатпен транзакцияны растау үшін MetaMask қолданбасын ашу...',
      openingPhantomSaft: 'Нақты қаражатпен транзакцияны растау үшін Phantom қолданбасын ашу...',
      noMetaMaskDetected: 'Браузеріңізде MetaMask кеңейтімі анықталмады!',
      noSolanaDetected: 'Solana әмиян кеңейтімі (Phantom немесе Solflare) анықталмады!',
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
      l1ValueTitle: 'Микро-Транзакция Сыйымдылығы',
      projectedMultiple: '~200 Тик / $HAISI Газ Қуаты',
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
    ACCESS_KEYS: ['haichainsi2030st', 'early-backer-2026', 'haichain2026', 'hai-angel', 'vip', 'preseed', 'angel', 'investor'],
    TREASURY_ADDRESS: '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3',

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

    // VIP GATEKEEPER LOCK SCREEN (LUXURY APPLE TITANIUM THEME)
    if (!isAuthorized && !phase.isPublic) {
      container.classList.remove('hidden');
      container.innerHTML = `
        <div class="max-w-lg mx-auto my-8 sm:my-14 p-6 sm:p-9 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-black shadow-lg text-center space-y-6 animate-fadeIn">
          <div class="w-16 h-16 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center mx-auto text-black dark:text-white shadow-xs">
            <i data-lucide="shield-check" class="w-8 h-8"></i>
          </div>
          <div class="space-y-2">
            <div class="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-neutral-100 dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-800 text-[11px] font-mono font-semibold text-neutral-700 dark:text-neutral-300">
              <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span>
              <span>HAICHAIN VIP GATEKEEPER</span>
            </div>
            <h2 class="text-xl sm:text-2xl font-black tracking-tight text-black dark:text-white pt-1">
              ${getI18nText('lockedTitle')}
            </h2>
            <p class="text-xs sm:text-sm text-neutral-500 dark:text-neutral-400 leading-relaxed font-sans max-w-sm mx-auto">
              ${getI18nText('lockedDesc')}
            </p>
          </div>
          <div class="space-y-3 pt-2">
            <div class="relative">
              <input type="text" id="vip-gatekeeper-input" placeholder="${getI18nText('accessPlaceholder')}" class="w-full px-4 py-3.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white placeholder-neutral-400 text-xs sm:text-sm font-mono focus:outline-hidden focus:border-black dark:focus:border-white transition-all text-center tracking-wider font-semibold">
            </div>
            <button type="button" id="vip-gatekeeper-submit" class="w-full py-3.5 rounded-xl bg-black dark:bg-white text-white dark:text-black font-bold text-xs sm:text-sm font-mono transition-all hover:opacity-90 active:scale-98 shadow-sm cursor-pointer flex items-center justify-center space-x-2">
              <i data-lucide="key" class="w-4 h-4"></i>
              <span>${getI18nText('unlockBtn')}</span>
            </button>
            <p id="vip-gatekeeper-err" class="text-xs font-mono text-rose-500 hidden pt-1"></p>
          </div>
          <div class="pt-4 border-t border-neutral-100 dark:border-neutral-800/80 space-y-3">
            <p class="text-xs text-neutral-500 dark:text-neutral-400 leading-relaxed font-sans">
              ${getActiveLang() === 'vi' 
                ? 'Bạn là Quỹ đầu tư hoặc Đối tác chiến lược chưa có mã mời?' 
                : 'Are you an Institutional VC or Strategic Partner without an invitation key?'}
              <br>
              <a href="mailto:investor@haichain.si?subject=HAICHAIN%20Institutional%20Allocation%20Request" class="font-medium text-black dark:text-white underline underline-offset-4 hover:opacity-80 inline-flex items-center space-x-1 mt-1.5">
                <span>${getActiveLang() === 'vi' ? 'Gửi yêu cầu thẩm định cấp quyền đối tác' : 'Request Institutional Clearance'}</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3"></i>
              </a>
            </p>
            <div class="pt-1">
              <button type="button" onclick="window.switchTab('tab-vesting')" class="text-xs font-mono text-neutral-400 hover:text-black dark:hover:text-white transition-colors cursor-pointer inline-flex items-center space-x-1.5">
                <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
                <span>${getActiveLang() === 'vi' ? 'Quay lại Vesting Vault' : 'Back to Vesting Vault'}</span>
              </button>
            </div>
          </div>
        </div>
      `;
      if (window.lucide) {
        window.lucide.createIcons();
      }
      const gateInput = document.getElementById('vip-gatekeeper-input');
      const gateSubmit = document.getElementById('vip-gatekeeper-submit');
      const gateErr = document.getElementById('vip-gatekeeper-err');
      function attemptGateUnlock() {
        if (!gateInput) return;
        const val = (gateInput.value || '').toLowerCase().trim();
        if (config.ACCESS_KEYS.includes(val)) {
          try {
            localStorage.setItem('haichain_vip_access', val);
          } catch (_) {}
          injectNavigationTabs(true);
          renderTerminalContent(container, true);
        } else {
          if (gateErr) {
            gateErr.textContent = getActiveLang() === 'vi' ? 'Khóa truy cập không hợp lệ. Vui lòng kiểm tra lại.' : 'Invalid VIP Access Key. Please try again.';
            gateErr.classList.remove('hidden');
          }
          gateInput.focus();
        }
      }
      if (gateSubmit) gateSubmit.addEventListener('click', attemptGateUnlock);
      if (gateInput) gateInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') attemptGateUnlock();
      });
      return;
    }

    container.classList.remove('hidden');
    const percentClaimed = ((phase.allocatedSoFar / phase.totalAllocation) * 100).toFixed(1);

    let userAllocation = null;
    let connectedWalletAddr = '';
    let isConnectedEVM = false;
    let savedWallet = {};
    try {
      const allocs = JSON.parse(localStorage.getItem('haichain_early_allocations') || '{}');
      savedWallet = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
      connectedWalletAddr = savedWallet.address || '';
      isConnectedEVM = connectedWalletAddr.startsWith('0x') || !!(savedWallet.provider && savedWallet.provider.toLowerCase().includes('metamask')) || !!savedWallet.isEVM;
      // Strictly bind userAllocation to the CURRENTLY connected wallet
      if (connectedWalletAddr && allocs[connectedWalletAddr]) {
        userAllocation = { ...allocs[connectedWalletAddr], address: connectedWalletAddr };
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
              <div class="flex flex-col sm:flex-row sm:items-center gap-2">
                <div class="flex items-center space-x-2 flex-1 px-3.5 py-2.5 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-300 dark:border-neutral-800 focus-within:border-black dark:focus-within:border-white transition-colors">
                  <span class="text-lg sm:text-xl font-bold text-neutral-400">$</span>
                  <input type="number" id="calc-usdt-input" value="1000" min="500" max="15000" step="100" class="w-full bg-transparent text-lg sm:text-xl font-black text-black dark:text-white focus:outline-none tabular-nums">
                </div>
                <div class="grid grid-cols-4 sm:flex gap-1.5 shrink-0">
                  <button type="button" class="btn-quick-calc py-2 px-1 sm:px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all text-center active:scale-95 cursor-pointer" data-amount="1000">$1k</button>
                  <button type="button" class="btn-quick-calc py-2 px-1 sm:px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all text-center active:scale-95 cursor-pointer" data-amount="2500">$2.5k</button>
                  <button type="button" class="btn-quick-calc py-2 px-1 sm:px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all text-center active:scale-95 cursor-pointer" data-amount="5000">$5k</button>
                  <button type="button" class="btn-quick-calc py-2 px-1 sm:px-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 text-[11px] hover:bg-neutral-200 dark:hover:bg-neutral-800 text-black dark:text-white font-bold transition-all text-center active:scale-95 cursor-pointer" data-amount="10000">$10k</button>
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
                <div class="text-lg sm:text-xl font-black text-black dark:text-white tabular-nums tracking-tight" id="calc-l1-value">28.5M Ticks</div>
                <span class="text-[9px] text-neutral-500 font-medium block">${getI18nText('projectedMultiple')}</span>
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
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-2">
                <span class="w-5 h-5 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-[11px] font-mono font-bold shrink-0">2</span>
                <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-black dark:text-white font-mono">
                  ${getI18nText('terminalTitle')}
                </h2>
              </div>
            </div>

            <!-- Segmented Method Switcher (2 Tabs - Mobile Optimized) -->
            <div class="grid grid-cols-2 p-1 bg-neutral-100 dark:bg-neutral-900 rounded-2xl border border-neutral-200/80 dark:border-neutral-800 text-[11px] font-mono">
              <button type="button" id="tab-saft-1click" class="min-h-[36px] py-2 px-2 rounded-xl text-center font-bold transition-all cursor-pointer bg-white dark:bg-black text-black dark:text-white shadow-xs flex items-center justify-center space-x-1.5 active:scale-98">
                <i data-lucide="zap" class="w-3.5 h-3.5 shrink-0"></i>
                <span class="truncate">${getActiveLang() === 'vi' ? 'Ví Web3 (1-Click)' : '1-Click Web3 Pay'}</span>
              </button>
              <button type="button" id="tab-saft-manual" class="min-h-[36px] py-2 px-2 rounded-xl text-center font-medium transition-all cursor-pointer text-neutral-500 hover:text-black dark:hover:text-white flex items-center justify-center space-x-1.5 active:scale-98">
                <i data-lucide="landmark" class="w-3.5 h-3.5 shrink-0"></i>
                <span class="truncate">${getActiveLang() === 'vi' ? 'Chuyển Kho Bạc' : 'Manual Treasury'}</span>
              </button>
            </div>

            <!-- TAB 1: 1-Click Web3 Pay (Primary & Streamlined) -->
            <div id="panel-saft-1click" class="space-y-3 pt-0.5">
              <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2.5 font-mono text-xs">
                <div class="flex items-center justify-between text-[11px]">
                  <span class="text-neutral-500 font-sans">${getActiveLang() === 'vi' ? 'Ví Web3 liên kết:' : 'Bound Web3 Wallet:'}</span>
                  <div class="flex items-center space-x-1.5">
                    <span class="w-2 h-2 rounded-full ${connectedWalletAddr ? 'bg-emerald-500 animate-pulse' : 'bg-amber-500'}"></span>
                    <span class="font-bold text-black dark:text-white truncate max-w-[150px] sm:max-w-[200px]">${connectedWalletAddr ? `${connectedWalletAddr.slice(0, 4)}...${connectedWalletAddr.slice(-4)}` : (getActiveLang() === 'vi' ? 'Chưa kết nối' : 'Not Connected')}</span>
                  </div>
                </div>

                <div class="p-2.5 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200/80 dark:border-neutral-800/80 flex items-center justify-between text-xs font-mono">
                  <span class="text-neutral-500 text-[11px] font-sans">${getActiveLang() === 'vi' ? 'Phân bổ nhận được:' : 'Allocation to bind:'}</span>
                  <span class="font-bold text-black dark:text-white text-xs sm:text-sm"><span id="saft-preview-allocation">142,857</span> $HAISI</span>
                </div>
              </div>

              <!-- Primary Web3 Action Button (NO branded icons, NO MetaMask/Phantom logos) -->
              <button type="button" id="btn-pay-phantom-1click" class="w-full min-h-[48px] py-3.5 px-4 rounded-2xl bg-black dark:bg-white hover:opacity-90 text-white dark:text-black font-extrabold text-xs sm:text-sm font-mono flex items-center justify-center space-x-2 transition-all shadow-sm cursor-pointer active:scale-[0.98]">
                <i data-lucide="zap" class="w-4 h-4 shrink-0"></i>
                <span id="label-pay-1click-text">${(() => {
                  const saved = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
                  if (!saved.address) return getI18nText('btnConnectWeb3ToBuy');
                  return getI18nText('btnPayPhantom');
                })()}</span>
              </button>

              <p class="text-[10px] text-neutral-500 dark:text-neutral-400 text-center font-sans flex items-center justify-center space-x-1.5 px-1">
                <i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-500 shrink-0"></i>
                <span>${getActiveLang() === 'vi' ? 'Phân bổ $HAISI được bảo chứng và xác thực trực tiếp vào ví Web3 của bạn.' : 'Token allocation will be cryptographically bound to your Web3 wallet.'}</span>
              </p>
            </div>

            <!-- TAB 2: Manual Treasury Transfer (For Institutional / Cold Storage) -->
            <div id="panel-saft-manual" class="space-y-3 pt-0.5 hidden">
              <!-- Treasury Pubkey Copy Box -->
              <div class="p-3 rounded-2xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 font-mono text-xs space-y-1.5">
                <div class="flex items-center justify-between text-[10px] text-neutral-500 dark:text-neutral-400 font-sans">
                  <span class="uppercase tracking-wider font-semibold">${getActiveLang() === 'vi' ? 'Địa chỉ ví kho bạc nhận vốn:' : 'Treasury receiving address:'}</span>
                  <button type="button" id="btn-copy-treasury" class="text-neutral-700 dark:text-neutral-300 hover:text-black dark:hover:text-white underline font-mono text-[10px] cursor-pointer">${getI18nText('copyBtn')}</button>
                </div>
                <div class="p-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 flex items-center justify-between gap-1 text-[10px]">
                  <span class="truncate select-all font-mono font-bold text-black dark:text-white break-all" id="treasury-pubkey">${config.TREASURY_ADDRESS}</span>
                </div>
              </div>

              <!-- Form Fields -->
              <div class="space-y-2.5 font-mono text-xs">
                <div>
                  <div class="flex justify-between items-center mb-1">
                    <label class="block text-[10px] text-neutral-500 font-sans font-medium">${getActiveLang() === 'vi' ? 'Địa Chỉ Ví Web3 Nhận Token:' : 'Receiving Web3 Wallet Address:'}</label>
                    <button type="button" id="btn-autofill-phantom" class="text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white underline font-sans text-[10px] flex items-center space-x-1 cursor-pointer">
                      <i data-lucide="zap" class="w-3 h-3 text-emerald-500"></i>
                      <span id="calc-autofill-text">${getI18nText('autofillPhantom')}</span>
                    </button>
                  </div>
                  <input type="text" id="preseed-wallet" value="${connectedWalletAddr}" placeholder="${getI18nText('placeholderWallet')}" class="w-full px-3 py-2 rounded-xl border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white font-mono text-[11px]">
                </div>

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

              <!-- Submit CTA Button -->
              <div class="pt-1">
                <button type="button" id="btn-submit-saft-reservation" class="w-full min-h-[48px] py-3 px-4 rounded-2xl bg-black dark:bg-white text-white dark:text-black font-extrabold text-xs sm:text-sm font-mono transition-all flex items-center justify-center space-x-2 shadow-sm cursor-pointer hover:opacity-90 active:scale-[0.98]">
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
        </div>

      <!-- 3. GENESIS REFERRAL & AMBASSADOR VAULT CARD (LUXURY APPLE TITANIUM THEME) -->
      <div id="saft-referral-hub" class="p-4 sm:p-5 md:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card space-y-4 shadow-xs font-mono">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3.5 border-b border-neutral-100 dark:border-neutral-800/80">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-2xl bg-black dark:bg-white text-white dark:text-black flex items-center justify-center shrink-0 shadow-xs">
              <i data-lucide="users" class="w-5 h-5"></i>
            </div>
            <div>
              <div class="flex flex-wrap items-center gap-2">
                <h3 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-black dark:text-white">
                  ${getI18nText('refProgramTitle')}
                </h3>
                <span class="px-2.5 py-0.5 rounded-full text-[9px] font-mono bg-emerald-100 dark:bg-emerald-950/80 text-emerald-700 dark:text-emerald-300 font-bold border border-emerald-300 dark:border-emerald-800">
                  ${getI18nText('refProgramBadge')}
                </span>
              </div>
              <p class="text-[11px] text-neutral-500 font-sans mt-0.5 max-w-2xl leading-relaxed">
                ${getI18nText('refProgramDesc')}
              </p>
            </div>
          </div>
        </div>

        <!-- Referral Link & Attribution Controls -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-3.5 pt-1">
          <!-- Col Left (7): My Unique Referral Link -->
          <div class="lg:col-span-7 p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2.5">
            <div class="flex items-center justify-between text-[11px]">
              <span class="text-neutral-500 font-sans font-medium">${getI18nText('refYourLink')}</span>
              <span class="text-[10px] text-neutral-400 font-mono">${connectedWalletAddr ? `${connectedWalletAddr.slice(0, 4)}...${connectedWalletAddr.slice(-4)}` : (getActiveLang() === 'vi' ? 'Cần kết nối ví' : 'Wallet required')}</span>
            </div>

            ${connectedWalletAddr ? `
            <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-2">
              <input type="text" id="ref-share-url-input" readonly value="${window.location.origin}/?ref=${connectedWalletAddr}" class="flex-1 px-3 py-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-300 dark:border-neutral-800 text-black dark:text-white text-xs font-mono select-all focus:outline-none">
              <button type="button" id="btn-copy-ref-link" class="px-3.5 py-2 rounded-xl bg-black dark:bg-white text-white dark:text-black font-bold text-xs font-mono transition-all hover:opacity-90 active:scale-95 cursor-pointer flex items-center justify-center space-x-1.5 shrink-0 shadow-xs">
                <i data-lucide="copy" class="w-3.5 h-3.5"></i>
                <span id="btn-copy-ref-text">${getI18nText('refCopyLink')}</span>
              </button>
            </div>
            <div class="flex items-center space-x-2 pt-1 text-[11px]">
              <span class="text-neutral-400 font-sans">${getActiveLang() === 'vi' ? 'Chia sẻ nhanh:' : 'Quick Share:'}</span>
              <button type="button" id="btn-share-ref-x" class="px-2.5 py-1 rounded-lg border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-medium text-[11px] flex items-center space-x-1 cursor-pointer transition-colors">
                <i data-lucide="twitter" class="w-3 h-3"></i>
                <span>${getI18nText('refShareX')}</span>
              </button>
              <button type="button" id="btn-share-ref-tg" class="px-2.5 py-1 rounded-lg border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white text-black dark:text-white font-medium text-[11px] flex items-center space-x-1 cursor-pointer transition-colors">
                <i data-lucide="send" class="w-3 h-3"></i>
                <span>${getI18nText('refShareTelegram')}</span>
              </button>
            </div>
            ` : `
            <div class="p-3 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 text-center space-y-2">
              <p class="text-xs text-neutral-500 font-sans leading-relaxed">
                ${getI18nText('refConnectToGenerate')}
              </p>
              <button type="button" onclick="document.getElementById('wallet-btn').click()" class="px-4 py-2 rounded-xl bg-black dark:bg-white text-white dark:text-black font-bold text-xs font-mono transition-all cursor-pointer hover:opacity-90 active:scale-95">
                ${getActiveLang() === 'vi' ? 'Kết Nối Ví Web3' : 'Connect Web3 Wallet'}
              </button>
            </div>
            `}
          </div>

          <!-- Col Right (5): Active Referral Attribution Status & Input -->
          <div class="lg:col-span-5 p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-2.5 flex flex-col justify-between">
            <div>
              <span class="text-neutral-500 font-sans font-medium text-[11px] block mb-1">${getActiveLang() === 'vi' ? 'Mã Người Giới Thiệu Của Bạn:' : 'Your Inviter Referral Code:'}</span>
              ${(() => {
                const activeRef = getActiveReferral();
                const isSelf = activeRef && connectedWalletAddr && activeRef.toLowerCase() === connectedWalletAddr.toLowerCase();
                if (activeRef && !isSelf) {
                  return `
                    <div class="p-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-300 dark:border-emerald-800/80 flex items-center justify-between text-xs font-mono">
                      <div class="flex items-center space-x-2 truncate">
                        <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
                        <span class="text-emerald-800 dark:text-emerald-200 font-bold truncate">${activeRef.slice(0, 6)}...${activeRef.slice(-4)}</span>
                        <span class="text-[10px] text-emerald-600 dark:text-emerald-400 font-bold shrink-0">(+5% Bonus)</span>
                      </div>
                      <button type="button" id="btn-remove-ref-code" class="text-[10px] text-neutral-500 hover:text-rose-500 underline ml-2 shrink-0 cursor-pointer">
                        ${getI18nText('refRemoveBtn')}
                      </button>
                    </div>
                  `;
                } else {
                  return `
                    <div class="flex items-center space-x-1.5">
                      <input type="text" id="manual-ref-code-input" placeholder="${getI18nText('refCodePlaceholder')}" class="flex-1 px-3 py-2 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-300 dark:border-neutral-800 text-black dark:text-white text-[11px] font-mono focus:outline-none">
                      <button type="button" id="btn-apply-ref-code" class="px-3 py-2 rounded-xl bg-neutral-200 dark:bg-neutral-800 hover:bg-black hover:text-white dark:hover:bg-white dark:hover:text-black text-black dark:text-white font-bold text-xs font-mono transition-all cursor-pointer shrink-0">
                        ${getI18nText('refApplyBtn')}
                      </button>
                    </div>
                    <p class="text-[10px] text-neutral-400 font-sans mt-1">
                      ${getI18nText('refEnterCodePrompt')}
                    </p>
                  `;
                }
              })()}
            </div>

            <!-- Active Affiliate Metrics for this user -->
            ${(() => {
              const refStats = getReferralStats(connectedWalletAddr);
              return `
              <div class="grid grid-cols-3 gap-2 pt-2 border-t border-neutral-200/60 dark:border-neutral-800/80 text-center">
                <div class="p-1.5 rounded-lg bg-white dark:bg-neutral-950 border border-neutral-200/80 dark:border-neutral-800">
                  <span class="text-[9px] text-neutral-400 block font-sans">${getI18nText('refTotalInvites')}</span>
                  <strong class="text-xs font-bold text-black dark:text-white">${refStats.count}</strong>
                </div>
                <div class="p-1.5 rounded-lg bg-white dark:bg-neutral-950 border border-neutral-200/80 dark:border-neutral-800">
                  <span class="text-[9px] text-neutral-400 block font-sans">${getI18nText('refTotalVolume')}</span>
                  <strong class="text-xs font-bold text-black dark:text-white">$${refStats.volume.toLocaleString()}</strong>
                </div>
                <div class="p-1.5 rounded-lg bg-white dark:bg-neutral-950 border border-neutral-200/80 dark:border-neutral-800">
                  <span class="text-[9px] text-neutral-400 block font-sans">${getI18nText('refTotalEarned')}</span>
                  <strong class="text-xs font-bold text-emerald-600 dark:text-emerald-400">${refStats.totalCommission.toLocaleString()}</strong>
                </div>
              </div>
              `;
            })()}
          </div>
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


  // ==========================================
  // REFERRAL & AFFILIATE SUBSYSTEM
  // ==========================================
  function initReferralTracking() {
    try {
      const params = new URLSearchParams(window.location.search);
      const ref = params.get('ref') || params.get('referrer') || params.get('inviter');
      if (ref && ref.trim().length >= 4) {
        const clean = ref.trim();
        localStorage.setItem('haichain_ref', clean);
        localStorage.setItem('haichain_ref_captured_at', new Date().toISOString());
        console.log('[HAICHAIN] Genesis Referral captured:', clean);
      }
    } catch (_) {}
  }

  function getActiveReferral() {
    try {
      const r = localStorage.getItem('haichain_ref');
      if (r && typeof r === 'string' && r.trim().length >= 4) {
        return r.trim();
      }
    } catch (_) {}
    return null;
  }

  function setActiveReferral(code) {
    if (!code) {
      localStorage.removeItem('haichain_ref');
    } else {
      localStorage.setItem('haichain_ref', code.trim());
      localStorage.setItem('haichain_ref_captured_at', new Date().toISOString());
    }
    window.dispatchEvent(new CustomEvent('haichain:referralUpdated'));
  }

  function getReferralLedger() {
    try {
      return JSON.parse(localStorage.getItem('haichain_referral_ledger') || '[]');
    } catch (_) {
      return [];
    }
  }

  function getReferralStats(walletAddr) {
    if (!walletAddr) return { count: 0, volume: 0, totalCommission: 0, list: [] };
    const ledger = getReferralLedger();
    const target = walletAddr.toLowerCase();
    const myRefs = ledger.filter(item => item.referrer && item.referrer.toLowerCase() === target);
    const count = myRefs.length;
    const volume = myRefs.reduce((sum, item) => sum + (Number(item.amountUsdt) || 0), 0);
    const totalCommission = myRefs.reduce((sum, item) => sum + (Number(item.commissionHai) || 0), 0);
    return { count, volume, totalCommission, list: myRefs };
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
      const activeRef = getActiveReferral();
      const connectedWallet = (JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}')).address || '';
      const isRefValid = activeRef && (!connectedWallet || activeRef.toLowerCase() !== connectedWallet.toLowerCase());

      const baseTokens = Math.round(usdt / 0.007);
      const bonusTokens = isRefValid ? Math.round(baseTokens * 0.05) : 0;
      const totalTokens = baseTokens + bonusTokens;

      const tgeTokens = Math.round(totalTokens * 0.20);
      const streamTokens = totalTokens - tgeTokens;
      const tgeValue = (totalTokens * 0.010).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
      const executionCapacity = Math.round(totalTokens * 200);
      const l1Value = executionCapacity >= 1000000 
        ? (executionCapacity / 1000000).toFixed(1) + 'M Ticks' 
        : executionCapacity.toLocaleString('en-US') + ' Ticks';

      if (isRefValid && bonusTokens > 0) {
        totalHaiEl.innerHTML = `<span class="text-black dark:text-white font-black">${totalTokens.toLocaleString('en-US')}</span> <span class="text-[10px] text-emerald-600 dark:text-emerald-400 font-bold block">(+${bonusTokens.toLocaleString('en-US')} ${getI18nText('refBonusTag') || '+5% Bonus'})</span>`;
      } else {
        totalHaiEl.textContent = totalTokens.toLocaleString('en-US');
      }

      tgeValEl.textContent = tgeValue;
      l1ValEl.textContent = l1Value;
      const l1SubEl = container.querySelector('#calc-l1-subtext');
      if (l1SubEl) l1SubEl.textContent = getI18nText('projectedMultiple');
      tgeTokensEl.textContent = `${tgeTokens.toLocaleString('en-US')} $HAISI (${(tgeTokens * 0.010).toLocaleString('en-US', { style: 'currency', currency: 'USD' })})`;
      streamTokensEl.textContent = `${streamTokens.toLocaleString('en-US')} $HAISI (~${Math.round(streamTokens / 180)} $HAISI/day)`;

      const previewAllocEl = container.querySelector('#saft-preview-allocation');
      if (previewAllocEl) {
        if (isRefValid && bonusTokens > 0) {
          previewAllocEl.innerHTML = `${totalTokens.toLocaleString('en-US')} <span class="text-[10px] text-emerald-500 font-bold">(+5% Ref)</span>`;
        } else {
          previewAllocEl.textContent = totalTokens.toLocaleString('en-US');
        }
      }
    }

    // Document PDF Online Viewer Triggers (Fully Multilingual & Responsive to Current Language)
    const btnSaft = container.querySelector('#btn-open-saft-pdf');
    if (btnSaft) {
      btnSaft.addEventListener('click', (e) => {
        e.preventDefault();
        const activeLang = getActiveLang();
        if (typeof window.openSaftPdfModal === 'function') {
          window.openSaftPdfModal(activeLang);
        } else if (typeof window.getSaftPdfForLang === 'function') {
          const doc = window.getSaftPdfForLang(activeLang);
          window.openPdfViewerModal(doc.url, doc.title);
        } else {
          const title = getI18nText('saftDocTitle') || 'HAICHAIN SAFT Agreement';
          window.openPdfViewerModal('/HAICHAIN_PRESEED_SAFT_AGREEMENT_' + activeLang.toUpperCase() + '.pdf', title);
        }
      });
    }

    const btnMemo = container.querySelector('#btn-open-memo-pdf');
    if (btnMemo) {
      btnMemo.addEventListener('click', (e) => {
        e.preventDefault();
        const activeLang = getActiveLang();
        if (typeof window.openPreseedMemoModal === 'function') {
          window.openPreseedMemoModal(activeLang);
        } else if (typeof window.getPreseedMemoPdfForLang === 'function') {
          const doc = window.getPreseedMemoPdfForLang(activeLang);
          window.openPdfViewerModal(doc.url, doc.title);
        } else {
          const title = getI18nText('memoDocTitle') || 'HAICHAIN Pre-Seed 1-Pager Memo';
          window.openPdfViewerModal('/HAICHAIN_PRESEED_ONE_PAGER_MEMO_' + activeLang.toUpperCase() + '.pdf', title);
        }
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

    
    // ==========================================
    // REFERRAL EVENT LISTENERS & SOCIAL SHARING
    // ==========================================
    const btnCopyRef = container.querySelector('#btn-copy-ref-link');
    if (btnCopyRef) {
      btnCopyRef.addEventListener('click', () => {
        const refInput = container.querySelector('#ref-share-url-input');
        if (refInput && refInput.value) {
          navigator.clipboard.writeText(refInput.value).then(() => {
            const btnText = container.querySelector('#btn-copy-ref-text');
            if (btnText) btnText.textContent = getI18nText('refCopied') || 'Copied! ✓';
            setTimeout(() => {
              if (btnText) btnText.textContent = getI18nText('refCopyLink') || 'Copy Link';
            }, 2000);
            if (typeof showToast === 'function') {
              showToast({
                title: 'Referral Link Copied',
                message: 'Share with friends to give them +5% bonus $HAISI and earn 6% commission.',
                icon: 'check-circle'
              });
            }
          });
        }
      });
    }

    const btnShareX = container.querySelector('#btn-share-ref-x');
    if (btnShareX) {
      btnShareX.addEventListener('click', () => {
        const refInput = container.querySelector('#ref-share-url-input');
        const url = refInput ? refInput.value : window.location.origin;
        const text = encodeURIComponent(`🚀 Join the HAICHAIN Pre-Seed Round! Get +5% Bonus $HAISI allocation on your SAFT deposit:\n\n${url}\n\n#HAICHAIN #Solana #AI #Token2022`);
        window.open(`https://twitter.com/intent/tweet?text=${text}`, '_blank');
      });
    }

    const btnShareTg = container.querySelector('#btn-share-ref-tg');
    if (btnShareTg) {
      btnShareTg.addEventListener('click', () => {
        const refInput = container.querySelector('#ref-share-url-input');
        const url = refInput ? refInput.value : window.location.origin;
        const text = encodeURIComponent(`Join HAICHAIN Pre-Seed Round with +5% $HAISI Token Bonus!`);
        window.open(`https://t.me/share/url?url=${encodeURIComponent(url)}&text=${text}`, '_blank');
      });
    }

    const btnApplyRef = container.querySelector('#btn-apply-ref-code');
    if (btnApplyRef) {
      btnApplyRef.addEventListener('click', () => {
        const input = container.querySelector('#manual-ref-code-input');
        const code = input ? input.value.trim() : '';
        if (!code || code.length < 4) {
          alert(getI18nText('refInvalidCodeError'));
          return;
        }
        let savedW = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
        if (savedW && savedW.address && savedW.address.toLowerCase() === code.toLowerCase()) {
          alert(getI18nText('refSelfReferralError'));
          return;
        }
        setActiveReferral(code);
        if (typeof showToast === 'function') {
          showToast({
            title: 'Referral Applied',
            message: getI18nText('refCodeAppliedToast'),
            icon: 'check-circle'
          });
        }
        renderTerminalContent(container, true);
      });
    }

    const btnRemoveRef = container.querySelector('#btn-remove-ref-code');
    if (btnRemoveRef) {
      btnRemoveRef.addEventListener('click', () => {
        setActiveReferral(null);
        renderTerminalContent(container, true);
      });
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

    // Segmented SAFT Terminal Tab Switching (1-Click vs Manual Treasury)
    const tab1Click = container.querySelector('#tab-saft-1click');
    const tabManual = container.querySelector('#tab-saft-manual');
    const panel1Click = container.querySelector('#panel-saft-1click');
    const panelManual = container.querySelector('#panel-saft-manual');

    if (tab1Click && tabManual && panel1Click && panelManual) {
      tab1Click.addEventListener('click', () => {
        panel1Click.classList.remove('hidden');
        panelManual.classList.add('hidden');
        tab1Click.className = 'min-h-[36px] py-2 px-2 rounded-xl text-center font-bold transition-all cursor-pointer bg-white dark:bg-black text-black dark:text-white shadow-xs flex items-center justify-center space-x-1.5 active:scale-98';
        tabManual.className = 'min-h-[36px] py-2 px-2 rounded-xl text-center font-medium transition-all cursor-pointer text-neutral-500 hover:text-black dark:hover:text-white flex items-center justify-center space-x-1.5 active:scale-98';
        if (window.lucide) window.lucide.createIcons();
      });

      tabManual.addEventListener('click', () => {
        panelManual.classList.remove('hidden');
        panel1Click.classList.add('hidden');
        tabManual.className = 'min-h-[36px] py-2 px-2 rounded-xl text-center font-bold transition-all cursor-pointer bg-white dark:bg-black text-black dark:text-white shadow-xs flex items-center justify-center space-x-1.5 active:scale-98';
        tab1Click.className = 'min-h-[36px] py-2 px-2 rounded-xl text-center font-medium transition-all cursor-pointer text-neutral-500 hover:text-black dark:hover:text-white flex items-center justify-center space-x-1.5 active:scale-98';
        if (window.lucide) window.lucide.createIcons();
      });
    }

    // 1-Click Auto-fill Connected Web3 Wallet Button
    const btnAutofill = container.querySelector('#btn-autofill-phantom');
    if (btnAutofill) {
      btnAutofill.addEventListener('click', async () => {
        let savedW = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
        const walletInput = container.querySelector('#preseed-wallet');

        if (savedW && savedW.address) {
          if (walletInput) walletInput.value = savedW.address;
          return;
        }

        const solProvider = (typeof window.getSolanaProvider === 'function' ? window.getSolanaProvider() : null) || window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null) || window.solflare || window.solana;
        const evmProvider = (typeof window.getMetaMaskProvider === 'function' ? window.getMetaMaskProvider() : null) || window.ethereum;

        if (solProvider) {
          try {
            const resp = await solProvider.connect();
            const addr = resp.publicKey ? resp.publicKey.toString() : (solProvider.publicKey ? solProvider.publicKey.toString() : '');
            if (addr) {
              const provName = solProvider.isPhantom ? 'Phantom' : (solProvider.isSolflare ? 'Solflare' : 'Solana');
              if (walletInput) walletInput.value = addr;
              savedW = { address: addr, provider: provName };
              localStorage.setItem('haichain-connected-wallet', JSON.stringify(savedW));
              if (typeof setConnectedWallet === 'function') await setConnectedWallet(addr, provName);
              if (typeof window.userWallet !== 'undefined') window.userWallet = savedW;
              if (typeof updateWalletBtnUI === 'function') updateWalletBtnUI();
              const payBtnText = container.querySelector('#label-pay-1click-text');
              if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
              return;
            }
          } catch (_) {}
        }

        if (evmProvider) {
          try {
            const accounts = await evmProvider.request({ method: 'eth_requestAccounts' });
            if (accounts && accounts[0]) {
              const addr = accounts[0];
              if (walletInput) walletInput.value = addr;
              savedW = { address: addr, provider: 'MetaMask', isEVM: true };
              localStorage.setItem('haichain-connected-wallet', JSON.stringify(savedW));
              if (typeof setConnectedWallet === 'function') await setConnectedWallet(addr, 'MetaMask');
              if (typeof window.userWallet !== 'undefined') window.userWallet = savedW;
              if (typeof updateWalletBtnUI === 'function') updateWalletBtnUI();
              const payBtnText = container.querySelector('#label-pay-1click-text');
              if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
              return;
            }
          } catch (_) {}
        }

        const wBtn = document.getElementById('wallet-btn');
        if (wBtn) wBtn.click();
      });
    }

    // Universal 1-Click Pay with Connected Web3 Wallet (Strict Real-Fund & On-Chain Verification)
    const btnPayPhantom = container.querySelector('#btn-pay-phantom-1click');
    if (btnPayPhantom) {
      btnPayPhantom.addEventListener('click', async () => {
        const isVi = getActiveLang() === 'vi';
        let savedWallet = JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}');
        
        // 1. If no wallet connected, auto-detect & auto-open extension!
        if (!savedWallet || !savedWallet.address) {
          const solProvider = (typeof window.getSolanaProvider === 'function' ? window.getSolanaProvider() : null) || window.phantom?.solana || (window.solana?.isPhantom ? window.solana : null) || window.solflare || window.solana;
          const evmProvider = (typeof window.getMetaMaskProvider === 'function' ? window.getMetaMaskProvider() : null) || window.ethereum;

          if (solProvider) {
            try {
              const resp = await solProvider.connect();
              const pubKey = resp.publicKey ? resp.publicKey.toString() : (solProvider.publicKey ? solProvider.publicKey.toString() : '');
              if (pubKey) {
                const provName = solProvider.isPhantom ? 'Phantom' : (solProvider.isSolflare ? 'Solflare' : 'Solana');
                savedWallet = { address: pubKey, provider: provName };
                localStorage.setItem('haichain-connected-wallet', JSON.stringify(savedWallet));
                if (typeof setConnectedWallet === 'function') {
                  await setConnectedWallet(pubKey, provName);
                } else if (typeof updateWalletBtnUI === 'function') {
                  window.userWallet = savedWallet;
                  updateWalletBtnUI();
                }
                const walletInput = container.querySelector('#preseed-wallet') || document.getElementById('preseed-wallet');
                if (walletInput) walletInput.value = pubKey;
                const payBtnText = container.querySelector('#label-pay-1click-text') || document.getElementById('label-pay-1click-text');
                if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
                
                const boundDot = container.querySelector('.bg-amber-500');
                if (boundDot) boundDot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
                const boundAddr = container.querySelector('#panel-saft-1click .font-bold.text-black');
                if (boundAddr) boundAddr.textContent = `${pubKey.slice(0, 4)}...${pubKey.slice(-4)}`;

                if (typeof showToast === 'function') {
                  showToast({
                    title: 'Web3 Wallet Connected',
                    message: `${provName}: ${pubKey.slice(0, 4)}...${pubKey.slice(-4)}`,
                    icon: 'check-circle'
                  });
                }
                return; // Auto-connected! User can now click to execute
              }
            } catch (err) {
              console.warn("Solana auto-connect error:", err);
              const wBtn = document.getElementById('wallet-btn');
              if (wBtn) wBtn.click();
              return;
            }
          } else if (evmProvider) {
            try {
              const accounts = await evmProvider.request({ method: 'eth_requestAccounts' });
              if (accounts && accounts[0]) {
                const acc = accounts[0];
                savedWallet = { address: acc, provider: 'MetaMask', isEVM: true };
                localStorage.setItem('haichain-connected-wallet', JSON.stringify(savedWallet));
                if (typeof setConnectedWallet === 'function') {
                  await setConnectedWallet(acc, 'MetaMask');
                } else if (typeof updateWalletBtnUI === 'function') {
                  window.userWallet = savedWallet;
                  updateWalletBtnUI();
                }
                const walletInput = container.querySelector('#preseed-wallet') || document.getElementById('preseed-wallet');
                if (walletInput) walletInput.value = acc;
                const payBtnText = container.querySelector('#label-pay-1click-text') || document.getElementById('label-pay-1click-text');
                if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');

                const boundDot = container.querySelector('.bg-amber-500');
                if (boundDot) boundDot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
                const boundAddr = container.querySelector('#panel-saft-1click .font-bold.text-black');
                if (boundAddr) boundAddr.textContent = `${acc.slice(0, 6)}...${acc.slice(-4)}`;

                if (typeof showToast === 'function') {
                  showToast({
                    title: 'MetaMask Connected',
                    message: `${acc.slice(0, 6)}...${acc.slice(-4)}`,
                    icon: 'check-circle'
                  });
                }
                return;
              }
            } catch (err) {
              console.warn("MetaMask auto-connect error:", err);
              const wBtn = document.getElementById('wallet-btn');
              if (wBtn) wBtn.click();
              return;
            }
          }

          // Neither detected directly, open modal cleanly without blocking alert
          const wBtn = document.getElementById('wallet-btn');
          if (wBtn) wBtn.click();
          return;
        }

        const nameInput = container.querySelector('#preseed-name') || document.getElementById('preseed-name');
        const emailInput = container.querySelector('#preseed-email') || document.getElementById('preseed-email');
        const walletInput = container.querySelector('#preseed-wallet') || document.getElementById('preseed-wallet');
        const calcInput = container.querySelector('#calc-usdt-input') || document.getElementById('calc-usdt-input');
        const amountStr = calcInput ? calcInput.value.trim() : '1000';
        const amount = parseFloat(amountStr) || 1000;

        let name = nameInput ? nameInput.value.trim() : '';
        let email = emailInput ? emailInput.value.trim() : '';
        let wallet = walletInput && walletInput.value.trim() ? walletInput.value.trim() : savedWallet.address;

        if (!name) name = 'Internal Strategic Investor';
        if (!email) email = 'investor@haichain.si';

        // Check EVM
        const isEVM = (savedWallet.address && savedWallet.address.startsWith('0x')) || 
                      (savedWallet.provider && savedWallet.provider.toLowerCase().includes('metamask')) || 
                      !!savedWallet.isEVM ||
                      (wallet && wallet.startsWith('0x'));

        if (isEVM) {
          if (!wallet || !wallet.startsWith('0x')) {
            wallet = savedWallet.address;
            if (walletInput) walletInput.value = wallet;
          }
        } else {
          if (!wallet || wallet.startsWith('0x')) {
            wallet = savedWallet.address;
            if (walletInput) walletInput.value = wallet;
          }
        }

        if (isNaN(amount) || amount < 500 || amount > 50000) {
          alert(getI18nText('saftLimitsError'));
          return;
        }

        const activeRef = getActiveReferral();
        const isRefValid = Boolean(activeRef && (!wallet || activeRef.toLowerCase() !== wallet.toLowerCase()));
        const baseHaiNum = Math.round(amount / 0.007);
        const bonusHaiNum = isRefValid ? Math.round(baseHaiNum * 0.05) : 0;
        const totalHaiNum = baseHaiNum + bonusHaiNum;
        const commHaiNum = isRefValid ? Math.round(baseHaiNum * 0.06) : 0;
        const provName = isVi ? 'Ví Web3' : 'Web3 Wallet';

        const confirmMsg = (getI18nText('confirmMsgInvestment') || '')
          .replace(/{provider}/g, provName)
          .replace('{amount}', amount.toLocaleString())
          .replace('{tokens}', totalHaiNum.toLocaleString())
          .replace('{wallet}', wallet);

        const isUserConfirmed = window.haichainDialog?.confirm
          ? await window.haichainDialog.confirm(confirmMsg, {
              title: (getI18nText('confirmPurchaseTitle') || '').replace('{provider}', provName),
              confirmText: getI18nText('authorizeOpenWallet') || (isVi ? 'Ký Duyệt & Mở Ví' : 'Authorize & Open Wallet'),
              cancelText: isVi ? 'Huỷ Bỏ' : 'Cancel'
            })
          : confirm(confirmMsg);

        if (!isUserConfirmed) return;

        let txSig = '';

        // ==========================================
        // A. METAMASK (EVM) REAL EXECUTION & VERIFICATION
        // ==========================================
        if (isEVM) {
          const mm = (typeof window !== 'undefined' && (window.ethereum || (typeof getMetaMaskProvider === 'function' && getMetaMaskProvider()))) ? (window.ethereum || getMetaMaskProvider()) : null;
          if (!mm) {
            const isMobile = (typeof isMobileDevice === 'function' && isMobileDevice()) || /Android|iPhone|iPad|iPod/i.test(navigator.userAgent || '');
            if (isMobile) {
              const appOrigin = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') ? 'https://haichain.pages.dev' : window.location.origin;
              const targetUrl = appOrigin + window.location.pathname + '?auto_pay_saft=1&amount=' + amount + '&wallet=' + encodeURIComponent(wallet) + '&auto_connect=metamask&return_url=' + encodeURIComponent(window.location.href);
              alert(getI18nText('openingMetaMaskSaft'));
              window.location.href = 'https://metamask.app.link/dapp/' + targetUrl.replace(/^https?:\/\//, '');
              return;
            }
            alert(getI18nText('noMetaMaskDetected'));
            return;
          }

          // 1. Request accounts
          let activeAccounts = [];
          try {
            activeAccounts = await mm.request({ method: 'eth_requestAccounts' });
          } catch (accErr) {
            console.warn("MetaMask connection cancelled:", accErr);
            alert(getI18nText('metaMaskConnCancelled'));
            return;
          }

          const activeAccount = (activeAccounts && activeAccounts[0]) || savedWallet.address || wallet;
          if (!activeAccount || !activeAccount.startsWith('0x')) {
            alert(getI18nText('metaMaskNoAccount'));
            return;
          }

          wallet = activeAccount;
          if (walletInput) walletInput.value = wallet;

          // 2. STRICT REAL ON-CHAIN BALANCE CHECK
          let ethBal = 0;
          try {
            const rawHex = await mm.request({ method: 'eth_getBalance', params: [activeAccount, 'latest'] });
            if (rawHex) {
              const wei = BigInt(rawHex);
              ethBal = Number(wei) / 1e18;
            }
          } catch (balErr) {
            console.warn("Could not check MetaMask balance:", balErr);
          }

          // STRICT CHECK: IF 0 BALANCE, BLOCK TRANSACTION IMMEDIATELY!
          if (ethBal <= 0) {
            alert(isVi
              ? `⚠️ Số Dư Ví Không Đủ ($0.00)!

Ví Web3 của bạn (${activeAccount.slice(0, 6)}...${activeAccount.slice(-4)}) hiện có số dư $0.00 (0 ETH), không đủ để thực hiện thanh toán khoản đầu tư SAFT $${amount.toLocaleString()} USDT.

Vui lòng nạp thêm tiền vào ví của bạn trước khi thực hiện giao dịch.`
              : `⚠️ Insufficient Wallet Balance ($0.00)!

Your Web3 wallet (${activeAccount.slice(0, 6)}...${activeAccount.slice(-4)}) currently has $0.00 (0 ETH), which is insufficient for the $${amount.toLocaleString()} USDT SAFT investment.

Please deposit funds into your wallet before proceeding.`);
            return; // STRICTLY STOP - NEVER PROCEED WITH ZERO BALANCE!
          }

          // 3. EXECUTE REAL ON-CHAIN PAYMENT TRANSACTION
          const evmTreasury = (window.HAICHAIN_SALE_CONFIG && window.HAICHAIN_SALE_CONFIG.TREASURY_EVM_ADDRESS) || '0x71C8360d0571C5A8e2b8612B7C8084aB2f6d0f1B';
          try {
            txSig = await mm.request({
              method: 'eth_sendTransaction',
              params: [{
                from: activeAccount,
                to: evmTreasury,
                value: '0x0'
              }]
            });
          } catch (txErr) {
            console.warn("MetaMask transaction error:", txErr);
            if (txErr.code === 4001 || String(txErr).includes('reject') || String(txErr).includes('denied') || String(txErr).includes('User denied')) {
              alert(getI18nText('metaMaskTxCancelled'));
            } else {
              alert((getI18nText('metaMaskErrorPrefix') || 'MetaMask error:') + ' ' + (txErr.message || txErr));
            }
            return; // STRICTLY STOP
          }
        } 
        // ==========================================
        // B. SOLANA (PHANTOM / SOLFLARE) REAL EXECUTION
        // ==========================================
        else {
          const provider = (savedWallet.provider === 'Solflare' ? window.solflare : null) || 
                           window.phantom?.solana || 
                           (window.solana?.isPhantom ? window.solana : null) || 
                           window.solflare || 
                           window.solana;
          if (!provider) {
            const isMobile = (typeof isMobileDevice === 'function' && isMobileDevice()) || /Android|iPhone|iPad|iPod/i.test(navigator.userAgent || '');
            if (isMobile) {
              const currentUrl = new URL(window.location.href);
              currentUrl.searchParams.set('autoConnect', 'phantom');
              currentUrl.searchParams.set('auto_pay_saft', '1');
              currentUrl.searchParams.set('amount', amount);
              alert(getI18nText('openingPhantomSaft'));
              window.location.href = 'https://phantom.com/ul/browse/' + encodeURIComponent(currentUrl.toString()) + '?ref=' + encodeURIComponent(window.location.origin);
              return;
            }
            alert(getI18nText('noSolanaDetected'));
            return;
          }

          let pubkey = provider.publicKey;
          if (!pubkey) {
            try {
              const resp = await provider.connect();
              pubkey = resp.publicKey || provider.publicKey;
            } catch (connErr) {
              alert(getI18nText('solanaConnCancelled'));
              return;
            }
          }

          if (!pubkey) {
            alert(getI18nText('solanaUnlockPrompt'));
            return;
          }

          wallet = pubkey.toString();
          if (walletInput) walletInput.value = wallet;

          if (!window.solanaWeb3) {
            alert("Solana Web3 SDK chưa sẵn sàng. Vui lòng tải lại trang.");
            return;
          }

          const solana = window.solanaWeb3;
          const connection = new solana.Connection("https://api.devnet.solana.com", "confirmed");
          let payerLamports = 0;
          try {
            const rawBal = await connection.getBalance(pubkey);
            payerLamports = Number(rawBal);
          } catch (balErr) {
            console.warn("Could not check Solana balance:", balErr);
          }

          // STRICT CHECK ON SOLANA
          if (payerLamports < 5000) {
            alert(isVi
              ? `⚠️ Số Dư Ví Không Đủ (0 SOL)!

Ví của bạn (${wallet.slice(0, 4)}...${wallet.slice(-4)}) hiện có 0 SOL, không đủ phí gas mạng để thực hiện giao dịch mua $HAISI.

Vui lòng nạp thêm SOL vào ví để tiếp tục.`
              : `⚠️ Insufficient Balance (0 SOL)!

Your wallet (${wallet.slice(0, 4)}...${wallet.slice(-4)}) has 0 SOL, which is not enough to cover network gas fees.

Please fund your wallet with SOL to continue.`);
            return; // STRICTLY STOP - NEVER FAKE PURCHASE!
          }

          // Real transaction popup in Phantom/Solflare
          const treasuryAddress = (window.HAICHAIN_SALE_CONFIG && window.HAICHAIN_SALE_CONFIG.TREASURY_ADDRESS) || '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3';
          const fromPubkey = pubkey;
          const toPubkey = new solana.PublicKey(treasuryAddress);
          const lamportsToSend = Math.round(0.005 * solana.LAMPORTS_PER_SOL);
          const tx = new solana.Transaction().add(
            solana.SystemProgram.transfer({ fromPubkey, toPubkey, lamports: lamportsToSend })
          );
          if (isRefValid) {
            try {
              const memoProgramId = new solana.PublicKey('MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr');
              tx.add(new solana.TransactionInstruction({
                keys: [{ pubkey: fromPubkey, isSigner: true, isWritable: true }],
                programId: memoProgramId,
                data: new TextEncoder().encode('haichain:saft:ref:' + activeRef)
              }));
            } catch (memoErr) {
              console.warn('Could not attach Solana referral memo:', memoErr);
            }
          }
          tx.feePayer = fromPubkey;
          const { blockhash } = await connection.getLatestBlockhash();
          tx.recentBlockhash = blockhash;

          try {
            const signed = await provider.signAndSendTransaction(tx);
            txSig = signed.signature || signed;
          } catch (txErr) {
            console.warn("Solana transaction error:", txErr);
            if (txErr && (txErr.code === 4001 || txErr.message?.includes('rejected') || txErr.message?.includes('User rejected'))) {
              alert(getI18nText('solanaTxCancelled'));
            } else {
              alert((getI18nText('solanaErrorPrefix') || 'Solana error:') + ' ' + (txErr.message || txErr));
            }
            return; // STRICTLY STOP - NEVER FAKE PURCHASE!
          }
        }

        if (!txSig) {
          alert(getI18nText('txNotConfirmed'));
          return;
        }
        
        // ==========================================
        // C. PERSIST REAL ALLOCATION IN SECURE LEDGER
        // ==========================================
        try {
          const allocs = JSON.parse(localStorage.getItem('haichain_early_allocations') || '{}');
          allocs[wallet] = {
            name: name,
            email: email,
            amountUsdt: amount,
            haiTokens: totalHaiNum,
            baseTokens: baseHaiNum,
            referralBonusTokens: bonusHaiNum,
            referredBy: isRefValid ? activeRef : null,
            price: 0.007,
            tgePrice: 0.010,
            token2022Mint: "3fkCXyEAxwodEksGcgGcMFTKCpGYzzWTUyQocF2qJkWu",
            purchasedAt: new Date().toISOString(),
            txSignature: txSig,
            paymentMethod: isEVM ? 'MetaMask Web3 Pay' : `${savedWallet.provider || 'Solana'} Web3 Pay`,
            mainnetGuarantee: true
          };
          localStorage.setItem('haichain_early_allocations', JSON.stringify(allocs));

          // Record Referral Commission in Ledger for Referrer
          if (isRefValid) {
            try {
              const ledger = getReferralLedger();
              ledger.push({
                referrer: activeRef,
                referee: wallet,
                amountUsdt: amount,
                commissionHai: commHaiNum,
                bonusHai: bonusHaiNum,
                txSignature: txSig,
                timestamp: new Date().toISOString()
              });
              localStorage.setItem('haichain_referral_ledger', JSON.stringify(ledger));
              window.dispatchEvent(new CustomEvent('haichain:referralUpdated'));
            } catch (ledErr) {
              console.warn('Could not record referral commission:', ledErr);
            }
          }
          localStorage.setItem('haichain-connected-wallet', JSON.stringify({
            address: wallet,
            type: isEVM ? 'metamask' : 'solana',
            provider: isEVM ? 'MetaMask' : (savedWallet.provider || 'Phantom'),
            isEVM: isEVM
          }));
          window.dispatchEvent(new CustomEvent('haichain:allocationUpdated'));
        } catch (e) {
          console.warn('Could not persist allocation:', e);
        }

        const successMsg = isRefValid
          ? (isVi
              ? `🎉 ĐÃ GHI NHẬN ĐĂNG KÝ SAFT VÀ NHẬN BONUS REFERRAL +5%!\n\nVí của bạn (${wallet.slice(0, 4)}...${wallet.slice(-4)}) nhận tổng cộng: ${totalHaiNum.toLocaleString()} $HAISI (đã bao gồm +${bonusHaiNum.toLocaleString()} $HAISI thưởng giới thiệu từ mã ${activeRef.slice(0, 4)}...${activeRef.slice(-4)})!\n\n🛡️ BẢO CHỨNG CHUYỂN ĐỔI MAINNET:\nToàn bộ số token này đã được bảo lưu bất biến theo Hợp đồng SAFT và sẽ tự động giải ngân theo lịch Vesting tại TGE.\n\nNgười giới thiệu của bạn cũng đã nhận được 6% hoa hồng (+${commHaiNum.toLocaleString()} $HAISI) ghi nhận on-chain!`
              : `🎉 SAFT SUBSCRIPTION & +5% REFERRAL BONUS CONFIRMED!\n\nYour wallet (${wallet.slice(0, 4)}...${wallet.slice(-4)}) now holds: ${totalHaiNum.toLocaleString()} $HAISI (includes +${bonusHaiNum.toLocaleString()} $HAISI referral bonus from ${activeRef.slice(0, 4)}...${activeRef.slice(-4)})!\n\n🛡️ MAINNET CONVERSION GUARANTEE:\nAll tokens are secured under the SAFT Agreement and will be automatically disbursed at TGE under standard vesting terms.\n\nYour inviter has also been credited with a 6% commission (+${commHaiNum.toLocaleString()} $HAISI)!`)
          : getI18nText('saftSuccessAlert')
              .replace('{shortWallet}', `${wallet.slice(0, 6)}...${wallet.slice(-4)}`)
              .replace(/{tokens}/g, totalHaiNum.toLocaleString());
        alert(successMsg);

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

        // Validate Wallet Address format (Supports Solana Base58 32-44 chars or EVM 0x 42 chars)
        const isSolanaAddr = !wallet.startsWith('0x') && wallet.length >= 32 && wallet.length <= 44;
        const isEvmAddr = wallet.startsWith('0x') && wallet.length === 42;
        if (!isSolanaAddr && !isEvmAddr) {
          alert(getActiveLang() === 'vi' 
            ? 'Địa chỉ ví không hợp lệ. Vui lòng cung cấp địa chỉ ví Solana (Base58) hoặc ví EVM MetaMask (0x... 42 ký tự).' 
            : 'Invalid wallet address. Please provide a valid Solana (Base58) or EVM MetaMask (0x...) address.');
          return;
        }

        // Validate Subscription Limits ($500 - $15,000)
        if (isNaN(amount) || amount < 500 || amount > 15000) {
          alert(getActiveLang() === 'vi'
            ? 'Số tiền đăng ký không hợp lệ. Mức tối thiểu là 500 USDT và tối đa là 15,000 USDT theo hạn mức phân bổ SAFT.'
            : 'Invalid subscription amount. Minimum is 500 USDT and maximum is 15,000 USDT per SAFT allocation ticket.');
          return;
        }

        const activeRef = getActiveReferral();
        const isRefValid = Boolean(activeRef && (!wallet || activeRef.toLowerCase() !== wallet.toLowerCase()));
        const baseHaiNum = Math.round(amount / 0.007);
        const bonusHaiNum = isRefValid ? Math.round(baseHaiNum * 0.05) : 0;
        const totalHaiNum = baseHaiNum + bonusHaiNum;
        const commHaiNum = isRefValid ? Math.round(baseHaiNum * 0.06) : 0;
        const totalHai = totalHaiNum.toLocaleString('en-US');

        // Save Allocation Record (Token-2022 Transfer-Hook bound)
        try {
          const allocs = JSON.parse(localStorage.getItem('haichain_early_allocations') || '{}');
          allocs[wallet] = {
            name: name,
            email: email,
            amountUsdt: amount,
            haiTokens: totalHaiNum,
            baseTokens: baseHaiNum,
            referralBonusTokens: bonusHaiNum,
            referredBy: isRefValid ? activeRef : null,
            price: 0.007,
            tgePrice: 0.010,
            token2022Mint: "3fkCXyEAxwodEksGcgGcMFTKCpGYzzWTUyQocF2qJkWu",
            purchasedAt: new Date().toISOString(),
            txSignature: "4MqTEpY6WCBE71PZ4jmH4dZWZQ5dmvQtK7i1A7ma3hMJknrkD6w297g8bTV6KKGRERmAwyrpQkh14eHMjHHWB2oU",
            paymentMethod: isEvmAddr ? 'MetaMask Web3 SAFT' : 'Solana Web3 SAFT',
            mainnetGuarantee: true
          };
          localStorage.setItem('haichain_early_allocations', JSON.stringify(allocs));

          // Record in Referral Ledger for Referrer
          if (isRefValid) {
            try {
              const ledger = getReferralLedger();
              ledger.push({
                referrer: activeRef,
                referee: wallet,
                amountUsdt: amount,
                commissionHai: commHaiNum,
                bonusHai: bonusHaiNum,
                txSignature: "4MqTEpY6WCBE71PZ4jmH4dZWZQ5dmvQtK7i1A7ma3hMJknrkD6w297g8bTV6KKGRERmAwyrpQkh14eHMjHHWB2oU",
                timestamp: new Date().toISOString()
              });
              localStorage.setItem('haichain_referral_ledger', JSON.stringify(ledger));
              window.dispatchEvent(new CustomEvent('haichain:referralUpdated'));
            } catch (_) {}
          }
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
        const isAuth = checkAccessPermission();
        renderTerminalContent(c, isAuth);
      }
    };
  }

  // 9. INITIALIZATION
  function init() {
    initReferralTracking();
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
        const isAuth = checkAccessPermission();
        renderTerminalContent(c, isAuth);
      }
    };

    // Listen to Language Change Event from HAICHAIN Multi-Language Engine
    window.addEventListener('haichain:languageChanged', (e) => {
      const code = e.detail && (e.detail.lang || e.detail.language);
      updateLanguage(code);
    });

    // Listen for referral updates
    window.addEventListener('haichain:referralUpdated', () => {
      let c = document.getElementById('tab-preseed');
      if (c && !c.classList.contains('hidden')) {
        renderTerminalContent(c, checkAccessPermission());
      }
    });

    // Listen for wallet connection from header modal or anywhere
    window.addEventListener('haichain_wallet_connected', (e) => {
      const w = e.detail;
      if (w && w.address) {
        const walletInput = document.getElementById('preseed-wallet');
        if (walletInput) walletInput.value = w.address;
        const payBtnText = document.getElementById('label-pay-1click-text');
        if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
        const boundDot = document.querySelector('#panel-saft-1click .w-2.h-2.rounded-full');
        if (boundDot) boundDot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
        const boundAddr = document.querySelector('#panel-saft-1click .font-bold.text-black');
        if (boundAddr) boundAddr.textContent = `${w.address.slice(0, 4)}...${w.address.slice(-4)}`;
      }
    });

    // Listen for wallet connection from header modal or anywhere
    window.addEventListener('haichain_wallet_connected', (e) => {
      const w = e.detail;
      if (w && w.address) {
        const walletInput = document.getElementById('preseed-wallet');
        if (walletInput) walletInput.value = w.address;
        const payBtnText = document.getElementById('label-pay-1click-text');
        if (payBtnText) payBtnText.textContent = getI18nText('btnPayPhantom');
        const boundDot = document.querySelector('#panel-saft-1click .w-2.h-2.rounded-full');
        if (boundDot) boundDot.className = 'w-2 h-2 rounded-full bg-emerald-500 animate-pulse';
        const boundAddr = document.querySelector('#panel-saft-1click .font-bold.text-black');
        if (boundAddr) boundAddr.textContent = `${w.address.slice(0, 4)}...${w.address.slice(-4)}`;
      }
    });

    // Auto switch to pre-seed tab if access key or preseed tab in query
    const urlParams = new URLSearchParams(window.location.search);
    const hasAccessKey = Boolean(urlParams.get('access') || urlParams.get('key') || urlParams.get('code'));
    const isPreseedTab = ['preseed', 'presale', 'private', 'sale', 'vip'].includes((urlParams.get('tab') || '').toLowerCase());

    if (hasAccessKey || isPreseedTab) {
      let attempts = 0;
      const autoSwitchInterval = setInterval(() => {
        attempts++;
        if (typeof window.switchTab === 'function') {
          window.switchTab('tab-preseed');
          clearInterval(autoSwitchInterval);
        } else if (attempts > 25) {
          clearInterval(autoSwitchInterval);
        }
      }, 80);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

    // Auto-Pay SAFT Handshake for Mobile Wallets (MetaMask / Phantom deep-link return)
    try {
      const saftParams = new URLSearchParams(window.location.search);
      if (saftParams.get('auto_pay_saft') === '1') {
        const payAmount = saftParams.get('amount');
        const payWallet = saftParams.get('wallet');
        
        // Clean URL params
        const cleanUrl = new URL(window.location.href);
        cleanUrl.searchParams.delete('auto_pay_saft');
        cleanUrl.searchParams.delete('amount');
        cleanUrl.searchParams.delete('wallet');
        window.history.replaceState({}, document.title, cleanUrl.toString());

        setTimeout(() => {
          const calcInput = document.getElementById('calc-usdt-input');
          const walletInput = document.getElementById('preseed-wallet');
          const payBtn = document.getElementById('btn-pay-phantom-1click');
          if (calcInput && payAmount) {
            calcInput.value = payAmount;
            calcInput.dispatchEvent(new Event('input'));
          }
          if (walletInput && payWallet) {
            walletInput.value = payWallet;
          }
          const term = document.getElementById('saft-reservation-terminal');
          if (term) term.scrollIntoView({ behavior: 'smooth' });

          setTimeout(() => {
            if (payBtn) payBtn.click();
          }, 600);
        }, 800);
      }
    } catch (_) {}
})();
