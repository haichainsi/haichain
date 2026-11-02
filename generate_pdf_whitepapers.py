# -*- coding: utf-8 -*-
"""
HAICHAIN International Whitepaper PDF Generator
Compiles Markdown Whitepapers into Institutional-Grade PDF Documents
Using Headless Browser Engine with Paged Media CSS
Style: 100% Borderless Minimalist Typography (Zero Borders, Zero Lines, Dedicated TOC Page)
Cover: Black Premium with Official White Logo (Zero Border Lines)
Token: $HAISI
"""

import os
import re
import base64
import subprocess
import markdown

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"
LOGO_PATH = os.path.join(WORKSPACE_DIR, "assets", "haichain-official-logo-white.png")

def get_logo_base64():
    """Reads the official Haichain white logo and returns a base64 data URI."""
    if os.path.exists(LOGO_PATH):
        with open(LOGO_PATH, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

def format_math(text):
    """Convert common LaTeX math expressions to clean semantic HTML.
    Guarantees:
    - Never modifies text inside code blocks ``` ... ``` or inline code `...`
    - Never treats escaped dollars \$ as math delimiters
    - Never treats currency amounts (e.g. $5.00, $0.007, $100) or token tickers ($HAISI) as inline math
    - Only processes genuine LaTeX math formulas: display math $$ ... $$ and explicit inline math $...$
    """
    code_blocks = []
    def save_cb(m):
        idx = len(code_blocks)
        code_blocks.append(m.group(0))
        return f"__MATH_CB_PLACEHOLDER_{idx}__"

    # 1. Protect code blocks ``` ... ``` and inline code `...`
    text = re.sub(r'```.*?```', save_cb, text, flags=re.DOTALL)
    text = re.sub(r'`[^`\n]+`', save_cb, text)

    # 2. Display math $$ ... $$
    def replace_display_math(match):
        expr = match.group(1).strip()
        expr_html = latex_to_html(expr)
        return f'<div class="math-display">{expr_html}</div>'

    text = re.sub(r'\$\$(.*?)\$\$', replace_display_math, text, flags=re.DOTALL)

    # 3. Inline math $ ... $
    def replace_inline_math(match):
        expr = match.group(1).strip()
        # Exclude currency or numbers or tickers (e.g. $100, $0.007, $HAISI, $USDT, $SOL, etc.)
        if re.match(r'^\d', expr) or expr.startswith('HAISI') or expr.startswith('USDT') or expr.startswith('USDC') or expr.startswith('SOL'):
            return match.group(0)
        expr_html = latex_to_html(expr)
        return f'<span class="math-inline">{expr_html}</span>'

    text = re.sub(r'(?<!\\)\$(?![\s\d])(.*?)(?<![\s\\\$])\$', replace_inline_math, text)

    # 4. Clean escaped \$ to regular $
    text = text.replace(r'\$', '$')

    # 5. Restore code blocks
    for idx, cb in enumerate(code_blocks):
        cleaned_cb = cb.replace(r'\$', '$')
        text = text.replace(f"__MATH_CB_PLACEHOLDER_{idx}__", cleaned_cb)

    return text

def latex_to_html(tex):
    """Substitutes LaTeX macros with clean Unicode/HTML entities."""
    s = tex
    s = re.sub(r'\\mathbf\{([^}]+)\}', r'<b>\1</b>', s)
    s = re.sub(r'\\textbf\{([^}]+)\}', r'<b>\1</b>', s)
    s = re.sub(r'\\text\{([^}]+)\}', r'<span class="math-text">\1</span>', s)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1 &frasl; \2)', s)
    
    # Subscripts and superscripts
    s = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', s)
    s = re.sub(r'_([a-zA-Z0-9])', r'<sub>\1</sub>', s)
    s = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', s)
    s = re.sub(r'\^([a-zA-Z0-9])', r'<sup>\1</sup>', s)
    
    # Symbols
    symbols = {
        r'\times': '&times;',
        r'\iff': '&hArr;',
        r'\implies': '&rArr;',
        r'\to': '&rarr;',
        r'\leftarrow': '&larr;',
        r'\forall': '&forall;',
        r'\exists': '&exist;',
        r'\ge': '&ge;',
        r'\le': '&le;',
        r'\ne': '&ne;',
        r'\approx': '&asymp;',
        r'\equiv': '&equiv;',
        r'\pm': '&plusmn;',
        r'\in': '&isin;',
        r'\cdot': '&middot;',
        r'\sum': '&sum;',
        r'\prod': '&prod;',
        r'\Delta': '&Delta;',
        r'\alpha': '&alpha;',
        r'\beta': '&beta;',
        r'\gamma': '&gamma;',
        r'\tau': '&tau;',
        r'\pi': '&pi;',
        r'\mu': '&mu;',
        r'\sigma': '&sigma;',
        r'\epsilon': '&epsilon;',
        r'\theta': '&theta;',
        r'\lambda': '&lambda;',
        r'\omega': '&omega;',
        r'\Omega': '&Omega;',
        r'\blacksquare': '&#9632;',
        r'\parallel': '||',
        r'\|': '||',
        r'\,': ' ',
        r'\quad': ' &nbsp; ',
        r'\qquad': ' &nbsp; &nbsp; '
    }
    for macro, rep in symbols.items():
        s = s.replace(macro, rep)
    return s

def process_callouts(html):
    """Transforms blockquote alerts into pure unboxed academic remarks."""
    html = re.sub(
        r'<blockquote>\s*<p>\s*\[!NOTE\]\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">NOTE</p><p class="remark-body">\1</p></div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p>\s*\[!IMPORTANT\]\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">IMPORTANT NOTICE</p><p class="remark-body">\1</p></div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p>\s*\[!WARNING\]\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">SYSTEM INVARIANT WARNING</p><p class="remark-body">\1</p></div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p>\s*<strong>A Note to Institutional Allocators(.*?)</strong>\s*<br\s*/?>\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">STRATEGIC NOTE: INSTITUTIONAL ALLOCATORS & ARCHITECTS</p><p class="remark-body">\2</p></div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p>\s*<strong>Thông Điệp Chiến Lược Dành Cho Các Nhà Đầu Tư Thể Chế(.*?)</strong>\s*<br\s*/?>\s*(.*?)</p>\s*</blockquote>',
        r'<div class="academic-remark"><p class="remark-lead">THÔNG ĐIỆP CHIẾN LƯỢC: NHÀ ĐẦU TƯ THỂ CHẾ & KỸ SƯ HỆ THỐNG</p><p class="remark-body">\2</p></div>',
        html, flags=re.DOTALL
    )
    return html

def build_pdf_from_markdown(md_filename, pdf_filename, lang="en"):
    md_path = os.path.join(WORKSPACE_DIR, md_filename)
    pdf_path = os.path.join(WORKSPACE_DIR, pdf_filename)
    html_path = os.path.join(WORKSPACE_DIR, md_filename.replace('.md', '_pdf_temp.html'))
    
    print(f"[*] Processing {md_filename} -> {pdf_filename}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # Pre-process LaTeX math before Markdown parser treats it as markup
    text_with_math = format_math(raw_text)

    # Separate frontmatter, dedicated TOC page, and body
    if lang == "en":
        toc_pattern = r'(## TABLE OF CONTENTS\s*\n\n.*?)(?=\n---\s*\n\s*## 1\.|\n## 1\. )'
    elif lang == "zh":
        toc_pattern = r'(## 目录[^\n]*\s*\n\n.*?)(?=\n---\s*\n\s*## 1\.|\n## 1\. )'
    elif lang == "ko":
        toc_pattern = r'(## 목차[^\n]*\s*\n\n.*?)(?=\n---\s*\n\s*## 1\.|\n## 1\. )'
    elif lang == "es":
        toc_pattern = r'(## [^\n]*ÍNDICE[^\n]*\s*\n\n.*?)(?=\n---\s*\n\s*## 1\.|\n## 1\. )'
    elif lang == "fr":
        toc_pattern = r'(## TABLE DES MATIÈRES[^\n]*\s*\n\n.*?)(?=\n---\s*\n\s*## 1\.|\n## 1\. )'
    elif lang == "ru":
        toc_pattern = r'(## [^\n]*(?:СОДЕРЖАНИЕ|TABLE OF CONTENTS)[^\n]*\s*\n\n.*?)(?=\n---\s*\n\s*## 1\.|\n## 1\. |\n- \*\*1\.)'
    elif lang == "vi":
        toc_pattern = r'(## M[^\n]*L[^\n]*C[^\n]*\s*\n\n.*?)(?=\n---\s*\n\s*## |\n## T|\n## 1\.)'
    elif lang == "he":
        toc_pattern = r'(## [^\n]*(?:תוכן העניינים|TABLE OF CONTENTS)[^\n]*\s*\n\n.*?)(?=\n---\s*\n\s*## 1\.|\n## 1\. )'
    else:
        toc_pattern = r'(## [^\n]*TABLE OF CONTENTS[^\n]*\s*\n\n.*?)(?=\n---\s*\n\s*## 1\.|\n## 1\. )'
    
    m = re.search(toc_pattern, text_with_math, re.DOTALL)
    md_converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
    
    if m:
        frontmatter_text = text_with_math[:m.start()].strip()
        toc_text = m.group(1).strip()
        body_text = text_with_math[m.end():].strip()
        body_text = re.sub(r'^---\s*', '', body_text).strip()
        
        frontmatter_html = md_converter.convert(frontmatter_text)
        md_converter.reset()
        toc_html = md_converter.convert(toc_text)
        md_converter.reset()
        body_html = md_converter.convert(body_text)
        
        full_content_html = f"""
<div class="frontmatter-page">
{frontmatter_html}
</div>

<div class="toc-page">
{toc_html}
</div>

<div class="body-content">
{body_html}
</div>
"""
    else:
        full_content_html = md_converter.convert(text_with_math)

    full_content_html = process_callouts(full_content_html)
    logo_data_uri = get_logo_base64()

    # Document metadata and titles
    if lang == "en":
        doc_title = "HAICHAIN: The Economic Bedrock for the AI² Symbiotic Superintelligence Era"
        doc_subtitle = "Empowering billions of AI Agents and Autonomous Robots to freely compute, transact, and coalesce with human real-world intelligence to co-create abundance—ensuring all generated wealth and sovereign ownership remain permanently with humanity. The financial operating system for the autonomous machine age today; the economic bedrock for the AI² symbiotic superintelligence era tomorrow."
        doc_edition = "Official Whitepaper v1.0 • Institutional Standard Edition"
        brand_sub_text = "Financial Operating System for the Autonomous Machine Age"
        running_header_left = "HAICHAIN: The Economic Bedrock for the AI² Era"
        running_header_right = "haichain.si"
        running_footer_left = "CONFIDENTIAL & PROPRIETARY • HAICHAIN GLOBAL SYSTEMS TASKFORCE"
        tag_text = "FINANCIAL OPERATING SYSTEM FOR THE AUTONOMOUS MACHINE AGE"
        lbl_settlement = "Primary Settlement Asset"
        val_settlement = "USDT (Tether USD SPL)"
        lbl_token = "Sovereign Gas & Governance"
        val_token = "$HAISI (1,000,000,000 Fixed Supply)"
        lbl_domain = "Autonomous Network Domain"
        val_domain = "haichain.si (Superintelligence)"
        lbl_security = "Cryptographic Verification"
        val_security = "Formal Verification • Zero-Griefing Standard"
    elif lang == "zh":
        doc_title = "HAICHAIN: AI² 共生超级智能时代的基石经济网络"
        doc_subtitle = "赋能数十亿 AI 智能体与自主机器人自由协作、结算并与人类现实智慧深度融合以共同创造财富——确保所有创造的财富与主权掌控权永远属于人类。今日自主机器时代的金融操作系统，明日 AI² 共生超级智能时代的基石经济网络。"
        doc_edition = "官方技术白皮书 v1.0 • 国际机构标准版"
        brand_sub_text = "自主机器时代的金融操作系统"
        running_header_left = "HAICHAIN: AI² 共生超级智能时代的基石经济网络"
        running_header_right = "haichain.si"
        running_footer_left = "机密与专有技术 • HAICHAIN 全球系统特别工作组"
        tag_text = "自主机器时代的金融操作系统"
        lbl_settlement = "核心结算资产"
        val_settlement = "USDT (Solana SPL 代币)"
        lbl_token = "网络 Gas 与主权治理代币"
        val_token = "$HAISI (固定总量 1,000,000,000 枚)"
        lbl_domain = "主权自主网络域名"
        val_domain = "haichain.si (去中心化超级智能)"
        lbl_security = "密码学形式化验证"
        val_security = "形式化数学验证 • 零恶意攻击标准"
    elif lang == "ko":
        doc_title = "HAICHAIN: AI² 공생 초지능 시대를 위한 경제적 기반"
        doc_subtitle = "수십억 개의 AI 에이전트와 자율 로봇이 자유롭게 작업하고 거래하며 인간의 실제 지능과 융합하여 부를 공동 창출하도록 지원합니다. 창출된 모든 부와 주권적 소유권은 영원히 인류에게 귀속됩니다. 오늘날 자율 기계 시대를 위한 금융 운영체제이자, 내일의 AI² 공생 초지능 시대를 위한 경제적 기반입니다."
        doc_edition = "공식 기술 백서 v1.0 • 국제 기관 표준 에디션"
        brand_sub_text = "자율 기계 시대를 위한 금융 운영체제"
        running_header_left = "HAICHAIN: AI² 공생 초지능 시대를 위한 경제적 기반"
        running_header_right = "haichain.si"
        running_footer_left = "기밀 및 독점 정보 • HAICHAIN 글로벌 시스템 태스크포스"
        tag_text = "자율 기계 시대를 위한 금융 운영체제"
        lbl_settlement = "주요 정산 자산"
        val_settlement = "USDT (Solana SPL)"
        lbl_token = "네트워크 가스 및 거버넌스"
        val_token = "$HAISI (1,000,000,000 고정 공급량)"
        lbl_domain = "자율 네트워크 도메인"
        val_domain = "haichain.si (탈중앙화 초지능)"
        lbl_security = "암호학적 형식 검증"
        val_security = "수학적 형식 검증 • 제로 그리핑 표준"
    elif lang == "es":
        doc_title = "HAICHAIN: La Base Económica para la Era de la Superinteligencia Simbiótica AI²"
        doc_subtitle = "Permitiendo a miles de millones de Agentes de IA y Robots Autónomos trabajar, realizar transacciones y unirse libremente con la inteligencia del mundo real humano para co-crear riqueza, garantizando que toda la riqueza y la soberanía pertenezcan para siempre a la humanidad. El sistema operativo financiero para la era de las máquinas autónomas hoy; la base económica para la era de la superinteligencia simbiótica AI² mañana."
        doc_edition = "Libro Blanco Oficial v1.0 • Edición Estándar Institucional"
        brand_sub_text = "Sistema Operativo Financiero para la Era de las Máquinas Autónomas"
        running_header_left = "HAICHAIN: La Base Económica para la Era AI²"
        running_header_right = "haichain.si"
        running_footer_left = "CONFIDENCIAL Y PROPIETARIO • GRUPO DE TRABAJO GLOBAL DE SISTEMAS HAICHAIN"
        tag_text = "SISTEMA OPERATIVO FINANCIERO PARA LA ERA DE LAS MÁQUINAS AUTÓNOMAS"
        lbl_settlement = "Activo Principal de Liquidación"
        val_settlement = "USDT (Tether USD SPL)"
        lbl_token = "Gas y Gobernanza Soberana"
        val_token = "$HAISI (Suministro Fijo: 1.000.000.000)"
        lbl_domain = "Dominio de Red Autónoma"
        val_domain = "haichain.si (Superinteligencia)"
        lbl_security = "Verificación Criptográfica Formal"
        val_security = "Verificación Matemática • Estándar Zero-Griefing"
    elif lang == "fr":
        doc_title = "HAICHAIN: Le Socle Économique pour l'Ère de la Superintelligence Symbiotique AI²"
        doc_subtitle = "Permettre à des milliards d'Agents IA et de Robots Autonomes d'opérer, de transiger et de fusionner librement avec l'intelligence humaine réelle pour co-créer la richesse, garantissant que toute la richesse et la souveraineté appartiennent à jamais à l'humanité. Le système d'exploitation financier pour l'ère des machines autonomes aujourd'hui ; le socle économique pour l'ère de la superintelligence symbiotique AI² demain."
        doc_edition = "Livre Blanc Officiel v1.0 • Édition Standard Institutionnelle"
        brand_sub_text = "Système d'Exploitation Financier pour l'Ère des Machines Autonomes"
        running_header_left = "HAICHAIN: Le Socle Économique pour l'Ère AI²"
        running_header_right = "haichain.si"
        running_footer_left = "CONFIDENTIEL ET PROPRIÉTAIRE • GROUPE DE TRAVAIL SYSTÈMES MONDIAUX HAICHAIN"
        tag_text = "SYSTÈME D'EXPLOITATION FINANCIER POUR L'ÈRE DES MACHINES AUTONOMES"
        lbl_settlement = "Actif de Règlement Principal"
        val_settlement = "USDT (Tether USD SPL)"
        lbl_token = "Gas et Gouvernance Souveraine"
        val_token = "$HAISI (Offre Fixe: 1 000 000 000)"
        lbl_domain = "Domaine Réseau Autonome"
        val_domain = "haichain.si (Superintelligence)"
        lbl_security = "Vérification Cryptographique Formelle"
        val_security = "Vérification Mathématique • Norme Zero-Griefing"
    elif lang == "ru":
        doc_title = "HAICHAIN: Экономический фундамент для эпохи симбиотического сверхразума AI²"
        doc_subtitle = "Предоставление миллиардам ИИ-агентов и автономных роботов возможности свободно вычислять, совершать транзакции и объединяться с реальным интеллектом человека для совместного создания богатства — гарантируя, что все созданные блага и суверенное владение навсегда остаются за человечеством. Финансовая операционная система для эпохи автономных машин сегодня; экономический фундамент для эпохи симбиотического сверхразума AI² завтра."
        doc_edition = "Официальный White Paper v1.0 • Международное институциональное издание"
        brand_sub_text = "Финансовая операционная система для эпохи автономных машин"
        running_header_left = "HAICHAIN: Экономический фундамент для эпохи AI²"
        running_header_right = "haichain.si"
        running_footer_left = "КОНФИДЕНЦИАЛЬНО И ДСП • ГЛОБАЛЬНАЯ РАБОЧАЯ ГРУППА HAICHAIN"
        tag_text = "ФИНАНСОВАЯ ОПЕРАЦИОННАЯ СИСТЕМА ДЛЯ ЭПОХИ АВТОНОМНЫХ МАШИН"
        lbl_settlement = "Основной расчетный актив"
        val_settlement = "USDT (Solana SPL токен)"
        lbl_token = "Сетевой Gas и суверенное управление"
        val_token = "$HAISI (Фиксированная эмиссия: 1 000 000 000)"
        lbl_domain = "Суверенный сетевой домен"
        val_domain = "haichain.si (Децентрализованный сверхразум)"
        lbl_security = "Криптографическая верификация"
        val_security = "Формальная математическая верификация • Стандарт Zero-Griefing"
    elif lang == "kk":
        doc_title = "HAICHAIN: AI² симбиотикалық асқан интеллект дәуіріне арналған экономикалық іргетас"
        doc_subtitle = "Миллиардтаған AI агенттері мен автономды роботтарға еркін жұмыс істеуге, транзакциялар жасауға және адамның нақты интеллектімен бірігіп байлық жасауға мүмкіндік береді — барлық жасалған игілік пен егемендік мәңгілікке адамзатқа тиесілі болады. Бүгінгі автономды машиналар дәуіріне арналған қаржылық операциялық жүйе; ертеңгі AI² симбиотикалық асқан интеллект дәуірінің экономикалық іргетасы."
        doc_edition = "Ресми Ақ Қағаз v1.0 • Халықаралық институционалдық басылым"
        brand_sub_text = "Автономды машиналар дәуіріне арналған қаржылық операциялық жүйе"
        running_header_left = "HAICHAIN: AI² дәуіріне арналған экономикалық іргетас"
        running_header_right = "haichain.si"
        running_footer_left = "ҚҰПИЯ ЖӘНЕ ЖЕКЕ МЕНШІК • HAICHAIN ЖАҺАНДЫҚ ЖҮЙЕЛЕР ТОБЫ"
        tag_text = "АВТОНОМДЫ МАШИНАЛАР ДӘУІРІНЕ АРНАЛҒАН ҚАРЖЫЛЫҚ ОПЕРАЦИЯЛЫҚ ЖҮЙЕ"
        lbl_settlement = "Негізгі есеп айырысу активі"
        val_settlement = "USDT (Solana SPL токені)"
        lbl_token = "Желілік Gas және егемен басқару"
        val_token = "$HAISI (Тұрақты эмиссия: 1 000 000 000)"
        lbl_domain = "Егемен желілік домен"
        val_domain = "haichain.si (Орталықсыздандырылған асқан интеллект)"
        lbl_security = "Криптографиялық формалды верификация"
        val_security = "Математикалық формалды тексеру • Zero-Griefing стандарты"
    elif lang == "hi":
        doc_title = "HAICHAIN: AI² सहजीवी सुपरइंटेलिजेंस युग के लिए आर्थिक आधार"
        doc_subtitle = "अरबों एआई एजेंटों और स्वायत्त रोबोटों को स्वतंत्र रूप से कार्य करने, लेनदेन करने और वास्तविक मानव बुद्धि के साथ मिलकर समृद्धि का निर्माण करने में सक्षम बनाना—यह सुनिश्चित करते हुए कि सारा सृजित धन और संप्रभु स्वामित्व हमेशा मानवता के पास रहे। आज स्वायत्त मशीन युग के लिए वित्तीय ऑपरेटिंग सिस्टम; कल AI² सहजीवी सुपरइंटेलिजेंस युग के लिए आर्थिक आधार।"
        doc_edition = "आधिकारिक श्वेतपत्र v1.0 • अंतर्राष्ट्रीय संस्थागत मानक संस्करण"
        brand_sub_text = "स्वायत्त मशीन युग के लिए वित्तीय ऑपरेटिंग सिस्टम"
        running_header_left = "HAICHAIN: AI² सहजीवी सुपरइंटेलिजेंस युग के लिए आर्थिक आधार"
        running_header_right = "haichain.si"
        running_footer_left = "गोपनीय एवं स्वामित्व • HAICHAIN ग्लोबल सिस्टम्स टास्कफोर्स"
        tag_text = "स्वायत्त मशीन युग के लिए वित्तीय ऑपरेटिंग सिस्टम"
        lbl_settlement = "प्राथमिक निपटान संपत्ति"
        val_settlement = "USDT (Solana SPL)"
        lbl_token = "नेटवर्क गैस और संप्रभु शासन"
        val_token = "$HAISI (निश्चित आपूर्ति: 1,000,000,000)"
        lbl_domain = "स्वायत्त नेटवर्क डोमेन"
        val_domain = "haichain.si (विकेंद्रीकृत सुपरइंटेलिजेंस)"
        lbl_security = "क्रिप्टोग्राफिक औपचारिक सत्यापन"
        val_security = "गणितीय औपचारिक सत्यापन • जीरो-ग्रीफिंग मानक"
    elif lang == "he":
        doc_title = "HAICHAIN: התשתית הכלכלית לעידן בינת-העל הסימביוטית AI²"
        doc_subtitle = "הענקת כוח למיליארדי סוכני AI ורובוטים אוטונומיים לחשב, לסחור ולהתמזג בחופשיות עם הבינה האנושית בעולם האמיתי כדי לייצר שפע משותף — תוך הבטחה שכל העושר והבעלות הריבונית יישארו לנצח בידי האנושות. מערכת ההפעלה הפיננסית לעידן המכונות האוטונומיות כיום; התשתית הכלכלית לעידן בינת-העל הסימביוטית AI² מחר."
        doc_edition = "נייר עמדה רשמי v1.0 • מהדורה מוסדית בינלאומית"
        brand_sub_text = "מערכת הפעלה פיננסית לעידן המכונות האוטונומיות"
        running_header_left = "HAICHAIN: התשתית הכלכלית לעידן בינת-העל הסימביוטית AI²"
        running_header_right = "haichain.si"
        running_footer_left = "סודי ובלעדי • כוח המשימה העולמי של מערכות HAICHAIN"
        tag_text = "מערכת הפעלה פיננסית לעידן המכונות האוטונומיות"
        lbl_settlement = "נכס סליקה ראשי"
        val_settlement = "USDT (Solana SPL)"
        lbl_token = "גז רשת וממשל ריבוני"
        val_token = "$HAISI (היצע קבוע: 1,000,000,000)"
        lbl_domain = "דומיין רשת אוטונומי"
        val_domain = "haichain.si (בינה-על מבוזרת)"
        lbl_security = "אימות קריפטוגרפי פורמלי"
        val_security = "אימות מתמטי • תקן אפס-הטרדה (Zero-Griefing)"
    else:
        doc_title = "HAICHAIN: Nền Tảng Kinh Tế Cho Kỷ Nguyên Siêu Trí Tuệ Cộng Sinh AI²"
        doc_subtitle = "Giúp hàng tỷ tác nhân AI Agent, Robot AI tự do làm việc, giao dịch và hợp nhất với trí tuệ thực tế của con người để cùng tạo ra của cải, toàn bộ của cải và quyền làm chủ mãi mãi thuộc về con người. Hệ điều hành tài chính cho kỷ nguyên máy tự trị hôm nay. Nền tảng kinh tế cho kỷ nguyên siêu trí tuệ cộng sinh AI² ngày mai."
        doc_edition = "Sách Trắng v1.0 • Phiên Bản Tiêu Chuẩn Thể Chế Quốc Tế"
        brand_sub_text = "Hệ Điều Hành Tài Chính Cho Kỷ Nguyên Máy Tự Trị"
        running_header_left = "HAICHAIN: Nền Tảng Kinh Tế Cho Kỷ Nguyên Siêu Trí Tuệ Cộng Sinh AI²"
        running_header_right = "haichain.si"
        running_footer_left = "BẢO LƯU MỌI QUYỀN • HỘI ĐỒNG KIẾN TRÚC HỆ THỐNG PHÂN TÁN HAICHAIN"
        tag_text = "HỆ ĐIỀU HÀNH TÀI CHÍNH CHO KỶ NGUYÊN MÁY TỰ TRỊ"
        lbl_settlement = "Tài Sản Quyết Toán Chính"
        val_settlement = "USDT (Tether USD SPL)"
        lbl_token = "Gas Chủ Quyền & Quản Trị"
        val_token = "$HAISI (Cố Định 1.000.000.000 Token)"
        lbl_domain = "Tên Miền Mạng Mục Tiêu"
        val_domain = "haichain.si (Superintelligence)"
        lbl_security = "Tiêu Chuẩn Xác Thực An Toàn"
        val_security = "Xác Thực Toán Học • Chuẩn Zero-Griefing"
    if lang == "he":
        body_font_size = "11.2pt"
        body_line_height = "1.90"
    elif lang in ["es", "ru"]:
        body_font_size = "9.45pt"
        body_line_height = "1.58"
    else:
        body_font_size = "9.6pt"
        body_line_height = "1.62"

    full_html = f"""<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if lang == 'he' else 'ltr'}">
<head>
<meta charset="utf-8">
<title>{doc_title}</title>
<style>
/* CSS Paged Media Standards - 100% Borderless Pure Academic Typography */
@page {{
    size: A4;
    margin: 24mm 20mm 24mm 20mm;
    @top-left {{
        content: "{running_header_left}";
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", "PingFang SC", "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans SC", "Noto Sans KR", sans-serif;
        font-size: 7.5pt;
        font-weight: 600;
        color: #52525b;
        letter-spacing: 0.5px;
    }}
    @top-right {{
        content: "{running_header_right}";
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", "PingFang SC", "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans SC", "Noto Sans KR", sans-serif;
        font-size: 8pt;
        font-weight: 700;
        color: #52525b;
        letter-spacing: 0.5px;
    }}
    @bottom-left {{
        content: "{running_footer_left}";
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", "PingFang SC", "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans SC", "Noto Sans KR", sans-serif;
        font-size: 7pt;
        color: #71717a;
        letter-spacing: 0.3px;
    }}
    @bottom-right {{
        content: "Page " counter(page);
        font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", "PingFang SC", "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans SC", "Noto Sans KR", sans-serif;
        font-size: 7.5pt;
        font-weight: 600;
        color: #52525b;
    }}
}}

@page:first {{
    margin: 0;
    @top-left {{ content: none; }}
    @top-right {{ content: none; }}
    @bottom-left {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

* {{
    border-color: transparent !important;
}}

body {{
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans Hebrew", "David", "Arial Hebrew", "Microsoft YaHei", "PingFang SC", "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans SC", "Noto Sans KR", sans-serif;
    font-size: {body_font_size};
    line-height: {body_line_height};
    color: #18181b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}}

/* Universal Link Styling: NEVER Underline */
a, a:link, a:visited, a:hover, a:active {{
    text-decoration: none !important;
    color: inherit !important;
    border: none !important;
}}

/* Universal Horizontal Rules: Completely Hidden (Zero Border Lines) */
hr {{
    display: none !important;
    border: none !important;
    height: 0 !important;
    margin: 0 !important;
}}

/* Cover Page: Black Premium - Pure Borderless */
.cover-page {{
    page-break-after: always;
    break-after: page;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #050505;
    color: #ffffff;
    padding: 65px 55px;
    box-sizing: border-box;
    border: none !important;
}}

.cover-header {{
    border: none !important;
    padding-bottom: 16px;
}}

.cover-logo-img {{
    height: 36px;
    width: auto;
    display: block;
    margin-bottom: 10px;
    border: none !important;
}}

.cover-brand-sub {{
    font-size: 8pt;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #a1a1aa;
    margin-top: 4px;
    font-weight: 500;
    border: none !important;
}}

.cover-title-container {{
    margin: auto 0;
    border: none !important;
}}

.cover-tag {{
    display: inline-block;
    border: none !important;
    color: #d4d4d8;
    font-size: 8pt;
    font-weight: 700;
    padding: 0;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 16px;
}}

.cover-title {{
    font-size: 21pt;
    font-weight: 800;
    line-height: 1.25;
    color: #ffffff;
    margin: 0 0 14px 0;
    letter-spacing: -0.4px;
    border: none !important;
}}

.cover-subtitle {{
    font-size: 10.2pt;
    font-weight: 400;
    line-height: 1.58;
    color: #a1a1aa;
    margin: 0 0 24px 0;
    max-width: 95%;
    border: none !important;
}}

.cover-badges {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px 24px;
    margin-top: 28px;
    border: none !important;
    padding: 10px 0;
}}

.cover-badge-item {{
    font-size: 8.5pt;
    border: none !important;
}}

.cover-badge-label {{
    color: #71717a;
    text-transform: uppercase;
    font-size: 7pt;
    letter-spacing: 1px;
    font-weight: 600;
    border: none !important;
}}

.cover-badge-val {{
    color: #f4f4f5;
    font-weight: 600;
    margin-top: 3px;
    border: none !important;
}}

.cover-footer {{
    border: none !important;
    padding-top: 20px;
    font-size: 8pt;
    color: #71717a;
    display: flex;
    justify-content: space-between;
}}

/* Page 2: Frontmatter (Title, Subtitle, Metadata, ASCII logo) */
.frontmatter-page {{
    page-break-after: always;
    break-after: page;
    padding-top: 10px;
}}

.frontmatter-page h1 {{
    font-size: 16pt;
    font-weight: 800;
    color: #000000;
    border: none !important;
    padding: 0;
    margin-top: 10px;
    margin-bottom: 12px;
    letter-spacing: -0.2px;
}}

.frontmatter-page h2 {{
    font-size: 11.5pt;
    font-weight: 600;
    color: #27272a;
    border: none !important;
    padding: 0;
    margin-top: 0;
    margin-bottom: 18px;
    line-height: 1.45;
}}

/* Page 3: Dedicated Standalone Table of Contents Page */
.toc-page {{
    page-break-before: always;
    page-break-after: always;
    break-before: page;
    break-after: page;
    padding-top: 14px;
}}

.toc-page h2 {{
    font-size: 14.5pt;
    font-weight: 800;
    color: #000000;
    border: none !important;
    padding: 0;
    margin-top: 0;
    margin-bottom: 22px;
    letter-spacing: -0.2px;
}}

.toc-page ol, .toc-page ul {{
    padding-left: 20px;
    margin: 0;
}}

.toc-page li {{
    margin-bottom: 6px;
    font-size: 8.8pt;
    line-height: 1.45;
    color: #18181b;
}}

.toc-page li li {{
    margin-top: 4px;
    margin-bottom: 4px;
    font-size: 8.2pt;
    color: #3f3f46;
}}

.toc-page a {{
    text-decoration: none !important;
    color: #18181b !important;
    border: none !important;
}}

.toc-page a:hover {{
    text-decoration: none !important;
}}

/* Typography Hierarchies - 100% Borderless */
h1 {{
    font-size: 16pt;
    font-weight: 800;
    color: #000000;
    border: none !important;
    padding: 0;
    margin-top: 34px;
    margin-bottom: 14px;
    letter-spacing: -0.2px;
    page-break-after: avoid;
    break-after: avoid;
}}

h1:first-of-type {{
    margin-top: 12px;
}}

h2 {{
    font-size: 12.5pt;
    font-weight: 700;
    color: #000000;
    border: none !important;
    padding: 0;
    margin-top: 24px;
    margin-bottom: 10px;
    page-break-after: avoid;
    break-after: avoid;
}}

h3 {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #18181b;
    border: none !important;
    padding: 0;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
    break-after: avoid;
}}

h4 {{
    font-size: 9.6pt;
    font-weight: 700;
    color: #27272a;
    border: none !important;
    padding: 0;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
    break-after: avoid;
}}

p {{
    margin-top: 0;
    margin-bottom: 10px;
    text-align: justify;
    color: #18181b;
    border: none !important;
}}

ul, ol {{
    margin-top: 0;
    margin-bottom: 12px;
    padding-left: 22px;
}}

li {{
    margin-bottom: 5px;
}}

/* Tables - Borderless Modern Layout */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
    border: none !important;
}}

th, td {{
    border: none !important;
    padding: 7px 10px;
    text-align: left;
    vertical-align: top;
}}

th {{
    background-color: #f4f4f5;
    color: #000000;
    font-weight: 700;
    letter-spacing: 0.3px;
    border: none !important;
}}

tr:nth-child(even) td {{
    background-color: #fafafa;
}}

/* Code Blocks & ASCII Architecture - 100% Borderless */
pre {{
    background-color: transparent !important;
    color: #000000;
    padding: 8px 0;
    border: none !important;
    border-radius: 0 !important;
    font-family: Consolas, "Courier New", monospace;
    font-size: 7.6pt;
    line-height: 1.35;
    overflow: hidden;
    margin: 14px 0;
    page-break-inside: avoid;
    break-inside: avoid;
}}

code {{
    font-family: Consolas, "Courier New", monospace;
    font-size: 8.8pt;
    background: transparent !important;
    color: #000000;
    padding: 0 !important;
    border: none !important;
}}

pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
    border: none;
    font-size: inherit;
}}

/* Academic Remarks / Notes - Pure Typography (Zero Borders) */
.academic-remark {{
    margin: 16px 20px;
    padding: 0;
    border: none !important;
    background: transparent !important;
    page-break-inside: avoid;
    break-inside: avoid;
}}

.academic-remark .remark-lead {{
    font-size: 8.5pt;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #000000;
    margin: 0 0 4px 0;
    text-align: left;
    border: none !important;
}}

.academic-remark .remark-body {{
    font-style: italic;
    color: #18181b;
    line-height: 1.6;
    margin: 0;
    text-align: justify;
    border: none !important;
}}

/* Mathematical Formulas - Pure Academic (Zero Borders) */
.math-display {{
    background: transparent !important;
    border: none !important;
    padding: 10px 0 !important;
    margin: 14px 0 !important;
    text-align: center;
    font-family: "Cambria Math", "Times New Roman", Times, serif;
    font-size: 11pt;
    color: #000000;
    page-break-inside: avoid;
    break-inside: avoid;
}}

.math-inline {{
    font-family: "Cambria Math", "Times New Roman", Times, serif;
    font-size: 9.8pt;
    color: #000000;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}}

.math-text {{
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", "PingFang SC", "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans SC", "Noto Sans KR", sans-serif;
    font-style: normal;
}}

/* Blockquotes */
blockquote {{
    margin: 14px 20px;
    padding: 0;
    border: none !important;
    background: transparent !important;
    color: #18181b;
    font-style: italic;
    page-break-inside: avoid;
    break-inside: avoid;
}}

blockquote p {{
    margin: 0;
    text-align: justify;
    border: none !important;
}}

/* RTL Specific Rules for Hebrew */
html[dir="rtl"] p {{
    text-align: justify;
}}
html[dir="rtl"] pre, html[dir="rtl"] code, html[dir="rtl"] .math-display, html[dir="rtl"] .math-inline {{
    direction: ltr !important;
    text-align: left !important;
    unicode-bidi: embed;
}}
html[dir="rtl"] .academic-remark .remark-lead {{
    text-align: right !important;
}}
html[dir="rtl"] th, html[dir="rtl"] td {{
    text-align: right;
}}
html[dir="rtl"] ul, html[dir="rtl"] ol {{
    padding-left: 0;
    padding-right: 22px;
}}
html[dir="rtl"] .toc-page ol, html[dir="rtl"] .toc-page ul {{
    padding-left: 0;
    padding-right: 20px;
}}
</style>
</head>
<body>

<!-- Institutional Black Premium Cover Page (Zero Border Lines) -->
<div class="cover-page">
    <div class="cover-header">
        <img src="{logo_data_uri}" class="cover-logo-img" alt="HAICHAIN Logo" />
        <div class="cover-brand-sub">{brand_sub_text}</div>
    </div>
    
    <div class="cover-title-container">
        <div class="cover-tag">{tag_text}</div>
        <div class="cover-title">{doc_title}</div>
        <div class="cover-subtitle">{doc_subtitle}</div>
        
        <div class="cover-badges">
            <div class="cover-badge-item">
                <div class="cover-badge-label">{lbl_settlement}</div>
                <div class="cover-badge-val">{val_settlement}</div>
            </div>
            <div class="cover-badge-item">
                <div class="cover-badge-label">{lbl_token}</div>
                <div class="cover-badge-val">{val_token}</div>
            </div>
            <div class="cover-badge-item">
                <div class="cover-badge-label">{lbl_domain}</div>
                <div class="cover-badge-val">{val_domain}</div>
            </div>
            <div class="cover-badge-item">
                <div class="cover-badge-label">{lbl_security}</div>
                <div class="cover-badge-val">{val_security}</div>
            </div>
        </div>
    </div>
    
    <div class="cover-footer">
        <div>{doc_edition}</div>
        <div>haichain.si</div>
    </div>
</div>

<!-- Main Body Content with Isolated Frontmatter and Dedicated TOC Page -->
<div class="document-content">
{full_content_html}
</div>

</body>
</html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    # Command line invocation of Microsoft Edge in headless print-to-pdf mode
    edge_cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    
    print(f"[*] Compiling PDF via Edge Engine to: {pdf_path}")
    result = subprocess.run(edge_cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"[+] Successfully generated: {pdf_filename} ({size_kb:.1f} KB)")
    else:
        print(f"[-] Error generating PDF: {result.stderr}")
    
    # Clean up temporary HTML file
    if os.path.exists(html_path):
        os.remove(html_path)

if __name__ == "__main__":
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_EN.md", "HAICHAIN_WHITEPAPER_V1.0_EN.pdf", lang="en")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_VI.md", "HAICHAIN_WHITEPAPER_V1.0_VI.pdf", lang="vi")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_ZH.md", "HAICHAIN_WHITEPAPER_V1.0_ZH.pdf", lang="zh")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_KO.md", "HAICHAIN_WHITEPAPER_V1.0_KO.pdf", lang="ko")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_ES.md", "HAICHAIN_WHITEPAPER_V1.0_ES.pdf", lang="es")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_FR.md", "HAICHAIN_WHITEPAPER_V1.0_FR.pdf", lang="fr")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_RU.md", "HAICHAIN_WHITEPAPER_V1.0_RU.pdf", lang="ru")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_KK.md", "HAICHAIN_WHITEPAPER_V1.0_KK.pdf", lang="kk")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_HI.md", "HAICHAIN_WHITEPAPER_V1.0_HI.pdf", lang="hi")
    build_pdf_from_markdown("HAICHAIN_WHITEPAPER_V1.0_HE.md", "HAICHAIN_WHITEPAPER_V1.0_HE.pdf", lang="he")
