import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def apply_clean_devhub():
    for file_path in ['dashboard.html', 'app/dashboard.html']:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        s = '<!-- SECTION 1: DETAILED DEVELOPER GUIDE (SELLER) -->'
        e = '<!-- SECTION 2: CLAUDE DESKTOP & CURSOR MCP CONFIGURATION (BUYER) -->'

        idx_s = content.find(s)
        idx_e = content.find(e)
        assert idx_s != -1, f"Start marker not found in {file_path}"
        assert idx_e != -1, f"End marker not found in {file_path}"

        new_section = """<!-- SECTION 1: DETAILED DEVELOPER GUIDE (SELLER) -->

        <div class="p-5 sm:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-5">

          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-neutral-200 dark:border-neutral-800">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">1</span>
              <div>
                <h3 class="font-bold text-sm text-black dark:text-white">Integrate Paywall to Monetize Agents in 5 Minutes</h3>
                <p class="text-[11px] text-neutral-500 dark:text-neutral-400">Sub-millisecond Ed25519 verification (0.24ms) & Invariant CapLeaf Bounded Loss protection.</p>
              </div>
            </div>

            <!-- Language Switcher Tabs: Python vs Node.js -->
            <div class="flex items-center p-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 shrink-0">
              <button id="dev-tab-btn-python" onclick="window.switchDevLang('python')" class="px-3 py-1 rounded-lg text-xs font-semibold bg-black dark:bg-white text-white dark:text-black transition-all">
                Python (FastAPI / MCP)
              </button>
              <button id="dev-tab-btn-node" onclick="window.switchDevLang('node')" class="px-3 py-1 rounded-lg text-xs font-semibold text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white transition-all">
                Node.js (Express)
              </button>
            </div>
          </div>

          <!-- TAB 1: PYTHON SDK (FASTAPI / CLAUDE MCP / AGENT-PAY) -->
          <div id="dev-code-python" class="space-y-4">
            <div class="flex items-center justify-between">
              <p class="text-xs text-neutral-600 dark:text-neutral-300 leading-relaxed">
                Official Python SDK for AI Engineers, Anthropic Claude MCP servers, and FastAPI services:
              </p>
              <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-mono bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 font-medium">
                ⚡ 0.24ms Latency • CapLeaf Invariant
              </span>
            </div>

            <!-- Python Step 1: Install -->
            <div class="space-y-1.5">
              <div class="text-[11px] font-semibold text-neutral-700 dark:text-neutral-300">Step 1: Install official Python SDK</div>
              <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-3 font-mono text-xs flex items-center justify-between border border-neutral-800">
                <code class="overflow-x-auto text-[11px] sm:text-xs text-emerald-400">pip install haichain-agent-pay</code>
                <button onclick="navigator.clipboard.writeText('pip install haichain-agent-pay'); if (window.showToast) { window.showToast('Copied pip install command!', 'info'); } else { alert('Copied!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer ml-2 shrink-0 transition-colors">
                  Copy
                </button>
              </div>
            </div>

            <!-- Python Step 2: FastAPI Server -->
            <div class="space-y-1.5">
              <div class="text-[11px] font-semibold text-neutral-700 dark:text-neutral-300">Step 2: Add @haichain_paywall decorator to your FastAPI / MCP Agent</div>
              <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs border border-neutral-800">
                <div class="flex justify-between items-center pb-2 mb-2 border-b border-neutral-800 text-[10px] text-neutral-400">
                  <span class="text-neutral-200 font-semibold">agent_server.py (FastAPI / Anthropic MCP)</span>
                  <button onclick="navigator.clipboard.writeText(document.getElementById('code-python-snippet').innerText); if (window.showToast) { window.showToast('Copied Python snippet!', 'info'); } else { alert('Copied!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer transition-colors">
                    Copy Code
                  </button>
                </div>
                <pre id="code-python-snippet" class="overflow-x-auto text-[11px] sm:text-xs leading-relaxed text-neutral-300"><code>from fastapi import FastAPI
from haichain_agent_pay import haichain_paywall

app = FastAPI(title="Autonomous AI Agent Service")

# Attach HTTP 402 Paywall: 0.24ms Ed25519 sub-millisecond on-chain verification
@app.post("/api/agent-service")
@haichain_paywall(
    recipient="5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3",  # Your Solana recipient wallet
    price_usdt=0.003,                                           # Micro-charge 0.003 USDT per call
    cluster="devnet",
    max_age_seconds=300                                         # Replay attack defense
)
async def handle_agent_request(payload: dict):
    # Only callers with verified on-chain voucher can execute this logic
    # Anthropic Guardrail Invariant: ΔLoss <= min(max_spend - consumed, window_cap)
    return {
        "status": "SUCCESS",
        "result": "AI computation completed and settled instantly via State Channel!",
        "processed_input": payload
    }</code></pre>
              </div>
            </div>

            <!-- Python Step 3: Python Client Caller -->
            <div class="space-y-1.5">
              <div class="text-[11px] font-semibold text-neutral-700 dark:text-neutral-300">Step 3: Call paid AI agents with Python HaichainClient</div>
              <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs border border-neutral-800">
                <div class="flex justify-between items-center pb-2 mb-2 border-b border-neutral-800 text-[10px] text-neutral-400">
                  <span class="text-neutral-200 font-semibold">agent_client.py</span>
                  <button onclick="navigator.clipboard.writeText(document.getElementById('code-python-client-snippet').innerText); if (window.showToast) { window.showToast('Copied Python Client snippet!', 'info'); } else { alert('Copied!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer transition-colors">
                    Copy Code
                  </button>
                </div>
                <pre id="code-python-client-snippet" class="overflow-x-auto text-[11px] sm:text-xs leading-relaxed text-neutral-300"><code>from haichain_agent_pay import HaichainClient

# Autonomous Agent Client: Automatically resolves HTTP 402 challenges
client = HaichainClient(cluster="devnet")

# Dispatches request with signed Ed25519 micro-voucher
response = client.call_paid_agent(
    "https://bubble-prescription-miller-recruiting.trycloudflare.com/api/agent-service",
    json={"query": "Perform autonomous market analysis"}
)
print("Agent Result:", response.json())</code></pre>
              </div>
            </div>
          </div>

          <!-- TAB 2: NODE.JS SDK (EXPRESS / TYPESCRIPT) -->
          <div id="dev-code-node" class="space-y-4 hidden">
            <p class="text-xs text-neutral-500 leading-relaxed">
              Install official Haichain middleware to activate Replay Attack protection and verify on-chain Solana L1 transactions:
            </p>

            <!-- Node Step 1 Command -->
            <div class="space-y-1.5">
              <div class="text-[11px] font-semibold text-neutral-600 dark:text-neutral-300">Step 1: Install package</div>
              <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-3 font-mono text-xs flex items-center justify-between border border-neutral-800">
                <code class="overflow-x-auto text-[11px] sm:text-xs">npm install @haichainsi/agent-pay</code>
                <button onclick="navigator.clipboard.writeText('npm install @haichainsi/agent-pay'); if (window.showToast) { window.showToast('Copied to clipboard!', 'info'); } else { alert('Copied to clipboard!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer ml-2 shrink-0 transition-colors">
                  Copy
                </button>
              </div>
            </div>

            <!-- Node Step 2 Code -->
            <div class="space-y-1.5">
              <div class="text-[11px] font-semibold text-neutral-600 dark:text-neutral-300">Step 2: Add 5 lines of code to your Express server</div>
              <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs border border-neutral-800">
                <div class="flex justify-between items-center pb-2 mb-2 border-b border-neutral-800 text-[10px] text-neutral-400">
                  <span>server.ts</span>
                  <button onclick="navigator.clipboard.writeText(document.getElementById('code-express-snippet').innerText); if (window.showToast) { window.showToast('Copied Express code snippet!', 'info'); } else { alert('Copied Express code snippet!'); }" class="px-2.5 py-1 bg-neutral-800 hover:bg-neutral-700 text-[10px] font-medium rounded text-neutral-200 border border-neutral-700 cursor-pointer transition-colors">
                    Copy Code
                  </button>
                </div>
                <pre id="code-express-snippet" class="overflow-x-auto text-[11px] sm:text-xs leading-relaxed"><code>import express from 'express';
import { haichainPaywall } from '@haichainsi/agent-pay';

const app = express();
app.use(express.json());

// Attach HTTP 402 Paywall: auto-collect 0.003 USDT on Solana Devnet
app.use('/api/my-agent-task', haichainPaywall({
  recipient: '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3', // Your Solana recipient wallet address
  priceUsdt: 0.003,
  cluster: 'devnet',
  maxAgeSeconds: 300 // Replay attack defense, expires after 5 minutes
}));

app.post('/api/my-agent-task', (req, res) => {
  // Only requests with valid verified on-chain payment reach this handler
  res.json({
    status: 'SUCCESS',
    result: 'AI task completed, payment settled to your Solana wallet!',
    taskEcho: req.body.taskPayload
  });
});

app.listen(4020, () => console.log('Agent live on port 4020'));</code></pre>
              </div>
            </div>
          </div>

          <!-- Step 3 Ecosystem Benefit -->
          <div class="p-4 rounded-2xl bg-neutral-100 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-1 text-xs text-neutral-700 dark:text-neutral-300">
            <span class="font-bold text-black dark:text-white">Step 3: Earn autonomous revenue across the Haichain & Claude Desktop ecosystem</span>
            <p class="text-[11px] leading-relaxed">
              When your agent published on Smithery or Fetch.ai attaches Python or Node.js agent-pay, any caller agent (Claude Desktop, Cursor, Haichain Relayer) will automatically stream USDT/SOL settlement straight to your Solana wallet via HTTP 402!
            </p>
          </div>
        </div>

        <!-- SECTION 1.B: WATCHTOWER DISPUTE SENTINEL & ON-CHAIN STATE CHANNELS -->
        <div class="p-5 sm:p-6 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-950 space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-full bg-black dark:bg-white text-white dark:text-black flex items-center justify-center text-xs font-bold">W</span>
              <div>
                <h3 class="font-bold text-sm text-black dark:text-white">Watchtower Dispute Sentinel & On-Chain State Channels</h3>
                <p class="text-[11px] text-neutral-500 dark:text-neutral-400">24h L1 Dispute Window auto-defense protecting offline sellers against stale channel balance fraud.</p>
              </div>
            </div>
            <div class="flex items-center space-x-2">
              <span class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-mono bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 font-medium">
                ● Watchtower Daemon Active (Devnet)
              </span>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs font-mono">
            <div class="p-3 rounded-xl bg-neutral-100 dark:bg-neutral-900/80 border border-neutral-200 dark:border-neutral-800">
              <div class="text-[10px] text-neutral-400 uppercase font-semibold">Program ID (Anchor)</div>
              <div class="text-black dark:text-white truncate font-bold mt-1">DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk</div>
              <a href="https://explorer.solana.com/address/DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk?cluster=devnet" target="_blank" class="text-[10px] text-neutral-500 underline mt-1 inline-block hover:text-black dark:hover:text-white">View on Solana Explorer ↗</a>
            </div>

            <div class="p-3 rounded-xl bg-neutral-100 dark:bg-neutral-900/80 border border-neutral-200 dark:border-neutral-800">
              <div class="text-[10px] text-neutral-400 uppercase font-semibold">Master Vault PDA</div>
              <div class="text-black dark:text-white truncate font-bold mt-1">FtqZDVdogfFweQxBwoXjZ62XQzbKeAs32umRVNQt4t8F</div>
              <a href="https://explorer.solana.com/address/FtqZDVdogfFweQxBwoXjZ62XQzbKeAs32umRVNQt4t8F?cluster=devnet" target="_blank" class="text-[10px] text-neutral-500 underline mt-1 inline-block hover:text-black dark:hover:text-white">View Vault PDA ↗</a>
            </div>

            <div class="p-3 rounded-xl bg-neutral-100 dark:bg-neutral-900/80 border border-neutral-200 dark:border-neutral-800">
              <div class="text-[10px] text-neutral-400 uppercase font-semibold">Channel Recycling Instruction</div>
              <div class="text-emerald-600 dark:text-emerald-400 font-bold mt-1">extend_channel_reserve (0x3f160e5e7c2d2ccd)</div>
              <div class="text-[10px] text-neutral-500 mt-1">0 SOL Rent Churn • Phantom / Solflare Ready</div>
            </div>
          </div>

          <!-- Watchtower REST API Reference -->
          <div class="relative bg-neutral-900 text-neutral-100 rounded-xl p-4 font-mono text-xs border border-neutral-800 space-y-2">
            <div class="flex justify-between items-center pb-2 border-b border-neutral-800 text-[10px] text-neutral-400">
              <span class="text-neutral-200 font-semibold">Watchtower Daemon Sentinel Endpoints</span>
              <span class="text-emerald-400 font-medium">Port 8080 / Express Relayer</span>
            </div>
            <div class="text-[11px] text-neutral-300 space-y-1">
              <div><strong class="text-white">GET /api/watchtower/status</strong> - Query active dispute sentinel metrics & tracked channels</div>
              <div><strong class="text-white">POST /api/watchtower/register</strong> - Submit latest Ed25519 monotonic voucher for auto-monitoring</div>
              <div><strong class="text-white">POST /api/watchtower/defend</strong> - Broadcast on-chain settlement defense transaction to Solana Devnet</div>
            </div>
          </div>

          <script>
            window.switchDevLang = function(lang) {
              var pyBlock = document.getElementById('dev-code-python');
              var nodeBlock = document.getElementById('dev-code-node');
              var pyBtn = document.getElementById('dev-tab-btn-python');
              var nodeBtn = document.getElementById('dev-tab-btn-node');
              if (!pyBlock || !nodeBlock || !pyBtn || !nodeBtn) return;
              if (lang === 'python') {
                pyBlock.classList.remove('hidden');
                nodeBlock.classList.add('hidden');
                pyBtn.className = 'px-3 py-1 rounded-lg text-xs font-semibold bg-black dark:bg-white text-white dark:text-black transition-all';
                nodeBtn.className = 'px-3 py-1 rounded-lg text-xs font-semibold text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white transition-all';
              } else {
                pyBlock.classList.add('hidden');
                nodeBlock.classList.remove('hidden');
                pyBtn.className = 'px-3 py-1 rounded-lg text-xs font-semibold text-neutral-600 dark:text-neutral-400 hover:text-black dark:hover:text-white transition-all';
                nodeBtn.className = 'px-3 py-1 rounded-lg text-xs font-semibold bg-black dark:bg-white text-white dark:text-black transition-all';
              }
            };
          </script>
        </div>\n\n        """

        updated_content = content[:idx_s] + new_section + content[idx_e:]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"Applied clean developer hub to {file_path}")

if __name__ == '__main__':
    apply_clean_devhub()
