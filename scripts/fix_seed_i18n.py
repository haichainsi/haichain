# -*- coding: utf-8 -*-
import sys

for fpath in ['i18n.js', 'app/i18n.js']:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('"investor.seedNotice": "Стратегиялық үлестірім (7 млн долларлық FDV бойынша , 30% TGE жеңілдігі) және әзірлеуші құралдары"',
                  '"investor.seedNotice": "Стратегиялық үлестірім (7 млн долларлық FDV бойынша $175k, 30% TGE жеңілдігі) және әзірлеуші құралдары"')
    c = c.replace('"investor.seedNotice": "Allocation Stratégique ( à  FDV, 30% Remise TGE) et Outils"',
                  '"investor.seedNotice": "Allocation Stratégique ($175k à $7M FDV, 30% Remise TGE) et Outils"')
    c = c.replace('"investor.seedNotice": "전략적 배분 (700만 달러 FDV 기준 , 30% TGE 할인) 및 개발자 도구 세트"',
                  '"investor.seedNotice": "전략적 배분 (700만 달러 FDV 기준 $175k, 30% TGE 할인) 및 개발자 도구 세트"')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Fixed $175k in i18n files successfully.")
