import re

new_sections_html = """  <!-- ======================== SECTION: AGENTIC SHIFT ======================== -->
  <section id="agentic-shift" class="py-16 sm:py-20 border-b border-brand-lightBorder dark:border-brand-border bg-white dark:bg-black relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <div class="inline-flex items-center justify-center gap-1.5 sm:gap-2 px-3 py-1 sm:px-3.5 sm:py-1 rounded-full border border-neutral-300 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-[10px] sm:text-xs font-mono text-neutral-800 dark:text-neutral-200 mb-4 shadow-xs max-w-[94vw] sm:max-w-none mx-auto">
          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse shrink-0"></span>
          <span class="leading-tight sm:leading-normal text-center whitespace-normal" data-i18n="agenticShift.badge">LÀN SÓNG TOÀN CẦU &bull; KỶ NGUYÊN AI AGENT (2026+)</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-black dark:text-white" data-i18n="agenticShift.title">
          Cả thế giới công nghệ đều nhận ra: "AI Agent bắt buộc phải có tiền!"
        </h2>
        <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-400 mt-4 leading-relaxed font-light" data-i18n="agenticShift.subtitle">
          Cả thế giới công nghệ (từ OpenAI, Google, Stripe cho đến Coinbase) đều đã nhận ra một sự thật: &ldquo;Năm 2023 - 2024 là kỷ nguyên AI biết trò chuyện (Chatbot). Nhưng từ năm 2026 trở đi là kỷ nguyên AI biết tự hành động (AI Agent). Và một khi AI hành động, nó BẮT BUỘC phải có tiền!&rdquo;
        </p>
      </div>

      <!-- 3 Global Proof Pillars Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Stripe -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all group flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center text-black dark:text-white mb-6 group-hover:scale-105 transition-transform">
              <i data-lucide="credit-card" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="agenticShift.card1Title">
              Gã khổng lồ thanh toán Stripe (Mỹ)
            </h3>
            <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 mt-3 leading-relaxed font-sans" data-i18n="agenticShift.card1Desc">
              Vừa thành lập một bộ phận riêng nghiên cứu "Agentic Commerce" (Thương mại cho AI).
            </p>
          </div>
          <div class="pt-4 mt-6 border-t border-neutral-100 dark:border-neutral-800/80 flex items-center justify-between text-[11px] font-mono text-neutral-500">
            <span>Agentic Commerce</span>
            <span class="font-bold text-black dark:text-white">Silicon Valley, USA</span>
          </div>
        </div>

        <!-- Coinbase -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all group flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center text-black dark:text-white mb-6 group-hover:scale-105 transition-transform">
              <i data-lucide="wallet" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="agenticShift.card2Title">
              Sàn tiền mã hóa Coinbase (Mỹ)
            </h3>
            <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 mt-3 leading-relaxed font-sans" data-i18n="agenticShift.card2Desc">
              CEO Brian Armstrong vừa tuyên bố: "Các nhà phát triển hãy cấp ví tiền cho AI đi, tương lai là máy móc tự thanh toán với nhau".
            </p>
          </div>
          <div class="pt-4 mt-6 border-t border-neutral-100 dark:border-neutral-800/80 flex items-center justify-between text-[11px] font-mono text-neutral-500">
            <span>AI Crypto Wallets</span>
            <span class="font-bold text-black dark:text-white">Nasdaq: COIN</span>
          </div>
        </div>

        <!-- Mega Startups -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all group flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center text-black dark:text-white mb-6 group-hover:scale-105 transition-transform">
              <i data-lucide="trending-up" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="agenticShift.card3Title">
              Các Startup gọi vốn khủng
            </h3>
            <p class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 mt-3 leading-relaxed font-sans" data-i18n="agenticShift.card3Desc">
              Các công ty như Skyfire Systems hay Nevermined vừa huy động hàng chục triệu USD từ các quỹ lớn chỉ để giải quyết bài toán: Làm sao để AI có thể tự quẹt tiền?
            </p>
          </div>
          <div class="pt-4 mt-6 border-t border-neutral-100 dark:border-neutral-800/80 flex items-center justify-between text-[11px] font-mono text-neutral-500">
            <span>Venture Backed</span>
            <span class="font-bold text-black dark:text-white">Skyfire &bull; Nevermined</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================== SECTION: HAICHAIN ADVANTAGES ======================== -->
  <section id="haichain-advantages" class="py-16 sm:py-20 border-b border-brand-lightBorder dark:border-brand-border bg-neutral-50/70 dark:bg-neutral-950/70 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <div class="inline-flex items-center justify-center gap-1.5 sm:gap-2 px-3 py-1 sm:px-3.5 sm:py-1 rounded-full border border-neutral-300 dark:border-neutral-800 bg-white dark:bg-neutral-900 text-[10px] sm:text-xs font-mono text-neutral-800 dark:text-neutral-200 mb-4 shadow-xs max-w-[94vw] sm:max-w-none mx-auto">
          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse shrink-0"></span>
          <span class="leading-tight sm:leading-normal text-center whitespace-normal" data-i18n="advantages.badge">4 KHÁC BIỆT SỐNG CÒN &bull; CÔNG NGHỆ ĐỘT PHÁ</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-black dark:text-white" data-i18n="advantages.title">
          Vậy HAICHAIN có gì KHÁC BIỆT để vượt trội?
        </h2>
        <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-400 mt-4 leading-relaxed font-light" data-i18n="advantages.subtitle">
          Hầu hết các dự án trên thế giới hiện nay chỉ mới là ý tưởng trên giấy hoặc làm theo lối mòn cũ. HAICHAIN tạo ra 4 sự khác biệt mang tính sống còn:
        </p>
      </div>

      <!-- 4 Pillars Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Pillar 1: Sub-Cent Micro-Escrow -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all flex flex-col justify-between group space-y-4">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center text-black dark:text-white mb-6 group-hover:scale-105 transition-transform">
              <i data-lucide="zap" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="advantages.item1Title">
              1. Thanh toán siêu nhỏ (Dưới 1 xu Mỹ) với 0% Phí
            </h3>
          </div>
          <div class="space-y-3">
            <div class="p-4 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="advantages.item1Rival">
              <strong>Các đối thủ trên thế giới:</strong> Họ cố dùng thẻ tín dụng hoặc cổng thanh toán truyền thống. Nhưng thẻ Visa/Mastercard có phí tối thiểu là $0.30 + 2.9% cho mỗi giao dịch. Nếu con AI của bạn chỉ đọc 1 đoạn văn tốn $0.002, bạn không thể trả $0.30 tiền phí cho một việc giá $0.002 được (phí đắt gấp 150 lần giá trị công việc)!
            </div>
            <div class="p-4 rounded-2xl bg-neutral-100/80 dark:bg-neutral-800/60 border border-neutral-300 dark:border-neutral-700 text-xs sm:text-sm text-black dark:text-white leading-relaxed font-sans" data-i18n="advantages.item1Hai">
              <strong>HAICHAIN:</strong> Thiết kế riêng công nghệ Kênh thanh toán vi mô (State Channel) trên nền tảng Solana. Cho phép AI chi trả các khoản $0.001, $0.002 với <strong>0% phí trung gian</strong> và độ trễ chỉ <strong>160 mili-giây</strong> (nhanh hơn cái chớp mắt)!
            </div>
          </div>
        </div>

        <!-- Pillar 2: 380ms Emergency Circuit Breaker -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all flex flex-col justify-between group space-y-4">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center text-black dark:text-white mb-6 group-hover:scale-105 transition-transform">
              <i data-lucide="shield-alert" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="advantages.item2Title">
              2. Cầu dao an toàn 380ms (Chống mất tiền do AI bị hack)
            </h3>
          </div>
          <div class="space-y-3">
            <div class="p-4 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="advantages.item2Rival">
              <strong>Các đối thủ:</strong> Họ chỉ mải mê nghĩ cách "Làm sao cho AI tiêu tiền thật nhanh", mà quên mất bài toán an toàn: Lỡ con AI bị kẻ xấu lừa (Prompt Injection) hoặc bị lỗi lặp tiêu sạch tiền thì sao?
            </div>
            <div class="p-4 rounded-2xl bg-neutral-100/80 dark:bg-neutral-800/60 border border-neutral-300 dark:border-neutral-700 text-xs sm:text-sm text-black dark:text-white leading-relaxed font-sans" data-i18n="advantages.item2Hai">
              <strong>HAICHAIN:</strong> Đặt "Quyền kiểm soát của con người" lên số 1:<br>&bull; <strong>Hạn mức vận tốc (Velocity Cap):</strong> Khóa cứng tốc độ tiêu tiền (ví dụ không quá $0.50/phút).<br>&bull; <strong>Cầu dao ngắt khẩn cấp (Emergency Kill-Switch):</strong> Nếu thấy AI có dấu hiệu bất thường, bạn chỉ cần bấm 1 nút hoặc nhắn 1 tin, Hợp đồng thông minh sẽ đóng băng toàn bộ quỹ và rút tiền về túi bạn trong đúng <strong>380 mili-giây</strong>, không một ai có thể lấy cắp tiền của bạn.
            </div>
          </div>
        </div>

        <!-- Pillar 3: Ultra-Simple MCP Standard -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all flex flex-col justify-between group space-y-4">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center text-black dark:text-white mb-6 group-hover:scale-105 transition-transform">
              <i data-lucide="smartphone" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="advantages.item3Title">
              3. Cực kỳ đơn giản cho người dùng cuối (Chuẩn MCP của Claude)
            </h3>
          </div>
          <div class="space-y-3">
            <div class="p-4 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans" data-i18n="advantages.item3Rival">
              <strong>Các đối thủ:</strong> Bắt người dùng phải là lập trình viên giỏi, phải tự viết mã code, cấu hình máy chủ, tạo API phức tạp thì mới dùng được.
            </div>
            <div class="p-4 rounded-2xl bg-neutral-100/80 dark:bg-neutral-800/60 border border-neutral-300 dark:border-neutral-700 text-xs sm:text-sm text-black dark:text-white leading-relaxed font-sans" data-i18n="advantages.item3Hai">
              <strong>HAICHAIN:</strong> Tiên phong đón đầu chuẩn giao thức MCP (Model Context Protocol) mới nhất của công ty Anthropic (nhà sáng lập Claude).<br>👉 <strong>Người dùng bình thường không biết code chỉ cần copy 1 đường link dán vào app Claude trên điện thoại là xong trong 30 giây!</strong>
            </div>
          </div>
        </div>

        <!-- Pillar 4: Blockchain Transparency & Merkle Proof -->
        <div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm hover:border-black dark:hover:border-white transition-all flex flex-col justify-between group space-y-4">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center text-black dark:text-white mb-6 group-hover:scale-105 transition-transform">
              <i data-lucide="file-check-2" class="w-6 h-6"></i>
            </div>
            <h3 class="text-lg font-bold text-black dark:text-white tracking-tight" data-i18n="advantages.item4Title">
              4. Minh bạch tuyệt đối trên Blockchain (Không ai gian lận được)
            </h3>
          </div>
          <div class="space-y-3">
            <div class="p-5 rounded-2xl bg-neutral-100/80 dark:bg-neutral-800/60 border border-neutral-300 dark:border-neutral-700 text-xs sm:text-sm text-black dark:text-white leading-relaxed font-sans" data-i18n="advantages.item4Desc">
              Mọi khoản chi dù chỉ 1 phần nghìn cent đều có chứng thực mật mã độc lập (Merkle Proof) gắn liền với mạng lưới Solana. Doanh nghiệp khi kiểm toán cuối năm có thể mở sổ cái ra đối chiếu từng giao dịch một, minh bạch 100%, không bao giờ lo nhân viên hay AI gian lận báo khống chi phí.
            </div>
            <div class="p-4 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 flex items-center justify-between text-xs font-mono text-neutral-500">
              <span class="flex items-center space-x-2">
                <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>
                <span>Solana Cryptographic Anchor</span>
              </span>
              <span class="font-bold text-black dark:text-white">Merkle Root Verified</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

"""

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    s_start = c.find('<!-- ======================== SECTION: AGENTIC SHIFT ======================== -->')
    if s_start == -1:
        s_start = c.find('<section id="agentic-shift"')
    s_end = c.find('<!-- ======================== SECTION: MARKET PROOF & DATA ======================== -->')
    if s_end == -1:
        s_end = c.find('<section id="market-evidence"')

    assert s_start != -1, f"Start marker not found in {path}"
    assert s_end != -1, f"End marker not found in {path}"

    new_c = c[:s_start] + new_sections_html + c[s_end:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Successfully updated {path}")

update_file('index.html')
update_file('app/index.html')
