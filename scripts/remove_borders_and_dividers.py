import re

# 1. Update sale-controller.js & app/sale-controller.js
vip_replacements = [
    # Outer box border
    ('border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-black shadow-lg text-center',
     'bg-white dark:bg-black text-center'),
    # Icon box border
    ('bg-neutral-100 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 flex items-center justify-center mx-auto text-black dark:text-white shadow-xs',
     'bg-neutral-100 dark:bg-neutral-900 flex items-center justify-center mx-auto text-black dark:text-white'),
    # Badge border
    ('bg-neutral-100 dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-800 text-[11px]',
     'bg-neutral-100 dark:bg-neutral-900 text-[11px]'),
    # Divider line
    ('pt-4 border-t border-neutral-100 dark:border-neutral-800/80 space-y-3',
     'pt-4 space-y-3'),
]

for spath in ['sale-controller.js', 'app/sale-controller.js']:
    with open(spath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in vip_replacements:
        assert old in content, f"Target not found in {spath}: {old[:40]}"
        content = content.replace(old, new)
    
    with open(spath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {spath} successfully!")

# 2. Update dashboard.html & app/dashboard.html
vesting_replacements = [
    # Main outer card border
    ('class="p-6 sm:p-8 rounded-3xl border border-neutral-200/60 dark:border-white/[0.06] bg-white dark:bg-[#0a0a0a] shadow-sm space-y-6"',
     'class="p-6 sm:p-8 rounded-3xl bg-white dark:bg-[#0a0a0a] space-y-6"'),
    
    # Header divider line (STATE 1 & 2)
    ('class="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-neutral-100 dark:border-white/[0.04] gap-4"',
     'class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 gap-4"'),
    
    # Header divider line (STATE 3)
    ('class="flex flex-col lg:flex-row lg:items-center justify-between pb-6 border-b border-neutral-100 dark:border-white/[0.04] gap-4"',
     'class="flex flex-col lg:flex-row lg:items-center justify-between pb-4 gap-4"'),
    
    # Inner box border
    ('class="p-6 sm:p-8 rounded-2xl bg-neutral-50/50 dark:bg-white/[0.015] border border-neutral-100 dark:border-white/[0.04] text-center max-w-xl mx-auto space-y-4"',
     'class="p-6 sm:p-8 rounded-2xl bg-neutral-50/50 dark:bg-white/[0.015] text-center max-w-xl mx-auto space-y-4"'),
    
    # Header icon border
    ('border border-neutral-200/60 dark:border-white/[0.08] flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1.5 mt-0.5"',
     'flex items-center justify-center shrink-0 overflow-hidden p-1.5 mt-0.5"'),
    
    # Solana L1 badge border
    ('text-neutral-600 dark:text-neutral-400 border border-neutral-200/50 dark:border-white/[0.06]"',
     'text-neutral-600 dark:text-neutral-400"'),
    
    # Lock prompt icon border
    ('border border-neutral-200/50 dark:border-white/[0.06] flex items-center justify-center mx-auto text-black dark:text-white',
     'flex items-center justify-center mx-auto text-black dark:text-white'),
    
    # Inbox icon border in STATE 2
    ('border border-neutral-200/50 dark:border-white/[0.06] flex items-center justify-center mx-auto text-neutral-400 dark:text-neutral-500',
     'flex items-center justify-center mx-auto text-neutral-400 dark:text-neutral-500'),
]

for dpath in ['dashboard.html', 'app/dashboard.html']:
    with open(dpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in vesting_replacements:
        assert old in content, f"Target not found in {dpath}: {old[:40]}"
        content = content.replace(old, new)
    
    with open(dpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {dpath} successfully!")

print("\nAll files updated cleanly!")
