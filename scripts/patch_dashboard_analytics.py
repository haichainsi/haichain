import sys
import time
sys.stdout.reconfigure(encoding='utf-8')

new_ver = f"v44_referral_click_telemetry_{int(time.time()*1000)}"

with open('dashboard.html', 'r', encoding='utf-8') as f:
    dhtml = f.read()

# 1. Bump cachebuster
import re
dhtml = re.sub(
    r'/app/sale-controller\.js\?v=[^\"]+',
    f'/app/sale-controller.js?v={new_ver}',
    dhtml
)

# 2. Add quick telemetry row in Vesting Vault
target_share_box = """            <!-- Commission Summary -->"""
replacement_share_box = """            <!-- Referral Click Telemetry Quick Bar in Vesting -->
            ${(() => {
              const localClicks = JSON.parse(localStorage.getItem('haichain_referral_clicks') || '[]')
                .filter(c => c.ref && c.ref.toLowerCase() === currentAddress.toLowerCase());
              const totalClicks = localClicks.length;
              const uniqueClicks = localClicks.filter(c => c.isUnique).length || totalClicks;
              return `
              <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200 dark:border-neutral-800 flex items-center justify-between text-[11px] font-mono">
                <div class="flex items-center space-x-2">
                  <i data-lucide="bar-chart-3" class="w-3.5 h-3.5 text-emerald-500"></i>
                  <span class="text-neutral-500 font-sans">${lang === 'vi' ? 'Lượt click link:' : 'Link Clicks:'}</span>
                  <strong class="text-black dark:text-white font-bold">${totalClicks}</strong>
                  <span class="text-neutral-400 font-sans">(${uniqueClicks} ${lang === 'vi' ? 'khách độc nhất' : 'unique'})</span>
                </div>
                <button onclick="window.switchTab('tab-preseed')" class="text-[10px] text-neutral-400 hover:text-black dark:hover:text-white underline font-sans cursor-pointer">
                  ${lang === 'vi' ? 'Xem báo cáo chi tiết →' : 'View full analytics →'}
                </button>
              </div>
              `;
            })()}

            <!-- Commission Summary -->"""

if target_share_box in dhtml:
    dhtml = dhtml.replace(target_share_box, replacement_share_box, 1)
    print("Added referral telemetry quick bar in dashboard.html")
else:
    print("Could not find target_share_box in dashboard.html")

# Write to dashboard.html and app/dashboard.html
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dhtml)

with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dhtml)

print("Successfully updated dashboard.html and app/dashboard.html with version:", new_ver)
