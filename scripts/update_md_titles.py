# -*- coding: utf-8 -*-
import os, glob

TITLES = {
    'EN': '# HAICHAIN: The Economic Bedrock for the AI² Symbiotic Superintelligence Era',
    'ZH': '# HAICHAIN: AI² 共生超级智能时代的基石经济网络',
    'KO': '# HAICHAIN: AI² 공생 초지능 시대를 위한 경제적 기반',
    'ES': '# HAICHAIN: La Base Económica para la Era de la Superinteligencia Simbiótica AI²',
    'FR': '# HAICHAIN: Le Socle Économique pour l\'Ère de la Superintelligence Symbiotique AI²',
    'RU': '# HAICHAIN: Экономический фундамент для эпохи симбиотического сверхразума AI²',
    'KK': '# HAICHAIN: AI² симбиотикалық асқан интеллект дәуіріне арналған экономикалық іргетас',
    'HI': '# HAICHAIN: AI² सहजीवी सुपरइंटेलिजेंस युग के लिए आर्थिक आधार',
    'HE': '# HAICHAIN: התשתית הכלכלית לעידן בינת-העל הסימביוטית AI²',
    'VI': '# HAICHAIN: Nền Tảng Kinh Tế Cho Kỷ Nguyên Siêu Trí Tuệ Cộng Sinh AI²',
}

for folder in ['.', 'app']:
    for lang, title in TITLES.items():
        fname = os.path.join(folder, f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md')
        if not os.path.exists(fname):
            continue
        with open(fname, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Replace line 1 (first heading)
        if lines and lines[0].startswith('# '):
            lines[0] = title + '\n'
            with open(fname, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print(f'Updated {fname}')
