import os, subprocess, markdown, shutil, sys, fitz, re, base64
sys.stdout.reconfigure(encoding='utf-8')

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"
APP_DIR = os.path.join(WORKSPACE_DIR, "app")

with open(os.path.join(WORKSPACE_DIR, "assets/haichain-official-logo-white.png"), "rb") as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')

cover_dict = {
    'EN': {
        'title_pdf': 'HAICHAIN Official Whitepaper v1.1 (CapLeaf & 9 Invariants Edition) (English Standard)',
        'sub': 'FINANCIAL OPERATING SYSTEM FOR THE AUTONOMOUS MACHINE AGE',
        'cat': 'FINANCIAL OPERATING SYSTEM FOR THE AUTONOMOUS MACHINE AGE',
        'title': 'HAICHAIN: The Economic Bedrock for the AI²<br>Symbiotic Superintelligence Era',
        'summary': 'Empowering billions of AI Agents and Autonomous Robots to freely compute, transact, and coalesce with human real-world intelligence to co-create abundance—ensuring all generated wealth and sovereign ownership remain permanently with humanity. The financial operating system for the autonomous machine age today; the economic bedrock for the AI² symbiotic superintelligence era tomorrow.',
        'asset_lbl': 'PRIMARY SETTLEMENT ASSET',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': 'SOVEREIGN GAS & GOVERNANCE',
        'gas_val': '$HAISI (1,000,000,000 Fixed Supply)',
        'dom_lbl': 'AUTONOMOUS NETWORK DOMAIN',
        'dom_val': 'haichain.si (Superintelligence)',
        'verif_lbl': 'CRYPTOGRAPHIC VERIFICATION',
        'verif_val': 'Formal Verification • Zero-Griefing Standard',
        'footer_left': 'Official Whitepaper v1.0 • Institutional Standard Edition',
        'footer_right': 'haichain.si'
    },
    'VI': {
        'title_pdf': 'Bản Sách Trắng Kỹ Thuật HAICHAIN v1.1 (Bản CapLeaf & 9 Bất Biến) (Tiếng Việt)',
        'sub': 'HỆ ĐIỀU HÀNH TÀI CHÍNH CHO KỶ NGUYÊN MÁY MÓC TỰ HÀNH',
        'cat': 'HỆ ĐIỀU HÀNH TÀI CHÍNH CHO KỶ NGUYÊN MÁY MÓC TỰ HÀNH',
        'title': 'HAICHAIN: Nền Tảng Kinh Tế Cho Kỷ Nguyên<br>Siêu Trí Tuệ Cộng Sinh AI²',
        'summary': 'Trao quyền cho hàng tỷ Tác tử AI và Robot tự hành tự do tính toán, giao dịch và hợp nhất với trí tuệ thế giới thực của con người để kiến tạo sự thịnh vượng—đảm bảo toàn bộ tài sản được tạo ra và quyền làm chủ tối cao thuộc về nhân loại. Hệ điều hành tài chính cho kỷ nguyên máy móc tự hành hôm nay; nền tảng kinh tế cho kỷ nguyên siêu trí tuệ cộng sinh AI² ngày mai.',
        'asset_lbl': 'TÀI SẢN THANH TOÁN CHÍNH',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': 'PHÍ GAS & QUẢN TRỊ TỐI CAO',
        'gas_val': '$HAISI (Tổng cung cố định 1.000.000.000)',
        'dom_lbl': 'TÊN MIỀN MẠNG TỰ HÀNH',
        'dom_val': 'haichain.si (Siêu Trí Tuệ)',
        'verif_lbl': 'XÁC MINH MẬT MÃ TOÁN HỌC',
        'verif_val': 'Kiểm Chứng Hình Thức • Chuẩn Zero-Griefing',
        'footer_left': 'Bạch Thư Chính Thức v1.0 • Phiên Bản Tiêu Chuẩn Thể Chế',
        'footer_right': 'haichain.si'
    },
    'ZH': {
        'title_pdf': 'HAICHAIN 官方白皮书 v1.1（CapLeaf 与 9 大不变量正式版）（中文正式版）',
        'sub': '自主机器时代的金融操作系统',
        'cat': '自主机器时代的金融操作系统',
        'title': 'HAICHAIN：AI² 共生超智能时代的<br>经济基石',
        'summary': '赋能数十亿AI智能体与自主机器人自由计算、交易，并与人类现实世界的智慧深度融合，共同创造丰裕——确保所有创造的财富与主权掌控权永久归全人类所有。今天作为自主机器时代的金融操作系统，明天成为 AI² 共生超智能时代的经济基石。',
        'asset_lbl': '主要结算资产',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': '主权燃料与治理代币',
        'gas_val': '$HAISI (恒定供应 1,000,000,000)',
        'dom_lbl': '自主网络域名',
        'dom_val': 'haichain.si (Superintelligence)',
        'verif_lbl': '密码学形式化验证',
        'verif_val': '形式化验证 • 零博弈标准 (Zero-Griefing)',
        'footer_left': '官方白皮书 v1.0 • 机构标准版',
        'footer_right': 'haichain.si'
    },
    'KO': {
        'title_pdf': 'HAICHAIN 공식 백서 v1.1 (CapLeaf 및 9대 불변성 에디션) (한국어 표준판)',
        'sub': '자율 기계 시대를 위한 금융 운영체제',
        'cat': '자율 기계 시대를 위한 금융 운영체제',
        'title': 'HAICHAIN: AI² 공생 슈퍼인텔리전스 시대를 위한<br>경제적 기반',
        'summary': '수십억 개의 AI 에이전트와 자율 로봇이 자유롭게 연산하고 거래하며 인류의 실제 지능과 융합하여 풍요를 공동 창출하도록 지원합니다. 생성된 모든 부와 주권적 소유권이 인류에게 영구히 귀속되도록 보장합니다. 오늘날 자율 기계 시대를 위한 금융 OS이자 내일의 AI² 공생 슈퍼인텔리전스 시대를 위한 경제적 기반입니다.',
        'asset_lbl': '주요 결제 자산',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': '주권 가스 및 거버넌스',
        'gas_val': '$HAISI (총 공급량 1,000,000,000 고정)',
        'dom_lbl': '자율 네트워크 도메인',
        'dom_val': 'haichain.si (Superintelligence)',
        'verif_lbl': '암호학적 정형 검증',
        'verif_val': '정형 검증 (Formal Verification) • 제로그리핑 표준',
        'footer_left': '공식 백서 v1.0 • 기관 표준판',
        'footer_right': 'haichain.si'
    },
    'FR': {
        'title_pdf': 'Livre Blanc Officiel HAICHAIN v1.1 (CapLeaf & 9 Invariants) (Édition Française)',
        'sub': 'SYSTÈME D\'EXPLOITATION FINANCIER POUR L\'ÈRE DES MACHINES AUTONOMES',
        'cat': 'SYSTÈME D\'EXPLOITATION FINANCIER POUR L\'ÈRE DES MACHINES AUTONOMES',
        'title': 'HAICHAIN : Le Socle Économique de l\'Ère de la<br>Superintelligence Symbiotique AI²',
        'summary': 'Permettre à des milliards d\'agents IA et de robots autonomes de calculer, d\'effectuer des transactions et de fusionner librement với l\'intelligence humaine du monde réel pour co-créer l\'abondance, tout en garantissant que toute la richesse générée et la propriété souveraine demeurent définitivement entre les mains de l\'humanité. Le système d\'exploitation financier de l\'ère des machines autonomes aujourd\'hui ; le socle économique de l\'ère de la superintelligence symbiotique AI² demain.',
        'asset_lbl': 'ACTIF DE RÈGLEMENT PRINCIPAL',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': 'GAZ SOUVERAIN ET GOUVERNANCE',
        'gas_val': '$HAISI (Offre Fixe 1 000 000 000)',
        'dom_lbl': 'DOMAINE DU RÉSEAU AUTONOME',
        'dom_val': 'haichain.si (Superintelligence)',
        'verif_lbl': 'VÉRIFICATION CRYPTOGRAPHIQUE',
        'verif_val': 'Vérification Formelle • Norme Zéro-Griefing',
        'footer_left': 'Livre Blanc Officiel v1.0 • Édition Standard Institutionnelle',
        'footer_right': 'haichain.si'
    },
    'ES': {
        'title_pdf': 'Libro Blanco Oficial HAICHAIN v1.1 (CapLeaf y 9 Invariantes) (Edición en Español)',
        'sub': 'SISTEMA OPERATIVO FINANCIERO PARA LA ERA DE LAS MÁQUINAS AUTÓNOMAS',
        'cat': 'SISTEMA OPERATIVO FINANCIERO PARA LA ERA DE LAS MÁQUINAS AUTÓNOMAS',
        'title': 'HAICHAIN: El Pilar Económico para la Era de la<br>Superinteligencia Simbiótica AI²',
        'summary': 'Empoderando a miles de millones de Agentes de IA y Robots Autónomos para computar, realizar transacciones y unirse libremente con la inteligencia del mundo real de la humanidad para co-crear abundancia, asegurando que toda la riqueza generada y la propiedad soberana permanezcan permanentemente con la humanidad. El sistema operativo financiero para la era de las máquinas autónomas hoy; la base económica para la era de la superinteligencia simbiótica AI² mañana.',
        'asset_lbl': 'ACTIVO DE LIQUIDACIÓN PRINCIPAL',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': 'GAS SOBERANO Y GOBERNANZA',
        'gas_val': '$HAISI (Suministro Fijo 1.000.000.000)',
        'dom_lbl': 'DOMINIO DE RED AUTÓNOMA',
        'dom_val': 'haichain.si (Superintelligence)',
        'verif_lbl': 'VERIFICACIÓN CRIPTOGRÁFICA',
        'verif_val': 'Verificación Formal • Estándar Cero-Griefing',
        'footer_left': 'Libro Blanco Oficial v1.0 • Edición Estándar Institucional',
        'footer_right': 'haichain.si'
    },
    'RU': {
        'title_pdf': 'Официальный Whitepaper HAICHAIN v1.1 (CapLeaf и 9 Инвариантов) (Русское издание)',
        'sub': 'ФИНАНСОВАЯ ОПЕРАЦИОННАЯ СИСТЕМА ДЛЯ ЭПОХИ АВТОНОМНЫХ МАШИН',
        'cat': 'ФИНАНСОВАЯ ОПЕРАЦИОННАЯ СИСТЕМА ДЛЯ ЭПОХИ АВТОНОМНЫХ МАШИН',
        'title': 'HAICHAIN: Экономический фундамент эпохи<br>симбиотического сверхинтеллекта AI²',
        'summary': 'Расширение возможностей миллиардов ИИ-агентов и автономных роботов для свободных вычислений, расчетов и слияния с реальным интеллектом человечества для совместного создания изобилия — гарантируя, что все созданные богатства и суверенная собственность навсегда останутся у человечества. Финансовая ОС для эпохи автономных машин сегодня; экономический базис эпохи симбиотического сверхинтеллекта AI² завтра.',
        'asset_lbl': 'ОСНОВНОЙ РАСЧЕТНЫЙ АКТИВ',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': 'СУВЕРЕННЫЙ ГАЗ И УПРАВЛЕНИЕ',
        'gas_val': '$HAISI (Фиксированная эмиссия 1 000 000 000)',
        'dom_lbl': 'ДОМЕН АВТОНОМНОЙ СЕТИ',
        'dom_val': 'haichain.si (Superintelligence)',
        'verif_lbl': 'КРИПТОГРАФИЧЕСКАЯ ВЕРИФИКАЦИЯ',
        'verif_val': 'Формальная верификация • Стандарт Zero-Griefing',
        'footer_left': 'Официальный Whitepaper v1.0 • Институциональное издание',
        'footer_right': 'haichain.si'
    },
    'KK': {
        'title_pdf': 'HAICHAIN Ресми Ақ Қағазы v1.1 (CapLeaf және 9 Инвариант) (Қазақ тіліндегі басылым)',
        'sub': 'АВТОНОМДЫ МАШИНАЛАР ДӘУІРІНЕ АРНАЛҒАН ҚАРЖЫЛЫҚ ОПЕРАЦИЯЛЫҚ ЖҮЙЕ',
        'cat': 'АВТОНОМДЫ МАШИНАЛАР ДӘУІРІНЕ АРНАЛҒАН ҚАРЖЫЛЫҚ ОПЕРАЦИЯЛЫҚ ЖҮЙЕ',
        'title': 'HAICHAIN: AI² Симбиотикалық Аса Жоғары<br>Интеллект Дәуірінің Экономикалық Іргетасы',
        'summary': 'Миллиардтаған AI агенттері мен автономды роботтарға еркін есептеулер жүргізуге, транзакциялар жасауға және адамзаттың нақты интеллектімен бірігіп молшылықты бірге жасауға мүмкіндік береді — барлық жасалған байлық пен егеменді меншік мәңгілікке адамзатта қалуын қамтамасыз етеді. Бүгінгі автономды машиналар дәуірінің қаржылық ОС; ертеңгі AI² симбиотикалық аса жоғары интеллект дәуірінің экономикалық іргетасы.',
        'asset_lbl': 'НЕГІЗГІ ЕСЕП АЙЫРЫСУ АКТИВІ',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': 'ЕГЕМЕНДІ ГАЗ ЖӘНЕ БАСҚАРУ',
        'gas_val': '$HAISI (Тұрақты эмиссия 1 000 000 000)',
        'dom_lbl': 'АВТОНОМДЫ ЖЕЛІ ДОМЕНІ',
        'dom_val': 'haichain.si (Superintelligence)',
        'verif_lbl': 'КРИПТОГРАФИЯЛЫҚ ТЕКСЕРУ',
        'verif_val': 'Формальды тексеру • Zero-Griefing стандарты',
        'footer_left': 'Ресми Whitepaper v1.0 • Институционалдық стандарт басылымы',
        'footer_right': 'haichain.si'
    },
    'HI': {
        'title_pdf': 'HAICHAIN आधिकारिक श्वेतपत्र v1.1 (CapLeaf और 9 नियम) (हिन्दी संस्करण)',
        'sub': 'स्वायत्त मशीन युग के लिए वित्तीय ऑपरेटिंग सिस्टम',
        'cat': 'स्वायत्त मशीन युग के लिए वित्तीय ऑपरेटिंग सिस्टम',
        'title': 'HAICHAIN: AI² सहजीवी सुपरइंटेलिजेंस युग के लिए<br>आर्थिक आधारशिला',
        'summary': 'अरबों AI एजेंटों और स्वायत्त रोबोटों को स्वतंत्रता से गणना करने, लेनदेन करने और प्रचुरता का सह-निर्माण करने के लिए मानव वास्तविक बुद्धिमत्ता के साथ एकजुट होने में सक्षम बनाना—यह सुनिश्चित करते हुए कि सारा अर्जित धन और संप्रभु स्वामित्व हमेशा मानवता के पास रहे। आज स्वायत्त मशीन युग के लिए वित्तीय ऑपरेटिंग सिस्टम; कल AI² सहजीवी सुपरइंटेलिजेंस युग के लिए आर्थिक आधारशिला।',
        'asset_lbl': 'प्राथमिक निपटान संपत्ति',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': 'संप्रभु गैस और शासन',
        'gas_val': '$HAISI (1,000,000,000 निश्चित आपूर्ति)',
        'dom_lbl': 'स्वायत्त नेटवर्क डोमेन',
        'dom_val': 'haichain.si (Superintelligence)',
        'verif_lbl': 'क्रिप्टोग्राफ़िक सत्यापन',
        'verif_val': 'औपचारिक सत्यापन (Formal Verification) • ज़ीरो-ग्रीफ़िंग मानक',
        'footer_left': 'आधिकारिक श्वेतपत्र v1.0 • संस्थागत मानक संस्करण',
        'footer_right': 'haichain.si'
    },
    'HE': {
        'title_pdf': 'הספר הלבן הרשמי של HAICHAIN v1.1 (מהדורת CapLeaf ו-9 אינווריאנטים) (מהדורה עברית)',
        'sub': 'מערכת הפעלה פיננסית לעידן המכונות האוטונומיות',
        'cat': 'מערכת הפעלה פיננסית לעידן המכונות האוטונומיות',
        'title': 'HAICHAIN: התשתית הכלכלית לעידן מחשוב-העל<br>הסימביוטי AI²',
        'summary': 'העצמת מיליארדי סוכני AI ורובוטים אוטונומיים לחשב, לבצע עסקאות ולהתמזג בחופשיות עם האינטליגנציה האנושית בעולם האמיתי ליצירת שגשוג משותף—תוך הבטחה שכל העושר שנוצר והבעלות הריבונית יישארו לצמיתות בידי האנושות. מערכת ההפעלה הפיננסית לעידן המכונות האוטונומיות כיום; המסד הכלכלי לעידן מחשוב-העל הסימביוטי AI² מחר.',
        'asset_lbl': 'נכס סליקה ראשי',
        'asset_val': 'USDT (Tether USD SPL)',
        'gas_lbl': 'גז ריבוני וממשל',
        'gas_val': '$HAISI (היצע קבוע 1,000,000,000)',
        'dom_lbl': 'דומיין רשת אוטונומית',
        'dom_val': 'haichain.si (Superintelligence)',
        'verif_lbl': 'אימות קריפטוגרפי',
        'verif_val': 'אימות פורמלי (Formal Verification) • תקן Zero-Griefing',
        'footer_left': 'נייר עמדה רשמי v1.0 • מהדורה מוסדית סטנדרטית',
        'footer_right': 'haichain.si'
    }
}

def compile_pdf(lang):
    c = cover_dict[lang]
    md_filename = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md"
    pdf_filename = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.pdf"
    
    md_path = os.path.join(WORKSPACE_DIR, md_filename)
    pdf_path = os.path.join(WORKSPACE_DIR, pdf_filename)
    html_path = os.path.join(WORKSPACE_DIR, f"temp_{os.path.splitext(pdf_filename)[0]}.html")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Match TOC header and body
    toc_pattern = r'(^##[^\n]*TABLE OF CONTENTS[^\n]*\n)(.*?)(\n---\n|\n## 1|\n# 1|\n## [^\n]*1\.)'
    m = re.search(toc_pattern, md_text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    
    if m:
        toc_header_md = m.group(1).strip()
        toc_body_md = m.group(2).strip()
        
        before_toc_md = md_text[:m.start()].strip()
        after_toc_md = md_text[m.end():].strip()
        
        conv = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
        toc_html = conv.convert(f"{toc_header_md}\n\n{toc_body_md}")
        # Strip code tags inside TOC links
        toc_html = re.sub(r'<code>(.*?)</code>', r'\1', toc_html)
        
        conv2 = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
        before_toc_html = conv2.convert(before_toc_md)
        
        conv3 = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
        after_toc_html = conv3.convert(after_toc_md)
        
        content_html = f"""
        <div class="toc-page">
            {toc_html}
        </div>
        <div class="body-content">
            {before_toc_html}
            <hr />
            {after_toc_html}
        </div>
        """
    else:
        conv = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
        body_html = conv.convert(md_text)
        content_html = f'<div class="body-content">{body_html}</div>'

    direction = "rtl" if lang == "HE" else "ltr"

    cover_html = f"""
    <div class="cover-page">
        <div class="cover-header">
            <div class="cover-logo-row">
                <img class="cover-logo-img" src="data:image/png;base64,{b64_logo}" alt="HAICHAIN" />
            </div>
            <div class="cover-top-sub">{c['sub']}</div>
        </div>
        
        <div class="cover-body">
            <div class="cover-category">{c['cat']}</div>
            <div class="cover-title">{c['title']}</div>
            <div class="cover-summary">{c['summary']}</div>
            
            <div class="cover-grid">
                <div>
                    <div class="cover-grid-item-label">{c['asset_lbl']}</div>
                    <div class="cover-grid-item-val">{c['asset_val']}</div>
                </div>
                <div>
                    <div class="cover-grid-item-label">{c['gas_lbl']}</div>
                    <div class="cover-grid-item-val">{c['gas_val']}</div>
                </div>
                <div>
                    <div class="cover-grid-item-label">{c['dom_lbl']}</div>
                    <div class="cover-grid-item-val">{c['dom_val']}</div>
                </div>
                <div>
                    <div class="cover-grid-item-label">{c['verif_lbl']}</div>
                    <div class="cover-grid-item-val">{c['verif_val']}</div>
                </div>
            </div>
        </div>
        
        <div class="cover-footer">
            <div>{c['footer_left']}</div>
            <div>{c['footer_right']}</div>
        </div>
    </div>
    """

    full_html = f"""<!DOCTYPE html>
<html lang="{lang.lower()}" dir="{direction}">
<head>
<meta charset="utf-8">
<title>{c['title_pdf']}</title>
<style>
/* NAMED PAGES FOR 100% FULL-BLEED COVER & STANDARDIZED INSIDE MARGINS */
@page {{
    size: A4;
    margin: 0;
}}
@page cover {{
    size: A4;
    margin: 0;
}}
@page standard {{
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
    @bottom-right {{
        content: counter(page);
        font-size: 8pt;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: #71717a;
    }}
}}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Helvetica, Arial, sans-serif;
    color: #18181b;
    line-height: 1.55;
    font-size: 9pt;
    background: #ffffff;
    margin: 0;
    padding: 0;
    max-width: 100%;
    overflow-x: hidden;
}}

/* COVER PAGE (100% TRUE FULL-BLEED BLACK PREMIUM) */
.cover-page {{
    page: cover;
    width: 210mm;
    height: 297mm;
    box-sizing: border-box;
    background: #000000 !important;
    color: #ffffff;
    padding: 24mm 22mm 20mm 22mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    break-after: page;
}}
.cover-header {{
    display: flex;
    flex-direction: column;
    gap: 8px;
}}
.cover-logo-row {{
    display: flex;
    align-items: center;
    gap: 12px;
}}
.cover-logo-img {{
    height: 32px;
    width: auto;
    object-contain: contain;
}}
.cover-top-sub {{
    font-size: 8pt;
    font-family: "SFMono-Regular", Consolas, monospace;
    letter-spacing: 1.5px;
    color: #71717a;
    text-transform: uppercase;
}}
.cover-body {{
    margin-top: auto;
    margin-bottom: auto;
    padding: 16mm 0 8mm 0;
}}
.cover-category {{
    font-size: 8pt;
    font-family: "SFMono-Regular", Consolas, monospace;
    letter-spacing: 2px;
    color: #a1a1aa;
    text-transform: uppercase;
    margin-bottom: 16px;
    font-weight: 600;
}}
.cover-title {{
    font-size: 26pt;
    font-weight: 800;
    line-height: 1.18;
    letter-spacing: -0.8px;
    color: #ffffff;
    margin-bottom: 22px;
}}
.cover-summary {{
    font-size: 10pt;
    line-height: 1.65;
    color: #a1a1aa;
    margin-bottom: 24mm;
    max-width: 165mm;
}}
.cover-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px 24px;
    max-width: 165mm;
    border-top: 1px solid #27272a;
    padding-top: 18px;
}}
.cover-grid-item-label {{
    font-size: 7.5pt;
    font-family: "SFMono-Regular", Consolas, monospace;
    letter-spacing: 1.2px;
    color: #71717a;
    text-transform: uppercase;
    margin-bottom: 4px;
}}
.cover-grid-item-val {{
    font-size: 9.5pt;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.2px;
}}
.cover-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #18181b;
    padding-top: 14px;
    font-size: 8pt;
    color: #52525b;
    font-family: "SFMono-Regular", Consolas, monospace;
}}

/* DEDICATED TOC PAGE */
.toc-page {{
    page: standard;
    page-break-before: always !important;
    page-break-after: always !important;
    break-before: page !important;
    break-after: page !important;
    padding-top: 5mm;
}}
.toc-page h2 {{
    font-size: 13.5pt !important;
    font-weight: 800 !important;
    letter-spacing: -0.3px !important;
    border-bottom: 2px solid #18181b !important;
    padding-bottom: 6px !important;
    margin-bottom: 12px !important;
    color: #09090b !important;
    text-transform: uppercase !important;
}}
.toc-page a, .toc-page a:visited, .toc-page a:active {{
    color: #18181b !important;
    text-decoration: none !important;
    font-weight: 500 !important;
}}
.toc-page a:hover {{
    color: #000000 !important;
    text-decoration: none !important;
}}
.toc-page code {{
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    font-family: inherit !important;
    font-size: inherit !important;
    color: inherit !important;
}}
.toc-page ol, .toc-page ul {{
    list-style: none !important;
    padding-left: 0 !important;
    margin: 0 !important;
}}
.toc-page li {{
    margin-bottom: 2.8px !important;
    line-height: 1.34 !important;
    color: #18181b !important;
    font-size: 8pt !important;
}}
.toc-page li ul, .toc-page li ol {{
    padding-left: 14px !important;
    margin-top: 2px !important;
    margin-bottom: 2px !important;
}}

/* BODY CONTENT & HEADINGS */
.body-content {{
    page: standard;
    page-break-before: always !important;
    break-before: page !important;
    max-width: 100%;
    overflow: hidden;
}}
h1 {{
    font-size: 16pt;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-top: 0;
    margin-bottom: 5px;
    color: #09090b;
    border-bottom: 2px solid #18181b;
    padding-bottom: 6px;
}}
h2 {{
    font-size: 11.5pt;
    font-weight: 700;
    margin-top: 14px;
    margin-bottom: 4px;
    color: #18181b;
}}
h3 {{
    font-size: 9.5pt;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 3px;
    color: #3f3f46;
}}
p, li {{
    color: #27272a;
    margin-bottom: 5px;
}}
ul, ol {{
    padding-left: 20px;
    margin-top: 2px;
    margin-bottom: 8px;
}}
strong {{
    font-weight: 700;
    color: #09090b;
}}
code {{
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 8pt;
    background-color: #f4f4f5;
    padding: 1.5px 3.5px;
    border-radius: 4px;
    border: 1px solid #e4e4e7;
    color: #09090b;
}}

/* UNBROKEN DIAGRAMS & NO HORIZONTAL SCROLL/CLIPPING */
pre, table, blockquote, .diagram-container {{
    page-break-inside: avoid !important;
    break-inside: avoid !important;
}}
pre {{
    background-color: #09090b;
    color: #f4f4f5;
    padding: 7px 9px;
    border-radius: 4px;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 5.1pt;
    line-height: 1.22;
    letter-spacing: -0.28px;
    white-space: pre !important;
    overflow: hidden !important;
    margin: 8px 0;
    max-width: 100% !important;
    box-sizing: border-box !important;
}}
pre code {{
    background-color: transparent !important;
    padding: 0 !important;
    border: none !important;
    color: inherit !important;
    font-size: inherit !important;
    letter-spacing: inherit !important;
    white-space: pre !important;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8pt;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
}}
th, td {{
    border: 1px solid #d4d4d8;
    padding: 5px 8px;
    text-align: left;
}}
th {{
    background-color: #f4f4f5;
    font-weight: 700;
    color: #09090b;
}}
hr {{
    border: none;
    border-top: 1px solid #e4e4e7;
    margin: 10px 0;
}}
</style>
</head>
<body>
{cover_html}
{content_html}
</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(html_path):
        os.remove(html_path)
    
    # Mirror to app/ directory
    app_pdf_path = os.path.join(APP_DIR, pdf_filename)
    shutil.copy2(pdf_path, app_pdf_path)
    
    # Verify compiled PDF content using fitz
    doc = fitz.open(pdf_path)
    pages = len(doc)
    text = ""
    for p in doc:
        text += p.get_text() + "\n"
    
    has_sys = "Sysvar1nstructions1111111111111111111111111" in text
    size_kb = os.path.getsize(pdf_path) / 1024.0
    
    # Verify 100% full bleed black on page 0
    p0 = doc[0]
    drawings = [d for d in p0.get_drawings() if d['type'] == 'f' and d.get('fill') == (0.0, 0.0, 0.0)]
    black_rect = drawings[0]['rect'] if drawings else None
    is_full_bleed = black_rect and black_rect.width >= p0.rect.width and black_rect.height >= p0.rect.height
    
    p1_text = doc[0].get_text()[:40].replace('\n', ' ')
    p2_text = doc[1].get_text()[:40].replace('\n', ' ')
    
    print(f"[{lang}] Compiled: {pages} pages | {size_kb:.1f} KB | FullBleed Black: {is_full_bleed} ({black_rect}) | Sysvar: {has_sys}")

if __name__ == "__main__":
    print("=== RECOMPILING ALL 10 OFFICIAL WHITEPAPER PDFS VIA MS EDGE HEADLESS ===")
    for lang in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
        compile_pdf(lang)
    print("\nALL 10 PDFS RECOMPILED & VERIFIED ACROSS WORKSPACE AND APP/!")
