# -*- coding: utf-8 -*-
import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

whitepapers = [
    'HAICHAIN_WHITEPAPER_V1.0_EN.md',
    'HAICHAIN_WHITEPAPER_V1.0_VI.md',
    'HAICHAIN_WHITEPAPER_V1.0_ZH.md',
    'HAICHAIN_WHITEPAPER_V1.0_ES.md',
    'HAICHAIN_WHITEPAPER_V1.0_FR.md',
    'HAICHAIN_WHITEPAPER_V1.0_KO.md',
    'HAICHAIN_WHITEPAPER_V1.0_RU.md',
    'HAICHAIN_WHITEPAPER_V1.0_KK.md',
    'HAICHAIN_WHITEPAPER_V1.0_HI.md',
    'HAICHAIN_WHITEPAPER_V1.0_HE.md'
]

for fname in whitepapers:
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()

    # Clean leftover line in VI diagram
    c = c.replace('└── 50% Nạp Quỹ Bảo Hiểm Rủi Ro (CHGB) để bảo chứng vốn và thanh khoản khẩn cấp mà không vướng rủi ro chứng khoán.\n                                                    cho người cọc hạn (veHAISI)',
                  '└── 50% Nạp Quỹ Bảo Hiểm Rủi Ro CHGB\n                                                    (Bảo vệ thanh khoản khẩn cấp)')

    # Save
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)

    app_target = os.path.join('app', fname)
    with open(app_target, 'w', encoding='utf-8') as f:
        f.write(c)

print("Diagram formatting polished.")
