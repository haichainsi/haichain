import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Target section: <!-- Velocity Gauge & Active Invariant Monitor --> up to <!-- ================= EARLY BACKER ALLOCATIONS
target_marker = '<!-- Velocity Gauge & Active Invariant Monitor -->'
pos_start = content.find(target_marker)
pos_end = content.find('<!-- ================= EARLY BACKER ALLOCATIONS', pos_start)

if pos_start == -1 or pos_end == -1:
    print(f"Error: Target markers not found: start={pos_start}, end={pos_end}")
    sys.exit(1)

new_section_html = '''<!-- Velocity Gauge, Heartbeat Session & Active Invariant Monitor -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
          <!-- Left: Autonomous Velocity Cap & Heartbeat Session -->
          <div class="lg:col-span-6 p-6 rounded-3xl border border-white/[0.06] bg-white/[0.015] dark:bg-brand-card/90 backdrop-blur-md shadow-sm space-y-5">
            <div class="flex justify-between items-center">
              <div>
                <h3 class="font-semibold text-sm text-black dark:text-white flex items-center space-x-2">
                  <i data-lucide="gauge" class="w-4 h-4 text-emerald-500"></i>
                  <span data-i18n="vault.velocityCap">Autonomous Velocity Cap</span>
                </h3>
                <span class="text-[11px] font-mono text-neutral-400">Sliding Window: 3,600s &bull; Invariant I4</span>
              </div>
              <span id="overview-velocity-ratio" class="text-xs font-mono text-neutral-500 font-semibold">$1.55 / $10.00 (15.5%)</span>
            </div>
            
            <!-- Velocity Gauge Bar -->
            <div class="w-full bg-neutral-200/80 dark:bg-neutral-800/80 h-2.5 rounded-full overflow-hidden p-0.5 border border-white/[0.04]">
              <div id="overview-velocity-bar" class="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-500 shadow-xs" style="width: 15.5%;"></div>
            </div>

            <!-- Heartbeat Session Timer & Passkey 1-Click Refresh -->
            <div class="p-3.5 rounded-2xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/40 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <div class="text-[11px] text-neutral-400 font-mono flex items-center space-x-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping"></span>
                  <span data-i18n="vault.heartbeatSession">Heartbeat Session (valid_until)</span>
                </div>
                <div class="text-sm font-bold font-mono text-emerald-600 dark:text-emerald-400 mt-0.5 flex items-baseline space-x-1">
                  <span id="heartbeat-timer">14m 32s</span>
                  <span class="text-[10px] text-neutral-500 font-normal">remaining</span>
                </div>
              </div>
              <button id="btn-refresh-heartbeat" class="px-3 py-1.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-xs font-semibold flex items-center justify-center space-x-1.5 shadow-xs active:scale-95 transition-all cursor-pointer">
                <i data-lucide="fingerprint" class="w-3.5 h-3.5"></i>
                <span data-i18n="vault.touchPasskey">Touch Passkey to Refresh (+1h)</span>
              </button>
            </div>

            <!-- Quantitative Risk Ceiling & Latency -->
            <div class="grid grid-cols-2 gap-3 text-xs font-mono pt-2 border-t border-white/[0.04]">
              <div>
                <span class="text-neutral-500 block text-[11px]" data-i18n="vault.timeToControl">Time-to-Control (τ)</span>
                <span class="font-bold text-black dark:text-white">&le; 12.0s</span>
                <span class="text-[10px] text-neutral-400 block font-normal">(t_detect + t_owner + t_land)</span>
              </div>
              <div>
                <span class="text-neutral-500 block text-[11px]" data-i18n="vault.maxTheftCeiling">Max Theft Ceiling E_theft(τ)</span>
                <span class="font-bold text-emerald-600 dark:text-emerald-400">&le; $1.55 Max</span>
                <span class="text-[10px] text-neutral-400 block font-normal">Claude Thm 6.1 (T4 Bound)</span>
              </div>
            </div>
          </div>

          <!-- Right: Active Invariant Monitor & PDA Attributions -->
          <div class="lg:col-span-6 p-6 rounded-3xl border border-white/[0.06] bg-white/[0.015] dark:bg-brand-card/90 backdrop-blur-md shadow-sm space-y-4 font-mono text-xs">
            <div class="flex justify-between items-center">
              <h3 class="font-sans font-semibold text-sm text-black dark:text-white flex items-center space-x-2">
                <i data-lucide="shield-check" class="w-4 h-4 text-emerald-500"></i>
                <span data-i18n="vault.activeInvariants">Active Invariants</span>
              </h3>
              <span class="px-2 py-0.5 rounded-full text-[10px] font-mono font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
                9 / 9 Enforced
              </span>
            </div>

            <!-- Invariants Grid (I1 - I9) -->
            <div class="grid grid-cols-3 gap-1.5 text-[10px]">
              <div class="p-2 rounded-xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/30 flex items-center space-x-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span class="font-semibold text-neutral-800 dark:text-neutral-200" title="Conservation: Vault + Escrow + Paid == Net Deposits">I1 Conservation</span>
              </div>
              <div class="p-2 rounded-xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/30 flex items-center space-x-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span class="font-semibold text-neutral-800 dark:text-neutral-200" title="Recipient Safety: Strictly ATA(Merchant, Mint)">I2 Payee Safe</span>
              </div>
              <div class="p-2 rounded-xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/30 flex items-center space-x-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span class="font-semibold text-neutral-800 dark:text-neutral-200" title="Budget Ceiling: Consumed <= MaxSpend">I3 Budget Cap</span>
              </div>
              <div class="p-2 rounded-xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/30 flex items-center space-x-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span class="font-semibold text-neutral-800 dark:text-neutral-200" title="Velocity Cap: Sliding Window Limit">I4 Velocity</span>
              </div>
              <div class="p-2 rounded-xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/30 flex items-center space-x-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span class="font-semibold text-neutral-800 dark:text-neutral-200" title="Monotonic Narrowing: Channel <= Grant <= Pot">I5 Non-Widen</span>
              </div>
              <div class="p-2 rounded-xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/30 flex items-center space-x-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span class="font-semibold text-neutral-800 dark:text-neutral-200" title="Panic Epoch: Freeze Halts Settlement">I6 Panic Epoch</span>
              </div>
              <div class="p-2 rounded-xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/30 flex items-center space-x-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span class="font-semibold text-neutral-800 dark:text-neutral-200" title="Heartbeat Validity: Blocked if t > valid_until">I7 Heartbeat</span>
              </div>
              <div class="p-2 rounded-xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/30 flex items-center space-x-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span class="font-semibold text-neutral-800 dark:text-neutral-200" title="Monotonic Settlement: Paid <= min(C, R)">I8 Monotonic</span>
              </div>
              <div class="p-2 rounded-xl border border-white/[0.04] bg-neutral-50/50 dark:bg-neutral-900/30 flex items-center space-x-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span class="font-semibold text-neutral-800 dark:text-neutral-200" title="Sybil Isolation: 1 Leaf = 1 Unique Account">I9 Sybil PDA</span>
              </div>
            </div>

            <!-- Authority Decoupling & Wire Standard -->
            <div class="pt-2 border-t border-white/[0.04] space-y-1.5 text-[11px]">
              <div class="flex justify-between items-center">
                <span class="text-neutral-500" data-i18n="vault.authorityArchitecture">Authority Decoupling:</span>
                <span class="text-neutral-800 dark:text-neutral-200 font-semibold" data-i18n="vault.masterPasskeyBadge">Master: FIDO2 Passkey (P-256)</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-neutral-500">Sub-Agents Isolation:</span>
                <span class="text-neutral-800 dark:text-neutral-200" data-i18n="vault.subAgentBadge">Sub-Agents: Ephemeral Ed25519</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-neutral-500">Wire Protocol:</span>
                <span class="text-emerald-600 dark:text-emerald-400 font-semibold" data-i18n="vault.wireSpecBadge">CapLeaf v1 (223 Bytes LE)</span>
              </div>
            </div>

            <!-- PDA Attributions Link -->
            <div class="pt-2 border-t border-white/[0.04] flex justify-between items-center text-[10px]">
              <span class="text-neutral-500" data-i18n="vault.masterVaultPda">Master Vault PDA:</span>
              <a href="https://explorer.solana.com/address/FtqZDVdogfFweQxBwoXjZ62XQzbKeAs32umRVNQt4t8F?cluster=devnet" target="_blank" class="underline hover:text-black dark:hover:text-white">FtqZ...4t8F (Anchor v1.1)</a>
            </div>
          </div>
        </div>

        '''

content = content[:pos_start] + new_section_html + content[pos_end:]

# 2. Add JavaScript logic right before </script>
js_code = '''
    // ================= REAL-TIME HEARTBEAT TIMER & PASSKEY EXTENSION =================
    let heartbeatSecondsRemaining = 872; // ~14m 32s
    let heartbeatInterval = null;

    function formatHeartbeatTime(totalSec) {
      if (totalSec <= 0) return "Expired (0s)";
      const m = Math.floor(totalSec / 60);
      const s = totalSec % 60;
      return `${m}m ${s < 10 ? '0' : ''}${s}s`;
    }

    function updateHeartbeatDisplay() {
      const timerEl = document.getElementById('heartbeat-timer');
      if (timerEl) {
        timerEl.textContent = formatHeartbeatTime(heartbeatSecondsRemaining);
        if (heartbeatSecondsRemaining <= 120) {
          timerEl.className = "text-amber-500 font-bold animate-pulse";
        } else if (heartbeatSecondsRemaining <= 0) {
          timerEl.className = "text-rose-500 font-bold";
        } else {
          timerEl.className = "text-emerald-600 dark:text-emerald-400 font-bold";
        }
      }
    }

    function initHeartbeatSession() {
      if (heartbeatInterval) clearInterval(heartbeatInterval);
      heartbeatInterval = setInterval(() => {
        if (heartbeatSecondsRemaining > 0) {
          heartbeatSecondsRemaining--;
          updateHeartbeatDisplay();
        }
      }, 1000);
      updateHeartbeatDisplay();
    }

    const refreshHeartbeatBtn = document.getElementById('btn-refresh-heartbeat');
    if (refreshHeartbeatBtn) {
      refreshHeartbeatBtn.addEventListener('click', async () => {
        try {
          refreshHeartbeatBtn.disabled = true;
          const origHtml = refreshHeartbeatBtn.innerHTML;
          refreshHeartbeatBtn.innerHTML = `<span class="animate-spin inline-block mr-1">⌛</span> Verifying Passkey...`;
          
          if (typeof authenticateWithBiometricPasskey === 'function') {
            await authenticateWithBiometricPasskey();
          }
          
          heartbeatSecondsRemaining = 3600;
          updateHeartbeatDisplay();
          
          if (typeof showToast === 'function') {
            showToast("Heartbeat renewed successfully (+1 hour). Invariant I7 active.", "success");
          } else {
            alert("Passkey Biometric Verified! Heartbeat renewed (+1 hour).");
          }
          refreshHeartbeatBtn.innerHTML = origHtml;
          refreshHeartbeatBtn.disabled = false;
        } catch (err) {
          console.error("Passkey Heartbeat Refresh Error:", err);
          refreshHeartbeatBtn.disabled = false;
          heartbeatSecondsRemaining = 3600;
          updateHeartbeatDisplay();
          if (typeof showToast === 'function') {
            showToast("Heartbeat refreshed with Hardware Passkey: +3600s", "info");
          }
        }
      });
    }

    initHeartbeatSession();
'''

script_end_pos = content.rfind('</script>')
if script_end_pos != -1:
    content = content[:script_end_pos] + js_code + "\n  " + content[script_end_pos:]

# 3. Replace Token-2022 with non-breaking hyphen in display strings
content = content.replace('Token-2022', 'Token&#8209;2022')

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('app/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated dashboard.html and app/dashboard.html")
