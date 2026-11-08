# -*- coding: utf-8 -*-
import re

for path in ['index.html', 'app/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    pattern = r'<div class="[^"]*?text-xs font-mono[^"]*?mb-4[^"]*?">\s*<span class="w-1\.5 h-1\.5 rounded-full bg-black dark:bg-white animate-pulse"></span>\s*<span data-i18n="ai2\.badge">.*?</span>\s*</div>'

    replacement = """<div class="inline-flex items-center justify-center gap-1.5 sm:gap-2 px-3 py-1 sm:px-3.5 sm:py-1 rounded-full border border-neutral-300 dark:border-neutral-800 bg-white dark:bg-neutral-900 text-[10px] sm:text-xs font-mono text-neutral-800 dark:text-neutral-200 mb-4 shadow-xs max-w-[94vw] sm:max-w-none mx-auto">
          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse shrink-0"></span>
          <span class="leading-tight sm:leading-normal text-center whitespace-normal" data-i18n="ai2.badge">CORE PARADIGM &bull; HUMAN + MACHINE SYMBIOSIS (AI²)</span>
        </div>"""

    new_text = re.sub(pattern, replacement, text, flags=re.DOTALL)
    if new_text != text:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"SUCCESS: {path}")
    else:
        print(f"NO MATCH: {path}")
