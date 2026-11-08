import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Translations dictionary for the 6 core tables across all 10 languages
# Format: tables[lang][table_key] = markdown_table_string

tables = {
    'ZH': {
        'cross_paradigm': """| 核心评估指标 | Web2 传统支付通道 (Stripe / Visa) | EVM L1/L2 公链 (Base / Arbitrum) | HAICHAIN 极速结算协议 (v1.1) |
| :--- | :--- | :--- | :--- |
| **最低实操费用下限** | $0.30 美元单笔固定底费 | $0.02 - $0.50 美元 Gas 突增 | $0.000001 美元 (1,000:1 对冲轧差) |
| **结算确认到账延迟** | 2 - 5 个传统银行工作日 | 2,000 - 15,000 毫秒拥堵等待 | < 400ms 线速终局 (τ ≤ 12s 链上安全上限) |
| **提示词注入攻击风险** | 信用卡账户被恶意脚本彻底刷爆 | 主钱包 EOA 私钥泄露导致资金归零 | 数学级绝对为 0 (PDA 隔离支出金库) |
| **用户准入入金门槛** | 冗长 KYC、银行表单、耗时 3 天 | 12 个助记词、自备 Gas、跨链桥摩擦 | 生物识别 Passkey FaceID (< 60s 无感入金) |
| **欺诈回滚 / 紧急熔断** | 拒付争议 (Chargeback 60-90 天) | 链上不可逆损失，黑客提款无法追回 | 一键紧急熔断 (< 400ms 冻结并提回冷钱包) |""",
        'saas': """| 经济学评估维度 | 传统按人头订阅 SaaS (Web2 陷阱) | HAICHAIN 真实效用微结算协议 (v1.1) |
| :--- | :--- | :--- |
| **计费底层哲学** | 付费买断访问权 (无论使用与否均扣固定月费) | 按单次执行精确结算 (细分至纳美分级别) |
| **未消耗算力配额** | 月底 100% 彻底作废清零 (企业纯沉没成本) | 100% 完整保留在用户自主掌握的 PDA 金库中 |
| **基础计费单元** | 粗糙的人类员工席位 ($20 - $50/人/月) | 真实消耗的算力与 Token ($0.0002/次调用) |
| **人机交互模式** | 人类员工手动点击网页图形界面 (UI) | 智能体集群经由 HTTP x402 自主机对机调用 |
| **资金风险边界** | 企业主信用卡明文绑定在第三方 SaaS 后台 | 物理隔离的 PDA 支出金库 (单任务 $5.00 硬顶) |
| **真实综合月支出** | $150.00 - $300.00 / 员工 / 月 | $3.40 / 月 (通过 BYOK 机制真实降本 97.7%) |""",
        'competitor': """| 平台 / 架构范式 | 核心架构致命盲区 | HAICHAIN SI 突破性解决方案 |
| :--- | :--- | :--- |
| **Coinbase AgentKit & ElizaOS (ai16z)** | 裸露 EOA 私钥; 间接提示词注入导致主钱包被黑客提空; 缺少链上速率限制与硬件级紧急断电开关。 | Merkle 能力树 (CapLeaf 4元组约束); 独立隔离 PDA 金库; 一键紧急熔断 (< 400ms 线速响应，τ ≤ 12s 链上安全保障)。 |
| **Bittensor (TAO)** | 12 秒区块确认延迟 (无法满足毫秒级微支付); Yuma 共识存在串谋刷分与权重抄袭漏洞; 缺乏人类基准导致自噬退化 (MAD)。 | 50ms 快速 BFT 对冲流水线; USDT/USDC 真实稳定币现金流; 实际智能证明 (PoAI) 引入人类活体智慧注入。 |
| **ASI Alliance (Fetch.ai / SingNet)** | Cosmos/EVM 智能合约跨程序调用 (CPI) 成本极高; 多秒级 BFT 延迟; 缺少原生微支付指令; 智能体与人类法律主体脱钩。 | 虚拟机底层原生集成 OP_402_PAY 操作码 (> 100,000 TPS, 零 CPI 开销); 绑定生物识别 Passkey 的 Soulbound DID (符合 EU AI Act)。 |
| **Virtuals Protocol (Base Layer 2)** | Base 单线程 EVM 状态写入冲突与锁争用; 以太坊 L1 Blob 费用波动剧烈 ($0.01 - $0.50); 专注 Meme 投机而非企业效用基建。 | Solana Sealevel 32 分区并发 ATA 架构; 链下对称对冲压缩率达 99.999% (771 字节紧凑报文); 纯稳定币结算无币价波动风险。 |
| **Stripe / Tempo MPP & Web2 传统管道** | $0.30 + 2.9% 固定高费率底线 (对 $0.0002 级 API 产生 150,000% 溢价); T+2 至 T+5 结算滞后; 存在恶意拒付欺诈风险。 | 纯净微效用计费 ($0.000001 轧差净额); 亚秒级密码学终局确认; 独立智能合约托管彻底杜绝拒付违约风险。 |
| **Worldcoin (Tools for Humanity)** | 仅靠专用虹膜扫描仪 (The Orb) 发放被动 UBI 代币; 缺乏智能体运行时执行环境; 无法对智能体授权约束; 未形成人机共生闭环。 | 拥抱开放硬件生物识别 (WebAuthn/ZK-PoH)，直接嵌入反向微任务经济闭环，将人类认知直觉转化为受偿超智能协处理器。 |
| **HTTP x402 & Pay.sh (Solana x Google Cloud)** | 仅提供传输层 HTTP 请求头代理规范; 单一 Delegate 限制; 早期客户端缺失严格支出硬顶 (V12 漏洞); 缺少链上罚没与自动断电。 | 可编程策略与金库治理层 (完美互补共生); 多重委派 Merkle 能力树; 独立隔离 PDA 金库; 紧急电路断路器; 有界损失定理彻底杜绝资金跑路。 |""",
        'onboarding': """| 第一步: 生物识别 Passkey 硬件安全区 | 第二步: 全球多渠道无感入金 (Sandbox Demo) | 第三步: 隔离安全金库 (Safe Pot PDA) |
| :--- | :--- | :--- |
| **硬件级安全芯片保护**<br>• Apple FaceID / TouchID / TPM 2.0<br>• WebAuthn 安全隔离区硬件背书<br>• 绝不保存任何助记词与明文私钥 | **极简全球资金网关**<br>• Apple Pay / Google Pay / 信用卡<br>• 银联 / 动态二维码即时结算<br>• 1:1 锚定合规储备金 USDT | **刚性有界损失安全金库**<br>• 独立 $10.00 微额支出子账户<br>• 防盗刷智能电路自动熔断器<br>• 一键紧急断电全额提款回冷钱包 |""",
        'invariants': """| 不变量 / 防护层级 | 历史重大攻击向量与漏洞利用范式 | HAICHAIN 密码学刚性执行机制 |
| :--- | :--- | :--- |
| **1. Sysvar 指令自省 (CVE-2022-24300 防护)** | 攻击者传入伪造的 Sysvar 上下文账户欺骗验证逻辑 | 硬编码硬锁 Sysvar Instructions 账户公钥: `Sysvar1nstructions1111111111111111111111111`。 |
| **2. 非零 Merkle 根与未初始化 PDA 抵御** | 在 Merkle 根尚未初始化为全零状态时执行提款调用 | 强制执行前置断言: `require!(composite_root != [0u8; 32])`。 |
| **3. 间接提示词注入 (Prompt Injection) 免疫** | 被攻击者劫持的智能体试图将大额资金转向黑客地址 | 4 元组绑定能力叶片 (`Pubkey \|\| MaxSpend \|\| Expiry \|\| Nonce`) 限制单次任务最大额度。 |
| **4. 实时 SPL ATA 余额对账与防滑点护栏** | 内部记账漂移或基于外生 Donation 的汇率操纵攻击 | 严格重载最新链上真实代币余额: `require!(actual_ata_balance >= spend_amount)`。 |
| **5. 多槽位闪电贷流动性隔离期 (Anti-Flashloan)** | 在同一区块槽位内部借入巨资、操纵状态并迅速抽干 | 多槽位时间锁强制隔离: `require!(slot >= last_deposit_slot + 2)`。 |
| **6. Tether 关联代币账户物理级隔离** | 第三方钱包遭遇合规冻结引发跨账户连锁反应 | 每个企业金库生成完全独立的 Associated Token Account (ATA)，零交叉传染风险。 |""",
        'roadmap': """| 战略规划时间表 | 核心里程碑战略目标 | 关键工程交付成果与技术规范 |
| :--- | :--- | :--- |
| **第一阶段: 1–12 个月 (2026 Q4)** | **Solana L1 商业化深耕与企业级集成**<br>(市场全面渗透与规模化商业落地 PMF) | • Solana 主网部署加固核心程序 v6.9.3<br>• WebAuthn 生物识别 Passkey 极简入金网关集成<br>• 面向 Cursor、Claude、Antigravity 的 MCP 权威服务节点上线<br>• 72/72 核心不变量单元与集成测试套件全绿<br>• OtterSec 与 Neodyme 顶级第三方智能合约形式化安全审计 |
| **第二阶段: 12–24 个月 (2027 Q2)** | **专用高吞吐 SVM App-Rollup 扩展**<br>(生态网络爆发与去中心化中继集群) | • 自研 SVM 专用排序器 (Sequencer) 测试网正式启动<br>• 集成 Celestia / EigenDA 模块化数据可用性 (DA) 层<br>• 人机共生知识市场 (Marketplace) 与反向微任务协议全面上线<br>• 聚合承载突破 50,000+ 机器专用每秒事务数 (TPS) |
| **第三阶段: 24–36+ 个月 (2027 Q4+)** | **HAICHAIN 主权 AI 机器 L1 终局公链**<br>(去中心化超级智能 ASI 最终协调网络) | • HAI-VM 裸金属虚拟机测试网正式发布<br>• 原生硬件级 `OP_402_PAY` 操作码编译入虚拟机指令集<br>• 双层共识机制落地: 智能体工作量证明 (PoAW) + 实际智能证明 (PoAI)<br>• SPL 与原生 $HAISI 资产 1:1 双向瞬移跨链桥<br>• 实测承载突破 100,000+ 机器微结算 TPS |"""
    }
}

# Clone for other languages with proper translations
print("Table definitions compiled for transformation.")
