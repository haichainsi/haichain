import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the corrupted character in badge
content = content.replace('Haichain Developer Toolkit v1.1  HTTP 402 On-Chain', 'Haichain Developer Toolkit v1.1 &bull; HTTP 402 On-Chain')

# 2. Remove the buttons container from Developer Docs header
target_block = '''            <div class="flex items-center space-x-2 shrink-0">
              <a href="https://github.com/haichainsi/haichain" target="_blank" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-neutral-100 hover:bg-neutral-200 dark:bg-neutral-800 dark:hover:bg-neutral-700 text-black dark:text-white transition-all flex items-center space-x-1.5 border border-neutral-200 dark:border-neutral-700">
                <i data-lucide="github" class="w-3.5 h-3.5"></i>
                <span data-i18n="dev.btnGithub">GitHub Repo</span>
              </a>
              <button onclick="window.syncGlobalRegistries?.();" class="px-4 py-2 rounded-xl text-xs font-semibold bg-black hover:bg-neutral-800 text-white dark:bg-white dark:hover:bg-neutral-200 dark:text-black border border-black dark:border-white transition-all shadow-sm flex items-center space-x-1.5 cursor-pointer active:scale-98">
                <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                <span data-i18n="marketplace.syncRegistriesShort">Sync Global Registries</span>
              </button>
            </div>'''

if target_block in content:
    content = content.replace(target_block, '')
    print('Successfully removed GitHub Repo and Sync buttons from Developer Docs header!')
else:
    print('Warning: exact target block not found! Trying regex replacement...')
    # Regex fallback
    content = re.sub(
        r'<div class="flex items-center space-x-2 shrink-0">\s*<a href="https://github\.com/haichainsi/haichain"[^<]*<i data-lucide="github"[^<]*</i>\s*<span[^<]*GitHub Repo</span>\s*</a>\s*<button onclick="window\.syncGlobalRegistries\?\.\(\);"[^<]*<i data-lucide="refresh-cw"[^<]*</i>\s*<span[^<]*Sync Global Registries</span>\s*</button>\s*</div>',
        '',
        content
    )
    print('Regex replacement applied.')

# 3. Add window.syncGlobalRegistries for the Marketplace tab
sync_function = '''
    window.syncGlobalRegistries = function() {
      const btn = document.getElementById('sync-global-registries-btn');
      const icon = btn ? btn.querySelector('svg, i') : null;
      if (icon) icon.classList.add('animate-spin');
      if (typeof loadGlobalAgentMarketplace === 'function') {
        loadGlobalAgentMarketplace();
      }
      setTimeout(() => {
        if (icon) icon.classList.remove('animate-spin');
        if (typeof showToast === 'function') {
          const isVi = window.haichainI18n ? window.haichainI18n.current() === 'vi' : false;
          showToast({
            title: isVi ? 'Đồng bộ Registries thành công' : 'Registries Synchronized',
            message: isVi ? 'Đã làm mới danh bạ AI Agent liên kết.' : 'Synchronized latest autonomous agents list.',
            icon: 'check-circle'
          });
        }
      }, 500);
    };
'''

# Find loadGlobalAgentMarketplace to place syncGlobalRegistries near it
if 'window.syncGlobalRegistries = function' not in content:
    marker = 'window.loadGlobalAgentMarketplace = renderGlobalAgentMarketplace;'
    if marker in content:
        content = content.replace(marker, marker + '\n' + sync_function)
        print('Successfully added window.syncGlobalRegistries implementation for Marketplace tab!')

# Save dashboard.html
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Copy to app/dashboard.html
import shutil
shutil.copy2('dashboard.html', 'app/dashboard.html')
print('Copied dashboard.html -> app/dashboard.html')
