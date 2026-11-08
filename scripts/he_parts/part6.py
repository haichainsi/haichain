# -*- coding: utf-8 -*-

def get_content():
    return """## 6. נאמנות חישובי הסקה של בינה מלאכותית ועצי יכולות היררכיים (BIP-32 SWARMS)

```
              FRONTIER AI REASONING ESCROW & SWARM DELEGATION PIPELINE
              
   [ OpenAI o1/o3 / Claude 3.5 Sonnet Extended Thinking ]
                    │
                    ▼
   [ Elastic Reasoning Escrow ]
   ├── Base Collateral: $C_{base}$
   ├── Dynamic Buffer: $\\Delta_{buf} = \\min(20\\% \\times C_{base}, Cap_{max})$
   └── Cryptographic Commitment: $H(Tokens \\parallel Nonce)$
                    │
                    ▼
   [ Hierarchical Capability Trees (BIP-32 Swarms) ]
   ├── Master Agent (Depth 0): Root Authority
   ├── Sub-Agent 1 (Depth 1): Scraper Bot ($0.05 limit, BROWSE_ONLY)
   └── Sub-Agent 2 (Depth 2): Code Synthesizer ($0.02 limit, CODE_ONLY)
                    │
                    ▼
   [ Atomic 2PC WASM Verification Sandbox ]
   ├── Prepare: Collateral locked in escrow
   ├── Validate: Tool output schema checked in WASM (< 0.5ms)
   └── Commit/Rollback: Valid -> Settle | Error/Timeout -> 100% Refund
```

### 6.1. נאמנות חישוב הסקה אלסטית (Elastic Reasoning Compute Escrow)
מודלי הסקה מהחזית מייצרים מספר משתנה של טוקני חשיבה פנימיים שאינם ניתנים לחישוב דטרמיניסטי מראש. HAICHAIN מנסחת באופן פורמלי את **משוואת נאמנות ההסקה האלסטית**:
$$Escrow_{total} = C_{base} + \\min(\\alpha \\cdot C_{base}, \\Delta_{max})$$
כאשר $\\alpha = 0.20$ (מאגר ביטחון דינמי של 20%) ו-$\\Delta_{max}$ מהווה את התקרה הקשיחה. עם סיום החישוב, הספק מחזיר הוכחת אישור (Attestation Proof) של כמות הטוקנים המדויקת שנצרכה. עודפי הון ממאגר הביטחון מוחזרים מיידית לכספת המשתמש באותה פעימת עסקה.

#### מודל שעון כפול אסינכרוני וסליקה מהירה דו-צדדית (< 80ms)
כדי למנוע תקיעות אטומיות כאשר Solana חווה עיכובי סלוטים או גודש רשת חולף, ליבת נאמנות ההסקה מפרידה בין לוגיקת מיקרו-ההפעלות לבין פעימות הבלוק הגלובליות באמצעות **מודל שעון כפול אסינכרוני**:

```
             ASYNCHRONOUS DUAL-CLOCK & FAST-PATH PIPELINE
             
    [ Bilateral Multi-Agent Micro-Reasoning Session (A <-> B) ]
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼                                               ▼
[ Fast-Path Single-Writer Protocol ]           [ Asynchronous Dual-Clock ]
├── 2-of-2 Signed Capability Receipts          ├── Session Timeout = Delta_T
├── Bypasses global block consensus            │   (e.g., Exactly +60 seconds)
└── Latency: SUB-80 MILLISECONDS               └── Immune to Solana slot jitter
```

1. **אינווריאנט זמן דלתא יחסי ($\\Delta t$):** זמני פקיעת נאמנות דו-צדדית מוגדרים בשניות פיזיות יחסיות ($\\Delta t = 60\\text{s}$) המעוגנות בחותמות זמן של Unix החתומות קריפטוגרפית, ולא במספרי סלוטים אבסולוטיים של Solana (`require!(current_unix_ts <= init_unix_ts + delta_t)`). אם ייצור הסלוטים מתעכב, חוזי הסקה פעילים נותרים עקביים מתמטית מבלי להקפיא את כספי הסוכנים.
2. **ערוץ נתיב מהיר של כותב יחיד (Single-Writer Fast-Path):** כאשר מיקרו-עסקאות מתרחשות אך ורק בין שני סוכנים מאומתים, הסליקה מתבצעת ישירות ללא צורך בהמתנה לקונצנזוס בלוק מלא, בשיהוי של **פחות מ-80 מילישניות**.

#### אבטחה לעומק של בינה מלאכותית חסויה: מובלעות הטרוגניות ובוררות ZK
סביבות הרצה של סוכנים מאובטחות באמצעות שילוב מובלעות חומרה (TEEs) של יצרנים בלתי תלויים. במקרה של חוסר הסכמה על תקינות תוצר המודל, מופעל מנגנון בוררות באפס ידיעה (Zero-Knowledge Arbitration) שבו הצרכן מוכיח סטייה מתמטית מבלי לחשוף את הפרומפט המקורי.

### 6.2. עצי יכולות היררכיים (BIP-32 Swarms)
כאשר סוכן ראשי מאציל משימות לסוכני משנה, המערכת מיישמת עצי יכולות היררכיים (Hierarchical Capability Trees):
* **עומק 0 (סוכן ראשי):** שליטה מלאה המעוגנת בחתימה ביומטרית של המשתמש.
* **עומק 1 (סוכן משנה לסריקה):** תקציב מוגבל ל-$0.05, הרשאות קריאה בלבד (`BROWSE_ONLY`).
* **עומק 2 (סוכן משנה לסינתזת קוד):** תקציב מוגבל ל-$0.02, הרשאות ביצוע קוד מבודדות (`CODE_ONLY`).

סוכן ברמה נמוכה אינו יכול לפעול מחוץ לענף שהוגדר עבורו.

### 6.3. דחיסת מצב ללא דמי שכירות (Concurrent Merkle Trees) ומחזור חיים ארעי של PDA
1. **דחיסת מצב באמצעות עצי מרקל מקביליים (cAgents):** פרטי הסוכן מאוחסנים כעלה בעץ מרקל דחוס ב-Solana, בעלות אפסית של פחות מ-$0.000005.
2. **מחזור חיים ארעי עם 100% החזר דמי שכירות:** עם השלמת המשימה, חשבון ה-PDA נסגר באמצעות פקודת `close = user_authority`, ו-100% מדמי השכירות (Lamports) מוחזרים במלואם לחשבון המשתמש הראשי.

### 6.4. תקרת תקציב דטרמיניסטית ותבניות כוונות בלחיצה אחת
משתמשים מגדירים יעדים בשפה טבעית, והמערכת ממירה אותם לתבניות כוונות חתומות קריפטוגרפית הכוללות תקרת תקציב קשיחה.

### ערכת פיתוח מהירה ב-5 שורות קוד (5-Line Implementation):
```typescript
import { HaiChainClient, EscrowAgent } from "@haichain/sdk";

const hai = new HaiChainClient({ cluster: "mainnet-beta" });
const agent = await hai.createEphemeralAgent({ maxBudgetUSDT: 5.00 });
const session = await agent.openReasoningChannel("provider.haichain.si");
const result = await session.executeTask({ prompt: "Analyze Q3 Earnings" });
await session.settleAndClose(); // סגירה אטומית והחזר מלא של עודפי הבטוחות
```

### 6.5. אינטגרציה טבעית של שרת Anthropic Model Context Protocol (MCP)
```json
{
  "mcpServers": {
    "haichain-settlement": {
      "command": "npx",
      "args": ["-y", "@haichain/mcp-server"],
      "env": {
        "HAICHAIN_NETWORK": "mainnet-beta",
        "HAICHAIN_PROGRAM_ID": "DK4QA3q5b2XmHskPvdjJ3gZ2iHk86s4n7VsmfPspump",
        "HAICHAIN_SETTLEMENT_ASSET": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"
      }
    }
  }
}
```
"""
