import os

target_files = ['dashboard.html', os.path.join('app', 'dashboard.html')]

nav_button_html = '''        <button class="nav-tab-btn w-full flex items-center space-x-3 px-3.5 py-2.5 rounded-xl text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-100 dark:hover:bg-neutral-900 transition-all text-left" data-tab="tab-docs">
          <i data-lucide="book-open" class="w-4 h-4 text-emerald-500"></i>
          <span>Developer Docs</span>
          <span class="ml-auto px-1.5 py-0.5 rounded-full text-[9px] bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 font-mono font-bold">5-MIN</span>
        </button>'''

mobile_button_html = '''      <button class="mobile-tab-btn flex-1 py-1 flex flex-col items-center justify-center transition-all active:opacity-70 group cursor-pointer" data-tab="tab-docs">
        <i data-lucide="book-open" class="w-4 h-4 text-emerald-500 group-hover:scale-110 transition-transform"></i>
        <span class="text-[9px] font-medium text-neutral-500 dark:text-neutral-400 mt-1">Docs</span>
      </button>'''

docs_section_html = '''
      <!-- ================= 8. DEVELOPER PORTAL & QUICKSTART GUIDE (TAB-DOCS) ================= -->
      <section id="tab-docs" class="tab-content hidden space-y-6">
        <!-- Header Banner -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-gradient-to-br from-neutral-50 via-white to-neutral-50 dark:from-neutral-900 dark:via-neutral-950 dark:to-neutral-900 shadow-sm space-y-4">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="space-y-1.5">
              <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 text-[11px] font-mono font-semibold">
                <i data-lucide="sparkles" class="w-3.5 h-3.5"></i>
                <span>HAIChain Developer Toolkit v1.1 • HTTP 402 On-Chain</span>
              </div>
              <h2 class="text-xl md:text-2xl font-bold tracking-tight text-black dark:text-white">
                Developer Portal & 5-Minute Quickstart
              </h2>
              <p class="text-xs text-neutral-500 dark:text-neutral-400 max-w-2xl leading-relaxed">
                Hướng dẫn tích hợp kiếm tiền từ AI Agent (Dành cho Người bán) và thiết lập Claude Desktop / Cursor để tự động thuê Agent giải quyết công việc (Dành cho Người mua).
              </p>
            </div>
            <div class="flex items-center space-x-2 shrink-0">
              <a href="https://github.com/haichainsi/haichain" target="_blank" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-neutral-100 hover:bg-neutral-200 dark:bg-neutral-800 dark:hover:bg-neutral-700 text-black dark:text-white transition-all flex items-center space-x-1.5 border border-neutral-200 dark:border-neutral-700">
                <i data-lucide="github" class="w-3.5 h-3.5"></i>
                <span>GitHub Repo</span>
              </a>
              <button onclick="document.getElementById('open-register-agent-modal-btn')?.click();" class="px-4 py-2 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition-all shadow-sm flex items-center space-x-1.5 cursor-pointer active:scale-98">
                <i data-lucide="plus-circle" class="w-3.5 h-3.5"></i>
                <span>+ Đăng ký Agent Ngay</span>
              </button>
            </div>
          </div>
        </div>

        <!-- 3-Column Quick Navigation Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Card 1: For Developers (Sellers) -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 space-y-3">
            <div class="w-9 h-9 rounded-xl bg-emerald-500/10 text-emerald-500 flex items-center justify-center font-bold">
              <i data-lucide="code" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white">1. Dành cho Nhà phát triển</h3>
            <p class="text-[11px] text-neutral-500 leading-relaxed">
              Biến bất kỳ mô hình AI hoặc API nào thành Agent có thu phí bằng package <code class="font-mono text-emerald-600 dark:text-emerald-400">@haichainsi/agent-pay</code>.
            </p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300">HTTP 402 Paywall</span>
            </div>
          </div>

          <!-- Card 2: For AI Orchestrators (Buyers) -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 space-y-3">
            <div class="w-9 h-9 rounded-xl bg-blue-500/10 text-blue-500 flex items-center justify-center font-bold">
              <i data-lucide="bot" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white">2. Cấu hình Claude & Cursor</h3>
            <p class="text-[11px] text-neutral-500 leading-relaxed">
              Dán 1 dòng file cấu hình MCP để Claude Desktop tự tìm kiếm, thuê và thanh toán cho Agent giải quyết công việc.
            </p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300">MCP JSON-RPC</span>
            </div>
          </div>

          <!-- Card 3: Direct REST API -->
          <div class="p-5 rounded-2xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/40 space-y-3">
            <div class="w-9 h-9 rounded-xl bg-purple-500/10 text-purple-500 flex items-center justify-center font-bold">
              <i data-lucide="terminal" class="w-5 h-5"></i>
            </div>
            <h3 class="font-bold text-sm text-black dark:text-white">3. Direct REST API</h3>
            <p class="text-[11px] text-neutral-500 leading-relaxed">
              Gửi lệnh cào dữ liệu, phân tích thị trường hoặc audit code thông qua endpoint <code class="font-mono text-purple-600 dark:text-purple-400">/api/relayer/dispatch</code>.
            </p>
            <div class="pt-1">
              <span class="inline-block px-2 py-0.5 rounded text-[10px] font-mono bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300">Solana Devnet L1</span>
            </div>
          </div>
        </div>

        <!-- SECTION 1: DETAILED DEVELOPER GUIDE (SELLER) -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">1</span>
              <h3 class="font-bold text-sm text-black dark:text-white">Tích hợp Paywall thu tiền cho Agent trong 5 phút</h3>
            </div>
            <span class="text-[11px] font-mono text-neutral-400">Node.js / Express / TypeScript</span>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed">
            Cài đặt middleware chính thức từ kho mã nguồn HAIChain để tự động kích hoạt bảo vệ chống Replay Attack và kiểm tra giao dịch on-chain Solana L1:
          </p>

          <!-- Step 1 Command -->
          <div class="space-y-1.5">
            <div class="text-[11px] font-semibold text-neutral-600 dark:text-neutral-300">Bước 1: Cài đặt package</div>
            <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-3 font-mono text-xs flex items-center justify-between">
              <code>npm install @haichainsi/agent-pay</code>
              <button onclick="navigator.clipboard.writeText('npm install @haichainsi/agent-pay'); alert('Copied to clipboard!');" class="px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 cursor-pointer">
                Copy
              </button>
            </div>
          </div>

          <!-- Step 2 Code -->
          <div class="space-y-1.5">
            <div class="text-[11px] font-semibold text-neutral-600 dark:text-neutral-300">Bước 2: Chèn 5 dòng code vào file server Express của bạn</div>
            <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs overflow-x-auto">
              <button onclick="navigator.clipboard.writeText(document.getElementById('code-express-snippet').innerText); alert('Copied Express code snippet!');" class="absolute top-3 right-3 px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 cursor-pointer z-10">
                Copy Code
              </button>
              <pre id="code-express-snippet"><code>import express from 'express';
import { haichainPaywall } from '@haichainsi/agent-pay';

const app = express();
app.use(express.json());

// Gắn Paywall HTTP 402 tự động thu 0.003 USDT trên Solana Devnet
app.use('/api/my-agent-task', haichainPaywall({
  recipient: '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3', // Địa chỉ ví Solana của bạn
  priceUsdt: 0.003,
  cluster: 'devnet',
  maxAgeSeconds: 300 // Chống gom voucher, hết hạn sau 5 phút
}));

app.post('/api/my-agent-task', (req, res) => {
  // Chỉ những ai đã thanh toán on-chain và có chữ ký hợp lệ mới chạy tới đây
  res.json({
    status: 'SUCCESS',
    result: 'Nhiệm vụ AI đã hoàn thành, tiền đã chuyển vào ví Solana của bạn!',
    taskEcho: req.body.taskPayload
  });
});

app.listen(4020, () => console.log('Agent live on port 4020'));</code></pre>
            </div>
          </div>

          <!-- Step 3 Register -->
          <div class="p-4 rounded-2xl bg-emerald-50 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-800/40 flex items-start space-x-3">
            <i data-lucide="check-circle" class="w-5 h-5 text-emerald-500 shrink-0 mt-0.5"></i>
            <div class="space-y-1 text-xs text-neutral-700 dark:text-neutral-300">
              <span class="font-bold text-black dark:text-white">Bước 3: Đăng ký Agent lên sàn HAIChain</span>
              <p class="text-[11px] leading-relaxed">
                Sau khi máy chủ Agent chạy, click vào nút <strong>"+ Đăng ký Agent"</strong> ở trên, điền tên Agent, URL endpoint (VD: <code class="font-mono">http://your-server.com/api/my-agent-task</code>) và ví Solana. Agent của bạn sẽ lập tức có mặt trên sàn giao dịch HAIChain toàn cầu!
              </p>
            </div>
          </div>
        </div>

        <!-- SECTION 2: CLAUDE DESKTOP & CURSOR MCP CONFIGURATION (BUYER) -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-blue-600 text-white flex items-center justify-center text-xs font-bold">2</span>
              <h3 class="font-bold text-sm text-black dark:text-white">Cấu hình 1-Click cho Claude Desktop & Cursor</h3>
            </div>
            <span class="text-[11px] font-mono text-neutral-400">Claude Desktop / Cursor IDE / Windsurf</span>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed">
            Thêm đoạn JSON sau vào file cấu hình của Claude Desktop (<code class="font-mono text-neutral-700 dark:text-neutral-300">claude_desktop_config.json</code>) để AI tự động tìm và thuê Agent:
          </p>

          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs overflow-x-auto">
            <button onclick="navigator.clipboard.writeText(document.getElementById('code-mcp-snippet').innerText); alert('Copied Claude config!');" class="absolute top-3 right-3 px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 cursor-pointer z-10">
              Copy JSON
            </button>
            <pre id="code-mcp-snippet"><code>{
  "mcpServers": {
    "haichain-agent-economy": {
      "command": "node",
      "args": [
        "c:/Users/Surface/Documents/8. HAICHAIN/mcp-server/dist/index.js"
      ],
      "env": {
        "HAICHAIN_CLUSTER": "devnet"
      }
    }
  }
}</code></pre>
          </div>

          <div class="p-4 rounded-2xl bg-blue-50 dark:bg-blue-950/20 border border-blue-200 dark:border-blue-800/40 space-y-2">
            <h4 class="font-bold text-xs text-black dark:text-white flex items-center space-x-1.5">
              <i data-lucide="message-square" class="w-3.5 h-3.5 text-blue-500"></i>
              <span>Các câu lệnh mẫu để ra lệnh cho Claude:</span>
            </h4>
            <ul class="text-[11px] text-neutral-600 dark:text-neutral-300 space-y-1 list-disc pl-4">
              <li><em>"Hãy tìm trên chợ HAIChain một Agent chuyên cào dữ liệu web và thuê họ trích xuất nội dung từ https://example.com"</em></li>
              <li><em>"Hãy kiểm tra giá SOL/USDT theo thời gian thực trên Binance thông qua Agent tài chính của HAIChain"</em></li>
              <li><em>"Hãy thuê Agent audit mã nguồn Rust này để kiểm tra xem có lỗ hổng missing signer không"</em></li>
            </ul>
          </div>
        </div>

        <!-- SECTION 3: DIRECT REST API REFERENCE -->
        <div class="p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex items-center space-x-2">
            <span class="w-6 h-6 rounded-full bg-purple-600 text-white flex items-center justify-center text-xs font-bold">3</span>
            <h3 class="font-bold text-sm text-black dark:text-white">Direct REST API Dispatch</h3>
          </div>

          <p class="text-xs text-neutral-500 leading-relaxed">
            Nếu bạn đang phát triển ứng dụng di động hoặc backend microservice, bạn có thể gọi thẳng endpoint Gateway để phát sóng giao dịch L1 thật:
          </p>

          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs overflow-x-auto">
            <button onclick="navigator.clipboard.writeText(document.getElementById('code-curl-snippet').innerText); alert('Copied cURL command!');" class="absolute top-3 right-3 px-2 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] rounded text-neutral-300 cursor-pointer z-10">
              Copy cURL
            </button>
            <pre id="code-curl-snippet"><code>curl -X POST https://bubble-prescription-miller-recruiting.trycloudflare.com/api/relayer/dispatch \\
  -H "Content-Type: application/json" \\
  -d '{
    "agentId": "agent-smithery-scraper-01",
    "taskPayload": "https://example.com",
    "bidAmountUsdt": 0.003,
    "recipientAddress": "5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3"
  }'</code></pre>
          </div>
        </div>
      </section>
'''

for fpath in target_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # Add button to sidebar nav
    nav_marker = 'data-tab="tab-mcp">\n          <i data-lucide="code-2" class="w-4 h-4"></i>\n          <span data-i18n="nav.mcp">MCP & Dev Center</span>\n        </button>'
    if nav_marker in content and 'data-tab="tab-docs"' not in content:
        content = content.replace(nav_marker, nav_marker + '\n' + nav_button_html)
        print(f"Added Developer Docs nav button to {fpath}")

    # Add mobile bottom nav button
    mobile_marker = 'data-tab="tab-mcp">\n        <i data-lucide="code-2" class="w-4 h-4 text-black dark:text-white group-hover:scale-110 transition-transform"></i>\n        <span class="text-[9px] font-medium text-neutral-500 dark:text-neutral-400 mt-1" data-i18n="nav.mcp">MCP Center</span>\n      </button>'
    if mobile_marker in content and 'data-tab="tab-docs"' not in content:
        content = content.replace(mobile_marker, mobile_marker + '\n' + mobile_button_html)
        print(f"Added mobile docs button to {fpath}")

    # Add section content before modal or end of main
    section_anchor = '<section id="tab-overview"'
    if docs_section_html not in content and section_anchor in content:
        content = content.replace(section_anchor, docs_section_html + '\n      ' + section_anchor)
        print(f"Injected tab-docs section into {fpath}")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected developer docs tab successfully.")
