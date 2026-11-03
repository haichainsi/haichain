import json, re, time

STREAMLINED_SECTIONS_HTML = """  <!-- ======================== SECTION: AGENTIC SHIFT ======================== -->
  <section id="agentic-shift" class="py-14 sm:py-18 border-b border-brand-lightBorder dark:border-brand-border bg-white dark:bg-black relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-3xl mx-auto mb-10 sm:mb-14">
        <div class="inline-flex items-center justify-center gap-1.5 px-3 py-1 rounded-full border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-[10px] sm:text-xs font-mono text-neutral-700 dark:text-neutral-300 mb-4 max-w-[94vw] sm:max-w-none mx-auto">
          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse shrink-0"></span>
          <span data-i18n="agenticShift.badge">LÀN SÓNG TOÀN CẦU &bull; KỶ NGUYÊN AI AGENT (2026+)</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-neutral-950 dark:text-white" data-i18n="agenticShift.title">
          Cả thế giới công nghệ đều nhận ra: "AI Agent bắt buộc phải có tiền!"
        </h2>
        <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-400 mt-4 leading-relaxed font-light" data-i18n="agenticShift.subtitle">
          Từ OpenAI, Google, Stripe cho đến Coinbase đều xác định: 2023 - 2024 là thời kỳ AI trò chuyện (Chatbot), nhưng từ 2026 trở đi là kỷ nguyên AI tự hành động (AI Agent). Và một khi AI hành động, nó bắt buộc phải có tiền.
        </p>
      </div>

      <!-- 3 Columns: Minimalist, unboxed, airy -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5 lg:gap-6">
        <!-- Stripe -->
        <div class="p-6 sm:p-7 rounded-2xl bg-neutral-50/60 dark:bg-neutral-900/40 border border-neutral-200/70 dark:border-neutral-800/70 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors">
          <div class="flex items-center space-x-3 mb-3.5">
            <i data-lucide="credit-card" class="w-5 h-5 text-neutral-900 dark:text-white shrink-0"></i>
            <h3 class="text-base sm:text-lg font-semibold text-neutral-950 dark:text-white tracking-tight" data-i18n="agenticShift.card1Title">
              Stripe (Mỹ)
            </h3>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="agenticShift.card1Desc">
            Thành lập bộ phận riêng nghiên cứu "Agentic Commerce" - xây dựng hạ tầng thanh toán chuyên biệt cho AI tự giao dịch.
          </p>
        </div>

        <!-- Coinbase -->
        <div class="p-6 sm:p-7 rounded-2xl bg-neutral-50/60 dark:bg-neutral-900/40 border border-neutral-200/70 dark:border-neutral-800/70 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors">
          <div class="flex items-center space-x-3 mb-3.5">
            <i data-lucide="wallet" class="w-5 h-5 text-neutral-900 dark:text-white shrink-0"></i>
            <h3 class="text-base sm:text-lg font-semibold text-neutral-950 dark:text-white tracking-tight" data-i18n="agenticShift.card2Title">
              Coinbase (Mỹ)
            </h3>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="agenticShift.card2Desc">
            CEO Brian Armstrong kêu gọi: "Hãy cấp ví tiền cho AI, tương lai là máy móc tự thanh toán với nhau trên chuỗi".
          </p>
        </div>

        <!-- Venture Backed -->
        <div class="p-6 sm:p-7 rounded-2xl bg-neutral-50/60 dark:bg-neutral-900/40 border border-neutral-200/70 dark:border-neutral-800/70 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors">
          <div class="flex items-center space-x-3 mb-3.5">
            <i data-lucide="trending-up" class="w-5 h-5 text-neutral-900 dark:text-white shrink-0"></i>
            <h3 class="text-base sm:text-lg font-semibold text-neutral-950 dark:text-white tracking-tight" data-i18n="agenticShift.card3Title">
              Các Quỹ Đầu Tư Lớn
            </h3>
          </div>
          <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="agenticShift.card3Desc">
            Skyfire Systems, Nevermined huy động hàng chục triệu USD từ các quỹ mạo hiểm chỉ để giải bài toán AI tự thanh toán.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================== SECTION: HAICHAIN ADVANTAGES ======================== -->
  <section id="haichain-advantages" class="py-14 sm:py-18 border-b border-brand-lightBorder dark:border-brand-border bg-neutral-50/70 dark:bg-neutral-950/70 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-3xl mx-auto mb-10 sm:mb-14">
        <div class="inline-flex items-center justify-center gap-1.5 px-3 py-1 rounded-full border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-900 text-[10px] sm:text-xs font-mono text-neutral-700 dark:text-neutral-300 mb-4 max-w-[94vw] sm:max-w-none mx-auto">
          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse shrink-0"></span>
          <span data-i18n="advantages.badge">LỢI THẾ CỐT LÕI &bull; 4 ĐỘT PHÁ SỐNG CÒN</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-neutral-950 dark:text-white" data-i18n="advantages.title">
          Vậy HAICHAIN có gì KHÁC BIỆT để vượt trội?
        </h2>
        <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-400 mt-4 leading-relaxed font-light" data-i18n="advantages.subtitle">
          Hầu hết các dự án trên thế giới hiện nay chỉ mới là ý tưởng trên giấy hoặc làm theo lối mòn cũ. HAICHAIN tạo ra 4 sự khác biệt mang tính sống còn:
        </p>
      </div>

      <!-- 4 Refined Items: Clean, unboxed typography -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-5 lg:gap-6">
        
        <!-- Pillar 1: Sub-Cent Micro-Escrow -->
        <div class="p-6 sm:p-7 rounded-2xl bg-white dark:bg-brand-card border border-neutral-200/80 dark:border-neutral-800/80 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors flex flex-col justify-between">
          <div>
            <div class="flex items-start space-x-3 mb-3.5">
              <i data-lucide="zap" class="w-5 h-5 text-neutral-950 dark:text-white shrink-0 mt-0.5"></i>
              <h3 class="text-base sm:text-lg font-bold text-neutral-950 dark:text-white tracking-tight" data-i18n="advantages.item1Title">
                1. Thanh toán siêu nhỏ (Dưới 1 xu Mỹ) với 0% Phí
              </h3>
            </div>
            <div class="space-y-3 font-sans text-xs sm:text-sm leading-relaxed">
              <p class="text-neutral-500 dark:text-neutral-400" data-i18n="advantages.item1Rival">
                <strong>Các đối thủ:</strong> Dùng thẻ Visa/Mastercard với phí tối thiểu $0.30 + 2.9%. Tác vụ AI chỉ tốn $0.002 nhưng phí đắt gấp 150 lần giá trị công việc.
              </p>
              <p class="text-neutral-900 dark:text-neutral-100 font-medium" data-i18n="advantages.item1Hai">
                <strong>HAICHAIN:</strong> Kênh thanh toán vi mô (State Channel) trên Solana. AI chi trả $0.001 - $0.002 với 0% phí trung gian, độ trễ chỉ 160ms.
              </p>
            </div>
          </div>
        </div>

        <!-- Pillar 2: 380ms Emergency Circuit Breaker -->
        <div class="p-6 sm:p-7 rounded-2xl bg-white dark:bg-brand-card border border-neutral-200/80 dark:border-neutral-800/80 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors flex flex-col justify-between">
          <div>
            <div class="flex items-start space-x-3 mb-3.5">
              <i data-lucide="shield-alert" class="w-5 h-5 text-neutral-950 dark:text-white shrink-0 mt-0.5"></i>
              <h3 class="text-base sm:text-lg font-bold text-neutral-950 dark:text-white tracking-tight" data-i18n="advantages.item2Title">
                2. Cầu dao an toàn 380ms (Chống hack & cạn ví)
              </h3>
            </div>
            <div class="space-y-3 font-sans text-xs sm:text-sm leading-relaxed">
              <p class="text-neutral-500 dark:text-neutral-400" data-i18n="advantages.item2Rival">
                <strong>Các đối thủ:</strong> Chỉ tập trung chi tiêu mà thiếu phòng thủ Prompt Injection hoặc lỗi lặp tiêu cạn kiệt số dư ví.
              </p>
              <p class="text-neutral-900 dark:text-neutral-100 font-medium" data-i18n="advantages.item2Hai">
                <strong>HAICHAIN:</strong> Đặt con người nắm chủ quyền: Khóa hạn mức vận tốc (Velocity Cap) & Cầu dao ngắt khẩn cấp (Emergency Kill-Switch) thu hồi 100% quỹ về ví cá nhân trong 380 mili-giây.
              </p>
            </div>
          </div>
        </div>

        <!-- Pillar 3: Ultra-Simple MCP Standard -->
        <div class="p-6 sm:p-7 rounded-2xl bg-white dark:bg-brand-card border border-neutral-200/80 dark:border-neutral-800/80 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors flex flex-col justify-between">
          <div>
            <div class="flex items-start space-x-3 mb-3.5">
              <i data-lucide="smartphone" class="w-5 h-5 text-neutral-950 dark:text-white shrink-0 mt-0.5"></i>
              <h3 class="text-base sm:text-lg font-bold text-neutral-950 dark:text-white tracking-tight" data-i18n="advantages.item3Title">
                3. Cực kỳ đơn giản cho người dùng (Chuẩn MCP Claude)
              </h3>
            </div>
            <div class="space-y-3 font-sans text-xs sm:text-sm leading-relaxed">
              <p class="text-neutral-500 dark:text-neutral-400" data-i18n="advantages.item3Rival">
                <strong>Các đối thủ:</strong> Yêu cầu kiến thức lập trình phức tạp, tự dựng server, cấu hình API rắc rối.
              </p>
              <p class="text-neutral-900 dark:text-neutral-100 font-medium" data-i18n="advantages.item3Hai">
                <strong>HAICHAIN:</strong> Chuẩn giao thức MCP (Model Context Protocol) của Anthropic Claude. Người dùng không cần biết code, chỉ cần dán 1 đường link vào app Claude trên điện thoại là hoàn tất trong 30 giây.
              </p>
            </div>
          </div>
        </div>

        <!-- Pillar 4: Blockchain Transparency & Merkle Proof -->
        <div class="p-6 sm:p-7 rounded-2xl bg-white dark:bg-brand-card border border-neutral-200/80 dark:border-neutral-800/80 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors flex flex-col justify-between">
          <div>
            <div class="flex items-start space-x-3 mb-3.5">
              <i data-lucide="file-check-2" class="w-5 h-5 text-neutral-950 dark:text-white shrink-0 mt-0.5"></i>
              <h3 class="text-base sm:text-lg font-bold text-neutral-950 dark:text-white tracking-tight" data-i18n="advantages.item4Title">
                4. Minh bạch 100% trên Blockchain (Không thể gian lận)
              </h3>
            </div>
            <div class="space-y-3 font-sans text-xs sm:text-sm leading-relaxed">
              <p class="text-neutral-900 dark:text-neutral-100 font-medium" data-i18n="advantages.item4Desc">
                Mọi khoản chi dù chỉ 1 phần nghìn cent đều có chứng thực mật mã độc lập (Merkle Proof) neo trực tiếp trên Solana L1. Doanh nghiệp kiểm toán cuối năm mở sổ cái đối chiếu từng giao dịch tức thì, triệt tiêu hoàn toàn gian lận hay báo khống chi phí.
              </p>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

"""

REFINED_TRANSLATIONS = {
    "vi": {
        "agenticShift.badge": "LÀN SÓNG TOÀN CẦU • KỶ NGUYÊN AI AGENT (2026+)",
        "agenticShift.title": "Cả thế giới công nghệ đều nhận ra: \"AI Agent bắt buộc phải có tiền!\"",
        "agenticShift.subtitle": "Từ OpenAI, Google, Stripe cho đến Coinbase đều xác định: 2023 - 2024 là thời kỳ AI trò chuyện (Chatbot), nhưng từ 2026 trở đi là kỷ nguyên AI tự hành động (AI Agent). Và một khi AI hành động, nó bắt buộc phải có tiền.",
        "agenticShift.card1Title": "Stripe (Mỹ)",
        "agenticShift.card1Desc": "Thành lập bộ phận riêng nghiên cứu \"Agentic Commerce\" - xây dựng hạ tầng thanh toán chuyên biệt cho AI tự giao dịch.",
        "agenticShift.card2Title": "Coinbase (Mỹ)",
        "agenticShift.card2Desc": "CEO Brian Armstrong kêu gọi: \"Hãy cấp ví tiền cho AI, tương lai là máy móc tự thanh toán với nhau trên chuỗi\".",
        "agenticShift.card3Title": "Các Quỹ Đầu Tư Lớn",
        "agenticShift.card3Desc": "Skyfire Systems, Nevermined huy động hàng chục triệu USD từ các quỹ mạo hiểm chỉ để giải bài toán AI tự thanh toán.",
        "advantages.badge": "LỢI THẾ CỐT LÕI • 4 ĐỘT PHÁ SỐNG CÒN",
        "advantages.title": "Vậy HAICHAIN có gì KHÁC BIỆT để vượt trội?",
        "advantages.subtitle": "Hầu hết các dự án trên thế giới hiện nay chỉ mới là ý tưởng trên giấy hoặc làm theo lối mòn cũ. HAICHAIN tạo ra 4 sự khác biệt mang tính sống còn:",
        "advantages.item1Title": "1. Thanh toán siêu nhỏ (Dưới 1 xu Mỹ) với 0% Phí",
        "advantages.item1Rival": "<strong>Các đối thủ:</strong> Dùng thẻ Visa/Mastercard với phí tối thiểu $0.30 + 2.9%. Tác vụ AI chỉ tốn $0.002 nhưng phí đắt gấp 150 lần giá trị công việc.",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Kênh thanh toán vi mô (State Channel) trên Solana. AI chi trả $0.001 - $0.002 với 0% phí trung gian, độ trễ chỉ 160ms.",
        "advantages.item2Title": "2. Cầu dao an toàn 380ms (Chống hack & cạn ví)",
        "advantages.item2Rival": "<strong>Các đối thủ:</strong> Chỉ tập trung chi tiêu mà thiếu phòng thủ Prompt Injection hoặc lỗi lặp tiêu cạn kiệt số dư ví.",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> Đặt con người nắm chủ quyền: Khóa hạn mức vận tốc (Velocity Cap) & Cầu dao ngắt khẩn cấp (Emergency Kill-Switch) thu hồi 100% quỹ về ví cá nhân trong 380 mili-giây.",
        "advantages.item3Title": "3. Cực kỳ đơn giản cho người dùng (Chuẩn MCP Claude)",
        "advantages.item3Rival": "<strong>Các đối thủ:</strong> Yêu cầu kiến thức lập trình phức tạp, tự dựng server, cấu hình API rắc rối.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Chuẩn giao thức MCP (Model Context Protocol) của Anthropic Claude. Người dùng không cần biết code, chỉ cần dán 1 đường link vào app Claude trên điện thoại là hoàn tất trong 30 giây.",
        "advantages.item4Title": "4. Minh bạch 100% trên Blockchain (Không thể gian lận)",
        "advantages.item4Desc": "Mọi khoản chi dù chỉ 1 phần nghìn cent đều có chứng thực mật mã độc lập (Merkle Proof) neo trực tiếp trên Solana L1. Doanh nghiệp kiểm toán cuối năm mở sổ cái đối chiếu từng giao dịch tức thì, triệt tiêu hoàn toàn gian lận hay báo khống chi phí."
    },
    "en": {
        "agenticShift.badge": "GLOBAL AGENTIC SHIFT • 2026+ REALITY",
        "agenticShift.title": "The Tech World Realizes: \"AI Agents Must Have Money!\"",
        "agenticShift.subtitle": "From OpenAI and Google to Stripe and Coinbase, consensus is clear: 2023–2024 was conversational AI (Chatbots). 2026 onward is autonomous action (AI Agents). And autonomous action requires direct capital.",
        "agenticShift.card1Title": "Stripe (USA)",
        "agenticShift.card1Desc": "Established a dedicated Agentic Commerce unit to engineer autonomous payment rails for AI agents.",
        "agenticShift.card2Title": "Coinbase (USA)",
        "agenticShift.card2Desc": "CEO Brian Armstrong urges: \"Give AI agents crypto wallets. The future is machines paying machines on-chain.\"",
        "agenticShift.card3Title": "Tier-1 Venture Capital",
        "agenticShift.card3Desc": "Startups like Skyfire Systems and Nevermined raised tens of millions to solve agentic autonomous spending.",
        "advantages.badge": "CORE ADVANTAGES • 4 VITAL BREAKTHROUGHS",
        "advantages.title": "How Does HAICHAIN Truly Stand Apart?",
        "advantages.subtitle": "Most industry projects remain whitepaper theories or legacy wrappers. HAICHAIN engineers 4 vital architectural breakthroughs:",
        "advantages.item1Title": "1. Sub-Cent Micro-Escrow (<$0.01) with 0% Fee",
        "advantages.item1Rival": "<strong>Competitors:</strong> Force credit cards with $0.30 + 2.9% min fees. A $0.002 AI inference incurs 150x its value in transaction fees.",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Custom Solana State Channels settle $0.001–$0.002 micro-ticks with 0% intermediary fee and 160ms latency.",
        "advantages.item2Title": "2. 380ms Emergency Circuit Breaker (Anti-Drain)",
        "advantages.item2Rival": "<strong>Competitors:</strong> Focus on velocity without defense, leaving wallets vulnerable to Prompt Injections and runaway drain loops.",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> Human sovereign velocity caps & hardware-speed Emergency Kill-Switch recalling 100% of funds to safe storage in 380ms.",
        "advantages.item3Title": "3. Ultra-Simple for End Users (Claude MCP Standard)",
        "advantages.item3Rival": "<strong>Competitors:</strong> Demand heavy engineering skills, manual server hosting, and tedious API keys.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Native Anthropic Claude MCP standard. Zero coding required - paste a single link into Claude mobile in 30 seconds.",
        "advantages.item4Title": "4. 100% Cryptographic Ledger Transparency",
        "advantages.item4Desc": "Every fractional cent disbursement produces an independent cryptographic Merkle Proof anchored to Solana L1, enabling instant, tamper-proof corporate audits."
    },
    "zh": {
        "agenticShift.badge": "全球范式转移 • AI Agent 时代 (2026+)",
        "agenticShift.title": "全球科技巨头的共识：\"AI Agent 必须拥有自己的资金！\"",
        "agenticShift.subtitle": "从 OpenAI、Google 到 Stripe 与 Coinbase，共识已达成：2023-2024 年是对话式 AI（Chatbot），而 2026 年起是自主行动的 AI Agent。一旦 AI 开始执行任务，就必须拥有支付能力。",
        "agenticShift.card1Title": "Stripe（美国）",
        "agenticShift.card1Desc": "设立专属 Agentic Commerce 部门，为自主 AI 代理构建专用商业支付通道。",
        "agenticShift.card2Title": "Coinbase（美国）",
        "agenticShift.card2Desc": "CEO Brian Armstrong 呼吁：\"请为 AI 配置加密钱包，未来将是机器与机器在链上直接结算。\"",
        "agenticShift.card3Title": "顶级风险投资",
        "agenticShift.card3Desc": "Skyfire Systems、Nevermined 等初创公司从顶级机构筹集数千万美元，专注解决 AI 自动结算。",
        "advantages.badge": "核心竞争优势 • 4 项生死攸关的突破",
        "advantages.title": "HAICHAIN 究竟有何不同，凭何脱颖而出？",
        "advantages.subtitle": "业内多数项目仍停留在白皮书或沿袭旧模式。HAICHAIN 打造了 4 项至关重要的核心突破：",
        "advantages.item1Title": "1. 亚美分级微支付（<1 美分）0% 中介费",
        "advantages.item1Rival": "<strong>竞争对手：</strong>套用 Visa/Mastercard，单笔最低 $0.30 + 2.9%。$0.002 的 AI 调用中介费高达任务价值的 150 倍。",
        "advantages.item1Hai": "<strong>HAICHAIN：</strong>Solana 状态通道技术，实现 $0.001 - $0.002 毫厘结算，0% 中介费且延迟仅 160 毫秒。",
        "advantages.item2Title": "2. 380 毫秒硬件级紧急熔断（防提示词注入与清空钱包）",
        "advantages.item2Rival": "<strong>竞争对手：</strong>只顾让 AI 快速消费，缺乏防御 Prompt Injection 或死循环耗尽钱包的安全机制。",
        "advantages.item2Hai": "<strong>HAICHAIN：</strong>人类主权速率上限（Velocity Cap）与 380 毫秒紧急熔断，瞬间冻结并 100% 撤回资产。",
        "advantages.item3Title": "3. 终端用户极简体验（Claude MCP 标准）",
        "advantages.item3Rival": "<strong>竞争对手：</strong>要求用户具备复杂编程能力、自建服务器与繁琐的 API 配置。",
        "advantages.item3Hai": "<strong>HAICHAIN：</strong>原生支持 Anthropic Claude 的 MCP 协议。无需代码，手机 Claude 粘贴链接 30 秒立即可用。",
        "advantages.item4Title": "4. 区块链 100% 绝对透明（杜绝虚报欺诈）",
        "advantages.item4Desc": "每笔微额支出均生成独立默克尔证明（Merkle Proof）锚定 Solana L1，企业年终审计一键核对，杜绝虚假报销。"
    },
    "ko": {
        "agenticShift.badge": "글로벌 패러다임 전환 • AI 에이전트 시대 (2026+)",
        "agenticShift.title": "글로벌 테크 기업들의 공통 인식: \"AI 에이전트는 반드시 돈이 필요하다!\"",
        "agenticShift.subtitle": "OpenAI, Google부터 Stripe, Coinbase까지: 2023-2024년이 대화형 AI(Chatbot)였다면 2026년부터는 자율 행동 AI(AI Agent)의 시대입니다. 행동하는 AI는 독립적인 결제 자금이 필수적입니다.",
        "agenticShift.card1Title": "Stripe (미국)",
        "agenticShift.card1Desc": "'에이전틱 커머스' 전담 부서를 신설하여 AI 에이전트 전용 결제 인프라 구축.",
        "agenticShift.card2Title": "Coinbase (미국)",
        "agenticShift.card2Desc": "CEO 브라이언 암스트롱: \"AI에 암호화폐 지갑을 부여하십시오. 미래는 온체인 기계 간 자율 결제입니다.\"",
        "agenticShift.card3Title": "글로벌 벤처 캐피탈",
        "agenticShift.card3Desc": "Skyfire Systems, Nevermined 등 스타트업들이 AI 자율 결제 해결을 위해 수천만 달러 유치.",
        "advantages.badge": "핵심 경쟁 우위 • 4대 필수 생존 혁신",
        "advantages.title": "HAICHAIN은 무엇이 다르며 어떻게 압도하는가?",
        "advantages.subtitle": "대부분의 프로젝트는 백서에 머물러 있습니다. HAICHAIN은 4대 생존 핵심 차별화를 실현합니다:",
        "advantages.item1Title": "1. 1센트 미만 마이크로 결제 0% 수수료",
        "advantages.item1Rival": "<strong>경쟁사:</strong> 건당 최소 $0.30 + 2.9% 수수료의 신용카드 고집. $0.002 AI 추론에 작업 가치의 150배 수수료 발생.",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> 솔라나 기반 상태 채널. $0.001 - $0.002 결제를 0% 중개 수수료, 160ms 지연 속도로 정산.",
        "advantages.item2Title": "2. 380ms 긴급 차단기 (프롬프트 주입 및 자금 탈취 방지)",
        "advantages.item2Rival": "<strong>경쟁사:</strong> 보안 없이 소비에만 집중하여 프롬프트 인젝션이나 무한 루프 시 지갑 잔고가 바닥남.",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> 인간 주권 보장: 속도 한도(Velocity Cap) & 380ms 킬스위치로 이상 감지 시 자금 100% 즉시 회수.",
        "advantages.item3Title": "3. 최종 사용자를 위한 극상의 간편함 (Claude MCP 표준)",
        "advantages.item3Rival": "<strong>경쟁사:</strong> 사용자에게 복잡한 코딩, 서버 배포, 난해한 API 연동 강요.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Anthropic Claude MCP 공식 표준 채택. 코딩 없이 모바일 Claude 앱에 링크 복사-붙여넣기 30초 완료.",
        "advantages.item4Title": "4. 블록체인 기반 100% 완벽한 투명성",
        "advantages.item4Desc": "센트의 천분의 일 단위 지출까지 솔라나 L1 머클 증명(Merkle Proof) 생성, 기업 감사 시 즉각 대조 가능."
    },
    "fr": {
        "agenticShift.badge": "REVOLUTION AGENTIQUE • HORIZON 2026+",
        "agenticShift.title": "Le Monde Tech Réalise : \"Les Agents IA Doivent Avoir de l'Argent !\"",
        "agenticShift.subtitle": "D'OpenAI à Google, Stripe et Coinbase : 2023-2024 était l'ère conversationnelle. Dès 2026, l'ère est aux Agents IA autonomes, et tout agent autonome nécessite des capitaux pour agir.",
        "agenticShift.card1Title": "Stripe (USA)",
        "agenticShift.card1Desc": "Création d'une division dédiée à l'Agentic Commerce pour concevoir l'infrastructure de paiement autonome des IA.",
        "agenticShift.card2Title": "Coinbase (USA)",
        "agenticShift.card2Desc": "Brian Armstrong : \"Attribuez des portefeuilles crypto aux IA, le futur est aux machines qui se paient entre elles sur la chaîne.\"",
        "agenticShift.card3Title": "Grands Fonds VC",
        "agenticShift.card3Desc": "Des startups comme Skyfire Systems et Nevermined lèvent des dizaines de millions de dollars pour le paiement autonome par IA.",
        "advantages.badge": "AVANTAGES MAJEURS • 4 RUPTURES VITALES",
        "advantages.title": "En Quoi HAICHAIN Surpasse-t-il les Autres Projets ?",
        "advantages.subtitle": "La plupart des initiatives restent théoriques. HAICHAIN apporte 4 différenciations décisives :",
        "advantages.item1Title": "1. Micro-Paiements (<1 cent) à 0% de Commission",
        "advantages.item1Rival": "<strong>Concurrents :</strong> Dépendance Visa/Mastercard (frais min $0.30 + 2.9%). Pour une tâche à $0.002, les frais sont 150 fois supérieurs à la valeur.",
        "advantages.item1Hai": "<strong>HAICHAIN :</strong> State Channels dédiés sur Solana. Règlement de $0.001 à $0.002 avec 0% de frais intermédiaires en 160 millisecondes.",
        "advantages.item2Title": "2. Coupe-Circuit 380ms (Anti-Piratage & Siphonnage)",
        "advantages.item2Rival": "<strong>Concurrents :</strong> Négligent la sécurité contre les injections de prompts ou les boucles infinies vidant le solde.",
        "advantages.item2Hai": "<strong>HAICHAIN :</strong> Souveraineté humaine : Plafond de vélocité & Arrêt d'urgence rapatriant 100% des fonds en 380ms.",
        "advantages.item3Title": "3. Simplicité Maximale (Standard MCP Claude)",
        "advantages.item3Rival": "<strong>Concurrents :</strong> Exigent des compétences de programmation, la configuration de serveurs et d'API complexes.",
        "advantages.item3Hai": "<strong>HAICHAIN :</strong> Standard MCP officiel d'Anthropic Claude. Sans code, collez simplement un lien dans l'application Claude en 30 secondes.",
        "advantages.item4Title": "4. Transparence Blockchain Absolue (Inviolable)",
        "advantages.item4Desc": "Chaque fraction de centime bénéficie d'une preuve Merkle indépendante ancrée sur Solana L1, assurant un audit irréfutable."
    },
    "es": {
        "agenticShift.badge": "CAMBIO AGÉNTICO GLOBAL • REALIDAD 2026+",
        "agenticShift.title": "El Ecosistema Tecnológico lo Confirma: \"¡Los Agentes IA Necesitan Dinero!\"",
        "agenticShift.subtitle": "De OpenAI y Google a Stripe y Coinbase: 2023-2024 fue la era conversacional. A partir de 2026 es la era de la acción autónoma (AI Agents), y toda acción autónoma exige fondos inmediatos.",
        "agenticShift.card1Title": "Stripe (EE. UU.)",
        "agenticShift.card1Desc": "Creó una división dedicada a 'Agentic Commerce' para construir rieles de pago autónomos para agentes IA.",
        "agenticShift.card2Title": "Coinbase (EE. UU.)",
        "agenticShift.card2Desc": "Brian Armstrong: \"Den billeteras cripto a las IA; el futuro son máquinas pagándose mutuamente en cadena.\"",
        "agenticShift.card3Title": "Fondos de Capital Riesgo",
        "agenticShift.card3Desc": "Skyfire Systems y Nevermined levantaron decenas de millones para resolver el pago autónomo de agentes IA.",
        "advantages.badge": "VENTAJAS VITALES • 4 PILARES CRÍTICOS",
        "advantages.title": "¿Por Qué HAICHAIN Marca una Diferencia Superior?",
        "advantages.subtitle": "Frente a proyectos teóricos o convencionales, HAICHAIN crea 4 diferenciadores esenciales:",
        "advantages.item1Title": "1. Micropagos (<1 centavo) con 0% de Comisión",
        "advantages.item1Rival": "<strong>Rivales:</strong> Usan tarjetas bancarias con tarifa mínima de $0.30 + 2.9%. En una tarea de $0.002, la comisión es 150 veces mayor que el valor.",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Canales de estado en Solana. Liquida micro-pagos de $0.001 - $0.002 con 0% de intermediación en 160 milisegundos.",
        "advantages.item2Title": "2. Disyuntor de Emergencia 380ms (Anti-Drenaje)",
        "advantages.item2Rival": "<strong>Rivales:</strong> Ignoran riesgos de Prompt Injection o bucles que vacían la billetera por completo.",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> Control humano soberano: Límites de velocidad y Kill-Switch de emergencia que congela y rescata el 100% de fondos en 380ms.",
        "advantages.item3Title": "3. Simplicidad Radical (Estándar Claude MCP)",
        "advantages.item3Rival": "<strong>Rivales:</strong> Exigen conocimientos de programación, configuración de servidores y claves API complejas.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Protocolo MCP de Anthropic Claude. Sin código, solo pega un enlace en la app móvil de Claude en 30 segundos.",
        "advantages.item4Title": "4. Transparencia Blockchain Inalterable",
        "advantages.item4Desc": "Cada fracción de centavo genera una prueba criptográfica Merkle en Solana L1, garantizando auditorías corporativas 100% transparentes."
    },
    "ru": {
        "agenticShift.badge": "ГЛОБАЛЬНЫЙ СДВИГ • ЭРА ИИ-АГЕНТОВ (2026+)",
        "agenticShift.title": "Мировые IT-лидеры признали: \"ИИ-агентам необходимы деньги!\"",
        "agenticShift.subtitle": "От OpenAI и Google до Stripe и Coinbase: 2023-2024 были эрой чат-ботов. С 2026 года наступает эра автономных ИИ-агентов, а автономные действия требуют собственных платежных средств.",
        "agenticShift.card1Title": "Stripe (США)",
        "agenticShift.card1Desc": "Создал отдельное подразделение Agentic Commerce для разработки автономных платежных рельсов для ИИ.",
        "agenticShift.card2Title": "Coinbase (США)",
        "agenticShift.card2Desc": "Брайан Армстронг: \"Дайте ИИ криптокошельки. Будущее за взаимными расчетами машин на блокчейне\".",
        "agenticShift.card3Title": "Крупнейшие венчурные фонды",
        "agenticShift.card3Desc": "Стартапы вроде Skyfire Systems и Nevermined привлекли десятки миллионов долларов на решение задачи автономных платежей ИИ.",
        "advantages.badge": "КЛЮЧЕВЫЕ ПРЕИМУЩЕСТВА • 4 ЖИЗНЕННЫХ ПРОРЫВА",
        "advantages.title": "В чем фундаментальное превосходство HAICHAIN?",
        "advantages.subtitle": "Пока другие проекты остаются на бумаге, HAICHAIN реализует 4 решающих технологических прорыва:",
        "advantages.item1Title": "1. Микроплатежи (<1 цента) с 0% комиссии",
        "advantages.item1Rival": "<strong>Конкуренты:</strong> Используют карты Visa/Mastercard с комиссией $0.30 + 2.9%. Для задачи в $0.002 комиссия в 150 раз превышает ее стоимость.",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Каналы состояния на Solana. Платежи $0.001 - $0.002 с 0% комиссии посредников и задержкой всего 160 мс.",
        "advantages.item2Title": "2. Аварийный выключатель 380 мс (Защита от взлома)",
        "advantages.item2Rival": "<strong>Конкуренты:</strong> Забывают об уязвимостях Prompt Injection или цикличных сбоях, опустошающих баланс.",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> Полный контроль человека: лимиты скорости и Kill-Switch, возвращающий 100% средств на кошелек за 380 мс.",
        "advantages.item3Title": "3. Предельная простота (Стандарт Claude MCP)",
        "advantages.item3Rival": "<strong>Конкуренты:</strong> Требуют навыков программирования, настройки серверов и сложных API.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Официальный стандарт MCP от Anthropic Claude. Без кода - просто вставьте ссылку в приложение Claude за 30 секунд.",
        "advantages.item4Title": "4. 100% криптографическая прозрачность",
        "advantages.item4Desc": "Каждая доля цента подтверждается доказательством Меркла на Solana L1, обеспечивая мгновенный безошибочный аудит предприятия."
    },
    "hi": {
        "agenticShift.badge": "वैश्विक परिवर्तन • AI एजेंट युग (2026+)",
        "agenticShift.title": "तकनीकी दुनिया ने स्वीकार किया: \"AI एजेंटों के पास पैसा होना अनिवार्य है!\"",
        "agenticShift.subtitle": "OpenAI, Google से लेकर Stripe और Coinbase तक: 2023-2024 चैटबॉट्स का युग था। 2026 से AI एजेंटों का युग है, और स्वायत्त कार्यों के लिए सीधे पूंजी की आवश्यकता होती है।",
        "agenticShift.card1Title": "Stripe (यूएसए)",
        "agenticShift.card1Desc": "AI एजेंटों के लिए स्वायत्त भुगतान प्रणाली तैयार करने हेतु 'Agentic Commerce' प्रभाग की स्थापना।",
        "agenticShift.card2Title": "Coinbase (यूएसए)",
        "agenticShift.card2Desc": "ब्रायन आर्मस्ट्रांग: \"AI को क्रिप्टो वॉलेट दें, भविष्य मशीनों द्वारा ऑन-चेन भुगतान का है।\"",
        "agenticShift.card3Title": "शीर्ष वेंचर फंड्स",
        "agenticShift.card3Desc": "Skyfire Systems और Nevermined जैसे स्टार्टअप्स ने AI स्वायत्त भुगतान के लिए करोड़ों डॉलर जुटाए।",
        "advantages.badge": "मुख्य लाभ • 4 महत्वपूर्ण सफलताएँ",
        "advantages.title": "HAICHAIN किस प्रकार वास्तव में श्रेष्ठ और अलग है?",
        "advantages.subtitle": "जहाँ अधिकांश परियोजनाएँ केवल कागज़ पर हैं, HAICHAIN ने 4 महत्वपूर्ण अंतर निर्मित किए हैं:",
        "advantages.item1Title": "1. 1 सेंट से कम का माइक्रो-भुगतान 0% शुल्क पर",
        "advantages.item1Rival": "<strong>प्रतिद्वंद्वी:</strong> $0.30 + 2.9% न्यूनतम शुल्क वाले क्रेडिट कार्ड। $0.002 के AI कार्य पर 150 गुना अधिक शुल्क।",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Solana स्टेट चैनल। $0.001 - $0.002 का भुगतान 0% मध्यस्थ शुल्क और केवल 160ms लेटेंसी पर।",
        "advantages.item2Title": "2. 380ms आपातकालीन सर्किट ब्रेकर (सुरक्षा कवच)",
        "advantages.item2Rival": "<strong>प्रतिद्वंद्वी:</strong> सुरक्षा की अनदेखी, जिससे प्रॉम्प्ट इंजेक्शन या लूप एरर से पूरा वॉलेट खाली हो सकता है।",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> मानवीय संप्रभुता: वेलोसिटी कैप और 380ms आपातकालीन किल-स्विच से 100% फंड सुरक्षित वापसी।",
        "advantages.item3Title": "3. उपयोगकर्ताओं के लिए अत्यंत सरल (Claude MCP मानक)",
        "advantages.item3Rival": "<strong>प्रतिद्वंद्वी:</strong> कोडिंग ज्ञान, सर्वर कॉन्फ़िगरेशन और जटिल API की मांग।",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Anthropic Claude MCP मानक। बिना कोडिंग के 30 सेकंड में Claude ऐप में लिंक पेस्ट करके शुरू करें।",
        "advantages.item4Title": "4. ब्लॉकचेन पर 100% पूर्ण पारदर्शिता",
        "advantages.item4Desc": "प्रत्येक सूक्ष्म भुगतान Solana L1 पर मर्कल प्रूफ द्वारा सत्यापित होता है, जिससे किसी भी धोखे की संभावना समाप्त होती है।"
    },
    "he": {
        "agenticShift.badge": "תפנית גלובלית • עידן סוכני ה-AI (2026+)",
        "agenticShift.title": "עולם הטכנולוגיה מבין: \"סוכני AI חייבים כסף משלהם!\"",
        "agenticShift.subtitle": "מ-OpenAI וגוגל ועד Stripe ו-Coinbase: 2023-2024 היה עידן הצ'אטבוטים. מ-2026 ואילך מתחיל עידן סוכני ה-AI האוטונומיים, ופעולה אוטונומית מחייבת אמצעי תשלום עצמאיים.",
        "agenticShift.card1Title": "Stripe (ארה\"ב)",
        "agenticShift.card1Desc": "הקימה חטיבת 'Agentic Commerce' ייעודית לבניית תשתיות תשלום אוטונומיות עבור AI.",
        "agenticShift.card2Title": "Coinbase (ארה\"ב)",
        "agenticShift.card2Desc": "בריאן ארמסטרונג: \"תנו ל-AI ארנקי קריפטו, העתיד שייך למכונות שמשלמות למכונות על גבי הבלוקצ'יין\".",
        "agenticShift.card3Title": "קרנות הון סיכון מובילות",
        "agenticShift.card3Desc": "סטארטאפים כמו Skyfire Systems ו-Nevermined גייסו עשרות מיליוני דולרים לפתרון תשלומים אוטונומיים של AI.",
        "advantages.badge": "יתרונות ליבה • 4 פריצות דרך חיוניות",
        "advantages.title": "במה HAICHAIN שונה ומתעלה על כולם?",
        "advantages.subtitle": "בזמן שרוב הפרויקטים נשארים על הנייר, HAICHAIN יוצרת 4 יתרונות הישרדותיים מכריעים:",
        "advantages.item1Title": "1. מיקרו-תשלומים (פחות מסנט) ב-0% עמלה",
        "advantages.item1Rival": "<strong>המתחרים:</strong> מסתמכים על כרטיסי אשראי בעמלת מינימום של $0.30 + 2.9%. משימת AI של $0.002 נושאת עמלה יקרה פי 150 משווי העבודה.",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> ערוצי מצב ייעודיים על Solana. סליקת $0.001 - $0.002 ב-0% עמלות תיווך ובמהירות שיא של 160 מילי-שניות.",
        "advantages.item2Title": "2. מפסק ביטחון 380ms (הגנה מפני גניבה וריקון)",
        "advantages.item2Rival": "<strong>המתחרים:</strong> מתמקדים רק בהוצאות ללא הגנה מפני Prompt Injection או לולאות תקולות המרוקנות את הארנק.",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> שליטה אנושית מלאה: הגבלת קצב הוצאה ומתג חירום המחזיר 100% מהכספים לארנק תוך 380 מילי-שניות.",
        "advantages.item3Title": "3. פשטות מוחלטת למשתמש (תקן Claude MCP)",
        "advantages.item3Rival": "<strong>המתחרים:</strong> דורשים ידע בתכנות, הקמת שרתים והגדרות API מורכבות.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> תקן ה-MCP הרשמי של Claude Anthropic. ללא צורך בקוד, פשוט מדביקים קישור באפליקציית Claude תוך 30 שניות.",
        "advantages.item4Title": "4. שקיפות בלוקצ'יין מוחלטת של 100%",
        "advantages.item4Desc": "כל שבריר סנט מגובה בהוכחת מרקל עצמאית על גבי Solana L1, מה שמאפשר ביקורת חשבונאית מיידית ללא חשש מאי-סדרים."
    },
    "kk": {
        "agenticShift.badge": "ЖАҺАНДЫҚ ТҮБЕГЕЙЛІ БЕТБҰРЫС • AI АГЕНТТЕР ДӘУІРІ (2026+)",
        "agenticShift.title": "Әлемдік IT алпауыттары мойындады: \"AI агенттерге міндетті түрде ақша қажет!\"",
        "agenticShift.subtitle": "OpenAI, Google-ден бастап Stripe және Coinbase-ге дейін: 2023-2024 жылдар чат-боттар дәуірі болса, 2026 жылдан бастап дербес AI агенттер заманы басталады. Ал дербес әрекет ететін AI-ға қаржы құралдары қажет.",
        "agenticShift.card1Title": "Stripe (АҚШ)",
        "agenticShift.card1Desc": "AI агенттерінің автономды төлем жасауына арналған арнайы 'Agentic Commerce' бөлімін құрды.",
        "agenticShift.card2Title": "Coinbase (АҚШ)",
        "agenticShift.card2Desc": "Брайан Армстронг: \"AI-ға криптоәмиян беріңіздер, болашақ блокчейнде машиналардың бір-біріне төлем жасауында\".",
        "agenticShift.card3Title": "Ірі венчурлік қорлар",
        "agenticShift.card3Desc": "Skyfire Systems пен Nevermined стартаптары AI-дың дербес төлем жасау мәселесін шешу үшін ондаған миллион доллар тартты.",
        "advantages.badge": "НЕГІЗГІ АРТЫҚШЫЛЫҚТАР • 4 ӨМІРЛІК ТЕХНОЛОГИЯЛЫҚ СЕРПІЛІС",
        "advantages.title": "HAICHAIN-нің басты ЕРЕКШЕЛІГІ мен артықшылығы неде?",
        "advantages.subtitle": "Көптеген жобалар әлі де қағаз жүзінде қалып жатқанда, HAICHAIN 4 өмірлік серпіліс жасады:",
        "advantages.item1Title": "1. 0% комиссиямен 1 центтен төмен микротөлемдер",
        "advantages.item1Rival": "<strong>Бәсекелестер:</strong> $0.30 + 2.9% ең төменгі комиссиясы бар банк карталарын қолданады. $0.002 тұратын AI тапсырмасы үшін комиссия 150 есе қымбат.",
        "advantages.item1Hai": "<strong>HAICHAIN:</strong> Solana-дағы арнайы мемлекеттік арналар (State Channels). 0% комиссиямен және 160 мс жылдамдықпен $0.001 - $0.002 микротөлемдерді есептейді.",
        "advantages.item2Title": "2. 380 мс қауіпсіздік ажыратқышы (Әмиянды жылыстатудан қорғау)",
        "advantages.item2Rival": "<strong>Бәсекелестер:</strong> Қауіпсіздікті ескермейді, соның салдарынан Prompt Injection шабуылдары әмиянды босатып кетуі мүмкін.",
        "advantages.item2Hai": "<strong>HAICHAIN:</strong> Адамның толық бақылауы: шығыс шектеулері және 380 мс ішінде қаражатты 100% қайтаратын апаттық Kill-Switch жүйесі.",
        "advantages.item3Title": "3. Қолданушылар үшін өте қарапайым (Claude MCP стандарты)",
        "advantages.item3Rival": "<strong>Бәсекелестер:</strong> Бағдарламалау білімін, серверлерді баптауды және күрделі API кілттерін талап етеді.",
        "advantages.item3Hai": "<strong>HAICHAIN:</strong> Anthropic Claude компаниясының ресми MCP стандарты. Бағдарламалаусыз, 1 сілтемені Claude мобильді қосымшасына 30 секундта енгізіп іске қосуға болады.",
        "advantages.item4Title": "4. Блокчейндегі 100% толық ашықтық",
        "advantages.item4Desc": "Әрбір центтің мыңнан бір бөлігіне дейін Solana L1 желісінде криптографиялық Меркл дәлелімен (Merkle Proof) расталып, ашықтықты қамтамасыз етеді."
    }
}

# 1. Update HTML files
def update_html(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    s_start = c.find('<!-- ======================== SECTION: AGENTIC SHIFT ======================== -->')
    if s_start == -1:
        s_start = c.find('<section id="agentic-shift"')
    s_end = c.find('<!-- ======================== SECTION: MARKET PROOF & DATA ======================== -->')
    if s_end == -1:
        s_end = c.find('<section id="market-evidence"')

    assert s_start != -1 and s_end != -1, f"Markers not found in {path}"
    new_c = c[:s_start] + STREAMLINED_SECTIONS_HTML + c[s_end:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Updated HTML: {path}")

# 2. Update i18n files safely using line replacement
def update_i18n_safely(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    total = len(lines)
    while i < total:
        line = lines[i]
        matched_lang = None
        for lang in REFINED_TRANSLATIONS.keys():
            if line.strip() == f'"{lang}": {{' or line.strip() == f"'{lang}': {{":
                matched_lang = lang
                break

        if matched_lang:
            new_lines.append(line)
            i += 1
            # Check how many consecutive injected keys follow
            injected_count = 0
            temp_idx = i
            while temp_idx < total:
                l_str = lines[temp_idx].strip()
                if any(l_str.startswith(f'"{p}') for p in ['advantages.', 'agenticShift.']):
                    injected_count += 1
                    temp_idx += 1
                else:
                    break
            
            # Skip the old injected lines
            i += injected_count

            # Insert the new refined translations
            kvs = REFINED_TRANSLATIONS[matched_lang]
            for k, v in kvs.items():
                v_json = json.dumps(v, ensure_ascii=False)
                new_lines.append(f'    "{k}": {v_json},\n')
        else:
            new_lines.append(line)
            i += 1

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Safely updated i18n lines: {path}")

update_html('index.html')
update_html('app/index.html')

update_i18n_safely('i18n.js')
update_i18n_safely('app/i18n.js')

# 3. Bump cache
ts = int(time.time() * 1000)
new_ver = f"?v=v35_streamlined_unboxed_{ts}"

def bump_cache(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'i18n\.js(\?v=[a-zA-Z0-9_\.]*)?', f'i18n.js{new_ver}', c)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Bumped cache in {path}")

bump_cache('index.html')
bump_cache('app/index.html')
bump_cache('dashboard.html')
bump_cache('app/dashboard.html')

print("All tasks completed cleanly!")
