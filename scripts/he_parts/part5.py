# -*- coding: utf-8 -*-

def get_content():
    return """## 5. ליבת הסליקה בשרשרת: מבצר חסינות גרעינית (SOLANA v6.9.3)

ליבת החוזים החכמים (`haichain-core v6.9.3`) עברה אימות פורמלי והוקשחה נגד מתקפות עבר היסטוריות שהיקפן המצטבר עלה על 800,000,000 דולר ברחבי עולם הפיננסים המבוזרים (DeFi):

```
+---------------------------------------------------------------------------------+
|               HAICHAIN v6.9.3 SIX INVARIANTS EXPLOIT DEFENSE MATRIX             |
+---------------------------------------------------------------------------------+
| 1. WORMHOLE DEFENSE ($320M FIX):                                                |
|   - Hardcoded Sysvar Instructions Pubkey: Sysvar1nstruction5111111111111111111 |
|   - דחיית כתובות sysvar מזויפות המועברות דרך חשבונות הקשר שרירותיים.             |
|                                                                                 |
| 2. NOMAD BRIDGE DEFENSE ($190M FIX):                                            |
|   - Non-Zero Root Invariant: require!(composite_root != [0u8; 32])            |
|   - מניעת פגיעויות המאפשרות ביצוע עסקאות כנגד שורשי מרקל לא מאותחלים.          |
|                                                                                 |
| 3. ELIZAOS PROMPT INJECTION DEFENSE:                                            |
|   - 4-Tuple Bound Capability Leaf: Hash(Pubkey || MaxSpend || Expiry || Nonce) |
|   - איסור מוחלט על סוכנים מורעלים להפנות כספים לארנקי תוקפים.                   |
|                                                                                 |
| 4. EULER FINANCE DEFENSE ($197M FIX):                                           |
|   - Strict ATA Balance Reload: require!(actual_ata_balance >= spend_amount)    |
|   - מניעת סטיות הנהלת חשבונות פנימיות ושגיאות שערי חליפין מבוססות תרומות.      |
|                                                                                 |
| 5. MANGO MARKETS DEFENSE ($114M FLASH LOAN FIX):                                |
|   - Multi-Slot Quarantine: require!(slot >= last_deposit_slot + 2)             |
|   - מניעת מניפולציות הפקדה-ומיד-ריקון של הלוואות בזק (Flash Loan) באותו בלוק.    |
|                                                                                 |
| 6. TETHER USDT FREEZE DEFENSE:                                                  |
|   - Segregated Vault ATAs: Each user vault maintains an isolated SPL ATA.     |
|   - אפס הדבקה צולבת אם ארנקי צדדים שלישיים עומדים בפני הקפאה רגולטורית.        |
+---------------------------------------------------------------------------------+
```

### 5.1. מקביליות Sealevel וחשבונות ATA מונעי-התנגשות
כדי למנוע תחרות על משאבי מצב תחת עומסי כתיבה בתדר גבוה:
* הפרוטוקול מקצה **32 חשבונות ATA מפוצלים לקליטה** עבור ספקי שירות מרכזיים:
  $$\text{PartitionIndex} = \text{Blake3}(\text{Nonce}) \pmod{32}$$
* מבנה זה מאפשר למנוע הביצוע המקבילי Sealevel של Solana לתזמן עסקאות תשלום על פני 32 ליבות מעבד פיזיות בו-זמנית, ללא עצירות סריאליזציה בצינור הביצוע.

### 5.2. שידור הבזק רב-מסילתי והגנת MEV ברמת האפליקציה בשיטת Commit-Reveal
הסתמכות בלעדית על רשתות ממסרי חבילות חיצוניות (כגון Jito) יוצרת נקודות כשל בודדות, צווארי בקבוק של שיהוי אזורי ופגיעות בזמן זינוקי מכרזי טיפים. HAICHAIN מהנדסת **מנוע שידור הבזק רב-מסילתי** בשילוב **אינווריאנט Commit-Reveal ברמת האפליקציה** כדי להבטיח ביצוע דטרמיניסטי וחסינות מתמטית מפני ארביטראז' של כריית ערך מקסימלי (MEV):

```
            HAICHAIN MULTI-RAIL FLASH BROADCAST & MEV DEFENSE PIPELINE
            
   [ High-Frequency Autonomous Agent Transaction / Reasoning Batch ]
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
  [ Rail 1: Jito Private ]  [ Rail 2: Direct TPU ]   [ Rail 3: SWQoS Priority ]
  ├── Bypasses public gossip├── Direct QUIC UDP to   ├── Stake-weighted QoS
  ├── Tip floor target: 75th│   current & next 4     │   via bonded validator RPCs
  └── Zero public mempool   │   leader validators    └── Guaranteed bandwidth
                            └── Sub-5ms raw ingress      under 99% load
                                  │
                                  ▼
             [ Dual-State On-Chain Execution Invariant ]
             ├── Slot N:   Commitment Hash Ingestion (Blind Lock)
             └── Slot N+1: Ephemeral Key Release & Value Settlement
```

#### 1. פרוטוקול הפצה רב-מסילתי (Multi-Rail Dissemination Protocol):
* **מסילה 1 (Jito Private Bundle):** עוקפת את בריכת הזיכרון (Mempool) הציבורית לחלוטין. טיפים מכוילים לאחוזון ה-75 להבטחת הכללה מיידית.
* **מסילה 2 (TPU ישיר באמצעות QUIC):** שידור ישיר של מנות UDP ל-Leader הנוכחי ול-4 ה-Leaders הבאים בתור.
* **מסילה 3 (SWQoS מבוסס סטייקינג):** איכות שירות מובטחת באמצעות צמתי RPC בעלי סטייק גבוה, המבטיחים רוחב פס גם בתנאי עומס רשת של 99%.

#### 2. אינווריאנט נעילת גיבוב Commit-Reveal:
* בבלוק הראשון ($Slot_N$), הסוכן שולח התחייבות עיוורת:
  $$\mathcal{H}_{\text{commit}} = \text{BLAKE3}\left(\text{Tx}_{\text{payload}} \parallel \text{salt} \parallel k_{\text{eph}}\right)$$
* בבלוק הבא ($Slot_{N+1}$), נחשף המפתח הארעי $k_{\text{eph}}$. מנוע הליבה מאמת את ההתאמה ומבצע את העסקה באופן חסין-חזיתית (Anti-Frontrunning).

#### 3. אינווריאנט קנסות דינמי מותאם תנודתיות:
אם ולידטור או ממסר מעכבים את שלב החשיפה כדי לנצל שינויי מחיר, מופעל קנס חיתוך מיידי:
$$\mathcal{S}_{\text{slash}} = \mathcal{B}_{\text{stake}} \cdot \min\left(1.0, \; \gamma \cdot \frac{|\Delta P|}{P_0} + \alpha \cdot \Delta t\right)$$

### 5.3. שרשור בלוקי עסקאות ניתנים לתכנות (PTB Chaining) על גבי SVM
מערכת HAICHAIN משתמשת בהרכבה אטומית של הוראות מרובות בטרנזקציה בודדת:
1. אימות חתימת מפתח ביומטרי (Passkey).
2. אימות עלה מרקל של סוכן המשנה (Merkle Leaf Check).
3. בדיקת תקרת תקציב וטעינה מחדש של יתרת ה-ATA.
4. העברת תשלום תת-סנטי לנאמנות הספק.
5. שחרור תוצר ההסקה וסגירת החשבון הארעי.

כל ההוראות מתבצעות כיחידה אחת בלתי-ניתנת לחלוקה באותו מחזור מחשב.

### 5.4. מבנה חוזה Anchor Rust וחסינות מוחלטת מכניסה מחדש
החוזה נכתב ב-Rust וכולל בדיקות בטיחות מחמירות:

```rust
#[account]
pub struct ReasoningEscrowVault {
    pub principal_authority: Pubkey,   // הריבון האנושי
    pub delegate_agent: Pubkey,        // סוכן המכונה המורשה
    pub settlement_asset: Pubkey,      // כתובת חוזה ה-USDT SPL
    pub locked_collateral: u64,        // סכום הבטוחה הנעול
    pub cumulative_settled: u64,       // סך הכל סכום שסולק
    pub max_budget_cap: u64,           // תקרת תקציב עליונה בלתי-עבירה
    pub emergency_timelock: i64,       // מועד שחרור חירום
    pub circuit_breaker_active: bool,  // סטטוס מפסק ביטחון
    pub bump: u8,                      // קבוע PDA
}
```

### 5.7. כלב שמירה אוטונומי של בינת המכונה (Sentinel Watchdog תת-10ms)
אלגוריתם ה-Sentinel רץ על גבי צמתי קצה ייעודיים, דוגם את זרימת העסקאות ומזהה דפוסי מתקפה או הזרקת פקודות זדוניות בתוך פחות מ-10 מילישניות. זיהוי אנומליה מפעיל מיד הקפאה רכה ברמת החוזה, מבלי להשבית את שאר סוכני הרשת.
"""
