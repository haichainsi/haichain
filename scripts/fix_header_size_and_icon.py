import os

target_files = ['dashboard.html', os.path.join('app', 'dashboard.html')]

old_block = '''              <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 text-[11px] font-mono font-semibold">
                <i data-lucide="sparkles" class="w-3.5 h-3.5"></i>
                <span>Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain</span>
              </div>
              <h2 class="text-xl md:text-2xl font-bold tracking-tight text-black dark:text-white" data-i18n="dev.title">
                Developer Portal & 5-Minute Quickstart
              </h2>'''

new_block = '''              <div class="inline-flex items-center px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 text-[11px] font-mono font-semibold">
                <span>Haichain Developer Toolkit v1.1 • HTTP 402 On-Chain</span>
              </div>
              <h2 class="font-bold text-base sm:text-lg text-black dark:text-white leading-tight" data-i18n="dev.title">
                Developer Portal & 5-Minute Quickstart
              </h2>'''

for fpath in target_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SUCCESS: Updated icon and title size in {fpath}")
    else:
        print(f"FAILED: old_block not found in {fpath}")

print("Fix completed.")
