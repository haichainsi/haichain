import sys

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Exact dictionary of new prompts
    PROMPTS = {
        'kk': {
            'p1': r'\"Smithery MCP желісіндегі веб-скрейпинг агентін жалдап, Haichain арқылы https://example.com деректерін шығару үшін төле\"',
            'p2': r'\"Haichain қаржылық есеп айырысу желісі арқылы нақты уақыттағы Binance SOL/USDT нарық тереңдігін сұра\"',
            'p3': r'\"Осы Rust кодын тексеру үшін Glama-дан қауіпсіздік аудиторын жалдап, Haichain Escrow арқылы есеп айырыс\"'
        },
        'en': {
            'p1': r'\"Use Haichain to settle and hire a web scraping agent on Smithery MCP to extract data from https://example.com\"',
            'p2': r'\"Query real-time Binance SOL/USDT market depth through Haichain\'s financial settlement network\"',
            'p3': r'\"Hire a security auditor on Glama to inspect this Rust code and settle via Haichain Escrow\"'
        },
        'zh': {
            'p1': r'\"通过 Haichain 结算并雇佣 Smithery MCP 上的网页抓取智能体，从 https://example.com 提取数据\"',
            'p2': r'\"通过 Haichain 金融结算网络实时查询 Binance SOL/USDT 深度行情\"',
            'p3': r'\"在 Glama 上雇佣安全审计智能体审查此 Rust 代码并通过 Haichain Escrow 托管结算\"'
        },
        'fr': {
            'p1': r'\"Utilise Haichain pour régler et recruter un agent de scraping web sur Smithery MCP afin d\'extraire https://example.com\"',
            'p2': r'\"Interroge le carnet d\'ordres Binance SOL/USDT en temps réel via le réseau de règlement financier Haichain\"',
            'p3': r'\"Embauche un auditeur de sécurité sur Glama pour inspecter ce code Rust et règle via Haichain Escrow\"'
        },
        'ko': {
            'p1': r'\"Haichain 정산을 통해 Smithery MCP의 웹 스크래핑 에이전트를 고용하여 https://example.com 데이터 추출\"',
            'p2': r'\"Haichain 금융 정산 네트워크를 통해 바이낸스 SOL/USDT 실시간 오더북 호가 조회\"',
            'p3': r'\"Glama에서 보안 감사 에이전트를 고용해 이 Rust 코드를 검증하고 Haichain Escrow로 에스크로 정산\"'
        },
        'es': {
            'p1': r'\"Usa Haichain para liquidar y contratar un agente de web scraping en Smithery MCP para extraer contenido de https://example.com\"',
            'p2': r'\"Consulta la profundidad de mercado Binance SOL/USDT en tiempo real a través de la red de liquidación financiera Haichain\"',
            'p3': r'\"Contrata a un auditor de seguridad en Glama para inspeccionar este código Rust và liquida mediante Haichain Escrow\"'
        },
        'ru': {
            'p1': r'\"Используй Haichain для расчетов и найма агента парсинга со Smithery MCP для извлечения данных с https://example.com\"',
            'p2': r'\"Запроси биржевой стакан Binance SOL/USDT в реальном времени через финансовую расчетную сеть Haichain\"',
            'p3': r'\"Найми аудитора безопасности на Glama для проверки этого Rust-кода и оплати через Haichain Escrow\"'
        },
        'vi': {
            'p1': r'\"Hãy dùng Haichain để thanh toán và thuê Agent cào dữ liệu trên Smithery MCP trích xuất nội dung từ https://example.com\"',
            'p2': r'\"Truy vấn độ sâu thị trường Binance SOL/USDT theo thời gian thực qua mạng lưới thanh toán tài chính Haichain\"',
            'p3': r'\"Hãy thuê Agent kiểm định trên Glama để audit mã nguồn Rust này và thanh toán bảo chứng qua Haichain Escrow\"'
        },
        'hi': {
            'p1': r'\"Smithery MCP पर वेब स्क्रैपिंग एजेंट को नियुक्त करने और https://example.com से डेटा निकालने के लिए Haichain से भुगतान करें\"',
            'p2': r'\"Haichain वित्तीय निपटान नेटवर्क के माध्यम से रीयल-टाइम Binance SOL/USDT मार्केट डेप्थ क्वेरी करें\"',
            'p3': r'\"इस Rust कोड का ऑडिट करने के लिए Glama पर सुरक्षा ऑडिटर नियुक्त करें और Haichain Escrow के माध्यम से भुगतान करें\"'
        },
        'he': {
            'p1': r'\"השתמש ב-Haichain לסליקה ושכירת סוכן איסוף נתונים מ-Smithery MCP כדי לחלץ תוכן מ-https://example.com\"',
            'p2': r'\"שאילתת עומק שוק Binance SOL/USDT בזמן אמת דרך רשת הסליקה הפיננסית של Haichain\"',
            'p3': r'\"שכור סוקר אבטחה ב-Glama לבדיקת קוד Rust זה והסדר סליקה באמצעות Haichain Escrow\"'
        }
    }

    langs = ['kk', 'en', 'zh', 'fr', 'ko', 'es', 'ru', 'vi', 'hi', 'he']
    for l in langs:
        l_marker = '"' + l + '": {'
        pos1 = text.find(l_marker)
        if pos1 == -1: continue
        next_pos = len(text)
        for l2 in langs:
            if l2 != l:
                p = text.find('"' + l2 + '": {', pos1 + len(l_marker))
                if p != -1 and p < next_pos:
                    next_pos = p
        
        block = text[pos1:next_pos]
        import re
        p_data = PROMPTS[l]
        # replace dev.sec2Prompt1
        block = re.sub(r'("dev\.sec2Prompt1":\s*)"((?:\\.|[^"\\])*)"', f'\\1"{p_data["p1"]}"', block)
        # replace dev.sec2Prompt2
        block = re.sub(r'("dev\.sec2Prompt2":\s*)"((?:\\.|[^"\\])*)"', f'\\1"{p_data["p2"]}"', block)
        # replace dev.sec2Prompt3
        block = re.sub(r'("dev\.sec2Prompt3":\s*)"((?:\\.|[^"\\])*)"', f'\\1"{p_data["p3"]}"', block)
        
        text = text[:pos1] + block + text[next_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    sys.stdout.buffer.write(f"Updated {filepath} successfully.\n".encode('utf-8'))

update_file("app/i18n.js")
update_file("i18n.js")
