# -*- coding: utf-8 -*-
"""
HAICHAIN Risk Due Diligence Report - Complete Multi-Language Invariant & Formula Fix
Updates scripts/build_all_risk_reports.py and recompiles all 10 PDFs with flawless formatting:
1. Fixes underscore subscript bug (payee\_ata -> clean payee_ata code badge)
2. Fixes list numbering reset bug (guaranteed 1 to 9 invariant cards)
3. Fixes math symbols (leq, geq, land, neg, forall, in, omega, tau, etc.)
4. Adds full 9 Invariants with mathematical formulas across ALL 10 LANGUAGES
5. Recompiles all 10 PDFs and updates web deployment targets
"""

import os
import re
import sys
import shutil
import subprocess
import markdown

sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
LOGO_PATH = os.path.join(WORKSPACE_DIR, "assets", "haichain-official-logo-white.png")

# Complete 9 Mathematical Invariants data across all 10 languages
INVARIANTS_DATA = {
    'en': {
        'sec_title': '4. MATHEMATICAL INVARIANTS AUDIT REPORT ($I_1 \\dots I_9$)',
        'sec_intro': 'Every on-chain instruction in `programs/haichain-core/src/lib.rs` preserves all 9 state invariants without exception:',
        'items': [
            ("1", "Conservation of Capital", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{Net Deposits}", "Verified by `test_invariant_i1_conservation` in test suite."),
            ("2", "Canonical Payee Safety", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "Enforced on-chain via Anchor constraint; prevents third-party token account redirection."),
            ("3", "Budget Ceiling", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "Checked before every reserve or settlement execution."),
            ("4", "Autonomous Velocity Rate Limiter", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "Prevents rapid automated capital drainage."),
            ("5", "Monotonic PDA Narrowing", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "Child instances cannot broaden permissions granted by parent."),
            ("6", "Panic Epoch & Freeze Isolation", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "Instant protocol shutdown completely halts all voucher processing."),
            ("7", "Heartbeat Expiration", r"\text{current\_time} \le \text{valid\_until}", "Stale or abandoned sessions cannot execute new reserves."),
            ("8", "Monotonic Settlement & Settle-Once", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "Guarantees zero double-spending across channel vouchers."),
            ("9", "Sybil Account Isolation", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ is unique}', "One capability leaf maps to exactly one on-chain account.")
        ]
    },
    'vi': {
        'sec_title': '4. BÁO CÁO KIỂM TOÁN 9 BẤT BIẾN TOÁN HỌC ($I_1 \\dots I_9$)',
        'sec_intro': 'Mọi chỉ thị trên chuỗi trong `programs/haichain-core/src/lib.rs` đều bảo toàn 9 bất biến trạng thái không có ngoại lệ:',
        'items': [
            ("1", "Bảo toàn Vốn Tối cao", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{Tổng Tiền Nạp Ròng}", "Được xác thực bởi kiểm thử `test_invariant_i1_conservation` trong bộ kiểm thử."),
            ("2", "An toàn Người Thụ hưởng Đích thực", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "Thực thi trên chuỗi qua ràng buộc Anchor; triệt tiêu hoàn toàn chuyển hướng tài khoản bên thứ ba."),
            ("3", "Hạn mức Ngân sách Bất biến", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "Kiểm tra bắt buộc trước mọi thao tác dự trữ hoặc thanh toán."),
            ("4", "Giới hạn Tốc độ Tiêu tiền Tự hành", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "Ngăn chặn hành vi rút cạn vốn thần tốc tự động."),
            ("5", "Thu hẹp Quyền Hạn Đơn điệu PDA", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "Các thực thể con không bao giờ có thể mở rộng quyền vượt quá thực thể cha."),
            ("6", "Cách ly Kỷ nguyên Khẩn cấp & Đóng băng Tức thì", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "Đóng băng hệ thống lập tức vô hiệu hóa 100% chứng từ thanh toán đang lưu hành."),
            ("7", "Hạn Khóa Phiên Làm việc Sinh trắc học", r"\text{current\_time} \le \text{valid\_until}", "Các phiên làm việc hết hạn hoặc bị bỏ rơi không thể thực hiện thêm giao dịch."),
            ("8", "Thanh toán Đơn điệu & Quyết toán Một lần", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "Đảm bảo tuyệt đối không có gian lận chi tiêu kép giữa các chứng từ."),
            ("9", "Cách ly Tài khoản Chống Tấn công Sybil", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ là duy nhất}', "Một lá phân quyền tương ứng chính xác với một tài khoản trên chuỗi duy nhất.")
        ]
    },
    'zh': {
        'sec_title': '4. 9 大数学不变性链上审计报告 ($I_1 \\dots I_9$)',
        'sec_intro': '`programs/haichain-core/src/lib.rs` 中的所有链上指令均严格且不可改变地遵循以下 9 大数学不变性：',
        'items': [
            ("1", "资本守恒定律", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{净充值总额}", "在测试套件中通过 `test_invariant_i1_conservation` 严格验证。"),
            ("2", "规范收款人安全", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "通过 Anchor 链上约束强制执行，杜绝第三方代币账户劫持重定向。"),
            ("3", "预算绝不超支", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "在每次预留资金或通道结算执行前进行确定性安全核验。"),
            ("4", "自主速率限流", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "彻底阻断恶意并发调用导致的瞬时自动化资金抽干攻击。"),
            ("5", "PDA 单调权限收窄", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "子实例派生权限只能逐级缩减，绝无法突破上级授权边界。"),
            ("6", "纪元隔离与即时冻结", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "触发主控熔断后，当前金库下存量未结算的所有离线凭证全部作废。"),
            ("7", "心跳会话过期机制", r"\text{current\_time} \le \text{valid\_until}", "超时或废弃的智能体代理会话无法再发起任何新增资金锁定。"),
            ("8", "单调单次清算", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "彻底消除各通道凭证之间的双花欺诈与重放攻击。"),
            ("9", "账户防重叠隔离", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ 唯一绑定}', "每个能力叶节点严格一对一映射到唯一的链上独立账户。")
        ]
    },
    'ko': {
        'sec_title': '4. 9대 수학적 불변성 온체인 감사 보고서 ($I_1 \\dots I_9$)',
        'sec_intro': '`programs/haichain-core/src/lib.rs`의 모든 온체인 명령어는 예외 없이 다음 9가지 상태 불변성을 영구히 준수합니다:',
        'items': [
            ("1", "자본 보존의 법칙", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{순 예치금 총액}", "테스트 스위트의 `test_invariant_i1_conservation` 검증을 통해 완전 보장."),
            ("2", "정규 수취인 안전성", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "Anchor 온체인 제약 조건을 통해 강제 집행; 제3자 토큰 계정 탈취 원천 차단."),
            ("3", "불가침 예산 상한선", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "모든 자금 예약 및 정산 실행 전 온체인 사전 검증 완료."),
            ("4", "자율 속도 제한기", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "자동화된 급속 자본 유출 공격을 사전에 완벽 차단."),
            ("5", "단조적 PDA 권한 축소", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "하위 인스턴스는 상위 인스턴스가 부여한 권한 범위를 결코 확장할 수 없음."),
            ("6", "패닉 에포크 및 즉각 동결 격리", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "프로토콜 셧다운 즉시 유통 중인 모든 미정산 바우처 일괄 무효화."),
            ("7", "하트비트 세션 만료 제어", r"\text{current\_time} \le \text{valid\_until}", "만료되거나 방치된 세션은 신규 자금 예약을 집행할 수 없음."),
            ("8", "단조 정산 및 단 1회 정산 보장", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "바우처 간 이중 지불 및 리플레이 공격 영구 배제."),
            ("9", "시빌 계정 격리성", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ 고유성 보장}', "단일 기능 리프는 단 하나의 온체인 계정에만 1:1 결합.")
        ]
    },
    'fr': {
        'sec_title': "4. RAPPORT D'AUDIT DES 9 INVARIANTS MATHÉMATIQUES ($I_1 \\dots I_9$)",
        'sec_intro': "Toutes les instructions on-chain de `programs/haichain-core/src/lib.rs` respectent scrupuleusement les 9 invariants mathématiques sans exception :",
        'items': [
            ("1", "Conservation du Capital", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{Dépôts Nets}", "Vérifié formellement par `test_invariant_i1_conservation` dans la suite de tests."),
            ("2", "Sécurité du Bénéficiaire Canonique", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "Appliqué on-chain via contrainte Anchor ; élimine tout détournement d'adresse."),
            ("3", "Plafond Budgétaire Inviolable", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "Contrôlé obligatoirement avant toute réservation ou règlement."),
            ("4", "Limiteur de Vélocité Autonome", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "Empêche la vidange rapide et automatisée des fonds."),
            ("5", "Rétrécissement Monotone des PDA", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "Les instances enfants ne peuvent jamais élargir les privilèges accordés par le parent."),
            ("6", "Époque de Panique & Gel Immédiat", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "L'arrêt d'urgence invalide instantanément tous les bons de paiement en circulation."),
            ("7", "Expiration du Battement de Cœur", r"\text{current\_time} \le \text{valid\_until}", "Les sessions expirées ou abandonnées ne peuvent exécuter de nouvelles réservations."),
            ("8", "Règlement Monotone & Unique", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "Garantit l'absence totale de double dépense entre bons de paiement."),
            ("9", "Isolation de Compte Anti-Sybil", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ est unique}', "Chaque feuille de capacité correspond exactement à un compte on-chain unique.")
        ]
    },
    'es': {
        'sec_title': '4. INFORME DE AUDITORÍA DE LOS 9 INVARIANTES MATEMÁTICOS ($I_1 \\dots I_9$)',
        'sec_intro': 'Todas las instrucciones on-chain en `programs/haichain-core/src/lib.rs` satisfacen los 9 invariantes matemáticos sin excepción:',
        'items': [
            ("1", "Conservación de Capital", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{Depósitos Netos}", "Verificado formalmente mediante `test_invariant_i1_conservation` en la suite de pruebas."),
            ("2", "Seguridad de Destinatario Canónico", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "Ejecutado on-chain mediante restricciones Anchor; previene desvíos de tokens a terceros."),
            ("3", "Tope Presupuestario Inviolable", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "Verificado antes de cada reserva o liquidación on-chain."),
            ("4", "Limitador de Velocidad Autónomo", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "Previene el vaciado rápido y automatizado del capital."),
            ("5", "Estrechamiento Monótono de PDA", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "Las instancias hijas jamás pueden expandir los permisos otorgados por la entidad padre."),
            ("6", "Época de Pánico y Congelación Inmediata", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "La parada de emergencia invalida inmediatamente todos los vales en circulación."),
            ("7", "Expiración del Latido de Sesión", r"\text{current\_time} \le \text{valid\_until}", "Las sesiones caducadas o abandonadas no pueden ejecutar nuevas reservas de fondos."),
            ("8", "Liquidación Monótona y Única", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "Garantiza cero doble gasto entre vales del canal."),
            ("9", "Aislamiento de Cuentas Anti-Sybil", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ es único}', "Una hoja de capacidad se asigna exactamente a una única cuenta on-chain.")
        ]
    },
    'ru': {
        'sec_title': '4. ОТЧЕТ ОБ АУДИТЕ 9 МАТЕМАТИЧЕСКИХ ИНВАРИАНТОВ ($I_1 \\dots I_9$)',
        'sec_intro': 'Все ончейн-инструкции в `programs/haichain-core/src/lib.rs` строго соблюдают 9 математических инвариантов состояния без исключений:',
        'items': [
            ("1", "Сохранение Капитала", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{Чистые Депозиты}", "Верифицировано тестом `test_invariant_i1_conservation` в тестовом наборе."),
            ("2", "Безопасность Канонического Получателя", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "Принудительно исполняется ончейн через Anchor; исключает подмену адреса третьими лицами."),
            ("3", "Неприкосновенный Бюджетный Лимит", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "Проверяется перед каждой операцией резервирования или расчета."),
            ("4", "Автономный Ограничитель Скорости", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "Предотвращает быстрое автоматизированное исчерпание капитала."),
            ("5", "Монотонное Сужение Полномочий PDA", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "Дочерние инстансы не могут расширять права, предоставленные родителем."),
            ("6", "Паническая Эпоха и Мгновенная Заморозка", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "Экстренная заморозка мгновенно аннулирует все незавершенные ваучеры."),
            ("7", "Истечение Сессионного Тайм-аута", r"\text{current\_time} \le \text{valid\_until}", "Истекшие или брошенные сессии не могут инициировать новые резервы."),
            ("8", "Монотонный Однократный Расчет", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "Гарантирует абсолютное отсутствие двойного расходования средств."),
            ("9", "Изоляция Счетов от Атак Сивиллы", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ уникален}', "Один лист полномочий сопоставляется ровно с одним ончейн-аккаунтом.")
        ]
    },
    'kk': {
        'sec_title': '4. 9 МАТЕМАТИКАЛЫҚ ИНВАРИАНТТЫҢ АУДИТ ЕСЕБІ ($I_1 \\dots I_9$)',
        'sec_intro': '`programs/haichain-core/src/lib.rs` ішіндегі барлық ончейн нұсқаулар келесі 9 күй инвариантын бұлжытпай сақтайды:',
        'items': [
            ("1", "Капиталдың Сақталу Заңы", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{Таза Салымдар}", "Сынақ жинағында `test_invariant_i1_conservation` арқылы толық тексерілген."),
            ("2", "Каноникалық Алушының Қауіпсіздігі", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "Anchor шектеуі арқылы мәжбүрленеді; бөтен шотқа бағыттауды болдырмайды."),
            ("3", "Бұзылмайтын Бюджет Шектігі", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "Әрбір резервтеу немесе есеп айырысу алдында міндетті түрде тексеріледі."),
            ("4", "Автономды Жылдамдық Шектегіші", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "Қаражаттың жылдам автоматты түрде ағып кетуіне тосқауыл қояды."),
            ("5", "PDA Құқықтарын Біркелкі Тарылту", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "Туынды нысандар негізгі нысан берген өкілеттіктерді кеңейте алмайды."),
            ("6", "Үрей Дәуірі және Жедел Тоқтату", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "Жүйені шұғыл тоқтату барлық өңделмеген ваучерлерді бірден жояды."),
            ("7", "Сессиялық Уақыттың Аяқталуы", r"\text{current\_time} \le \text{valid\_until}", "Мерзімі өткен сессиялар жаңа қаражат резервтерін орындай алмайды."),
            ("8", "Біркелкі және Біржолғы Есеп айырысу", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "Ваучерлер арасында қайталанатын жұмсаудың болмауына кепілдік береді."),
            ("9", "Сибилла Шабуылынан Оқшаулау", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ бірегей}', "Бір мүмкіндік жапырағы тек бір ончейн шотына 1:1 сәйкес келеді.")
        ]
    },
    'hi': {
        'sec_title': '4. 9 गणितीय अपरिवर्तनीयता ऑन-चेन ऑडिट रिपोर्ट ($I_1 \\dots I_9$)',
        'sec_intro': '`programs/haichain-core/src/lib.rs` में प्रत्येक ऑन-चेन निर्देश बिना किसी अपवाद के सभी 9 स्थिति अपरिवर्तनीयों को सुरक्षित रखता है:',
        'items': [
            ("1", "पूंजी संरक्षण सिद्धांत", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{शुद्ध जमा}", "परीक्षण सूट में `test_invariant_i1_conservation` द्वारा सत्यापित।"),
            ("2", "विहित प्राप्तकर्ता सुरक्षा", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "Anchor बाधा के माध्यम से ऑन-चेन लागू; टोकन खाते के अनधिकृत पुनर्निर्देशन को रोकता है।"),
            ("3", "अपरिवर्तनीय बजट सीमा", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "प्रत्येक रिजर्व या निपटान निष्पादन से पहले अनिवार्य रूप से जांचा गया।"),
            ("4", "स्वायत्त वेग दर सीमक", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "तीव्र स्वचालित पूंजी निकासी को रोकता है।"),
            ("5", "एकदिष्ट PDA संकीर्णन", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "उप-उदाहरण कभी भी मूल द्वारा दी गई अनुमतियों को विस्तृत नहीं कर सकते।"),
            ("6", "पैनिक युग और तत्काल फ्रीज अलगाव", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "तत्काल प्रोटोकॉल फ्रीज सभी संचलन में मौजूद वाउचर को तुरंत रद्द कर देता है।"),
            ("7", "सत्र समाप्ति नियंत्रण", r"\text{current\_time} \le \text{valid\_until}", "समाप्त या परित्यक्त सत्र नए रिजर्व निष्पादित नहीं कर सकते।"),
            ("8", "एकदिष्ट निपटान और एक बार का दावा", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "वाउचर में डबल-स्पेंडिंग और रीप्ले हमलों को पूरी तरह समाप्त करता है।"),
            ("9", "सिबिल खाता अलगाव", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ अद्वितीय है}', "एक क्षमता लीफ ठीक एक ऑन-चेन खाते से विशिष्ट रूप से मैप होती है।")
        ]
    },
    'he': {
        'sec_title': '4. דוח ביקורת 9 אינווריאנטים מתמטיים ($I_1 \\dots I_9$)',
        'sec_intro': 'כל ההוראות ב-`programs/haichain-core/src/lib.rs` שומרות על 9 אינווריאנטי המצב ללא יוצא מן הכלל:',
        'items': [
            ("1", "שימור הון מוחלט", r"\text{Vault}_{\text{ATA}} + \sum_{\text{channels}} \text{Escrow}_j + \sum \text{Paid}_j + \text{Refunds} = \text{סך הפקדות נטו}", "מאומת רשמית על ידי `test_invariant_i1_conservation` במערך הבדיקות."),
            ("2", "בטיחות מוטב קנוני", r"\text{payee\_ata} \equiv \text{get\_associated\_token\_address}(\text{merchant}, \text{mint})", "נאכף בשרשרת דרך אילוץ Anchor; מונע ניתוב מחדש של חשבונות טוקן."),
            ("3", "תקרת תקציב בלתי ניתנת לפריצה", r"\text{consumed} \le \text{max\_spend} \quad \land \quad \text{budget\_used} \le \text{budget\_total}", "נבדק לפני כל ביצוע הקצאה או סילוקין בשרשרת."),
            ("4", "מגביל מהירות זרימה אוטונומי", r"\text{window\_used} \le \text{window\_cap} \quad \forall t \in [T_0, T_0 + \omega]", "מונע ריקון הון מהיר ואוטומטי."),
            ("5", "הצרת הרשאות מונוטונית של PDA", r"\text{Channel PDA} \subseteq \text{Grant PDA} \subseteq \text{Pot PDA}", "מופעי צאצא אינם יכולים להרחיב הרשאות שניתנו על ידי ההורה."),
            ("6", "בידוד תקופת פאניקה והקפאה מיידית", r"\text{pot.panic\_epoch} == \text{channel.created\_at\_epoch} \quad \land \quad \neg\text{pot.frozen}", "הקפאת חירום מבטלת באופן מיידי את כל השוברים שטרם סולקו."),
            ("7", "פקיעת תוקף סשן", r"\text{current\_time} \le \text{valid\_until}", "סשנים שפג תוקפם אינם יכולים לבצע הקצאות חדשות של הון."),
            ("8", "סילוקין מונוטוני וחד-פעמי", r"\text{paid}_{\text{new}} \le \min(\text{cumulative\_amount}, \text{reserved\_amount}) \quad \land \quad \text{paid}_{\text{new}} \ge \text{paid}_{\text{old}}", "מבטיח אפס הוצאה כפולה בין שוברים ומונע מתקפות שידור חוזר."),
            ("9", "בידוד חשבונות נגד התקפת סיביל", r'\text{PDA}(\text{"chan"}, \text{grant}, \text{channel\_id}) \text{ ייחודי}', "עלה יכולת ממופה בדיוק לחשבון בשרשרת יחיד.")
        ]
    }
}

def get_logo_base64():
    if os.path.exists(LOGO_PATH):
        with open(LOGO_PATH, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

import base64

def latex_to_html(tex):
    s = tex
    text_placeholders = []
    def save_text(m):
        raw = m.group(1).replace(r'\_', '_').replace('\\', '')
        idx = len(text_placeholders)
        if '_' in raw or '.' in raw or '(' in raw or raw.startswith('PDA'):
            text_placeholders.append(f'<code class="math-code">{raw}</code>')
        else:
            text_placeholders.append(f'<span class="math-text">{raw}</span>')
        return f'@@@TEXTPH{idx}@@@'

    # Pre-clean macros with braces before subscript regex
    s = re.sub(r'\\mathbf\{([^}]+)\}', save_text, s)
    s = re.sub(r'\\textbf\{([^}]+)\}', save_text, s)
    s = re.sub(r'\\text\{([^}]+)\}', save_text, s)
    s = re.sub(r'\\mathcal\{A\}', r'<i>A</i>', s)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1 &frasl; \2)', s)

    # Subscripts and superscripts (applied strictly to mathematical variables)
    s = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', s)
    s = re.sub(r'_([a-zA-Z0-9])', r'<sub>\1</sub>', s)
    s = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', s)
    s = re.sub(r'\^([a-zA-Z0-9])', r'<sup>\1</sup>', s)

    # Delimiters and operators
    s = re.sub(r'\\lceil', r'&lceil;', s)
    s = re.sub(r'\\rceil', r'&rceil;', s)
    s = re.sub(r'\\min', r'<span class="math-op">min</span>', s)
    s = re.sub(r'\\left\(', r'(', s)
    s = re.sub(r'\\right\)', r')', s)
    s = re.sub(r'\\land', r'&and;', s)
    s = re.sub(r'\\neg', r'&not;', s)
    s = re.sub(r'\\subseteq', r'&sube;', s)

    symbols = {
        r'\times': '&times;', r'\iff': '&hArr;', r'\implies': '&rArr;', r'\to': '&rarr;',
        r'\leftarrow': '&larr;', r'\forall': '&forall;', r'\exists': '&exist;', r'\ge': '&ge;',
        r'\le': '&le;', r'\ne': '&ne;', r'\approx': '&asymp;', r'\equiv': '&equiv;',
        r'\pm': '&plusmn;', r'\in': '&isin;', r'\cdot': '&middot;', r'\sum': '&sum;',
        r'\prod': '&prod;', r'\Delta': '&Delta;', r'\alpha': '&alpha;', r'\beta': '&beta;',
        r'\gamma': '&gamma;', r'\tau': '&tau;', r'\pi': '&pi;', r'\mu': '&mu;',
        r'\sigma': '&sigma;', r'\epsilon': '&epsilon;', r'\theta': '&theta;', r'\lambda': '&lambda;',
        r'\omega': '&omega;', r'\Omega': '&Omega;', r'\,': ' ', r'\quad': ' &emsp; ', r'\qquad': ' &emsp;&emsp; ',
        r'\dots': '&hellip;', r'\\': '<br>', r'\;': ' &ensp; '
    }
    for macro, rep in symbols.items():
        s = s.replace(macro, rep)

    s = re.sub(r'\b([tij])\b', r'<i>\1</i>', s)

    for idx, ph in enumerate(text_placeholders):
        s = s.replace(f'@@@TEXTPH{idx}@@@', ph)

    return s

def format_math(text):
    math_blocks = []
    def save_block(m):
        math_blocks.append(m.group(1))
        return f"@@@MATHBLOCK{len(math_blocks)-1}@@@"
    text = re.sub(r'\$\$(.*?)\$\$', save_block, text, flags=re.DOTALL)
    
    math_inlines = []
    def save_inline(m):
        math_inlines.append(m.group(1))
        return f"@@@MATHINLINE{len(math_inlines)-1}@@@"
    text = re.sub(r'\$([^\$\n]+?)\$', save_inline, text)
    
    for idx, block in enumerate(math_blocks):
        clean_html = latex_to_html(block.strip())
        text = text.replace(f"@@@MATHBLOCK{idx}@@@", f'<div class="math-display">{clean_html}</div>')
        
    for idx, inline in enumerate(math_inlines):
        clean_html = latex_to_html(inline.strip())
        text = text.replace(f"@@@MATHINLINE{idx}@@@", f'<span class="math-inline">{clean_html}</span>')
        
    return text

def build_invariants_html(lang_code):
    inv_data = INVARIANTS_DATA.get(lang_code, INVARIANTS_DATA['en'])
    cards = []
    for num, name, formula, note in inv_data['items']:
        clean_formula = latex_to_html(formula)
        card = f"""
<div class="invariant-card">
  <div class="invariant-header">
    <span class="inv-num">{num}.</span>
    <span class="inv-title"><strong><i>I</i><sub>{num}</sub> ({name}):</strong></span>
  </div>
  <div class="math-display">{clean_formula}</div>
  <div class="invariant-note">{note}</div>
</div>"""
        cards.append(card)
    return f"""
<div class="invariants-container">
{''.join(cards)}
</div>
"""

def generate_updated_markdown(lang_code, original_md):
    inv_data = INVARIANTS_DATA.get(lang_code, INVARIANTS_DATA['en'])
    
    # Build clean markdown list for the .md file
    md_items = []
    for num, name, formula, note in inv_data['items']:
        # Ensure clean code ticks in markdown
        item_str = f"{num}. **$I_{num}$ ({name}):**\n   $${formula}$$\n   {note}"
        md_items.append(item_str)
    
    invariants_md_block = f"## {inv_data['sec_title']}\n\n{inv_data['sec_intro']}\n\n" + "\n\n".join(md_items) + "\n\n---"
    
    # Replace Section 4 in original_md
    pattern = re.compile(r'## 4\..*?(?=## 5\.|\Z)', re.DOTALL)
    if pattern.search(original_md):
        updated_md = pattern.sub(lambda _: invariants_md_block + "\n\n", original_md)
    else:
        # Fallback append if not matched
        updated_md = original_md + "\n\n" + invariants_md_block
        
    return updated_md

def compile_risk_report(lang_code, info):
    md_filename = f"HAICHAIN_RISK_REPORT_{lang_code.upper()}.md"
    pdf_filename = f"HAICHAIN_RISK_REPORT_{lang_code.upper()}.pdf"
    html_temp = f"HAICHAIN_RISK_REPORT_{lang_code.upper()}_temp.html"
    
    md_path = os.path.join(WORKSPACE_DIR, md_filename)
    pdf_path = os.path.join(WORKSPACE_DIR, pdf_filename)
    html_path = os.path.join(WORKSPACE_DIR, html_temp)
    
    # 1. Generate updated Markdown
    updated_md = generate_updated_markdown(lang_code, info['md'])
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(updated_md)
    print(f"[+] Wrote updated markdown: {md_filename}")
    
    # 2. Process text & math for body
    text_with_math = format_math(updated_md)
    md_converter = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list'])
    body_html = md_converter.convert(text_with_math)
    
    # 3. Replace Section 4 in body_html with the guaranteed non-glitching invariant cards
    invariants_html = build_invariants_html(lang_code)
    pattern_sec4_html = re.compile(
        r'(<h2[^>]*>.*?4\..*?</h2>\s*<p>.*?</p>).*?(?=<h2[^>]*>.*?5\.|\Z)',
        re.DOTALL
    )
    if pattern_sec4_html.search(body_html):
        body_html = pattern_sec4_html.sub(lambda m: m.group(1) + invariants_html + '<hr />\n', body_html)
    
    # 4. Tag Section 3 hardening table with class
    pattern_hardening = re.compile(r"(<table>\s*<thead>\s*<tr>\s*<th[^>]*>\s*(?:#|STT|序号|№|क्र|מס))")
    body_html = pattern_hardening.sub(r'<table class="hardening-matrix-table">\n<thead>\n<tr>\n<th style="text-align: center;">', body_html, count=1)
    
    logo_uri = get_logo_base64()
    is_rtl = (lang_code == 'he')
    direction = "rtl" if is_rtl else "ltr"
    
    full_html = f"""<!DOCTYPE html>
<html lang="{lang_code}" dir="{direction}">
<head>
<meta charset="utf-8">
<title>{info['title']}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

@page {{
  size: A4;
  margin: 22mm 18mm 22mm 18mm;
  @top-left {{
    content: "{info['title']}";
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 7pt;
    font-weight: 600;
    letter-spacing: 0.8px;
    color: #71717a;
    text-transform: uppercase;
  }}
  @top-right {{
    content: "haichain.si";
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    font-weight: 500;
    color: #71717a;
  }}
  @bottom-left {{
    content: "{info['footer']}";
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 6.5pt;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: #a1a1aa;
    text-transform: uppercase;
  }}
  @bottom-right {{
    content: "Page " counter(page);
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    font-weight: 600;
    color: #18181b;
  }}
}}

@page :first {{
  margin: 0;
  @top-left {{ content: none; }}
  @top-right {{ content: none; }}
  @bottom-left {{ content: none; }}
  @bottom-right {{ content: none; }}
}}

body {{
  margin: 0;
  padding: 0;
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  color: #18181b;
  background: #ffffff;
  font-size: 9pt;
  line-height: 1.6;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}}

/* Premium Cover Page */
.cover-page {{
  page-break-after: always;
  height: 100vh;
  box-sizing: border-box;
  background: #09090b;
  color: #ffffff;
  padding: 38mm 24mm 28mm 24mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

.cover-header {{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 20mm;
}}

.cover-brand-block {{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 14px;
}}

.cover-logo {{
  height: 36px;
  width: auto;
  display: block;
}}

.cover-tag {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 7.5pt;
  font-weight: 600;
  letter-spacing: 1.2px;
  color: #a1a1aa;
  text-transform: uppercase;
}}

.cover-hero {{
  margin-bottom: auto;
}}

.cover-badge {{
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 8pt;
  font-weight: 600;
  color: #a1a1aa;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 4px;
  padding: 5px 12px;
  margin-bottom: 18px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}

.cover-title {{
  font-size: 26pt;
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.8px;
  color: #ffffff;
  margin-bottom: 14px;
}}

.cover-subtitle {{
  font-size: 11pt;
  font-weight: 400;
  line-height: 1.5;
  color: #a1a1aa;
  max-width: 620px;
}}

.cover-footer {{
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  padding-top: 18px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}}

.cover-meta-col {{
  display: flex;
  flex-direction: column;
  gap: 4px;
}}

.cover-meta-lbl {{
  font-size: 7pt;
  font-weight: 600;
  letter-spacing: 0.8px;
  color: #71717a;
  text-transform: uppercase;
}}

.cover-meta-val {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8pt;
  font-weight: 500;
  color: #ffffff;
}}

/* Body Content */
.body-container {{
  padding-top: 8mm;
}}

h1, h2, h3, h4 {{
  color: #09090b;
  font-weight: 700;
  letter-spacing: -0.3px;
}}

h1 {{
  font-size: 18pt;
  margin-top: 0;
  margin-bottom: 12px;
  border-bottom: 1.5px solid #18181b;
  padding-bottom: 6px;
}}

h2 {{
  font-size: 13pt;
  margin-top: 22px;
  margin-bottom: 10px;
  border-bottom: 1px solid #e4e4e7;
  padding-bottom: 4px;
  page-break-after: avoid;
}}

h3 {{
  font-size: 10.5pt;
  margin-top: 16px;
  margin-bottom: 6px;
  page-break-after: avoid;
}}

p {{
  margin: 0 0 10px 0;
  text-align: justify;
}}

table {{
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  font-size: 8pt;
  page-break-inside: avoid;
}}

th, td {{
  padding: 6px 10px;
  border: 1px solid #e4e4e7;
  text-align: left;
  vertical-align: top;
}}

th {{
  background: #f4f4f5;
  color: #18181b;
  font-weight: 600;
}}

.hardening-matrix-table th:first-child,
.hardening-matrix-table td:first-child {{
  width: 32px;
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 600;
}}

code {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8pt;
  background: #f4f4f5;
  padding: 2px 4px;
  border-radius: 3px;
  color: #09090b;
}}

pre {{
  background: #f4f4f5;
  padding: 10px 14px;
  border-radius: 6px;
  overflow-x: auto;
  font-family: 'JetBrains Mono', monospace;
  font-size: 7.5pt;
  line-height: 1.45;
  margin: 12px 0;
  color: #09090b;
}}

pre code {{
  background: transparent;
  color: inherit;
  padding: 0;
}}

/* Mathematical Formulas & Invariants Cards */
.math-display {{
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 5px;
  padding: 9px 14px !important;
  margin: 7px 0 !important;
  text-align: center;
  font-family: 'Cambria Math', 'Times New Roman', Times, serif;
  font-size: 10pt;
  color: #000000;
  page-break-inside: avoid;
  break-inside: avoid;
}}

.math-code {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8pt;
  font-style: normal;
  color: #09090b;
  background: #f1f5f9;
  padding: 1px 5px;
  border-radius: 3px;
  border: 1px solid #cbd5e1;
}}

.math-text {{
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  font-style: normal;
  font-size: 8.5pt;
  color: #1e293b;
}}

.math-op {{
  font-family: 'Cambria Math', 'Times New Roman', serif;
  font-style: normal;
  font-size: 9.5pt;
}}

.math-inline {{
  font-family: 'Cambria Math', 'Times New Roman', Times, serif;
  font-size: 9pt;
  color: #000000;
  background: transparent;
  padding: 0;
}}

.invariants-container {{
  margin: 14px 0 20px 0;
}}

.invariant-card {{
  margin: 8px 0 12px 0;
  padding: 9px 13px;
  background: #fafafa;
  border: 1px solid #e4e4e7;
  border-radius: 6px;
  page-break-inside: avoid;
  break-inside: avoid;
}}

.invariant-header {{
  font-size: 8.5pt;
  font-weight: 700;
  color: #09090b;
  margin-bottom: 5px;
  display: flex;
  align-items: baseline;
  gap: 5px;
}}

.inv-num {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 8.5pt;
  font-weight: 700;
  color: #18181b;
  margin-right: 4px;
}}

.inv-title {{
  color: #18181b;
}}

.inv-title i {{
  font-family: 'Cambria Math', 'Times New Roman', serif;
  font-style: italic;
  font-size: 9.5pt;
}}

.invariant-note {{
  font-size: 7.5pt;
  color: #71717a;
  margin-top: 4px;
  line-height: 1.4;
  font-style: italic;
}}

.invariant-note code {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 7.5pt;
  background: #f4f4f5;
  padding: 1px 4px;
  border-radius: 3px;
  color: #09090b;
  font-style: normal;
}}

hr {{
  border: 0;
  height: 1px;
  background: #e4e4e7;
  margin: 18px 0;
}}

ul, ol {{
  margin: 0 0 10px 0;
  padding-left: 20px;
}}

li {{
  margin-bottom: 4px;
}}

html[dir="rtl"] {{
  font-family: 'Plus Jakarta Sans', 'Arial', sans-serif;
}}
html[dir="rtl"] th, html[dir="rtl"] td {{
  text-align: right;
}}
html[dir="rtl"] .math-display {{
  direction: ltr !important;
  unicode-bidi: embed;
}}
</style>
</head>
<body>

<!-- Cover Page -->
<div class="cover-page">
  <div class="cover-header">
    <div class="cover-brand-block">
      <img src="{logo_uri}" class="cover-logo" alt="HAICHAIN" />
      <div class="cover-tag">{info['tag']}</div>
    </div>
  </div>
  
  <div class="cover-hero">
    <div class="cover-badge">{info['edition']}</div>
    <div class="cover-title">{info['title']}</div>
    <div class="cover-subtitle">{info['subtitle']}</div>
  </div>
  
  <div class="cover-footer">
    <div class="cover-meta-col">
      <span class="cover-meta-lbl">{info['meta_audience_lbl']}</span>
      <span class="cover-meta-val">{info['meta_audience_val']}</span>
    </div>
    <div class="cover-meta-col">
      <span class="cover-meta-lbl">{info['meta_sec_lbl']}</span>
      <span class="cover-meta-val">{info['meta_sec_val']}</span>
    </div>
    <div class="cover-meta-col">
      <span class="cover-meta-lbl">{info['meta_kern_lbl']}</span>
      <span class="cover-meta-val">{info['meta_kern_val']}</span>
    </div>
  </div>
</div>

<!-- Body Document -->
<div class="body-container">
{body_html}
</div>

</body>
</html>
"""
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if os.path.exists(html_path):
        os.remove(html_path)
        
    if os.path.exists(pdf_path):
        size = os.path.getsize(pdf_path)
        print(f"[✓] Compiled {pdf_filename}: {size:,} bytes")
        app_pdf = os.path.join(WORKSPACE_DIR, "app", pdf_filename)
        shutil.copy2(pdf_path, app_pdf)
        print(f"[✓] Mirrored to app/{pdf_filename}")
        return True
    else:
        print(f"[✗] Failed to compile {pdf_filename}")
        return False

if __name__ == "__main__":
    # Import DOCS from build_all_risk_reports
    sys.path.append(os.path.join(WORKSPACE_DIR, "scripts"))
    import build_all_risk_reports
    
    langs = ['en', 'vi', 'zh', 'ko', 'fr', 'es', 'ru', 'kk', 'hi', 'he']
    success = []
    print(f"[*] Recompiling all 10 Risk Reports with institutional invariants formatting...")
    for l in langs:
        data = build_all_risk_reports.DOCS[l]
        if compile_risk_report(l, data):
            success.append(l)
    print(f"\n[*] ALL DONE: {len(success)}/10 PDFs generated and deployed successfully!")
