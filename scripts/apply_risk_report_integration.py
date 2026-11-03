# -*- coding: utf-8 -*-
"""
Applies i18n, pdf-modal, and index.html updates for:
1. Menu text "Technical Whitepaper v1.1" -> "Whitepaper" across all 10 languages
2. Risk Report menu clicks open HAICHAIN_RISK_REPORT_{LANG}.pdf in the in-page PDF modal
3. Dynamic switching of Risk Report PDF when changing language inside modal or on the site
4. Exact synchronization between root files and app/ mirrors.
"""

import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"

# =========================================================================
# 1. UPDATE i18n.js & app/i18n.js
# =========================================================================
def update_i18n_file(file_path):
    print(f"[*] Updating {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for nav.whitepaper
    replacements = {
        r'"nav\.whitepaper":\s*"Техникалық Ақ Қағаз v1\.1"': '"nav.whitepaper": "Ақ Қағаз"',
        r'"nav\.whitepaper":\s*"Technical Whitepaper v1\.1"': '"nav.whitepaper": "Whitepaper"',
        r'"nav\.whitepaper":\s*"技术白皮书 v1\.1"': '"nav.whitepaper": "白皮书"',
        r'"nav\.whitepaper":\s*"Livre Blanc Technique v1\.1"': '"nav.whitepaper": "Livre Blanc"',
        r'"nav\.whitepaper":\s*"기술 백서 v1\.1"': '"nav.whitepaper": "백서"',
        r'"nav\.whitepaper":\s*"Libro Blanco Técnico v1\.1"': '"nav.whitepaper": "Libro Blanco"',
        r'"nav\.whitepaper":\s*"Технический Whitepaper v1\.1"': '"nav.whitepaper": "Whitepaper"',
        r'"nav\.whitepaper":\s*"Sách Trắng Kỹ Thuật v1\.1"': '"nav.whitepaper": "Whitepaper"',
        r'"nav\.whitepaper":\s*"तकनीकी श्वेतपत्र v1\.1"': '"nav.whitepaper": "श्वेतपत्र"',
        r'"nav\.whitepaper":\s*"ספר לבן טכני v1\.1"': '"nav.whitepaper": "ספר לבן"'
    }

    count = 0
    for pattern, repl in replacements.items():
        if re.search(pattern, content):
            content = re.sub(pattern, repl, content)
            count += 1
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] {file_path} updated ({count} language entries updated).")

update_i18n_file(os.path.join(WORKSPACE_DIR, "i18n.js"))
update_i18n_file(os.path.join(WORKSPACE_DIR, "app", "i18n.js"))

# =========================================================================
# 2. UPDATE pdf-modal.js & app/pdf-modal.js
# =========================================================================
RISK_REPORT_RESOLVER_CODE = """
  // =========================================================================
  // GLOBAL MULTI-LANGUAGE RISK REPORT RESOLVER (10 LANGUAGES)
  // =========================================================================
  window.getRiskReportPdfForLang = function(lang) {
    const l = (lang || (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en')).toLowerCase();
    const titles = {
      vi: 'Báo Cáo Thẩm Định Rủi Ro & Phòng Thủ Mật Mã HAICHAIN',
      en: 'HAICHAIN Institutional Risk Due Diligence Report',
      zh: 'HAICHAIN 机构级风险尽职调查与安全防御报告',
      ko: 'HAICHAIN 기관용 위험 실사 및 암호학적 보안 감사 보고서',
      fr: 'Rapport de Diligence Raisonnable des Risques Institutionnels HAICHAIN',
      es: 'Informe de Diligencia Debida de Riesgos Institucionales de HAICHAIN',
      ru: 'Отчет об Институциональном Дью-Дилидженсе Рисков HAICHAIN',
      kk: 'HAICHAIN Институционалдық Тәуекелдерді Бағалау Және Сенімділік Есебі',
      hi: 'HAICHAIN संस्थागत जोखिम देय परिश्रम और सुरक्षा ऑडिट रिपोर्ट',
      he: 'דוח בדיקת נאותות סיכונים מוסדיים ואבטחת קריפטוגרפיה של HAICHAIN'
    };
    const title = titles[l] || titles['en'];
    const validLangs = ['en', 'vi', 'zh', 'ko', 'es', 'fr', 'ru', 'kk', 'hi', 'he'];
    const chosenLang = validLangs.includes(l) ? l.toUpperCase() : 'EN';
    return {
      url: `/HAICHAIN_RISK_REPORT_${chosenLang}.pdf`,
      title: title
    };
  };

  window.openRiskReportPdfModal = function(lang) {
    const doc = window.getRiskReportPdfForLang(lang);
    window.openPdfViewerModal(doc.url, doc.title);
  };
"""

def update_pdf_modal_file(file_path):
    print(f"[*] Updating {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add getRiskReportPdfForLang if not already present
    if "window.getRiskReportPdfForLang" not in content:
        # Insert before window.getSaftPdfForLang
        target = "  window.getSaftPdfForLang = function(lang) {"
        if target in content:
            content = content.replace(target, RISK_REPORT_RESOLVER_CODE + "\n" + target)
            print("[+] Added getRiskReportPdfForLang and openRiskReportPdfModal.")

    # 2. Add language synchronization for RISK report
    lang_sync_target = """        } else if (u.includes('MEMO')) {
          const doc = typeof window.getPreseedMemoPdfForLang === 'function' ? window.getPreseedMemoPdfForLang(lang) : null;
          if (doc && doc.url !== currentPdfUrl) window.openPdfViewerModal(doc.url, doc.title);
        }"""
    lang_sync_replacement = """        } else if (u.includes('MEMO')) {
          const doc = typeof window.getPreseedMemoPdfForLang === 'function' ? window.getPreseedMemoPdfForLang(lang) : null;
          if (doc && doc.url !== currentPdfUrl) window.openPdfViewerModal(doc.url, doc.title);
        } else if (u.includes('RISK')) {
          const doc = typeof window.getRiskReportPdfForLang === 'function' ? window.getRiskReportPdfForLang(lang) : null;
          if (doc && doc.url !== currentPdfUrl) window.openPdfViewerModal(doc.url, doc.title);
        }"""
    if "u.includes('RISK')" not in content and lang_sync_target in content:
        content = content.replace(lang_sync_target, lang_sync_replacement)
        print("[+] Added RISK report language switcher listener.")

    # 3. Add document click listener for risk report links
    click_listener = """
  // Global Event Listener for Risk Report links
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('#nav-risk-report-link, [data-mobile-risk-report="true"], [data-risk-report="true"], a[href*="HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT"], a[href*="HAICHAIN_RISK_REPORT"]');
    if (trigger) {
      e.preventDefault();
      e.stopPropagation();
      if (typeof window.closeMobileMenu === 'function') {
        window.closeMobileMenu();
      }
      const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en');
      window.openRiskReportPdfModal(lang);
    }
  }, true);
"""
    if "data-mobile-risk-report" not in content:
        content += "\n" + click_listener
        print("[+] Added global click listener for Risk Report.")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] {file_path} updated.")

update_pdf_modal_file(os.path.join(WORKSPACE_DIR, "pdf-modal.js"))
update_pdf_modal_file(os.path.join(WORKSPACE_DIR, "app", "pdf-modal.js"))

# =========================================================================
# 3. UPDATE index.html & app/index.html
# =========================================================================
def update_index_file(file_path):
    print(f"[*] Updating {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update mobile menu text from Technical Whitepaper v1.1 to Whitepaper
    content = content.replace(
        '<span data-i18n="nav.whitepaper">Technical Whitepaper v1.1</span>',
        '<span data-i18n="nav.whitepaper">Whitepaper</span>'
    )

    # 2. Update nav-risk-report-link in desktop navbar
    old_nav_risk = '<a href="/docs/HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT.md" target="_blank" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1.5 cursor-pointer text-xs px-2.5 py-1 rounded-full bg-neutral-100 dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-800 text-neutral-800 dark:text-neutral-200" id="nav-risk-report-link" title="Institutional Risk Due Diligence Report">'
    new_nav_risk = '<a href="/HAICHAIN_RISK_REPORT_EN.pdf" target="_blank" onclick="if (window.openRiskReportPdfModal) { event.preventDefault(); const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem(\'haichain_lang\') || \'en\'); window.openRiskReportPdfModal(lang); }" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1.5 cursor-pointer text-xs px-2.5 py-1 rounded-full bg-neutral-100 dark:bg-neutral-900 border border-neutral-300 dark:border-neutral-800 text-neutral-800 dark:text-neutral-200" id="nav-risk-report-link" title="Institutional Risk Due Diligence Report" data-risk-report="true">'
    if old_nav_risk in content:
        content = content.replace(old_nav_risk, new_nav_risk)
        print("[+] Updated desktop nav-risk-report-link.")

    # 3. Update mobile risk report link
    old_mobile_risk = '<a href="/docs/HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT.md" target="_blank" onclick="if (typeof window.closeMobileMenu === \'function\') { window.closeMobileMenu(); }" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" data-mobile-risk-report="true">'
    new_mobile_risk = '<a href="/HAICHAIN_RISK_REPORT_EN.pdf" target="_blank" onclick="if (typeof window.closeMobileMenu === \'function\') { window.closeMobileMenu(); } if (window.openRiskReportPdfModal) { event.preventDefault(); const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem(\'haichain_lang\') || \'en\'); window.openRiskReportPdfModal(lang); }" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" data-mobile-risk-report="true">'
    if old_mobile_risk in content:
        content = content.replace(old_mobile_risk, new_mobile_risk)
        print("[+] Updated mobile-risk-report-link.")

    # 4. Bump cachebuster for i18n.js and pdf-modal.js
    content = re.sub(r'i18n\.js\?v=[^"\'\s>]+', 'i18n.js?v=v1.2.8_risk_pdf', content)
    content = re.sub(r'pdf-modal\.js\?v=[^"\'\s>]+', 'pdf-modal.js?v=v1.2.8_risk_pdf', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[✓] {file_path} updated.")

update_index_file(os.path.join(WORKSPACE_DIR, "index.html"))
update_index_file(os.path.join(WORKSPACE_DIR, "app", "index.html"))

print("\n[*] All updates applied successfully!")
