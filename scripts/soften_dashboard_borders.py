import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Vietnamese vaultTitle to use non-breaking hyphen for Token-2022
old_vi_title = '"vaultTitle": "Két Vesting & Phân Bổ Token-2022",'
new_vi_title = '"vaultTitle": "Két Vesting & Phân Bổ Token\\u20112022",'

# Also do for other languages if they use Token-2022 with normal hyphen in vaultTitle
if old_vi_title in content:
    content = content.replace(old_vi_title, new_vi_title, 1)

# 2. In State 1: Soften borders
old_state1_card = '<div class="p-6 sm:p-8 rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-black shadow-sm space-y-6">'
new_state1_card = '<div class="p-6 sm:p-8 rounded-3xl border border-neutral-200/60 dark:border-white/[0.06] bg-white dark:bg-[#0a0a0a] shadow-sm space-y-6">'

# 3. Soften the divider line across all states
old_divider = 'pb-6 border-b border-neutral-100 dark:border-neutral-900 gap-4'
new_divider = 'pb-6 border-b border-neutral-100 dark:border-white/[0.04] gap-4'
content = content.replace(old_divider, new_divider)

# 4. Soften the HAISI icon frame
old_icon_frame = '<div class="w-10 h-10 rounded-xl bg-black border border-neutral-800 flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1.5 mt-0.5">'
new_icon_frame = '<div class="w-10 h-10 rounded-xl bg-neutral-100 dark:bg-white/[0.03] border border-neutral-200/60 dark:border-white/[0.08] flex items-center justify-center shrink-0 overflow-hidden shadow-sm p-1.5 mt-0.5">'
content = content.replace(old_icon_frame, new_icon_frame)

# 5. Soften the Solana L1 badge in State 1
old_solana_badge = 'border border-neutral-200 dark:border-neutral-800'
# We will do targeted replacements for badges and cards

# State 1 Lock Box Prompt (replace inner box border and bg)
old_state1_box = '''            <!-- Lock Box Prompt -->
            <div class="p-8 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-center max-w-xl mx-auto space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-neutral-200 dark:bg-neutral-800 flex items-center justify-center mx-auto text-black dark:text-white">'''

new_state1_box = '''            <!-- Lock Box Prompt -->
            <div class="p-6 sm:p-8 rounded-2xl bg-neutral-50/50 dark:bg-white/[0.015] border border-neutral-100 dark:border-white/[0.04] text-center max-w-xl mx-auto space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-white/[0.04] border border-neutral-200/50 dark:border-white/[0.06] flex items-center justify-center mx-auto text-black dark:text-white">'''

if old_state1_box in content:
    content = content.replace(old_state1_box, new_state1_box, 1)

# State 2 Empty State Box
old_state2_box = '''            <div class="p-8 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 text-center max-w-xl mx-auto space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-neutral-200 dark:bg-neutral-800 flex items-center justify-center mx-auto text-neutral-500">'''

new_state2_box = '''            <div class="p-6 sm:p-8 rounded-2xl bg-neutral-50/50 dark:bg-white/[0.015] border border-neutral-100 dark:border-white/[0.04] text-center max-w-xl mx-auto space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-neutral-100 dark:bg-white/[0.04] border border-neutral-200/50 dark:border-white/[0.06] flex items-center justify-center mx-auto text-neutral-400 dark:text-neutral-500">'''

if old_state2_box in content:
    content = content.replace(old_state2_box, new_state2_box, 1)

# Soften secondary button in State 2 (Switch wallet)
old_switch_btn = 'class="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white font-mono text-xs text-neutral-700 dark:text-neutral-300 transition-all"'
new_switch_btn = 'class="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-neutral-200 dark:border-white/[0.08] hover:border-neutral-300 dark:hover:border-white/20 hover:bg-neutral-50 dark:hover:bg-white/[0.02] font-mono text-xs text-neutral-700 dark:text-neutral-300 transition-all"'
content = content.replace(old_switch_btn, new_switch_btn)

# Soften secondary button in State 1 (Mã Mời Phân Bổ VIP)
old_subscribe_btn = 'class="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white font-mono text-xs text-neutral-700 dark:text-neutral-300 transition-all flex items-center justify-center space-x-1.5 cursor-pointer"'
new_subscribe_btn = 'class="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-neutral-200 dark:border-white/[0.08] hover:border-neutral-300 dark:hover:border-white/20 hover:bg-neutral-50 dark:hover:bg-white/[0.02] font-mono text-xs text-neutral-700 dark:text-neutral-300 transition-all flex items-center justify-center space-x-1.5 cursor-pointer"'
content = content.replace(old_subscribe_btn, new_subscribe_btn)

# Soften wallet address badges in State 1 and State 2
old_state1_badge = '<span class="self-start sm:self-center shrink-0 whitespace-nowrap px-2.5 py-0.5 rounded-full text-[9.5px] sm:text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800">'
new_state1_badge = '<span class="self-start sm:self-center shrink-0 whitespace-nowrap px-2.5 py-0.5 rounded-full text-[9.5px] sm:text-[10px] font-mono bg-neutral-100/70 dark:bg-white/[0.03] text-neutral-600 dark:text-neutral-400 border border-neutral-200/50 dark:border-white/[0.06]">'
content = content.replace(old_state1_badge, new_state1_badge)

old_state2_badge = '<span class="self-start sm:self-center shrink-0 px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 dark:bg-neutral-900 text-neutral-600 dark:text-neutral-400 border border-neutral-200 dark:border-neutral-800">'
new_state2_badge = '<span class="self-start sm:self-center shrink-0 px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100/70 dark:bg-white/[0.03] text-neutral-600 dark:text-neutral-400 border border-neutral-200/50 dark:border-white/[0.06]">'
content = content.replace(old_state2_badge, new_state2_badge)

# Replace outer card containers in State 1, State 2, and State 3
content = content.replace(old_state1_card, new_state1_card)

# In State 3: Soften certificate box and internal elements
old_state3_cert = 'p-5 sm:p-6 rounded-2xl bg-neutral-900 border border-neutral-700/80 text-white font-mono text-xs space-y-4 shadow-sm relative overflow-hidden'
new_state3_cert = 'p-5 sm:p-6 rounded-2xl bg-neutral-950/70 dark:bg-white/[0.02] border border-neutral-200/60 dark:border-white/[0.08] text-white font-mono text-xs space-y-4 shadow-sm relative overflow-hidden'
content = content.replace(old_state3_cert, new_state3_cert)

old_state3_subbox = 'p-3 rounded-xl bg-neutral-950/80 border border-neutral-800 space-y-1'
new_state3_subbox = 'p-3 rounded-xl bg-black/40 dark:bg-white/[0.02] border border-neutral-200/30 dark:border-white/[0.05] space-y-1'
content = content.replace(old_state3_subbox, new_state3_subbox)

old_state3_reset_btn = 'class="p-2.5 rounded-xl border border-neutral-200 dark:border-neutral-800 text-neutral-400 hover:text-black dark:hover:text-white transition-colors"'
new_state3_reset_btn = 'class="p-2.5 rounded-xl border border-neutral-200/50 dark:border-white/[0.08] text-neutral-400 hover:text-black dark:hover:text-white hover:bg-neutral-50 dark:hover:bg-white/[0.02] transition-colors"'
content = content.replace(old_state3_reset_btn, new_state3_reset_btn)

# Write back to both dashboard.html and app/dashboard.html
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Border softening complete for both dashboard.html and app/dashboard.html!")
