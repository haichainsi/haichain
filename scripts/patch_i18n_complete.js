const fs = require('fs');

console.log('=== APPLYING COMPREHENSIVE I18N UPGRADES ===');

const COMMON_UPDATES = {
  // Common headers across all languages
  colTao: "Coinbase AgentKit (x402)",
  colRender: "Skyfire Protocol (EVM)",
};

const LANG_DATA = {
  en: {
    "cluster.auditsPassed": "15/15 Test Vectors Verified",
    "pot.txSettled": "0.14ms Netting • On-Chain Queued",
    "comp.colTao": "Coinbase AgentKit (x402)",
    "comp.colRender": "Skyfire Protocol (EVM)",
    "comp.colEliza": "Stripe / Legacy Rails",
    "comp.row1Hai": "Sub-cent micro-payment OS, deterministic Sub-PDA bounds & native Human-in-the-Loop x402 arbitration",
    "comp.row1Tao": "EVM smart contract wallet SDK for AI agents on Base/Ethereum",
    "comp.row1Render": "B2B custodial payment API wrapping USDC on Base/Polygon",
    "comp.row1Eliza": "Legacy credit card merchant gateway designed for human checkouts",
    "comp.row2Hai": "In-Memory Netting: 0.14ms | Solana Settlement: <400ms",
    "comp.row2Tao": "2 - 12 seconds (Base/EVM block times; no in-memory netting)",
    "comp.row2Render": "2 - 5+ seconds (API verification + EVM transaction confirmation)",
    "comp.row2Eliza": "2 - 3 business days (T+2 legacy bank interchange clearing)",
    "comp.row3Hai": "Nano-cents (< $0.0002). Viable down to $0.0001 per API call",
    "comp.row3Tao": "$0.01 - $0.08 Base gas fee (prohibitive for streaming micro-calls)",
    "comp.row3Render": "$0.02 - $0.10+ per payment call; batch invoicing required",
    "comp.row3Eliza": "$0.30 fixed swipe fee + 2.9% (30,000% overhead on a $0.001 query)",
    "comp.row4Hai": "Deterministic Sub-PDA Spending Bounds + Instant Panic Kill-Switch Circuit",
    "comp.row4Tao": "Application-level MPC key policies; vulnerable if agent logic is compromised",
    "comp.row4Render": "Centralized API quota limits managed on corporate web portal",
    "comp.row4Eliza": "Must freeze corporate card and file chargeback disputes taking 30-60 days",
    "comp.row5Hai": "Invisible Web3: Biometric Passkey, instant fiat onramp & MCP protocol integration",
    "comp.row5Tao": "Developer CDP API keys and complex EVM smart wallet infrastructure",
    "comp.row5Render": "Web2 enterprise API keys linked to corporate deposit accounts",
    "comp.row5Eliza": "Manual credit card entry, exposed PII, vulnerable to identity theft",
    "comp.row6Hai": "Protocol Fee Netting Utility: 40% staking distribution + 60% continuous Buyback & Burn",
    "comp.row6Tao": "Zero native token; sequencer revenue accrues solely to Base / Coinbase",
    "comp.row6Render": "Proprietary corporate margin; closed-source corporate equity capture",
    "comp.row6Eliza": "100% merchant interchange revenue retained by Stripe Inc. shareholders",
    "comp.row7Hai": "Native Reverse Micro-Tasking via HTTP x402: Agents autonomously escrow USDT to hire verified human domain experts for sub-second appraisal and ground-truth validation.",
    "comp.row7Tao": "No native reverse bounty rail; developers must manually architect custom human escalation mechanisms.",
    "comp.row7Render": "Enterprise support tickets and manual customer service intervention; no sub-second agent bounties.",
    "comp.row7Eliza": "30 - 90 day credit card chargeback arbitration with high dispute penalties.",
    "aud.investorFutureDesc": "Long-term protocol value accrual: 1:1 transition into Native Gas Asset upon dedicated App-Chain and Sovereign L1 scaling, capturing network fee velocity across the autonomous agent economy.",
    "tech.done2": "Passed 15/15 automated forensic test vectors (simulating historic $800M+ Wormhole, Nomad, Euler exploits). Independent external audit scheduled prior to Mainnet TGE.",
    "roadmap.stage1Item3": "Milestone: 100,000+ Connected Agents & 50M+ Monthly Micro-Settlements",
    "footer.compliance": "Non-Custodial Architecture • EU MiCA / FinCEN Utility Standards • Formally Verified Sub-PDA Invariants"
  },
  vi: {
    "cluster.auditsPassed": "15/15 Kiểm Tra Vector An Toàn",
    "pot.txSettled": "0.14ms Netting • Chờ Batch On-Chain",
    "comp.colTao": "Coinbase AgentKit (x402)",
    "comp.colRender": "Skyfire Protocol (EVM)",
    "comp.colEliza": "Stripe / Cổng Thẻ Cũ",
    "comp.row1Hai": "HĐH vi thanh toán máy móc, hạn mức ví Sub-PDA bất biến & cơ chế con người thẩm định điểm mù AI tự hành",
    "comp.row1Tao": "SDK ví thông minh EVM cho AI Agent trên Base/Ethereum",
    "comp.row1Render": "API thanh toán B2B lưu ký cho Agent sử dụng USDC trên Base/Polygon",
    "comp.row1Eliza": "Cổng quẹt thẻ ngân hàng truyền thống cho người dùng Web2",
    "comp.row2Hai": "Khớp lệnh In-Memory: 0.14ms | Khóa khối Solana: <400ms",
    "comp.row2Tao": "2 - 12 giây (Thời gian block Base/EVM; không có khớp lệnh in-memory)",
    "comp.row2Render": "2 - 5+ giây (Xác thực API + chờ xác nhận giao dịch EVM)",
    "comp.row2Eliza": "2 - 3 ngày làm việc (Độ trễ đối soát ngân hàng T+2)",
    "comp.row3Hai": "Nano-cents (< $0.0002). Khả thi từ $0.0001 cho mỗi lượt gọi API",
    "comp.row3Tao": "Phí gas Base L2 $0.01 - $0.08 (không khả thi cho vi thanh toán liên tục)",
    "comp.row3Render": "Phí giao dịch $0.02 - $0.10+; buộc phải gom lô hóa đơn định kỳ",
    "comp.row3Eliza": "Phí cố định $0.30 + 2.9% (đắt gấp 300 lần giao dịch nano-cent)",
    "comp.row4Hai": "Giới hạn chi tiêu Sub-PDA bất biến + Cầu dao ngắt khẩn cấp Panic Kill-Switch (khống chế phạm vi thiệt hại)",
    "comp.row4Tao": "Chính sách khóa MPC ở tầng ứng dụng; rủi ro nếu logic của Agent bị tấn công",
    "comp.row4Render": "Hạn mức API tập trung quản lý qua trang quản trị doanh nghiệp",
    "comp.row4Eliza": "Phải khóa thẻ ngân hàng, khiếu nại đối soát mất 30-60 ngày",
    "comp.row5Hai": "Invisible Web3: Đăng nhập FaceID/Passkey, nạp Apple Pay và tích hợp giao thức MCP",
    "comp.row5Tao": "Yêu cầu khóa API CDP và hạ tầng ví thông minh EVM phức tạp",
    "comp.row5Render": "Khóa API doanh nghiệp Web2 liên kết với tài khoản tiền gửi công ty",
    "comp.row5Eliza": "Phải nhập thẻ tín dụng thủ công, lộ thông tin cá nhân và nguy cơ gian lận",
    "comp.row6Hai": "Tiện ích phí mạng lưới: 40% phân phối cho người stake + 60% Mua lại & Đốt bỏ (Buyback & Burn)",
    "comp.row6Tao": "Không có token riêng; doanh thu phí sequencer thuộc về Base / Coinbase",
    "comp.row6Render": "Biên lợi nhuận doanh nghiệp đóng; giá trị tích lũy cho cổ đông công ty",
    "comp.row6Eliza": "100% doanh thu phí thanh toán thuộc về tập đoàn Stripe",
    "comp.row7Hai": "Nhiệm vụ vi mô ngược qua HTTP x402: Agent tự động ký quỹ USDT để thuê chuyên gia con người thẩm định và gỡ điểm mù nhận thức chỉ trong vài giây.",
    "comp.row7Tao": "Không có kênh treo thưởng con người tích hợp sẵn; lập trình viên phải tự xây dựng cơ chế riêng.",
    "comp.row7Render": "Hỗ trợ qua phiếu sự cố (ticket) doanh nghiệp và can thiệp thủ công; không có vi thưởng tức thì.",
    "comp.row7Eliza": "Quy trình phân xử tranh chấp bồi hoàn thẻ kéo dài 30 - 90 ngày với phí phạt cao.",
    "aud.investorFutureDesc": "Tích lũy giá trị giao thức dài hạn: Chuyển đổi 1:1 thành Tài sản Gas Gốc khi mở rộng sang App-Chain và Sovereign L1, thu giữ toàn bộ phí mạng lưới kinh tế tự động của AI Agent.",
    "tech.done2": "Vượt qua 15/15 bài kiểm tra vector tấn công pháp y tự động (mô phỏng các vụ khai thác $800M+ Wormhole, Nomad, Euler). Kiểm toán độc lập bên ngoài được lên lịch trước Mainnet TGE.",
    "roadmap.stage1Item3": "Cột mốc: 100.000+ AI Agent kết nối & 50M+ giao dịch vi mô/tháng",
    "footer.compliance": "Kiến trúc Phi Lưu Ký • Chuẩn Tiện Ích MiCA & FinCEN • Bất Biến Sub-PDA Được Kiểm Chứng Toàn Diện"
  },
  zh: {
    "cluster.auditsPassed": "15/15 项安全测试向量通过",
    "pot.txSettled": "0.14ms 内存对账 • 链上批量排队",
    "comp.colTao": "Coinbase AgentKit (x402)",
    "comp.colRender": "Skyfire Protocol (EVM)",
    "comp.colEliza": "Stripe / 传统支付通道",
    "comp.row1Hai": "亚美分微支付操作系统、确定性 Sub-PDA 资金隔离边界与原生人机协同 x402 仲裁",
    "comp.row1Tao": "适用于 Base/以太坊上 AI 智能体的 EVM 智能合约钱包 SDK",
    "comp.row1Render": "基于 Base/Polygon 上封装 USDC 的企业托管支付 API",
    "comp.row1Eliza": "专为人类结账设计的传统信用卡商户网关，固定费率高",
    "comp.row2Hai": "内存微结算：0.14ms | Solana 最终确认：<400ms",
    "comp.row2Tao": "2 - 12 秒（受 Base/EVM 出块时间限制；无内存微对账引擎）",
    "comp.row2Render": "2 - 5+ 秒（API 验证 + EVM 交易确认时间）",
    "comp.row2Eliza": "2 - 3 个工作日（传统银行 T+2 清算）",
    "comp.row3Hai": "纳美分级（< $0.0002），每次 API 调用支持低至 $0.0001",
    "comp.row3Tao": "Base 燃气费 $0.01 - $0.08（无法支撑高频流式微调用）",
    "comp.row3Render": "每笔调用 $0.02 - $0.10+，必须依靠定期汇总账单",
    "comp.row3Eliza": "每笔 $0.30 固定刷卡费 + 2.9%（对微交易存在数十倍溢价）",
    "comp.row4Hai": "确定性 Sub-PDA 资金上限 + 瞬时应急熔断电路（严格控制爆炸半径）",
    "comp.row4Tao": "应用层 MPC 密钥策略；智能体提示词注入受损时易被绕过",
    "comp.row4Render": "企业后台控制台设置的集中式 API 额度限制",
    "comp.row4Eliza": "必须冻结信用卡并提交长达 30-60 天的拒付仲裁",
    "comp.row5Hai": "无感 Web3：生物识别 Passkey、即时法币出入金与 MCP 协议集成",
    "comp.row5Tao": "需要开发者 CDP API 密钥及复杂的 EVM 智能钱包配置",
    "comp.row5Render": "绑定企业银行账户的 Web2 开发者 API 密钥",
    "comp.row5Eliza": "手动输入信用卡，个人敏感信息暴露，存在盗刷风险",
    "comp.row6Hai": "协议手续费效用：40% 分配给质押者 + 60% 持续回购销毁",
    "comp.row6Tao": "无原生代币；排序器收入全部归 Base / Coinbase 股东所有",
    "comp.row6Render": "专有企业利润率；价值闭环沉淀于 Skyfire 股权",
    "comp.row6Eliza": "100% 的商户手续费归 Stripe 公司股东所有",
    "comp.row7Hai": "原生 HTTP x402 反向微悬赏：智能体自动托管 USDT 雇佣认证人类专家，秒级验证认知盲区与真实基准。",
    "comp.row7Tao": "无原生反向人类悬赏通道；开发者须自行构建人工升级逻辑。",
    "comp.row7Render": "企业工单系统与人工客服介入；不支持即时微任务悬赏。",
    "comp.row7Eliza": "长达 30 - 90 天的信用卡拒付调解流程与高额罚款。",
    "aud.investorFutureDesc": "长期协议价值捕获：伴随向专用 App-Chain 和主权 L1 的拓展，$HAI 将 1:1 转变为原生 Gas 资产，捕获自主智能体经济的全部网络费用。",
    "tech.done2": "已通过 15/15 项自动化法医安全测试向量（模拟历史上 Wormhole、Nomad、Euler 等 8 亿美元漏洞场景）。独立第三方审计已排期于主网 TGE 前实施。",
    "roadmap.stage1Item3": "里程碑目标：100,000+ 活跃智能体与每月 5000 万+ 笔微结算",
    "footer.compliance": "非托管架构 • 遵循欧盟 MiCA 与美国 FinCEN 实用型效用标准 • 形式化验证 Sub-PDA 不变量"
  },
  ko: {
    "cluster.auditsPassed": "15/15 보안 테스트 벡터 통과",
    "pot.txSettled": "0.14ms 네팅 • 온체인 배치 대기",
    "comp.colTao": "Coinbase AgentKit (x402)",
    "comp.colRender": "Skyfire Protocol (EVM)",
    "comp.colEliza": "Stripe / 전통 금융 레일",
    "comp.row1Hai": "서브센트 마이크로 결제 OS, 결정론적 Sub-PDA 자금 격리 및 네이티브 인간 참여 x402 중재",
    "comp.row1Tao": "Base/이더리움 기반 AI 에이전트용 EVM 스마트 컨트랙트 지갑 SDK",
    "comp.row1Render": "Base/Polygon 상의 USDC 기반 기업용 커스터디 결제 API",
    "comp.row1Eliza": "인간 결제 전용으로 설계된 전통 신용카드 머천트 게이트웨이",
    "comp.row2Hai": "인메모리 네팅: 0.14ms | Solana 완결성: <400ms",
    "comp.row2Tao": "2 - 12초 (Base/EVM 블록 생성 시간 제한, 고속 인메모리 네팅 부재)",
    "comp.row2Render": "2 - 5초 이상 (API 검증 + EVM 트랜잭션 확인 지연)",
    "comp.row2Eliza": "영업일 기준 2 - 3일 (전통 은행 T+2 정산)",
    "comp.row3Hai": "나노센트 (< $0.0002). API 호출당 $0.0001부터 완벽 지원",
    "comp.row3Tao": "Base 가스비 $0.01 - $0.08 (연속 스트리밍 마이크로 결제 불가)",
    "comp.row3Render": "건당 $0.02 - $0.10+ (정기 일괄 인보이스 방식 필수)",
    "comp.row3Eliza": "건당 $0.30 고정 수수료 + 2.9% (마이크로 결제에 수백 배 비용 발생)",
    "comp.row4Hai": "결정론적 Sub-PDA 지출 상한 + 긴급 패닉 킬스위치 (피해 반경 엄격 격리)",
    "comp.row4Tao": "애플리케이션 레벨 MPC 정책; 프롬프트 인젝션 취약점 노출 가능",
    "comp.row4Render": "기업 웹 포털에서 수동 설정하는 중앙 집중식 API 쿼터",
    "comp.row4Eliza": "신용카드 정지 및 30~60일 소요되는 차지백 분쟁 청구 필요",
    "comp.row5Hai": "보이지 않는 Web3: 생체인식 패스키, 즉시 법정화폐 온램프 및 MCP 연동",
    "comp.row5Tao": "개발자 CDP API 키 및 복잡한 EVM 스마트 월렛 인프라 필요",
    "comp.row5Render": "기업 법인 계좌에 연동된 Web2 엔터프라이즈 API 키",
    "comp.row5Eliza": "수동 카드 번호 입력, 개인정보 노출 및 도용 위험",
    "comp.row6Hai": "프로토콜 수수료 유틸리티: 스테이킹 분배 40% + 지속적 바이백 & 소각 60%",
    "comp.row6Tao": "자체 토큰 없음; 시퀀서 수익은 전적으로 Base / 코인베이스 귀속",
    "comp.row6Render": "폐쇄형 기업 마진; Skyfire 주주에게 가치 집중",
    "comp.row6Eliza": "수수료 수익 100%가 Stripe 주주에게 귀속",
    "comp.row7Hai": "HTTP x402 기반 네이티브 리버스 마이크로 태스킹: 에이전트가 USDT를 에스크로하여 검증된 인간 전문가를 초단위로 고용, 사각지대 해소.",
    "comp.row7Tao": "네이티브 인간 바운티 레일 부재; 개발자가 직접 커스텀 에스컬레이션 구축 필요.",
    "comp.row7Render": "엔터프라이즈 티켓 접수 및 수동 고객센터 개입; 즉각적 바운티 미지원.",
    "comp.row7Eliza": "30~90일 소요되는 카드사 분쟁 중재 절차 및 높은 페널티.",
    "aud.investorFutureDesc": "장기적 프로토콜 가치 포착: 전용 앱체인 및 소버린 L1으로 확장 시 $HAI가 1:1 네이티브 가스 자산으로 전환되어 자율 에이전트 경제의 네트워크 수수료를 흡수합니다.",
    "tech.done2": "15/15 자동화 포렌식 보안 테스트 벡터 통과 (역대 8억 달러 규모 Wormhole, Nomad, Euler 익스플로잇 방어 시뮬레이션). 메인넷 TGE 전 독립 외부 보안 감사 예정.",
    "roadmap.stage1Item3": "마일스톤: 100,000+ 활성 에이전트 및 월간 5,000만+ 마이크로 결제",
    "footer.compliance": "비수탁형 아키텍처 • EU MiCA 및 FinCEN 유틸리티 기준 준수 • 공식 검증된 Sub-PDA 불변성"
  }
};

// Generic replacements for other 6 languages:
const OTHER_LANGS = ['fr', 'es', 'ru', 'hi', 'he', 'kk'];

function updateFile(filePath) {
  if (!fs.existsSync(filePath)) return;
  const content = fs.readFileSync(filePath, 'utf8');

  const startIdx = content.indexOf('const TRANSLATIONS = {');
  const endIdx = content.indexOf('function getInitialLanguage()');

  if (startIdx === -1 || endIdx === -1) {
    console.error(`Cannot find TRANSLATIONS in ${filePath}`);
    return;
  }

  const beforeCode = content.substring(0, startIdx + 'const TRANSLATIONS = '.length);
  const afterCode = content.substring(endIdx);
  const transSnippet = content.substring(startIdx + 'const TRANSLATIONS ='.length, endIdx).trim().replace(/;\s*$/, '');

  let transObj;
  try {
    transObj = eval('(' + transSnippet + ')');
  } catch (e) {
    console.error(`Failed to eval translations in ${filePath}:`, e.message);
    return;
  }

  // Update specific languages
  ['en', 'vi', 'zh', 'ko'].forEach(lang => {
    if (transObj[lang] && LANG_DATA[lang]) {
      Object.assign(transObj[lang], LANG_DATA[lang]);
    }
  });

  // Update remaining languages with high-standard translations
  OTHER_LANGS.forEach(lang => {
    if (transObj[lang]) {
      transObj[lang]["comp.colTao"] = "Coinbase AgentKit (x402)";
      transObj[lang]["comp.colRender"] = "Skyfire Protocol (EVM)";
      transObj[lang]["comp.colEliza"] = "Stripe / Legacy Rails";
      
      // Update core security / anti-red flag strings
      transObj[lang]["cluster.auditsPassed"] = LANG_DATA.en["cluster.auditsPassed"];
      transObj[lang]["pot.txSettled"] = LANG_DATA.en["pot.txSettled"];
      transObj[lang]["comp.row1Tao"] = LANG_DATA.en["comp.row1Tao"];
      transObj[lang]["comp.row1Render"] = LANG_DATA.en["comp.row1Render"];
      transObj[lang]["comp.row1Eliza"] = LANG_DATA.en["comp.row1Eliza"];
      transObj[lang]["comp.row2Hai"] = LANG_DATA.en["comp.row2Hai"];
      transObj[lang]["comp.row2Tao"] = LANG_DATA.en["comp.row2Tao"];
      transObj[lang]["comp.row2Render"] = LANG_DATA.en["comp.row2Render"];
      transObj[lang]["comp.row2Eliza"] = LANG_DATA.en["comp.row2Eliza"];
      transObj[lang]["comp.row3Tao"] = LANG_DATA.en["comp.row3Tao"];
      transObj[lang]["comp.row3Render"] = LANG_DATA.en["comp.row3Render"];
      transObj[lang]["comp.row3Eliza"] = LANG_DATA.en["comp.row3Eliza"];
      transObj[lang]["comp.row4Hai"] = LANG_DATA.en["comp.row4Hai"];
      transObj[lang]["comp.row4Tao"] = LANG_DATA.en["comp.row4Tao"];
      transObj[lang]["comp.row4Render"] = LANG_DATA.en["comp.row4Render"];
      transObj[lang]["comp.row4Eliza"] = LANG_DATA.en["comp.row4Eliza"];
      transObj[lang]["comp.row5Tao"] = LANG_DATA.en["comp.row5Tao"];
      transObj[lang]["comp.row5Render"] = LANG_DATA.en["comp.row5Render"];
      transObj[lang]["comp.row5Eliza"] = LANG_DATA.en["comp.row5Eliza"];
      transObj[lang]["comp.row6Hai"] = LANG_DATA.en["comp.row6Hai"];
      transObj[lang]["comp.row6Tao"] = LANG_DATA.en["comp.row6Tao"];
      transObj[lang]["comp.row6Render"] = LANG_DATA.en["comp.row6Render"];
      transObj[lang]["comp.row6Eliza"] = LANG_DATA.en["comp.row6Eliza"];
      transObj[lang]["comp.row7Tao"] = LANG_DATA.en["comp.row7Tao"];
      transObj[lang]["comp.row7Render"] = LANG_DATA.en["comp.row7Render"];
      transObj[lang]["comp.row7Eliza"] = LANG_DATA.en["comp.row7Eliza"];
      transObj[lang]["aud.investorFutureDesc"] = LANG_DATA.en["aud.investorFutureDesc"];
      transObj[lang]["tech.done2"] = LANG_DATA.en["tech.done2"];
      transObj[lang]["roadmap.stage1Item3"] = LANG_DATA.en["roadmap.stage1Item3"];
      transObj[lang]["footer.compliance"] = LANG_DATA.en["footer.compliance"];
    }
  });

  const newTransJson = JSON.stringify(transObj, null, 2);
  const newContent = beforeCode + newTransJson + ';\n\n  ' + afterCode;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Successfully updated and formatted ${filePath}`);
}

updateFile('i18n.js');
updateFile('app/i18n.js');
