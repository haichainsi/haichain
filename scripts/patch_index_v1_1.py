import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for filepath in ['index.html', 'app/index.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update fallback text for tech.done1
    content = re.sub(
        r'<span data-i18n="tech\.done1">[^<]*</span>',
        '<span data-i18n="tech.done1">Solana Rust Anchor Kernel v1.1 (Program ID: DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk) enforcing 9 mathematical invariants (I1 - I9) & CapLeaf v1 (223 Bytes LE).</span>',
        content
    )

    # 2. Update fallback text for tech.done2
    content = re.sub(
        r'<span data-i18n="tech\.done2">[^<]*</span>',
        '<span data-i18n="tech.done2">Passed 72/72 automated formal verification tests (407ms) across 6 test suites with Claude Theorem 6.1 bounded risk exposure. External audits with OtterSec & Neodyme scheduled prior to Mainnet TGE.</span>',
        content
    )

    # 3. Update fallback text for roadmap.stage1Item1
    content = re.sub(
        r'<span data-i18n="roadmap\.stage1Item1">[^<]*</span>',
        '<span data-i18n="roadmap.stage1Item1">Anchor Kernel v1.1 & CapLeaf v1 (223 Bytes Wire Schema)</span>',
        content
    )

    # 4. Update fallback text for footer.certified
    content = re.sub(
        r'<span data-i18n="footer\.certified">[^<]*</span>',
        '<span data-i18n="footer.certified">v1.1 PRODUCTION CERTIFIED (CapLeaf v1 & 9 Invariants)</span>',
        content
    )

    # 5. Update mobile nav fallback text for nav.whitepaper
    content = re.sub(
        r'<span data-i18n="nav\.whitepaper">Technical Whitepaper v1\.0</span>',
        '<span data-i18n="nav.whitepaper">Technical Whitepaper v1.1</span>',
        content
    )

    # 6. Add nav-risk-report-link next to nav-whitepaper-link in desktop nav
    if 'id="nav-risk-report-link"' not in content:
        target_desktop = 'id="nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">\n\n          <span data-i18n="nav.whitepaper">Whitepaper</span>\n\n        </a>'
        if target_desktop in content:
            replacement_desktop = target_desktop + '\n\n        <a href="/docs/HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT.md" target="_blank" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1.5 cursor-pointer text-xs px-2.5 py-1 rounded-full bg-neutral-100 dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-800 text-neutral-800 dark:text-neutral-200" id="nav-risk-report-link" title="Institutional Risk Due Diligence Report">\n          <i data-lucide="shield-alert" class="w-3.5 h-3.5 text-emerald-500"></i>\n          <span data-i18n="nav.riskReport">Institutional Risk Report</span>\n        </a>'
            content = content.replace(target_desktop, replacement_desktop)
            print(f"Added desktop risk report link in {filepath}")
        else:
            print(f"Warning: target_desktop not found exactly in {filepath}")

    # 7. Add mobile risk report link in mobile nav
    if 'data-mobile-risk-report="true"' not in content:
        target_mobile = 'id="mobile-nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">\n        <span data-i18n="nav.whitepaper">Technical Whitepaper v1.1</span>\n        <i data-lucide="file-text" class="w-4 h-4 text-neutral-400"></i>\n      </a>'
        if target_mobile in content:
            replacement_mobile = target_mobile + '\n      <a href="/docs/HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT.md" target="_blank" onclick="if (typeof window.closeMobileMenu === \'function\') { window.closeMobileMenu(); }" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" data-mobile-risk-report="true">\n        <span data-i18n="nav.riskReport">Institutional Risk Report</span>\n        <i data-lucide="shield-alert" class="w-4 h-4 text-emerald-500"></i>\n      </a>'
            content = content.replace(target_mobile, replacement_mobile)
            print(f"Added mobile risk report link in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated index.html and app/index.html successfully.")
