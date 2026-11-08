import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ORIGINAL_AI_BTN = '''<!-- Consolidated Unified AI Integration Hub Trigger -->
        <button id="ai-hub-btn" type="button" class="haichain-action-btn has-label text-neutral-700 dark:text-neutral-300 hover:text-black dark:hover:text-white" title="AI Integration Hub: Connect AI">
          <i data-lucide="cpu" class="w-3.5 h-3.5 shrink-0 pointer-events-none"></i>
          <span class="hidden md:inline font-mono text-xs font-semibold">Connect AI</span>
          <span class="hidden sm:inline md:hidden text-[10px] font-bold font-mono">AI</span>
        </button>'''

def clean_file(filepath):
    print(f"=== Processing {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Restore the original refined header button style
    btn_start = content.find('id="ai-hub-btn"')
    if btn_start != -1:
        tag_start = content.rfind('<button', 0, btn_start)
        # also look back for comment
        comment_start = content.rfind('<!-- Consolidated Unified AI Integration Hub', 0, tag_start)
        if comment_start != -1 and tag_start - comment_start < 250:
            replace_start = comment_start
        else:
            replace_start = tag_start
        tag_end = content.find('</button>', btn_start) + 9
        content = content[:replace_start] + ORIGINAL_AI_BTN + content[tag_end:]
        print("✓ Header button restored to original refined style (.haichain-action-btn has-label)")
    else:
        print("! Header button id not found")

    # 2. Remove the Overview banner completely
    banner_start = content.find('<!-- High-Impact AI Integration Banner')
    if banner_start != -1:
        # Find closing </div> of the banner
        banner_end = content.find('</div>', content.find('</button>', banner_start)) + 6
        # Eat any extra blank line or spaces
        while banner_end < len(content) and content[banner_end] in ['\n', '\r', ' ']:
            banner_end += 1
        content = content[:banner_start] + content[banner_end:]
        print("✓ Red-boxed Overview banner completely removed")
    else:
        print("! Overview banner not found (already clean)")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath} ({len(content)} bytes)\n")

for p in ['dashboard.html', 'app/dashboard.html']:
    clean_file(p)
