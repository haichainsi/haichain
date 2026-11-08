import sys
sys.stdout.reconfigure(encoding='utf-8')

def build_luxury_bw_modal():
    return '''<!-- UNIFIED MASTER AI INTEGRATION MODAL (PREMIUM LUXURY MONOCHROME: BLACK & WHITE) -->
  <div id="ai-hub-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-xl hidden flex items-end sm:items-center justify-center p-0 sm:p-4 transition-all duration-300">
    <div class="w-full sm:max-w-xl rounded-t-[28px] sm:rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-[#080808] p-4 sm:p-6 shadow-2xl relative max-h-[88vh] sm:max-h-[92vh] overflow-y-auto no-scrollbar animate-fadeIn flex flex-col">
      
      <!-- Mobile Pull Bar Indicator -->
      <div class="sm:hidden w-12 h-1 bg-neutral-300 dark:bg-neutral-800 rounded-full mx-auto mb-3 shrink-0"></div>
      
      <!-- Modal Header -->
      <div class="flex justify-between items-center pb-3 border-b border-neutral-200 dark:border-neutral-800/80 shrink-0">
        <div class="flex items-center space-x-3 min-w-0">
          <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-sm shrink-0 shadow-sm">
            <i data-lucide="bot" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <div class="flex items-center space-x-2">
              <h3 class="font-bold text-sm sm:text-base text-black dark:text-white tracking-tight truncate">Kết nối HAICHAIN với AI</h3>
              <span class="px-2 py-0.5 text-[9px] font-mono rounded-full bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-300 border border-neutral-300 dark:border-neutral-800 shrink-0 font-semibold uppercase tracking-wider">3 Lựa Chọn</span>
            </div>
            <p class="text-[10.5px] sm:text-[11.5px] text-neutral-500 truncate">Chọn cách kết nối phù hợp nhất với trải nghiệm của bạn</p>
          </div>
        </div>
        <button id="close-ai-hub-modal" type="button" class="w-9 h-9 rounded-full flex items-center justify-center text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-colors cursor-pointer shrink-0" title="Đóng">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <!-- 3 Main Segment Tabs (Monochrome Minimalist) -->
      <div class="my-3 flex p-1 bg-neutral-100 dark:bg-neutral-900/80 rounded-xl text-xs font-semibold shrink-0 gap-1 border border-neutral-200/50 dark:border-neutral-800/50">
        <button id="hub-tab-desktop" type="button" class="flex-1 py-2 sm:py-2.5 rounded-lg sm:rounded-xl bg-black text-white dark:bg-white dark:text-black shadow-xs text-center font-bold flex items-center justify-center space-x-1 sm:space-x-1.5 transition-all cursor-pointer text-[11px] sm:text-xs">
          <i data-lucide="laptop" class="w-3.5 h-3.5 shrink-0"></i>
          <span class="truncate">1. Desktop App</span>
        </button>
        <button id="hub-tab-online" type="button" class="flex-1 py-2 sm:py-2.5 rounded-lg sm:rounded-xl text-neutral-500 hover:text-black dark:hover:text-white text-center font-medium flex items-center justify-center space-x-1 sm:space-x-1.5 transition-all cursor-pointer text-[11px] sm:text-xs">
          <i data-lucide="globe" class="w-3.5 h-3.5 shrink-0"></i>
          <span class="truncate">2. Claude Online</span>
        </button>
        <button id="hub-tab-web" type="button" class="flex-1 py-2 sm:py-2.5 rounded-lg sm:rounded-xl text-neutral-500 hover:text-black dark:hover:text-white text-center font-medium flex items-center justify-center space-x-1 sm:space-x-1.5 transition-all cursor-pointer text-[11px] sm:text-xs">
          <i data-lucide="zap" class="w-3.5 h-3.5 shrink-0"></i>
          <span class="truncate">3. Web Direct</span>
        </button>
      </div>

      <!-- ================= TAB 1: CLAUDE DESKTOP & CURSOR (1-CLICK INSTALL) ================= -->
      <div id="hub-section-desktop" class="space-y-3 font-mono text-xs">
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="text-black dark:text-white font-sans font-bold text-xs flex items-center space-x-1.5">
              <i data-lucide="terminal" class="w-3.5 h-3.5 text-neutral-500"></i>
              <span>Cài đặt 1-Click Tự Động (Khuyên dùng)</span>
            </span>
            <span class="text-[9.5px] px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-black dark:text-white font-mono uppercase tracking-wider font-semibold">Tự Động 100%</span>
          </div>
          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">
            Dành cho máy tính đã cài <strong>Claude Desktop</strong> hoặc <strong>Cursor IDE</strong>. Tự động cấu hình MCP server và kết nối két chi tiêu on-chain.
          </p>
        </div>

        <!-- Terminal Command Box -->
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-950 border border-neutral-800 space-y-2">
          <div class="flex items-center justify-between text-[11px] text-neutral-400">
            <span class="flex items-center space-x-1.5 font-sans">
              <i data-lucide="terminal" class="w-3.5 h-3.5 text-neutral-300"></i>
              <span>Mở Terminal / PowerShell và chạy:</span>
            </span>
            <span class="text-[10px] bg-neutral-900 border border-neutral-800 px-2 py-0.5 rounded-full text-neutral-400 font-mono">v6.2.1</span>
          </div>
          <div class="p-2.5 rounded-xl bg-black border border-neutral-800 font-mono text-neutral-100 text-xs sm:text-[13px] overflow-x-auto select-all break-all flex items-center justify-between">
            <code id="cmd-install-snippet">npx -y @haichainsi/mcp-server --install</code>
          </div>
        </div>

        <button id="copy-desktop-install-btn" type="button" class="w-full py-3 px-4 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-bold text-xs sm:text-sm flex items-center justify-center space-x-2 shadow-sm transition-all active:scale-98 cursor-pointer">
          <i data-lucide="copy" class="w-4 h-4"></i>
          <span id="copy-desktop-install-text">Sao chép lệnh cài đặt 1-Click</span>
        </button>

        <!-- 3 Step Walkthrough -->
        <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200 dark:border-neutral-800 text-[11px] text-neutral-600 dark:text-neutral-300 space-y-2 font-sans">
          <div class="font-bold text-black dark:text-white flex items-center space-x-1.5 text-xs">
            <i data-lucide="check" class="w-3.5 h-3.5 text-neutral-400 shrink-0"></i>
            <span>3 bước kích hoạt:</span>
          </div>
          <div class="space-y-1.5 text-[10.5px] sm:text-[11px]">
            <div class="flex items-start space-x-2">
              <span class="w-4 h-4 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">1</span>
              <span>Sao chép lệnh trên và dán vào <strong>Terminal / PowerShell / Command Prompt</strong> rồi nhấn Enter.</span>
            </div>
            <div class="flex items-start space-x-2">
              <span class="w-4 h-4 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">2</span>
              <span>Khởi động lại ứng dụng <strong>Claude Desktop</strong>.</span>
            </div>
            <div class="flex items-start space-x-2">
              <span class="w-4 h-4 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">3</span>
              <span>Biểu tượng 🔨 Tools sẽ xuất hiện ở góc khung chat! Bạn chỉ cần gõ: <em>"Kiểm tra số dư két chi tiêu HAICHAIN"</em>.</span>
            </div>
          </div>
        </div>

        <!-- Optional Manual JSON Download -->
        <div class="pt-1 flex items-center justify-between text-[11px] text-neutral-500 font-sans">
          <span>Cấu hình thủ công qua file JSON?</span>
          <a href="/download/claude_desktop_config.json" download="claude_desktop_config.json" class="text-black dark:text-white hover:underline font-semibold flex items-center space-x-1">
            <span>Tải file .json</span>
            <i data-lucide="download" class="w-3 h-3"></i>
          </a>
        </div>
      </div>

      <!-- ================= TAB 2: CLAUDE.AI ONLINE (WEB / CLOUD CONNECTOR) ================= -->
      <div id="hub-section-online" class="hidden space-y-3 font-mono text-xs">
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="text-black dark:text-white font-sans font-bold text-xs flex items-center space-x-1.5">
              <i data-lucide="cloud" class="w-3.5 h-3.5 text-neutral-500"></i>
              <span>Remote MCP Server (SSE qua HTTPS)</span>
            </span>
            <span class="text-[9.5px] px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-black dark:text-white font-mono uppercase tracking-wider font-semibold">Đám Mây</span>
          </div>
          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">
            Dành cho người dùng chat trên web <strong>claude.ai</strong> trên trình duyệt (Chrome, Safari, Brave, Edge). Kết nối trực tiếp qua giao thức đám mây.
          </p>
        </div>

        <!-- Remote MCP URL Box -->
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-950 border border-neutral-800 space-y-2">
          <div class="flex items-center justify-between text-[11px] text-neutral-400">
            <span class="flex items-center space-x-1.5 font-sans">
              <i data-lucide="link" class="w-3.5 h-3.5 text-neutral-300"></i>
              <span>Đường dẫn Remote MCP Connector URL:</span>
            </span>
            <span class="text-[10px] bg-neutral-900 border border-neutral-800 px-2 py-0.5 rounded-full text-neutral-400 font-mono">SSE / HTTPS</span>
          </div>
          <div class="p-2.5 rounded-xl bg-black border border-neutral-800 font-mono text-neutral-100 text-xs sm:text-[13px] overflow-x-auto select-all break-all flex items-center justify-between">
            <code id="online-mcp-url-snippet">https://mcp.haichain.si/sse</code>
          </div>
        </div>

        <button id="copy-online-mcp-btn" type="button" class="w-full py-3 px-4 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-bold text-xs sm:text-sm flex items-center justify-center space-x-2 shadow-sm transition-all active:scale-98 cursor-pointer">
          <i data-lucide="copy" class="w-4 h-4"></i>
          <span id="copy-online-mcp-text">Sao chép đường dẫn Remote MCP</span>
        </button>

        <!-- 3 Step Guide for claude.ai online -->
        <div class="p-3 rounded-2xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200 dark:border-neutral-800 text-[11px] text-neutral-600 dark:text-neutral-300 space-y-2 font-sans">
          <div class="font-bold text-black dark:text-white flex items-center space-x-1.5 text-xs">
            <i data-lucide="info" class="w-3.5 h-3.5 text-neutral-400 shrink-0"></i>
            <span>Cách thiết lập trên claude.ai:</span>
          </div>
          <div class="space-y-1.5 text-[10.5px] sm:text-[11px]">
            <div class="flex items-start space-x-2">
              <span class="w-4 h-4 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">1</span>
              <span>Truy cập <strong>claude.ai</strong> và đăng nhập vào tài khoản của bạn.</span>
            </div>
            <div class="flex items-start space-x-2">
              <span class="w-4 h-4 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">2</span>
              <span>Bấm vào Avatar (góc dưới bên trái) ➔ Chọn <strong>Settings</strong> ➔ <strong>Developer / Connectors</strong>.</span>
            </div>
            <div class="flex items-start space-x-2">
              <span class="w-4 h-4 rounded-full bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">3</span>
              <span>Dán đường link <code class="font-bold text-black dark:text-white">https://mcp.haichain.si/sse</code> vào ô Server URL rồi bấm <strong>Connect</strong>.</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ================= TAB 3: WEB DASHBOARD DIRECT (INSTANT PLAYGROUND) ================= -->
      <div id="hub-section-web" class="hidden space-y-3 font-mono text-xs">
        <div class="p-3 sm:p-3.5 rounded-2xl bg-neutral-50 dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-1">
          <div class="flex items-center justify-between">
            <span class="text-black dark:text-white font-sans font-bold text-xs flex items-center space-x-1.5">
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-neutral-400"></i>
              <span>Trải nghiệm Trực tiếp trên Web</span>
            </span>
            <span class="text-[9.5px] px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-black dark:text-white font-mono uppercase tracking-wider font-semibold">Web3 Direct</span>
          </div>
          <p class="text-[11px] text-neutral-600 dark:text-neutral-400 font-sans leading-relaxed">
            Dành cho người dùng Web3 muốn gọi AI suy luận ngay trên trình duyệt mà không cần cài Claude hay sử dụng dòng lệnh.
          </p>
        </div>

        <!-- 3 Feature Badges (Monochrome Luxury) -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 font-sans text-center">
          <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/50 border border-neutral-200 dark:border-neutral-800">
            <span class="block text-[11px] font-bold text-black dark:text-white">Đa Mô Hình AI</span>
            <span class="text-[10px] text-neutral-500">Gemini, GPT-4o, Claude 3.5, DeepSeek</span>
          </div>
          <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/50 border border-neutral-200 dark:border-neutral-800">
            <span class="block text-[11px] font-bold text-black dark:text-white">Két Chi Tiêu Bảo Vệ</span>
            <span class="text-[10px] text-neutral-500">Khống chế ngân sách, an toàn vốn 100%</span>
          </div>
          <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/50 border border-neutral-200 dark:border-neutral-800">
            <span class="block text-[11px] font-bold text-black dark:text-white">Nút Khẩn Cấp Panic</span>
            <span class="text-[10px] text-neutral-500">Thu hồi toàn bộ tiền về ví trong 380ms</span>
          </div>
        </div>

        <!-- Big Launch CTA Button (Solid Monochrome) -->
        <button id="btn-open-web-playground" type="button" class="w-full py-3.5 px-4 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-bold text-xs sm:text-sm flex items-center justify-center space-x-2 shadow-sm active:scale-98 transition-all cursor-pointer">
          <i data-lucide="play" class="w-4 h-4 fill-current"></i>
          <span>Mở AI Playground Ngay Bây Giờ &rarr;</span>
        </button>

        <p class="text-center text-[10.5px] text-neutral-500 font-sans">
          Chỉ cần kết nối ví Phantom / Solflare hoặc nhập API key của riêng bạn (BYOK).
        </p>
      </div>

    </div>
  </div>'''

print("Length of luxury monochrome modal:", len(build_luxury_bw_modal()))
