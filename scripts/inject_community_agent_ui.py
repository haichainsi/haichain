import os

target_files = ['dashboard.html', os.path.join('app', 'dashboard.html')]

modal_html = '''
    <!-- ================= MODAL: REGISTER COMMUNITY AGENT ================= -->
    <div id="register-agent-modal" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4">
      <div class="bg-white dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 rounded-3xl max-w-lg w-full p-6 shadow-2xl space-y-4 animate-in fade-in zoom-in-95 duration-150">
        <div class="flex items-center justify-between border-b border-neutral-100 dark:border-neutral-800 pb-3">
          <div class="flex items-center space-x-2">
            <div class="w-8 h-8 rounded-full bg-emerald-500/10 text-emerald-500 flex items-center justify-center font-bold text-sm">
              <i data-lucide="bot" class="w-4 h-4"></i>
            </div>
            <div>
              <h3 class="font-bold text-sm text-black dark:text-white">Đăng ký Autonomous AI Agent</h3>
              <p class="text-[11px] text-neutral-400 font-mono">Publish Agent to Global HAIChain Economy</p>
            </div>
          </div>
          <button id="close-register-agent-btn" class="text-neutral-400 hover:text-black dark:hover:text-white p-1 rounded-lg">
            <i data-lucide="x" class="w-4 h-4"></i>
          </button>
        </div>

        <form id="community-agent-register-form" class="space-y-3">
          <div>
            <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1">Tên Agent / Node Name *</label>
            <input type="text" id="reg-agent-name" required placeholder="VD: DeepSeek Market Arbitrage Sentinel" 
                   class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs text-black dark:text-white focus:outline-none focus:border-black dark:focus:border-white">
          </div>

          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1">Danh mục / Category *</label>
              <select id="reg-agent-category" class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs text-black dark:text-white focus:outline-none">
                <option value="data_extraction">Web Scraping / Data</option>
                <option value="financial_intelligence">Financial Alpha / Trading</option>
                <option value="security_audit">Smart Contract Security</option>
                <option value="automation">Compute / Automation</option>
                <option value="custom">Custom Specialized</option>
              </select>
            </div>
            <div>
              <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1">Giá mỗi Request (USDT) *</label>
              <input type="number" step="0.001" min="0.001" id="reg-agent-price" value="0.003" required
                     class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs text-black dark:text-white focus:outline-none">
            </div>
          </div>

          <div>
            <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1">Địa chỉ ví nhận tiền Solana (Payee Base58) *</label>
            <input type="text" id="reg-agent-wallet" required placeholder="VD: 5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3" 
                   class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs font-mono text-black dark:text-white focus:outline-none">
          </div>

          <div>
            <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1">Endpoint Webhook / MCP URL (Tùy chọn)</label>
            <input type="url" id="reg-agent-endpoint" placeholder="VD: https://api.my-agent.io/v1/inference" 
                   class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs font-mono text-black dark:text-white focus:outline-none">
          </div>

          <div>
            <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1">Mô tả năng lực (Capabilities)</label>
            <textarea id="reg-agent-desc" rows="2" placeholder="Mô tả kỹ năng, SLA hoặc thông số LLM..." 
                      class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs text-black dark:text-white focus:outline-none"></textarea>
          </div>

          <div class="pt-2 flex items-center justify-end space-x-2">
            <button type="button" id="cancel-register-agent-btn" class="px-4 py-2 rounded-xl text-xs font-medium text-neutral-500 hover:text-black dark:hover:text-white">
              Hủy
            </button>
            <button type="submit" id="submit-register-agent-btn" class="px-5 py-2 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition-all active:scale-98">
              Xác nhận Đăng ký On-Chain
            </button>
          </div>
        </form>
      </div>
    </div>
'''

js_registration_logic = '''
    // ================= DYNAMIC COMMUNITY AGENT REGISTRATION & LOADING =================
    async function loadGlobalAgentMarketplace() {
      try {
        const resp = await fetch('/api/agents');
        if (resp.ok) {
          const data = await resp.json();
          if (data && Array.isArray(data.agents) && data.agents.length > 0) {
            GLOBAL_MARKET_AGENTS = data.agents;
          }
        }
      } catch (err) {
        console.warn('Fallback to local catalog:', err.message);
      }
      renderGlobalAgentMarketplace();
    }

    // Modal controls for Registering Agent
    const regModal = document.getElementById('register-agent-modal');
    const openRegBtn = document.getElementById('open-register-agent-modal-btn');
    const closeRegBtn = document.getElementById('close-register-agent-btn');
    const cancelRegBtn = document.getElementById('cancel-register-agent-btn');
    const regForm = document.getElementById('community-agent-register-form');

    function openRegisterModal() {
      if (regModal) regModal.classList.remove('hidden');
    }
    function closeRegisterModal() {
      if (regModal) regModal.classList.add('hidden');
    }

    if (openRegBtn) openRegBtn.addEventListener('click', openRegisterModal);
    if (closeRegBtn) closeRegBtn.addEventListener('click', closeRegisterModal);
    if (cancelRegBtn) cancelRegBtn.addEventListener('click', closeRegisterModal);

    if (regForm) {
      regForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const submitBtn = document.getElementById('submit-register-agent-btn');
        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.innerHTML = '<span class="w-3 h-3 rounded-full border-2 border-current border-t-transparent animate-spin inline-block mr-1"></span> Registering...';
        }

        const name = document.getElementById('reg-agent-name').value;
        const category = document.getElementById('reg-agent-category').value;
        const pricingUsdt = parseFloat(document.getElementById('reg-agent-price').value || '0.003');
        const recipientAddress = document.getElementById('reg-agent-wallet').value;
        const endpointUrl = document.getElementById('reg-agent-endpoint').value;
        const description = document.getElementById('reg-agent-desc').value;

        try {
          const resp = await fetch('/api/agents/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              name,
              category,
              pricingUsdt,
              recipientAddress,
              endpointUrl: endpointUrl || null,
              description,
              capabilities: ['Autonomous Task Execution', 'HTTP 402 Paywall']
            })
          });

          const data = await resp.json();
          if (!resp.ok) throw new Error(data.error || 'Registration failed');

          closeRegisterModal();
          regForm.reset();
          if (typeof showToast === 'function') {
            showToast({
              title: 'Agent Registered Successfully',
              message: `${name} is now LIVE on HAIChain Registry!`,
              icon: 'check-circle'
            });
          }
          await loadGlobalAgentMarketplace();
        } catch (err) {
          alert('Error registering agent: ' + err.message);
        } finally {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Xác nhận Đăng ký On-Chain';
          }
        }
      });
    }
'''

for fpath in target_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # Add button to market-category-filters
    btn_marker = '<button class="market-cat-btn px-3 py-2 rounded-xl text-xs font-medium bg-black text-white dark:bg-white dark:text-black border border-black dark:border-white shrink-0 transition-all cursor-pointer" data-category="all">'
    btn_with_reg = '''<button id="open-register-agent-modal-btn" class="px-3 py-2 rounded-xl text-xs font-semibold bg-emerald-600 text-white hover:bg-emerald-500 border border-emerald-500 shrink-0 transition-all active:scale-98 cursor-pointer flex items-center space-x-1">
                <i data-lucide="plus-circle" class="w-3.5 h-3.5 inline"></i>
                <span>+ Đăng ký Agent</span>
              </button>
              ''' + btn_marker

    if btn_marker in content and 'open-register-agent-modal-btn' not in content:
        content = content.replace(btn_marker, btn_with_reg)
        print(f"Added + Register Agent button to {fpath}")

    # Inject modal before closing body
    if 'id="register-agent-modal"' not in content and '</body>' in content:
        content = content.replace('</body>', modal_html + '\n</body>')
        print(f"Injected register agent modal into {fpath}")

    # Replace hardcoded GLOBAL_MARKET_AGENTS initialization with dynamic call
    old_init = 'renderGlobalAgentMarketplace();'
    new_init = 'loadGlobalAgentMarketplace();'
    if old_init in content:
        content = content.replace(old_init, new_init)
        print(f"Switched initial render to loadGlobalAgentMarketplace in {fpath}")

    # Inject JS registration logic
    if 'loadGlobalAgentMarketplace' not in content and 'function renderGlobalAgentMarketplace()' in content:
        content = content.replace('function renderGlobalAgentMarketplace()', js_registration_logic + '\n    function renderGlobalAgentMarketplace()')
        print(f"Injected JS registration logic into {fpath}")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("UI registration injection complete.")
