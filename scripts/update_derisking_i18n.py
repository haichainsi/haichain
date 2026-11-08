import os, re

i18n_path = 'app/i18n.js'
with open(i18n_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any lingering hype terms with precise institutional terms
replacements = [
    ("v1.1 PRODUCTION CERTIFIED (CapLeaf v1 & 9 Invariants)", "v1.1 PROTOCOL SPECIFICATION (Live on Solana Devnet • Pre-Audit Stage)"),
    ("100% COMPLETED (LIVE & VERIFIED ON DEVNET)", "CORE INVARIANTS IMPLEMENTED (72/72 PASSING TESTS • LIVE ON DEVNET)"),
    ("100% ĐÃ HOÀN THÀNH (ĐÃ XÁC MINH TRÊN DEVNET)", "ĐÃ HOÀN THÀNH BỘ BẤT BIẾN LÕI (72/72 BÀI TEST XANH • TRÊN DEVNET)"),
    ("100% 已完成 (DEVNET 实机已验证)", "核心不变量已完成 (72/72 单元测试通过 • DEVNET 实机运行)"),
    ("100% 완료 (DEVNET 검증 완료)", "핵심 불변성 구현 완료 (72/72 테스트 통과 • DEVNET 가동)"),
    ("100% COMPLETADO (VERIFICADO EN DEVNET)", "INVARIANTES PRINCIPALES IMPLEMENTADOS (72/72 TESTS PASADOS • EN DEVNET)"),
    ("100% TERMINÉ (VÉRIFIÉ SUR DEVNET)", "INVARIANTS CLÉS IMPLÉMENTÉS (72/72 TESTS RÉUSSIS • SUR DEVNET)"),
    ("100% ЗАВЕРШЕНО (ПРОВЕРЕНО НА DEVNET)", "КЛЮЧЕВЫЕ ИНВАРИАНТЫ РЕАЛИЗОВАНЫ (72/72 ТЕСТОВ ПРОЙДЕНО • НА DEVNET)"),
    ("100% АЯҚТАЛДЫ (DEVNET-ТЕ ТЕКСЕРІЛГЕН)", "НЕГІЗГІ ИНВАРИАНТТАР ІСКЕ АСЫРЫЛДЫ (72/72 ТЕСТ ӨТКЕН • DEVNET-ТЕ)"),
    ("100% पूर्ण (DEVNET पर सत्यापित)", "मुख्य इनवेरिएंट लागू (72/72 परीक्षण सफल • DEVNET पर सक्रिय)"),
    ("100% הושלם (מאומת ב-DEVNET)", "אינווריאנטים מרכזיים יושמו (72/72 מבחנים עברו • ב-DEVNET)"),
    ("Confidential Institutional Early Backer allocation", "Confidential Strategic Contributor & Ecosystem allocation"),
    ("Phân bổ Nhà đầu tư sớm Thể chế Kín", "Phân bổ Người đóng góp Chiến lược & Hệ sinh thái"),
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        print(f"Replaced: {old[:40]} -> {new[:40]}")

with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated app/i18n.js successfully.")
