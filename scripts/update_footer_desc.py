import json
import re

footer_translations = {
    'vi': 'Hệ điều hành tài chính & nhận thức phổ quát dành cho máy móc tự hành. Ký quỹ vi mô phi lưu ký và thanh toán năng lực AI tức thì trên Solana - Nền tảng kiến tạo Siêu Trí Tuệ Phi Tập Trung.',
    'en': 'Universal Autonomous Machine Financial & Cognitive Operating System. Non-custodial micro-escrows and instant AI capability settlements on Solana - The Bedrock for Decentralized Superintelligence.',
    'zh': '自主机器通用财务与认知操作系统。基于 Solana 的非托管微型托管与即时 AI 能力结算 - 去中心化超级智能的基石。',
    'fr': "Système d'exploitation cognitif et financier universel pour machines autonomes. Micro-tiers de confiance non dépositaires et règlements instantanés des capacités IA sur Solana - Le socle de la superintelligence décentralisée.",
    'ko': '자율 기계를 위한 보편적 금융 및 인지 운영체제. Solana 기반 비수탁 마이크로 에스크로 및 즉각적인 AI 역량 결제 - 탈중앙화 초지능을 구축하는 기반.',
    'es': 'Sistema operativo cognitivo y financiero universal para máquinas autónomas. Micro-fideicomisos no custodiales y liquidaciones instantáneas de capacidades de IA en Solana - La base de la superinteligencia descentralizada.',
    'ru': 'Универсальная финансовая и когнитивная операционная система для автономных машин. Некастодиальные микро-эскроу и мгновенные расчеты возможностей ИИ на Solana - фундамент децентрализованного сверхразума.',
    'kk': 'Автономды машиналарға арналған әмбебап қаржылық және когнитивтік операциялық жүйе. Solana-дағы кастодиалды емес микро-эскроу және AI мүмкіндіктерін лезде есептеу - деорталықтандырылған супер интеллекті құру негізі.',
    'hi': 'स्वायत्त मशीनों के लिए सार्वभौमिक वित्तीय और संज्ञानात्मक ऑपरेटिंग सिस्टम। सोलाना पर गैर-कस्टोडियल माइक्रो-एस्क्रो और त्वरित एआई क्षमता निपटान - विकेंद्रीकृत सुपरइंटेलिजेंस के निर्माण की नींव।',
    'he': 'מערכת הפעלה פיננסית וקוגניטיבית אוניברסלית למכונות אוטונומיות. מיקרו-נאמנות ללא משמורת והסדרי יכולות AI מיידיים על Solana - הבסיס ליצירת סופר-אינטליגנציה מבוזרת.'
}

# 1. Update i18n.js and app/i18n.js
for filepath in ['i18n.js', 'app/i18n.js']:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    start_line = 42
    end_line = 4013
    raw_json = lines[start_line][len('  const TRANSLATIONS = '):] + ''.join(lines[start_line+1:end_line]) + '}'
    data = json.loads(raw_json)
    
    for lang, val in footer_translations.items():
        clean_val = val.replace('\u2014', '-')
        data[lang]['footer.desc'] = clean_val
        if 'home.footerDesc' in data[lang]:
            data[lang]['home.footerDesc'] = clean_val

    formatted = json.dumps(data, indent=2, ensure_ascii=False)
    new_lines = lines[:start_line] + ['  const TRANSLATIONS = ' + formatted + ';\n'] + lines[end_line+1:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f'Updated {filepath} footer descriptions across 10 languages')

# 2. Update index.html and app/index.html static fallback
old_footer_pattern = re.compile(
    r'(<p[^>]*data-i18n="footer\.desc"[^>]*>)[\s\S]*?(</p>)',
    re.MULTILINE
)
new_footer_html = (
    r'\1\n'
    'Universal Autonomous Machine Financial &amp; Cognitive Operating System. Non-custodial micro-escrows and instant AI capability settlements on Solana - The Bedrock for Decentralized Superintelligence.\n'
    r'\2'
)

for html_file in ['index.html', 'app/index.html']:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content, count = old_footer_pattern.subn(new_footer_html, content)
    if count > 0:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated static footer.desc in {html_file}')
    else:
        print(f'Warning: footer.desc pattern not matched in {html_file}')
