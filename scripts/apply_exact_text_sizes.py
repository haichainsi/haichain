import re

replacements = [
    # Subtitles in both sections
    ('class="text-sm sm:text-base text-neutral-600 dark:text-neutral-400 mt-4 leading-relaxed font-light"',
     'class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 mt-3 leading-relaxed font-light"'),
    
    # agentic-shift card padding
    ('class="p-6 sm:p-7 rounded-2xl bg-neutral-50/60',
     'class="p-5 sm:p-6 rounded-2xl bg-neutral-50/60'),
    
    # agentic-shift card inner flex
    ('class="flex items-center space-x-3 mb-3.5"',
     'class="flex items-center space-x-2.5 mb-2.5"'),
    
    # agentic-shift lucide icon size
    ('class="w-5 h-5 text-neutral-900 dark:text-white shrink-0"',
     'class="w-4 h-4 text-neutral-900 dark:text-white shrink-0"'),
    
    # agentic-shift card title size
    ('class="text-base sm:text-lg font-semibold text-neutral-950 dark:text-white tracking-tight"',
     'class="text-sm sm:text-base font-semibold text-neutral-950 dark:text-white tracking-tight"'),
    
    # agentic-shift card description font size
    ('class="text-xs sm:text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans"',
     'class="text-xs text-neutral-600 dark:text-neutral-400 leading-relaxed font-sans"'),
    
    # haichain-advantages card padding
    ('class="p-6 sm:p-7 rounded-2xl bg-white dark:bg-brand-card',
     'class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-brand-card'),
    
    # haichain-advantages card inner flex
    ('class="flex items-start space-x-3 mb-3.5"',
     'class="flex items-start space-x-2.5 mb-2.5"'),
    
    # haichain-advantages lucide icon size
    ('class="w-5 h-5 text-neutral-950 dark:text-white shrink-0 mt-0.5"',
     'class="w-4 h-4 text-neutral-950 dark:text-white shrink-0 mt-0.5"'),
    
    # haichain-advantages card title size
    ('class="text-base sm:text-lg font-bold text-neutral-950 dark:text-white tracking-tight"',
     'class="text-sm sm:text-base font-bold text-neutral-950 dark:text-white tracking-tight"'),
    
    # haichain-advantages inner body space & font size
    ('class="space-y-3 font-sans text-xs sm:text-sm leading-relaxed"',
     'class="space-y-2.5 font-sans text-xs leading-relaxed"'),
]

for file_path in ['index.html', 'app/index.html']:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only replace within agentic-shift and haichain-advantages
    s_start = content.find('id="agentic-shift"')
    s_end = content.find('id="market-evidence"')
    assert s_start != -1 and s_end != -1, f"Sections not found in {file_path}"
    
    sec_content = content[s_start:s_end]
    for old, new in replacements:
        count = sec_content.count(old)
        sec_content = sec_content.replace(old, new)
        print(f"[{file_path}] Replaced {count} occurrences of {old[:40]}...")
    
    content = content[:s_start] + sec_content + content[s_end:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {file_path}\n")
