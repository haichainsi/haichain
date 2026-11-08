import re, time

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's inspect current agentic-shift and haichain-advantages
s1 = c.find('id="agentic-shift"')
s2 = c.find('id="haichain-advantages"')
s3 = c.find('id="market-evidence"')

agentic_html = """  <!-- ======================== SECTION: AGENTIC SHIFT ======================== -->
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
        <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 mt-3 leading-relaxed font-light" data-i18n="agenticShift.subtitle">
          Từ OpenAI, Google, Stripe cho đến Coinbase đều xác định: 2023 - 2024 là thời kỳ AI trò chuyện (Chatbot), nhưng từ 2026 trở đi là kỷ nguyên AI tự hành động (AI Agent). Và một khi AI hành động, nó bắt buộc phải có tiền.
        </p>
      </div>

      <!-- 3 Columns: Minimalist, unboxed, airy -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5 lg:gap-6">
        <!-- Stripe -->
        <div class="p-5 sm:p-6 rounded-2xl bg-neutral-50/60 dark:bg-neutral-900/40 border border-neutral-200/70 dark:border-neutral-800/70 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors">
          <div class="flex items-center space-x-2.5 mb-2.5">
            <i data-lucide="credit-card" class="w-4 h-4 text-neutral-900 dark:text-white shrink-0"></i>
            <h3 class="text-sm sm:text-base font-semibold text-neutral-950 dark:text-white tracking-tight" data-i18n="agenticShift.card1Title">
              Stripe (Mỹ)
            </h3>
          </div>
          <p class="text-xs text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="agenticShift.card1Desc">
            Thành lập bộ phận riêng nghiên cứu "Agentic Commerce" — xây dựng hạ tầng thanh toán chuyên biệt cho AI tự giao dịch.
          </p>
        </div>

        <!-- Coinbase -->
        <div class="p-5 sm:p-6 rounded-2xl bg-neutral-50/60 dark:bg-neutral-900/40 border border-neutral-200/70 dark:border-neutral-800/70 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors">
          <div class="flex items-center space-x-2.5 mb-2.5">
            <i data-lucide="wallet" class="w-4 h-4 text-neutral-900 dark:text-white shrink-0"></i>
            <h3 class="text-sm sm:text-base font-semibold text-neutral-950 dark:text-white tracking-tight" data-i18n="agenticShift.card2Title">
              Coinbase (Mỹ)
            </h3>
          </div>
          <p class="text-xs text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="agenticShift.card2Desc">
            CEO Brian Armstrong kêu gọi: "Hãy cấp ví tiền cho AI, tương lai là máy móc tự thanh toán với nhau trên chuỗi".
          </p>
        </div>

        <!-- Venture Backed -->
        <div class="p-5 sm:p-6 rounded-2xl bg-neutral-50/60 dark:bg-neutral-900/40 border border-neutral-200/70 dark:border-neutral-800/70 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors">
          <div class="flex items-center space-x-2.5 mb-2.5">
            <i data-lucide="trending-up" class="w-4 h-4 text-neutral-900 dark:text-white shrink-0"></i>
            <h3 class="text-sm sm:text-base font-semibold text-neutral-950 dark:text-white tracking-tight" data-i18n="agenticShift.card3Title">
              Các Quỹ Đầu Tư Lớn
            </h3>
          </div>
          <p class="text-xs text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="agenticShift.card3Desc">
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
        <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 mt-3 leading-relaxed font-light" data-i18n="advantages.subtitle">
          Hầu hết các dự án trên thế giới hiện nay chỉ mới là ý tưởng trên giấy hoặc làm theo lối mòn cũ. HAICHAIN tạo ra 4 sự khác biệt mang tính sống còn:
        </p>
      </div>

      <!-- 4 Refined Items: Clean, unboxed typography -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-5 lg:gap-6">
        
        <!-- Pillar 1: Sub-Cent Micro-Escrow -->
        <div class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-brand-card border border-neutral-200/80 dark:border-neutral-800/80 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors flex flex-col justify-between">
          <div>
            <div class="flex items-start space-x-2.5 mb-2.5">
              <i data-lucide="zap" class="w-4 h-4 text-neutral-950 dark:text-white shrink-0 mt-0.5"></i>
              <h3 class="text-sm sm:text-base font-bold text-neutral-950 dark:text-white tracking-tight" data-i18n="advantages.item1Title">
                Thanh toán siêu nhỏ (Dưới 1 xu Mỹ) với 0% Phí
              </h3>
            </div>
            <div class="space-y-2.5 font-sans text-xs leading-relaxed">
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
        <div class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-brand-card border border-neutral-200/80 dark:border-neutral-800/80 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors flex flex-col justify-between">
          <div>
            <div class="flex items-start space-x-2.5 mb-2.5">
              <i data-lucide="shield-alert" class="w-4 h-4 text-neutral-950 dark:text-white shrink-0 mt-0.5"></i>
              <h3 class="text-sm sm:text-base font-bold text-neutral-950 dark:text-white tracking-tight" data-i18n="advantages.item2Title">
                Cầu dao an toàn 380ms (Chống hack & cạn ví)
              </h3>
            </div>
            <div class="space-y-2.5 font-sans text-xs leading-relaxed">
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
        <div class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-brand-card border border-neutral-200/80 dark:border-neutral-800/80 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors flex flex-col justify-between">
          <div>
            <div class="flex items-start space-x-2.5 mb-2.5">
              <i data-lucide="smartphone" class="w-4 h-4 text-neutral-950 dark:text-white shrink-0 mt-0.5"></i>
              <h3 class="text-sm sm:text-base font-bold text-neutral-950 dark:text-white tracking-tight" data-i18n="advantages.item3Title">
                Cực kỳ đơn giản cho người dùng (Chuẩn MCP Claude)
              </h3>
            </div>
            <div class="space-y-2.5 font-sans text-xs leading-relaxed">
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
        <div class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-brand-card border border-neutral-200/80 dark:border-neutral-800/80 hover:border-neutral-400 dark:hover:border-neutral-600 transition-colors flex flex-col justify-between">
          <div>
            <div class="flex items-start space-x-2.5 mb-2.5">
              <i data-lucide="file-check-2" class="w-4 h-4 text-neutral-950 dark:text-white shrink-0 mt-0.5"></i>
              <h3 class="text-sm sm:text-base font-bold text-neutral-950 dark:text-white tracking-tight" data-i18n="advantages.item4Title">
                Minh bạch 100% trên Blockchain (Không thể gian lận)
              </h3>
            </div>
            <div class="space-y-2.5 font-sans text-xs leading-relaxed">
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

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    s_start = content.find('<!-- ======================== SECTION: AGENTIC SHIFT ======================== -->')
    if s_start == -1:
        s_start = content.find('<section id="agentic-shift"')
    s_end = content.find('<!-- ======================== SECTION: MARKET PROOF & DATA ======================== -->')
    if s_end == -1:
        s_end = content.find('<section id="market-evidence"')

    assert s_start != -1 and s_end != -1, f"Markers not found in {path}"
    new_content = content[:s_start] + agentic_html + content[s_end:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {path}")

update_file('index.html')
update_file('app/index.html')

# Bump cachebuster
ts = int(time.time() * 1000)
new_ver = f"?v=v37_exact_small_text_{ts}"

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

print("Sync complete!")
