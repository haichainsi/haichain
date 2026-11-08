import re, sys, os

sys.stdout.reconfigure(encoding='utf-8')

appendix_headers = {
    'EN': '## APPENDIX A: TECHNICAL ADDENDUM V1.1 — CAPLEAF V1 BINARY ARCHITECTURE, 9 INVARIANTS, THREAT MODEL & BOUNDED THEFT EXPOSURE',
    'VI': '## PHỤ LỤC A: ĐẶC TẢ KỸ THUẬT V1.1 — CẤU TRÚC NHỊ PHÂN CAPLEAF V1, 9 BẤT BIẾN TOÁN HỌC, MÔ HÌNH ĐE DỌA & TRẦN RỦI RO',
    'ZH': '## 附录 A: 技术增补规范 V1.1 — CAPLEAF V1 二进制架构、9大数学不变量、威胁模型与损失上限',
    'KO': '## 부록 A: 기술 보충 명세 V1.1 — CAPLEAF V1 바이너리 아키텍처, 9대 수학적 불변성, 위협 모델 및 손실 상한',
    'ES': '## APÉNDICE A: ADENDA TÉCNICA V1.1 — ARQUITECTURA BINARIA CAPLEAF V1, 9 INVARIANTES, MODELO DE AMENAZAS Y TECHO DE RIESGO',
    'FR': '## ANNEXE A: ADDENDA TECHNIQUE V1.1 — ARCHITECTURE BINAIRE CAPLEAF V1, 9 INVARIANTS, MODÈLE DE MENACE ET PLAFOND DE RISQUE',
    'RU': '## ПРИЛОЖЕНИЕ A: ТЕХНИЧЕСКИЙ АДДЕНДУМ V1.1 — БИНАРНАЯ АРХИТЕКТУРА CAPLEAF V1, 9 ИНВАРИАНТОВ, МОДЕЛЬ УГРОЗ И ПРЕДЕЛ РИСКА',
    'KK': '## A ҚОСЫМШАСЫ: ТЕХНИКАЛЫҚ ҚОСЫМША V1.1 — CAPLEAF V1 ЕКІЛІК АРХИТЕКТУРАСЫ, 9 ИНВАРИАНТ, ҚАУІП-ҚАТЕР МОДЕЛІ ЖӘНЕ ШЫҒЫН ШЕГІ',
    'HI': '## परिशिष्ट A: तकनीकी परिशिष्ट V1.1 — CAPLEAF V1 बाइनरी वास्तुकला, 9 गणितीय नियम, खतरा मॉडल और अधिकतम जोखिम सीमा',
    'HE': '## נספח א: תוספת טכנית V1.1 — ארכיטקטורה בינארית CAPLEAF V1, 9 אינווריאנטים, מודל איומים ותקרת סיכון'
}

langs = ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']

for lang in langs:
    fname = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md"
    if not os.path.exists(fname):
        continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Fix corrupted escape sequences
    text = text.replace('\text', r'\text')
    text = text.replace('\tau', r'\tau')
    text = text.replace('\times', r'\times')
    text = text.replace('\right', r'\right')
    text = text.replace('\rceil', r'\rceil')
    text = text.replace('\lceil', r'\lceil')
    text = text.replace('\neg', r'\neg')
    text = text.replace('eg\text', r'\neg \text')
    text = text.replace('eg\\text', r'\neg \text')
    
    # Clean broken newline in \right)
    text = re.sub(r'\\sum_\{i:\\, m_i \\in \\mathcal\{A\}\} E_i\(\\tau\)\s*\r?\n\s*ight\)', 
                  r'\\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)', text)
    text = re.sub(r'\\sum_\{i:\\, m_i \\in \\mathcal\{A\}\} E_i\(\\tau\)\s*\r?\n\s*\\right\)', 
                  r'\\sum_{i:\\, m_i \\in \\mathcal{A}} E_i(\\tau)\\right)', text)

    # Clean broken newline in \neg\text{pot.frozen}
    text = re.sub(r';\s*\r?\n\s*eg\\text\{pot\.frozen\}', r' ;\\land; \\neg \\text{pot.frozen}', text)
    text = re.sub(r';\s*\r?\n\s*\\neg\s*\\text\{pot\.frozen\}', r' ;\\land; \\neg \\text{pot.frozen}', text)

    # Clean broken newline in \rceil
    text = re.sub(r'\\lceil\s*\\tau\s*/\s*\\omega_p\s*\r?\n\s*ceil\$', r'\\lceil \\tau / \\omega_p \\rceil$', text)
    text = re.sub(r'\\lceil\s*\\tau\s*/\s*\\omega_p\s*\r?\n\s*\\rceil\$', r'\\lceil \\tau / \\omega_p \\rceil$', text)

    # Fix 2\times
    text = re.sub(r'2\s*imes', r'2\\times', text)

    # 2. Fix Section header at the end (from duplicate 12 to Appendix A)
    # Match the last section header
    last_sec_pattern = re.compile(r'##\s*(?:12|14)\.\s*(?:TECHNICAL APPENDIX|PHỤ LỤC|技术附录|기술 부록|APÉNDICE|ANNEXE|ТЕХНИЧЕСКОЕ ПРИЛОЖЕНИЕ|ТЕХНИКАЛЫҚ ҚОСЫМША|तकनीकी परिशिष्ट|נספח).*$', re.MULTILINE | re.IGNORECASE)
    if last_sec_pattern.search(text):
        text = last_sec_pattern.sub(appendix_headers[lang], text)
        print(f"[{lang}] Updated duplicate Section 12 header to Appendix A header")

    # 3. Fix EN ## 9.6 to ### 9.6
    if lang == 'EN':
        text = text.replace('## 9.6. Zero-Knowledge Ephemeral DIDs', '### 9.6. Zero-Knowledge Ephemeral DIDs')

    # 4. Fix clumped lists (missing blank line before lists)
    lines = text.splitlines()
    new_lines = []
    for i in range(len(lines)):
        curr = lines[i]
        if i > 0:
            prev = lines[i-1]
            # If current line starts a list (*, -, 1.)
            is_list_start = (curr.startswith('* ') or curr.startswith('- ') or re.match(r'^\d+\.\s', curr))
            is_prev_list = (prev.startswith('* ') or prev.startswith('- ') or re.match(r'^\d+\.\s', prev))
            is_prev_header = prev.startswith('#')
            is_prev_blank = (prev.strip() == '')
            is_in_code_block = False # code blocks start with ```
            
            # If current line is a list item and previous line is non-empty normal text, insert blank line
            if is_list_start and not is_prev_list and not is_prev_header and not is_prev_blank:
                # Don't add blank line if inside a table or fenced code
                # Check if prev line is not a table row '|'
                if not prev.startswith('|') and not curr.startswith('|'):
                    new_lines.append('')
        new_lines.append(curr)

    fixed_text = '\n'.join(new_lines) + '\n'

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(fixed_text)

    # Also copy to app/
    app_fname = os.path.join('app', fname)
    with open(app_fname, 'w', encoding='utf-8') as f:
        f.write(fixed_text)

    print(f"[{lang}] Cleaned escape chars, appendix headers, and list spacing ({len(new_lines)} lines)")

print("All 10 markdown whitepapers successfully sanitized!")
