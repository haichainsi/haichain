import os
import re

print("Starting clean i18n & icon fix...")

# 1. Update i18n.js and app/i18n.js: clean '+' from marketplace.registerBtn and dev.btnRegisterNow in all 10 languages
i18n_files = ['i18n.js', os.path.join('app', 'i18n.js')]

clean_replacements = [
    # Strip leading "+ " or "+" from marketplace.registerBtn
    (r'"marketplace\.registerBtn":\s*"\+\s*([^"]+)"', r'"marketplace.registerBtn": "\1"'),
    (r'"dev\.btnRegisterNow":\s*"\+\s*([^"]+)"', r'"dev.btnRegisterNow": "\1"')
]

for fpath in i18n_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    for pattern, repl in clean_replacements:
        content = re.sub(pattern, repl, content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned leading '+' in {fpath}")

# 2. Update dashboard.html and app/dashboard.html
dash_files = ['dashboard.html', os.path.join('app', 'dashboard.html')]

for fpath in dash_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read().replace('\r\n', '\n')

    # Fix 1: Remove redundant pulse dot before globe icon in Marketplace header
    # Replace:
    # <div class="flex items-center space-x-2">
    #   <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
    #   <h3 class="font-bold text-base text-black dark:text-white flex items-center space-x-2">
    #     <i data-lucide="globe" class="w-4 h-4 text-emerald-500"></i>
    #     <span data-i18n="marketplace.title">
    old_header = r'''<div class="flex items-center space-x-2">\s*<span class="w-2\.5 h-2\.5 rounded-full bg-emerald-500 animate-pulse"></span>\s*<h3 class="font-bold text-base text-black dark:text-white flex items-center space-x-2">\s*<i data-lucide="globe" class="w-4 h-4 text-emerald-500"></i>'''
    new_header = '''<div class="flex items-center space-x-2">
                <h3 class="font-bold text-base text-black dark:text-white flex items-center space-x-2">
                  <i data-lucide="globe" class="w-4 h-4 text-emerald-500"></i>'''
    c = re.sub(old_header, new_header, c)

    # Fix 2: Restore open-register-agent-modal-btn with single plus icon and data-i18n="marketplace.registerBtn"
    # In market-category-filters, replace sync-global-registries-btn or open-register-agent-modal-btn
    filter_pattern = r'<div class="flex items-center gap-1\.5 overflow-x-auto pb-1 sm:pb-0" id="market-category-filters">\s*(?:<button id="[^"]+".*?</button>\s*)+'
    
    # We want: open-register-agent-modal-btn (primary) + sync-global-registries-btn (secondary)
    target_buttons = '''<div class="flex items-center gap-1.5 overflow-x-auto pb-1 sm:pb-0" id="market-category-filters">
              <button id="open-register-agent-modal-btn" class="px-3 py-2 rounded-xl text-xs font-semibold bg-emerald-600 text-white hover:bg-emerald-500 border border-emerald-500 shrink-0 transition-all active:scale-98 cursor-pointer flex items-center space-x-1.5">
                <i data-lucide="plus" class="w-3.5 h-3.5 inline"></i>
                <span data-i18n="marketplace.registerBtn">Register Agent</span>
              </button>
              <button id="sync-global-registries-btn" onclick="window.syncGlobalRegistries?.();" class="px-3 py-2 rounded-xl text-xs font-semibold bg-neutral-900 hover:bg-neutral-800 text-white dark:bg-white dark:text-black dark:hover:bg-neutral-200 border border-neutral-800 dark:border-neutral-200 shrink-0 transition-all active:scale-98 cursor-pointer flex items-center space-x-1.5">
                <i data-lucide="refresh-cw" class="w-3.5 h-3.5 inline"></i>
                <span data-i18n="marketplace.syncRegistriesShort">Sync</span>
              </button>
              <button class="market-cat-btn px-3 py-2 rounded-xl text-xs font-medium bg-black text-white dark:bg-white dark:text-black border border-black dark:border-white shrink-0 transition-all cursor-pointer" data-category="all" data-i18n="marketplace.catAll">
                All Categories
              </button>
              <button class="market-cat-btn px-3 py-2 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer" data-category="data_extraction" data-i18n="marketplace.catScraping">
                Web Scraping
              </button>
              <button class="market-cat-btn px-3 py-2 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer" data-category="financial_intelligence" data-i18n="marketplace.catAlpha">
                Market Alpha
              </button>
              <button class="market-cat-btn px-3 py-2 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer" data-category="security_audit" data-i18n="marketplace.catSecurity">
                Security Audit
              </button>
              <button class="market-cat-btn px-3 py-2 rounded-xl text-xs font-medium bg-neutral-100 text-neutral-700 dark:bg-neutral-900 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 shrink-0 hover:border-black dark:hover:border-white transition-all cursor-pointer" data-category="automation" data-i18n="marketplace.catCompute">
                TEE Compute
              </button>'''
    
    # Replace the filter bar buttons
    # Check if market-category-filters is present
    if 'id="market-category-filters"' in c:
        # Find start of id="market-category-filters"
        start_idx = c.find('id="market-category-filters"')
        div_start = c.rfind('<div', 0, start_idx)
        # Find closing </div> of this filter bar
        # It's right before <!-- Live Agent Cards Grid
        end_idx = c.find('<!-- Live Agent Cards Grid', div_start)
        div_end = c.rfind('</div>', div_start, end_idx)
        # Find the inner div end
        # Let's inspect snippet:
        # <div class="flex items-center gap-1.5 overflow-x-auto pb-1 sm:pb-0" id="market-category-filters"> ... </div>
        # and then </div> closing the parent flex container
        c = c[:div_start] + target_buttons + '\n            </div>' + c[end_idx-12:]
        print(f"Replaced category filter bar in {fpath}")

    # Fix 3: Also update tab-docs line 722 button to open register modal with data-i18n="dev.btnRegisterNow"
    docs_btn_pattern = r'<button onclick="window\.syncGlobalRegistries\?\.\(\);"\s*class="px-4 py-2 rounded-xl text-xs font-semibold bg-emerald-600.*?</button>'
    docs_btn_repl = '''<button onclick="document.getElementById('open-register-agent-modal-btn')?.click();" class="px-4 py-2 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition-all shadow-sm flex items-center space-x-1.5 cursor-pointer active:scale-98">
                <i data-lucide="plus" class="w-3.5 h-3.5"></i>
                <span data-i18n="dev.btnRegisterNow">Register Agent Now</span>
              </button>'''
    c = re.sub(docs_btn_pattern, docs_btn_repl, c)

    # Fix 4: Ensure register-agent-modal is present in HTML before </body>
    if 'id="register-agent-modal"' not in c:
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
              <h3 class="font-bold text-sm text-black dark:text-white" data-i18n="marketplace.regModalTitle">Register Autonomous AI Agent</h3>
              <p class="text-[11px] text-neutral-400 font-mono" data-i18n="marketplace.regModalSub">Publish Agent to Global Haichain Economy</p>
            </div>
          </div>
          <button id="close-register-agent-btn" class="text-neutral-400 hover:text-black dark:hover:text-white p-1 rounded-lg cursor-pointer">
            <i data-lucide="x" class="w-4 h-4"></i>
          </button>
        </div>

        <form id="community-agent-register-form" class="space-y-3">
          <div>
            <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1" data-i18n="marketplace.regNameLabel">Agent Name / Node Name *</label>
            <input type="text" id="reg-agent-name" required placeholder="VD: DeepSeek Market Arbitrage Sentinel" 
                   class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs text-black dark:text-white focus:outline-none focus:border-black dark:focus:border-white">
          </div>

          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1" data-i18n="marketplace.regCatLabel">Category *</label>
              <select id="reg-agent-category" class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs text-black dark:text-white focus:outline-none">
                <option value="data_extraction" data-i18n="marketplace.catScraping">Web Scraping / Data</option>
                <option value="financial_intelligence" data-i18n="marketplace.catAlpha">Financial Alpha / Trading</option>
                <option value="security_audit" data-i18n="marketplace.catSecurity">Smart Contract Security</option>
                <option value="automation" data-i18n="marketplace.catCompute">Compute / Automation</option>
                <option value="custom">Custom Specialized</option>
              </select>
            </div>
            <div>
              <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1" data-i18n="marketplace.regPriceLabel">Price per Request (USDT) *</label>
              <input type="number" step="0.001" min="0.001" id="reg-agent-price" value="0.003" required
                     class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs text-black dark:text-white focus:outline-none">
            </div>
          </div>

          <div>
            <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1" data-i18n="marketplace.regWalletLabel">Solana Payout Wallet (Base58) *</label>
            <input type="text" id="reg-agent-wallet" required placeholder="VD: 5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3" 
                   class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs font-mono text-black dark:text-white focus:outline-none">
          </div>

          <div>
            <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1" data-i18n="marketplace.regEndpointLabel">Webhook / MCP URL Endpoint (Optional)</label>
            <input type="url" id="reg-agent-endpoint" placeholder="VD: https://api.my-agent.io/v1/inference" 
                   class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs font-mono text-black dark:text-white focus:outline-none">
          </div>

          <div>
            <label class="block text-[11px] font-semibold text-neutral-600 dark:text-neutral-300 mb-1" data-i18n="marketplace.regDescLabel">Capabilities Description</label>
            <textarea id="reg-agent-desc" rows="2" data-i18n-placeholder="marketplace.regDescPlaceholder" placeholder="Describe agent capabilities, SLA or LLM parameters..." 
                      class="w-full px-3 py-2 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 text-xs text-black dark:text-white focus:outline-none"></textarea>
          </div>

          <div class="pt-2 flex items-center justify-end space-x-2">
            <button type="button" id="cancel-register-agent-btn" class="px-4 py-2 rounded-xl text-xs font-medium text-neutral-500 hover:text-black dark:hover:text-white cursor-pointer" data-i18n="marketplace.regCancel">
              Cancel
            </button>
            <button type="submit" id="submit-register-agent-btn" class="px-5 py-2 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition-all active:scale-98 cursor-pointer" data-i18n="marketplace.regSubmit">
              Confirm On-Chain Registration
            </button>
          </div>
        </form>
      </div>
    </div>
'''
        body_idx = c.rfind('</body>')
        if body_idx != -1:
            c = c[:body_idx] + modal_html + '\n' + c[body_idx:]
            print(f"Appended register modal to {fpath}")

    # Fix 5: Ensure JavaScript handles register modal events
    if 'community-agent-register-form' not in c or 'openRegBtn.addEventListener' not in c:
        js_modal_handlers = '''
      // Modal controls for Registering Agent
      const regModal = document.getElementById('register-agent-modal');
      const openRegBtn = document.getElementById('open-register-agent-modal-btn');
      const closeRegBtn = document.getElementById('close-register-agent-btn');
      const cancelRegBtn = document.getElementById('cancel-register-agent-btn');
      const regForm = document.getElementById('community-agent-register-form');

      function showRegisterModal() {
        if (regModal) regModal.classList.remove('hidden');
      }
      function hideRegisterModal() {
        if (regModal) regModal.classList.add('hidden');
      }

      if (openRegBtn) openRegBtn.addEventListener('click', showRegisterModal);
      if (closeRegBtn) closeRegBtn.addEventListener('click', hideRegisterModal);
      if (cancelRegBtn) cancelRegBtn.addEventListener('click', hideRegisterModal);

      if (regForm) {
        regForm.addEventListener('submit', async (e) => {
          e.preventDefault();
          const submitBtn = document.getElementById('submit-register-agent-btn');
          const origText = submitBtn ? submitBtn.textContent : '';
          if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Registering on Solana...';
          }

          const agentData = {
            name: document.getElementById('reg-agent-name')?.value,
            category: document.getElementById('reg-agent-category')?.value,
            pricingUsdt: parseFloat(document.getElementById('reg-agent-price')?.value || '0.003'),
            recipientAddress: document.getElementById('reg-agent-wallet')?.value,
            endpointUrl: document.getElementById('reg-agent-endpoint')?.value,
            description: document.getElementById('reg-agent-desc')?.value
          };

          try {
            const resp = await fetch('/api/agents/register', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(agentData)
            });

            const resJson = await resp.json();
            if (!resp.ok) throw new Error(resJson.error || 'Registration failed');

            if (typeof showToast === 'function') {
              showToast({
                title: 'Agent Registered Successfully',
                message: `${agentData.name} is now live in the Haichain Mesh!`,
                icon: 'check-circle'
              });
            }

            regForm.reset();
            hideRegisterModal();
            if (typeof loadGlobalAgentMarketplace === 'function') {
              loadGlobalAgentMarketplace();
            }
          } catch (err) {
            alert('Registration Error: ' + err.message);
          } finally {
            if (submitBtn) {
              submitBtn.disabled = false;
              submitBtn.textContent = origText;
            }
          }
        });
      }
'''
        # Insert before initGlobalAgentMarketplaceEvents closing
        if 'initGlobalAgentMarketplaceEvents()' in c:
            idx = c.find('initGlobalAgentMarketplaceEvents()')
            # find opening of function initGlobalAgentMarketplaceEvents
            fn_idx = c.rfind('function initGlobalAgentMarketplaceEvents', 0, idx)
            # find last brace before initGlobalAgentMarketplaceEvents()
            last_brace = c.rfind('}', fn_idx, idx)
            c = c[:last_brace] + js_modal_handlers + '\n    ' + c[last_brace:]
            print(f"Added JS modal handlers to {fpath}")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Finished applying clean fixes.")
