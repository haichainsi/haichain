import re

def update_vesting(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Find function renderVestingVaultPage()
    func_start = c.find('function renderVestingVaultPage() {')
    if func_start == -1:
        print(f"renderVestingVaultPage not found in {filepath}")
        return

    # Add activeSaft retrieval and renderSignedContractCardHtml after `const alloc = currentAddress ? allocations[currentAddress] : null;`
    target = 'const alloc = currentAddress ? allocations[currentAddress] : null;'
    replacement = '''const alloc = currentAddress ? allocations[currentAddress] : null;

      // Retrieve any signed SAFT record for the user (by wallet or active device session)
      let activeSaft = null;
      try {
        const rawActive = localStorage.getItem('HAICHAIN_ACTIVE_SAFT');
        if (rawActive) activeSaft = JSON.parse(rawActive);
        if (!activeSaft) {
          const list = JSON.parse(localStorage.getItem('HAICHAIN_SIGNED_SAFT_RECORDS') || '[]');
          if (list && list.length > 0) {
            if (currentAddress) {
              activeSaft = list.find(r => r.wallet && r.wallet.toLowerCase() === currentAddress.toLowerCase()) || list[0];
            } else {
              activeSaft = list[0];
            }
          }
        }
      } catch (_) {}

      function renderSignedContractCardHtml(saft, currentLang) {
        if (!saft) return '';
        const isVi = currentLang === 'vi';
        const formattedAmount = Number(saft.amount || 1000).toLocaleString('en-US');
        const formattedTokens = Number(saft.tokens || Math.round(Number(saft.amount || 1000) / 0.007)).toLocaleString('en-US');
        const dateStr = (saft.timestamp || new Date().toISOString()).replace('T', ' ').substring(0, 19);
        const shortW = saft.wallet ? (saft.wallet.length > 12 ? `${saft.wallet.slice(0, 6)}...${saft.wallet.slice(-6)}` : saft.wallet) : 'N/A';
        const titleText = isVi ? 'Hợp đồng SAFT đã ký' : 'Signed SAFT Agreement';
        const statusBadge = isVi ? 'Đã ký kết • US ESIGN Act' : 'Executed • US ESIGN Act';
        const signatoryLabel = isVi ? 'Người ký' : 'Signatory';
        const amountLabel = isVi ? 'Số tiền đầu tư' : 'Investment';
        const tokensLabel = isVi ? 'Token phân bổ' : 'Allocation';
        const dateLabel = isVi ? 'Thời gian ký' : 'Signed Time';
        const walletLabel = isVi ? 'Ví thụ hưởng:' : 'Beneficiary Wallet:';
        const btnText = isVi ? 'Xem lại hợp đồng đã ký' : 'Review Signed Agreement';

        return `
          <!-- SIGNED SAFT CONTRACT SECTION (STRICT MONOCHROME, ZERO OVERFLOW) -->
          <div class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-4 shadow-xs">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-neutral-100 dark:border-neutral-900 gap-2">
              <div class="space-y-0.5">
                <h3 class="font-bold text-sm sm:text-base text-black dark:text-white leading-snug">
                  ${titleText}
                </h3>
                <p class="text-[11px] text-neutral-400 font-mono">
                  Contract ID: <span class="text-black dark:text-white font-semibold">${saft.contractId || 'SAFT-2026-HAI-001'}</span>
                </p>
              </div>
              <span class="self-start sm:self-auto px-2.5 py-0.5 rounded-md text-[10px] font-mono whitespace-nowrap bg-neutral-100 dark:bg-neutral-900 text-neutral-800 dark:text-neutral-200 border border-neutral-200 dark:border-neutral-800 font-semibold">
                ${statusBadge}
              </span>
            </div>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3 text-xs font-mono">
              <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800">
                <span class="text-neutral-400 block text-[10px]">${signatoryLabel}</span>
                <span class="font-bold text-black dark:text-white truncate block text-[11px] sm:text-xs">${saft.name || 'Investor'}</span>
              </div>
              <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800">
                <span class="text-neutral-400 block text-[10px]">${amountLabel}</span>
                <span class="font-bold text-black dark:text-white block text-[11px] sm:text-xs">$${formattedAmount} USDT</span>
              </div>
              <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800">
                <span class="text-neutral-400 block text-[10px]">${tokensLabel}</span>
                <span class="font-bold text-black dark:text-white block text-[11px] sm:text-xs">${formattedTokens} HAISI</span>
              </div>
              <div class="p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800">
                <span class="text-neutral-400 block text-[10px]">${dateLabel}</span>
                <span class="font-bold text-black dark:text-white block text-[11px] sm:text-xs truncate">${dateStr}</span>
              </div>
            </div>

            <div class="p-2.5 sm:p-3 rounded-xl bg-neutral-50 dark:bg-neutral-900/40 border border-neutral-200/60 dark:border-neutral-800 text-[10px] font-mono break-all text-neutral-500">
              <span class="text-neutral-400">SHA-256 Hash:</span> <span class="text-neutral-700 dark:text-neutral-300">${saft.hashHex || 'N/A'}</span>
            </div>

            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-1">
              <div class="text-[11px] text-neutral-500 font-mono truncate">
                ${walletLabel} <span class="text-black dark:text-white font-semibold">${shortW}</span>
              </div>
              <button onclick="if(window.openSaftPdfModal){window.openSaftPdfModal('${currentLang}');}else{window.openPdfViewerModal('/HAICHAIN_PRESEED_SAFT_AGREEMENT_VI.pdf', 'Thỏa Thuận SAFT');}" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 text-xs font-semibold transition-all cursor-pointer text-center">
                ${btnText}
              </button>
            </div>
          </div>
        `;
      }'''

    c = c.replace(target, replacement, 1)

    # Insert ${renderSignedContractCardHtml(activeSaft, lang)} in State 1
    # Right before `<!-- Lock Box Prompt -->`
    c = c.replace(
        '<!-- Lock Box Prompt -->',
        '${renderSignedContractCardHtml(activeSaft, lang)}\n\n            <!-- Lock Box Prompt -->'
    )

    # Insert in State 2
    # Find State 2 lock box
    target_s2 = '<div class="p-6 sm:p-8 rounded-2xl bg-neutral-50/50 dark:bg-white/[0.015] text-center max-w-xl mx-auto space-y-4">'
    # Only replace in State 2 (after // STATE 2:)
    idx_s2 = c.find('// STATE 2:', func_start)
    if idx_s2 != -1:
        idx_box = c.find(target_s2, idx_s2)
        if idx_box != -1:
            c = c[:idx_box] + '${renderSignedContractCardHtml(activeSaft, lang)}\n\n            ' + c[idx_box:]

    # Insert in State 3
    # Right after `<!-- Official Mainnet Allocation Guarantee Certificate`
    target_s3 = '<!-- Official Mainnet Allocation Guarantee Certificate'
    idx_s3 = c.find('// STATE 3:', func_start)
    if idx_s3 != -1:
        idx_cert = c.find(target_s3, idx_s3)
        if idx_cert != -1:
            c = c[:idx_cert] + '${renderSignedContractCardHtml(activeSaft, lang)}\n\n          ' + c[idx_cert:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated vesting in {filepath}")

update_vesting('dashboard.html')
update_vesting('app/dashboard.html')
