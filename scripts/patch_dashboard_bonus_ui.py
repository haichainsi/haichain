import sys
import time
import re
sys.stdout.reconfigure(encoding='utf-8')

new_ver = f"v47_audit_hardened_{int(time.time()*1000)}"

with open('dashboard.html', 'r', encoding='utf-8') as f:
    dhtml = f.read()

target = """              <div class="text-xl sm:text-2xl font-black text-black dark:text-white tabular-nums">${haiTotal.toLocaleString()} <span class="text-xs font-bold text-neutral-400">HAISI</span></div>
              </div>
              <span class="text-[10px] text-neutral-500 font-sans block">${getVestingText('kpiTokenStandard', lang)}</span>"""

replacement = """              <div class="text-xl sm:text-2xl font-black text-black dark:text-white tabular-nums">${haiTotal.toLocaleString()} <span class="text-xs font-bold text-neutral-400">HAISI</span></div>
              </div>
              ${(alloc.referralBonusTokens && alloc.referralBonusTokens > 0) ? `
              <span class="inline-flex items-center space-x-1 px-2 py-0.5 rounded-md text-[9.5px] font-mono bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 font-bold border border-emerald-500/20">
                <span>🎁 +${alloc.referralBonusTokens.toLocaleString()} Bonus Ref (+5%)</span>
              </span>
              ` : `
              <span class="text-[10px] text-neutral-500 font-sans block">${getVestingText('kpiTokenStandard', lang)}</span>
              `}"""

if target in dhtml:
    dhtml = dhtml.replace(target, replacement, 1)
    print("Added bonus indicator in Vesting Vault card!")
else:
    print("Target not found in dashboard.html!")
    sys.exit(1)

dhtml = re.sub(
    r'/app/sale-controller\.js\?v=[^\"]+',
    f'/app/sale-controller.js?v={new_ver}',
    dhtml
)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dhtml)
with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dhtml)

print("Successfully updated dashboard.html and app/dashboard.html with version:", new_ver)
