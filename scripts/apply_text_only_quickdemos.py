import re

# 1. Update i18n.js and app/i18n.js
emojis_to_strip = {
    'playground.demoAntiDrain': '🛡️ ',
    'playground.demoMicroEscrow': '⚡ ',
    'playground.demoOptimus': '🤖 ',
    'playground.demoAnchor': '📜 '
}

for i18n_path in ['i18n.js', 'app/i18n.js']:
    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for key, prefix in emojis_to_strip.items():
        # Replace '"key": "PREFIX...' with '"key": "...'
        pattern = rf'("{re.escape(key)}":\s*"){re.escape(prefix)}'
        new_content, count = re.subn(pattern, r'\1', content)
        print(f"In {i18n_path}, replaced {count} occurrences for {key}")
        content = new_content

    with open(i18n_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update dashboard.html and app/dashboard.html
for dash_path in ['dashboard.html', 'app/dashboard.html']:
    with open(dash_path, 'r', encoding='utf-8') as f:
        d_content = f.read()

    # Pattern for the 4 buttons under Quick Demos
    # Replace the buttons removing the emoji spans and space-x-1.5
    old_block = '''              <div class="grid grid-cols-2 sm:flex sm:flex-wrap gap-1.5 text-[11px] font-mono">
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start space-x-1.5 truncate cursor-pointer active:scale-98" data-prompt="Explain how HAICHAIN protects AI agents from prompt injection wallet drain" data-model="Claude 3.5 Sonnet">
                  <span class="shrink-0">🛡️</span>
                  <span class="truncate" data-i18n="playground.demoAntiDrain">Anti-Drain</span>
                </button>
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start space-x-1.5 truncate cursor-pointer active:scale-98" data-prompt="Calculate sub-second micro-escrow netting for autonomous agent swarm on Solana L1" data-model="DeepSeek R1">
                  <span class="shrink-0">⚡</span>
                  <span class="truncate" data-i18n="playground.demoMicroEscrow">Micro-Escrow</span>
                </button>
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start space-x-1.5 truncate cursor-pointer active:scale-98" data-prompt="Compute joint torques and collision envelope for Optimus kinematic actuator tick" data-model="Optimus Kinematics">
                  <span class="shrink-0">🤖</span>
                  <span class="truncate" data-i18n="playground.demoOptimus">Optimus AI</span>
                </button>
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start space-x-1.5 truncate cursor-pointer active:scale-98" data-prompt="Anchor Core Program Instruction: haichain_micro_escrow_settle CPI dispatch" data-model="Perplexity Search">
                  <span class="shrink-0">📜</span>
                  <span class="truncate" data-i18n="playground.demoAnchor">Anchor CPI</span>
                </button>
              </div>'''

    new_block = '''              <div class="grid grid-cols-2 sm:flex sm:flex-wrap gap-1.5 text-[11px] font-mono">
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start truncate cursor-pointer active:scale-98" data-prompt="Explain how HAICHAIN protects AI agents from prompt injection wallet drain" data-model="Claude 3.5 Sonnet">
                  <span class="truncate" data-i18n="playground.demoAntiDrain">Anti-Drain</span>
                </button>
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start truncate cursor-pointer active:scale-98" data-prompt="Calculate sub-second micro-escrow netting for autonomous agent swarm on Solana L1" data-model="DeepSeek R1">
                  <span class="truncate" data-i18n="playground.demoMicroEscrow">Micro-Escrow</span>
                </button>
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start truncate cursor-pointer active:scale-98" data-prompt="Compute joint torques and collision envelope for Optimus kinematic actuator tick" data-model="Optimus Kinematics">
                  <span class="truncate" data-i18n="playground.demoOptimus">Optimus AI</span>
                </button>
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start truncate cursor-pointer active:scale-98" data-prompt="Anchor Core Program Instruction: haichain_micro_escrow_settle CPI dispatch" data-model="Perplexity Search">
                  <span class="truncate" data-i18n="playground.demoAnchor">Anchor CPI</span>
                </button>
              </div>'''

    # Normalize line endings for replacement
    d_content_crlf = d_content.replace('\r\n', '\n')
    old_block_norm = old_block.replace('\r\n', '\n')
    new_block_norm = new_block.replace('\r\n', '\n')

    if old_block_norm in d_content_crlf:
        d_content_crlf = d_content_crlf.replace(old_block_norm, new_block_norm)
        # Restore CRLF if original had CRLF
        if '\r\n' in d_content:
            d_content = d_content_crlf.replace('\n', '\r\n')
        else:
            d_content = d_content_crlf
        with open(dash_path, 'w', encoding='utf-8') as f:
            f.write(d_content)
        print(f"Successfully updated buttons in {dash_path}")
    else:
        print(f"WARNING: old_block not found in {dash_path}")
