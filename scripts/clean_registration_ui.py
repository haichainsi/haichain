import os
import re

target_files = ['dashboard.html', os.path.join('app', 'dashboard.html')]

for fpath in target_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read().replace('\r\n', '\n')

    # Replace open-register-agent-modal-btn
    c = re.sub(
        r'<button id="open-register-agent-modal-btn".*?</button>',
        '''<button id="sync-global-registries-btn" onclick="window.syncGlobalRegistries?.();" class="px-3 py-2 rounded-xl text-xs font-semibold bg-neutral-900 hover:bg-neutral-800 text-white dark:bg-white dark:text-black dark:hover:bg-neutral-200 border border-neutral-800 dark:border-neutral-200 shrink-0 transition-all active:scale-98 cursor-pointer flex items-center space-x-1.5">
                <i data-lucide="refresh-cw" class="w-3.5 h-3.5 inline"></i>
                <span>Đồng bộ Sàn Toàn cầu (Smithery • Fetch.ai)</span>
              </button>''',
        c,
        flags=re.DOTALL
    )

    # Remove modal HTML
    c = re.sub(r'<!-- ================= MODAL: REGISTER COMMUNITY AGENT ================= -->.*?</form>\s*</div>\s*</div>', '', c, flags=re.DOTALL)
    c = re.sub(r'<div id="register-agent-modal".*?</form>\s*</div>\s*</div>', '', c, flags=re.DOTALL)

    # Replace JS registration logic
    old_reg_pattern = r'// Modal controls for Registering Agent.*?regForm\.addEventListener\(.*?\n    \}'
    new_sync_js = '''// ================= GLOBAL FEDERATED REGISTRY SYNC =================
    window.syncGlobalRegistries = async function() {
      const btn = document.getElementById('sync-global-registries-btn');
      let origHtml = '';
      if (btn) {
        origHtml = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = '<span class="w-3 h-3 rounded-full border-2 border-current border-t-transparent animate-spin inline-block mr-1"></span> Đang đồng bộ sàn quốc tế...';
      }

      try {
        const resp = await fetch('/api/registry/federation');
        if (resp.ok) {
          const data = await resp.json();
          if (typeof showToast === 'function') {
            showToast({
              title: 'Đã Đồng bộ Sàn Toàn cầu',
              message: `Kết nối thành công ${data.totalLeveragedAgents} từ Smithery (MCP), Fetch.ai & Glama!`,
              icon: 'check-circle'
            });
          }
        }
        await loadGlobalAgentMarketplace();
      } catch (err) {
        console.warn('Sync notice:', err.message);
      } finally {
        if (btn) {
          btn.disabled = false;
          btn.innerHTML = origHtml;
          if (typeof safeCreateIcons === 'function') safeCreateIcons();
        }
      }
    };'''
    c = re.sub(old_reg_pattern, new_sync_js, c, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Cleaned registration UI and added sync button in {fpath}")

print("Clean registration UI complete.")
