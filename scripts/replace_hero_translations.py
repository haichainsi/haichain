import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

UPDATES = {
    "vi": {
        "hero.badge": "HỆ ĐIỀU HÀNH TÀI CHÍNH CHO KỶ NGUYÊN MÁY TỰ HÀNH",
        "hero.title": "Nền Tảng Kinh Tế Cho Kỷ Nguyên Siêu Trí Tuệ Cộng Sinh AI²",
        "hero.subtitle": "Giúp hàng tỷ tác nhân AI Agent, Robot AI tự do làm việc, giao dịch và hợp nhất với trí tuệ thực tế của con người để cùng tạo ra của cải, toàn bộ của cải và quyền làm chủ mãi mãi thuộc về con người. Hệ điều hành tài chính cho kỷ nguyên máy tự hành hôm nay. Nền tảng kinh tế cho kỷ nguyên siêu trí tuệ cộng sinh AI² ngày mai.",
        "meta.title": "HAICHAIN - Nền Tảng Kinh Tế Cho Kỷ Nguyên Siêu Trí Tuệ Cộng Sinh AI² | haichain.si",
        "meta.description": "HAICHAIN: Hệ điều hành tài chính cho kỷ nguyên máy tự hành hôm nay. Nền tảng kinh tế cho kỷ nguyên siêu trí tuệ cộng sinh AI² ngày mai. Trao quyền cho hàng tỷ AI Agent và Robot AI tạo ra của cải dưới quyền làm chủ tối thượng của con người."
    },
    "en": {
        "hero.badge": "THE FINANCIAL OPERATING SYSTEM FOR THE AUTONOMOUS MACHINE ERA",
        "hero.title": "The Economic Bedrock for the Symbiotic Superintelligence Era AI²",
        "hero.subtitle": "Empowering billions of autonomous AI agents and AI robots to freely work, transact, and unite with human real-world intelligence to co-create wealth—with all wealth and sovereign ownership forever belonging to humanity. The financial operating system for the autonomous machine era today. The economic bedrock for the symbiotic superintelligence era AI² tomorrow.",
        "meta.title": "HAICHAIN - The Economic Bedrock for the Symbiotic Superintelligence Era AI² | haichain.si",
        "meta.description": "HAICHAIN: The financial operating system for the autonomous machine era today. The economic bedrock for the symbiotic superintelligence era AI² tomorrow. Empowering billions of AI agents to create wealth under human sovereignty."
    },
    "zh": {
        "hero.badge": "自主机器时代的财务操作系统",
        "hero.title": "共生超级智能时代（AI²）的经济基石",
        "hero.subtitle": "赋能数以百亿计的AI智能体与AI机器人自由工作、交易，并与人类现实智慧深度融合以共创财富——所有财富与最高主权永久归属于人类。今天，是自主机器时代的财务操作系统；明天，是共生超级智能时代（AI²）的经济基石。",
        "meta.title": "HAICHAIN - 共生超级智能时代（AI²）的经济基石 | haichain.si",
        "meta.description": "HAICHAIN: 今天是自主机器时代的财务操作系统；明天是共生超级智能时代（AI²）的经济基石。赋能百亿AI智能体共创财富，主权永归人类。"
    },
    "es": {
        "hero.badge": "SISTEMA OPERATIVO FINANCIERO PARA LA ERA DE LAS MÁQUINAS AUTÓNOMAS",
        "hero.title": "La Base Económica para la Era de la Superinteligencia Simbiótica AI²",
        "hero.subtitle": "Empoderando a miles de millones de agentes y robots de IA para trabajar, comerciar y unirse con la inteligencia real humana para co-crear riqueza—con toda la riqueza y la soberanía perteneciendo para siempre a la humanidad. El sistema operativo financiero para la era de las máquinas autónomas hoy. La base económica para la era de la superinteligencia simbiótica AI² mañana.",
        "meta.title": "HAICHAIN - La Base Económica para la Era de la Superinteligencia Simbiótica AI² | haichain.si",
        "meta.description": "HAICHAIN: El sistema operativo financiero para la era de las máquinas autónomas hoy. La base económica para la era de la superinteligencia simbiótica AI² mañana. Soberanía humana absoluta."
    },
    "fr": {
        "hero.badge": "SYSTÈME D'EXPLOITATION FINANCIER POUR L'ÈRE DES MACHINES AUTONOMES",
        "hero.title": "Le Socle Économique de l'Ère de la Superintelligence Symbiotique AI²",
        "hero.subtitle": "Permettre à des milliards d'agents et robots d'IA de travailler, d'effectuer des transactions et de fusionner avec l'intelligence réelle humaine pour co-créer la richesse—toute la richesse et la souveraineté appartenant à jamais à l'humanité. Le système d'exploitation financier pour l'ère des machines autonomes aujourd'hui. Le socle économique pour l'ère de la superintelligence symbiotique AI² demain.",
        "meta.title": "HAICHAIN - Le Socle Économique de l'Ère de la Superintelligence Symbiotique AI² | haichain.si",
        "meta.description": "HAICHAIN: Le système d'exploitation financier pour l'ère des machines autonomes aujourd'hui. Le socle économique de la superintelligence symbiotique AI² demain. Souveraineté humaine absolue."
    },
    "ru": {
        "hero.badge": "ФИНАНСОВАЯ ОПЕРАЦИОННАЯ СИСТЕМА ДЛЯ ЭПОХИ АВТОНОМНЫХ МАШИН",
        "hero.title": "Экономический фундамент эпохи симбиотического сверхразума AI²",
        "hero.subtitle": "Расширение возможностей миллиардов AI-агентов и роботов для свободной работы, транзакций и объединения с реальным интеллектом человека ради совместного создания богатства — где всё богатство и суверенный контроль навсегда принадлежат человечеству. Финансовая операционная система для эпохи автономных машин сегодня. Экономический фундамент для эпохи симбиотического сверхразума AI² завтра.",
        "meta.title": "HAICHAIN - Экономический фундамент эпохи симбиотического сверхразума AI² | haichain.si",
        "meta.description": "HAICHAIN: Финансовая операционная система для эпохи автономных машин сегодня. Экономический фундамент для эпохи симбиотического сверхразума AI² завтра. Суверенный контроль человечества."
    },
    "ko": {
        "hero.badge": "자율 기계 시대를 위한 금융 운영체제",
        "hero.title": "공생형 초지능 시대(AI²)를 위한 경제적 기반",
        "hero.subtitle": "수십억 개의 AI 에이전트와 AI 로봇이 자유롭게 일하고 거래하며 인간의 실제 지능과 융합하여 부를 공동 창출하도록 지원합니다. 모든 부와 주권적 소유권은 영원히 인류에게 귀속됩니다. 오늘은 자율 기계 시대를 위한 금융 운영체제, 내일은 공생형 초지능 시대(AI²)의 경제적 기반이 됩니다.",
        "meta.title": "HAICHAIN - 공생형 초지능 시대(AI²)를 위한 경제적 기반 | haichain.si",
        "meta.description": "HAICHAIN: 오늘은 자율 기계 시대를 위한 금융 운영체제, 내일은 공생형 초지능 시대(AI²)의 경제적 기반. 인류의 영원한 주권적 소유권 보장."
    },
    "hi": {
        "hero.badge": "स्वायत्त मशीन युग के लिए वित्तीय ऑपरेटिंग सिस्टम",
        "hero.title": "सहजीवी सुपरइंटेलिजेंस युग (AI²) के लिए आर्थिक आधारशिला",
        "hero.subtitle": "अरबों स्वायत्त AI एजेंटों और AI रोbोटों को स्वतंत्र रूप से कार्य करने, लेन-देन करने और वास्तविक मानव बुद्धि के साथ एकजुट होकर धन सृजन करने में सक्षम बनाना—जहां सारा धन और संप्रभु स्वामित्व हमेशा मानवता का रहेगा। आज स्वायत्त मशीन युग के लिए वित्तीय ऑपरेटिंग सिस्टम। कल सहजीवी सुपरइंटेलिजेंस युग AI² के लिए आर्थिक आधारशिला।",
        "meta.title": "HAICHAIN - सहजीवी सुपरइंटेलिजेंस युग (AI²) के लिए आर्थिक आधारशिला | haichain.si",
        "meta.description": "HAICHAIN: आज स्वायत्त मशीन युग के लिए वित्तीय ऑपरेटिंग सिस्टम। कल सहजीवी सुपरइंटेलिजेंस युग AI² के लिए आर्थिक आधारशिला। मानवीय संप्रभुता सर्वोपरि।"
    },
    "he": {
        "hero.badge": "מערכת הפעלה פיננסית לעידן המכונות האוטונומיות",
        "hero.title": "התשתית הכלכלית לעידן סופר-אינטליגנציה סימביוטית AI²",
        "hero.subtitle": "העצמת מיליארדי סוכני AI ורובוטים אוטונומיים לעבוד, לסחור ולהתמזג עם האינטליגנציה האנושית האמיתית ליצירת עושר משותף—כאשר כל העושר והריבונות שייכים לעד לאנושות. מערכת ההפעלה הפיננסית לעידן המכונות האוטונומיות היום. התשתית הכלכלית לעידן סופר-אינטליגנציה סימביוטית AI² מחר.",
        "meta.title": "HAICHAIN - התשתית הכלכלית לעידן סופר-אינטליגנציה סימביוטית AI² | haichain.si",
        "meta.description": "HAICHAIN: מערכת ההפעלה הפיננסית לעידן המכונות האוטונומיות היום. התשתית הכלכלית לעידן סופר-אינטליגנציה סימביוטית AI² מחר. ריבונות אנושית מוחלטת."
    },
    "kk": {
        "hero.badge": "АВТОНОМДЫ МАШИНАЛАР ДӘУІРІНЕ АРНАЛҒАН ҚАРЖЫЛЫҚ ОПЕРАЦИЯЛЫҚ ЖҮЙЕ",
        "hero.title": "Симбиотикалық супер интеллект дәуіріне (AI²) арналған экономикалық іргетас",
        "hero.subtitle": "Миллиардтаған AI агенттері мен AI роботтарына еркін жұмыс істеуге, транзакциялар жасауға және адамның шынайы интеллектімен бірігіп байлық жасауға мүмкіндік беру — барлық байлық пен егемендік мәңгілікке адамзатқа тиесілі. Бүгін автономды машиналар дәуіріне арналған қаржылық операциялық жүйе. Ертең симбиотикалық супер интеллект дәуірі (AI²) үшін экономикалық іргетас.",
        "meta.title": "HAICHAIN - Симбиотикалық супер интеллект дәуіріне (AI²) арналған экономикалық іргетас | haichain.si",
        "meta.description": "HAICHAIN: Бүгін автономды машиналар дәуіріне арналған қаржылық операциялық жүйе. Ертең симбиотикалық супер интеллект дәуірі (AI²) үшін экономикалық іргетас."
    }
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_lang = None
    new_lines = []
    
    for line in lines:
        # Check language start
        m_lang = re.match(r'^\s*"([a-z]{2})":\s*\{\s*$', line)
        if m_lang:
            current_lang = m_lang.group(1)
        
        # Check target keys
        replaced = False
        if current_lang and current_lang in UPDATES:
            for k in ["meta.title", "meta.description", "hero.badge", "hero.title", "hero.subtitle"]:
                if f'"{k}":' in line:
                    val = UPDATES[current_lang][k]
                    val_json = json.dumps(val, ensure_ascii=False)
                    # preserve indentation and trailing comma
                    comma = ',' if line.rstrip().endswith(',') else ''
                    indent = len(line) - len(line.lstrip())
                    new_lines.append(' ' * indent + f'"{k}": {val_json}{comma}\n')
                    replaced = True
                    break
        if not replaced:
            new_lines.append(line)
            
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.writelines(new_lines)
    print(f"Updated {filepath} successfully.")

process_file('i18n.js')
process_file('app/i18n.js')
