import os, sys, shutil

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
from generate_pdf_whitepapers import build_pdf_from_markdown

# 1. Fix ES.md
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.md', 'r', encoding='utf-8') as f:
    t = f.read()
t = t.replace(
    "* **Captura de Valor del Token:** El 50% de las tarifas globales financia la **Recompra y Quema Continua (Buyback & Burn)**; el 50% se distribuye como **Rendimiento Real (USDC/USDT)** a los stakers de gobernanza veHAI.",
    "* **Captura de Valor del Token (Utilidad Conforme a Howey):** El 50% de las tarifas del protocolo financia la **Recompra y Quema Continua (Buyback & Burn)**; el 50% se asigna a Reservas del Protocolo y al fondo de seguros CHGB. Cero distribuciones pasivas de dividendos (arquitectura de utilidad que no constituye valor)."
)
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.md', 'w', encoding='utf-8') as f:
    f.write(t)
shutil.copy2('HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.md', 'app/HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.md')

# 2. Fix FR.md
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.md', 'r', encoding='utf-8') as f:
    t = f.read()
t = t.replace(
    "* **Accumulation de Valeur du Token:** 50% de l'ensemble des frais mondiaux financent le **Rachat & Destruction Automatique (Buyback & Burn)**; 50% sont distribués sous forme de **Rendement Réel (USDC/USDT)** aux stakers de gouvernance veHAI.",
    "* **Accumulation de Valeur du Token (Utilité Conforme à Howey):** 50% des frais de protocole financent le **Rachat & Destruction Automatique (Buyback & Burn)**; 50% sont alloués aux Réserves du Protocole et au CHGB. Zéro distribution passive de dividendes (architecture d'utilité non-titre financier)."
)
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.md', 'w', encoding='utf-8') as f:
    f.write(t)
shutil.copy2('HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.md', 'app/HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.md')

# 3. Fix HE.md
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.md', 'r', encoding='utf-8') as f:
    t = f.read()
t = t.replace(
    "* **צבירת ערך הטוקן:** 50% מעמלות הפרוטוקול העולמיות מיועדות ל**רכישה חוזרת ושריפה (Buyback & Burn)**; 50% מחולקים כ**תשואה אמיתית בסטייבלקוינס (USDC/USDT)** למחזיקי veHAI.",
    "* **צבירת ערך הטוקן (תועלת תואמת מבחן Howey):** 50% מעמלות הפרוטוקול מיועדות ל**רכישה חוזרת ושריפה (Buyback & Burn)**; 50% מוקצות לעתודות הפרוטוקול וקרן ביטוח CHGB. אפס חלוקת דיבידנדים פסיביים (ארכיטקטורת תועלת שאינה נייר ערך)."
)
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.md', 'w', encoding='utf-8') as f:
    f.write(t)
shutil.copy2('HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.md', 'app/HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.md')

# 4. Fix HI.md
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.md', 'r', encoding='utf-8') as f:
    t = f.read()
t = t.replace(
    "* **टोकन मूल्य संचय:** वैश्विक निपटान शुल्क का 50% स्वचालित **बायबैक और बर्न** में जाता है; 50% veHAI स्टेकरों को **शुद्ध स्टेबलकॉइन (USDC/USDT)** के रूप में रियल यील्ड के रूप में वितरित किया जाता है।",
    "* **टोकन मूल्य संचय (Howey परीक्षण अनुपालक उपयोगिता):** प्रोटोकॉल शुल्क का 50% स्वचालित **बायबैक और बर्न** में जाता है; 50% प्रोटोकॉल रिजर्व और CHGB बीमा फंड को आवंटित किया जाता है। शून्य निष्क्रिय लाभांश वितरण (गैर-सुरक्षा उपयोगिता वास्तुकला)।"
)
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.md', 'w', encoding='utf-8') as f:
    f.write(t)
shutil.copy2('HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.md', 'app/HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.md')

# 5. Fix RU.md
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.md', 'r', encoding='utf-8') as f:
    t = f.read()
t = t.replace(
    "* **Накопление стоимости токена:** 50% всех сборов направляются на **Автоматический выкуп и сжигание (Buyback & Burn)**; 50% выплачиваются в **чистых стейблкоинах (USDC/USDT)** в качестве 50% Buyback & Burn + 50% Protocol Reserves (CHGB - Howey Test Compliant).",
    "* **Накопление стоимости токена (Howey Test Compliant):** 50% сборов протокола направляются на **Автоматический выкуп и сжигание (Buyback & Burn)**; 50% выделяются в Резервы протокола и страховой фонд CHGB. Ноль пассивных дивидендных выплат (чисто утилитарная архитектура без признаков ценной бумаги)."
)
with open('HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.md', 'w', encoding='utf-8') as f:
    f.write(t)
shutil.copy2('HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.md', 'app/HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.md')

print("Recompiling the 5 updated memos...")
for lang, md, pdf in [
    ('es', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.md', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_ES.pdf'),
    ('fr', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.md', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_FR.pdf'),
    ('he', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.md', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_HE.pdf'),
    ('hi', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.md', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_HI.pdf'),
    ('ru', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.md', 'HAICHAIN_PRESEED_ONE_PAGER_MEMO_RU.pdf'),
]:
    build_pdf_from_markdown(md, pdf, lang=lang)
    shutil.copy2(pdf, os.path.join('app', pdf))
    print(f"Recompiled and synced {pdf}")

print("Done updating and recompiling the 5 memos.")
