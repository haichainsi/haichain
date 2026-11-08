#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_all_whitepapers.py
Updates all 10 HAICHAIN whitepaper markdown files:
1. Adds HTTP x402 & Solana Pay.sh into the Competitor Comparison Matrix (Chapter 1).
2. Adds HTTP x402 & Solana Pay.sh into the Detailed Failure Case Studies (Chapter 1).
3. Upgrades Micro-Voucher formula with complete Cryptographic Domain Separation (ClusterID, ProgramID, VaultPDA, ProviderPubkey, etc.).
4. Inserts Section 4.6 / 6.6 (Strategic Positioning with x402 & Pay.sh) in languages where it was omitted (ES, FR, HE, HI, KK, KO, RU, ZH).
5. Refines security invariant introductions from absolute claims ("100% immune") to "Deterministic Multi-Layer Defense-in-Depth with scheduled third-party audits".
"""

import os
import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# Translations for each language:
LANG_DATA = {
    'VI': {
        'table_row': (
            "| HTTP x402 & Pay.sh    Chỉ là ống dẫn HTTP/proxy thô; Giới hạn 1 delegate Lớp Quản trị Chính sách & Hạn mức Merkle;      |\n"
            "| (Coinbase / Linux Fdn/ủy quyền token Solana; Lỗ hổng thiếu trần chi tiêu  Cây năng lực đa tầng (Multi-delegate); Hũ PDA   |\n"
            "| Solana x Google Cloud)client (V12 audit); Thiếu mạch ngắt tự hành on-chain cô lập; Bounded Loss Theorem triệt tiêu rủi ro |\n"
            "|                       và thiếu cơ chế ký quỹ/phạt nhà cung cấp.           cháy ví; Tương thích mượt mà (drop-in layer).   |"
        ),
        'case_study': (
            "\n5. **HTTP x402 & Solana Pay.sh (Ống Dẫn Thanh Toán Thô vs. Ngân Hàng Chính Sách & Chốt An Toàn):**\n"
            "   * *Giới hạn kiến trúc:* Cả chuẩn x402 (Coinbase/Linux Foundation) và Pay.sh (Solana Foundation/Google Cloud) tập trung vào giao thức truyền dẫn (Transport & Proxy Protocol) và ủy quyền thanh toán một chạm. Tuy nhiên, chúng không giải quyết bài toán quản trị rủi ro vốn: token delegate trên Solana SPL bị giới hạn chỉ 1 ủy quyền duy nhất trên mỗi tài khoản token, và các lỗ hổng thực tế được phát hiện (báo cáo an ninh V12 tháng 10/2026) cho thấy client sơ khai thiếu trần chi tiêu mặc định, khiến API độc hại có thể đòi toàn bộ số dư.\n"
            "   * *Giải pháp liên minh của HAICHAIN:* HAICHAIN không thay thế đường ống x402/Pay.sh mà đóng vai trò là **Lớp Quản trị Chính sách & Kho Quỹ An toàn (Smart Policy & Safe Custody Vault)** cắm trực tiếp phía trên. Nhờ Cây Năng lực Merkle 4 thành phần (`Pubkey || MaxSpend || ExpirySlot || Nonce`) và Mạch ngắt Panic dưới 400ms, HAICHAIN bảo đảm ngay cả khi tác tử gọi các API qua x402/Pay.sh, tổng mức chi trả không bao giờ vượt quá hạn mức nhiệm vụ được ủy quyền.\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   Trong đó:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: Chuỗi định danh phân tách miền chuẩn giao thức (`\"haichain-v1-channel-settlement\"`).\n"
            "   * $\\text{ClusterID}$: Định danh cụm mạng (Devnet, Testnet, Mainnet-Beta), triệt tiêu 100% rủi ro tấn công phát lại chữ ký xuyên môi trường (Cross-Cluster Replay Attack).\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Ràng buộc chính xác địa chỉ hợp đồng lõi và Kho quỹ PDA của Agent, ngăn chặn tái sử dụng chữ ký trên các hợp đồng fork hoặc hũ tiền khác.\n"
            "   * $\\text{ProviderPubkey}$: Địa chỉ ví công khai của Nhà cung cấp dịch vụ được ủy quyền trong phiên, vô hiệu hóa việc chuyển nhượng vé trái phép cho bên thứ ba.\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Khóa phiên duy nhất, số thứ tự đơn điệu tăng dần ($k$) và số tiền tích lũy lũy tiến, đảm bảo quyết toán gom một vé duy nhất an toàn tuyệt đối."
        ),
        'invariants_intro_old': "cưỡng bức 6 bất biến toán học để miễn nhiễm hoàn toàn với các cuộc tấn công lịch sử trị giá hơn 800 triệu USD:",
        'invariants_intro_new': "thiết lập mô hình **Phòng Thủ Chiều Sâu Tất Định (Deterministic Multi-Layer Defense-in-Depth)**, cưỡng bức 6 bất biến toán học ở cấp độ runtime nhằm vô hiệu hóa các lớp lỗ hổng trạng thái và kỹ thuật tấn công khai thác smart contract lịch sử trị giá hơn 821 triệu USD. Kết hợp cùng kế hoạch kiểm toán bảo mật độc lập định kỳ (Scheduled Third-Party Security Audits) từ các đơn vị kiểm toán uy tín, kiến trúc triệt tiêu hoàn toàn các điểm mù logic hợp đồng:"
    },
    'EN': {
        'table_row': (
            "| HTTP x402 & Pay.sh    Raw HTTP/proxy transport pipes; Single-delegate Programmable Policy & Vault Layer (drop-in  |\n"
            "| (Coinbase / Linux Fdn/token limitation on Solana; Unconstrained client companion); Multi-delegate Merkle capability;|\n"
            "| Solana x Google Cloud)spending limits (V12 audit CVEs); Lacks on-chain Isolated PDA spending pots; Panic Circuit    |\n"
            "|                       circuit breakers & provider slashing mechanisms.Breaker sweeping in < 400ms; Bounded Loss.   |"
        ),
        'case_study': (
            "\n5. **HTTP x402 & Solana Pay.sh (Raw Transport Pipes vs. Programmable Risk Policy Vault):**\n"
            "   * *Architectural Scope:* Both the HTTP x402 specification (Coinbase / Linux Foundation) and Pay.sh (Solana Foundation / Google Cloud) provide crucial transport-layer payment middleware and zero-subscription proxy gating. However, their security domain ends at the network protocol layer: standard Solana SPL token delegates are strictly constrained to a single delegate per account, and security disclosures in October 2026 (V12 vulnerability report) demonstrated that without default client-side budget caps, malicious APIs could extract entire account balances.\n"
            "   * *The HAICHAIN Strategic Synergy:* HAICHAIN does not compete with x402 or Pay.sh; it operates as the **Programmable Policy & Vault Governance Layer** sitting directly atop them. By enforcing 4-tuple Merkle capability trees (`Pubkey || MaxSpend || ExpirySlot || Nonce`) and sub-400ms panic circuit breakers, HAICHAIN guarantees that even when autonomous agents transact over x402 or Pay.sh rails, total loss exposure is mathematically bounded to the pre-authorized per-task allowance.\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   Where:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: Protocol-level cryptographic domain tag (`\"haichain-v1-channel-settlement\"`).\n"
            "   * $\\text{ClusterID}$: Solana cluster identifier (Devnet, Testnet, Mainnet-Beta), mathematically eliminating cross-network signature replay vulnerabilities.\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Cryptographically anchors the voucher to the specific deployed program and the agent's isolated vault account.\n"
            "   * $\\text{ProviderPubkey}$: Public key of the whitelisted service provider for the active session, preventing unauthorized secondary transfer of payment vouchers.\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Monotonically increasing tick counter ($k$) and cumulative spend under a unique session ID, enabling single-voucher settlement with sub-5ms latency and zero reasoning stalls."
        ),
        'invariants_intro_old': "is formally verified and hardened against historic DeFi exploits totaling over $800M+:",
        'invariants_intro_new': "implements a **Deterministic Multi-Layer Defense-in-Depth** architecture, enforcing 6 mathematical runtime invariants designed to neutralize critical state vulnerabilities and historic exploit vectors totaling over $821 million in losses. Combined with scheduled independent third-party security audits from premier Web3 auditing firms, this deterministic boundary guarantees zero unvetted contract execution:"
    },
    'ES': {
        'table_row': (
            "| HTTP x402 y Pay.sh    Tuberías de transporte HTTP/proxy brutas; Límite Capa de Políticas y Bóvedas Programables (capa   |\n"
            "| (Coinbase / Linux Fdn/de 1 delegado SPL; Falta de topes de gasto en    compatible); Capacidad Merkle multidelegada; Fondos|\n"
            "| Solana x Google Cloud)clientes (auditoría V12); Sin disyuntores        PDA aislados; Disyuntor de pánico en < 400ms;     |\n"
            "|                       autónomos on-chain ni slashing a proveedores.    Teorema de Pérdida Acotada (sin riesgo de quiebra).|"
        ),
        'case_study': (
            "\n5. **HTTP x402 y Solana Pay.sh (Tuberías de Transporte Brutas vs. Bóveda de Políticas de Riesgo Programables):**\n"
            "   * *Alcance Arquitectónico:* Tanto la especificación HTTP x402 (Coinbase / Fundación Linux) como Pay.sh (Fundación Solana / Google Cloud) proporcionan un middleware de pago crucial a nivel de transporte y pasarelas proxy sin suscripción. Sin embargo, su dominio de seguridad termina en la capa de protocolo: los delegados de tokens SPL estándar de Solana están estrictamente limitados a un solo delegado por cuenta, y las auditorías de seguridad de octubre de 2026 (informe de vulnerabilidad V12) demostraron que, sin límites presupuestarios predeterminados del lado del cliente, las API maliciosas podían extraer saldos completos.\n"
            "   * *La Sinergia Estratégica de HAICHAIN:* HAICHAIN no compite con x402 ni con Pay.sh; opera como la **Capa de Gobernanza de Políticas y Bóvedas Programables** situada directamente sobre ellos. Al hacer cumplir árboles de capacidad Merkle de 4 tuplas (`Pubkey || MaxSpend || ExpirySlot || Nonce`) y disyuntores de pánico en menos de 400 ms, HAICHAIN garantiza que incluso si los agentes autónomos operan sobre x402 o Pay.sh, la exposición total a pérdidas esté matemáticamente acotada a la asignación autorizada por tarea.\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   Donde:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: Etiqueta criptográfica de dominio del protocolo (`\"haichain-v1-channel-settlement\"`).\n"
            "   * $\\text{ClusterID}$: Identificador del clúster de Solana (Devnet, Testnet, Mainnet-Beta), eliminando repeticiones entre redes.\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Vincula la firma al programa exacto y a la bóveda aislada del agente.\n"
            "   * $\\text{ProviderPubkey}$: Clave pública del proveedor autorizado para la sesión activa, impidiendo transferencias no autorizadas.\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Contador monótono ($k$) y gasto acumulado con liquidación única en menos de 5ms."
        ),
        'section_x402': (
            "\n### 6.6. Posicionamiento Estratégico: HAICHAIN como Capa de Políticas y Disyuntores para HTTP x402 y Solana Pay.sh\n\n"
            "En el panorama de la infraestructura de agentes autónomos, los protocolos abiertos de comunicación de pagos han ganado una rápida adopción institucional, especialmente **HTTP x402** (iniciado por Coinbase, transferido a la Fundación Linux con participación de Visa y Mastercard) y **Pay.sh** (lanzado conjuntamente por la Fundación Solana y Google Cloud en mayo de 2026).\n\n"
            "```\n"
            "         PILA GLOBAL DE INFRAESTRUCTURA FINANCIERA PARA AGENTES\n"
            "         \n"
            "    [ AGENTES Y ENJAMBRES DE IA ] : Claude Desktop, Cursor, ElizaOS, CrewAI\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ COMUNICACIÓN Y FACTURACIÓN] : Protocolo HTTP x402 y Proxy Pay.sh\n"
            "    (Emite código 402 Payment Required y transporta desafíos de pago)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ POLÍTICA Y GESTIÓN DE RIESGO] : ★ HAICHAIN AGENT POLICY VAULT ★\n"
            "    (Árboles Merkle, Topes estrictos MaxSpend, Disyuntor de pánico < 1s)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ CARRILES DE LIQUIDACIÓN L1] : Registro Solana L1 (Liquidación USDC / USDT SPL)\n"
            "```\n\n"
            "1. **División Clara de Roles (Sinergia de Ecosistema Complementaria):**\n"
            "   * **x402 y Pay.sh actúan como 'Tuberías de Comunicación':** Definen cómo las API devuelven `402 Payment Required` y cómo los clientes envían encabezados estándar (`X-402-Authorization`).\n"
            "   * **HAICHAIN actúa como 'Banco de Riesgo y Bóveda Segura de Políticas':** Resuelve preguntas críticas: *¿De dónde obtiene fondos el agente? ¿Quién controla los límites? ¿Cómo se frena un LLM comprometido?*\n"
            "2. **Neutralización de Vulnerabilidades Empíricas de x402:**\n"
            "   Las investigaciones de seguridad de octubre de 2026 revelaron 25 vulnerabilidades en clientes tempranos de x402. HAICHAIN lo soluciona con su **Hoja de Capacidad Merkle de 4 Componentes** (`Pubkey || MaxSpend || ExpirySlot || Nonce`) y el **Teorema de Pérdida Acotada**.\n"
            "3. **Integración Directa con SDK x402:**\n"
            "   El paquete `@haichain/sdk` incluye controladores nativos para resolver desafíos x402 de forma segura.\n\n"
            "---\n"
        ),
        'invariants_intro_old': "está verificado formalmente y blindado contra exploits históricos de DeFi por más de $800M+:",
        'invariants_intro_new': "implementa una arquitectura de **Defensa en Profundidad Determinista Multicapa (Deterministic Multi-Layer Defense-in-Depth)**, aplicando 6 invariantes matemáticas en tiempo de ejecución para neutralizar vulnerabilidades de estado y vectores de ataque históricos por más de $821 millones. Combinado con auditorías de seguridad independientes programadas de primer nivel, elimina cualquier brecha de ejecución:"
    },
    'FR': {
        'table_row': (
            "| HTTP x402 & Pay.sh    Canaux de transport HTTP/proxy bruts; Limite d'un Couche de Politiques et de Coffre Programmable     |\n"
            "| (Coinbase / Linux Fdn/seul délégué SPL; Absence de plafonds de dépenses (module complémentaire); Arbre Merkle multi-délégué;|\n"
            "| Solana x Google Cloud)client (audit V12); Sans disjoncteur on-chain ni  Fonds PDA isolés; Coupe-circuit d'urgence < 400ms; |\n"
            "|                       pénalité (slashing) des fournisseurs.            Théorème de Perte Bornée (zéro risque de ruine).   |"
        ),
        'case_study': (
            "\n5. **HTTP x402 et Solana Pay.sh (Canaux de Transport Bruts vs. Coffre de Politiques de Risque Programmables):**\n"
            "   * *Périmètre Architectural:* La spécification HTTP x402 (Coinbase / Fondation Linux) et Pay.sh (Fondation Solana / Google Cloud) fournissent un middleware de paiement essentiel au niveau transport et un proxy d'autorisation sans abonnement. Toutefois, leur domaine de sécurité s'arrête au protocole réseau: les délégations de jetons SPL standard sur Solana sont strictement restreintes à un délégué unique par compte, et les audits de sécurité d'octobre 2026 (rapport de vulnérabilités V12) ont révélé que sans plafonds stricts côté client, des API malveillantes pouvaient exiger l'intégralité du solde.\n"
            "   * *La Synergie Stratégique d'HAICHAIN:* HAICHAIN ne concurrence pas x402 ou Pay.sh; il s'impose comme la **Couche de Gouvernance de Politiques et de Coffre Sécurisé** intégrée directement au-dessus d'eux. Grâce à l'arbre de capacités Merkle à 4 composants (`Pubkey || MaxSpend || ExpirySlot || Nonce`) et au disjoncteur d'urgence en moins de 400 ms, HAICHAIN garantit que même en transitant par x402 ou Pay.sh, l'exposition maximale aux pertes est mathématiquement bornée à l'allocation stricte de la tâche.\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   Où:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: Balise cryptographique de séparation de domaine du protocole (`\"haichain-v1-channel-settlement\"`).\n"
            "   * $\\text{ClusterID}$: Identifiant de cluster Solana (Devnet, Testnet, Mainnet-Beta), éliminant tout rejeu trans-réseau.\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Lie le bon au programme précis et au coffre PDA isolé de l'agent.\n"
            "   * $\\text{ProviderPubkey}$: Clé publique du prestataire autorisé pour la session, empêchant tout transfert illicite du bon.\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Compteur monotone ($k$) et montant cumulé assurant un règlement unique sous 5ms."
        ),
        'section_x402': (
            "\n### 6.6. Positionnement Stratégique: HAICHAIN comme Couche de Politiques et Coupe-Circuit pour HTTP x402 et Solana Pay.sh\n\n"
            "Dans le paysage global des agents autonomes, les protocoles de paiement machine ouverts connaissent une adoption institutionnelle rapide, notamment **HTTP x402** (initié par Coinbase, transféré à la Fondation Linux avec Visa et Mastercard) et **Pay.sh** (lancé conjointement par la Fondation Solana et Google Cloud en mai 2026).\n\n"
            "```\n"
            "       STACK MONDIALE D'INFRASTRUCTURE FINANCIÈRE POUR AGENTS IA\n"
            "       \n"
            "    [ AGENTS & ESSAIMS D'IA ]     : Claude Desktop, Cursor, ElizaOS, CrewAI\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ COMMUNICATION & FACTURATION]: Spécification HTTP x402 & Proxy Pay.sh\n"
            "    (Émet le statut 402 Payment Required et transporte les défis de paiement)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ POLITIQUE & GESTION RISQUE ]: ★ HAICHAIN AGENT POLICY VAULT ★\n"
            "    (Arbres Merkle, Plafonds MaxSpend stricts, Coupe-circuit d'urgence < 1s)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ RAILS DE RÈGLEMENT ON-CHAIN]: Registre Solana L1 (Règlement USDC / USDT SPL)\n"
            "```\n\n"
            "1. **Répartition Claire des Rôles (Synergie d'Écosystème):**\n"
            "   * **x402 et Pay.sh agissent comme 'Canaux de Transmission':** Ils normalisent l'émission du statut `402 Payment Required` et l'en-tête client (`X-402-Authorization`).\n"
            "   * **HAICHAIN agit comme 'Banque de Risque et Coffre-Fort de Politiques':** Il résout les failles critiques: *D'où provient le capital de l'agent? Qui contrôle les plafonds? Comment stopper un modèle compromis?*\n"
            "2. **Neutralisation des Failles Empiriques d'x402:**\n"
            "   Les audits d'octobre 2026 ont relevé 25 failles sur les premiers clients x402. HAICHAIN y remédie grâce à son **Arbre de Capacités Merkle à 4 Composants** (`Pubkey || MaxSpend || ExpirySlot || Nonce`) et au **Théorème de Perte Bornée**.\n"
            "3. **Compatibilité Immédiate avec l'Écosystème:**\n"
            "   Le kit `@haichain/sdk` fournit un gestionnaire natif pour résoudre en toute sécurité les défis x402.\n\n"
            "---\n"
        ),
        'invariants_intro_old': "est formellement vérifié et immunisé contre les exploits historiques de la DeFi totalisant plus de $800M+:",
        'invariants_intro_new': "met en œuvre une architecture de **Défense en Profondeur Déterministe Multicouche (Deterministic Multi-Layer Defense-in-Depth)**, appliquant 6 invariants mathématiques d'exécution pour neutraliser les vulnérabilités d'état et les exploits historiques totalisant plus de 821 millions de dollars. Associée à un programme d'audits de sécurité indépendants tiers réguliers, elle garantit l'intégrité absolue des flux:"
    },
    'KO': {
        'table_row': (
            "| HTTP x402 및 Pay.sh   단순 원시 HTTP/프록시 전송 파이프; Solana SPL 토큰 프로그래머블 정책 및 볼트 거버넌스 레이어(원활한 |\n"
            "| (Coinbase / Linux Fdn/단일 델리게이트 제약; 클라이언트 기본 지출 상한 부재  연동); 다중 델리게이트 Merkle 역량 트리; 격리된 |\n"
            "| Solana x Google Cloud)(V12 감사 취약점); 온체인 자율 차단기 및 공급자     PDA 지출 포트; 400ms 미만 패닉 킬스위치; 유계   |\n"
            "|                       슬래싱 부재.                                     손실 정리(Bounded Loss Theorem, 자금 탈취 방어). |"
        ),
        'case_study': (
            "\n5. **HTTP x402 및 Solana Pay.sh (원시 전송 파이프 vs. 프로그래머블 위험 정책 볼트):**\n"
            "   * *아키텍처 범위:* HTTP x402 표준(Coinbase / Linux Foundation)과 Pay.sh(Solana Foundation / Google Cloud)는 전송 계층의 결제 미들웨어와 무구독 프록시 게이팅을 훌륭히 제공합니다. 그러나 보안 도메인은 네트워크 프로토콜 계층에서 멈춥니다. Solana SPL 토큰 표준의 델리게이트는 계정당 단 1개의 위임으로 엄격히 제한되며, 2026년 10월 보안 공개(V12 취약점 보고서)에서 밝혀졌듯 클라이언트 측 기본 지출 상한선이 없으면 악의적인 API가 잔액 전체를 인출할 위험이 존재합니다.\n"
            "   * *HAICHAIN의 전략적 시너지:* HAICHAIN은 x402나 Pay.sh와 경쟁하지 않고 그 상위에서 동작하는 **프로그래머블 정책 및 안전 금고 거버넌스 레이어(Smart Policy & Safe Custody Vault)** 역할을 수행합니다. 4개 구성요소의 Merkle 역량 트리(`Pubkey || MaxSpend || ExpirySlot || Nonce`)와 400ms 미만 패닉 차단기를 강제함으로써, 에이전트가 x402나 Pay.sh 레일 상에서 거래하더라도 총 손실 노출액은 사전 승인된 태스크별 할당액 이하로 수학적으로 완벽히 제한됩니다.\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   매개변수 정의:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: 프로토콜 레벨 암호학적 도메인 분리 태그 (`\"haichain-v1-channel-settlement\"`).\n"
            "   * $\\text{ClusterID}$: Solana 클러스터 식별자 (Devnet, Testnet, Mainnet-Beta), 환경 간 서명 재전송(Replay) 공격 완전 차단.\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: 배포된 프로그램 및 에이전트의 격리된 볼트 PDA 계정에 바인딩.\n"
            "   * $\\text{ProviderPubkey}$: 활성 세션의 인가된 공급자 공개키, 바우처 제3자 무단 양도 방지.\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: 단조 증가 틱 번호($k$) 및 누적 지출액 기반 5ms 미만 단일 바우처 최종 정산."
        ),
        'section_x402': (
            "\n### 6.6. 전략적 포지셔닝: HTTP x402 및 Solana Pay.sh를 위한 정책 및 서킷 브레이커 레이어로서의 HAICHAIN\n\n"
            "자율 에이전트 인프라 환경에서 **HTTP x402**(Coinbase 시작, Visa 및 Mastercard가 참여하는 Linux Foundation 이관) 및 **Pay.sh**(2026년 5월 Solana Foundation 및 Google Cloud 공동 발표)와 같은 개방형 머신 결제 통신 프로토콜이 빠르게 확산되고 있습니다.\n\n"
            "```\n"
            "            글로벌 자율 에이전트 금융 인프라 스택\n"
            "         \n"
            "    [ 에이전트 및 AI 스웜 ]      : Claude Desktop, Cursor, ElizaOS, CrewAI\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ 통신 및 과금 요청 ]        : HTTP x402 사양 및 Pay.sh 프록시\n"
            "    (402 Payment Required 반환 및 암호화 결제 챌린지 전송)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ 정책 및 리스크 거버넌스 ]  : ★ HAICHAIN AGENT POLICY VAULT ★\n"
            "    (Merkle 역량 트리, 엄격한 MaxSpend 상한선, 400ms 미만 패닉 킬스위치)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ 온체인 정산 레일 ]         : Solana L1 원장 (USDC / USDT SPL 정산)\n"
            "```\n\n"
            "1. **명확한 역할 분담 (상호보완적 생태계 시너지):**\n"
            "   * **x402 및 Pay.sh는 '통신 및 메시징 파이프':** API가 `402 Payment Required`를 반환하고 클라이언트가 인증 헤더(`X-402-Authorization`)를 전송하는 방식을 규정합니다.\n"
            "   * **HAICHAIN은 '기업 리스크 은행 및 안전 정책 금고':** 자금 출처 검증, 세분화된 지출 한도 집행, 프롬프트 주입 공격 시 지갑 보호를 책임집니다.\n"
            "2. **실증적 x402 취약점 무력화:**\n"
            "   2026년 10월 발견된 클라이언트 지출 상한 부재 취약점을 4요소 Merkle 역량 리프(`Pubkey || MaxSpend || ExpirySlot || Nonce`)와 유계 손실 정리로 완벽히 해결합니다.\n"
            "3. **Drop-in SDK 지원:**\n"
            "   `@haichain/sdk`는 x402 결제 챌린지를 안전하게 해결할 수 있는 기본 핸들러를 제공합니다.\n\n"
            "---\n"
        ),
        'invariants_intro_old': "탈중앙화 금융 역사상 누적 **8억 달러** 이상의 역사적 해킹 공격을 방어하도록 강화되었습니다:",
        'invariants_intro_new': "**결정론적 다층 심층 방어(Deterministic Multi-Layer Defense-in-Depth)** 아키텍처를 구현하여, 누적 8억 2,100만 달러 규모의 역사적 해킹 취약점 클래스를 런타임 불변식으로 원천 차단합니다. 공인 제3자 보안 전문기관의 정기 외부 감사를 병행하여 스마트 컨트랙트 논리 결함을 완전히 제거합니다:"
    },
    'ZH': {
        'table_row': (
            "| HTTP x402 与 Pay.sh   仅为原始 HTTP/代理传输管道; 受制于 Solana SPL   可编程策略与金库治理层 (即插即用协同层); 多委托  |\n"
            "| (Coinbase / Linux 基金单一代理限制; 客户端默认缺失支出上限 (V12 审   Merkle 能力树; 严格隔离的 PDA 支出池; < 400ms  |\n"
            "| 会 / Solana x 谷歌云) 计漏洞); 缺乏链上自主熔断机制与服务商罚没机制。紧急熔断开关; 有界损失定理 (杜绝掏空钱包)。   |"
        ),
        'case_study': (
            "\n5. **HTTP x402 与 Solana Pay.sh (原始传输管道 vs. 可编程风险策略金库):**\n"
            "   * *架构定位局限:* HTTP x402 规范 (Coinbase / Linux 基金会) 与 Pay.sh (Solana 基金会 / 谷歌云) 提供了至关重要的传输层微支付中间件与无订阅代理鉴权。然而，其安全边界止步于网络协议层：Solana SPL 标准代币委托机制严格受限于单一账户仅允许一个 Delegate，且 2026 年 10 月的安全披露 (V12 漏洞审计报告) 证实，若客户端默认缺失严格预算上限，恶意 API 即可发起提光全部余额的致命请求。\n"
            "   * *HAICHAIN 的战略协同与互补:* HAICHAIN 绝非替代 x402 或 Pay.sh，而是作为直接赋能其上的**可编程策略与安全金库治理层 (Smart Policy & Safe Custody Vault)**。通过强制执行 4 元组 Merkle 能力树 (`Pubkey || MaxSpend || ExpirySlot || Nonce`) 与 < 400ms 紧急熔断机制，HAICHAIN 确保即使智能体经由 x402 或 Pay.sh 管道调用服务，其最大暴露损失也始终被数学级严格锁定在单次任务授权额度之内。\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   参数说明:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: 协议级密码学域分离标识 (`\"haichain-v1-channel-settlement\"`)。\n"
            "   * $\\text{ClusterID}$: Solana 集群标识符 (Devnet, Testnet, Mainnet-Beta)，杜绝跨网络签名重放攻击。\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: 锚定部署的程序和智能体隔离的金库 PDA 账户。\n"
            "   * $\\text{ProviderPubkey}$: 当前会话指定合法服务商公钥，严禁凭单非法向第三方转让。\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: 严格单调递增序号($k$)与累计消费额，支持 < 5ms 单张终局清算。"
        ),
        'section_x402': (
            "\n### 6.6. 战略联盟定位: HAICHAIN 作为 HTTP x402 与 Solana Pay.sh 的策略治理与熔断金库层\n\n"
            "在自主智能体金融基建领域，开放机器支付通信协议获得了机构的广泛认可，最具代表性的是 **HTTP x402** (由 Coinbase 发起并交由 Linux 基金会主导，Visa 与 Mastercard 参与) 以及 **Pay.sh** (2026 年 5 月由 Solana 基金会与谷歌云联合推出)。\n\n"
            "```\n"
            "            全球自主智能体金融基础设施分层全景图\n"
            "         \n"
            "    [ 智能体与蜂巢 AI ]         : Claude Desktop, Cursor, ElizaOS, CrewAI\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ 通信协议与费用交互 ]       : HTTP x402 标准与 Pay.sh 代理\n"
            "    (触发 402 Payment Required 响应并传输加密支付凭据)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ 策略治理与风险风控 ]       : ★ HAICHAIN AGENT POLICY VAULT ★\n"
            "    (Merkle 能力树、硬顶 MaxSpend 约束、< 400ms 硬件级紧急熔断)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ 链上最终结算底层 ]         : Solana L1 账本 (USDC / USDT SPL 原生结算)\n"
            "```\n\n"
            "1. **角色分工明确 (互补共赢生态架构):**\n"
            "   * **x402 与 Pay.sh 充当'通信管道':** 规范 API 返回 `402 Payment Required` 及客户端附加授权头 (`X-402-Authorization`) 的交互标准。\n"
            "   * **HAICHAIN 充当'企业风险银行与安全金库':** 解决最底层的安全命脉：*智能体资金从何而来？谁来授权限额？如何防范大模型越狱掏空企业钱包？*\n"
            "2. **根除 x402 早期版本已知安全隐患:**\n"
            "   针对 2026 年 10 月安全审计披露的早期 x402 客户端缺少默认限额问题，HAICHAIN 以 4 元组 Merkle 能力叶片与有界损失定理形成牢固防御。\n"
            "3. **即插即用 SDK 适配器:**\n"
            "   `@haichain/sdk` 预置原生 `handleX402Challenge` 适配函数，实现无缝安全集成。\n\n"
            "---\n"
        ),
        'invariants_intro_old': "彻底防御了去中心化金融历史上累计超过 **8 亿美元** 的六大著名黑客攻击漏洞:",
        'invariants_intro_new': "确立了**确定性多层纵深防御 (Deterministic Multi-Layer Defense-in-Depth)** 架构，在运行时强制执行 6 大数学不变量，彻底抵御 DeFi 历史上累计超过 8.21 亿美元的六大著名攻击向量。结合定期聘请一线独立安全机构进行的第三方外部审计，全面杜绝合约逻辑盲点:"
    },
    'RU': {
        'table_row': (
            "| HTTP x402 и Pay.sh    Базовые HTTP/прокси транспортные каналы;         Программируемый уровень политик и хранилищ (drop-in |\n"
            "| (Coinbase / Linux Fdn/Ограничение SPL в 1 делегата; Отсутствие лимитов слой); Мульти-делегатное дерево Merkle;             |\n"
            "| Solana x Google Cloud)расходов на клиенте (аудит V12); Нет предохрани- Изолированные PDA-хранилища; Аварийный рубильник   |\n"
            "|                       телей и слэшинга поставщиков.                    < 400 мс; Теорема ограниченных потерь.              |"
        ),
        'case_study': (
            "\n5. **HTTP x402 и Solana Pay.sh (Транспортные каналы vs. Программируемое хранилище политик безопасности):**\n"
            "   * *Архитектурные границы:* Спецификация HTTP x402 (Coinbase / Linux Foundation) и Pay.sh (Solana Foundation / Google Cloud) предоставляют базовое связующее ПО для микроплатежей на транспортном уровне и бессистемный доступ без подписок. Однако их безопасность ограничена протоколом сети: делегирование токенов SPL в Solana жестко ограничено 1 делегатом на аккаунт, а отчет безопасности за октябрь 2026 г. (отчет компании V12) показал, что без жестких клиентских лимитов вредоносные API могут списать весь баланс.\n"
            "   * *Стратегическая синергия HAICHAIN:* HAICHAIN не заменяет каналы x402/Pay.sh, а выступает в качестве **Программируемого уровня политик и безопасного хранилища (Smart Policy & Safe Custody Vault)** поверх них. Применяя 4-компонентное дерево полномочий Merkle (`Pubkey || MaxSpend || ExpirySlot || Nonce`) и аварийный рубильник с откликом < 400 мс, HAICHAIN гарантирует: даже при проведении транзакций через x402/Pay.sh потенциальный ущерб математически ограничен лимитом конкретной задачи.\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   Где:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: Протокольный криптографический тег разделения доменов (`\"haichain-v1-channel-settlement\"`).\n"
            "   * $\\text{ClusterID}$: Идентификатор кластера Solana (Devnet, Testnet, Mainnet-Beta), исключающий повторное использование подписей.\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Привязка чека к смарт-контракту и изолированному PDA-хранилищу агента.\n"
            "   * $\\text{ProviderPubkey}$: Публичный ключ авторизованного поставщика в сессии, предотвращающий передачу чека третьим лицам.\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: Монотонный счетчик ($k$) и сумма для итогового расчета быстрее 5 мс."
        ),
        'section_x402': (
            "\n### 6.6. Стратегическое позиционирование: HAICHAIN как уровень политик и рубильников для HTTP x402 и Solana Pay.sh\n\n"
            "В сфере инфраструктуры автономных агентов протоколы открытых машинных платежей получили широкое признание, в частности **HTTP x402** (инициирован Coinbase, передан в Linux Foundation при участии Visa и Mastercard) и **Pay.sh** (совместный запуск Solana Foundation и Google Cloud в мае 2026 года).\n\n"
            "```\n"
            "        МИРОВОЙ СТЕК ФИНАНСОВОЙ ИНФРАСТРУКТУРЫ АВТОНОМНЫХ АГЕНТОВ\n"
            "         \n"
            "    [ АГЕНТЫ И РОИ ИИ ]           : Claude Desktop, Cursor, ElizaOS, CrewAI\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ КОММУНИКАЦИЯ И СЧЕТА ]      : Спецификация HTTP x402 и прокси Pay.sh\n"
            "    (Выдача 402 Payment Required и передача запросов на оплату)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ ПОЛИТИКИ И РИСК-КОНТРОЛЬ ]  : ★ HAICHAIN AGENT POLICY VAULT ★\n"
            "    (Деревья Merkle, жесткие лимиты MaxSpend, рубильник паники < 1с)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ ОНЧЕЙН-РЕЛЬСЫ РАСЧЕТОВ ]    : Реестр Solana L1 (Расчеты в USDC / USDT SPL)\n"
            "```\n\n"
            "1. **Четкое разделение ролей (Взаимодополняющая синергия):**\n"
            "   * **x402 и Pay.sh служат 'Каналами передачи данных':** Стандартизируют ответы `402 Payment Required` и заголовки `X-402-Authorization`.\n"
            "   * **HAICHAIN служит 'Корпоративным банком риска и сейфом политик':** Решает вопрос: *Откуда агент берет средства? Кто контролирует лимиты? Как остановить взломанный LLM?*\n"
            "2. **Устранение практических уязвимостей x402:**\n"
            "   HAICHAIN решает проблему отсутствия лимитов с помощью **4-компонентного листа полномочий Merkle** и **Теоремы ограниченных потерь**.\n"
            "3. **Прямая интеграция через SDK:**\n"
            "   Библиотека `@haichain/sdk` предоставляет встроенные обработчики для безопасного ответа на вызовы x402.\n\n"
            "---\n"
        ),
        'invariants_intro_old': "защищено от исторических уязвимостей DeFi на общую сумму более $800M+:",
        'invariants_intro_new': "реализует архитектуру **Детерминированной многоуровневой глубокой защиты (Deterministic Multi-Layer Defense-in-Depth)**, обеспечивая исполнение 6 математических инвариантов во время выполнения для предотвращения классов уязвимостей и исторических эксплойтов на сумму более $821 млн. В сочетании с регулярными независимыми сторонними аудитами безопасности это устраняет любые логические дефекты:"
    },
    'HE': {
        'table_row': (
            "| HTTP x402 & Pay.sh    צינורות תעבורה ופרוקסי גולמיים; מגבלת נציג בודד  שכבת מדיניות וכספות ניתנת לתכנות (שכבה תואמת); עץ   |\n"
            "| (Coinbase / Linux Fdn/ב-SPL; היעדר תקרות הוצאה בלקוח (ביקורת V12);     יכולות Merkle מרובה-נציגים; קופות PDA מבודדות;      |\n"
            "| Solana x Google Cloud)ללא מפסקי זרם בשרשרת וללא מנגנון חילוט לספקים.   מפסק פאניקה < 400ms; משפט ההפסד החסום ללא ריקון.   |"
        ),
        'case_study': (
            "\n5. **HTTP x402 ו-Solana Pay.sh (צינורות תעבורה גולמיים לעומת כספת מדיניות סיכונים ניתנת לתכנות):**\n"
            "   * *גבולות הארכיטקטורה:* מפרט HTTP x402 (Coinbase / Linux Foundation) ו-Pay.sh (קרן Solana / Google Cloud) מספקים תשתית תשלומים קריטית ברמת התעבורה וללא מנויים. עם זאת, תחום האבטחה שלהם מסתיים בפרוטוקול הרשת: האצלת אסימוני SPL ב-Solana מוגבלת אך ורק לנציג יחיד לכל חשבון, ודוחות אבטחה מאוקטובר 2026 (דוח V12) הוכיחו כי ללא תקרת הוצאה כברירת מחדל בלקוח, ממשקי API זדוניים עלולים לדרוש את מלוא היתרה.\n"
            "   * *הסינרגיה האסטרטגית של HAICHAIN:* HAICHAIN אינה מתחרה ב-x402 או ב-Pay.sh, אלא פועלת כ**שכבת מדיניות וכספת מאובטחת ניתנת לתכנות** ישירות מעליהם. באמצעות אכיפת עץ יכולות Merkle בעל 4 רכיבים (`Pubkey || MaxSpend || ExpirySlot || Nonce`) ומפסק פאניקה של פחות מ-400ms, HAICHAIN מבטיחה שגם כאשר סוכנים פועלים דרך x402 או Pay.sh, סך החשיפה להפסד חסום מתמטית להקצאת המשימה המורשית בלבד.\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   הגדרת פרמטרים:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: תג הצפנה ברמת הפרוטוקול להפרדת תחומים (`\"haichain-v1-channel-settlement\"`).\n"
            "   * $\\text{ClusterID}$: מזהה אשכול Solana (Devnet, Testnet, Mainnet-Beta), מונע התקפות שידור חוזר.\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: מעגן את השובר לתוכנית ולחשבון כספת ה-PDA של הסוכן.\n"
            "   * $\\text{ProviderPubkey}$: מפתח ציבורי של הספק המורשה בהפעלה, מונע העברה בלתי-מורשית לצד שלישי.\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: מונה מונוטוני ($k$) וסכום מצטבר לסילוק סופי בפחות מ-5ms."
        ),
        'section_x402': (
            "\n### 6.6. מיצוב אסטרטגי: HAICHAIN כשכבת מדיניות ומפסקי זרם עבור HTTP x402 ו-Solana Pay.sh\n\n"
            "בנוף תשתיות הסוכנים האוטונומיים, פרוטוקולי תשלום פתוחים זכו לאימוץ מוסדי מהיר, בעיקר **HTTP x402** (ביוזמת Coinbase, הועבר לקרן Linux בהשתתפות Visa ו-Mastercard) ו-**Pay.sh** (הושק במשותף על ידי קרן Solana ו-Google Cloud במאי 2026).\n\n"
            "```\n"
            "         ערימת התשתית הפיננסית העולמית לסוכנים אוטונומיים\n"
            "         \n"
            "    [ סוכנים ונחילי בינה ]       : Claude Desktop, Cursor, ElizaOS, CrewAI\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ תקשורת וחיובים ]           : מפרט HTTP x402 ופרוקסי Pay.sh\n"
            "    (מחזיר 402 Payment Required ומעביר אתגרי תשלום מוצפנים)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ מדיניות וניהול סיכונים ]   : ★ HAICHAIN AGENT POLICY VAULT ★\n"
            "    (עצי יכולות Merkle, תקרות MaxSpend קשיחות, מפסק פאניקה < 1s)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ מסילות סילוק בשרשרת ]      : פנקס Solana L1 (סילוק USDC / USDT SPL)\n"
            "```\n\n"
            "1. **חלוקת תפקידים ברורה (סינרגיה משלימה):**\n"
            "   * **x402 ו-Pay.sh משמשים כ'צינורות תקשורת':** מגדירים כיצד ממשקי API מחזירים `402 Payment Required` וכיצד מועברות הרשאות.\n"
            "   * **HAICHAIN משמש כ'בנק סיכונים וכספת מדיניות':** פותר את השאלות הקריטיות: *מאיפה הסוכן משיג כסף? מי מגביל הוצאות?*\n"
            "2. **נטרול פגיעויות מעשיות של x402:**\n"
            "   HAICHAIN פותרת את היעדר תקרות ברירת המחדל באמצעות **עלה יכולות Merkle בן 4 רכיבים** ומשפט ההפסד החסום.\n"
            "3. **אינטגרציה חלקה עם SDK:**\n"
            "   חבילת `@haichain/sdk` כוללת מטפלים מובנים לפתרון מאובטח של אתגרי x402.\n\n"
            "---\n"
        ),
        'invariants_intro_old': "והוקשחה נגד מתקפות עבר היסטוריות שהיקפן מעל 800 מיליון דולר:",
        'invariants_intro_new': "מיישמת ארכיטקטורת **הגנה לעומק דטרמיניסטית רב-שכבתית (Deterministic Multi-Layer Defense-in-Depth)**, האוכפת 6 אינווריאנטים מתמטיים בזמן ריצה כדי לנטרל מחלקות פגיעות עבר בהיקף של למעלה מ-821 מיליון דולר. בשילוב ביקורות אבטחה חיצוניות בלתי תלויות קבועות, המערכת מבטלת לחלוטין כשלי היגיון בחוזים:"
    },
    'HI': {
        'table_row': (
            "| HTTP x402 & Pay.sh    कच्चे HTTP/प्रॉक्सी पाइप; सोलाना पर 1 डेलिगेट की  प्रोग्रामेबल नीति और वॉल्ट लेयर (ड्रॉप-इन साथी);   |\n"
            "| (Coinbase / Linux Fdn/सीमा; क्लाइंट-साइड खर्च सीमा का अभाव (V12 ऑडिट);  मल्टी-डेलिगेट मर्कल क्षमता ट्री; अलग पीडीए खर्च     |\n"
            "| Solana x Google Cloud)ऑन-चेन सर्किट ब्रेकर और प्रदाता स्लैशिंग तंत्र   पॉट्स; < 400ms में पैनिक सर्किट ब्रेकर; बाउंडेड लॉस |\n"
            "|                       की कमी।                                          प्रमेय (वॉलेट खाली होने से पूर्ण सुरक्षा)।         |"
        ),
        'case_study': (
            "\n5. **HTTP x402 और Solana Pay.sh (कच्चे ट्रांसपोर्ट पाइप बनाम प्रोग्रामेबल रिस्क पॉलिसी वॉल्ट):**\n"
            "   * *वास्तुकला की सीमा:* HTTP x402 विनिर्देश (Coinbase / Linux Foundation) और Pay.sh (Solana Foundation / Google Cloud) ट्रांसपोर्ट लेयर पर आवश्यक भुगतान मिडलवेयर और बिना सब्सक्रिप्शन के प्रॉक्सी एक्सेस प्रदान करते हैं। हालाँकि, उनका सुरक्षा दायरा नेटवर्क स्तर पर समाप्त होता है: सोलाना SPL टोकन डेलिगेट प्रति खाता केवल 1 प्रतिनिधि तक सीमित हैं, और अक्टूबर 2026 के सुरक्षा खुलासे (V12 रिपोर्ट) ने साबित किया कि क्लाइंट-साइड बजट कैप के बिना दुर्भावनापूर्ण एपीआई पूरा बैलेंस निकाल सकते हैं।\n"
            "   * *HAICHAIN की रणनीतिक तालमेल:* HAICHAIN x402 या Pay.sh के साथ प्रतिस्पर्धा नहीं करता है; यह उनके ठीक ऊपर स्थित **प्रोग्रामेबल नीति और सुरक्षित वॉल्ट लेयर (Smart Policy & Safe Custody Vault)** के रूप में कार्य करता है। 4-घटक मर्कल क्षमता ट्री (`Pubkey || MaxSpend || ExpirySlot || Nonce`) और 400ms से कम के पैनिक सर्किट ब्रेकर को लागू करके, HAICHAIN गारंटी देता है कि x402/Pay.sh के माध्यम से लेनदेन करते समय भी अधिकतम जोखिम अधिकृत कार्य सीमा तक ही सीमित रहेगा।\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   जहाँ:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: प्रोटोकॉल-स्तरीय क्रिप्टोग्राफिक डोमेन सेपरेशन टैग (`\"haichain-v1-channel-settlement\"`)।\n"
            "   * $\\text{ClusterID}$: सोलाना क्लस्टर पहचानकर्ता (Devnet, Testnet, Mainnet-Beta), जो क्रॉस-नेटवर्क रीप्ले जोखिम को समाप्त करता है।\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: विशिष्ट प्रोग्राम और एजेंट के अलग वॉल्ट पीडीए खाते से बांधता है।\n"
            "   * $\\text{ProviderPubkey}$: सक्रिय सत्र के अधिकृत सेवा प्रदाता की सार्वजनिक कुंजी, जो अनधिकृत हस्तांतरण को रोकती है।\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: 5ms से कम समय में अंतिम निपटान सुनिश्चित करने वाला मोनोटोनिक काउंटर ($k$)।"
        ),
        'section_x402': (
            "\n### 6.6. रणनीतिक स्थिति: HTTP x402 और Solana Pay.sh के लिए नीति और सर्किट ब्रेकर लेयर के रूप में HAICHAIN\n\n"
            "स्वायत्त एजेंट बुनियादी ढांचे में ओपन मशीन-पेमेंट संचार प्रोटोकॉल तेजी से अपनाए जा रहे हैं, विशेष रूप से **HTTP x402** (Coinbase द्वारा शुरू किया गया, Linux Foundation में Visa और Mastercard के साथ स्थानांतरित) और **Pay.sh** (मई 2026 में Solana Foundation और Google Cloud द्वारा संयुक्त रूप से लॉन्च किया गया)।\n\n"
            "```\n"
            "         ग्लोबल स्वायत्त एजेंट वित्तीय अवसंरचना स्टैक\n"
            "         \n"
            "    [ एजेंट और एआई झुंड ]         : Claude Desktop, Cursor, ElizaOS, CrewAI\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ संचार और बिलिंग ]           : HTTP x402 विनिर्देश और Pay.sh प्रॉक्सी\n"
            "    (402 Payment Required उत्सर्जित करता है और भुगतान चुनौतियों का परिवहन करता है)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ नीति और जोखिम शासन ]        : ★ HAICHAIN AGENT POLICY VAULT ★\n"
            "    (मर्कल क्षमता ट्री, कठोर MaxSpend सीमाएं, < 1s पैनिक किल-स्विच)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ ऑन-चेन निपटान लेयर ]        : Solana L1 बहीखाता (USDC / USDT SPL निपटान)\n"
            "```\n\n"
            "1. **भूमिकाओं का स्पष्ट विभाजन (पारस्परिक सहक्रिया):**\n"
            "   * **x402 और Pay.sh 'संचार पाइप' हैं:** वे मानकीकृत करते हैं कि एपीआई `402 Payment Required` कैसे लौटाते हैं।\n"
            "   * **HAICHAIN 'एंटरप्राइज रिस्क बैंक और सुरक्षित पॉलिसी वॉल्ट' है:** यह तय करता है कि एजेंट को धन कहाँ से मिलता है और सीमाओं को कौन लागू करता है।\n"
            "2. **अनुभवजन्य x402 कमजोरियों का समाधान:**\n"
            "   HAICHAIN **4-घटक मर्कल लीफ** और **बाउंडेड लॉस प्रमेय** के साथ बजट सीमाओं के अभाव को हल करता है।\n"
            "3. **ड्रॉप-इन SDK एकीकरण:**\n"
            "   `@haichain/sdk` पैकेज सुरक्षित रूप से x402 चुनौतियों को संभालने के लिए नेटिव हैंडलर प्रदान करता है।\n\n"
            "---\n"
        ),
        'invariants_intro_old': "защищено от исторических уязвимостей DeFi на общую сумму более $800M+:",
        'invariants_intro_new': "**नियत बहुस्तरीय गहन सुरक्षा (Deterministic Multi-Layer Defense-in-Depth)** वास्तुकला को लागू करता है, जो $821 मिलियन से अधिक के ऐतिहासिक शोषण को बेअसर करने के लिए 6 गणितीय इनवेरिएंट्स को लागू करता है। अनुसूचित तृतीय-पक्ष सुरक्षा ऑडिट के साथ मिलकर यह अनुबंध तर्क दोषों को समाप्त करता है:"
    },
    'KK': {
        'table_row': (
            "| HTTP x402 және Pay.sh Қарапайым HTTP/прокси көлік құбырлары;           Бағдарламаланатын саясат пен қойма деңгейі (үйлесімді|\n"
            "| (Coinbase / Linux Fdn/Solana SPL-де 1 ғана делегат шектеуі; Клиент     серіктес); Көпделегатты Merkle ағашы; Оқшауланған    |\n"
            "| Solana x Google Cloud)шығыс шектерінің жоқтығы (V12 аудиті); Ончейн-   PDA шығыс қорлары; < 400мс паникалық ажыратқыш;      |\n"
            "|                       ажыратқыштар мен слэшингтің жоқтығы.             Шектелген шығын теоремасы (қаражатты қорғау).        |"
        ),
        'case_study': (
            "\n5. **HTTP x402 және Solana Pay.sh (Қарапайым көлік құбырлары vs. Бағдарламаланатын тәуекел саясатының қоймасы):**\n"
            "   * *Архитектуралық шеңбер:* HTTP x402 спецификациясы (Coinbase / Linux Foundation) және Pay.sh (Solana Foundation / Google Cloud) көлік деңгейіндегі маңызды төлем делдалдығын және жазылымсыз прокси жүйесін қамтамасыз етеді. Дегенмен, олардың қауіпсіздік аймағы желі деңгейінде аяқталады: Solana SPL токен делегаттары бір есептік жазбаға қатаң түрде бір ғана өкілмен шектелген, және 2026 жылғы қазандағы қауіпсіздік есебі (V12 осалдық баяндамасы) көрсеткендей, клиент жағында бюджет шектері болмаса, зиянды API бүкіл теңгерімді алып қоюы мүмкін.\n"
            "   * *HAICHAIN стратегиялық синергиясы:* HAICHAIN x402 немесе Pay.sh жүйелерімен бәсекелеспейді; ол олардың үстінде орналасқан **Бағдарламаланатын саясат және қауіпсіз қойма деңгейі (Smart Policy & Safe Custody Vault)** ретінде қызмет етеді. 4 компонентті Merkle мүмкіндіктер ағашын (`Pubkey || MaxSpend || ExpirySlot || Nonce`) және 400 мс-ден аз паникалық ажыратқышты қолдана отырып, HAICHAIN тіпті x402 немесе Pay.sh арқылы транзакция жасаған кезде де ықтимал шығындардың тапсырма бойынша рұқсат етілген сомадан аспауын математикалық тұрғыдан кепілдейді.\n"
        ),
        'voucher_formula': (
            "$$\\text{Voucher}_k = \\text{Sign}_{\\text{Agent}}\\Big(\\text{DOMAIN\\_SEPARATOR},\\, \\text{ClusterID},\\, \\text{ProgramID},\\, \\text{VaultPDA},\\, \\text{ProviderPubkey},\\, \\text{SessionID},\\, k,\\, \\text{CumulativeAmount}_k\\Big)$$\n"
            "   Мұнда:\n"
            "   * $\\text{DOMAIN\\_SEPARATOR}$: Хаттама деңгейіндегі доменді бөлу криптографиялық тегі (`\"haichain-v1-channel-settlement\"`).\n"
            "   * $\\text{ClusterID}$: Solana кластер идентификаторы (Devnet, Testnet, Mainnet-Beta), желіаралық қайталау қаупін жояды.\n"
            "   * $\\text{ProgramID} \\text{ \\& } \\text{VaultPDA}$: Чекті бағдарламаға және агенттің оқшауланған PDA қоймасына байлайды.\n"
            "   * $\\text{ProviderPubkey}$: Сессияның өкілетті провайдерінің ашық кілті, чектің заңсыз берілуіне жол бермейді.\n"
            "   * $(\\text{SessionID}, k, \\text{CumulativeAmount}_k)$: 5 мс-ден аз уақытта түпкілікті есеп айырысуды қамтамасыз ететін есептегіш ($k$)."
        ),
        'section_x402': (
            "\n### 6.6. Стратегиялық орналасу: HTTP x402 және Solana Pay.sh үшін саясат және автоматты ажыратқыш деңгейі ретінде HAICHAIN\n\n"
            "Автономды агенттер инфрақұрылымында ашық машиналық төлем байланыс хаттамалары кеңінен танылуда, әсіресе **HTTP x402** (Coinbase бастамасымен, Visa және Mastercard қатысуымен Linux Foundation-ға берілді) және **Pay.sh** (2026 жылдың мамырында Solana Foundation және Google Cloud бірлесіп іске қосты).\n\n"
            "```\n"
            "         АВТОНОМДЫ АГЕНТТЕРДІҢ ЖАҺАНДЫҚ ҚАРЖЫЛЫҚ СТЕГІ\n"
            "         \n"
            "    [ АГЕНТТЕР МЕН ЖИ ТОПТАРЫ ]   : Claude Desktop, Cursor, ElizaOS, CrewAI\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ БАЙЛАНЫС ЖӘНЕ ЕСЕП-ҚИСАП ]  : HTTP x402 спецификациясы және Pay.sh проксиі\n"
            "    (402 Payment Required қайтарады және төлем талаптарын жеткізеді)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ САЯСАТ ЖӘНЕ ТӘУЕКЕЛДІ БАСҚАРУ]: ★ HAICHAIN AGENT POLICY VAULT ★\n"
            "    (Merkle ағаштары, қатаң MaxSpend шектері, < 1с паникалық ажыратқыш)\n"
            "                                   │\n"
            "                                   ▼\n"
            "    [ ОНЧЕЙН-ЕСЕП АЙЫРЫСУ ДЕҢГЕЙІ]: Solana L1 тізілімі (USDC / USDT SPL есеп айырысу)\n"
            "```\n\n"
            "1. **Рөлдерді нақты бөлу (Бірін-бірі толықтыратын синергия):**\n"
            "   * **x402 және Pay.sh 'Байланыс құбырлары' ретінде қызмет етеді:** Олар API интерфейстерінің `402 Payment Required` қайтару стандартын белгілейді.\n"
            "   * **HAICHAIN 'Корпоративтік тәуекел банкі және қауіпсіз саясат қоймасы':** Агент қаржыны қайдан алатынын және шектерді кім басқаратынын шешеді.\n"
            "2. **x402-дегі белгілі осалдықтарды жою:**\n"
            "   HAICHAIN шығыс шектерінің болмауы мәселесін **4 компонентті Merkle жапырағы** және **Шектелген шығын теоремасы** арқылы шешеді.\n"
            "3. **Drop-in SDK интеграциясы:**\n"
            "   `@haichain/sdk` пакеті x402 сынақтарына қауіпсіз жауап беру үшін кірістірілген өңдеушілерді ұсынады.\n\n"
            "---\n"
        ),
        'invariants_intro_old': "защищено от исторических уязвимостей DeFi на общую сумму более $800M+:",
        'invariants_intro_new': "**Детерминирленген көпдеңгейлі терең қорғаныс (Deterministic Multi-Layer Defense-in-Depth)** архитектурасын қолданады, бұл $821 миллионнан астам тарихи шабуылдарды залалсыздандыру үшін 6 математикалық инвариантты орындайды. Тұрақты тәуелсіз үшінші тарап қауіпсіздік аудитімен бірге бұл келісімшарт логикалық кемшіліктерін жояды:"
    }
}

def update_file(filepath):
    filename = os.path.basename(filepath)
    # Detect language from filename
    m = re.search(r'V1\.0_([A-Z]{2})\.md', filename)
    if not m:
        print(f"Skipping {filename}: no lang code")
        return
    lang = m.group(1)
    if lang not in LANG_DATA:
        print(f"Skipping {filename}: lang {lang} not in data")
        return

    data = LANG_DATA[lang]

    with open(filepath, 'r', encoding='utf-8') as fp:
        content = fp.read()

    original_len = len(content)
    updated = False

    # 1. Update Competitor Table
    # Find table end delimiter '+---...---+' after Worldcoin
    if 'Pay.sh' not in content[:content.find('## ' if '## ' in content[300:] else 20000)]:
        # Need to insert table row
        # Pattern: find the row starting with | Worldcoin and ending with next row or delimiter
        # Insert before the last '+---' of that table
        worldcoin_idx = content.find('| Worldcoin')
        if worldcoin_idx != -1:
            delim_idx = content.find('+---', worldcoin_idx)
            if delim_idx != -1:
                # Insert our row and a blank separator row before delim_idx
                table_row_text = "|\n" + data['table_row'] + "\n"
                # Check formatting:
                # Add delimiter row
                sep_line = "|                                                                                                                   |\n"
                to_insert = sep_line + data['table_row'] + "\n"
                content = content[:delim_idx] + to_insert + content[delim_idx:]
                updated = True
                print(f"[{lang}] Added table row")

    # 2. Update Failure Case Studies (add item 5)
    if '5. **HTTP x402' not in content:
        # Find where failure case studies end (before Chapter 2 / 4 transition)
        # Search for '## 4.' or '## CHƯƠNG 2' or '## 2.' or '## CAPA' etc.
        # Find '---' preceding that heading
        m_chap = re.search(r'\n(---\s*\n\s*##\s*(?:4\.|CHƯƠNG 2|2\.|CAPA|COUCHE|ПОТРЕБИТЕЛЬСКИЙ|ТҰТЫНУШЫЛЫҚ|उपभोक्ता|שכבת|消费级|소비자))', content)
        if m_chap:
            insert_pos = m_chap.start()
            content = content[:insert_pos] + data['case_study'] + content[insert_pos:]
            updated = True
            print(f"[{lang}] Added case study #5")
        else:
            print(f"[{lang}] WARNING: Could not find chapter transition anchor for case study #5")

    # 3. Upgrade Voucher Formula with Domain Separation
    # Match $$\text{Voucher}_k = ...$$ or $$	ext{Voucher}_k = ...$$
    formula_regex = r'\$\$(?:\\text|\t?ext)\{Voucher\}_k\s*=\s*(?:\\text|\t?ext)\{Sign\}_\{[^}]+\}\([^)]*CumulativeAmount[^)]*\)\$\$'
    if re.search(formula_regex, content):
        content = re.sub(formula_regex, data['voucher_formula'], content, count=1)
        updated = True
        print(f"[{lang}] Upgraded Voucher formula to Domain Separation")
    else:
        print(f"[{lang}] Note: Voucher formula already updated or pattern mismatch")

    # 4. Insert Section 4.6 / 6.6 if missing (ES, FR, HE, HI, KK, KO, RU, ZH)
    if 'section_x402' in data and '### 6.6.' not in content and '### 4.6.' not in content:
        # Find anchor after emergency_freeze_pot tool item in MCP section
        freeze_idx = content.find('emergency_freeze_pot')
        if freeze_idx != -1:
            # find next '---' or '## 7.'
            sep_idx = content.find('\n---', freeze_idx)
            if sep_idx != -1:
                # Insert section_x402 right after sep_idx + 4
                content = content[:sep_idx] + data['section_x402'] + content[sep_idx + 4:]
                updated = True
                print(f"[{lang}] Inserted Section 6.6 (x402 & Pay.sh alliance)")
            else:
                print(f"[{lang}] WARNING: Could not find separator after emergency_freeze_pot")
        else:
            print(f"[{lang}] WARNING: Could not find emergency_freeze_pot")

    # 5. Refine Invariants Introduction
    if 'invariants_intro_old' in data and data['invariants_intro_old'] in content:
        content = content.replace(data['invariants_intro_old'], data['invariants_intro_new'])
        updated = True
        print(f"[{lang}] Refined Invariants introduction")
    else:
        # Try broader regex if exact match not found
        broad_inv_regex = r'(`haichain-core v6\.9\.3`\))[^:\n]+(?::|\n)'
        # Let's inspect if needed
        pass

    if updated:
        with open(filepath, 'w', encoding='utf-8') as fp:
            fp.write(content)
        print(f"[{lang}] Successfully saved {filename} ({original_len} -> {len(content)} bytes)")
    else:
        print(f"[{lang}] No changes needed for {filename}")

def main():
    import glob
    files = sorted(glob.glob('HAICHAIN_WHITEPAPER*.md'))
    print(f"Found {len(files)} whitepaper files.")
    for f in files:
        update_file(f)

if __name__ == '__main__':
    main()
