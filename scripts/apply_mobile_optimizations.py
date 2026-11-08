import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def optimize_file(filepath):
    print(f"=== Optimizing Mobile UI in {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # ================= TARGET 1: SSE / HTTPS BADGE IN MODAL =================
    # Target regex for Remote MCP URL header inside ai-hub-modal
    old_target1 = r'<div class="flex items-center justify-between text-\[11px\] text-neutral-400">\s*<span class="flex items-center space-x-1\.5 font-sans">\s*<i data-lucide="link" class="w-3\.5 h-3\.5 text-neutral-300"></i>\s*<span>Đường dẫn Remote MCP Connector URL:</span>\s*</span>\s*<span class="text-\[10px\] bg-neutral-900 border border-neutral-800 px-2 py-0\.5 rounded-full text-neutral-400 font-mono">SSE / HTTPS</span>\s*</div>'
    new_target1 = '''<div class="flex items-center justify-between gap-2 text-[11px] text-neutral-400">
            <span class="flex items-center space-x-1.5 font-sans truncate min-w-0">
              <i data-lucide="link" class="w-3.5 h-3.5 text-neutral-300 shrink-0"></i>
              <span class="truncate">Remote MCP Connector URL:</span>
            </span>
            <span class="text-[9.5px] bg-neutral-900 border border-neutral-800 px-2 py-0.5 rounded-full text-neutral-300 font-mono shrink-0 whitespace-nowrap">SSE / HTTPS</span>
          </div>'''

    if re.search(old_target1, content):
        content = re.sub(old_target1, new_target1, content)
        print("✓ Target 1 (SSE / HTTPS badge) optimized with whitespace-nowrap and truncate")
    else:
        # Fallback search if slightly different
        idx = content.find('online-mcp-url-snippet')
        if idx != -1:
            box_start = content.rfind('<div class="flex items-center justify-between', 0, idx)
            box_end = content.find('</div>', box_start) + 6
            content = content[:box_start] + new_target1 + content[box_end:]
            print("✓ Target 1 (SSE / HTTPS badge) replaced via fallback index slice")
        else:
            print("! Target 1 not found")

    # ================= TARGET 2: v6.9.3 L1 Core BADGE IN PLAYGROUND =================
    old_target2 = r'<div class="flex items-center space-x-2">\s*<h2 class="font-bold text-base sm:text-lg text-black dark:text-white" data-i18n="playground\.title">Live AI Agent Micro-Escrow Terminal</h2>\s*<span class="inline-flex items-center px-2 py-0\.5 rounded-full text-\[10px\] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800">\s*v6\.9\.3 L1 Core\s*</span>\s*</div>'
    new_target2 = '''<div class="flex items-start justify-between gap-2">
                <h2 class="font-bold text-base sm:text-lg text-black dark:text-white leading-tight" data-i18n="playground.title">Live AI Agent Micro-Escrow Terminal</h2>
                <span class="shrink-0 whitespace-nowrap px-2 py-0.5 rounded-full text-[9.5px] sm:text-[10px] font-mono font-medium bg-neutral-100 dark:bg-neutral-900 text-neutral-700 dark:text-neutral-300 border border-neutral-200 dark:border-neutral-800 mt-0.5">
                  v6.9.3 L1 Core
                </span>
              </div>'''

    if re.search(old_target2, content):
        content = re.sub(old_target2, new_target2, content)
        print("✓ Target 2 (v6.9.3 L1 Core badge) optimized with items-start justify-between and shrink-0")
    else:
        # Fallback index search
        idx2 = content.find('v6.9.3 L1 Core')
        if idx2 != -1:
            box_start = content.rfind('<div class="flex items-center space-x-2">', 0, idx2)
            box_end = content.find('</div>', idx2) + 6
            content = content[:box_start] + new_target2 + content[box_end:]
            print("✓ Target 2 replaced via fallback index slice")
        else:
            print("! Target 2 not found")

    # ================= TARGET 3: QUICK DEMOS 2x2 GRID ON MOBILE =================
    old_target3 = r'<!-- Production Task Templates -->\s*<div class="flex flex-wrap items-center gap-2 pt-1 text-\[11px\] font-mono">[\s\S]*?📜 Smart Contract Anchor\s*</button>\s*</div>'
    new_target3 = '''<!-- Production Task Templates (Optimized 2-Col Grid on Mobile, Flex on Desktop) -->
            <div class="space-y-1.5 pt-1">
              <div class="flex items-center justify-between text-[10px] text-neutral-400 dark:text-neutral-500 uppercase tracking-wider font-sans font-semibold">
                <span>Quick Demos:</span>
                <span class="text-[9px] text-neutral-500 font-mono">1-Tap Prompt</span>
              </div>
              <div class="grid grid-cols-2 sm:flex sm:flex-wrap gap-1.5 text-[11px] font-mono">
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start space-x-1.5 truncate cursor-pointer active:scale-98" data-prompt="Explain how HAICHAIN protects AI agents from prompt injection wallet drain" data-model="Claude 3.5 Sonnet">
                  <span class="shrink-0">🛡️</span>
                  <span class="truncate">Anti-Drain</span>
                </button>
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start space-x-1.5 truncate cursor-pointer active:scale-98" data-prompt="Calculate sub-second micro-escrow netting for autonomous agent swarm on Solana L1" data-model="DeepSeek R1">
                  <span class="shrink-0">⚡</span>
                  <span class="truncate">Micro-Escrow</span>
                </button>
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start space-x-1.5 truncate cursor-pointer active:scale-98" data-prompt="Compute joint torques and collision envelope for Optimus kinematic actuator tick" data-model="Optimus Kinematics">
                  <span class="shrink-0">🤖</span>
                  <span class="truncate">Optimus AI</span>
                </button>
                <button type="button" class="preset-prompt-btn px-2.5 py-2 sm:py-1 rounded-xl bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white hover:text-black dark:hover:text-white transition-all flex items-center justify-center sm:justify-start space-x-1.5 truncate cursor-pointer active:scale-98" data-prompt="Anchor Core Program Instruction: haichain_micro_escrow_settle CPI dispatch" data-model="Perplexity Search">
                  <span class="shrink-0">📜</span>
                  <span class="truncate">Anchor CPI</span>
                </button>
              </div>
            </div>'''

    if re.search(old_target3, content):
        content = re.sub(old_target3, new_target3, content)
        print("✓ Target 3 (Quick Demos) converted to optimized 2-column mobile grid")
    else:
        # Fallback index search
        idx3 = content.find('Anti-Drain Defense')
        if idx3 != -1:
            box_start = content.rfind('<!-- Production Task Templates -->', 0, idx3)
            btn4 = content.find('Smart Contract Anchor', idx3)
            box_end = content.find('</div>', btn4) + 6
            content = content[:box_start] + new_target3 + content[box_end:]
            print("✓ Target 3 replaced via fallback index slice")
        else:
            print("! Target 3 not found")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath} ({len(content)} bytes)\n")

for p in ['dashboard.html', 'app/dashboard.html']:
    optimize_file(p)
